from cryptography.fernet import Fernet #import fernet

'''
def write_key(): #Function to write key.key file(should be executed once)
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():               #Function to load the key
    file = open("key.key", "rb") #key.key file to read(open)
    key = file.read() #reading file
    file.close() #closing
    return key


key = load_key() #calling function
fer = Fernet(key) 

def view():   #view function
    with open('passwords.txt', 'r') as f: #open passwords file
        for line in f.readlines(): #read line in f file
            data = line.rstrip()   #.rstrip to nullyfy next line (\n)
            user, passw = data.split("|") #split usename and password
            print("User:", user, "| Password:",           #print password and user name split
                  fer.decrypt(passw.encode()).decode())   #encrpted passw is decrypted


def add():                                #add function
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:   # open file to append
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # format to add password


while True:     #executing statements
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue