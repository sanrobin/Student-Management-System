# Importing necessary Libraries

import tkinter as gui

import tkinter.messagebox as msgbox

import mysql.connector as sqltor

import csv

import subprocess as userget


# Defining Functions

def Connect():              # Connects to the server

    print("Trying to connect to server Please wait...")

    GetPasswd()

    GetDB()

    GetUser()

    global Connection

    try:

        #Connection = sqltor.connect(host = "localhost", user = user, passwd = gpass, database = db, autocommit = True)     # Statement to connect to MySQL Server

        Connection = sqltor.connect(host = "localhost", user = "root", passwd = "prime", database = "g12", autocommit = True)     # Statement to connect to MySQL Server

        if Connection.is_connected:     # Checks if the connection to the server is successful

            print("Successfully connected to MySQL Server!")

        else:

            print("Error connecting to the server. Retrying...")
            Connect()

        ConnectionWindow.destroy()

        MainMenuGUI()

    except:

        msgbox.showerror("Error", "An Error occured! Check the provided info and try again.")



def Disconnect():           # Disconnects from the server

    print("Attempting to save changes and disconnect from server...")
    Connection.commit()
    Connection.close()

    if Connection.is_connected == False:   # Checks if the server had disconnected successfully

        print("Successfully disconnected from MySQL Server!")

    print("Quitting...")

    MainMenu.destroy()

    ConnectionWindowGUI()


def GetUserNameOfThePC():   # Gets the username of the PC (used for exporting to csv part)

    global UserName

    UserName = userget.check_output("echo %username%", shell = True)


def BackToMainMenu():       # Function to return to main menu of the program

    try:

        ChemistryMenu.destroy()

    except:

        try:

            PhysicsMenu.destroy()

        except:

            try:

                MathsMenu.destroy()

            except:

                try:

                    CSMenu.destroy()

                except:

                    try:

                        EnglishMenu.destroy()

                    except:

                        print("Error Occured! Function BackToMainMenu called unexpectedly.")

    MainMenuGUI()


def BackToSubMenu():        # Function to return to the subject menu of the program

    try:

        InsertMenu.destroy()

    except:

        try:

            UpdateMenu.destroy()

        except:

            try:

                DeleteMenu.destroy()

            except:

                print("Error Occured! Function BackToSubMenu called unexpectedly")

    if SubName == 'Physics':

        PhysicsMenuGUI()

    elif SubName == 'Chemistry':

        ChemistryMenuGUI()()

    elif SubName == 'Maths':

        MathsMenuGUI()

    elif SubName == 'CS':

        CSMenuGUI()

    elif SubName == 'English':

        EnglishMenuGUI()

    else:

        print("Error Occured! Function BackToSubMenu called unexpectedly")
    


def InsertThings():         # Function to insert values to the MySQL Database

    AdmnoGet = InsertMenuWidget2.get()

    NameGet = InsertMenuWidget4.get()

    MarksGet = InsertMenuWidget6.get()

    InsertCursor = Connection.cursor()

    try:

        InsertCursor.execute("INSERT INTO {sub} VALUES ({adm},'{name}',{mark})".format(sub = SubName,adm = int(AdmnoGet),name = NameGet,mark = int(MarksGet)))

        msgbox.showinfo("Success!", "Values have been inserted")

        InsertCursor.close()

    except:

        msgbox.showerror("Error Occoured!", "An error occured")

        InsertCursor.close()

    InsertMenu.destroy()


