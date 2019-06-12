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
        #  check new node >= current node value
        if value >= self.value:
            # if no right child place new node
            if not self.right:
                self.right = BinarySearchTree(value)
                # otherwise repeat procceess
            else:
                self.right.insert(value)


  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass