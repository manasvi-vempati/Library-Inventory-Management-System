import mysql.connector
import datetime

def mydbConnection():
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost",user="root",passwd="sai1234!")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return connection

def mydbQuery(query):
    connection=mydbConnection()
    cursor=connection.cursor()
    try:
        if "select" in query:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        else:
            cursor.execute(query)
            connection.commit()    
    except Exception as e:
        print("Oops! An error occurred")

def newBook():
    n=int(input("Enter the total number of books to be added in the Books Inventory: "))
    try:
        for i in range(n):
            MaxBookIDQry="select max(Bkid) from LIBRARY.BOOKS" 
            retrnRslt=mydbQuery(MaxBookIDQry)
            MaxBookID=None
            for row in retrnRslt:
                if row[0] is None:
                    MaxBookID=99
                else:
                    MaxBookID=row[0]
            Bkname=input("Enter the Book Name: ")
            Authname=input("Enter the Author Name: ")
            Totcop=int(input("Enter the No. of total Copies: "))
            Circno=0
            Bal=Totcop
            BookAddQry="INSERT INTO LIBRARY.BOOKS VALUES ({},'{}','{}',{},{},{},'ACTIVE')".format(MaxBookID+1,Bkname,Authname,Totcop,Circno,Bal)
            mydbQuery(BookAddQry)
            print("\n **Book added succesfully to the library ** \n")
    except Exception as e:
        print("**Book record not added successfully, Error is : **  ",e)

def dispBooks():
    n=input("Enter the Book ID to display the details of the book, if no details given ALL books shown: ")
    try:
        if not n:
            dispBookQry="select * from LIBRARY.BOOKS"
            retrnRslt=mydbQuery(dispBookQry)
            for row in retrnRslt:
                print (" #################################################")
                print (" Book ID : ", row[0])
                print (" Book Name : ", row[1])
                print (" Book Author Name : ", row[2])
                print (" Total Book Count : ", row[3])
                print (" Books in circulation : ", row[4])
                print (" Total Books Available to lend : ", row[5])
                print (" Book status in Library : ", row[6])
                print (" #################################################\n")
        else:
            dispBookQry="select * from LIBRARY.BOOKS where Bkid=({})".format(n)
            retrnRslt=mydbQuery(dispBookQry)
            for row in retrnRslt:
                print (" #################################################")
                print (" Book ID : ", row[0])
                print (" Book Name : ", row[1])
                print (" Book Author Name : ", row[2])
                print (" Total Book Count : ", row[3])
                print (" Books in circulation : ", row[4])
                print (" Total Books Available to lend : ", row[5])
                print (" Book status in Library : ", row[6])
                print (" #################################################\n")
    except Exception as e:
        print("**Unable to retrive the Book details from the Library, Error is : **  ",e)

def delBooks():
    n=input("Enter the Book ID to delete from the LIBRARY: ")
    try:
        bookAvailChk="select bkid, Circno from LIBRARY.BOOKS where bkid=({})".format(n)
        retrnRslt=mydbQuery(bookAvailChk)
        if not retrnRslt:
            print("\n Given Book ID is not avaiable in the Inventory, Please check and re-enter it again! \n")
        else:
            for row in retrnRslt:
                Circno=row[1]
            if Circno == 0:
                delBookQry="update library.books set BookStatus='DELETED' where bkid=({})".format(n)
                mydbQuery(delBookQry)
                print("\n Book has been successfully deleted from the Books inventory! \n")
            else:
                print("\n Book is active in circulation so unable to delete the book ID from inventory \n")
    except Exception as e:
        print("**Unable to remove the book from the Library, Error is : **  ",e)

def newMem():
    n=int(input("Enter the total number of Members to be added: "))
    try:
        for i in range(n):
            MaxMemIDQry="select max(Memid) from LIBRARY.MEMBERS" 
            retrnRslt=mydbQuery(MaxMemIDQry)
            MaxMemID=None
            for row in retrnRslt:
                if row[0] is None:
                    MaxMemID=199
                else:
                    MaxMemID=row[0]
            memname=input("Enter the Member Name: ")
            memaddress=input("Enter the address: ")
            phno=int(input("Enter the phone no.: "))
            mememail=input("enter the email id: ")
            MemAddQry="INSERT INTO LIBRARY.MEMBERS VALUES ({},'{}',{},'{}','{}','ACTIVE')".format(MaxMemID+1,memname,phno,memaddress,mememail)
            mydbQuery(MemAddQry)
            print("\n **Member has been added succesfully to the memebers list ** \n")
    except Exception as e:
        print("**Member is not added successfully, Error is : **  ",e)

def dispMems():
    n=input("Enter the Member ID to display the details of the member, if no details given ALL members details shown: ")
    try:
        if not n:
            dispMemQry="select * from LIBRARY.MEMBERS"
            retrnRslt=mydbQuery(dispMemQry)
            for row in retrnRslt:
                print (" #################################################")
                print (" Member ID : ", row[0])
                print (" Member Name : ", row[1])
                print (" Member Phone Number : ", row[2])
                print (" Member Address : ", row[3])
                print (" Member E-Mail ID : ", row[4])
                print (" Member Status in Library : ", row[5])
                print (" #################################################\n")
        else:
            dispMemQry="select * from LIBRARY.MEMBERS where Memid=({})".format(n)
            retrnRslt=mydbQuery(dispMemQry)
            for row in retrnRslt:
                print (" #################################################")
                print (" Member ID : ", row[0])
                print (" Member Name : ", row[1])
                print (" Member Phone Number : ", row[2])
                print (" Member Address : ", row[3])
                print (" Member E-Mail ID : ", row[4])
                print (" Member Status in Library : ", row[5])
                print (" #################################################\n")
    except Exception as e:
        print("**Unable to retrive the Members details from the Library records, Error is : **  ",e)
        
