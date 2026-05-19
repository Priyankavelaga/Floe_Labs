# Floe Labs Agentic Credit Prototype

A Python prototype that simulates autonomous credit-line evaluation and capital drawdown loops using the Floe Labs developer framework. 

This repository implements a context-aware execution loop where an agent evaluates the economic viability of a task before executing transactions, while respecting protocol-enforced credit conditions and session-level safety guardrails.

## Features & Architectural Guardrails

The implementation incorporates three core layers of the Floe Labs credit architecture:

1. **State-Aware Risk Checks:** The agent queries `get_credit_remaining()` at every loop iteration to parse `utilizationBps`. If credit utilization exceeds a specified threshold (e.g., 8500 bps), the pipeline automatically freezes.
2. **Session Spend Limits:** The system calls `set_spend_limit()` during initialization to enforce a soft-cap restriction on total capital drawdown, preventing over-borrowing from recursive execution loops.
3. **Exception Handling:** Implements precise exception wrapping via `FloeAPIError` alongside catch-all blocks to simulate risk mitigation during unexpected network or execution-layer faults.

## Project Structure

```text
├── agent.py           # Core decision logic and economic margin heuristics.
├── app.py             # Main simulation engine and execution pipeline.
├── floe_client.py     # Client SDK wrapper simulating API state actions.
├── .env.example       # Configuration template for local credentials.
└── requirements.txt   # Explicit python package dependencies.


GETTING STARTED

Prerequisites:
Python 3.8 or higher 
pip (Python package installer)


Installation:
>> git clone 

Configure your environment variables:
>> python3.11 -m venv venv                    
>> source venv/bin/activate

Install Dependencies:
>> pip install requests python-dotenv

Open the `.env` file and populate it with your `AGENT_API_KEY`.

Running the agent:
>> python app.py



EXPECTED EXECUTION OUTPUT
Set session spend limit to $100.0 USDC.

Starting agent profile run...

--- Scenario Step [1] ---
Credit Utilization: 1500 bps
Action approved: Profitable margin detected.
[Floe] Matching solver liquidity for $30.0 USDC...
Tx confirmed: {'status': 'success', 'transactionHash': '0x2e...', 'asset': 'USDC', 'borrowedAmount': 30.0, 'interestRateBps': 1200, 'durationSeconds': 604800}
Pipeline tasks resolved successfully.

--- Scenario Step [2] ---
Credit Utilization: 1500 bps
Action rejected: Insufficient profit margin.

--- Scenario Step [3] ---
Credit Utilization: 1500 bps
Action rejected: Insufficient profit margin.