import numpy as np

def process_problem_input(problem_input):
    """
    Converts problem input into numeric features for AI training.
    """
    print("plain input:")
    print(problem_input)
    
    tasks = problem_input["tasks"]
    resources = problem_input["resources"]

    # Global features
    num_blocks = problem_input["blocks"]
    num_intervals = problem_input["intervals"]
    num_tasks = len(tasks)
    num_resources = len(resources)

    # Task features
    task_blocks = [t["time_blocks"] for t in tasks]
    task_max_per_interval = [t["max_per_interval"] for t in tasks]
    task_max_per_cicle = [t["max_per_cicle"] for t in tasks]
    task_num_tags = [len(t["compatible_tags"]) for t in tasks]

    avg_task_blocks = np.mean(task_blocks)
    max_task_blocks = np.max(task_blocks)
    min_task_blocks = np.min(task_blocks)
    avg_task_max_per_interval = np.mean(task_max_per_interval)
    avg_task_max_per_cicle = np.mean(task_max_per_cicle)
    avg_task_num_tags = np.mean(task_num_tags)

    # Resource features
    res_max_per_interval = [r["max_per_interval"] for r in resources]
    res_max_per_cicle = [r["max_per_cicle"] for r in resources]
    res_num_tags = [len(r["tags"]) for r in resources]

    avg_resource_max_per_interval = np.mean(res_max_per_interval)
    avg_resource_max_per_cicle = np.mean(res_max_per_cicle)
    avg_resource_num_tags = np.mean(res_num_tags)

    features = {
        "num_blocks": int(num_blocks),
        "num_intervals": int(num_intervals),
        "num_tasks": int(num_tasks),
        "num_resources": int(num_resources),
        "avg_task_blocks": float(avg_task_blocks),
        "max_task_blocks": int(max_task_blocks),
        "min_task_blocks": int(min_task_blocks),
        "avg_task_max_per_interval": float(avg_task_max_per_interval),
        "avg_task_max_per_cicle": float(avg_task_max_per_cicle),
        "avg_task_num_tags": float(avg_task_num_tags),
        "avg_resource_max_per_interval": float(avg_resource_max_per_interval),
        "avg_resource_max_per_cicle": float(avg_resource_max_per_cicle),
        "avg_resource_num_tags": float(avg_resource_num_tags)
    }
    print("processed features:")
    print(features)
    return features