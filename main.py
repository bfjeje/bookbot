import sys
from stats import get_num_words, number_times_each_char, sort_dictionary

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def create_report(num_words, dictionary_sorted, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dictionary_sorted:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def format_list(dictionary_sorted):
    temp_list = ""
    for item in dictionary_sorted:
        temp_list += f"{item["char"]}: {item["num"]}\n"
    return temp_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        num_words = get_num_words(book)
        dictionary_chars = number_times_each_char(book)
        dictionary_sorted = sort_dictionary(dictionary_chars)
        create_report(num_words, dictionary_sorted, book_path)
if __name__ == '__main__':
    main()