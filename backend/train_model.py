import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from scipy import stats

def calculate_spi(df, col='rainfall', rolling_window=3):
    """
    Calculates Standardized Precipitation Index (SPI) approximation.
    Simple method using rolling mean and Z-score (Standard Normal Distribution).
    A more rigorous SPI fits a Gamma distribution, but Z-score of log-precip is often used as a proxy.
    """
    # Replace 0 with a small epsilon to avoid log(0)
    df['log_precip'] = np.log(df[col] + 1)
    
    # Calculate rolling statistics
    df['rolling_mean'] = df['log_precip'].rolling(window=rolling_window*30, min_periods=30).mean()
    df['rolling_std'] = df['log_precip'].rolling(window=rolling_window*30, min_periods=30).std()
    
    # Calculate Z-score (SPI proxy)
    df['SPI'] = (df['log_precip'] - df['rolling_mean']) / df['rolling_std']
    
    return df

def generate_drought_label(spi):
    if np.isnan(spi): return 0 # Default to Low if unknown
    
    if spi > -0.5: return 0      # Low Risk
    elif spi > -1.0: return 1    # Moderate Risk
    elif spi > -1.5: return 2    # High Risk
    else: return 3               # Severe Risk

def simulate_ndvi(df):
    """
    Simulates NDVI based on Rainfall with a lag.
    """
    # Rolling rainfall impacts vegetation greenness
    df['rainfall_30d'] = df['rainfall'].rolling(window=30).mean()
    # Normalize rainfall to 0-1 range roughly -> NDVI 0.1-0.9
    df['ndvi'] = 0.1 + (0.8 * (df['rainfall_30d'] / df['rainfall_30d'].max()))
    # Add some noise
    df['ndvi'] += np.random.normal(0, 0.05, len(df))
    df['ndvi'] = df['ndvi'].clip(0, 1)
    return df

def train_and_save_model():
    print("Loading real data...")
    try:
        df = pd.read_csv("backend/ethiopia_climate_data.csv")
    except FileNotFoundError:
        print("Data file not found. Run fetch_real_data.py first.")
        return

    # Sort by date
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # Feature Engineering
    print("Calculating indices...")
    df = calculate_spi(df, rolling_window=3) # 3-month SPI
    df = simulate_ndvi(df)
    
    # Generate Target
    df['drought_risk'] = df['SPI'].apply(generate_drought_label)
    
    # Drop rows with NaN (early rolling window)
    df = df.dropna()
    
    features = ['rainfall', 'temperature', 'soil_moisture', 'ndvi']
    target = 'drought_risk'
    
    X = df[features]
    y = df[target]
    
    print(f"Training on {len(df)} samples...")
    print(f"Class distribution:\n{y.value_counts()}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Model...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    rf_model.fit(X_train, y_train)
    
    # Evaluate
    predictions = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    
    # Save Model
    model_filename = 'backend/drought_model.joblib'
    joblib.dump(rf_model, model_filename)
    print(f"Model saved to {model_filename}")

if __name__ == "__main__":
    train_and_save_model()
