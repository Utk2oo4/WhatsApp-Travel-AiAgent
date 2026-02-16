from langchain_community.chat_message_histories import RedisChatMessageHistory
import os

def get_chat_history(session_id: str):
    return RedisChatMessageHistory(
        session_id=session_id,
        url=os.getenv("REDIS_URL", "redis://localhost:6379/0")
    )