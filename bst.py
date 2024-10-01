


# searching a bst

def search(root, target):
    if not root:
        return False 
    # If root equals target return root
    if root.val == target:
        return True
    
    elif root.val < target:
        root = root.right
        search(root, target)
    else:
        root.val = root.left
        search(root, target)