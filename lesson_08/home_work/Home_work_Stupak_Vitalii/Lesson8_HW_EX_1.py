from collections import Counter
def count_it(sequence):
    digits = [int(digit) for digit in sequence if digit.isdigit()]
    counts = Counter(digits)
    sorted_counts = sorted(counts.items(), key=lambda item: [1], reverse=True)
    top_three = sorted_counts[:3]
    result = dict(top_three)
    return result

sequence = '1234567890'
result = count_it(sequence)
print(result)