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
