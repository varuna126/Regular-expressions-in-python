# Author: Varuna Dharmadasa
# Date: Thursday 22 November 2018


import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))

# Note, .match only looks tries to match with the beginning of the string.
# To search through a whole string, use .search

#print(re.search(r'Kenneth', data))

print()
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
print()
print(re.findall(r'\w*, \w+', data))
print()
print(re.findall(r'[-\w\d.+]+@[-\w\d.]+', data))
print()


