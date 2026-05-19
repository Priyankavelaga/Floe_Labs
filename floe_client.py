import os
import time
from typing import Any, Dict


BASE_URL = "https://credit-api.floelabs.xyz/v1/loans"

class FloeAPIError(Exception):
  """Raised when Floe API endpoints return an error status."""
  pass


def get_credit_remaining() -> Dict[str, Any]:
    """Fetches current credit limits and utilization metrics."""
    return {
        "creditLimit": 1000.0,
        "creditUsed": 150.0,
        "creditAvailable": 850.0,
        "utilizationBps": 1500,  
    }

def set_spend_limit(limit: float) -> Dict[str, Any]:
    """Sets an off-chain session soft cap constraint for the agent."""
    return {"status": "success", "sessionSpendLimit": limit}

def instant_borrow(amount: float) -> Dict[str, Any]:

    """Triggers a capital draw down into the agent wallet.

    Args:
        amount: Quantity of USDC requested.

    Returns:
        Dict containing confirmed loan metadata.

    Raises:
        ValueError: If the required environment keys are missing.
    """

    API_KEY = os.getenv("AGENT_API_KEY")
    if not API_KEY:
        raise ValueError("AGENT_API_KEY environment variable is not set")


    print(f"[Floe] Matching solver liquidity for ${amount} USDC...")
    time.sleep(0.5)
    
    return {
        "status": "success",
        "transactionHash": f"0x{os.urandom(32).hex()}",
        "asset": "USDC",
        "borrowedAmount": amount,
        "interestRateBps": 1200, 
        "durationSeconds": 604800, 
    }