from fastapi import FastAPI
from sqlmodel import SQLModel
from config.database_config import engine
app = FastAPI(debug=True)



# Check health
@app.get('/api/health')
def check_health():
    return {"Health": "Good!"}