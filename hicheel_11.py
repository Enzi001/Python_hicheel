# # def insert(head, data):
# #     new_node = {'data': data, 'next': head}
# #     return new_node

# # def display(head):
# #     current = head
# #     while current:
# #         print(current['data'], end = ' ')
# #         current = current['next']
# # head = None
# # head = insert(head, 3)
# # head = insert(head, 2)
# # head = insert(head, 1)
# # display(head)
# stack=[]
# def push(item):
#     stack.append(item)
# def pop():
#     if not is_empty():
#         return stack.pop()
#     else:
#         return "stack is empty"
# def is_empty():
#     return len(stack) == 0
# def peek():
#     if not is_empty():
#         return stack[-1]
#     else:
#         return "stack is empty"
# push(5)
# push(10)
# push(15)
# push("enkhjin")
# push(False)
# print(stack)

# pop()
# print(stack)


# def product_less_than_5(a, b, c, d):
#     product = 1
#     if a < 5:
#         product *= a
#     if b < 5:
#         product *= b
#     if c < 5:
#         product *= c
#     if d < 5:
#         product *= d
#     return product
# a, b, c, d = map(int, "3 6 2 4".split())
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('mango')
# fruits.append(4)
# fruits.append(True)
# sublist= fruits[0:7]
# # fruits.clear()
# print(sublist)
# numbers = [4, 2, 9, 1,5]
# numbers.sort()
# print(numbers)