def UpdateThings():         # Function to update values in MySQL Database

    AdmnoGet = UpdateMenuWidget2.get()

    NameGet = UpdateMenuWidget4.get()

    MarksGet = UpdateMenuWidget6.get()

    UpdateCursor = Connection.cursor()

    if NameGet == "":       # Condition which checks if the name is the same or not

        try:

            UpdateCursor.execute("UPDATE {sub} SET Marks = {mark} WHERE Admno = {adm}".format(sub = SubName, mark = int(MarksGet), adm = int(AdmnoGet)))

            msgbox.showinfo("Success!", "Values have been updated")

            UpdateCursor.close()


        except:

            msgbox.showerror("Error Occoured!", "An error occured")

            UpdateCursor.close()

    else:

        try:

            UpdateCursor.execute("UPDATE {sub} SET Marks = {mark}, Name = '{name}'  WHERE Admno = {adm}".format(sub = SubName,mark = int(MarksGet), name = NameGet, adm = int(AdmnoGet)))

            msgbox.showinfo("Success!", "Values have been updated")

            UpdateCursor.close()

        except:

            msgbox.showerror("Error Occoured!", "An error occured")

            UpdateCursor.close()


def DeleteThings():         # Function to delete values in MySQL Database

    AdmnoGet = DeleteMenuWidget2.get()

    DeleteCursor = Connection.cursor()

    try:

        DeleteCursor.execute("DELETE FROM {sub} WHERE admno = {adm}")

        msgbox.showinfo("Success!", "Values have been updated")

        DeleteCursor.close()

    except:

        msgbox.showerror("Error Occoured!", "An error occured")

        DeleteCursor.close()


def Physics():              # Function to call Physics menu and destroying the main menu

    MainMenu.destroy()

    PhysicsMenuGUI()
    

def Chemistry():            # Function to call Chemistry menu and destroying the main menu

    MainMenu.destroy()

    ChemistryMenuGUI()


def Maths():                # Function to call Maths menu and destroying the main menu

    MainMenu.destroy()

    MathsMenuGUI()


def CS():                   # Function to call CS menu and destroying the main menu

    MainMenu.destroy()

    CSMenuGUI()


def English():              # Function to call English menu and destroying the main menu

    MainMenu.destroy()

    EnglishMenuGUI()
    

def GetPasswd():            # Function to get password from the connection screen

    global gpass

    gpass = ConnectionWindowWidget7.get()


def GetDB():                # Function to get the database name (Class name) from the connection screen

    global db

    db = ConnectionWindowWidget5.get()


def GetUser():              # Function to get the username from the connection screen for MySQL login

    global user

    user = ConnectionWindowWidget3.get()

def jls_extract_def():      # idk why this is here. As there is a saying, "If your code works, dont touch the source code", I AM NOT TOUCHING IT.
    
    return "Please Enter your credentials"


def ConnectionWindowGUI():  # Creating GUI ConnectionWindow

    # Making variables global so they can be used in other programs

    global ConnectionWindow

    global ConnectionWindowWidget3

    global ConnectionWindowWidget5

    global ConnectionWindowWidget7

    ConnectionWindow = gui.Tk()

    ConnectionWindow.geometry("350x200")

    ConnectionWindow.title("Student Management System")

    ConnectionWindowWidget1 = gui.Label(ConnectionWindow, text = "Enter your credentials below")

    ConnectionWindowWidget1.pack()
    

    ConnectionWindowWidget2 = gui.Label(ConnectionWindow, text = "Username")

    ConnectionWindowWidget2.pack()
    

    ConnectionWindowWidget3 = gui.Entry(ConnectionWindow, width = 20)

    ConnectionWindowWidget3.pack()
    

    ConnectionWindowWidget4 = gui.Label(ConnectionWindow, text = "Class")

    ConnectionWindowWidget4.pack()
    

    ConnectionWindowWidget5 = gui.Entry(ConnectionWindow, width = 20)

    ConnectionWindowWidget5.pack()
    

    ConnectionWindowWidget6 = gui.Label(ConnectionWindow, text = "Password")

    ConnectionWindowWidget6.pack()
    

    ConnectionWindowWidget7 = gui.Entry(ConnectionWindow, width = 20, show = '●')

    ConnectionWindowWidget7.pack()
    

    ConnectionWindowWidget8 = gui.Button(ConnectionWindow, text = "Connect!", command = Connect)

    ConnectionWindowWidget8.pack()


    ConnectionWindowWidget9 = gui.Button(ConnectionWindow, text = "Quit", command = ProgQuit)

    ConnectionWindowWidget9.pack()
    

    ConnectionWindow.mainloop()


