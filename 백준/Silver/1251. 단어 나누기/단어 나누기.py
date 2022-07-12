word = input()
word_list = []

for i in range(1, len(word) - 2):
    part1 = word[0:i]
    for j in range(i + 1, len(word)):
        part2 = word[i:j]
        part3 = word[j:]
        word_list.append(''.join(reversed(part1)) + ''.join(reversed(part2)) + ''.join(reversed(part3)))

print(sorted(word_list)[0])