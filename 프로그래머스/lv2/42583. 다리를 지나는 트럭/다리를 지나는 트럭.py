from collections import deque

class Bridge:
    
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
        self.queue = deque()
        self.currentWeight = 0
        
    def append(self, next_weight):
        if next_weight + self.currentWeight <= self.weight and len(self.queue) < self.length:
            self.queue.append(next_weight)
            self.currentWeight += next_weight
            return True
        else:
            self.queue.append(0)
            return False
    
    def pop(self):
        self.currentWeight -= self.queue.popleft()
        return

def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(truck_weights)
    sec = 0
    
    for _ in range(bridge_length):
        bridge.append(0)

    while trucks:
        bridge.pop()
        
        if bridge.append(trucks[0]):
            trucks.popleft()
            
        sec += 1
        
    while bridge.queue:
        bridge.pop()
        sec += 1
        
    return sec
        
        