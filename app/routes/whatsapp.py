from fastapi import APIRouter, Form, Response
from twilio.twiml.messaging_response import MessagingResponse
from app.agent.agent_executor import TravelAgent
from app.services.redis_service import get_chat_history

router = APIRouter()
agent = TravelAgent()

@router.post("/whatsapp")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    # 1. Get History using the phone number as Session ID
    history = get_chat_history(From)
    messages = history.messages
    
    # 2. Run Agent
    response_text = await agent.run(Body, messages)
    
    # 3. Save to Redis
    history.add_user_message(Body)
    history.add_ai_message(response_text)
    
    # 4. Twilio Response
    twiml_resp = MessagingResponse()
    twiml_resp.message(response_text)
    return Response(content=str(twiml_resp), media_type="application/xml")