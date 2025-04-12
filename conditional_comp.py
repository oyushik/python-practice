my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [i**2 if i % 2 == 0 else i for i in my_list ]

print(my_list2)