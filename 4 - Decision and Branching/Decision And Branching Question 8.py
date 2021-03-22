if (userInput8 <= 12):
    print("Your ticket costs " +str(userChildTicket) + " dollars.")
elif (userInput8 >= 13) and (userInput8 <= 64):
    print("Your ticket costs " + str(userAdultTicket) + " dollars.")
else:
    print("Your ticket costs " + str(userSeniorTicket) + " dollars.")