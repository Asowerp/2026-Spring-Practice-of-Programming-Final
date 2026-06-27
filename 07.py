class CyclicContainer:
    def __init__(self,lst):
        self.lst=lst
    
    def __getitem__(self, key):
        return self.lst[key%len(self.lst)]
    
    def __setitem__(self, key, value):
        self.lst[key%len(self.lst)]=value
    
    def __contains__(self, item):
        return item in self.lst
    
    def __iter__(self):
        return iter(self.lst)
items = input().split()
operations = input().split()

container = CyclicContainer(items)
output = []

i = 0
while i < len(operations):
    op = operations[i]
    if op == "get":
        index = int(operations[i+1])
        output.append(str(container[index]))
        i += 2
    elif op == "set":
        index = int(operations[i+1])
        value = operations[i+2]
        container[index] = value
        i += 3
    elif op == "in":
        value = operations[i+1]
        output.append(str(value in container))
        i += 2
    elif op == "print_all":
        elements = [str(x) for x in container]
        output.append(" ".join(elements))
        i += 1

print("\n".join(output))
