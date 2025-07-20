print("This is the student portal.\nTo [E]xit.")
student_info = {

}


def take_info():
    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            id = input("Enter your ID number: ")
            courses = input("Enter the courses(comma-spearated): ")
            courses = set(courses.strip().replace(" ", "").title().split(","))
            return name, age, id, courses
        except ValueError:
            print("Please enter correct info type.")


while True:
    action = input(
        "\nWhat do you want to do? \n1-Register\n2-Unregister\n3-View\n ")
    if action.lower() == "e":
        break
    elif action == "1":
        name, age, id, courses = take_info()
        personal_info = {"Name: ": name.title(), "Age:": age}
        number_of_courses = len(courses)
        student_info[id] = {
            "Personal Info:": personal_info,
            "Courses": courses,
            "Number of Courses": number_of_courses
        }
        print(f"Student {name} registered succesfully.\n")
        print(student_info)

    elif action == "2":
        unregister = input(
            "1-From whole database\n2-Specific courses\n3-All courses\n ")
        if unregister == "1":
            id = input("Enter your ID number: ")
            if id in student_info:
                unregistered = student_info.pop(id)
                print(f"You have been unregistered completely: {id}")
            else:
                print("Id not registered.")
        elif unregister == "2":
            id = input("Enter your ID number: ")
            if id in student_info:
                courses_to_unregister = input("Which courses: ")
                courses_to_unregister = set(
                    courses_to_unregister.title().strip().replace(" ", "").split(","))
                student_info[id]["Courses"].difference_update(
                    courses_to_unregister)
                print("You have been unregistered from those courses.")
                print(student_info)
            else:
                print("ID does not exist.")
        elif unregister == "3":
            id = input("Enter your ID number: ")
            if id in student_info:
                student_info[id]["Courses"].clear()
                print("You have been unregistered from all courses.")
                print(student_info)
            else:
                print("ID does not exist.")
    elif action == "3":
        view_option = input(
            "1-View one student\n2-View all students\n3-View all courses\n")
        if view_option == "1":
            id = input("Enter your ID number: ")
            if id in student_info:
                print("Here is your info: ")
                print(student_info[id])
            else:
                print("ID not registered.")
        elif view_option == "2":
            print("All student Records:")
            for id, info in student_info.items():
                print(f"{id}, {info}")
        elif view_option == "3":
            id = input("Enter your ID number: ")
            if id in student_info:
                print(student_info[id]["Courses"])
            else:
                print("ID not registered.")
    else:
        print("Please enter correct action.")
