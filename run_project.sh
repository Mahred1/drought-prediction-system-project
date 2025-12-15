#!/bin/bash

# Function to kill child processes on exit
trap 'kill $(jobs -p)' EXIT

echo "Starting Backend..."
source venv/bin/activate
uvicorn backend.main:app --reload --port 8000 &
BACKEND_PID=$!

echo "Starting Frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!

echo "Backend running on PID $BACKEND_PID"
echo "Frontend running on PID $FRONTEND_PID"

echo "Application is starting..."
wait
