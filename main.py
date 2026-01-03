import sys

from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Expect exactly one argument: path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: file not found: {book_path}")
        sys.exit(1)

    num_words = get_num_words(book_text)

    print("============ BOOKBOT ============" )
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = get_char_counts(book_text)
    sorted_chars = get_sorted_char_counts(char_counts)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()