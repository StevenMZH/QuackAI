import random
from dataclasses.manager import TaskResourceManager

def generate_scheduling_problem(
    num_blocks=5,
    num_intervals=8,
    num_tasks=10,
    num_resources=5,
    max_time_blocks=4,
    max_per_cicle=6,
    max_per_interval=2,
    tags_pool=None
):
    """
    Generates a random scheduling problem instance.

    Returns:
    - manager: TaskResourceManager filled with tasks and resources
    - dataset_input: dict representing the input (tasks, resources, constraints)
    """

    if tags_pool is None:
        tags_pool = ["A", "B", "C", "D", "E"]  # default tag set

    manager = TaskResourceManager(interval_blocks=num_blocks, cicle_intervals=num_intervals)

    dataset_input = {
        "blocks": num_blocks,
        "intervals": num_intervals,
        "tasks": [],
        "resources": []
    }

    # Generate resources
    for r_idx in range(num_resources):
        num_tags = random.randint(1, min(3, len(tags_pool)))
        resource_tags = random.sample(tags_pool, num_tags)
        max_c = random.randint(1, max_per_cicle)
        max_i = random.randint(1, max_per_interval)
        manager.add_resource(
            name=f"R{r_idx+1}",
            tags=resource_tags,
            max_per_cicle=max_c,
            min_per_cicle=0,
            max_per_interval=max_i,
            min_per_interval=0
        )
        dataset_input["resources"].append({
            "name": f"R{r_idx+1}",
            "tags": resource_tags,
            "max_per_cicle": max_c,
            "max_per_interval": max_i
        })

    # Generate tasks
    for t_idx in range(num_tasks):
        time_blocks = random.randint(1, max_time_blocks)
        # Assign compatible resources by tag
        chooseable_resources = {}
        compatible_tags = random.sample(tags_pool, random.randint(1, len(tags_pool)))
        for tag in compatible_tags:
            # list resource ids that have this tag
            resources_with_tag = [
                res_id for res_id, res in manager.resources.items() if tag in res.tags
            ]
            chooseable_resources[tag] = resources_with_tag

        max_c = random.randint(1, max_per_cicle)
        max_i = random.randint(1, max_per_interval)
        manager.add_task(
            name=f"T{t_idx+1}",
            time_blocks=time_blocks,
            chooseable_resources=chooseable_resources,
            max_per_cicle=max_c,
            min_per_cicle=0,
            max_per_interval=max_i,
            min_per_interval=0
        )
        dataset_input["tasks"].append({
            "name": f"T{t_idx+1}",
            "time_blocks": time_blocks,
            "compatible_tags": compatible_tags,
            "max_per_cicle": max_c,
            "max_per_interval": max_i
        })

    return manager, dataset_input
