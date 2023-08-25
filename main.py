with open("books/frankenstein.txt") as f:
    result = {}
    file_contents = f.read()
    word_count = 0
    for words in file_contents.split():
        chars = words.lower().split()
        for char in chars:
            word_count += 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    alpha = [chr(i) for i in range(ord("a"), ord("z") + 1)]

    for words in file_contents.split():
        chars = words.lower().split()[0]
        for char in chars:
            if char in alpha:
                if char in result:
                    result[char] += 1
                else:
                    result[char] = 1

    alphaArray = []
    for key, value in result.items():
        alphaArray.append({"letter": key, "count": value})

    def get_count(alpha):
        return alpha.get("count")

    alphaArray.sort(key=get_count, reverse=True)

    for a in alphaArray:
        thisLetter = a["letter"]
        thisCount = a["count"]
        print(f"The '{thisLetter}' character was found {thisCount} times")

    print("--- End report ---")
