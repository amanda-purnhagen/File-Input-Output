class email():
    # Email class attributes
    toEmail = ""
    fromEmail = ""
    time = ""

    # email constructor
    def __init__(self, toE, fromE, time):
        self.toEmail = toE
        self.fromEmail = fromE
        self.time = time

    # Accessor methods
    def getToEmail(self):
        return self.toEmail

    def getFromEmail(self):
        return self.fromEmail

    def getTime(self):
        return self.time

    def __str__(self):
        return "From " + self.fromEmail + " to " + self.toEmail + " at " + self.time

def welcome_message():
    print("Welcome to the Email Analyzer program. Please choose from the following options: ")
    print("\t1. Upload text data")
    print("\t2. Find by Receiver")
    print("\t3. Download statistics")
    print("\t4. Exit the program")

    user_input()

def user_input():
    userInput = input(print(""))

    if userInput == "1":
        upload_text_data()
    elif userInput == "2":
        print_emails()
    elif userInput == "3":
        create_stats_file()
    elif userInput == "4":
        quit()
    else:
        print("Sorry, invalid input. Please try again.")
        welcome_message()

def upload_text_data():
    emailObjects = []

    inputInfile = input(print("What is the name of your data file? "))

    infile = open(inputInfile, 'r')

    for line in infile:
        line = line.rstrip("\n")
        stringList = line.split(" ")
        toEmail = stringList[0]
        fromEmail = stringList[1]
        time = stringList[2]

        # Create list with email objects
        emailObjects.append(email(toEmail, fromEmail, time))

    infile.close()

    return inputInfile, emailObjects

    welcome_message()

def print_emails():
    originalInputInfile, emailObjectsList = upload_text_data()
    inputReceiver = input(print("What is the receiver's email? "))

    print(inputReceiver + " received the following emails: ")

    for i in emailObjectsList:
        if inputReceiver == i.getToEmail():
            print("\t- From " + i.getFromEmail() + " at " + i.getTime())

    print("\n")
    welcome_message()

def create_stats_file():
    timesSeen = 0

    originalInputInfile, emailObjectsList = upload_text_data()

    strInputInfile = originalInputInfile[0:-4]
    statsOutfile = strInputInfile + "_stats.txt"

    outfile = open(statsOutfile, 'w')

    # Part a
    outfile.write("Here are all of the emails: \n")
    for i in emailObjectsList:
        outfile.write(i.__str__() + "\n")


    '''
    STUCK HERE
    '''
    # Part b
    for x in emailObjectsList:
        for y in emailObjectsList:
            if x == y:
                numOccurrences = emailObjectsList.count(x)
                print(x + " was emailed " + str(numOccurrences) + " times.")

    '''
    for x in emailObjectsList:
        thisToEmail = x.getToEmail()
        for y in emailObjectsList:
            if x.getToEmail() == y.getToEmail():
                timesSeen += 1

        print(x.getToEmail() + " received " + str(timesSeen) + " emails.")
    '''

def main():
    welcome_message()

main()