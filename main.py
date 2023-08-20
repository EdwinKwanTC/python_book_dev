with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = 0
    for word in file_contents.split():
        chars = word.split()
        for char in chars:
            word_count += 1
    print(word_count)
