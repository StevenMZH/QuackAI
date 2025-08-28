from core.data_processing.dataclasses.manager import TaskResourceManager
from core.data_processing.dataclasses.task import Task
from core.data_processing.dataclasses.resourse import Resource

# Greddy Scheduler

def greedy_scheduler(manager: "TaskResourceManager", task_heuristic=lambda t: 0, resource_heuristic=lambda r: 0):
    """
    Greedy resource assignment algorithm with pluggable heuristics.

    Parameters:
    - manager: TaskResourceManager instance with tasks and resources
    - task_heuristic: function(task) -> priority value (lower = higher priority)
    - resource_heuristic: function(resource) -> priority value (lower = higher priority)

    Returns:
    - assignments: dict mapping task.id -> number of assigned blocks
    """

    # Sort tasks according to the heuristic
    tasks_sorted = sorted(manager.tasks.values(), key=task_heuristic)

    assignments = {}

    for task in tasks_sorted:
        remaining_blocks = task.time_blocks
        assignments[task.id] = 0

        # Iterate over the scheduling grid (blocks × intervals)
        for block_idx in range(manager.blocks):
            if remaining_blocks <= 0:
                break  # Task fully assigned

            for interval_idx in range(manager.intervals):
                if remaining_blocks <= 0:
                    break  # Task fully assigned

                # Sort resources according to the heuristic
                resources_sorted = sorted(manager.resources.values(), key=resource_heuristic)

                for res in resources_sorted:
                    # Check if the resource can be assigned
                    if manager.can_assign(task, res, block_idx, interval_idx):
                        # Assign task and resource
                        task.schedule.blocks[block_idx][interval_idx] = task
                        res.schedule.blocks[block_idx][interval_idx] = res

                        remaining_blocks -= 1
                        assignments[task.id] += 1
                        break  # Go to next cell

    return assignments


# Heuristics for Tasks

def task_most_blocks(task):
    """
    Prioritize tasks that require the MOST time blocks.
    Useful for filling big/long tasks first.
    """
    return -task.time_blocks  # higher first

def task_least_blocks(task):
    """
    Prioritize tasks that require the FEWEST time blocks.
    Useful for quickly fitting small tasks first.
    """
    return task.time_blocks  # lower first


def task_max_interval(task):
    """
    Prioritize tasks with the HIGHEST maximum allowed per interval.
    These tasks are more flexible.
    """
    return -(task.max_per_interval if task.max_per_interval is not None else 0)

def task_min_interval(task):
    """
    Prioritize tasks with the LOWEST maximum allowed per interval.
    These are more constrained and should be scheduled first.
    """
    return task.max_per_interval if task.max_per_interval is not None else float("inf")


def task_fewest_resource_options(task):
    """
    Prioritize tasks with the FEWEST available/compatible resources.
    (Tasks with less flexibility should go earlier).
    """
    return len(task.chooseable_resources)

def task_most_resource_options(task):
    """
    Prioritize tasks with the MOST available/compatible resources.
    (Useful if you want to keep flexibility high).
    """
    return -len(task.chooseable_resources)


# Heuristics for Resources

def resource_max_cycle(resource):
    """Prioritize resources with the HIGHEST cycle capacity. """
    return -(resource.max_per_cicle if resource.max_per_cicle is not None else 0)

def resource_min_cycle(resource):
    """
    Prioritize resources with the LOWEST cycle capacity.
    (Scarce resources get scheduled first).
    """
    return resource.max_per_cicle if resource.max_per_cicle is not None else float("inf")


def resource_rare_tags(resource, tag_counts):
    """
    Prioritize resources with the RAREST tags in the system.
    `tag_counts` must be a Counter of all tag frequencies.
    """
    return min(tag_counts[tag] for tag in resource.tags)

def resource_common_tags(resource, tag_counts):
    """
    Prioritize resources with the MOST COMMON tags.
    (Opposite of rare_tags).
    """
    return -min(tag_counts[tag] for tag in resource.tags)


def resource_fewest_assignments(resource):
    """
    Prioritize resources that have been assigned the LEAST so far.
    Balances workload across resources.
    """
    assigned = sum(1 for b in resource.schedule.blocks for c in b if c is not None)
    return assigned

def resource_most_assignments(resource):
    """
    Prioritize resources that have been assigned the MOST so far.
    (Might be useful if you want to 'pack' some resources).
    """
    assigned = sum(1 for b in resource.schedule.blocks for c in b if c is not None)
    return -assigned



# Backtracking Scheduler

def assign_resources_backtracking(manager: "TaskResourceManager"):
    """
    Asigna tareas y recursos usando backtracking con el manager.
    """
    tasks_list = list(manager.tasks.values())
    return _assign_recursive(manager, tasks_list, 0, 0, 0)


def _assign_recursive(manager: "TaskResourceManager", tasks_list, task_idx, block_idx, interval_idx):
    if task_idx >= len(tasks_list):
        return True

    task = tasks_list[task_idx]

    if task.time_blocks <= 0:
        return _assign_recursive(manager, tasks_list, task_idx + 1, 0, 0)

    for b in range(block_idx, manager.blocks):
        for i in range(interval_idx, manager.intervals):
            for res in manager.resources.values():
                if manager.can_assign(task, res, b, i):
                    # Asignar temporal
                    task.schedule.blocks[b][i] = task
                    res.schedule.blocks[b][i] = res
                    task.time_blocks -= 1

                    if _assign_recursive(manager, tasks_list, task_idx, b, i + 1):
                        return True

                    # Retroceder
                    task.schedule.blocks[b][i] = None
                    res.schedule.blocks[b][i] = None
                    task.time_blocks += 1

        interval_idx = 0

    return False
