def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_letter_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print_letter_count(chars)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def print_letter_count(chars):
    chars = dict(sorted(chars.items()))
    for char, count in chars.items():
        if char.isalpha(): 
            print(f"The {char} character was found {count} times")


main()
