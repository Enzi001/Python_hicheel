# def функц зарлах түлхүүр үг
# hello функций нэр
# функц заралсан () хаалт авна
# a=5
# def hello(duudah):
#     print("Hello, world!")

# def hello(name, age,gender):
#     print("hello ," + {name})

# hello("oyun", 18, "female")

# def add(a,b):
#     return a + b
# num1 = float(input("Эхний тоогоо оруулна уу : "))
# num2 = float(input("Хоёр дахь тоогоо оруулна уу : "))
# result = add(num1, num2)
# print(f"Хоёр тооны нийлбэр : {result}")

# def greeting(name,age):
#     return f"Сайн байна уу, {name}. Та {age} настай"

# user_name = input("Та нэрээ оруулна уу : ")
# user_age = input("Та насаа оруулна уу : ")

# garalt = greeting(user_name,user_age)

# print(garalt)


# def is_even(number):
#     return number % 2 == 0

# if is_even(8):
#     print("Тэгш тоо байна")
# else:
#     print("Сондгой тоо байна")






# Global хувьсагч

# x = "Hello"
# def my_function():
#     print(x)
# my_function()

#local хувьсагч
# def my_function():
#     y="hello"
#     print(y)
# my_function()
# y="Сайн уу?"
# print(y)

# cars = ["audi","bmw","subaru","toyota"]

# for i in cars:
#     print(i)

# for i in range(1, 11):
#     print(i ** 2)

# i = 10

# while i >= 1:
#     i -= 1
#     print(i)

# numbers = [2 , 3 , 9 , 6 , 5] 
# largest_number = numbers  
# for number in numbers: 
#     if number > largest_number: 
#         largest_number = number 
# print("хамгийн их тоо бол :" +  number)

# numbers = [5, 2, 3, 9, 6, 5]
# largest_number = numbers[0]  # Жагсаалтын хамгийн эхний утга

# for number in numbers: 
#     if number > largest_number: 
#         largest_number = number  # хамгийн их утгыг шинэчилнэ

# print("хамгийн их тоо бол: " + str(largest_number))

# def sum_numbers():
#     total = 0
#     while True:
#         # Хэрэглэгчээс тоо авах
#         user_input = input("Тоо оруулна уу (done гэж бичиж дуусгана уу): ")
        
#         # Хэрэв хэрэглэгч 'done' гэж бичсэн бол давталтаас гарна
#         if user_input.lower() == "done":
#             break
        
#         # Тоог нийт нийлбэрт нэмэх
#         total += int(user_input)
    
#     # Бүх тооны нийлбэрийг хэвлэх
#     print("Бүх тооны нийлбэр:", total)


# sum_numbers()

