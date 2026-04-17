import requests
import os

BASE_URL = "https://credit-api.floelabs.xyz/v1"  
API_KEY = os.getenv("YOUR_AGENT_KEY")  


def instant_borrow(amount: float) -> dict:
    """Simulated borrowing from Floe"""
    return {
        "status": "success",
        "borrowed": amount,
        "interest_rate": 0.06,
        "duration_days": 30
    }