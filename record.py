import datetime

# 1. Define a data structure for holding each weather reading.
class Record:
    def __init__ (self, date, record):
        self.convert_date(date)
        self.record = record
    
    def convert_date(self, date):
        parts = date.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
                
        
        my_date = datetime.datetime(year, month, day)
        month_str = my_date.strftime('%B')
                
        if (day == 1):
            self.date = str(day) + "st " + month_str + " " + str(year)
        elif (day == 2):
            self.date = str(day) + "nd " + month_str + " " + str(year)
        elif (day == 3):
            self.date += str(day) + "rd " + month_str + " " + str(year)
        else:
            self.date += str(day) + "th " + month_str + " " + str(year)
                
    