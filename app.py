from agent import borrow
from floe_client import instant_borrow
from dotenv import load_dotenv
load_dotenv()


def run():
    scenarios = [
        {"task_value": 100, "cost": 30},  
        {"task_value": 20, "cost": 30},   
        {"task_value": 80, "cost": 80},   
    ]

    print("Starting agent...\n")

    for s in scenarios:
        print("\n--- New Scenario ---")
        print(f"Task Value: {s['task_value']}, Cost: {s['cost']}")
        print(f"Profit estimate: {s['task_value'] - s['cost']}")

        if borrow(s["task_value"], s["cost"]):
            print("Decision: Borrow")

            try:
                loan = instant_borrow(s["cost"])
                print("Borrow success:", loan)

                print("Executing task...")
                print("Task completed successfully")

            except Exception as e:
                print("Error after borrowing:", str(e))

        else:
            print("Decision: Skip borrowing")

if __name__ == "__main__":
    run()