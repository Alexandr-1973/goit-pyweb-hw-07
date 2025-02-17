import argparse
from cruds.grade_crud import create_grade, list_grades, remove_grade, update_grade
from cruds.group_crud import create_group, list_groups, remove_group, update_group
from cruds.student_crud import create_student, list_students, remove_student, update_student
from cruds.subject_crud import create_subject, list_subjects, remove_subject, update_subject
from cruds.teacher_crud import create_teacher, list_teachers, remove_teacher, update_teacher

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True)
parser.add_argument("-m", "--model", choices=["Teacher", "Student", "Grade", "Subject", "Group"], required=True)
parser.add_argument("-id", type=int)
parser.add_argument("-n", "--name", type=str)
parser.add_argument("-g", "--group_id", type=int)
parser.add_argument("-t", "--teacher_id", type=int)
parser.add_argument("-s", "--student_id", type=int)
parser.add_argument("-sb", "--subject_id", type=int)
parser.add_argument("-gr", "--grade", type=int)
parser.add_argument("-d", "--grade_date")

def main():
    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create":
            if args.name:
                create_teacher(args.name)
            else:
                print("Error: Name is required to create a teacher.")
        elif args.action == "list":
            list_teachers()
        elif args.action == "update":
            if args.id and args.name:
                update_teacher(args.id, args.name)
            else:
                print("Error: ID and new name are required to update a teacher.")
        elif args.action == "remove":
            if args.id:
                remove_teacher(args.id)
            else:
                print("Error: ID is required to remove a teacher.")

    elif args.model == "Student":
        if args.action == "create":
            if args.name and args.group_id:
                create_student(args.name, args.group_id)
            else:
                print("Error: Name and group ID are required to create a student.")
        elif args.action == "list":
            list_students()
        elif args.action == "update":
            if args.id and args.name and args.group_id:
                update_student(args.id, args.name, args.group_id)
            else:
                print("Error: ID, new name, and group ID are required to update a student.")
        elif args.action == "remove":
            if args.id:
                remove_student(args.id)
            else:
                print("Error: ID is required to remove a student.")

    elif args.model == "Grade":
        if args.action == "create":
            if args.grade is not None and args.grade_date and args.student_id and args.subject_id:
                create_grade(args.grade, args.grade_date, args.student_id, args.subject_id)
            else:
                print("Error: Grade, grade_date, student_id, and subject_id are required to create a grade.")
        elif args.action == "list":
            list_grades()
        elif args.action == "update":
            if args.id and args.grade is not None and args.grade_date and args.student_id and args.subject_id:
                update_grade(args.id, args.grade, args.grade_date, args.student_id, args.subject_id)
            else:
                print("Error: ID, new grade, grade_date, student_id, and subject_id are required to update a grade.")
        elif args.action == "remove":
            if args.id:
                remove_grade(args.id)
            else:
                print("Error: ID is required to remove a grade.")

    elif args.model == "Subject":
        if args.action == "create":
            if args.name and args.teacher_id:
                create_subject(args.name, args.teacher_id)
            else:
                print("Error: Name and teacher ID are required to create a subject.")
        elif args.action == "list":
            list_subjects()
        elif args.action == "update":
            if args.id and args.name and args.teacher_id:
                update_subject(args.id, args.name, args.teacher_id)
            else:
                print("Error: ID, new name, and teacher ID are required to update a subject.")
        elif args.action == "remove":
            if args.id:
                remove_subject(args.id)
            else:
                print("Error: ID is required to remove a subject.")

    elif args.model == "Group":
        if args.action == "create":
            if args.name:
                create_group(args.name)
            else:
                print("Error: Name is required to create a group.")
        elif args.action == "list":
            list_groups()
        elif args.action == "update":
            if args.id and args.name:
                update_group(args.id, args.name)
            else:
                print("Error: ID and new name are required to update a group.")
        elif args.action == "remove":
            if args.id:
                remove_group(args.id)
            else:
                print("Error: ID is required to remove a group.")

    else:
        print("Error: Invalid model specified.")



if __name__ == "__main__":
    main()
