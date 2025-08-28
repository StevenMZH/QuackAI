import json
from core.data_processing.dataclasses.manager import TaskResourceManager

def output_parser(manager: TaskResourceManager) -> dict:
    """
    Convierte el schedule de TaskResourceManager en un JSON estructurado.
    """
    blocks = [[{"tasks": [], "resources": []} for _ in range(manager.intervals)] for _ in range(manager.blocks)]

    # Tasks
    for task in manager.tasks.values():
        for block_idx, row in enumerate(task.schedule.blocks):
            for interval_idx, cell in enumerate(row):
                if cell:  # ya asignado
                    blocks[block_idx][interval_idx]["tasks"].append(task.name)

    # Resources
    for res in manager.resources.values():
        for block_idx, row in enumerate(res.schedule.blocks):
            for interval_idx, cell in enumerate(row):
                if cell:  # ya asignado
                    blocks[block_idx][interval_idx]["resources"].append(res.name)

    return {"schedule": blocks}
