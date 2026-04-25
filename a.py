# n = 5
# Target Output: 1, 2, 3, 4, 5
# for i in range(n):
#     print(i+1, end=', ')
# i = 1
# while (i <= n):
#     if i == 5:
#         print(i)
#     else:
#        print(i, end=", ")
#     i+=1

n = 4
# Target Output: 4, 3, 2, 1
a = []
for i in range(n):
    a.append(i + 1)
a.sort(reverse=True)
" ".join(a)
print(a)
