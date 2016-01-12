import re

test_string = 'Lorem ipsum dolor sit amet Consectetur adipisicing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad'


# The re.search() returns a True / False depending on whether the string matches the regex.
list_of_words = test_string.split(" ")
for word in list_of_words:
    if re.search('^i', word):
        print(word)

# re.findall() extracts all the matching strings.
list_of_extracted_words = re.findall('ci([^ ]*)', test_string)
print(list_of_extracted_words)

