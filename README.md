# AI-Powered WhatsApp Travel Assistant

An intelligent WhatsApp bot built with Python that leverages AI agents and real-time travel APIs to provide flight, hotel, and travel information directly to users.

---

## 🚀 Features
* **AI Agent Integration:** Uses a specialized agent executor to process natural language travel queries.
* **Real-time Travel Data:** Integrated with travel APIs (like Amadeus/TripAdvisor) for live data.
* **State Management:** Uses **Redis** for efficient session and conversation handling.
* **Modular Architecture:** Clean separation between routes, schemas, services, and AI logic.

---

## 📂 Project Structure
```text
WA_BOT/
├── app/
│   ├── agent/       # AI logic (agent_executor.py, tools.py, prompts.py)
│   ├── routes/      # WhatsApp webhook and API endpoints (whatsapp.py)
│   ├── schemas/     # Pydantic models for data validation (models.py)
│   └── services/    # External integrations (redis_service.py)
├── main.py          # Application entry point
├── .env             # Environment variables (Ignored by Git)
├── .gitignore       # Git ignore rules
└── requirements.txt # Project dependencies
```

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **LLM:** Groq (Llama 3.3 70B)  
- **Agent Framework:** LangChain + LangGraph  
- **Memory:** Redis  
- **Messaging:** Twilio WhatsApp API  
- **Language:** Python  

---



## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/wa-travel-bot.git](https://github.com/YOUR_USERNAME/wa-travel-bot.git)
cd wa-travel-bot
```
### 2. Set up the Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.Run Redis

Locally:
```bash
redis-server
```

Or use Docker:
```bash
docker run -p 6379:6379 redis
```
### 5.Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 6.Expose Localhost (for Twilio)

Use ngrok:
```bash
ngrok http 8000
```

Copy the HTTPS URL and paste it into your Twilio WhatsApp webhook:
```bash
https://your-ngrok-url/whatsapp
```
## 🔄 How It Works

- User sends a WhatsApp message.
- Twilio forwards it to the FastAPI webhook.
- Chat history is retrieved from Redis.
- The Travel Agent reasons about the request.
- Tools are invoked when needed.
- Response is sent back to the user on WhatsApp.

