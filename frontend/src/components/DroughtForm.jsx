import React, { useState } from 'react';
import './DroughtForm.css';

const DroughtForm = ({ onPredict, loading }) => {
    const [formData, setFormData] = useState({
        rainfall: '',
        temperature: '',
        soil_moisture: '',
        ndvi: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onPredict(formData);
    };

    return (
        <form className="drought-form" onSubmit={handleSubmit}>
            <h2>Enter Environmental Data</h2>
            <div className="form-group">
                <label>Rainfall (mm/month)</label>
                <input
                    type="number"
                    name="rainfall"
                    value={formData.rainfall}
                    onChange={handleChange}
                    required
                    placeholder="e.g. 120"
                />
            </div>
            <div className="form-group">
                <label>Temperature (°C)</label>
                <input
                    type="number"
                    name="temperature"
                    value={formData.temperature}
                    onChange={handleChange}
                    required
                    placeholder="e.g. 25"
                />
            </div>
            <div className="form-group">
                <label>Soil Moisture (%)</label>
                <input
                    type="number"
                    name="soil_moisture"
                    value={formData.soil_moisture}
                    onChange={handleChange}
                    required
                    placeholder="e.g. 30"
                />
            </div>
            <div className="form-group">
                <label>NDVI (0.0 - 1.0)</label>
                <input
                    type="number"
                    step="0.01"
                    name="ndvi"
                    value={formData.ndvi}
                    onChange={handleChange}
                    required
                    placeholder="e.g. 0.5"
                />
            </div>
            <button type="submit" disabled={loading}>
                {loading ? 'Analyzing...' : 'Predict Drought Risk'}
            </button>
        </form>
    );
};

export default DroughtForm;
