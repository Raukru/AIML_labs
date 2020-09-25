
A = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

B = {1,2,3,4,5,16,17,18,19,20}

def coefficient_Jaccard(A, B):

    a = list(A)
    b = list(B)

    similar_elements = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                similar_elements += 1

    return similar_elements / (len(a)+len(b)-similar_elements)

# 12 - мно-во A
# 23 - мно-во B

# 12 - 23 = 1
# 12 - 1 = 2    12 - (12 - 23) = 2
# 23 - 2 = 3    23 - (12 - (12 - 23) = 3
# len(1) + len(2) + len(3) = len(123)

# coefficient = len(2)/len(123)
# coefficient = len(2) / ( len(3)+len(2)+len(1) )
# coefficient = len(12 - (12 - 23)) / ( len(23-(12-(12-23)) + len(12-(12-23))+len(12-23) )

coefficient = len(A.difference(A.difference(B))) / ( len(B.difference(A.difference(A.difference(B)))) + len(A.difference(A.difference(B))) + len(A.difference(B)) )

print("Множество A:\t\t", A)
print("Множество B:\t\t", B, end="\n\n")
print("Пересечение множеств:\t\t", A.difference(A.difference(B)))
print("Объедиинение множеств:\t\t", A.difference(A.difference(B)), A.difference(B), B.difference(A.difference(A.difference(B))), end="\n\n")
print("Коэффициент сходства: ", coefficient)
print("Коэффициент сходства: ", coefficient_Jaccard(A, B))
