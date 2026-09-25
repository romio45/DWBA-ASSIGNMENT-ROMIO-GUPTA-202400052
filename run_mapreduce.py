from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

mapped_records = []
with open('all_subjects_grades.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split('\t')
            if len(parts) == 3:
                mapped_records.append((f'{parts[1]}_{parts[2]}', 1))

shuffled = defaultdict(list)
for key, val in sorted(mapped_records):
    shuffled[key].append(val)

reduced_rows = []
for key, values in shuffled.items():
    subject, grade = key.rsplit('_', 1)
    reduced_rows.append({'Subject': subject, 'Grade': grade, 'Count': sum(values)})

df_grades = pd.DataFrame(reduced_rows)
df_grades.to_csv('grade_distribution_by_subject.csv', index=False)

pivot_df = df_grades.pivot(index='Subject', columns='Grade', values='Count').fillna(0)
valid_cols = [c for c in ['S', 'A', 'B', 'C', 'D', 'E', 'F'] if c in pivot_df.columns]
pivot_df = pivot_df[valid_cols]

pivot_df.plot(kind='bar', stacked=True, figsize=(11, 6), colormap='plasma')
plt.title('Student Grade Distribution across Subjects')
plt.xlabel('Subjects')
plt.ylabel('Number of Students')
plt.xticks(rotation=25)
plt.legend(title='Grades')
plt.tight_layout()
plt.savefig('grade_distribution_chart.png')
plt.close()
print('Execution complete: generated grade_distribution_by_subject.csv and grade_distribution_chart.png')