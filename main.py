def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = sort_dict(count_characters(text))
    print_report(book_path, num_words, num_chars)

def count_words(text):
    words = len(text.split())
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(bookText):
    chars = {}
    for c in bookText:
        lchar = c.lower()
        if lchar in chars:
            chars[lchar] += 1
        else:
            chars[lchar] = 1
    return chars

def sort_dict(dictObj):
    dictKeys = list(dictObj.keys())
    dictKeys.sort()
    alph_dict = {i: dictObj[i] for i in dictKeys}
    return alph_dict

def print_report(bookPath, wordCount, charDict):
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document \n")
    for item in charDict:
        if item.isalpha():
            print(f"The '{item}' character was found {charDict[item]} times")
    print(f"\n --- End report ---")

main()