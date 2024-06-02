import random
import mysql.connector

mysqldb = mysql.connector.connect(user='root', password='123456', host='localhost', database='project')
mycursor = mysqldb.cursor()

#-------------------------------- Menu -----------------------------
def MENU():
    while True:
        print()
        print("-----------------------------------------------")
        print("---- Welcome to Railway Reservation System ----")
        print("-----------------------------------------------")
        print(" 1. Train Search ")
        print(" 2. Train Information ")
        print(" 3. Ticket Booking ")
        print(" 4. PNR Status ")
        print(" 5. Ticket Cancellation ")
        print(" 6. Admin ")
        print(" 7. Exit ")
        print("-----------------------------------------------")
        print()
        choice = int(input("Enter your Choice (1-7) : "))
        if choice == 1:
            TrainSearch()
        elif choice == 2:
            TrainInformation()
        elif choice == 3:
            TicketBooking()
        elif choice == 4:
            PNRStatus()
        elif choice == 5:
            TicketCancellation()
        elif choice == 6:
            Admin()
        elif choice == 7:
            break
        else:
            print("Error : Invalid choice, Please try again")
        conti = input("Please press any key to continue...")

#-------------------------------- Train Search -----------------------------
def TrainSearch():
    while True:
        print()
        print("-----------------------------------------------")
        print("----------- Welcome to Train Search -----------")
        print("-----------------------------------------------")
        print(" 1. Train Search by Train Number ")
        print(" 2. Train Search by Train Name ")
        print(" 3. Train Search by Source Station ")
        print(" 4. Train Search by Destination Station")
        print(" 5. Go back to main menu ")
        print(" 6. Exit ")
        print("-----------------------------------------------")
        print()
        choice = int(input("Enter your Choice (1-4) : "))
        print()
        if choice == 1:
            train_Number = int(input("Please enter Train number : "))
            mycursor.execute('SELECT * FROM Train WHERE Train_No = %d' % (train_Number))
            result = mycursor.fetchall()
            print()
            print("-----------------------------------------------------------------------------")
            print("Train No\t Train Name\t\t\t Source\t\t\t Destination")
            print("-----------------------------------------------------------------------------")
            for index, i in enumerate(result):
                Train_No = i[0]
                Train_Name = i[1]
                Train_Source = i[2]
                Train_Destination = i[3]
                print(f"{index}. {Train_No}\t\t {Train_Name}\t {Train_Source}\t\t\t {Train_Destination}")
        elif choice == 2:
            train_Name = input("Please enter Train Name : ")
            mycursor.execute("""SELECT * FROM Train WHERE Train_Name = %s""", (train_Name,))
            result = mycursor.fetchall()
            print()
            print("-----------------------------------------------------------------------------")
            print("Train No\t Train Name\t\t\t Source\t\t\t Destination")
            print("-----------------------------------------------------------------------------")
            for index, i in enumerate(result):
                Train_No = i[0]
                Train_Name = i[1]
                Train_Source = i[2]
                Train_Destination = i[3]
                print(f"{index}. {Train_No}\t\t {Train_Name}\t {Train_Source}\t\t\t {Train_Destination}")
        elif choice == 3:
            source_Station = input("Please enter Train Source station : ")
            mycursor.execute("""SELECT * FROM Train WHERE Train_Source = %s""", (source_Station,))
            result = mycursor.fetchall()
            print()
            print("-----------------------------------------------------------------------------")
            print("Train No\t Train Name\t\t\t Source\t\t\t Destination")
            print("-----------------------------------------------------------------------------")
            for index, i in enumerate(result):
                Train_No = i[0]
                Train_Name = i[1]
                Train_Source = i[2]
                Train_Destination = i[3]
                print(f"{index}. {Train_No}\t\t {Train_Name}\t {Train_Source}\t\t\t\t {Train_Destination}")
        elif choice == 4:
            destination_Station = input("Please enter Train Destination station : ")
            mycursor.execute("""SELECT * FROM Train WHERE Train_Destination = %s""", (destination_Station,))
            result = mycursor.fetchall()
            print()
            print("-----------------------------------------------------------------------------")
            print("Train No\t Train Name\t\t\t Source\t\t\t Destination")
            print("-----------------------------------------------------------------------------")
            for index, i in enumerate(result):
                Train_No = i[0]
                Train_Name = i[1]
                Train_Source = i[2]
                Train_Destination = i[3]
                print(f"{index}. {Train_No}\t\t {Train_Name}\t {Train_Source}\t\t\t {Train_Destination}")
        elif choice == 5:
            MENU()
        elif choice == 6:
            break
        else:
            print("Error : Invalid choice, Please try again")
        conti = input("Please press any key to continue...")

