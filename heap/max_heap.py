class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
     # in worst case element will need to make way to top of heap
     while index > 0:
       # get parent element
       parent = (index - 1) // 2
            # check if elem at index is highter priority than parent
       if self.storage[index] > self.storage[parent]:
         # if it is then swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        # update index to be new spot that swapped elem now resides at
        index = parent

       else:
        # otherwise our elem is at valid spot
        # we no longer need to bubble up
           break

  def _sift_down(self, index):
    pass
