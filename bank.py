# import pymysql module
import pymysql

# make a connection with database
db = pymysql.connect("localhost", "root", "", "bank")

# initialize cursor
cursor = db.cursor()


# add_details function to add details of customer
def add_details():
    acc_no = int(input("Enter the account number :"))
    acc_hold_name = input("Enter the account holder name :")
    acc_type = input("Enter the account type :")
    balance = float(input("Enter the balance :"))

    sql = "INSERT into account(acc_no, acc_hold_name, acc_type, balance)VALUES('%d','%s','%s','%f')" % (
        acc_no, acc_hold_name, acc_type, balance)

    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("customer details added!!")
    else:
        print("Not added!!")


# show_all function will show the details of all customers
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


# show_details functions will show the details of given account number
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


# update_details function for updating the details of given account number
def update_details():
    acc_no = int(input("Enter the account number which you want to update :"))
    acc_hold_name = input("Enter the account holder name :")
    acc_type = input("Enter the account type :")
    balance = float(input("Enter the account balance :"))

    sql = "UPDATE account SET acc_hold_name='%s', acc_type='%s', balance='%f' WHERE acc_no='%d'" % (
        acc_hold_name, acc_type, balance, acc_no)

    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("Record updated successfully")
    else:
        print("Record not updated")


# delete_details function for deleting details of given account number
def delete_details():
    acc_no = int(input("Enter the  account number whose details are to be deleted :"))

    sql = "DELETE FROM account WHERE acc_no='%d'" % (acc_no)
    r = cursor.execute(sql)

    db.commit()

    if r > 0:
        print("Record deleted successfully!!")
    else:
        print("No such record found!!")


# transfer function for transferring ammount from sender account to receiver account
def transfer():
    sender_acc_no = int(input("Enter the sender account number :"))
    receiver_acc_no = int(input("Enter the receiver account number :"))
    ammount = float(input("Enter the ammount to be transferred :"))

    sql = "SELECT balance FROM account where acc_no='%d'" % (sender_acc_no)
    cursor.execute(sql)
    sender_bal = cursor.fetchone()

    sql = "SELECT balance FROM account WHERE acc_no='%d'" % (receiver_acc_no)
    cursor.execute(sql)
    receiver_bal = cursor.fetchone()

    print(sender_bal)
    print(ammount)

    if (sender_bal[0] - ammount) < 1000:
        print("Not possible!! Minimum balance should be 1000.")
    else:
        send = "UPDATE account SET balance='%f' WHERE acc_no='%d'" % (sender_bal[0] - ammount, sender_acc_no)
        cursor.execute(send)
        receive = "UPDATE account SET balance='%f' WHERE acc_no='%d'" % (receiver_bal[0] + ammount, receiver_acc_no)
        cursor.execute(receive)
        print('''%f transferred successfully!!''' % ammount)
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

    if x == 1:
        add_details()
    elif x == 2:
        show_all()
    elif x == 3:
        show_details()
    elif x == 4:
        update_details()
    elif x == 5:
        delete_details()
    elif x == 6:
        transfer()
    elif x == 7:
        exit()
    else:
        print("Enter a valid choice!!")

db.close()
