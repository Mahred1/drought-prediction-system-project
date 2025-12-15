import React from 'react';
import './PredictionResult.css';

const PredictionResult = ({ result }) => {
    if (!result) return null;

    const getRiskColor = (level) => {
        switch (level) {
            case 'Low': return 'var(--color-low)';
            case 'Moderate': return 'var(--color-moderate)';
            case 'High': return 'var(--color-high)';
            case 'Severe': return 'var(--color-severe)';
            default: return '#ccc';
        }
    };

    const color = getRiskColor(result.drought_risk_level);

    return (
        <div className="prediction-result" style={{ borderColor: color }}>
            <h3>Prediction Result</h3>
            <div className="risk-level" style={{ color: color }}>
                {result.drought_risk_level} Risk
            </div>
            <p className="risk-message">{result.message}</p>
            <div className="risk-score">
                Score: {result.risk_score} / 3
            </div>
        </div>
    );
};

export default PredictionResult;
