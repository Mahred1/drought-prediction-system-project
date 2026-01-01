from fastapi import FastAPI

app = FastAPI(debug=True)



# Check health
@app.get('/api/health')
def check_health():
    return {"Health": "Good!"}