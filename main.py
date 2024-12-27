def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    sorted_list = sorted(count_dict.items())
    count_dict = dict(sorted_list)
    return count_dict

def read_frankenstein():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def main():
    text = read_frankenstein()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_characters(text)} words found in the document\n")
    characters = count_characters(text)
    for key, value in characters.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End Report ---")


main()