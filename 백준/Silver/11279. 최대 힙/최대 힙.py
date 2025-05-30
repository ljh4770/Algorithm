class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        max_value = self.heap[0]
        last_value = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_value
            self._sift_down(0)
        
        return max_value
    
    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] < self.heap[idx]:
                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break
    
    def _sift_down(self, idx):
        size = len(self.heap)
        
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest_idx = idx
            
            if left_child_idx < size and self.heap[left_child_idx] > self.heap[largest_idx]:
                largest_idx = left_child_idx
            
            if right_child_idx < size and self.heap[right_child_idx] > self.heap[largest_idx]:
                largest_idx = right_child_idx
            
            if largest_idx != idx:
                self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
                idx = largest_idx
            else:
                break

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    N = int(input())

    max_heap = MaxHeap()

    for _ in range(N):
        num = int(input())

        if num == 0:
            item = max_heap.pop()
            if item:
                print(item)
            else:
                print(0)
        else:
            max_heap.insert(num)