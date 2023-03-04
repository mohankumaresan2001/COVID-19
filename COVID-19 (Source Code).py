import os
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# DataBase Connection

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "covid19"
)

# ************************************************************************************************************* #

# Login Function

def Login():

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n")

    print("LOGIN TO YOUR ACCOUNT")
    print("*********************\n")

    user_name = input("Enter Your Username: ")
    password = input("Enter Your Password: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select name, user_name, password from users where user_name = %s"
    mycursor.execute(sql_query, (user_name,))
    rowcount = mycursor.rowcount

    if (rowcount == 0):
        os.system('CLS')
        print("Username Not Founded. Please Create New Account...!\n\n")
        Index()

    else:
        os.system('CLS')
        result = mycursor.fetchall()

        for i in result:
            
            name = i[0]
            db_password = i[2]

        if(password == db_password):

            os.system('CLS')
            Dashboard(name)

        else:
            os.system('CLS')
            print("Invalid Username or Password...!\n\n")
            Login()

# ************************************************************************************************************* #

# Registration Function

def Registration():

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n")

    print("CREATE NEW ACCOUNT")
    print("******************\n")

    user_name = input("Enter UserName: ")
    name = input("Enter Your Name : ")
    password = input("Enter Password: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select * from users where user_name = %s"
    mycursor.execute(sql_query, (user_name,))
    rowcount = mycursor.rowcount
        
    if (rowcount == 0):

        sql_query = "insert into users (name, user_name, password) values (%s, %s, %s)"
        value = (name, user_name, password)
        mycursor.execute(sql_query, value)

        mydb.commit()

        os.system('CLS')

        print("\nAccount Created Successfully...!\n\n")

        Index()

    else:
           
        os.system('CLS')
        print("Username is Already Taken...!\n\n")
        
        Registration()

# ************************************************************************************************************* #

# Cases Visualization

def CasesVisualization(name, case_type):

    def graph(result, mycolor, mytitle):

        count = 0
        date = []
        case_count = []
        for i in result:
            if count <= 6:
                date.append(i[0])
                case_count.append(int(i[1]))
                count = count + 1

        date.reverse()
        case_count.reverse()

        fig = plt.figure()
        fig.set_figwidth(10)

        x = np.array(date)
        y = np.array(case_count)

        plt.bar(x,y, width = 0.8, color = mycolor)

        plt.title(mytitle)
        plt.xlabel("Date")
        plt.ylabel("Cases")

        plt.show()

    result = ""
    mycolor = ""
    mytitle = ""

    mycursor = mydb.cursor(buffered = True)

    if case_type == "confirmed_cases":

        sql_query = "select date, confirmed_cases from cases_history order by id desc"
        mycursor.execute(sql_query)
        result = mycursor.fetchall()

        mycolor = "#ffa500"
        mytitle = "Confirmed Cases"
        graph(result, mycolor, mytitle)
        ConfirmedCases(name)

    elif case_type == "death_cases":

        sql_query = "select date, death_cases from cases_history order by id desc"
        mycursor.execute(sql_query)
        result = mycursor.fetchall()

        mycolor = "#ff0000"
        mytitle = "Death Cases"
        graph(result, mycolor, mytitle)
        DeathCases(name)

    elif case_type == "recovered_cases":

        sql_query = "select date, recovered_cases from cases_history order by id desc"
        mycursor.execute(sql_query)
        result = mycursor.fetchall()

        mycolor = "#228b22"
        mytitle = "Recovered Cases"
        graph(result, mycolor, mytitle)
        RecoveredCases(name)

# ************************************************************************************************************* #

# Update Today Confirmed Cases

def Update_Today_Confirmed_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("UPDATE TODAY CONFIRMED CASES")
    print("****************************\n\n")

    import datetime
    datetime = datetime.datetime.now()
    date = datetime.strftime("%d-%m-%Y")

    print("Date: ", date)

    try:

        confirmed_cases = int(input("Enter Today Confirmed Cases: "))

    except:

        os.system('CLS')
        print("Alphabets and Special Characters are not Accepted...!\n\n")
        Update_Today_Confirmed_Cases(name)

    else:

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select date, confirmed_cases from cases_history where date = %s"
        mycursor.execute(sql_query, (date,))
        rowcount = mycursor.rowcount
        
        if (rowcount == 0):

            sql_query = "insert into cases_history (date, confirmed_cases) values (%s, %s)"
            value = (date, confirmed_cases)
            mycursor.execute(sql_query, value)

            mydb.commit()

            os.system('CLS')

            print("\nToday Confirmed Cases Updated Successfully...!\n\n")

        else:

            mycursor = mydb.cursor(buffered = True)

            sql_query = "select confirmed_cases from cases_history where date = %s"
            value = (date,)
            mycursor.execute(sql_query, value)

            result = mycursor.fetchall()

            for i in result:
            
                db_confirmed_cases = i[0]

            confirmed_cases = db_confirmed_cases + confirmed_cases

            sql_query = "update cases_history set confirmed_cases = %s where date = %s"
            value = (confirmed_cases, date)
            mycursor.execute(sql_query, value)

            mydb.commit()
            
            os.system('CLS')

            print("\nToday Confirmed Cases Updated Successfully...!\n\n")

            def ConfirmedCaseChoice(name):
            
                print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
                print("\t\t\t\t**************************\n\n")

                print ("ENTER YOUR CHOICE")
                print ("*****************\n")

                print("""
                    *********************
                    *                   *
                    *  1 --> Back       *
                    *  2 --> Dashboard  *
                    *  3 --> Logout     *
                    *                   *
                    *********************\n
                    """)

                choice = input("Enter Your Choice: ")

                if(choice == "1"):

                    os.system('CLS')
                    ConfirmedCases(name)

                elif(choice == "2"):

                    os.system('CLS')
                    Dashboard(name)

                elif(choice == "3"):

                    os.system('CLS')
                    Index()

                else:
        
                    os.system('CLS')
                    print("Invalid Choice. Please try Again...!\n\n")
                    ConfirmedCaseChoice(name)

            ConfirmedCaseChoice(name)

# ************************************************************************************************************* #

# View Confirmed Cases

def View_Confirmed_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("VIEW CONFIRMED CASES")
    print("********************\n\n")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select date, confirmed_cases from cases_history order by id desc"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()

    print("\t************************************************")
    print("\t      Date                 Confirmed Cases       ")
    print("\t************************************************\n")

    for i in result:
        
        print("\t  ", i[0], "                  ", int(i[1]), "\n")

    print("\t************************************************")

    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        *********************
        *                   *
        *  1 --> Back       *
        *  2 --> Dashboard  *
        *  3 --> Logout     *
        *                   *
        *********************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        ConfirmedCases(name)

    elif(choice == "2"):

        os.system('CLS')
        Dashboard(name)

    elif(choice == "3"):

        os.system('CLS')
        Index()

    else:

        os.system('CLS')
        print("Invalid Choice. Please try Again...!\n\n")
        View_Confirmed_Cases(name)

# ************************************************************************************************************* #

# Confirmed Cases

def ConfirmedCases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ****************************************
        *                                      *
        *  1 --> Update Today Confirmed Cases  *
        *  2 --> View Confirmed Cases          *
        *  3 --> Graphical Visualization       *
        *  4 --> Back                          *
        *  5 --> Logout                        *
        *                                      *
        ****************************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        Update_Today_Confirmed_Cases(name)

    elif(choice == "2"):

        os.system('CLS')
        View_Confirmed_Cases(name)

    elif(choice == "3"):
        
        os.system('CLS')

        case_type = "confirmed_cases"
        CasesVisualization(name, case_type)

    elif(choice == "4"):
        
        os.system('CLS')
        Dashboard(name)

    elif(choice == "5"):

        os.system('CLS')
        Index()

    else:

        print("Invalid Choice. Please try Again...!\n\n")
        ConfirmedCases(name)

# ************************************************************************************************************* #

# Update Today Death Cases

def Update_Today_Death_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("UPDATE TODAY DEATH CASES")
    print("************************\n\n")

    import datetime
    datetime = datetime.datetime.now()
    date = datetime.strftime("%d-%m-%Y")

    print("Date: ", date)

    try:

        death_cases = int(input("Enter Today Death Cases: "))

    except:

        os.system('CLS')
        print("Alphabets and Special Characters are not Accepted...!\n\n")
        Update_Today_Death_Cases(name)

    else:

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select date, death_cases from cases_history where date = %s"
        mycursor.execute(sql_query, (date,))
        rowcount = mycursor.rowcount
        
        if (rowcount == 0):

            sql_query = "insert into cases_history (date, death_cases) values (%s, %s)"
            value = (date, death_cases)
            mycursor.execute(sql_query, value)

            mydb.commit()

            os.system('CLS')

            print("\nToday Death Cases Updated Successfully...!\n\n")

        else:

            mycursor = mydb.cursor(buffered = True)

            sql_query = "select death_cases from cases_history where date = %s"
            value = (date,)
            mycursor.execute(sql_query, value)

            result = mycursor.fetchall()

            for i in result:
            
                db_death_cases = i[0]

            death_cases = db_death_cases + death_cases

            sql_query = "update cases_history set death_cases = %s where date = %s"
            value = (death_cases, date)
            mycursor.execute(sql_query, value)

            mydb.commit()
            
            os.system('CLS')

            print("\nToday Death Cases Updated Successfully...!\n\n")

            def DeathCaseChoice(name):

                print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
                print("\t\t\t\t**************************\n\n")

                print ("ENTER YOUR CHOICE")
                print ("*****************\n")

                print("""
                    *********************
                    *                   *
                    *  1 --> Back       *
                    *  2 --> Dashboard  *
                    *  3 --> Logout     *
                    *                   *
                    *********************\n
                """)

                choice = input("Enter Your Choice: ")

                if(choice == "1"):

                    os.system('CLS')
                    DeathCases(name)

                elif(choice == "2"):

                    os.system('CLS')
                    Dashboard(name)

                elif(choice == "3"):
        
                    os.system('CLS')
                    Index()

                else:
                    os.system('CLS')
                    print("Invalid Choice. Please try Again...!\n\n")
                    DeathCaseChoice(name)

            DeathCaseChoice(name)

# ************************************************************************************************************* #

# View Death Cases

def View_Death_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("VIEW DEATH CASES")
    print("****************\n\n")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select date, death_cases from cases_history order by id desc"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()

    print("\t************************************************")
    print("\t      Date                    Death Cases       ")
    print("\t************************************************\n")

    for i in result:
        
        print("\t  ", i[0], "                   ", int(i[1]), "\n")

    print("\t************************************************")

    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        *********************
        *                   *
        *  1 --> Back       *
        *  2 --> Dashboard  *
        *  3 --> Logout     *
        *                   *
        *********************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        DeathCases(name)

    elif(choice == "2"):

        os.system('CLS')
        Dashboard(name)

    elif(choice == "3"):

        os.system('CLS')
        Index()

    else:

        os.system('CLS')
        print("Invalid Choice. Please try Again...!\n\n")
        View_Death_Cases(name)

# ************************************************************************************************************* #

# Death Cases

def DeathCases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ************************************
        *                                  *
        *  1 --> Update Today Death Cases  *
        *  2 --> View Death Cases          *
        *  3 --> Graphical Visualization   *
        *  4 --> Back                      *
        *  5 --> Logout                    *
        *                                  *
        ************************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        Update_Today_Death_Cases(name)

    elif(choice == "2"):

        os.system('CLS')
        View_Death_Cases(name)

    elif(choice == "3"):
        
        os.system('CLS')

        case_type = "death_cases"
        CasesVisualization(name, case_type)

    elif(choice == "4"):
        
        os.system('CLS')
        Dashboard(name)

    elif(choice == "5"):

        os.system('CLS')
        Index()

    else:

        print("Invalid Choice. Please try Again...!\n\n")
        ConfirmedCases(name)

# ************************************************************************************************************* #

# Update Today Recovered Cases

def Update_Today_Recovered_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("UPDATE TODAY RECOVERED CASES")
    print("****************************\n\n")

    import datetime
    datetime = datetime.datetime.now()
    date = datetime.strftime("%d-%m-%Y")

    print("Date: ", date)

    try:

        recovered_cases = int(input("Enter Today Recovered Cases: "))

    except:

        os.system('CLS')
        print("Alphabets and Special Characters are not Accepted...!\n\n")
        Update_Today_Recovered_Cases(name)

    else:

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select date, recovered_cases from cases_history where date = %s"
        mycursor.execute(sql_query, (date,))
        rowcount = mycursor.rowcount
        
        if (rowcount == 0):

            sql_query = "insert into cases_history (date, recovered_cases) values (%s, %s)"
            value = (date, recovered_cases)
            mycursor.execute(sql_query, value)

            mydb.commit()

            os.system('CLS')

            print("\nToday Recovered Cases Updated Successfully...!\n\n")

        else:

            mycursor = mydb.cursor(buffered = True)

            sql_query = "select recovered_cases from cases_history where date = %s"
            value = (date,)
            mycursor.execute(sql_query, value)

            result = mycursor.fetchall()

            for i in result:
            
                db_recovered_cases = i[0]

            recovered_cases = db_recovered_cases + recovered_cases

            sql_query = "update cases_history set recovered_cases = %s where date = %s"
            value = (recovered_cases, date)
            mycursor.execute(sql_query, value)

            mydb.commit()
            
            os.system('CLS')

            print("\nToday Recovered Cases Updated Successfully...!\n\n")

            def RecoveredCaseChoice(name):

                print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
                print("\t\t\t\t**************************\n\n")

                print ("ENTER YOUR CHOICE")
                print ("*****************\n")

                print("""
                    *********************
                    *                   *
                    *  1 --> Back       *
                    *  2 --> Dashboard  *
                    *  3 --> Logout     *
                    *                   *
                    *********************\n
                """)

                choice = input("Enter Your Choice: ")

                if(choice == "1"):

                    os.system('CLS')
                    RecoveredCases(name)

                elif(choice == "2"):

                    os.system('CLS')
                    Dashboard(name)

                elif(choice == "3"):
        
                    os.system('CLS')
                    Index()

                else:
                    os.system('CLS')
                    print("Invalid Choice. Please try Again...!\n\n")
                    RecoveredCaseChoice(name)

            RecoveredCaseChoice(name)

# ************************************************************************************************************* #

# View Death Cases

def View_Recovered_Cases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print("VIEW RECOVERED CASES")
    print("********************\n\n")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select date, recovered_cases from cases_history order by id desc"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()

    print("\t************************************************")
    print("\t      Date                Recovered Cases       ")
    print("\t************************************************\n")

    for i in result:
        
        print("\t  ", i[0], "                ", int(i[1]), "\n")

    print("\t************************************************")

    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        *********************
        *                   *
        *  1 --> Back       *
        *  2 --> Dashboard  *
        *  3 --> Logout     *
        *                   *
        *********************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        RecoveredCases(name)

    elif(choice == "2"):

        os.system('CLS')
        Dashboard(name)

    elif(choice == "3"):

        os.system('CLS')
        Index()

    else:

        os.system('CLS')
        print("Invalid Choice. Please try Again...!\n\n")
        View_Death_Cases(name)

# ************************************************************************************************************* #

# Recovered Cases

def RecoveredCases(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ****************************************
        *                                      *
        *  1 --> Update Today Recovered Cases  *
        *  2 --> View Recovered Cases          *
        *  3 --> Graphical Visualization       *
        *  4 --> Back                          *
        *  5 --> Logout                        *
        *                                      *
        ****************************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        Update_Today_Recovered_Cases(name)

    elif(choice == "2"):

        os.system('CLS')
        View_Recovered_Cases(name)

    elif(choice == "3"):
        
        os.system('CLS')

        case_type = "recovered_cases"
        CasesVisualization(name, case_type)

    elif(choice == "4"):
        
        os.system('CLS')
        Dashboard(name)

    elif(choice == "5"):

        os.system('CLS')
        Index()

    else:

        print("Invalid Choice. Please try Again...!\n\n")
        RecoveredCases(name)

# ************************************************************************************************************* #

# Dashboard Function

def Dashboard(name):

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    import datetime
    datetime = datetime.datetime.now()
    date = datetime.strftime("%d-%m-%Y")

    print("Welcome ", name , "\t\t\t\t\t\t\t\tDate: ", date, "\n\n")

    mycursor = mydb.cursor(buffered = True)
    
    sql_query = "select confirmed_cases, death_cases, recovered_cases from cases_history"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()

    c_count, d_count, r_count = 0, 0, 0

    for i in result:
        
        c_count = c_count + i[0]
        d_count = d_count + i[1]
        r_count = r_count + i[2]

    active_cases = c_count - (d_count + r_count)


    print("""
                **************************************************
                           TOTAL                CASES COUNT       
                **************************************************\n
                   CONFIRMED CASES                """,int(c_count),"""\n
                   DEATH CASES                    """,int(d_count),"""\n
                   RECOVERED CASES                """,int(r_count),"""\n
                   ACTIVE CASES                   """,int(active_cases),"""\n
                **************************************************
    """)

    def DashboardVisualization(d_cases, r_cases, a_cases, name):

        cases = np.array([d_cases, r_cases, a_cases])
        mylabels = ["Death Cases", "Recovered Cases", "Active Cases"]
        mycolors = ["#ff0000", "#228b22", "#ffa500"]

        fig = plt.figure()
        fig.set_figwidth(8)

        plt.title("COVID - 19 Cases Report \n")

        plt.pie(cases, labels = mylabels, colors = mycolors, startangle = 90)
        plt.legend(bbox_to_anchor = (1.02, 0.1), loc = "upper left", borderaxespad = 0)

        plt.show()

        os.system('CLS')
        Dashboard(name)

    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ****************************************
        *                                      *
        *  1 --> Confirmed Cases               *
        *  2 --> Death Cases                   *
        *  3 --> Recovered Cases               *
        *  4 --> Graphical Visualization       *
        *  5 --> Logout                        *
        *                                      *
        ****************************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):

        os.system('CLS')
        ConfirmedCases(name)

    elif(choice == "2"):

        os.system('CLS')
        DeathCases(name)

    elif(choice == "3"):
        
        os.system('CLS')
        RecoveredCases(name)

    elif(choice == "4"):
        os.system('CLS')
        DashboardVisualization(d_count, r_count, active_cases, name)

    elif(choice == "5"):

        os.system('CLS')
        Index()

    else:

        print("Invalid Choice. Please try Again...!\n\n")
        Dashboard(name)

# ************************************************************************************************************* #

# Index Function 

def Index():

    print("\t\t\t\tCOVID-19 MANAGEMENT SYSTEM")
    print("\t\t\t\t**************************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ***************************
        *                         *
        * 1--> Login              *
        * 2--> Create New Account *
        *                         *
        ***************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):
        os.system("CLS")
        Login()

    elif(choice == "2"):
        os.system("CLS")
        Registration()

    else:
        print("Invalid Choice. Please try Again...!\n\n")
        Index()

# ************************************************************************************************************* #

os.system("CLS")

Index()