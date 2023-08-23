with open("books/frankenstein.txt") as f:
    result = {}
    file_contents = f.read()
    word_count = 0
    for words in file_contents.split():
        chars = words.lower().split()[0]
        for char in chars:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
            word_count += 1
    print(word_count)
    print(result)