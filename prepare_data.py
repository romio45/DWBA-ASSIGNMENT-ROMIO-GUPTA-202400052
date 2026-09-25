import random
subjects = [
    'Machine_Learning', 'Cloud_Computing', 'Data_Mining',
    'Artificial_Intelligence', 'Compiler_Design', 'Distributed_Systems'
]
grades = ['S', 'A', 'B', 'C', 'D', 'E', 'F']
grade_weights = [0.12, 0.22, 0.26, 0.18, 0.10, 0.07, 0.05]
random.seed(202400052)
with open('all_subjects_grades.txt', 'w') as f:
    for student_id in range(1, 161):
        for sub in subjects:
            assigned_grade = random.choices(grades, weights=grade_weights, k=1)[0]
            f.write(f'{student_id}\t{sub}\t{assigned_grade}\n')
print('Generated all_subjects_grades.txt successfully.')