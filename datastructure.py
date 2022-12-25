from heapq import heappush, heappop

# Read the resumes into a list of strings
resumes = []
for i in range(1, 11):
    with open(f"resume ({i}).txt", "r") as f:
        resumes.append(f.read())

# Tokenize the resumes into a list of words
words = []
for resume in resumes:
    words += resume.split()

# Create a hash map to store the word counts
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Create a heap to store the word counts in sorted order
heap = []
for word, count in word_counts.items():
    heappush(heap, (count, word))

# Print the sorted word counts
while heap:
    count, word = heappop(heap)
    print(f"{word}: {count}")
