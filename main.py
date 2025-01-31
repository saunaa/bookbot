def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    num_char = count_char(text)
    num_char_print = print_count(num_char)

    

def count_words(text):
        words = text.split()
        count = len(words)
        return count

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_char(text):
    count = {}
    for char in text:
        lc = char.lower()
        if lc not in count:
            count[lc] = 0
        count[lc] +=1
    return dict(sorted(count.items()))
        
def print_count(dict):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in dict:
        if letter in alphabet:
            print(f"The '{letter}' character was found {dict[letter]} times")
     

     

main()

