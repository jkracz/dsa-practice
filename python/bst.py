class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.value = data
        self.right = right_child
        self.left = left_child


class BinarySearchTree:
    def __init__(self, data=None) -> None:
        if data != None:
            self.root = TreeNode(data)
        else:
            self.root = None

    def insert(self, data: int):
        if self.root == None:
            self.root = TreeNode(data)
            return self.root
        # traverse down until you hit bottom layer
        current_node = next_node = self.root
        # compare data to current val; if val is greater go right, if val is smaller go left
        # if next step is null, insert there, otherwise keep going

        while True:
            if data < current_node.value and current_node.left != None:
                current_node = current_node.left
            elif data >= current_node.value and current_node.right != None:
                current_node = current_node.right
            elif data < current_node.value and current_node.left == None:
                current_node.left = TreeNode(data)
                return current_node.left
            elif data >= current_node.value and current_node.right == None:
                current_node.right = TreeNode(data)
                return current_node.right

    def remove(self, data):
        if self.root == None:
            raise RuntimeError

        parent = curr_node = self.root
        while curr_node != None and curr_node.value != data:
            parent = curr_node
            if data < curr_node.value:
                curr_node = curr_node.left
            elif data > curr_node.value:
                curr_node = curr_node.right
            else:
                

        printTree(parent)
        if parent.left == curr_node:
            parent.left = curr_node.left
            if curr_node.left != None:
                curr_node.left.right = curr_node.right
        else:
            parent.right = curr_node.left
            if curr_node.left != None:
                curr_node.left.right = curr_node.right
        return curr_node

    def lookup(self, data):
        if self.root == None:
            raise RuntimeError
        node = self.root
        while node != None:
            if data == node.value:
                return node
            elif data < node.value:
                node = node.left
            else:
                node = node.right

        return node


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(" " * 4 * level + "-> " + str(node.value))
        printTree(node.left, level + 1)


def providedPrintTree(node):
    tree = {"value": node.value}
    tree["left"] = None if node.left == None else providedPrintTree(node.left)
    tree["right"] = None if node.right == None else providedPrintTree(node.right)
    return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# printTree(tree.root)
# printable = providedPrintTree(tree.root)
# print(printable)
tree.remove(15)
# printTree(tree.root)
