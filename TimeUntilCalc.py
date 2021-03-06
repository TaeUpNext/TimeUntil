import datetime
from datetime import timedelta
starting = True #Starting loop 
while starting == True:
  #*Starting Date
  startingDate_Entry = input('\nEnter the starting date in YYYY-MM-DD format: ')
  sMonth,sDay,sYear= map(int, startingDate_Entry.split('-'))
  startingDate = datetime.date(sMonth, sDay, sYear)
  formattedStartDate = (startingDate.strftime("\nStaring Date: %B/%d/%Y"))
  fStartDate = (startingDate.strftime("\n%B/%d/%Y"))

  #*Ending Date
  endingDate_Entry = input('\nEnter the ending date in YYYY-MM-DD format: ')
  eMonth,eDay,eYear= map(int, endingDate_Entry.split('-'))
  endingDate = datetime.date(eMonth, eDay, eYear)
  formattedEndDate = (endingDate.strftime("\nEnding Date: %B/%d/%Y"))

  fEndDate = (endingDate.strftime("\n%B/%d/%Y"))

  #!Global Vairables
  tUntil = endingDate - startingDate
  total_seconds = tUntil.total_seconds()
  total_minutes = total_seconds / 60 #*Converts the seconds into minutes
  total_hours = total_minutes / 60#*Convers the minutes into hours
  total_days = total_hours / 24 #*converts the hours into days
  total_weeks = total_days / 7 #*Converts the days into weeks 
  total_months = total_weeks / 4.34 #*Converts the week into months
  total_years = total_months / 12 #*Converts the months into years

  
  print(formattedStartDate) #*displays the inputted start date in Month/dd/yyyy format
  print(formattedEndDate) #*displays the inputted end date in Month/dd/yyyy format
  #tFrom = startingDate + endingDate
  
  #*determine time loop
  dTimeException = False #*exception handling for the determine time input 
  while dTimeException == False:
    determineTime = eval(input("\nWould You like to find the time until a date or the time from a date, Enter a 1 for time from or a 2 for time until: ")) #Determines if a user is finding out how long its been since a date or how long it will take to get to a date
    
    #!Time Until Formula
    if determineTime == 1: 
      dConversionException = False #*Exception handling for the time conversion
      while dConversionException == False:
        determineConversion = eval(input("\nHow would you like to convert the time? Enter a 1 for seconds, a 2 for minutes, a 3 for hours, a 4 for days, a 5 for weeks, a 6 for months or a 7 for years: ")) #*Determines how to convert the time between the 2 dates
        #!Time until formula for seconds
        if determineConversion == 1: 
          print(f"\nThere is {total_seconds:,.2f} seconds until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
          
        #!Time Until Minutes
        elif determineConversion == 2: 
          print(f"\nThere is {total_minutes:,.2f} minutes until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time Until Hours
        elif determineConversion == 3: 
          print(f"\nThere is {total_hours:,.2f} hours until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time Until Days
        elif determineConversion == 4: 
          print(f"\nThere is {total_days:,.2f} day/days until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
                  
        #!Time Until Weeks
        elif determineConversion == 5: 
          print(f"\nThere is {total_weeks:,.2f} week/weeks until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time until months
        elif determineConversion == 6: 
          print(f"\nThere is {total_months:,.2f} month/months until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time Until years
        elif determineConversion == 7: 
          print(f"\nThere is {total_years:,.2f} year/years until {fEndDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
                  
                  
    #!Time From Formula
    elif determineTime == 2: 
      dConversionException = False #*Exception handling for the time conversion
      while dConversionException == False:
        determineConversion = eval(input("\nHow would you like to convert the time? Enter a 1 for seconds, a 2 for minutes, a 3 for hours, a 4 for days, a 5 for weeks, a 6 for months or a 7 for years: ")) #*Determines how to convert the time between the 2 dates
        #!Time From formula for seconds
        if determineConversion == 1: 
          print(f"\nThere has been {total_seconds:,.2f} seconds since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
          
        #!Time From in Minutes
        if determineConversion == 2: 
          print(f"\nThere has been {total_minutes:,.2f} minutes since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time From in Hours
        if determineConversion == 3: 
          print(f"\nThere has been {total_hours:,.2f} hours since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time From in  Days
        if determineConversion == 4: 
          print(f"\nThere has been {total_days:,.2f} day/days since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
                  
        #!Time From in Weeks
        if determineConversion == 5: 
          print(f"\nThere has been {total_weeks:,.2f} week/weeks since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time From in months
        if determineConversion == 6: 
          print(f"\nThere has been {total_months:,.2f} month/months since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False
        
        #!Time From in years
        if determineConversion == 7: 
          print(f"\nThere has been {total_years:,.2f} year/years since {fStartDate}") #*Prints the time in seconds until the end date
          rConversionExcpetion = False #*Exception handling for the redoing 
          while rConversionExcpetion == False: #*Exception handling to determine if you would like to redo the conversion
            redoConversion = eval(input("\nwould you like to convert the time into another value? Enter a 1 for yes or a 2 for no: ")) 
            if redoConversion == 1:#*user wants to convert into another time 
              dConversionException = False #*Sets the determine conversion loop to False to reneter the loop
              rConversionExcpetion = True #*Approves the redo conversion exception
            elif redoConversion == 2: #*user does not want to redo  a conversion conversion
              rConversionExcpetion = True #*approves the redo conversion excpetion
              newDateConversionException = False #
              
              while newDateConversionException == False: #*Exception handling to determine if you would like to enter a new date
                redoDate= eval(input("\nwould you like to enter a new date? Enter a 1 for yes or a 2 for no: "))
                if redoDate == 1: #*User wants to enter a new date
                  starting = True #*sets the date loop to true so user can enter a new one
                  rConversionExcpetion = True
                  dConversionException = True
                  dTimeException = True
                  newDateConversionException = True
                elif redoConversion == 2: #*user would not like to enter a new date
                  starting = False
                  rConversionExcpetion = True
                  dConversionException = True #*exits the determine conversion loop
                  dTimeException = True
                  newDateConversionException = True
                else:
                  print("\nYou entered an invalid input, please try again: ")
                  newDateConversionException = False