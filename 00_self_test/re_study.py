import re

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0

for word in string_list:
    if pattern.search(word):
        count += 1
print ("Output #38:{0:d}".format(count))

