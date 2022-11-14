



def get_name_student():
    file_name = 'student.txt'
    file_stud = open(file_name, 'r')
    Name_stud_loc = []
    for line in file_stud:
        Name_stud_loc.append(line[0:len(line)-1])
    file_stud.close()
    return Name_stud_loc
