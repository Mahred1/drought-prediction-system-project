import requests
import pandas as pd
import json
import os
from datetime import datetime

# Configuration
# Region: Somali Region, Ethiopia (Drought prone)
LAT = 7.0
LON = 43.0
START_DATE = "20000101"
END_DATE = "20231231"
OUTPUT_FILE = "backend/ethiopia_climate_data.csv"

def fetch_data():
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "parameters": "PRECTOTCORR,T2M,GWETROOT,GWETTOP",
        "community": "AG",
        "longitude": LON,
        "latitude": LAT,
        "start": START_DATE,
        "end": END_DATE,
        "format": "JSON"
    }

    print(f"Fetching data for coordinates ({LAT}, {LON}) from {START_DATE} to {END_DATE}...")
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract features
        properties = data['properties']['parameter']
        rainfall = properties['PRECTOTCORR']
        temp = properties['T2M']
        soil_moisture_root = properties['GWETROOT'] # Root zone soil moisture (0-1)
        soil_moisture_top = properties['GWETTOP']   # Top soil moisture (0-1)

        # Convert to DataFrame
        dates = sorted(rainfall.keys())
        rows = []
        for date_str in dates:
            # Date format YYYYMMDD
            try:
                date_obj = datetime.strptime(date_str, "%Y%m%d")
                
                # PRECTOTCORR is mm/day
                r = rainfall.get(date_str, -999)
                t = temp.get(date_str, -999)
                sm_root = soil_moisture_root.get(date_str, -999)
                sm_top = soil_moisture_top.get(date_str, -999)
                
                if -999 in (r, t, sm_root, sm_top):
                    continue
                    
                rows.append({
                    "date": date_obj,
                    "rainfall": r,
                    "temperature": t,
                    "soil_moisture": sm_root * 100, # Convert 0-1 to Percentage
                    "soil_moisture_top": sm_top * 100
                })
            except ValueError:
                continue
                
        df = pd.DataFrame(rows)
        print(f"Downloaded {len(df)} records.")
        
        # Save to CSV
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Data saved to {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_data()
