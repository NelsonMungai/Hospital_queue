from priorityBase import PriorityQueueBase
class HeapPriorityQueue(PriorityQueueBase):
    # a min oriented priority queue implemented with a binary heap
    def _parent(self,j):
        return (j-1)//2
    def _left(self,j):
        return 2*j+1
    def _right(self,j):
        return 2*j+2
    def _has_left(self,j):
        return self._left(j)<len(self._data)
    def _has_right(self,j):
        return self._right(j)<len(self._data)
    def _swap(self,i,j):
        self._data[i],self._data[j]=self._data[j],self._data[i]

    def _upheap(self,j):
        parent=self._parent(j)
        if j>0 and self._data[j]._key > self._data[parent]._key:
            self._swap(j,parent)
            self._upheap(parent)

    def _downheap(self,j):
        if self._has_left(j):
            left=self._left(j)
            big_child=left
            if self._has_right(j):
                right=self._right(j)
                if self._data[right]._key > self._data[left]._key:
                    big_child=right
            if self._data[big_child]._key>self._data[j]._key:
                self._swap(j,big_child)
                self._downheap(big_child)
        
    def _heapify(self):
        start=self._parent(len(self)-1)
        for j in range(start,-1,-1):
            self._downheap(j)
        
    # public methods 
    def __init__(self,contents=()):
        # create a new empty priority Queue
        self._data=[self._item(k,v) for k,v in contents]
        if len(self._data)>1:
            self._heapify()

    def __len__(self):
        return len(self._data)
    def add(self,key,value):
        # add key value pair to the priority queue
        self._data.append(self._item(key,value))
        self._upheap(len(self._data)-1)
    
    def min(self):
        # return but don't remove(k,v) tuple with min key
        # raise exception if empty
        if self.is_empty():
            raise Exception("Priority QUeue is empty")
        item=self._data[0]
        return (item._key,item._value)
    def remove_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        # swap the root and last node
        self._swap(0,len(self._data)-1)
        # remove the root at end and
        item=self._data.pop()
        # fix the new root
        self._downheap(0)    
        return (item._key,item._value)
    
priority_queue=HeapPriorityQueue()
priority_queue.add(3,"C")
priority_queue.add(1,"A")
priority_queue.add(2,"B")

# display the content of the priority Queue
print("Priority Queue Content")
while not priority_queue.is_empty():
    print(priority_queue.remove_min())