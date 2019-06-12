# This is a python stuff
# Very interesting langauge
# Interpreted Language , WOW
# Careful with intentation
# 
from datetime import date, datetime, time, timedelta
import calendar
from os import path
import urllib.request
import json
import textwrap

def main():
    myClassInstance = myBaseClass()
    myClassInstance.myBaseMethod()
    myClassInstance.myControlFLowMethod(input("Enter a string"))
    myClassInstance.myLoopMethod(input("Enter a range of numbers"))
    myClassInstance.mybasicDateTime()
    myClassInstance.mybasicCalendar()
    myClassInstance.myBasicFile()
    myClassInstance.myFirstAPICall()


class myBaseClass():
    def myBaseMethod(self):
        print("Inside a class method")
        print("What a world")
        # Variable usage
        myIntVar = 1
        myStrVar = " Keep Going"
        print(myIntVar)
        print(myStrVar)
        # Type Cast
        mynewStr = str(myIntVar) + myStrVar
        print(mynewStr)
        print(type(mynewStr))

    def myControlFLowMethod(self, someParam):
        if ((len(someParam)) > 0) :
            print("You have passed " + someParam)
        else:
            print("You have passed ")
            
    def myLoopMethod(self, someParam1):
        # list fibonnaci numbers
        firstNumber = 1
        secondNumber = 2
        fib =[]

        for i in range(int(someParam1)-1):
            if(i==0):
               fib.append(firstNumber)    
               fib.append(secondNumber)          
            tempNumber = secondNumber
            secondNumber = firstNumber + secondNumber
            firstNumber = tempNumber
            
            fib.append(secondNumber)

        print("Fibonnaci series "+ str(fib))
# wORKING WITH dates, time
    def mybasicDateTime(self):
        today = date.today()
        print("Tday is :"  + str(today))
        now = datetime.now()
        print( "Time is "+ str(datetime.time(now)))
        # Formatting Dates
        print(now.strftime("%Y %a %b %I %m %p"))
        # Time deltas
        print (now + timedelta(days=365, weeks=1))
#wORKING WITH CALENDAR - gREAT
    def mybasicCalendar(self):
        myCal = calendar.TextCalendar(calendar.MONDAY)
        str = myCal.formatmonth(2019, 1, 0, 0)
        myCal1 = calendar.HTMLCalendar(calendar.MONDAY)
        for i in myCal1.itermonthdates(2019,6):
            print(i.strftime("%a %d %b %y"))
#Working with files,OS, shell util
    def myBasicFile(self):
        f = open("myfile.txt","w+")
        f.write("This is interesting")
        f.close
        print(path.exists("myfile.txt"))
        f= open("myfile.txt","r")
        print(f.read())
        f.close

    def myFirstAPICall(self):
        with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=Alchemist") as f:
             result = f.read()
            #  print (f" Its a wow thing calling a rest so easily  {result} ")
             myJson = json.loads(result)
            #  print(myJson)
             desc = textwrap.shorten(myJson['items'][1]['volumeInfo']['description'], 1000)
             print(f" My favourite all time is {myJson['items'][1]['volumeInfo']['title']}----- {desc} ")


if __name__ == "__main__":
    main()
