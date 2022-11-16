from collections import Counter

word = "commando"
# Get the frequency of a character
print(word.count('o'))

words = ['rat', 'cat', 'dog', 'cat', 'mouse', 'dog', 'cat', 'deer']
# Get the frequency of a list element
print(words.count('dog'))

# To get rid of duplicates, use a dictionary
counts = {}
# Loop through the list and update the dictionary
for i in animals:
  num = animals.count(i)
  counts.update({i: num})

print(counts)

# Sort by key
sorted_keys = sorted(counts.items())
print("Sorted by Key: ", sorted_keys)

# Sort by value
sorted_values = 
  sorted(counts.items(), key=lambda item: item[1], reverse=True)
print("Sorted by Values: ", sorted_values)

# Use Counter from Collections
counter = Counter(counts)
# Print the two most common words in the counts
print(counter.most_common(2))


# Open a file
with open('excerpt.txt', 'r', encoding='utf8') as f:
  text = f.read()

# Turn the file into a list of words
text = text.split()
# Initialize the counter
counter = Counter(text)
# Loop through the 10 most common words and print them
for i,j in counter.most_common(10):
  print(i,"--->",j)
