#  Зангилаа нь өгөгдлийг хадгалж буй нэгж
#  Ирмэг нь зангилаа хоорондын холболт

# def greet(name):
#     name= "enkhjin"
#     print( name)

#     for i faifniwn:
#         print(i)

# leaf
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
# root = [ 1, [ 2, [ 4,[],[]] , [5,[],[]]],[3,[],[]]]
# print(root)
#  Pre-order Эцэгээс эхэлж уншина Зүүн дэд Баруун дэд

# def pre_order(node):
#     if node:
#         print(node[0], end=' ')
#         pre_order(node[1])
#         pre_order(node[2])

# def in_order(node):
#     if node:
#         in_order(node[1])
#         print(node[0], end=' ')
#         in_order(node[2])

# def post_order(node):
#     if node:
#         post_order(node[1])
#         post_order(node[2])
#         print(node[0], end=' ')
# Бинар
# Зүүн талын нодууд эцэг нодоос бага утгатай.
# Баруун талын нодууд эцэг нодоос их утгатай.

def insert_bst(node,value):
    if not node:
        return [value, [],[]]
    if value <node[0]:
        node[1]= insert_bst(node[1],value)
    else:
        node[2]=insert_bst(node[2],value)

    return node

def search_bst(node,value):
    if not node:
        return False
    if value == node[0]:
        return True
    elif value < node[0]:
        return search_bst(node[1], value)
    else:
        return search_bst(node[2],value)

bst = []
bst = insert_bst(bst, 10)
bst = insert_bst(bst, 5)
bst = insert_bst(bst, 20)
bst = insert_bst(bst, 2)
bst = insert_bst(bst, 8)

print("15 ыг хайж байна уу" , search_bst(bst, 15))
print("20 ийг хайж байна уу" , search_bst(bst, 20))
    #     10
    #    /  \
    #   5    15
    #  / \
    # 2   8
