

file_contents = None

with open("./book/frankenstein.txt") as f:
    file_contents = f.read()


print(file_contents)

words = file_contents.split()
print(len(words))

counter = {}
for word in words:
    for l in word:
        l = l.lower()
        if l in counter:
            counter[l] = counter[l] + 1
        else:
            counter[l] = 1

print(counter)

letter_list = list(counter.items())
letter_list.sort()

for l in letter_list:
    if l[0].isalpha():
        print(f"The '{l[0]}' character was found {l[1]} times")
