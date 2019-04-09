import ctypes

class DynamicArray:
    #A dynamic array class akin to a simplified Python list.”””
    def __init__(self):
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A=self._make_array(self._capacity) # low-level array

    def __len__(self):
        return self._n
   
    def __getitem__(self,k):
        if not 0<=k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
   
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
   
    def _resize(self,c):
        B = self._make_array(c)
        print("Resize worked")
        for k in range(self._n):
            B[k]=self._A[k]
        self._A = B
        self._capacity = c
       
    def _make_array(self,c):
        return(c*ctypes.py_object)()
    
    def getLength(self):
        return self.__len__()
    c = DynamicArray()
    for i in range(10):
      c.append("Add an item"+ str(i))
      print(str(i) + " eklendi, dizi boyutu: " + str(c.getLength()))
    
