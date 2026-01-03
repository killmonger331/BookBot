from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = get_char_counts(book_text)
    sorted_chars = get_sorted_char_counts(char_counts)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()