class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            # if not then place new node
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise repeat the proccess
                self.left.insert(value)
        #  check new node >= self node value
        if value >= self.value:
            # if no right child place new node
            if not self.right:
                self.right = BinarySearchTree(value)
                # otherwise repeat procceess
            else:
                self.right.insert(value)

    def contains(self, target):
       while self.value != target:
         if target > self.value:
            if self.right is not None:
              self = self.right
            else:
              return False
         else:
            if self.left is not None:
              self = self.left
            else:
              return False
       if self.value == target:
         return True

    def get_max(self):
      # loop down to find right most
        while self.right is not None:
            self = self.right
        return self.value

    def for_each(self, cb):
       cb(self.value)
       if self.left:
           self.left.for_each(cb)
       if self.right:
           self.right.for_each(cb)

