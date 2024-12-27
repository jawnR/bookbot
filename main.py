def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(f"There are {word_count} words in the book.")     

def char_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        low_contents = file_contents.lower()
        occur = {}
        for char in set(low_contents):
            if char.isalpha():
                occur[char] = low_contents.count(char)
        list_occur = list(occur.items())
        list_occur.sort(reverse=True, key=lambda x: x[1])
        for char, count in list_occur:
            print(f"The '{char}' character was found {count} times")

char_count()