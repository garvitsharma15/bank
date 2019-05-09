import pymysql

db = pymysql.connect("localhost","root","","bank")

cursor = db.cursor()

def add_details():
    acc_no = int(input("Enter the account number :"))
    acc_hold_name = input("Enter the account holder name :")
    acc_type = input("Enter the account type :")
    balance = int(input("Enter the balance :"))

    sql = "INSERT into account(acc_no, acc_hold_name, acc_type, balance)VALUES('%d','%s','%s','%d')" % (
    acc_no, acc_hold_name, acc_type, balance)

    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("customer details added!!")
    else:
        print("Not added!!")

def show_all():
    show = "SELECT * from account"
    cursor.execute(show)

    r = cursor.fetchall()

    for i in r:
        print("Account number:", i[0])
        print("Account holder name:", i[1])
        print("Account type:", i[2])
        print("Account balance:", i[3])
        print("\n")

def show_details():
    acc_no = int(input("Enter the account number "))

    show = "SELECT * FROM account WHERE acc_no='%d'" % (acc_no)

    cursor.execute(show)
    r = cursor.fetchall()
    for i in r:
        print("\tAccount number:", i[0])
        print("\tAccount holder name:", i[1])
        print("\tAccount type:", i[2])
        print("\tAccount balance:", i[3])

def update_details():
    acc_no = int(input("Enter the account number which you want to update :"))
    acc_hold_name = input("Enter the account holder name :")
    acc_type = input("Enter the account type :")
    balance = int(input("Enter the account balance :"))

    sql = "UPDATE account SET acc_hold_name='%s', acc_type='%s', balance='%d' WHERE acc_no='%d'" % (
    acc_hold_name, acc_type, balance, acc_no)

    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("Record updated successfully")
    else:
        print("Record not updated")

def delete_details():
    acc_no = int(input("Enter the  account number whose details are to be deleted :"))

    sql = "DELETE FROM account WHERE acc_no='%d'" % (acc_no)
    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("Record deleted successfully!!")
    else:
        print("No such record found!!")

def transfer():
    sender_acc_no = int(input("Enter the sender account number :"))
    receiver_acc_no = int(input("Enter the receiver account number :"))
    ammount = int(input("Enter the ammount to be transferred :"))

    sql = "SELECT balance FROM account where acc_no='%d'" % (sender_acc_no)
    cursor.execute(sql)
    sender_bal = cursor.fetchone()

    sql = "SELECT balance FROM account WHERE acc_no='%d'" % (receiver_acc_no)
    cursor.execute(sql)
    receiver_bal = cursor.fetchone()

    if (sender_bal[0] - ammount) < 1000:
        print("Not possible!! Minimum balance should be 1000.")
    else:
        send = "UPDATE account SET balance='%d' WHERE acc_no='%d'" % (sender_bal[0] - ammount, sender_acc_no)
        cursor.execute(send)
        receive = "UPDATE account SET balance='%d' WHERE acc_no='%d'" % (receiver_bal[0] + ammount, receiver_acc_no)
        cursor.execute(receive)
        print('''%d transferred successfully!!''' % ammount)
    db.commit()

print("\n****Bank Management System****\n")
while 1:
    print("\n1.\tAdd account details")
    print("2.\tShow all user details")
    print("3.\tShow user details by account number")
    print("4.\tUpdate the user details by account number")
    print("5.\tDelete the user details by account number")
    print("6.\tTransfer funds")
    print("7.\tExit")

    x = int(input("Enter your choice :"))

    if x==1:
        add_details()
    elif x==2:
        show_all()
    elif x==3:
        show_details()
    elif x==4:
        update_details()
    elif x==5:
        delete_details()
    elif x==6:
        transfer()
    elif x==7:
        exit()

db.close()
