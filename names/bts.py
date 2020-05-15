class BtsNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree

    def insert(self, value):
        # compare new node to node value
        if value < self.value:
            # if left doesnt exist
            if self.left is None:
                # create left if no val to left
                self.left = BtsNode(value)
            else:
                # recurse left
                self.left.insert(value)
        else:
            # value is equal or greater recurse right
            if self.right is None:
                # create right is no val to right
                self.right = BtsNode(value)
            else:
                # recurse right
                self.right.insert(value)

    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BinarySearchTree
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BinarySearchTree
            if not self.right:
                return False
            return self.right.contains(target)
    # Return the maximum value found in the tree