def MainMenuGUI():          # Creating GUI MainMenu

    global MainMenu

    MainMenu = gui.Tk()

    MainMenu.geometry("200x200")
    
    MainMenu.title("Main Menu")

    MainMenuWidget1 = gui.Label(MainMenu, text = "Main Menu")

    MainMenuWidget1.pack()

    MainMenuWidget2 = gui.Button(MainMenu, text = "Physics", command = Physics)

    MainMenuWidget2.pack()

    MainMenuWidget3 = gui.Button(MainMenu, text = "Chemistry", command = Chemistry)

    MainMenuWidget3.pack()

    MainMenuWidget4 = gui.Button(MainMenu, text = "Maths", command = Maths)

    MainMenuWidget4.pack()

    MainMenuWidget5 = gui.Button(MainMenu, text = "CS", command = CS)

    MainMenuWidget5.pack()

    MainMenuWidget6 = gui.Button(MainMenu, text = "English", command = English)

    MainMenuWidget6.pack()

    MainMenuWidget7 = gui.Button(MainMenu, text = "Disconnect", command = Disconnect)
    
    MainMenuWidget7.pack()
    
    MainMenu.mainloop()


def ProgQuit():             # Function used to exit the application

    ConnectionWindow.destroy()


def PhysicsMenuGUI():       # Function used to draw the Physics Menu

    global SubName, PhysicsMenu

    SubName = "Physics"

    PhysicsMenu = gui.Tk()

    PhysicsMenu.geometry("300x300")

    PhysicsMenu.title("Physics Menu")

    PhysicsMenuWidget1 = gui.Label(PhysicsMenu, text = "Select an option")

    PhysicsMenuWidget1.pack()

    PhysicsMenuWidget2 = gui.Button(PhysicsMenu, text = "Insert", command = InsertMenuGUI)

    PhysicsMenuWidget2.pack()

    PhysicsMenuWidget3 = gui.Button(PhysicsMenu, text = "Update", command = UpdateMenuGUI)

    PhysicsMenuWidget3.pack()

    PhysicsMenuWidget4 = gui.Button(PhysicsMenu, text = "Delete", command = DeleteMenuGUI)

    PhysicsMenuWidget4.pack()

    PhysicsMenuWidget5 = gui.Button(PhysicsMenu, text = "Export as CSV", command = ExportAsCSV)

    PhysicsMenuWidget5.pack()

    PhysicsMenuWidget6 = gui.Button(PhysicsMenu, text = "Back to Main Menu", command = BackToMainMenu)

    PhysicsMenuWidget6.pack()

    PhysicsMenu.mainloop()


def ChemistryMenuGUI():     # Function used to draw the Chemistry Menu

    global SubName, ChemistryMenu

    SubName = "Chemistry"

    ChemistryMenu = gui.Tk()

    ChemistryMenu.geometry("200x200")

    ChemistryMenu.title('Maths Menu')

    ChemistryMenuWidget1 = gui.Label(ChemistryMenu, text = "Select an option")

    ChemistryMenuWidget1.pack()

    ChemistryMenuWidget2 = gui.Button(ChemistryMenu, text = "Insert", command = InsertMenuGUI)

    ChemistryMenuWidget2.pack()

    ChemistryMenuWidget3 = gui.Button(ChemistryMenu, text = "Update", command = UpdateMenuGUI)

    ChemistryMenuWidget3.pack()

    ChemistryMenuWidget4 = gui.Button(ChemistryMenu, text = "Delete", command = DeleteMenuGUI)

    ChemistryMenuWidget4.pack()

    ChemistryMenuWidget5 = gui.Button(ChemistryMenu, text = "Export as CSV", command = ExportAsCSV)

    ChemistryMenuWidget5.pack()

    ChemistryMenuWidget6 = gui.Button(ChemistryMenu, text = "Back to Main Menu", command = BackToMainMenu)

    ChemistryMenuWidget6.pack()

    ChemistryMenu.mainloop()


