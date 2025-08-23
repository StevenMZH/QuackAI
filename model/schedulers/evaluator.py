from dataclasses.manager import TaskResourceManager

def evaluate_schedule(manager: "TaskResourceManager"):
    """
    Evaluates the current schedule quality after running a scheduler.

    Returns a dict with:
    - total_tasks: number of tasks
    - fully_assigned_tasks: number of tasks fully scheduled
    - partially_assigned_tasks: number of tasks partially scheduled
    - unassigned_tasks: number of tasks with 0 assignments
    - total_requested_blocks: sum of all required blocks across tasks
    - total_assigned_blocks: sum of all assigned blocks across tasks
    - assignment_ratio: fraction of blocks successfully assigned
    - resource_usage_balance: variance of resource loads (lower = more balanced)
    """

    total_tasks = len(manager.tasks)
    fully_assigned = 0
    partially_assigned = 0
    unassigned = 0

    total_requested_blocks = 0
    total_assigned_blocks = 0

    resource_loads = []

    # Evaluate tasks
    for task in manager.tasks.values():
        requested = task.time_blocks
        assigned = sum(1 for b in task.schedule.blocks for c in b if c is not None)

        total_requested_blocks += requested
        total_assigned_blocks += assigned

        if assigned == 0:
            unassigned += 1
        elif assigned < requested:
            partially_assigned += 1
        else:
            fully_assigned += 1

    # Evaluate resource usage
    for res in manager.resources.values():
        load = sum(1 for b in res.schedule.blocks for c in b if c is not None)
        resource_loads.append(load)

    # Variance of load distribution (lower is better balance)
    if resource_loads:
        avg = sum(resource_loads) / len(resource_loads)
        variance = sum((l - avg) ** 2 for l in resource_loads) / len(resource_loads)
    else:
        variance = 0

    return {
        "total_tasks": total_tasks,
        "fully_assigned_tasks": fully_assigned,
        "partially_assigned_tasks": partially_assigned,
        "unassigned_tasks": unassigned,
        "total_requested_blocks": total_requested_blocks,
        "total_assigned_blocks": total_assigned_blocks,
        "assignment_ratio": total_assigned_blocks / total_requested_blocks if total_requested_blocks > 0 else 0,
        "resource_usage_balance": variance,
    }

def base_score_from_metrics(metrics: dict, weights=None):
    """
    Computes a score (0 to 1) from evaluation metrics only.
    """
    if weights is None:
        weights = {
            "assignment_ratio": 0.5,
            "fully_assigned_tasks_ratio": 0.3,
            "resource_balance": 0.2
        }

    total_tasks = metrics["total_tasks"]
    fully_assigned = metrics["fully_assigned_tasks"]
    assignment_ratio = metrics["assignment_ratio"]
    variance = metrics["resource_usage_balance"]

    fully_assigned_ratio = fully_assigned / total_tasks if total_tasks > 0 else 0
    balance_score = 1 / (1 + variance)  # smaller variance → mejor

    score = (
        weights["assignment_ratio"] * assignment_ratio +
        weights["fully_assigned_tasks_ratio"] * fully_assigned_ratio +
        weights["resource_balance"] * balance_score
    )

    return round(score, 4)


def score_schedule(metrics: dict, exec_time: float, weights=None, time_weight=0.2):
    """
    Combines metrics score with execution time into a single score (0..1).
    """
    base_score = base_score_from_metrics(metrics, weights)

    time_score = 1 / (1 + exec_time)

    combined_score = (1 - time_weight) * base_score + time_weight * time_score

    return round(combined_score, 4)
