def borrow(task_value: float, cost: float) -> bool:
    """Evaluates whether a target execution scenario yields profitable margins.

    Args:
        task_value: The expected economic yield from a specific task.
        cost: The upfront capital debt required to trigger execution.

    Returns:
        True if the reward outweighs the capital cost, False otherwise.
    """
    return task_value > cost