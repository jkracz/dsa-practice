from bstForSearch import BinarySearchTree

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.recursiveBFTraversal([tree.root], []))
print(tree.inorderDFS(tree.root, []))
print(tree.postorderDFS(tree.root, []))
print(tree.preorderDFS(tree.root, []))

#      9
#   4     20
# 1  6  15  170

# DFS
# inorder - [1, 4, 6, 9, 15, 20, 170]
# postorder - [1, 6, 4, 15, 170, 20, 9]
# preorder - [9, 4, 1, 6, 20, 15, 170]