def MathsMenuGUI():         # Function used to draw the Maths Menu

    global SubName, MathsMenu

    SubName = "Maths"

    MathsMenu = gui.Tk()

    MathsMenu.geometry("200x200")

    MathsMenu.title('Maths Menu')

    MathsMenuWidget1 = gui.Label(MathsMenu, text = "Select an option")

    MathsMenuWidget1.pack()

    MathsMenuWidget2 = gui.Button(MathsMenu, text = "Insert", command = InsertMenuGUI)

    MathsMenuWidget2.pack()

    MathsMenuWidget3 = gui.Button(MathsMenu, text = "Update", command = UpdateMenuGUI)

    MathsMenuWidget3.pack()

    MathsMenuWidget4 = gui.Button(MathsMenu, text = "Delete", command = DeleteMenuGUI)

    MathsMenuWidget4.pack()

    MathsMenuWidget5 = gui.Button(MathsMenu, text = "Export as CSV", command = ExportAsCSV)

    MathsMenuWidget5.pack()

    MathsMenuWidget6 = gui.Button(MathsMenu, text = "Back to Main Menu", command = BackToMainMenu)

    MathsMenuWidget6.pack()
    
    MathsMenu.mainloop()


def CSMenuGUI():            # Function used to draw the CS Menu

    global SubName, CSMenu

    SubName = "CS"

    CSMenu = gui.Tk()

    CSMenu.geometry("200x200")

    CSMenu.title('CS Menu')

    CSMenuWidget1 = gui.Label(CSMenu, text = "Select an option")

    CSMenuWidget1.pack()

    CSMenuWidget2 = gui.Button(CSMenu, text = "Insert", command = InsertMenuGUI)

    CSMenuWidget2.pack()

    CSMenuWidget3 = gui.Button(CSMenu, text = "Update", command = UpdateMenuGUI)

    CSMenuWidget3.pack()

    CSMenuWidget4 = gui.Button(CSMenu, text = "Delete", command = DeleteMenuGUI)

    CSMenuWidget4.pack()

    CSMenuWidget5 = gui.Button(CSMenu, text = "Export as CSV", command = ExportAsCSV)

    CSMenuWidget5.pack()

    CSMenuWidget6 = gui.Button(CSMenu, text = "Back to Main Menu", command = BackToMainMenu)

    CSMenuWidget6.pack()

    CSMenu.mainloop()


def EnglishMenuGUI():       # Function used to draw the English Menu

    global SubName, EnglishMenu

    SubName = "English"

    EnglishMenu = gui.Tk()

    EnglishMenu.geometry("200x200")

    EnglishMenu.title('Maths Menu')

    EnglishMenuWidget1 = gui.Label(EnglishMenu, text = "Select an option")

    EnglishMenuWidget1.pack()

    EnglishMenuWidget2 = gui.Button(EnglishMenu, text = "Insert", command = InsertMenuGUI)

    EnglishMenuWidget2.pack()

    EnglishMenuWidget3 = gui.Button(EnglishMenu, text = "Update", command = UpdateMenuGUI)

    EnglishMenuWidget3.pack()

    EnglishMenuWidget4 = gui.Button(EnglishMenu, text = "Delete", command = DeleteMenuGUI)

    EnglishMenuWidget4.pack()

    EnglishMenuWidget5 = gui.Button(EnglishMenu, text = "Export as CSV", command = ExportAsCSV)

    EnglishMenuWidget5.pack()

    EnglishMenuWidget6 = gui.Button(EnglishMenu, text = "Back to Main Menu", command = BackToMainMenu)

    EnglishMenuWidget6.pack()

    EnglishMenu.mainloop()


