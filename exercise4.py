scores = [45, 70, 85, 30, 90, 55]
def calculate_total(scores):
    return sum(scores)

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def classify_grade(scores):
    if scores < 0 or scores > 100:
        return "Invalid"
    elif scores >= 80:
        return "A"
    elif scores >= 60:
        return "B"
    elif scores >= 40:
        return "C"
    else:
        return "Fail"

def count_pass(scores):
    pass_count = 0
    fail_count = 0
    for score in scores:
        if score >= 40:
            pass_count += 1
        else:
            fail_count += 1
    return pass_count
print("Total:", calculate_total(scores))
print("Average:", calculate_average(scores))
print("Grade Classification :")
for score in scores:
    print(f"Score: {score}, Grade: {classify_grade(score)}")
print(f"Pass Count: {count_pass(scores)}")
