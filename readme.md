# # Floe Agent Prototype

## Overview
This project demonstrates a minimal autonomous agent that simulates how an agent would use Floe’s credit layer.

The focus is on **agent decision-making** rather than direct on-chain integration.



## Tech Stack
- Python
- Simple decision engine (profit-based borrowing logic)


## Agent Behavior
The agent:
- Evaluates whether a task is worth executing
- Decides whether to borrow based on profitability
- Simulates borrowing (`instant_borrow`)
- Executes the task after borrowing


## Scenarios Tested

### Scenario 1: Profitable Task
- Task Value: 100
- Cost: 30
- Profit: 70  
- Decision: Borrow → Execute

### Scenario 2: Non-Profitable Task
- Task Value: 20
- Cost: 30
- Profit: -10  
- Decision: Skip

### Scenario 3: Edge Case
- Task Value: 80
- Cost: 80
- Profit: 0  
- Decision: Skip



