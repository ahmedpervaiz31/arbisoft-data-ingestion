import datetime
import sys

def convert_date(date):
    parts = date.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
            
    my_date = datetime.datetime(year, month, day)
            
    month_str = my_date.strftime('%B')
            
    date = str(day) + "th " + month_str + " " + str(year)
    
    return date

# 1. Define a data structure for holding each weather reading.
class Record:
    def __init__ (self, date, record):
        self.date = convert_date(date)
        self.record = record
  

# 2. Define a class for parsing the files and populating the readings data structure with correct data types.
class ParseRecords:
    def __init__ (self, filenames):
        self.record_list = []
        for file in filenames:
            with open(file, "r") as f:
                self.populate(f)
            
    def populate(self, f):     
        f.readline()   
        # for all lines in file
        for line in f:
            # read an entire line and remove date
            terms = line.strip().split(",")
            
            date = terms[0] 
            readings = []
            
            for term in terms[1:]:
                # if value then append it
                # else append 0
                try:
                    reading = int(float(term))
                    readings.append(reading)
                except ValueError:
                    readings.append(0)
            
            # create record object
            record = Record(date, readings)
            # append into record_list
            self.record_list.append(record)  
        
    def print_records(self):
        for record in enumerate(self.record_list):
            print(record)
        
def dictionary(string: str): 
    diction = dict()
    
    items = string.split(",", "\n")
    for i in enumerate(items):
        diction[i] = items[i]
    return diction
        
# 3. Define a data structure for holding the calculations results.
# 4. Define a class for computing the calculations given the readings data structure.
class Calculations:  
    def __init__ (self, records: ParseRecords):
        self.record_list = records.record_list
           
    def __lt__ (self, other: Record):
        return self.record < other.record
    
    def __gt__ (self, other: Record):
        return self.record > other.record
    
    def max(self, index):
        max_val = self.record_list[0].record[index]
        for rec in self.record_list:
            if rec.record[index] > max_val:
                max_val = rec.record[index]
        return max_val

    def min(self, index):
        min_val = self.record_list[0].record[index]
        for rec in self.record_list:
            if rec.record[index] < min_val:
                min_val = rec.record[index]
        return min_val
    
    def avg(self, index):
        total = 0
        count = 0
        for record in self.record_list:
            if len(record.record) > index:
                total += record.record[index]
                count += 1
        return total/count if count > 0 else 0

        
# 5. Define a class for creating the reports given the results data structure.
class CreateReports:
    def __init__ (self, records: ParseRecords):
        self.record_list = records.record_list
        self.calculate = Calculations(records)
    
    def task1 (self):
        # highest temperature and day, lowest temperature and day, most humid day and humidity
        max_temp = self.calculate.max(1)
        min_temp = self.calculate.min(3)
        most_humid = self.calculate.max(7)
        print("Max Temp: " + str(max_temp)
              + " Min Temp: " + str(min_temp)
              + " Most Humid: " + str(most_humid))
        
    def task2 (self):
        # average highest temperature, average lowest temperature, average mean humidity
        max_avg_temp = self.calculate.max(1)
        min_avg_temp = self.calculate.min(3)
        avg_humidity = self.calculate.avg(7)
        print("Max Avg Temp: " + str(max_avg_temp)
              + " Min Avg Temp: " + str(min_avg_temp)
              + " Average Humid: " + str(avg_humidity))
        
    def task3 (self):
        # bar chart of max and min temp of each day
        for day in self.record_list:
            max_temp = day.record[1]
            min_temp = day.record[3]
            
            print("\033[31m" + "*" * max_temp)
            print("\033[36m" + "*" * min_temp)
            
    def task4 (self):
        # bar chart with min and max
        for day in self.record_list:
            max_temp = day.record[0]
            min_temp = day.record[1]
            
            print("\033[36m" + "*" * min_temp, end = "")
            print("\033[31m" + "*" * max_temp)
            
        
# 6. Define main for assembling the above and running the program.
def main():
    if len(sys.argv) < 4:
        print("Format: file path method files")
        return
    
    path = sys.argv[1]
    method = sys.argv[2]
    files = sys.argv[3:]
    
    print("Path: " + path
          + " Method: " + method
          + " Files: " + str(files))
    
    records = ParseRecords(files)
    reports = CreateReports(records)

    if method == "task1":
        reports.task1()
    elif method == "task2":
        reports.task2()
    elif method == "task3":
        reports.task3()
    elif method == "task4":
        reports.task4()

if __name__ == "__main__":
    main()
