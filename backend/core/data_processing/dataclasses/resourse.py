from core.data_processing.dataclasses.scheduable import Scheduable

class Resource(Scheduable):
    def __init__(self, name:str, interval_blocks:int, cicle_intervals:int, max_per_cicle:int, min_per_cicle:int, max_per_interval:int, min_per_interval:int, tags:list[str]):
        super().__init__(name, interval_blocks, cicle_intervals, max_per_cicle, min_per_cicle, max_per_interval, min_per_interval)
        self.tags = tags
    
    def __repr__(self):
        return (f"\nResource Name: {self.name}\n\n"
                f"Schedule:\n{self.schedule}\n"
                f"Max per cicle: {self.max_per_cicle}\n"
                f"Min per cicle: {self.min_per_cicle}\n"
                f"Max per interval: {self.max_per_interval}\n"
                f"Min per interval: {self.min_per_interval}\n\n"
                f"Tags: {self.tags}\n")
        