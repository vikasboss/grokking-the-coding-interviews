# Challenge: Find Ancestors of a given node in a BST


from bst import BinarySearchTree


def findAncesstorsAux(root, k, ancesstors):
    if root is not None:
        if k < root.val:
            ancesstors.insert(0, root.val)
            findAncesstorsAux(root.leftChild, k, ancesstors)
        elif k > root.val:
            ancesstors.insert(0, root.val)
            findAncesstorsAux(root.rightChild, k, ancesstors)
        else:
            return


def findAncestors(root, k):
    # Write your code here
    ancesstor = []
    findAncesstorsAux(root, k, ancesstor)
    return ancesstor


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    print(findAncestors(BST.root, 12))
