import datetime 
from speak import speak


def tellDay():
     day = datetime.datetime.today().weekday()
     
     Day_dict = {0:"Monday",
                 1:"Tuesday",
                 2:"Wednesday",
                 3:"Thursday",
                 4:"Friday",
                 5:"Saturday",
                 6:"Sunday" }
     if day in Day_dict:
         day_of_the_week = Day_dict[day]
         print("Today is day " +day_of_the_week)
         speak("Today is day " +day_of_the_week)
         
def tellTime():
    time = str(datetime.datetime.now())
    
    hour = time[11:13]
    minutes = time[14:16]
    print("The current time is " +hour+ " Hours and " +minutes+ " Minutes")
    speak("The current time is " +hour+ " Hours and " +minutes+ " Minutes")