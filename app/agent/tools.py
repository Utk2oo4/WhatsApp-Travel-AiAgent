import json
from langchain.tools import tool

@tool
def search_flights(destination: str, budget: float):
    """Searches for flights to a destination within a budget."""
    # Mock data logic
    flights = [
        {"id": "FL1", "price": budget * 0.4, "time": "6h", "carrier": "SkyHigh"},
        {"id": "FL2", "price": budget * 0.6, "time": "2h", "carrier": "FastJet"}
    ]
    return json.dumps(flights)

@tool
def search_hotels(destination: str, budget: float):
    """Searches for hotels in a destination based on budget."""
    hotels = [
        {"name": "Budget Inn", "price_per_night": budget * 0.1, "rating": 3.5},
        {"name": "Grand Plaza", "price_per_night": budget * 0.3, "rating": 4.8}
    ]
    return json.dumps(hotels)

@tool
def estimate_trip_cost(flight_price: float, hotel_price: float, days: int):
    """Calculates total trip cost and compares against constraints."""
    total = flight_price + (hotel_price * days)
    return json.dumps({"total_estimated_cost": total})

@tool
def generate_itinerary(destination: str, preferences: str):
    """Generates a structured day-by-day itinerary."""
    return f"Itinerary for {destination} focusing on {preferences}: Day 1: Sightseeing, Day 2: Food Tour."