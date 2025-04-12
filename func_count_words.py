def count_words(sentence: str) -> int:
    words = sentence.split() # type == list
    return len(words)

my_string = "Hello, world! This is a test string."
print(count_words(my_string))