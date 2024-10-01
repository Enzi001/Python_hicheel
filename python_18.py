# stack = []

# stack.append(51)
# stack.append(52)

# print(stack.pop())
# print(stack)

# LIFA last in fitst out
# queue FIFO Fitst in First out

# enqueue(5)
# dequeue(6)

# from collections import deque

# queue = deque()

# queue.append(1)
# queue.append(2)

# print(queue.popleft())
# # print(queue)

# from collections import deque
# queue = deque()
# def add_user(user):
#     queue.append(user)
#     print(f"{user} хэрэглэгчийг дараалалд нэмлээ.")

# def serve_user():
#     if queue:
#         served_user = queue.popleft()
#         print(f"{served_user} хэрэглэгч үйлчлүүллээ.")
#     else:
#         print("Дараалал хоосон байна.")

# def view_queue():
#     if queue:
#         print("Одоогийн дараалал:", list(queue))
#     else:
#         print("Дараалал хоосон байна.")
# add_user("1-р хэрэглэгч")
# add_user("2-р хэрэглэгч")
# add_user("3-р хэрэглэгч")
# view_queue() 
# serve_user() 
# view_queue()  
# serve_user()  
# view_queue()  

# def check_parentheses(expression):
#     stack = []
#     pairs = {')': '(', ']': '['}
    
#     for char in expression:
#         if char in '([':
#             stack.append(char)
#         elif char in ')]':
#             if not stack or stack[-1] != pairs[char]:
#                 return "Буруу хаалттай"
#             stack.pop()
    
#     return "Зөв хаалттай" if not stack else "Буруу хаалттай"

# expression1 = "([()])"
# expression2 = "[(])"
# print(check_parentheses(expression1)) 
# print(check_parentheses(expression2))  



