import json
import os
import time
from itertools import product
from copy import deepcopy
import numpy as np

from data_processing.dataset.problem_generator import generate_scheduling_problem
from schedulers.scheduler import greedy_scheduler
from schedulers.scheduler import (
    task_most_blocks, task_least_blocks, task_max_interval, task_min_interval,
    task_most_resource_options, task_fewest_resource_options,
)
from schedulers.scheduler import (
    resource_max_cycle, resource_min_cycle, resource_common_tags,
    resource_rare_tags, resource_most_assignments, resource_fewest_assignments,
)
from schedulers.evaluator import evaluate_schedule, score_schedule


def process_problem_input(problem_input):
    """
    Converts problem input into numeric features for AI training.
    """
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
        "num_blocks": num_blocks,
        "num_intervals": num_intervals,
        "num_tasks": num_tasks,
        "num_resources": num_resources,
        "avg_task_blocks": avg_task_blocks,
        "max_task_blocks": max_task_blocks,
        "min_task_blocks": min_task_blocks,
        "avg_task_max_per_interval": avg_task_max_per_interval,
        "avg_task_max_per_cicle": avg_task_max_per_cicle,
        "avg_task_num_tags": avg_task_num_tags,
        "avg_resource_max_per_interval": avg_resource_max_per_interval,
        "avg_resource_max_per_cicle": avg_resource_max_per_cicle,
        "avg_resource_num_tags": avg_resource_num_tags
    }

    return features


def generate_dataset(
    filename="dataset_scores.json",
    num_samples=10,
    heuristics_tasks=None,
    heuristics_resources=None
):
    """
    Generates a dataset for training an AI to choose heuristics.
    Stores only the scores for each heuristic combination.
    """

    if heuristics_tasks is None:
        heuristics_tasks = {
            "most_blocks": task_most_blocks,
            "least_blocks": task_least_blocks,
            "max_interval": task_max_interval,
            "min_interval": task_min_interval,
            "fewest_resource_options": task_fewest_resource_options,
            "most_resource_options": task_most_resource_options
        }

    if heuristics_resources is None:
        heuristics_resources = {
            "max_cycle": resource_max_cycle,
            "min_cycle": resource_min_cycle,
            "fewest_assignments": resource_fewest_assignments,
            "most_assignments": resource_most_assignments
        }

    # Load or create dataset
    if os.path.exists(filename):
        with open(filename, "r") as f:
            dataset = json.load(f)
    else:
        dataset = []

    for _ in range(num_samples):
        manager, problem_input = generate_scheduling_problem()
        
        # Procesamos input a features
        processed_input = process_problem_input(problem_input)
        
        entry = {"input": processed_input, "output": {}}

        # Evaluate all combinations of heuristics
        for t_name, r_name in product(heuristics_tasks.keys(), heuristics_resources.keys()):
            t_func = heuristics_tasks[t_name]
            r_func = heuristics_resources[r_name]

            manager_copy = deepcopy(manager)

            start_time = time.time()
            greedy_scheduler(manager_copy, task_heuristic=t_func, resource_heuristic=r_func)
            exec_time = time.time() - start_time

            score = score_schedule(
                evaluate_schedule(manager_copy),
                exec_time=exec_time
            )

            entry["output"][f"{t_name}_{r_name}"] = score

        dataset.append(entry)

        # Guardar dataset incrementalmente
        with open(filename, "w") as f:
            json.dump(dataset, f, indent=4)

    return dataset
