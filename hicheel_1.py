# anar = {"name": "Anar", 
#         "age": 22, 
#         "gender": "male", 
#         "isMarried": False, 
#         "hobbies": ["music", "reading","swimming"]}
# print(hash("Anar"))

# class HashTable:
#     def __init__(self,size):
#         self.size = size # Хүснэгтийн хэмжээг
#         self.table = [None] * self.size
#     def hash_function(self,key):
#         return hash(key) % self.size # Key ийг түлхүүр болгон хувилах
#     def insert(self,key,value):
#         index = self.hash_function(key)
#         self.table[index] = value
#     def get(self,key):
#         index = self.hash_function(key)
#         return self.table[index]
# hash_table = HashTable(10)
# hash_table.insert("name","Anar")
# # hash_table.insert("age": 22)
# # hash_table.insert("age": "22")
# print(hash_table.get("name"))

# \
# my_ticket=[dammow,dwfmwfowf,dwomfowfmw,   ]

# Стек үүсгэх
# stack = []
massiv = []
def hoosn_eseh():
    return len(massiv) == 0
def element_nemeh(a):
    massiv.append(a)
    print(f"{a} нэмэгдлээ.")
def ustgah():
    if hoosn_eseh():
        return "massiv chin hooson bn"
    return massiv.pop()
def tugsgul_avah():
    if hoosn_eseh():
        return "massiv chin hooson bn"
    return massiv[-1]
def hemjee():
    return len(massiv)
element_nemeh(5)
element_nemeh(10)
element_nemeh(15)
print(f"Хамгийн дээд элемент: {tugsgul_avah()}")
print(f"Гарсан элемент: {ustgah()}")
print(f"Стекийн хэмжээ: {hemjee()}")
print(f"Стек хоосон эсэх: {hoosn_eseh()}")

# # Стек хоосон эсэхийг шалгах функц
# def is_empty():
#     return len(stack) == 0
# # Стек рүү элемент нэмэх функц
# def push(item):
#     stack.append(item)
#     print(f"{item} нэмэгдлээ.")
# # Стекээс элемент гаргах функц
# def pop():
#     if is_empty():
#         return "Стек хоосон байна."
#     return stack.pop()
# # Стекээс дээд элементийг харах функц
# def peek():
#     if is_empty():
#         return "Стек хоосон байна."
#     return stack[-1]
# # Стекийн хэмжээ
# def size():
#     return len(stack)
# # Стек үүсгэх
# push(5)
# push(10)
# push(15)
# print(f"Гарсан элемент: {pop()}")
# print(f"Хамгийн дээд элемент: {peek()}")
# print(f"Стекийн хэмжээ: {size()}")
# print(f"Стек хоосон эсэх: {is_empty()}")