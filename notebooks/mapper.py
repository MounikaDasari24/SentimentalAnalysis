import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Counts: total, TP, TN, FP, FN, neutral, non-neutral, correct
for line in sys.stdin:
    line = line.rstrip("\n")

    if not line:
        continue

    try:
        actual_text, tweet = line.split("\t", 1)
        actual = int(actual_text)

        if actual not in (0, 1):
            continue

        compound = analyzer.polarity_scores(tweet)["compound"]

        if compound >= 0.05:
            predicted = 1
        elif compound <= -0.05:
            predicted = 0
        else:
            predicted = 2  # Neutral

        total = 1
        tp = int(actual == 1 and predicted == 1)
        tn = int(actual == 0 and predicted == 0)
        fp = int(actual == 0 and predicted == 1)
        fn = int(actual == 1 and predicted == 0)
        neutral = int(predicted == 2)
        non_neutral = int(predicted != 2)
        correct = int(predicted == actual)

        values = [
            total, tp, tn, fp, fn,
            neutral, non_neutral, correct
        ]

        print("ALL\t" + ",".join(map(str, values)))

    except (ValueError, IndexError):
        continue
