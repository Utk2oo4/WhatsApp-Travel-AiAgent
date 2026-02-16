from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found! Check your .env file.")

from app.routes import whatsapp

app = FastAPI(title="Autonomous Travel Agent MVP")

app.include_router(whatsapp.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)