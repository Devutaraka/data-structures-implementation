class DynamicArray:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def remove(self, value):
        self.data.remove(value)

    def get(self, index):
        return self.data[index]

    def size(self):
        return len(self.data)


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)

print(arr.get(1))
print(arr.size())
