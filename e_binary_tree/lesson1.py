# Challenge: Find minimum value in Binary Search Tree

from bst import BinarySearchTree


def inOrderPrint(node, inorderTraversal):
    if node is not None:
        inOrderPrint(node.leftChild, inorderTraversal)
        inorderTraversal.append(node.val)
        inOrderPrint(node.rightChild, inorderTraversal)


def findMin(root):
    # Write your code here
    inorderTraversal = []
    inOrderPrint(root, inorderTraversal)
    return inorderTraversal[0]


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    print(findMin(BST.root))
