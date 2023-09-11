from collections import defaultdict, Counter


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
freq = defaultdict(int)
for string in words:
    for character in string:
        freq[character.lower()] += 1

print("--- Begin report of books/frankenstein.txt ---")

print("Total Words: ", len(words))
print(dict(freq))
print()

alphabet_counts = Counter(file_contents.lower())
sorted_counts = sorted(alphabet_counts.items(), key=lambda item: item[1], reverse=True)

for letter, count in sorted_counts:
    if letter.isalpha():
        print(f"The '{letter}' character was found {count} times")


print("--- End report ---")

