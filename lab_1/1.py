
arr = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']

dictionary = dict((list(set(arr))[i], [j for j in range(len(arr)) if arr[j] == list(set(arr))[i]]) for i in range(len(set(arr))))

print(dictionary)
