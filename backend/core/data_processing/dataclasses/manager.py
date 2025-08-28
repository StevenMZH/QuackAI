from core.data_processing.dataclasses.task import Task
from core.data_processing.dataclasses.resourse import Resource

class TaskResourceManager:
    def __init__(self, interval_blocks:int, cicle_intervals:int):
        self.intervals = cicle_intervals
        self.blocks = interval_blocks
        self.tasks = {}
        self.resources = {}
        
    def __repr__(self):
        blocks = [[{"tasks": [], "resources": []} for _ in range(self.intervals)] for _ in range(self.blocks)]

        # Tasks
        for task in self.tasks.values():
            for block_idx, row in enumerate(task.schedule.blocks):
                for interval_idx, cell in enumerate(row):
                    if cell:  # if already assigned
                        blocks[block_idx][interval_idx]["tasks"].append(task.name)

        # Resources
        for res in self.resources.values():
            for block_idx, row in enumerate(res.schedule.blocks):
                for interval_idx, cell in enumerate(row):
                    if cell:  # if already assigned
                        blocks[block_idx][interval_idx]["resources"].append(res.name)

        # str
        result = ""
        for row in blocks:  # row = block
            for cell in row:  # column = interval
                tasks_str = ",".join(cell["tasks"])
                res_str = ",".join(cell["resources"])
                if tasks_str or res_str:
                    cell_str = f"T:{tasks_str}|R:{res_str}"
                else:
                    cell_str = "None"
                result += f"{cell_str}\t"
            result += "\n"


        return result

    
    def add_task(self, name:str, time_blocks:int, chooseable_resources:dict, max_per_cicle:int=None, min_per_cicle:int=0, max_per_interval:int=None, min_per_interval:int=0):
        task = Task(name, self.blocks, self.intervals, max_per_cicle, min_per_cicle, max_per_interval, min_per_interval, time_blocks, chooseable_resources)
        self.tasks[task.id] = task
            
    def add_resource(self, name:str, tags:list[str], max_per_cicle:int=None, min_per_cicle:int=0, max_per_interval:int=None, min_per_interval:int=0):
        resource = Resource(name, self.blocks, self.intervals, max_per_cicle, min_per_cicle, max_per_interval, min_per_interval, tags)
        self.resources[resource.id] = resource
    
    def can_assign(self, task: Task, resource: Resource, block_idx: int, interval_idx: int) -> bool:
        """
        Verifica si un recurso puede asignarse a un bloque específico de un intervalo para una tarea.
        """

        # Validate tags compatibility
        task_tags = set(task.chooseable_resources.keys())
        resource_tags = set(resource.tags)
        if not task_tags.intersection(resource_tags):
            return False
        
        # Validate resource actual block
        current_block = resource.schedule.blocks[block_idx][interval_idx]
        if current_block is not None:
            return False  # resource already assigned on this block

        # Count resource assignations on the cicle
        assigned_in_cycle = sum(
            1 for b in resource.schedule.blocks for cell in b if cell is not None
        )
        if resource.max_per_cicle is not None and assigned_in_cycle >= resource.max_per_cicle:
            return False  # overpass the cicle max
        if resource.min_per_cicle is not None and assigned_in_cycle < resource.min_per_cicle:
            pass  
        
        # Count resource assignations on the block/interval
        assigned_in_block = 0
        for r in resource.schedule.blocks[block_idx]:
            if r is not None:
                assigned_in_block += 1
        if resource.max_per_interval is not None and assigned_in_block >= resource.max_per_interval:
            return False

        # Count task assignations on the block/interval
        task_assigned_in_block = 0
        for t in task.schedule.blocks[block_idx]:
            if t is not None:
                task_assigned_in_block += 1
        if task.max_per_interval is not None and task_assigned_in_block >= task.max_per_interval:
            return False

        # restrictions passed
        return True
    