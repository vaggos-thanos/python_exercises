list1 = [14, 3, -7, -11, -5, 99, -20]

N = 0
for i in range(len(list1)):
    k = i + N
    if list1[k] < 0:
        list1.pop(k)
        N -= 1

print(list1)

# i = 0
# while i < len(list1):
#     if list1[i] < 0:
#         list1.pop(i)
#         i -= 1
#     else:
#         i += 1

# print(list1)
