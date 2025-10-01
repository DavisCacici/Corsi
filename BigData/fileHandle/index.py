f = open("student_exam_scores.csv", "rt")
# print(f.readlines())
student_id = []
hours_studied = []
sleep_hours = []
attendance_percent = []
previous_scores = []
exam_score = []
for i in f.readlines():
    element = i.split(",")
    # print(element)
    student_id.append(element[0])
    hours_studied.append(element[1])
    sleep_hours.append(element[2])
    attendance_percent.append(element[3])
    previous_scores.append(element[4])
    exam_score.append(element[5])

print(student_id)
print(hours_studied)
print(sleep_hours)
print(attendance_percent)
print(previous_scores)
print(exam_score)

f.close()