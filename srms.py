def main():
    print("""STUDENT RESULT MANAGEMENT SYSTEM
    =======================================================
    1. ENTER STUDENT DETAILS
    2. FETCH ALL THE STUDENT DETAILS
    3. INPUT STUDENT MARKS
    4. UPDATE STUDENT DETAILS
    5. DISPLAY CLASSWISE TOPPER
    6. DISPLAY AVERAGE CLASSWISE MARKS
    7. EXIT""")
    c = int(input("Enter choice: "))
    if c == 1:
        ad()
        main()
    elif c == 2:
        s()
        main()
    elif c == 3:
        marks()
        main()
    elif c == 4:
        studetail()
        main()
    elif c == 5:
        top()
        main()
    elif c == 6:
        avg()
        main()
    elif c == 7:
        exit()
    else:
        print("Invalid Input")

def ad():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    choice = "Y"
    while choice.upper() == "Y":
        a = int(input("Enter admission number: "))
        name = input("Enter name of the student: ")
        clas = int(input("Enter class: "))
        st = "Insert into detail(admn_num, name, class) Values({}, '{}', {})".format(a, name, clas)
        cursor.execute(st)
        cur.commit()
        choice = input("Would you like to continue adding more student details? (Y/N): ").upper()

def s():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    cursor.execute("select * from detail")
    data = cursor.fetchall()
    count = cursor.rowcount
    print("No of records:", count)
    print("{:<14}{:<22}{:>15}".format("ADMN_NUM", "NAME", "CLASS"))
    for ele1, ele2, ele3 in data:
        print("{:<14}{:<22}{:>15}".format(ele1, ele2, ele3))

def marks():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    choice = "Y"
    s = "select m.admn_num, d.name, d.class from detail d, marks m where d.admn_num = m.admn_num"
    cursor.execute(s)
    data = cursor.fetchall()
    print("The marks of following students are already entered:")
    print("{:<14}{:<22}{:>15}".format("ADMN_NUM", "NAME", "CLASS"))
    for a, b, c in data:
        print("{:<14}{:<22}{:>15}".format(a, b, c))
    print("==============================")
    print("INPUT MARKS:")

    while choice.upper() == "Y":
        a = int(input("Enter admission number: "))
        phy = int(input("Enter physics marks: "))
        english = int(input("Enter English marks: "))
        com = int(input("Enter CS marks: "))
        chem = int(input("Enter chemistry marks: "))
        maths = int(input("Enter maths marks: "))
        total = phy + chem + maths + english + com
        st = "Insert into marks(admn_num, physics, chemistry, maths, english, computer_sci, total) Values({}, {}, {}, {}, {}, {}, {})".format(
            a, phy, chem, maths, english, com, total)
        cursor.execute(st)
        cur.commit()
        choice = input("Would you like to continue adding more marks? (Y/N): ").upper()

def studetail():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    choice = "Y"
    while choice.upper() in ["Y", "YES"]:
        a = int(input("Enter admission number: "))
        s = "select * from detail where admn_num = {}".format(a)
        cursor.execute(s)
        data = cursor.fetchall()
        for ele1, ele2, ele3 in data:
            print("{:<14}{:<13}{:>15}".format("ADMN_NUM", "NAME", "CLASS"))
            print("{:<14}{:<13}{:>15}".format(ele1, ele2, ele3))
        print("========================================================")

        b = int(input("Type\n1 for updating student's name\n2 for updating class\n"))
        if b == 1:
            nm = input("Enter new name: ")
            sc = "update detail set name = '{}' where admn_num = {}".format(nm, a)
            cursor.execute(sc)
            cur.commit()
            print("Updation successful")
        elif b == 2:
            clss = int(input("Enter new class: "))
            sc = "update detail set class = {} where admn_num = {}".format(clss, a)
            cursor.execute(sc)
            cur.commit()
            print("Updation successful")
        choice = input("Would you like to continue? (Y/N): ").upper()

def top():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    s = '''select d.admn_num, d.name, d.class, max(total), max(total)/5
           from detail d, marks m
           where d.admn_num = m.admn_num
           group by class'''
    cursor.execute(s)
    data = cursor.fetchall()
    print("{:<14}{:<15}{:<19}{:>15}{:>15}".format("ADMN_NUM", "NAME", "CLASS", "TOTAL", "PERCENTAGE"))
    for a, b, c, d, e in data:
        print("{:<14}{:<15}{:<19}{:>15}{:>15}".format(a, b, c, d, str(e) + "%"))

def avg():
    import mysql.connector as a
    cur = a.connect(host="localhost", user="root", passwd="pw", charset="utf8", database="school")
    cursor = cur.cursor()
    s = '''select class, avg(total) from marks group by class'''
    cursor.execute(s)
    data = cursor.fetchall()
    print("{:<14}{:>15}".format("CLASS", "AVERAGE"))
    for a, b in data:
        print("{:<14}{:>15}".format(a, b))

def exit():
    print("You have successfully exited!")

main()
