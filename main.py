import sys 

from stats import (
    words_counter, 
    character_counter, 
    chars_dict_to_sorted_list,
)

def main():
    # Check if we have enough command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    book_path = sys.argv[1]
    
    # Rest of your code remains the same
    text = get_book_text(book_path)
    words = words_counter(text)
    char_counts = character_counter(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_counts)
    print_report(book_path, words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
