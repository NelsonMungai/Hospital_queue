from HeapPriorityQueue import HeapPriorityQueue
class AdaptablePriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._item):
        __slots__='_index'

        def __init__(self,k,v,j):
            super().__init__(k,v)
            self._index=j
    # non public methods
    def _swap(self,i,j):
        super()._swap(i,j)
        self._data[i]._index=i
        self._data[j]._index=j

    def _bubble(self,j):
        if j>0 and self._data[j]<self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self,key,value):
        token=self.Locator(key,value,len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token
    
    def update(self,loc,newkey,newval):
        j=loc._index
        if not(0<=j<len(self) and self._data[j]is loc):
            raise ValueError("Invalid Locator")
        loc._key=newkey
        loc._value=newval
        self._bubble(j)

    def remove(self,loc):
        j=loc._index
        if not(0<=j<len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j==len(self)-1:
            self._data.pop()
        else:
            self._swap(j,len(self)-1)
            self._data.pop()
            self._bubble(j)
        return (loc._key,loc._value)
    



adaptable_queue=AdaptablePriorityQueue()

locator1=adaptable_queue.add(3,"C")
locator2=adaptable_queue.add(1,"B")
locator3=adaptable_queue.add(2,"A")
print("Contents")
# while not adaptable_queue.is_empty():
#     print(adaptable_queue.remove_min())



# Update an element in the priority queue
adaptable_queue.update(locator2,0,"B")
print("\nPriority Queue content after update:")
for locator in adaptable_queue._data:
    print(locator._key,locator._value)

# Remove an element from the priority_queue
# removed_element=adaptable_queue.remove(locator3)


# display contents after removing elements
print("Priority Queue content after removal:")
for _ in adaptable_queue._data:
    print(_._key,_._value)

# print("\n removed Element",removed_element)

while not adaptable_queue.is_empty():
    print(adaptable_queue.remove_min())