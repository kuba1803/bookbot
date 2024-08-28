def character_count( text ):
    character = {}
    for c in text:
        if not c.isalpha():
            continue
        if c in character:
            character[c] += 1
        else:
            character[c] = 0
    return character



def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    words = file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("")
    characters = character_count(file_contents)
    for c in characters:
        print(f"The '{c}' character was fount {characters[c]} times")
    print("--- End report ---")


main()

