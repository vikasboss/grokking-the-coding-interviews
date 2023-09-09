# Challenge: Find Nodes at "k" distance from the Root


from bst import BinarySearchTree


def findKNodesAux(root, k, values):
    if root is not None:
        if k < 0:
            return
        findKNodesAux(root.leftChild, k-1, values)
        if k == 0:
            values.append(root.val)
        findKNodesAux(root.rightChild, k-1, values)


def findKNodes(root, k):
    values = []
    findKNodesAux(root, k, values)
    return values


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

    print(findKNodes(BST.root, 2))
