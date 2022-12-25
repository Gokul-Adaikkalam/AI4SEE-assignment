from abc import ABC, abstractmethod
from typing import List
from collections import Counter

class Counter(ABC):
    @abstractmethod
    def count_words(self, words: List[str]) -> Counter:
        pass

class TechnicalWordCounter(Counter):
    def count_words(self, words: List[str]) -> Counter:
        technical_words = ["python", "java", "c++", "database", "algorithm"]
        technical_word_counts = Counter()
        for word in words:
            if word.lower() in technical_words:
                technical_word_counts[word] += 1
        return technical_word_counts

class NonTechnicalWordCounter(Counter):
    def count_words(self, words: List[str]) -> Counter:
        non_technical_words = ["the", "and", "to", "a", "of"]
        non_technical_word_counts = Counter()
        for word in words:
            if word.lower() in non_technical_words:
                non_technical_word_counts[word] += 1
        return non_technical_word_counts
# Read the resumes into a list of strings
resumes = []
for i in range(1, 11):
    with open(f"resume ({i}).txt", "r") as f:
        resumes.append(f.read())

# Tokenize the resumes into a list of words
words = []
for resume in resumes:
    words += resume.split()

# Create a list of Counter objects
counters = [TechnicalWordCounter(), NonTechnicalWordCounter()]

# Call the count_words method on each object
for counter in counters:
    word_counts = counter.count_words(words)
    print(word_counts)
