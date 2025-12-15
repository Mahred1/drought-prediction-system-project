import { useState } from 'react'
import DroughtForm from './components/DroughtForm'
import PredictionResult from './components/PredictionResult'

function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handlePredict = async (data) => {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      // Assuming backend runs on port 8000. In production this needs config.
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error('Failed to fetch prediction')
      }

      const resultData = await response.json()
      setResult(resultData)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <header>
        <h1>Ethiopian Drought Prediction System</h1>
        <p>Enter environmental parameters to assess drought risk.</p>
      </header>

      <main>
        <DroughtForm onPredict={handlePredict} loading={loading} />

        {error && <div className="error-message">{error}</div>}

        <PredictionResult result={result} />
      </main>

      <footer>
        <p>Built for Ethiopian Context | Synthetic Model v1.0</p>
      </footer>
    </div>
  )
}

export default App
