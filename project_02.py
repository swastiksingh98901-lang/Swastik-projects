# Create a list called test_scores with at least 10 numerical grades (0-100)
test_scores = [85, 92, 78, 88, 95, 67, 73, 89, 91, 84, 76, 90]

# Find and display the highest and lowest scores
highest = max(test_scores)
lowest = min(test_scores)
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")

# Calculate and display the average score
average = sum(test_scores) / len(test_scores)
print(f"Average score: {average:.2f}")

# Count how many students scored above 80
above_80 = sum(1 for score in test_scores if score > 80)
print(f"Number of students above 80: {above_80}")

# Create a new list containing only the scores above the average
above_average = [score for score in test_scores if score > average]
print(f"Scores above average: {above_average}") 

# Sort the scores in descending order and display the top 3 scores
sorted_scores = sorted(test_scores, reverse=True)
top_3 = sorted_scores[:3]
print(f"Top 3 scores: {top_3}")

# Bonus: Determine letter grades and count each grade type
# A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for score in test_scores:
    if score >= 90:
        grades['A'] += 1
    elif score >= 80:
        grades['B'] += 1
    elif score >= 70:
        grades['C'] += 1
    elif score >= 60:
        grades['D'] += 1
    else:
        grades['F'] += 1

print("Grade counts:")
for grade, count in grades.items():
    print(f"  {grade}: {count}")