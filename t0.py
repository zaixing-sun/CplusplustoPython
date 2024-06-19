k = 4476801
str1 = "qdel "
for i in range(150):
    str1 += str(k) + ', '
    k = k + 1
print(str1)
