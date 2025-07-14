def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def number_times_each_char(text):
    lowered_text = text.lower()
    dictionary_chars = {}
    for char in lowered_text:
        if char in dictionary_chars:
            dictionary_chars[char] += 1
        else:
            dictionary_chars[char] = 1
    return dictionary_chars

def sort_dictionary(dictionary_chars):
    new_list_format = []
    for char, count in dictionary_chars.items():
        if char.isalpha():
            new_list_format.append({"char": char, "num": count})
    new_list_format.sort(reverse=True, key=lambda x: x["num"])
    return new_list_format