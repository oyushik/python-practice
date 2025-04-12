string = "Python is awesome"
alphabet_list = ["a", "e", "i", "o", "u"]
cnt = 0

for char in alphabet_list:
    string.count(char)
    cnt += string.count(char)

print(cnt)