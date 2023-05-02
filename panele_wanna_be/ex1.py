list1 = [12, 5, 3, 20, 60, 3, 44, 3, 9, 51, 7, 3, 42]

N = 0

for i in range(len(list1)):
    if list1[i] == 3:        
        N+=1

N += len(list1)
for i in range(N):
    if list1[i] == 3:
        list1.insert(i +1, 0)

print(list1)

# i = 0
# while i < len(list1):
#     if list1[i] == 3:
#         list1.insert(i+1, 0)
#     i += 1

# print(list1)