



# #         y                              x
# #        / \     Баруун эргүүлэлт       / \
# #       x   T3   --------------->      T1   y
# #      / \                              / \
# #     T1  T2                           T2  T3
# # #


# # def right_rotate(y):
# #     # y нь эхний үндэсийн зангилаа
# #     x = y.left # x ийн зүүн child
# #     T2 = x.right # T2 нь X ийн баруун талын child, y ийн зүүн child шилжүүлэх

# #     # эргүүлэх үйлдэл
# #     x.right = y
# #     y.left = T2
# #     # Өндөрийн өөрчлөлт
# #     y.height = 1 + max(height(y.left), height(y.right)) # y ийн шинэ өндөр
# #     x.height = 1 + max(height(x.left), height(x.right)) # x ийн шинэ өндөр
    
# #     # шинэ үүссэн зангилааг буцаах
# #     return x

# # def get_balance(zangilaa):
# #     height = 0
# #     if not zangilaa:
# #         return 0
# #     return height(zangilaa.left) - height(zangilaa.right)


# # Эхний индекс (low) болон сүүлийн индекс (high)-ийг тодорхойлно.
# # Жагсаалтын голд байгаа элементийг шалгана (mid индекс).
# # Хэрэв хайж буй тоо голд байгаа тоотой тэнцүү бол амжилттай хайлт гэж үзнэ.
# # Хэрэв хайж буй тоо голын тооноос бага бол зүүн тал руу хасах замаар хайна (high = mid - 1).
# # Хэрэв хайж буй тоо голын тооноос их бол баруун тал руу хасах замаар хайна (low = mid + 1)
# # Энэ процессыг олтол давтана эсвэл хайлт амжилтгүй болгоно (low > high бол).

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         # Голын индексийг тодорхойлно
#         mid = (low + high) // 2

#         # Хэрэв хайж буй тоо голын тоо байвал буцаана

#         if arr[mid] == target:

#             return mid

#         elif arr[mid] > target:

#             high = mid - 1

#         else:

#             low = mid + 1
            
#     return -1

# arr = [1,3,5,7,9,11,13,15,17,19]
# target = 13
# result = binary_search(arr,target)

# if result != -1:
#     print(f"{target} нь жагсаалтын {result} т байна")
# else:
#     print(f"{target} нь жагсаалтад байхгүй байна")


# # хайж байгаа тоо 7
# # эхний алхам low 0 high 9
# # 0+9 // 2 = 4
# #
# #
# #


# fruits = ['apple', 'banana', 'cherry']
# fruits.extend(['apple', 'pineapple'])
# # print(fruits)
# # index_of_cherry = fruits.index('apple')
# # print(index_of_cherry)
# # fruits.clear()
# count_of_apple = fruits.count('cherry')
# print(fruits)

# from collections import deque
# dq = deque([1,2,3])
# dq.appendleft(4)
# dq.appendleft(0)
# dq.pop()
# dq.popleft()
# print(dq)
# from collections import Counter
# cnt = Counter(['apple', 'orange', 'apple', 'cherry','cherry'])
# # cnt.append('apple')
# print(cnt.most_common(2))

# from collections import OrderedDict

# od = OrderedDict()
# od['name'] = 'bold'
# od['age'] = 28
# od['isMarried'] = False
# print(od)

# from collections import defaultdict

# def gurvaljin(a,b,c):
#     p=a+b+c
#     print(p)
#     return p
# gurvaljin(1,2,3)

# def insert(head, data):
#     new_node = {'data': data, 'next': head}
#     return new_node
# def display(head):
#     current = head
#     while current:
#         print(current['data'], end=' ')
#         current = current['next']
# # Жишээ ашиглалт
# head = None
# head = insert(head, 3)
# head = insert(head, 2)
# head = insert(head, 1)
# display(head) # Гаралт: 1 2 3

stack = []
def push(item):
    stack.append(item)
def pop():
    if not is_empty():
        return stack.pop()
    else:
      return "Stack is empty"
def is_empty():
    return len(stack) == 0
def peek():
    if not is_empty():
        return stack[-1]
    else:
        return "Stack is empty"
# Жишээ ашиглалт
push(1)
push(2)
push(3)
print(pop()) # Гаралт: 3
print(peek()) # Гаралт: 2