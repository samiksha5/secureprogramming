
import os
import csv
import re

phones = []
name_position = 0
phone_position = 1
phone_header = ['Name', 'Phone Number']


def choice(no):
    if not no.isdigit ():
        print ("'" + no + "' needs to be the number of a phone!")
        return False
    no = int (no)

    return True


def delete_phone(phono):
    i = 0
    flag=0
    for phone in phones:
        if phone[phone_position] == phono:
            print ("phone number exists")
            flag=1
            i = i + 1
        else:
            i = i + 1
    if flag==0 :
        print ("Record with phone no "+phono+" does not exist")
        exit(1)
    del phones[i]
    print ("Deleted record with phone number ", phono)
    save_list ()

def delete_phone2(name):
    i=0
    flag=0
    for phone in phones:
        if phone[name_position]==name:
            print("name exists")
            flag=1
            i=i+1
        else:
            i=i+1
    if flag==0 :
        print ("Record with name "+name+" does not exist")
        exit(1)
    del phones[i-1]
    print ("Deleted record with name ", name)
    save_list ()



def save_list():
    f = open ("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer (f).writerow (item)
    f.close ()


def load_list():
    if os.access ("myphones.csv", os.F_OK):
        f = open ("myphones.csv")
        for row in csv.reader (f):
            phones.append (row)
        f.close ()


def show_phones():
    show_phone (phone_header, "")
    index = 1
    for phone in phones:
        show_phone (phone, index)
        index = index + 1
    print ()


def show_phone(phone, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print (outputstr.format (index, phone[name_position], phone[phone_position]))

def check_name(name):
    regexA ='^([a-zA-Z])+$'
    regexB ='^[a-zA-Z]+(((\'|-|.)?([a-zA-Z])+))?$'
    regexC ='^[a-zA-Z]+((\\s)?((\'|-|.)?([a-zA-Z])+))*$'
    regexD= '^[a-zA-Z]+((\\s)?([a-zA-Z])+)*$'
    regexE ='^[^\s]+,?(\s[^\s]+)*$'
    regexF='^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))*$'
    regexG ='^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))+((\\s)?([a-zA-Z])+)*$'


    if (re.search ( regexA,name)):
        print("\nName Accepted")
    elif (re.search( regexB,name)):
        print ("\nName Accepted")
    elif (re.search( regexC,name)):
        print ("\nName Accepted")
    elif (re.search(regexD,name)):
        print ("\nName Accepted")
    elif (re.search(regexE,name )):
        print ("\nName Accepted")
    elif (re.search(regexF,name)):
        print ("\nName Accepted")
    elif (re.search(regexG,name)):
        print ("\nName Accepted")
    else:
        print("\nName Rejected")
        exit(1)

def check_phone_no(phone):
    regexa='^\\d{5}$'
    regexb ='^\\(\\d{3}\\)\\d{3}-\\d{4}$'
    regexc='^\\d{3}-\\d{4}$'
    regexd='^\\d{3}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
    regexe ='^\\d{5}.\\d{5}$'
    regexf='^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
    regexg='^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
    regexh='^\\d{1}\\(\\d{3}\\)\\d{3}-\\d{4}$'
    regexi ='^\\+\\d{2}\\s\\(\\d{2}\\)\\s\\d{3}-\\d{4}$'
    regexj ='^\\+\\d\\(\\d{3}\\)\\d{3}\\-\\d{4}$'
    if (re.search ( regexa,phone)):
        print("\nPhone Accepted")
    elif (re.search( regexb,phone)):
        print ("\nPhone Accepted")
    elif (re.search( regexc,phone)):
        print ("\nPhone Accepted")
    elif (re.search( regexd, phone)):
        print ("\nPhone Accepted")
    elif (re.search( regexe,phone)):
        print ("\nPhone Accepted")
    elif (re.search( regexf,phone)):
        print ("\nPhone Accepted")
    elif (re.search( regexg,phone)):
        print ("\nPhone Accepted")
    elif (re.search (regexh, phone)):
        print ("\nPhone Accepted")
    elif (re.search (regexi, phone)):
        print ("\nPhone Accepted")
    elif (re.search (regexj, phone)):
        print ("\nPhone Accepted")
    else:
        print("\nPhone Rejected")
        exit(1)

def create_phone():
    print ("Enter the data for a new phone:")
    newname = input ("Enter name: ")
    check_name(newname)
    newphone_num = input ("Enter phone number: ")
    check_phone_no(newphone_num)
    phone = [newname, newphone_num]
    phones.append (phone)


def menu_choice():
    """ Find out what the user wants to do next. """
    print ("Choose one of the following options?")
    print ("   s) Show")
    print ("   n) New")
    print ("   dp) Delete by phone number")
    print ("   dn) Delete by name")
    print ("   q) Quit")
    choice = input ("Choice: ")
    if choice.lower () in ['n', 'dn', 's', 'dp', 'q']:
        return choice.lower ()
    else:
        print (choice + "?")
        print ("Invalid option")
        return None


def main_loop():
    load_list ()

    while True:
        choice = menu_choice ()
        if choice == None:
            continue
        if choice == 'q':
            print ("Exiting...")
            break  # jump out of while loop
        elif choice == 'n':
            create_phone ()
        elif choice == 'dp':
            num = input ("Which item do you want to delete? ")
            print ("Phone number : ", num)
            delete_phone (num)
        elif choice == 's':
            show_phones ()
        elif choice == 'dn':
            num = input ("Which item do you want to delete? ")
            print ("Name : ", num)
            delete_phone2 (num)
        else:
            print ("Invalid choice.")

    save_list ()



if __name__ == '__main__':
    main_loop ()