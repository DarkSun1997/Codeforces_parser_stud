



def get_name_student():
    file_name = 'student.txt'
    f = open(file_name, 'r')
    for line in f:
        print(line)
    f.close()
    return f