def InsertMenuGUI():        # Function used to draw the Insert Menu

    global InsertMenu, InsertMenuWidget2, InsertMenuWidget4, InsertMenuWidget6

    InsertMenu = gui.Tk()

    InsertMenu.geometry("200x200")

    InsertMenu.title("Insertion Menu")

    InsertMenuWidget1 = gui.Label(InsertMenu, text = "Admission Number")

    InsertMenuWidget1.pack()

    InsertMenuWidget2 = gui.Entry(InsertMenu, width = 20) 

    InsertMenuWidget2.pack()  

    InsertMenuWidget3 = gui.Label(InsertMenu, text = "Name of the student") 

    InsertMenuWidget3.pack()

    InsertMenuWidget4 = gui.Entry(InsertMenu, width = 20)

    InsertMenuWidget4.pack()

    InsertMenuWidget5 = gui.Label(InsertMenu, text = "Marks to be added")

    InsertMenuWidget5.pack()

    InsertMenuWidget6 = gui.Entry(InsertMenu, width = 20)

    InsertMenuWidget6.pack()

    InsertMenuWidget7 = gui.Button(InsertMenu, text = "Insert!", command = InsertThings)

    InsertMenuWidget7.pack()

    InsertMenu.mainloop()


def UpdateMenuGUI():           # Function used to draw the Update Menu

    global UpdateMenu, UpdateMenuWidget2, UpdateMenuWidget4, UpdateMenuWidget6

    UpdateMenu = gui.Tk()

    UpdateMenu.geometry("200x200")

    UpdateMenu.title("Updating Menu")

    UpdateMenuWidget1 = gui.Label(UpdateMenu, text = "Admission Number")

    UpdateMenuWidget1.pack()

    UpdateMenuWidget2 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget2.pack()

    UpdateMenuWidget3 = gui.Label(UpdateMenu, text = "New Value for Name (if required to be changed or else be blank)")

    UpdateMenuWidget3.pack()

    UpdateMenuWidget4 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget4.pack()

    UpdateMenuWidget5 = gui.Label(UpdateMenu, text = "New Value for Marks")

    UpdateMenuWidget5.pack()

    UpdateMenuWidget6 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget6.pack()

    UpdateMenuWidget7 = gui.Button(UpdateMenu, text = "Update!", command = UpdateThings)

    UpdateMenuWidget7.pack()

    UpdateMenu.mainloop()


def DeleteMenuGUI():           # Function used to draw the Deletion Menu

    global DeleteMenu, DeleteMenuWidget2

    DeleteMenu = gui.Tk()

    DeleteMenu.geometry("300x100")

    DeleteMenu.title("Deleting Menu")

    DeleteMenuWidget1 = gui.Label(DeleteMenu, text = "Admission Number of the row to be deleted")

    DeleteMenuWidget1.pack()

    DeleteMenuWidget2 = gui.Entry(DeleteMenu, width = 20)

    DeleteMenuWidget2.pack()

    DeleteMenuWidget3 = gui.Button(DeleteMenu, text = "Delete!", command = DeleteThings)

    DeleteMenuWidget3.pack()


def ExportAsCSV():          # Function used to export the MySQL database as a .csv file onto the user's desktop

    GetUserNameOfThePC()

    ExportFile = open("C:\\Users\\"+str(UserName.decode().strip())+"\\Desktop\\Exported.csv", "w", newline = '\n')

    CSVWriter = csv.writer(ExportFile)

    ExportCursor = Connection.cursor()

    try:

        ExportCursor.execute("SELECT * FROM {sub}".format(sub = SubName))

        ExportValues = ExportCursor.fetchall()

        CSVWriter.writerow(["Admission Number","Name","Marks"])

        CSVWriter.writerows(ExportValues)

        msgbox.showinfo("Success!", "Value(s) have been exported!")

        BackToMainMenu()

        ExportFile.close()

    except:

        ExportFile.close()

        msgbox.showerror("Error", "An unexpected error occured!")

        BackToMainMenu()


ConnectionWindowGUI()