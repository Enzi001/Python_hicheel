# # Бинар хайлтын модод элемент нэмэх функц
# def insert_bst(node, value):
#     if not node:
#          return [value, [], []]
#     if value < node[0]:
#              node[1] = insert_bst(node[1], value)
#     else:
#             node[2] = insert_bst(node[2], value)
#     return node
# # Бинар хайлтын модод элемент хайх функц
# def search_bst(node, value):
#     if not node:
#         return False
#     if value == node[0]:
#         return True
#     elif value < node[0]:
#         return search_bst(node[1], value)
#     else:
#         return search_bst(node[2], value)
# # Бинар хайлтын мод үүсгэж турших
# bst = []
# bst = insert_bst(bst, 10)
# bst = insert_bst(bst, 5)
# bst = insert_bst(bst, 15)
# bst = insert_bst(bst, 2)
# bst = insert_bst(bst, 8)
# print("15-г хайж байна уу?", search_bst(bst, 15)) # True
# print("20-г хайж байна уу?", search_bst(bst, 20)) # False

def insert(root, key):
    # Root хоосон бол шинэ зангилаа үүсгэнэ
    if not root:
        return TreeNode(key) 
        # Оруулах утгын тохирох байрлалд оруулах хэсэг
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        # Уртыг шинэчилнэ 
    root.height = 1 + max(height(root.left), height(root.right))
    # Тэнцвэр тооцоолох
    balance = get_balance_factor(root)

# Зүүн-зүүн нөхцөл
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
# Баруун-баруун нөхцөл
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
# Зүүн-баруун нөхцөл
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
# Баруун-зүүн нөхцөл
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root