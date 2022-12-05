class LinkedList:
    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self, index, item):
        if 0 < index < self.numItems:
            node = LinkedList.__Node(item)
            cursor = self.first.getNext()
            for i in range(index-1):
                cursor = cursor.getNext()
                print(i)
    
            afterNew = cursor.getNext()
            cursor.setNext(node)
            node.setNext(afterNew)
            self.numItems += 1
            return
          
        elif index == 0:
            node = LinkedList.__Node(item)
            afterNew = self.first.getNext()
            self.first.setNext(node)
            node.setNext(afterNew)
            self.numItems += 1
            return
        
        elif index > self.numItems:
            self.append(item)
            return

        raise IndexError("LinkedList index out of range")

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))

        result = LinkedList()

        cursor_self = self.first.getNext()

        while cursor_self is not None:
          result.append(cursor_self.getItem())
          cursor_self = cursor_self.getNext()

        cursor_other = other.first.getNext()

        while cursor_other is not None:
          result.append(cursor_other.getItem())
          cursor_other = cursor_other.getNext()

        return result

    def __contains__(self, item):
        if self.numItems == 0:
          return False
      
        cursor = self.first.getNext()

        while cursor is not None:
          if cursor.getItem() == item:
            return True
          
          cursor = cursor.getNext()

        return False

    def isSorted(self):
      cursor = self.first.getNext()
      while cursor.getNext() is not None:
        if cursor.getItem() > cursor.getNext().getItem():
          return False
        cursor = cursor.getNext()

      return True

    def bubbleSort(self):
      while self.isSorted() == False:
        for i in range(self.numItems-1):
          if self[i] > self[i+1]:
            self.swap(i, i+1)
      return
            

    def __delitem__(self, index):
      if 0 < index < self.numItems:
          cursor = self.first.getNext()
          for i in range(index-1):
            cursor = cursor.getNext()

          toDelete = cursor.getNext()
          cursor.setNext(cursor.getNext().getNext())
          toDelete.setNext(None)
          self.numItems -= 1
          return
      elif index == 0:
        toDelete = self.first.getNext()
        self.first.setNext(self.first.getNext().getNext())
        toDelete.setNext(None)
        self.numItems -= 1
        return

      raise IndexError("LinkedList index out of range")


    def __eq__(self, other):
      if type(self) != type(other):
        return False

      if self.numItems != other.numItems:
        return False

      cursor_self = self.first.getNext()
      cursor_other = other.first.getNext()

      while cursor_self is not None:
        if cursor_self.getItem() != cursor_other.getItem():
          return False

        cursor_self = cursor_self.getNext()
        cursor_other = cursor_other.getNext()

      return True
      

    def __len__(self):
        return self.numItems

    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def swap(self, indexA, indexB):
        cursorA = self.first.getNext()
        cursorB = self.first.getNext()
        for i in range(indexA):
             cursorA = cursorA.getNext()
        for x in range(indexB):
             cursorB = cursorB.getNext()

        A = cursorA.getItem()
        B = cursorB.getItem()

        cursorA.setItem(B)
        cursorB.setItem(A)

        return
        

    def __str__(self):
      cursor = self.first.getNext()
      outstring = '['
      
      while cursor is not None:
        
        outstring += str(cursor.getItem())
        if cursor.getNext() is not None:
          outstring += ', '

        cursor = cursor.getNext()

      outstring = outstring.rstrip(', ')
      outstring += ']'

      return outstring

def main():
    lst = LinkedList()

    for i in range(100):
        lst.append(i)

    lst2 = LinkedList(lst)

    print(lst)
    print(lst2)

    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    lst3 = lst + lst2

    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    del lst[1]

    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")

    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")

    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")

    del lst2[2]

    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")

    lst4 = LinkedList(lst)
    lst.insert(0, 100)
    lst4 = LinkedList([100]) + lst4
  
    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")

    lst.insert(1000, 333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")

    
    lst.swap(1, 2)

    if lst != lst4:
        print("Test 11 Passed")
    else:
        print("Test 11 Failed")

    lst.bubbleSort()
    lst4.bubbleSort()

    if lst == lst4:
      print("Test 12 Passed")
    else:
      print("Test 12 Failed")

    print(lst)
    print(lst4)

if __name__ == "__main__":
    main()