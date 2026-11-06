import sys

totals = [0] * 8

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values_text = line.split("\t", 1)
        values = list(map(int, values_text.split(",")))

        if len(values) != 8:
            continue

        totals = [
            a + b for a, b in zip(totals, values)
        ]

    except ValueError:
        continue

total, tp, tn, fp, fn, neutral, non_neutral, correct = totals

def safe_divide(a, b):
    return a / b if b else 0.0

binary_accuracy = safe_divide(correct, non_neutral)
precision = safe_divide(tp, tp + fp)
recall = safe_divide(tp, tp + fn)
f1 = safe_divide(2 * precision * recall, precision + recall)
overall_accuracy = safe_divide(correct, total)

print("Metric\tValue")
print(f"Total tweets\t{total}")
print(f"True positives\t{tp}")
print(f"True negatives\t{tn}")
print(f"False positives\t{fp}")
print(f"False negatives\t{fn}")
print(f"Neutral predictions\t{neutral}")
print(f"Accuracy among non-neutral\t{binary_accuracy:.6f}")
print(f"Overall accuracy (neutral incorrect)\t{overall_accuracy:.6f}")
print(f"Precision\t{precision:.6f}")
print(f"Recall\t{recall:.6f}")
print(f"F1-score\t{f1:.6f}")
