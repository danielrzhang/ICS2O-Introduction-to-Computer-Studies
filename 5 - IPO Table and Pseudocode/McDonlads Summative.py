##########################################################################
# File Name: 10-03-2019 - McDonlads Summative.py                         #
# Description: Summative project to calculate employee pay at McDonlads  #
# Author: Daniel Zhang                                                   #
# Date: 9/30/2019                                                        #
##########################################################################

# Variables
employeeName = str(input("Welcome to the McDonlads Employee Salary Calculating System. \nTo begin, please enter your name here: "))
employeeType = str(input("\nHi, " + employeeName + "! Please enter in all capital letters. \nAre you a WORKER or a MANAGER?: "))
startDay = str(input("\nIn all capital letters, please enter the day of the week that your shift started on: "))
startHour = str(input("\nNow, in 24 hour time and with 2 digits, please enter the hour you started your shift: "))
startMinute = str(input("\nNext, please enter the minutes in the hour that your shift started: "))
endDay = str(input("\nIn all capital letters, please enter the day of the week that your shift ended on: "))
endHour = input("\nNow, in 24 hour time and with 2 digits, please enter the hour you ended your shift: ")
endMinute = input("\nFinally, please enter the minutes in the hour that your shift ended: ")

# Change starting days of the week into numbers in order to calculate the total number of hours
if startDay == "MONDAY":
  startDayReplace = 1
elif startDay == "TUESDAY":
  startDayReplace = 2
elif startDay == "WEDNESDAY":
  startDayReplace = 3
elif startDay == "THURSDAY":
  startDayReplace = 4
elif startDay == "FRIDAY":
  startDayReplace = 5
elif startDay == "SATURDAY":
  startDayReplace = 6
elif startDay == "SUNDAY":
  startDayReplace = 7
