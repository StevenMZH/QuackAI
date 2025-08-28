from core.data_processing.dataclasses.scheduable import Scheduable

class Task(Scheduable):
    def __init__(self, name:str, interval_blocks:int, cicle_intervals:int, max_per_cicle:int, min_per_cicle:int, max_per_interval:int, min_per_interval:int, time_blocks:int, chooseable_resources:dict):
        super().__init__(name, interval_blocks, cicle_intervals, max_per_cicle, min_per_cicle, max_per_interval, min_per_interval)
        self.time_blocks = time_blocks
        self.chooseable_resources = chooseable_resources
        
    def __repr__(self):
        return (f"\nTask Name: {self.name}\n\n"
                f"Schedule:\n{self.schedule}\n"
                f"Max per cicle: {self.max_per_cicle}\n"
                f"Min per cicle: {self.min_per_cicle}\n"
                f"Max per interval: {self.max_per_interval}\n"
                f"Min per interval: {self.min_per_interval}\n\n"
                f"Time Blocks: {self.time_blocks}\n"
                f"Chooseable Resources by tag: {self.chooseable_resources}\n"
                f"Min per interval: {self.min_per_interval}\n")
    