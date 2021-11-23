import csv, time
from math import log10

unique = set()
topic_frequency = {}
word_frequency = {}
word_counter = {}
n = 0

with open("bbc_train.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for topic, text in rd:
        n += 1
        # lowercase tokens longer than 3 chars
        words = [w.lower() for w in text.split() if len(w) > 3]

        unique.union(set(unique))

        if not topic_frequency.get(topic):
            topic_frequency[topic] = 0
        topic_frequency[topic] += 1

        if not word_counter.get(topic):
            word_counter[topic] = 0
        word_counter[topic] += len(words)

        if not word_frequency.get(topic):
            word_frequency[topic] = {}
        for word in words:
            if not word_frequency[topic].get(word):
                word_frequency[topic][word] = 0
            word_frequency[topic][word] += 1

tic = time.perf_counter()
with open("bbc_test.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    error = 0
    ok = 0
    for topic, text in rd:
        words = [w.lower() for w in text.split() if len(w) > 3]

        suggestions = {}

        for suggested_topic in topic_frequency.keys():
            probability = log10(topic_frequency[suggested_topic]/n)

            for word in words:
                formula = 0
                if word in word_frequency[suggested_topic].keys():
                    formula = (word_frequency[suggested_topic][word] + 1)/(word_counter[suggested_topic] + len(unique))
                else:
                    formula = 1/(word_counter[suggested_topic] + len(unique))
                probability += log10(formula)

            suggestions[suggested_topic] = probability

        maximal = float('-inf')
        topic_answer = ''
        for suggestion, probability in suggestions.items():
            if probability > maximal:
                maximal = probability
                topic_answer = suggestion

        if topic != topic_answer:
            error += 1

    print(error)