#-------------------------------- Train Information -----------------------------
def TrainInformation():
    while True:
        print()
        print("-----------------------------------------------")
        print("-------- Welcome to Train Information ---------")
        print("-----------------------------------------------")
        print(" 1. Information by Train Number ")
        print(" 2. Information by Train Name ")
        print(" 3. Go back to main menu ")
        print(" 4. Exit ")
        print("-----------------------------------------------")
        print()
        choice = int(input("Enter your Choice (1-4) : "))
        print()
        if choice == 1:
            train_Number = int(input("Please enter the Train number : "))
            mycursor.execute('''SELECT t.Train_Name, t.Train_Source, t.Train_Destination, ti.1AC_Availability as FirstAC_Availability, 
                                ti.1AC_Fare as First1AC_Fare, ti.2AC_Availability as SecondAC_Availability, ti.2AC_Fare as SecondAC_Fare, 
                                ti.3AC_Availability as ThirdAC_Availability, ti.3AC_Fare as ThirdAC_Fare
                                FROM Train t JOIN TrainInfo ti ON t.Train_No = ti.Train_No WHERE t.Train_No = %d''' % (train_Number))
            result = mycursor.fetchall()
            for index, i in enumerate(result):
                Train_Name = i[0]
                Train_Source = i[1]
                Train_Destination = i[2]
                FirstAC_Availability = i[3]
                FirstAC_Fare = i[4]
                SecondAC_Availability = i[5]
                SecondAC_Fare = i[6]
                ThirdAC_Availability = i[7]
                ThirdAC_Fare = i[8]
                print()
                print()
                print("---------------------------------------------------")
                print("---------------- Train Information ----------------")
                print("---------------------------------------------------")
                print(f"Train Name \t\t:\t {Train_Name}")
                print(f"Source Station \t\t:\t {Train_Source}")
                print(f"Destination Station \t:\t {Train_Destination}")
                print(f"Seats Availability (1AC):\t {FirstAC_Availability}")
                print(f"Fare (1AC) \t\t:\t {FirstAC_Fare}/-")
                print(f"Seats Availability (2AC):\t {SecondAC_Availability}")
                print(f"Fare (2AC) \t\t:\t {SecondAC_Fare}/-")
                print(f"Seats Availability (3AC):\t {ThirdAC_Availability}")
                print(f"Fare (3AC) \t\t:\t {ThirdAC_Fare}/-")
                print("---------------------------------------------------")
                print()
                print()
        elif choice == 2:
            train_Name = input("Please enter the Train Name : ")
            mycursor.execute('''SELECT t.Train_Name, t.Train_Source, t.Train_Destination, ti.1AC_Availability as FirstAC_Availability, 
                                ti.1AC_Fare as First1AC_Fare, ti.2AC_Availability as SecondAC_Availability, ti.2AC_Fare as SecondAC_Fare, 
                                ti.3AC_Availability as ThirdAC_Availability, ti.3AC_Fare as ThirdAC_Fare 
                                FROM Train t JOIN TrainInfo ti ON t.Train_No = ti.Train_No WHERE t.Train_Name = %s''', (train_Name,))
            result = mycursor.fetchall()
            for index, i in enumerate(result):
                Train_Name = i[0]
                Train_Source = i[1]
                Train_Destination = i[2]
                FirstAC_Availability = i[3]
                FirstAC_Fare = i[4]
                SecondAC_Availability = i[5]
                SecondAC_Fare = i[6]
                ThirdAC_Availability = i[7]
                ThirdAC_Fare = i[8]
                print()
                print()
                print("---------------------------------------------------")
                print("---------------- Train Information ----------------")
                print("---------------------------------------------------")
                print(f"Train Name \t\t:\t {Train_Name}")
                print(f"Source Station \t\t:\t {Train_Source}")
                print(f"Destination Station \t:\t {Train_Destination}")
                print(f"Seats Availability (1AC):\t {FirstAC_Availability}")
                print(f"Fare (1AC) \t\t:\t {FirstAC_Fare}/-")
                print(f"Seats Availability (2AC):\t {SecondAC_Availability}")
                print(f"Fare (2AC) \t\t:\t {SecondAC_Fare}/-")
                print(f"Seats Availability (3AC):\t {ThirdAC_Availability}")
                print(f"Fare (3AC) \t\t:\t {ThirdAC_Fare}/-")
                print("---------------------------------------------------")
                print()
                print()
        elif choice == 3:
            MENU()
        elif choice == 4:
            break
        else:
            print("Error : Invalid choice, Please try again")
        conti = input("Please press any key to continue...")

