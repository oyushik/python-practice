list_01 = [1, 2, 3]
list_02 = [4, 5, 6]

mapped_list = list(map(lambda x, y: x + y, list_01, list_02))
print(mapped_list)  # Output: [5, 7, 9]