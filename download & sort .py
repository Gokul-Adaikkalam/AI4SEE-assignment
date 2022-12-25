import urllib.request
import zipfile

# Download the zip file from the link
url = "https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset"
urllib.request.urlretrieve(url, "resumes.zip")

# Extract the contents of the zip file
with zipfile.ZipFile("resumes.zip", "r") as zip_ref:
    zip_ref.extractall(".")
from collections import Counter

# Read the resumes into a list of strings
resumes = []
for i in range(1, 11):
    with open(f"resume ({i}).txt", "r") as f:
        resumes.append(f.read())

# Tokenize the resumes into a list of words
words = []
for resume in resumes:
    words += resume.split()

# Count the occurrences of each word
word_counts = Counter(words)

# Sort the word counts in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sorted word counts
for word, count in sorted_word_counts:
    print(f"{word}: {count}")
