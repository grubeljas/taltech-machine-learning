import csv

with open("bbc_train.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for topic, text in rd:
        # lowercase tokens longer than 3 chars
        words = [w.lower() for w in text.split() if len(w) > 3]
        # store topic and words somewhere
