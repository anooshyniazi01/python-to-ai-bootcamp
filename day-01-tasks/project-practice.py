def analyze(marks):
    total = sum(marks)
    avg = total / len(marks)
    if avg > 85:
        print("Outstanding")
    elif avg > 70:
        print("Good")
    elif avg > 50:
        print("Average")
    else:
        print("Fail")
    for i in range(len(marks)):
        print("Mark:", marks[i])
    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))
    print("Total:", total)
    print("Average:", round(avg, 2))
marks = [65, 90, 75, 40, 85]
analyze(marks)
