import os
from agent import borrow
from dotenv import load_dotenv
import floe_client 

load_dotenv()

SESSION_MAX_CAP = 100.0

def run() -> None:
  """Iterates through execution targets to evaluate and process credit lines."""
  if not os.getenv("AGENT_API_KEY"):
    print("ERROR: 'AGENT_API_KEY' is missing from environment setup.\n")
    return
  
  floe_client.set_spend_limit(SESSION_MAX_CAP)
  print(f"Set session spend limit to ${SESSION_MAX_CAP} USDC.\n")

  scenarios = [
      {"task_value": 100.0, "cost": 30.0},
      {"task_value": 20.0, "cost": 30.0},
      {"task_value": 80.0, "cost": 80.0},
  ]

  print("Starting agent profile run...\n")

  for i, step in enumerate(scenarios, start=1):
    print(f"\n--- Scenario Step [{i}] ---")

    # Guardrail 1: Check baseline credit pool health
    credit_state = floe_client.get_credit_remaining()
    current_utilization = credit_state["utilizationBps"]
    print(f"Credit Utilization: {current_utilization} bps")

    if current_utilization > 8500:
      print("Utilization ceiling reached. Freezing borrow pipeline.")
      break


    # Guardrail 2: Enforce local operational caps
    if step["cost"] > SESSION_MAX_CAP:
      print(f"Skipping: Cost ${step['cost']} breaches session limit.")
      continue


    if borrow(step["task_value"], step["cost"]):
      print("Action approved: Profitable margin detected.")
      try:
        receipt = floe_client.instant_borrow(step["cost"])
        print("Tx confirmed:", receipt)
        print("Pipeline tasks resolved successfully.")
      except floe_client.FloeAPIError as err:
        print(f"Floe protocol execution aborted: {err}")
      except Exception as err:  
        print(f"Unexpected system error: {err}")
    else:
      print("Action rejected: Insufficient profit margin.")


if __name__ == "__main__":
  run()