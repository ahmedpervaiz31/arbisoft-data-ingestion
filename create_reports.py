from calculations import Calculations
from parse_records import ParseRecords

# 5. Define a class for creating the reports given the results data structure.
class CreateReports:
    def __init__ (self, records: ParseRecords, method):
        self.record_list = records.record_list
        self.calculate = Calculations(records)
        self.method = method
        
        self.operate()
    
    def operate(self):
        if self.method == "-e":
            self.task1()
        elif self.method == "-a":
            self.task2()
        elif self.method == "-c":
            self.task3()
        elif self.method == "-b":
            self.task4()
    
    def task1 (self):
        # highest temperature and day, lowest temperature and day, most humid day and humidity
        max_temp = self.calculate.max(1)
        min_temp = self.calculate.min(3)
        most_humid = self.calculate.max(7)
        
        print("Max Temp: ", max_temp)
        print("Min Temp: ", min_temp)
        print("Most Humid: ", most_humid)
        
    def task2 (self):
        # average highest temperature, average lowest temperature, average mean humidity
        max_avg_temp = self.calculate.max(1)
        min_avg_temp = self.calculate.min(3)
        avg_humidity = self.calculate.avg(7)
        
        print("Max Avg Temp: ", max_avg_temp) 
        print("Min Avg Temp: ", min_avg_temp) 
        print("Average Humid: ", avg_humidity)
        
    def task3 (self):
        # bar chart of max and min temp of each day
        for i, day in enumerate(self.record_list):
            max_temp = day.record[1]
            min_temp = day.record[3]
            
            date = self.record_list[i].date
            
            print(date, "\033[31m"
                  + "*" * max_temp,
                  max_temp)
            
            print(date, "\033[36m" 
                  + "*" * min_temp,
                  min_temp)
                  
        print("\033[39m")
            
    def task4 (self):
        # bar chart with min and max
        for i, day in enumerate(self.record_list):            
            max_temp = day.record[0]
            min_temp = day.record[1]
            
            date = self.record_list[i].date
            
            print("\033[39m", date, end = "")
            print("\033[36m", "*" * min_temp, end = "")
            print("\033[31m"+ "*" * max_temp, end = "")
            print("\033[39m", " ", max_temp, "-", min_temp)
        print("\033[39m")
            