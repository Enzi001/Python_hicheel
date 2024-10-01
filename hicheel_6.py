# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             # 2 ТООНЫ ИХ БАГЫГ ШАЛГАЖ БАЙНА
#             if arr[j] > arr[j+1]:
#             # хөрш элемэнтүүдийг солих
#              arr[j], arr[j+1] = arr[j+1], arr[j]
# arr= [62,34,25,12,7,22,11,90]
# bubble_sort(arr)
# print("Эрэмблэгдсэн массив: " ,arr)

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_number = i
#         for j in range(i+1, len(arr)):
#             if arr[min_number] > arr[j]:
#                 min_number = j
#         arr[i], arr[min_number] = arr[min_number], arr[i]
                
# arr=[64, 34, 25, 12, 22, 33, 11, 90]
# selection_sort(arr)
# print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr = [5, 3, 8, 4, 2]
insertion_sort(arr)
print(arr)