#-------------------------------- Ticket Booking -----------------------------
def TicketBooking():
    while True:
        print()
        print("-----------------------------------------------")
        print("-------- Welcome to Train Booking -------------")
        print("-----------------------------------------------")
        print()
        train_Number = int(input("Please enter the Train number : "))
        doj = input("Please enter Date & Time (dd/mm/yyyy hh:mm) : ")
        departure = input("from destination :")
        arrival = input("to destination :")
        nooftickets = int(input("Please enter the No. of Tickets :"))
        pnr = random.randint(100000, 200000)
        for i in range(1, nooftickets+1):
            name = input("Please enter your Name : ")
            jclass = int(input("Please enter the class (1/2/3) : "))
            sex = input("enter your gender :")
            aadharcard = input("enter Aadhar Card No. :")
            if len(aadharcard) == 12:
                print("aadhar card verified")
            else:
                print("aadhar details are wrong")
                break
            add_user = ("INSERT INTO BookingDetails (PNR, Train_No, Name, DOJ, Class, sex, departure, arrival) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            data_user = (pnr, train_Number, name, doj, jclass, sex, departure, arrival)
            mycursor.execute(add_user, data_user)
            mysqldb.commit()
            print()
        #code for seat calculation
        if jclass == 1:
            sql = "update TrainInfo set 1AC_Availability = 1AC_Availability - 1 where Train_No = " + str(train_Number)
        elif jclass == 2:
            sql = "update TrainInfo set 2AC_Availability = 2AC_Availability - 1 where Train_No = " + str(train_Number)
        else:
            sql = "update TrainInfo set 3AC_Availability = 3AC_Availability - 1 where Train_No = " + str(train_Number)
        mycursor.execute(sql)
        mysqldb.commit()
        #------------------------------------Payment-------------------------------------------
        print("-----------------------------------------------")
        print("---------------Payment-------------------------")
        print("-----------------------------------------------")
        phone_no = str(input("enter phone no. :"))
        creditcard = str(input("enter credit card number"))
        cvv = str(input("enter your cvv"))
        print(" ")
        if len(phone_no) == 10 and len(creditcard) == 16 and len(cvv) == 3:
            print("Your tickets have been booked ,Thanks for relying on us!")
        else:
            print("your details are wrong")
            break
        print()
        print('Your Ticket has been booked with PNR Number : ', pnr)
        print()
        print()
        break

#-------------------------------- PNR Status -----------------------------
def PNRStatus():
    while True:
        print("-----------------------------------------------")
        print("---- Welcome to PNR Status & Ticket Details ---")
        print("-----------------------------------------------")
        print(" 1. Check PNR Status ")
        print(" 2. Go Back to main menu ")
        print(" 3. Exit ")
        print("-----------------------------------------------")
        choice = int(input("Enter your Choice (1-3) : "))
        print()
        if choice == 1:
            pnr=int(input("Please enter the PNR Number : "))
            mycursor.execute('SELECT t.Train_No, t.Train_Name,
            t.Train_Source, t.Train_Destination, bd.Name, bd.DOJ, bd.Class, bd.sex,
            bd.departure, bd.arrival FROM Train t JOIN BookingDetails bd ON
            t.Train_No = bd.Train_No WHERE bd.PNR = %d' % (pnr))
            result=mycursor.fetchall() #fetches all the rows in a result set
            for i in result:
                             Train_No=i[0]
                             Train_Name=i[1]
                             Train_Source=i[2]
                             Train_Destination=i[3]
                             Name=i[4]
                             DOJ=i[5]
                             Class=i[6]
                             sex=i[7]
                             departure=i[8]
                             arrival=i[9]
                             print()
                             print()
                             print("-----------------------------------------------------------")
                             print("----------------- Ticket Details --------------------------")
                             print("-----------------------------------------------------------")
                             print("PNR \t\t\t:\t", pnr)
                             print("Booking Status \t\t:\t Confirmed")
                             print("Train Number \t\t:\t", Train_No)
                             print("Train Name \t\t:\t", Train_Name)
                             print("Date of Journey \t:\t", DOJ)
                             print("Passanger Name \t\t:\t", Name)
                             print("Class of Journey \t:\t", Class)
                             print("Gender \t\t\t:\t", sex)
                             print("from \t\t\t:\t", departure)
                             print("to \t\t\t:\t", arrival)
                             print("-----------------------------------------------------------")
                             print()
                             print()
                             print()
        elif choice==2:
            MENU()
        else:
            break

#-------------------------------- Ticket Cancellation -----------------------------
def TicketCancellation():
    print("-----------------------------------------------")
    print("------------- Ticket Cancellation -------------")
    print("-----------------------------------------------")
    pnr = int(input("Please enter the PNR Number : "))
    mycursor.execute('SELECT t.Train_No, t.Train_Name, t.Train_Source, t.Train_Destination, bd.Name, bd.DOJ, bd.Class, bd.sex, bd.departure, bd.arrival FROM Train t JOIN BookingDetails bd ON t.Train_No = bd.Train_No WHERE bd.PNR = %d' % (pnr))
    result = mycursor.fetchall()  # fetches all the rows in a result set
    for i in result:
        Train_No = i[0]
        Train_Name = i[1]
        Train_Source = i[2]
        Train_Destination = i[3]
        Name = i[4]
        DOJ = i[5]
        Class = i[6]
        sex = i[7]
        departure = i[8]
        arrival = i[9]
        print()
        print()
        print("---------------------------------------------------")
        print("----------------- Ticket Details ------------------")
        print("---------------------------------------------------")
        print("PNR \t\t\t:\t", pnr)
        print("Booking Status \t\t:\t Confirmed")
        print("Train Number \t\t:\t", Train_No)
        print("Train Name \t\t:\t", Train_Name)
        print("Date of Journey \t:\t", DOJ)
        print("Passenger Name \t\t:\t", Name)
        print("Class of Journey \t:\t", Class)
        print("Gender \t\t\t:\t", sex)
        print("from \t\t\t:\t", departure)
        print("to \t\t\t:\t", arrival)
        print("---------------------------------------------------")
        print()
        print()
    cancellationYes = input("Do you wish to cancel this ticket (Y/N) : ")
    if cancellationYes == 'Y':
        # code for seat calculation
        if Class == 1:
            sql = "update TrainInfo set 1AC_Availability = 1AC_Availability + 1 where Train_No = " + str(Train_No)
        elif Class == 2:
            sql = "update TrainInfo set 2AC_Availability = 2AC_Availability + 1 where Train_No = " + str(Train_No)
        else:
            sql = "update TrainInfo set 3AC_Availability = 3AC_Availability + 1 where Train_No = " + str(Train_No)
        mycursor.execute(sql)  # Execute SQL Query to update record
        mysqldb.commit()
        print("Your ticket with PNR : ", pnr, " has been cancelled successfully.Refund will be credited in 7 working days.")
        print()
    for j in result:
        Train_No = j[0]
        Train_Name = j[1]
        Train_Source = j[2]
        Train_Destination = j[3]
        Name = j[4]
        DOJ = j[5]
        Class = j[6]
        sex = j[7]
        departure = j[8]
        arrival = j[9]
        print("---------------------------------------------------")
        print("----------------- Ticket Details ------------------")
        print("---------------------------------------------------")
        print("PNR \t\t\t:\t", pnr)
        print("Booking Status \t\t:\t Cancelled")
        print("Train Number \t\t:\t", Train_No)
        print("Train Name \t\t:\t", Train_Name)
        print("Date of Journey \t:\t", DOJ)
        print("Passanger Name \t\t:\t", Name)
        print("Class of Journey \t:\t", Class)
        print("Gender \t\t\t:\t", sex)
        print("from \t\t\t:\t", departure)
        print("to \t\t\t:\t", arrival)
        print("---------------------------------------------------")
        print()
        print()

mycursor.execute('DELETE FROM BookingDetails WHERE PNR = %d' % (pnr))  # Execute SQL Query to delete a record
mysqldb.commit()  # Commit is used for your changes in the database
#-------------------------------- Admin -----------------------------
def Admin():
    while True:
        print()
        print("-----------------------------------------------")
        print("-------------- Welcome Admin ------------------")
        print("-----------------------------------------------")
        print(" 1. Add a Train ")
        print(" 2. Remove a Train ")
        print(" 3. Go back to main menu ")
        print(" 4. Exit ")
        print("-----------------------------------------------")
        print()
        choice = int(input("Enter your Choice (1-4) : "))
        print()
        
        if choice == 1:
            train_Number = int(input("Please enter the Train Number : "))
            train_Name = input("Please enter the Train Name : ")
            source = input("Please enter the Source Station : ")
            destination = input("Please enter the Destination Station : ")
            firstACSeats = int(input("Please enter the number of seats in First AC : "))
            firstACFare = int(input("Please enter the First AC Fare : "))
            secondACSeats = int(input("Please enter the number of seats in Second AC : "))
            secondACFare = int(input("Please enter the Second AC Fare : "))
            thirdACSeats = int(input("Please enter the number of seats in Third AC : "))
            thirdACFare = int(input("Please enter the Third AC Fare : "))
            
            sql = 'INSERT INTO Train (Train_No, Train_Name, Train_Source, Train_Destination) VALUES (%s, %s, %s, %s)'
            val = (train_Number, train_Name, source, destination)
            mycursor.execute(sql, val)
            mysqldb.commit()
            
            sql1 = 'INSERT INTO TrainInfo (Id, Train_No, 1AC_Availability, 1AC_Fare, 2AC_Availability, 2AC_Fare, 3AC_Availability, 3AC_Fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            val1 = (train_Number + 50, train_Number, firstACSeats, firstACFare, secondACSeats, secondACFare, thirdACSeats, thirdACFare)
            mycursor.execute(sql1, val1)
            mysqldb.commit()
            
            print()
            print("Train has been successfully created with following details")
            mycursor.execute('SELECT t.Train_Name, t.Train_Source, t.Train_Destination, ti.1AC_Availability as FirstAC_Availability, ti.1AC_Fare First1AC_Fare, ti.2AC_Availability as SecondAC_Availability, ti.2AC_Fare as SecondAC_Fare, ti.3AC_Availability as ThirdAC_Availability, ti.3AC_Fare as ThirdAC_Fare FROM Train t JOIN TrainInfo ti ON t.Train_No = ti.Train_No WHERE t.Train_No = %d' % (train_Number))
            result = mycursor.fetchall()  # fetches all the rows in a result set
            
            for i in result:
                Train_Name = i[0]
                Train_Source = i[1]
                Train_Destination = i[2]
                FirstAC_Availability = i[3]
                FirstAC_Fare = i[4]
                SecondAC_Availability = i[5]
                SecondAC_Fare = i[6]
                ThirdAC_Availability = i[7]
                ThirdAC_Fare = i[8]
                print()
                print("---------------------------------------------------")
                print("---------------- Train Information ----------------")
                print("---------------------------------------------------")
                print("Train Name \t\t:\t", Train_Name)
                print("Source Station \t\t:\t", Train_Source)
                print("Destination Station \t:\t", Train_Destination)
                print("Seats Availability (1AC):\t", FirstAC_Availability)
                print("Fare (1AC) \t\t:\t", FirstAC_Fare, "/-")
                print("Seats Availability (2AC):\t", SecondAC_Availability)
                print("Fare (2AC) \t\t:\t", SecondAC_Fare, "/-")
                print("Seats Availability (3AC):\t", ThirdAC_Availability)
                print("Fare (3AC) \t\t:\t", ThirdAC_Fare, "/-")
                print("---------------------------------------------------")
                print()
                print()
        
        elif choice == 2:
            train_No = int(input("Please enter the Train Number : "))
            mycursor.execute('DELETE FROM TrainInfo WHERE Train_No = %d' % (train_No))  # Execute SQL Query to delete a record
            mysqldb.commit()  # Commit is used for your changes in the database
            mycursor.execute('DELETE FROM Train WHERE Train_No = %d' % (train_No))  # Execute SQL Query to delete a record
            mysqldb.commit()  # Commit is used for your changes in the database
            print()
            print("Train has been successfully removed from chart")
            print()
        
        elif choice == 3:
            MENU()
        
        elif choice == 4:
            break
        
        else:
            print("Error : Invalid choice, Please try again")
            conti = input("Please press any key to continue...")
            MENU()


