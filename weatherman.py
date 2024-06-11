import datetime
import sys

def convert_date(self, date):
    year, month, day = date.split("-", "\n")
        
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
        
    my_date = datetime.datetime(year_int, month_int, day_int)
        
    month = datetime.datetime.strptime(my_date, '%B')
        
    date = day_int + "th " + month + year

# 1. Define a data structure for holding each weather reading.
class Record:
    def __init__ (self):
        self.date = ""
        self.record = []
   
    # use a list of records
    def add_record(self, date: str, record = []):
        convert_date(date)
        
        self.records.append((date, record))
        
    def show_record(self):
        print("On " + self.date + ": " + self.record)
    

def populate(f, record_list):
    dictionary(f.readline()) # creates dictionary of all the items
    
    # for all lines in file
    for line in f:
        # read an entire line and remove date
        terms = line.split(",", "\n")
        
        date = line[0] 
        reading = []
        
        for x in line[1:]:
            if line[x] == "":
                reading[x] = 0
            else:
                reading[x] = int(line[x])
            
        # create record object
        record = Record(date, reading)
        # append into record_list
        
        record_list.append(record)    

# 2. Define a class for parsing the files and populating the readings data structure with correct data types.
class ParseRecords:
    record_list = Record()
    
    def __init__ (self, filename: str):
        for i in filename:
            f = open(filename[i], "r")
            
            if f == -1:
                print("File doesnt exist")
                return
            
            populate(f, self.record_list)
            
        
    
    def print_records(self):
        for i in enumerate(self.record_list):
            print(self.record_list)
        
def dictionary(self, string: str): 
    diction = dict()
    
    items = string.split(",", "\n")
    for i in enumerate(items):
        dict[i] = items[i]
    return dict
        
# 3. Define a data structure for holding the calculations results.
# 4. Define a class for computing the calculations given the readings data structure.
class Calculations:  
    def __init__ (self, records: ParseRecords, dictionary: dict):
        self.record_list = records.record_list
        self.dictionary = dictionary 
           
    def __lt__ (self: Record, other: Record):
        return (self.record < other.record)
    
    def __gt__ (self: Record, other: Record):
        return (self.record > other.record)
    
    def max (self, index):
        return max(self.record_list[dictionary[index]])
    
    def min (self, index):
        return min(self.record_list[dictionary[index]])
    
    def avg (self, index):
        sum = 0
        num = 0
        for i in enumerate(self.record_list[dictionary[index]]):
            sum += self.record_list[dictionary[index]]
            num += 1
            
        return sum/num
        
        
        
# 5. Define a class for creating the reports given the results data structure.
class CreateReports:
    def __init__ (self, records: ParseRecords):
        self.record_list = ParseRecords.record_list
        calculate = Calculations(records)
    
    def task1 (self):
        # highest temperature and day, lowest temperature and day, most humid day and humidity
        max_temp = self.calculate.max("Max TemperatureC")
        min_temp = self.calculate.min("Min TemperatureC")
        most_humid = self.calculate.max("Max Humidity")
        
    def task2 (self):
        # average highest temperature, average lowest temperature, average mean humidity
        max_avg_temp = self.calculate.max("Mean TemperatureC")
        min_avg_temp = self.calculate.min("Mean TemperatureC")
        avg_humidity = self.calculate.avg("Mean Humidity")
        
    def task3 (self):
        # bar chart of max and min temp of each day
        for day in enumerate(self.record_list):
            record = Record()
            for i in enumerate(self.record_list):
                if i == day:
                    record = self.record_list[i].record
            max_temp = self.record[0]
            min_temp = self.record[1]
            
            print("\033[31m" + "*" * max_temp)
            print("\033[36m" + "*" * min_temp)
            
    def task4 (self):
        # bar chart with min and max
        for day in enumerate(self.record_list):
            record = Record()
            for i in enumerate(self.record_list):
                if i == day:
                    record = self.record_list[i].record
            max_temp = self.record[0]
            min_temp = self.record[1]
            
            print("\033[36m" + "*" * min_temp, end = "")
            print("\033[31m" + "*" * max_temp)
            
        
# 6. Define main for assembling the above and running the program.
def main():
    if len(sys.argv) < 4:
        print("Format: file path method files")
    
    path = sys.argv[1]
    method = sys.argv[2]
    files = sys.argv[3:]
    
    records = ParseRecords(files)
    reports = CreateReports(records)






