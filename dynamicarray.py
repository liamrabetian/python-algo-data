import ctypes


class DynamicArray(object):
    """This class is meant to produce the behavior of
    
    Dynamic array allocations in python.
    It is made for learning purposes.
    """
    def __init__(self):
        self.n = 0 # number of ellements in the array
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self): # implementaion of len method
        return self.n

    def __getitem__(self, k):
        """Produces the behavior of geting elements by their index"""
        if not 0 <= k < self.n:
            return IndexError('index is out of bounds!')
        return self.A[k]

    def append(self, element):
        """Appending new items to our array"""
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        """Make the capacity twice if there's no capacity."""
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_capacity

    def make_array(self, capacity):
        """Making the raw array via ctypes library"""
        return (capacity * ctypes.py_object)()

if __name__ == '__main__':
    arr = DynamicArray()
    print(arr[1]) # should return index error
    arr.append(2) # the rest should work flawlessly
    arr.append(3)
    print(len(arr))
    print(arr[1]) 
