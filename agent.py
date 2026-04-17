def borrow(task_value: float, cost: float) -> bool:
    """Decide whether borrowing is worth it."""
    return task_value > cost