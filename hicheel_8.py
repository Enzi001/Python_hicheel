# Стекийн тодорхойлолт:
# Стак бол өгөгдлийн бүтэц бөгөөд LIFO буюу "сүүлд орсон нь эхэнд гарна" зарчмаар ажилладаг.
# Жишээ: Тавиур дээр ном овоолох - Хамгийн сүүлд тавьсан номыг хамгийн түрүүнд гаргана.


# Үндсэн 4 үйлдэл

# push Шинэ элемэнтийг массивд нэмэх
# Pop Хамгийн сүүлд нэмэгдсэн элемэнтийг гаргах
# Peek Хамгийн сүүлд нэмэгдсэн элемэнтийг авах
# isEmpty Хоосон эсэхийг шалгах

# stack = []
# def push(item):
#     stack.append(item)
#     print(f"Push: {item} stack-д нэмэгдлээ")

# push(5)
# push(10)
# push(15)
# push("enkhjin")
# push(False)
# print(stack)

# Pop

# stack=[5,10,15,"enkhjin",False]
# #isempty хоосон байна уу?


# # print(f"Стак хоосон эсэх : {is_empty()}")

def pop():
    if not is_empty():
        return stack.pop()
    return "stack is empty"

# print(f"Pop: {pop()}")
# print(stack)

stack = [5,10,15,20,25,30,35,40]
def is_empty():
    return len(stack) == 0

def peek():
    if not is_empty():
        return stack[-1]
    return "stack is empty"

print(f'peek: {peek()}')
pop()
print(f'Peek: {peek()}')
print(stack)