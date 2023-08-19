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
        current_node = self.root
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
            return False

        remove_node = self.root
        parent_node = None
        while remove_node != None:
            if data < remove_node.value:
                parent_node = remove_node
                remove_node = remove_node.left
            elif data > remove_node.value:
                parent_node = remove_node
                remove_node = remove_node.right
            elif data == remove_node.value:
                # no right child
                if remove_node.right == None:
                    if parent_node == None:
                        self.root = remove_node.left
                    else:
                        if parent_node.value > remove_node.value:
                            parent_node.left = remove_node.left
                        elif parent_node.value < remove_node.value:
                            parent_node.right = remove_node.left

                # no left grandchild
                elif remove_node.right.left == None:
                    if parent_node == None:
                        self.root = remove_node.right
                    else:
                        if parent_node.value < remove_node.value:
                            parent_node.right = remove_node.right
                            parent_node.right.left = remove_node.left
                        elif parent_node.value > remove_node.value:
                            parent_node.left = remove_node.right
                            parent_node.left.left = remove_node.left

                # right child and left grandchild
                else:
                    leftmost_child = remove_node.right.left
                    leftmost_parent = remove_node.right
                    while leftmost_child.left != None:
                        leftmost_parent = leftmost_child
                        leftmost_child = leftmost_child.left

                    leftmost_parent.left = leftmost_child.right
                    leftmost_child.left = remove_node.left
                    leftmost_child.right = remove_node.right

                    if parent_node == None:
                        self.root = leftmost_child
                    else:
                        if remove_node.value < parent_node.value:
                            parent_node.left = leftmost_child
                        elif remove_node.value > parent_node.value:
                            parent_node.right = leftmost_child
                return True

        if remove_node == None:
            print(f"couldn't find {data}")
            return False

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
printTree(tree.root)
print("-----------------")
# printable = providedPrintTree(tree.root)
# print(printable)
tree.remove(4)
printTree(tree.root)
