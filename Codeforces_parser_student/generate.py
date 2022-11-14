#Библиотеки
import os


def get_name_student():
    file_name = 'student.txt'
    file_stud = open(file_name, 'r')
    Name_stud_loc = []
    for line in file_stud:
        Name_stud_loc.append(line[0:len(line)-1])
    file_stud.close()
    return Name_stud_loc


def get_name_contest():
    file_name = 'contest.txt'
    file_contest = open(file_name, 'r')
    Name_contest_loc = []
    for line in file_contest:
        Name_contest_loc.append(line[0:len(line)-1])
    file_contest.close()
    return Name_contest_loc


def generate_folder_stud():
    name_base_folder = 'stud_work'
    name_folder = name_base_folder
    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)
    list_name_stud = get_name_student()
    for name_stud in list_name_stud:
        name_folder = name_base_folder + '/'+ name_stud
        if not os.path.isdir(name_folder):
            os.mkdir(name_folder)
        list_name_contest = get_name_contest()
        for name_contest in list_name_contest:
            name_folder = name_base_folder + '/' + name_stud + '/' + name_contest
            if not os.path.isdir(name_folder):
                os.mkdir(name_folder)