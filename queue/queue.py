import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # insert 
    # new array if its full
    # create then import linked list 
    self.storage = linked_list.LinkedList

  def enqueue(self, item):
    pass
    # add item
    self.storage.insert(0, item)
  
  def dequeue(self):
    pass
    # remove item
    return self.storage.pop()
 
  def len(self):
    pass
    # counter
    return len(self.storage)
