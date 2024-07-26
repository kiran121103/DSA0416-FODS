import numpy as np

# Sample data: 10 students, 4 subjects (Math, Science, English, History)
student_scores = np.array([
    [85, 78, 92, 88],
    [79, 85, 91, 90],
    [90, 88, 94, 92],
    [82, 77, 85, 80],
    [88, 90, 91, 89],
    [91, 87, 88, 85],
    [84, 85, 89, 90],
    [78, 83, 86, 82],
    [89, 90, 93, 94],
    [85, 80, 87, 88]
])

# Calculate the average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Identify the subject with the highest average score
highest_average_score_index = np.argmax(average_scores)
subjects = ['Math', 'Science', 'English', 'History']
highest_average_subject = subjects[highest_average_score_index]

# Print the average scores and the subject with the highest average score
print("Average Scores for Each Subject:", average_scores)
print("Subject with the Highest Average Score:", highest_average_subject)
