# Counter = say you want to count the most common words in a text.

# splits a text into a list into separate elements
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()

# diplay elements from 0 to 4 (excludes 5)
print(words[:5])

common_words = {}
# populates the dictionary with words and their most common occurance
for word in words:
    if word not in common_words:
        common_words[word]=0
    common_words[word]+=1
# sort dict by values descending and slice first 5 values to get most common
for k,v in sorted(common_words.items(),
                  key=lambda x:x[1],
                  reverse=True)[:5]:
    print(k,v)

# using counter

from collections import Counter

print(Counter(words).most_common(5))