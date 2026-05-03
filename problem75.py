class vector:
    def __init__(self, values):
        self.values = values
        
    def __len__(self):
        return len(self.values)

v1 = vector([1, 2, 3])
print(len(v1))