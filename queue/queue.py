class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # insert 
    # new array if its full
    # linked list
    self.storage = []

  def enqueue(self, item):
    pass
    # add item
    return self.storage.insert(0, item)
  
  def dequeue(self):
    pass
    # remove item
    return self.storage.pop()

  def len(self):
    pass
    # counter
    return len(self.storage)
