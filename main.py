from stats import get_file_contents, get_num_words, get_num_char, sort_dict
import sys

def print_stats():
    filepath = sys.argv[1]
    text = get_file_contents(filepath)
    num_words = get_num_words(text)
    char_dict = get_num_char(text)
    list_dict = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count_dict in list_dict:
        print(f"{count_dict['char']}: {count_dict['count']}")
    print("============= END ===============")

def less_than_two_args():
    print("Usage: python3 main.py <path_to_book>")
    return sys.exit(1)

def main():
    if len(sys.argv) < 2:
        less_than_two_args()
    else:
        print_stats()

main()
