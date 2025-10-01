"""
Modifica l'esercizio precedente nel file index.py
creando una lista di dictionary piuttosto che avere 
tante liste separate
"""

f = open("student_exam_scores.csv", "rt")
# print(f.readlines())
data_array = []
data = {}
for i in f.readlines():
    element = i.split(",")
    # print(element)
    data['student_id'] = element[0]
    data['hours_studied'] = element[0]
    data['sleep_hours'] = element[0]
    data['attendace_percent'] = element[0]
    data['previous_scores'] = element[0]
    data['exam_score'] = element[0]
        
    data_array.append(data.copy())
print(data_array)

f.close()