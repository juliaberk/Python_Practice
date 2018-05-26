# This problem is in the HB resources
# multiple solutions
# depth first gives you ascending order

# WHITEBOARD

# Is this a binary search tree?

#global variable
values = []

# root node
# depth first left left left
def traverse(node):
    if node.left:
        #then we will keep going left
        traverse(node.left)
    values.append(node.value)

    if node.right:
        traverse(node.right)

    #we have taken care of left and right, hit bottom
    sorted(values) == values

# this solution isn't great for memory, making lists

# Another solutions

def is_BST(node):
    values = []

    # helper function, one level of nesting is cool
    def traverse (node):
        #append to local variable

        
#   ###################

class BinaryNode(object):   # ...
    def is_balanced(self):
        """Is the tree at this node balanced?"""

        # START SOLUTION

        def _num_descendants(node):
            """Returns number of descendants or None if already imbalanced."""

            if not node:
                # Our base case: we're not a real node (child of a leaf)
                return 0

            # Get descendants on left; if "None", already imbalanced---bail out
            left = _num_descendants(node.left)

            if left is None:
                return None

            # Get descendants on right; if "None", already imbalanced---bail out
            right = _num_descendants(node.right)

            if right is None:
                return None

            if abs(left - right) > 1:
                # Heights vary by more than 1 -- imbalanced!
                return None

            # Height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1

        return _num_descendants(self) is not None
