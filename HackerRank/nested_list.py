if __name__ == '__main__':
    list1 = []
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
    marks = []
    for each_item in sorted(list1):
        for item in each_item:
            marks.append(each_item[1])
            break

    mn = min(marks)
    while (min(marks) == mn):
        marks.remove(mn)
    sl = min(marks)
    for item in sorted(list1):
        for k in item:

            while sl in item:
                print(item[0])
                break
            break












