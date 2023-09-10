# Challenge: Find the Height of a BST


from bst import BinarySearchTree


def findDepth(root):
    # Write your code here
    if root is not None:
        left = findDepth(root.leftChild)
        right = findDepth(root.rightChild)
        return 1+max(left, right)
    else:
        return 0


def findHeight(root):
    depth = findDepth(root)
    return 0 if depth <= 0 else depth-1


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    BST.insert(10)
    BST.insert(14)

    print(findHeight(BST.root))
