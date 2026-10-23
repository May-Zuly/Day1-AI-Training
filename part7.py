def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

scores = [45, 70, 85, 30, 90, 55]
result = calculate_average(scores)
print(f"Average: {result}")