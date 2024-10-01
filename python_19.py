def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Массивын голыг олж авч байна
        left_half = arr[:mid] # Массивын эхний хагас
        right_half = arr[mid:] # Массивын дараагийн хагас
        merge_sort(left_half)
        merge_sort(right_half)
        # Эдгээр индексүүд нь нэгтгэхийн тулд ашиглагдана
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j+= 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1

        while j < len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(arr)