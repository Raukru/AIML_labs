A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

B = {1, 2, 3, 4, 5, 16, 17, 18, 19, 20}


def coefficient_Jokkard(a, b):
    union_len = 0
    len_a = len(a)
    len_b = len(b)
    for __ in range(len(b)):
        b_pop = b.pop()
        if b_pop in a:
            union_len += 1
            a.remove(b_pop)
    coefficient = union_len / (len_a + len_b - union_len)
    return coefficient


print("Множество A:\t\t", "({})".format(len(A)), A)
print("Множество B:\t\t", "({})".format(len(B)), B, end="\n\n")
print("Пересечение множеств:\t\t", "({})".format(len(A.intersection(B))), A.intersection(B))
print("Объедиинение множеств:\t\t", "({})".format(len(A.union(B))), A.union(B), end="\n\n")
print("Коэффициент сходства: ", coefficient_Jokkard(A, B))
