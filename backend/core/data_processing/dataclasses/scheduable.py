import uuid

class Schedule:
    def __init__(self, interval_blocks:int, cicle_intervals:int):
        self.blocks = [[None for _ in range(cicle_intervals)] for _ in range(interval_blocks)]
        
    def __repr__(self):
        result = ""
        for row in self.blocks:  # row = block
            for cell in row:     # column = interval
                result += f"{cell}\t"
            result += "\n"
        return result   
     
class Scheduable:
    def __init__(self, name:str, interval_blocks:int, cicle_intervals:int, max_per_cicle:int, min_per_cicle:int, max_per_interval:int, min_per_interval:int):
        self.id = uuid.uuid4()
        self.name = name
        
        self.schedule = Schedule(interval_blocks, cicle_intervals)
        
        self.max_per_cicle = max_per_cicle
        self.min_per_cicle = min_per_cicle
        self.max_per_interval = max_per_interval
        self.min_per_interval = min_per_interval

    def __repr__(self):
        return (f"\nName: {self.name}\n\n"
                f"Schedule:\n{self.schedule}\n"
                f"Max per cicle: {self.max_per_cicle}\n"
                f"Min per cicle: {self.min_per_cicle}\n"
                f"Max per interval: {self.max_per_interval}\n"
                f"Min per interval: {self.min_per_interval}\n")
     

