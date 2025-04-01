my_strings = ["de", "ma", "is", "quite", "the guy fr fr"]

def words_longer_than_5(my_strings):
    return len(my_strings) > 4

word_length = filter(words_longer_than_5,my_strings)
print(list(word_length))