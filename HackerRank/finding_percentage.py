n = int(input('n'))
student_marks = {}
for i in range(n):
    name, *line = input('name').split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input('query name')
list_marks = list(student_marks.get(query_name))
total=0
for i in (list_marks):

    total += i
print(total)
percentage = total/3
print(percentage)
print("{:.2f}".format(total / 3))