def delMems():
    n=input("Enter the Member ID to delete from the LIBRARY members list: ")
    try:
        memAvailChk="select Memid from LIBRARY.MEMBERS where Memid=({})".format(n)
        retrnRslt=mydbQuery(memAvailChk)
        if not retrnRslt:
            print("\n Given Member ID is not avaiable in the Inventory, Please check and re-enter it again! \n")
        else:
            memIssChk="select MemID from LIBRARY.Registry where Memid={} and DOR IS NULL".format(n)
            retrnRslt=mydbQuery(memIssChk)
            if retrnRslt:
                print("\n Given Member ID is currently holding books lended, Member cant be deleted until book return!! \n")
            else:
                delMemQry="update library.MEMBERS set MemStatus='DELETED' where Memid=({})".format(n)
                mydbQuery(delMemQry)
                print("\n Member has been successfully deleted from the members list! \n")
    except Exception as e:
        print("**Unable to remove the member from the Library members list, Error is : **  ",e)

def bksIssue():
    try:
        MaxRegIDQry="select max(RegID) from LIBRARY.Registry" 
        retrnRslt=mydbQuery(MaxRegIDQry)
        MaxRegID=None
        for row in retrnRslt:
            if row[0] is None:
                MaxRegID=499
            else:
                MaxRegID=row[0]
        tBkid=int(input("Enter id of the book being issued: "))
        MemberID=int(input("Enter id of the member borrowing the book: "))
        bkQry="select * from library.books where BookStatus='ACTIVE' and bkid=({})".format(tBkid)
        retrnRslt=mydbQuery(bkQry)
        BookNm=None
        balCnt=None
        circCnt=None
        if retrnRslt:
            for row in retrnRslt:
                BookNm=row[1]
                circCnt=row[4]
                balCnt=row[5]
        else:
            print("\n No Books available in the library with the given book ID or Book is Not Active \n")
            return

        memStsQry="select * from library.members where MemStatus='ACTIVE' and Memid=({})".format(MemberID)
        retrnRslt=mydbQuery(memStsQry)
        if not retrnRslt:
            print ("\n No Member available in the members list with the given member ID or Member is not Not Active \n")
            return
        else:        
            dateTme=str(datetime.datetime.now())
            DOI=dateTme[0:-7]
            DOR="NULL"
            addRegEntryQry="INSERT INTO LIBRARY.Registry VALUES ({},{},{},'{}','{}',{})".format(MaxRegID+1,MemberID,tBkid,BookNm,DOI,DOR)
            mydbQuery(addRegEntryQry)
            circIssueUpdQry="UPDATE LIBRARY.BOOKS SET Circno={}+1,Bal={}-1 WHERE BOOKS.Bkid={}".format(circCnt,balCnt,tBkid)
            mydbQuery(circIssueUpdQry)
            print("\n Books Issued details are successfully captured in the registry and Latest inventory is updated!! \n")
    except Exception as e:
        print("**Books Issued details are not captured in the registry, Error is: **",e)

def bksReturn():
    try:
        tBkid=int(input("Enter id of the book being returned: "))
        MemberID=int(input("Enter id of the member returning the book: "))
        regVldtQry="select RegID from library.Registry where BookID={} and MemID={} and DOR IS NULL".format(tBkid,MemberID)
        retrnRslt=mydbQuery(regVldtQry)
        RegID=None
        if retrnRslt:
            for row in retrnRslt:
                RegID=row[0]
        else:
            print ("\n No Book with given ID is issued to the member, please check and enter the details again \n")
            return
        
        bkQry="select * from library.books where bkid=({})".format(tBkid)
        retrnRslt=mydbQuery(bkQry)
        balCnt=None
        circCnt=None
        if retrnRslt:
            for row in retrnRslt:
                circCnt=row[4]
                balCnt=row[5]
        else:
            print ("\n No Books available in the library with the given book ID \n")
            return

        dateTme=str(datetime.datetime.now())
        DOR=dateTme[0:-7]

        circRtrnUpdQry="UPDATE LIBRARY.Registry SET DOR='{}' WHERE RegID={}".format(DOR,RegID)
        mydbQuery(circRtrnUpdQry)

        circBkUpdQry="UPDATE LIBRARY.BOOKS SET Circno={}-1,Bal={}+1 WHERE BOOKS.Bkid={}".format(circCnt,balCnt,tBkid)
        mydbQuery(circBkUpdQry)
        print("\n Books return details are successfully captured in the registry and Latest inventory is updated!!\n")
    except Exception as e:
        print("**Unable to update the return of books in the register, Error is: **",e)
        
def Menulib():
    while True:
        print("\033[1;34;49m")
        print("*********************************************************")
        print("\n\t\t Library Management\n")
        print("*********************************************************")
        print("1. Adding a Book in the Library")
        print("2. Display Book Record")
        print("3. Delete a Book Record")
        print("4. New member addition")
        print("5. Display Members List")
        print("6. Delete a Member")
        print("7. Issue book")
        print("8. Return book")
        print("9. Exit from Library Management Console")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 9 -------> :  "))
        if choice==1:
            newBook()
            continue
        elif choice==2:
            dispBooks()
            continue
        elif choice==3:
            delBooks()
            continue
        elif choice==4:
            newMem()
            continue
        elif choice==5:
            dispMems()
            continue
        elif choice==6:
            delMems()
            continue
        elif choice==7:
            bksIssue()
            continue
        elif choice==8:
            bksReturn()
            continue
        elif choice==9:
            break
        else:
            print("Wrong Choice......Enter Your Choice again")
            continue
try:
    Menulib()
    print("You have successfully stopped the project!!")
except Exception as e:
        print("**Library management project failed to start..., Error is: **",e)