else:
  print("\nSorry, but the entry '" + startDay + "' for the starting day of the week shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Change ending days of the weeks into hours in order to calculate the total number of hours
if endDay == "MONDAY":
  endDayReplace = 1
elif endDay == "TUESDAY":
  endDayReplace = 2
elif endDay == "WEDNESDAY":
  endDayReplace = 3
elif endDay == "THURSDAY":
  endDayReplace = 4
elif endDay == "FRIDAY":
  endDayReplace = 5
elif endDay == "SATURDAY":
  endDayReplace = 6
elif endDay == "SUNDAY":
  endDayReplace = 7
else:
  print("\nSorry, but the entry '" + endDay + "' for the ending day of the week shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Check to see if the starting hours entered have two digits
startHourTwoDigits = len(startHour)
if startHourTwoDigits == 2:
	startHourNew = startHour
else:
  print("\nSorry, but the entry '" + startHour + "' for the starting hour shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Check to see if the ending hours entered have two digits
endHourTwoDigits = len(endHour)
if endHourTwoDigits == 2:
  endHourNew = endHour
else:
  print("\nSorry, but the entry '" + endHour + "' for the ending hour shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Check to see if the starting minutes entered have two digits
startMinuteTwoDigits = len(startMinute)
if startMinuteTwoDigits == 2:
  startMinuteNew = startMinute
else:
  print("\nSorry, but the entry '" + startMinute + "' for the starting minute shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Check to see if the starting minutes entered have two digits
endMinuteTwoDigits = len(endMinute)
if endMinuteTwoDigits == 2:
  endMinuteNew = endMinute
else:
  print("\nSorry, but the entry '" + endMinute + "' for the ending minute shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Check if the employee’s shift stays within 1 work week
if (startDayReplace < endDayReplace):
  startDayReplaceCheck = startDayReplace
  endDayReplaceCheck = endDayReplace
elif (startDayReplace == endDayReplace):
  if (startHourNew < endHourNew):
      startDayReplaceCheck = startDayReplace
      endDayReplaceCheck = endDayReplace
  elif (startHourNew == endHourNew):
    if (startMinuteNew <= endMinuteNew):
      startDayReplaceCheck = startDayReplace
      endDayReplaceCheck = endDayReplace
    else:
      print("\nSorry, but your shift spans over a work week! You'll need to create two separate paychecks. \nPlease restart the Salary System now!")
  else:
    print("\nSorry, but your shift spans over a work week! You'll need to create two separate paychecks. \nPlease restart the Salary System now!")
else:
  print("\nSorry, but your shift spans over a work week! You'll need to create two separate paychecks. \nPlease restart the Salary System now!")

# Calculate the total number of hours on the days, without additional or excess hours on the first and last days
startEndHour = (int(endDayReplaceCheck) - int(startDayReplaceCheck)) * 24

# Check if the starting and ending hours entered are less than 24 and greater than or equal to 00
if (00 <= int(startHourNew) < 24):
  startHourNewCheck = startHourNew
else:
  print("\nSorry, but the entry '" + str(startHourNew) + "' for the starting hour shift is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
if (00 <= int(endHourNew) < 24):
  endHourNewCheck = endHourNew
else:
  print("\nSorry, but the entry '" + str(endHourNew) + "' for the ending hour is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Add or subtract the excess and additional hours from the first and last days
if startHourNew < endHourNew:
  startEndHourCheck = startEndHour + (24 - (int(endHourNewCheck) - int(startHourNewCheck)))
elif startHourNewCheck > endHourNewCheck:
  startEndHourCheck = (startEndHour - 24) + ((24 + int(endHourNewCheck)) - int(startHourNewCheck))
else:
  startEndHourCheck = startEndHour
  
# Convert minutes to hours
if (int(startMinuteNew) <= int(endMinuteNew)) and (00 <= int(startMinuteNew) < 60) and (00 <= int(endMinuteNew) < 60):
  startEndMinute = int(endMinuteNew) - int(startMinuteNew)
elif (int(startMinuteNew) > int(endMinuteNew)) and (00 <= int(startMinuteNew) < 60) and (00 <= int(endMinuteNew) < 60):
  startEndMinute = (int(endMinuteNew) + 60) - int(startMinuteNew)
  startEndHourCheck = startEndHourCheck - 1
else:
  print("\nSorry, but the entry '" + str(startEndMinute) + "' for the starting and/or ending minute is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Combines total hours and minutes together
startEndHourCheck += startEndMinute / 60
finalStartEndHour = round(startEndHourCheck, 2)

# Calculation of employee pay
if employeeType == "WORKER":
  salaryBeforeTax = finalStartEndHour * 6.50
elif employeeType == "MANAGER":
  salaryBeforeTax = finalStartEndHour * 10.00
else:
  print("\nSorry, but the entry '" + employeeType + "' for the employee position is invalid! \nPlease restart the Salary System and follow the instructions carefully!")
  
# Calculation of tax
tax = salaryBeforeTax * 0.20
tax = round(tax, 2)
salaryBeforeTax = round(salaryBeforeTax, 2)

# Calculation of tax-deducted salary
salaryAfterTax = salaryBeforeTax - tax
salaryAfterTax = round(salaryAfterTax, 2)

# Rounds the number of hours (without minutes)
startEndHour = round(startEndHour)

# Converts the hour decimal into minutes
startEndMinute = round(startEndMinute)

# Print Statements
print("\nThank you for your time, " + employeeName + "! Please wait a few moments as your payslip is being processed... \n")
print("\n       ---------------------")
print("       McDonlads \n       Employee Pay Slip")
print("       ---------------------")
print("       Employee Name: " + employeeName)
print("       Employee Type: " + employeeType)
print("       Time In: " + str(startDay) + ", " + str(startHourNew) + ":" + str(startMinuteNew))
print("       Time Out: " + str(endDay) + ", " + str(endHourNew) + ":" + str(endMinuteNew))
print("       Duration of Shift: " + str(startEndHour) + " hours and " + str(startEndMinute) + " minutes")
print("       Salary Before Tax: $" + str(salaryBeforeTax))
print("       Income Tax (20%): -$" + str(tax))
print("       Salary After Tax: $" + str(salaryAfterTax))
print("       ----------------------")
print("       Have a nice day!")



