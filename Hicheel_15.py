# import heapq

# heap=[]

# heapq.heappush(heap,1)
# heapq.heappush(heap,8)
# heapq.heappush(heap,7)

# print(heap)

import heapq

max_heap=[]

heapq.heappush(max_heap,-5)
heapq.heappush(max_heap,-10)
heapq.heappush(max_heap,-8)

print([-x for x in max_heap])

# import heapq
# heap=[]
# numbers = [30,10,40,5,20,50,1]
# for number in numbers:
#     heapq.heappush(heap,number)
#     heapq.hea
# print(heap)

#       1
#    /     \
#   5      10
# /  \   /   \
# 30 50 40   20