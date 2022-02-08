class Minheap():
    def __init__(self, sizeofheap):
        self.heapsize = sizeofheap
        self.heap = [0] * (sizeofheap + 1)

        self.realsize = 0

    def add(self, element):
        self.realsize += 1
        if self.realsize > self.heapsize:
            print(" added to many elements")
            self.realsize -= 1
            return
        self.heap[self.realsize] = element
        index = self.realsize
        parent = index // 2
        while (self.heap[index] < self.heap[parent] and index > 1):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2
    def peep(self):
        return self.heap[1]

a = [111,21, 441,1]

out = Minheap(15)
for i in a:
    out.add(i)
print(out.heap)
print(out.peep())


