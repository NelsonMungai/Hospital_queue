from AdaptablePriorityQueue import AdaptablePriorityQueue

class HospitalQueue(AdaptablePriorityQueue):
    class PatientLocator(AdaptablePriorityQueue.Locator):
        __slots__ = '_severity', '_age'

        def __init__(self, severity, age, key, value, j):
            super().__init__(key, value, j)
            self._severity = severity
            self._age = age
    
    def _bubble(self, j):
        if j > 0 and (self._data[j]._key > self._data[self._parent(j)]._key or
                      (self._data[j]._key == self._data[self._parent(j)]._key and
                       self._data[j]._value._age > self._data[self._parent(j)]._value._age)):
            self._upheap(j)
        else:
            self._downheap(j)

    def add_patient(self, severity, age, name):
        token = self.PatientLocator(severity, age, (severity, age), name, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update_patient(self, loc, new_severity, new_age):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid Locator")
        loc._key = (new_severity, new_age)
        loc._severity = new_severity
        loc._age = new_age
        self._bubble(j)

    def remove_patient(self, loc):
        return self.remove(loc)

# Example Usage
hospital_queue = HospitalQueue()
hospital_queue.add_patient(2,30,"John")
hospital_queue.add_patient(severity=1, age=25, name="Alice")
hospital_queue.add_patient(severity=3, age=22, name="Bob")
hospital_queue.add_patient(severity=1, age=25, name="Alice")
hospital_queue.add_patient(severity=1, age=12, name="Janice")
hospital_queue.add_patient(severity=1, age=45, name="ALicia")
hospital_queue.add_patient(severity=1, age=60, name="Jasper")

# while not hospital_queue.is_empty():
#     patient=hospital_queue.remove_min()
#     print(f"Patient:{patient}")

# Display patients in priority order
hospital_queue_copy=HospitalQueue()

