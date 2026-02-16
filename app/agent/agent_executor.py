import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from app.agent.tools import search_flights, search_hotels, estimate_trip_cost, generate_itinerary

class TravelAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        
        self.tools = [search_flights, search_hotels, estimate_trip_cost, generate_itinerary]
        
        
        self.agent = create_react_agent(
            model=self.llm,
            tools=self.tools,
            prompt="You are a helpful travel assistant. Use tools to provide real-time data."
        )

    async def run(self, user_input: str, chat_history: list):
        inputs = {"messages": chat_history + [("user", user_input)]}
        result = await self.agent.ainvoke(inputs)
        return result["messages"][-1].content