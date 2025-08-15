import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words

from stats import get_character_instances

from stats import get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_words = get_book_text(sys.argv[1])
    num_words = get_num_words(book_words)
    num_letters = get_character_instances(book_words)
    sorted_list = get_sorted_list(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_character in sorted_list:
        print(f"{sorted_character["char"]}: {sorted_character["num"]}")
    print("============= END ===============")

main()
