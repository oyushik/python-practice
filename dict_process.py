dict_01 = {"name": "John", "age": 30}
dict_02 = {"math": 90, "science": 85, "history": 78}
dict_03 = {'apple': 3, 'banana': 5}

print(f"나이: {dict_01["age"]}")
print(f"과목들: {[*dict_02.keys()]}")
dict_03['apple'] += 2
print(dict_03)