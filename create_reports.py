from calculations import Calculations
from record_collection import RecordCollection

# 5. Define a class for creating the reports given the results data structure.
class CreateReports:
    def __init__ (self, records, method):
        self.record_list = records
        self.calculate = Calculations(records)
        self.method = method
        
        self.task_map = {
            "-e": self.maxmin_temp_humid,
            "-a": self.average_temp_humid,
            "-c": self.graph_daily_temp,
            "-b": self.graph_bonus_temp
        }
        
        self.operate()
    
    def operate(self):
        task_function = self.task_map.get(self.method)
        task_function()
    
    def maxmin_temp_humid (self):
        # highest temperature and day, lowest temperature and day, most humid day and humidity
        max_temp = self.calculate.max_record(1)
        min_temp = self.calculate.min_record(3)
        most_humid = self.calculate.max_record(7)
        
        print(f"Max Temp: {max_temp}")
        print(f"Min Temp: {min_temp}")
        print(f"Most Humid: {most_humid}")  
        
    def average_temp_humid (self):
        # average highest temperature, average lowest temperature, average mean humidity
        max_avg_temp = self.calculate.max_record(1)
        min_avg_temp = self.calculate.min_record(3)
        avg_humidity = self.calculate.avg_record(7)
        
        print(f"Max Avg Temp: {max_avg_temp}") 
        print(f"Min Avg Temp: {min_avg_temp}") 
        print(f"Average Humid: {avg_humidity}")
        
    def graph_daily_temp (self):
        # bar chart of max and min temp of each day
        for i, day in enumerate(self.record_list):
            max_temp = day.reading[0]
            min_temp = day.reading[2]
            
            date = self.record_list[i].date
            
            print("\033[39m", date, end = "")
            print("\033[31m" + "*" * max_temp, max_temp)
            
            print("\033[39m", date, end = "")
            print("\033[36m" + "*" * min_temp, min_temp)
                  
        print("\033[39m")
            
    def graph_bonus_temp (self):
        # bar chart with min and max
        for i, day in enumerate(self.record_list):            
            max_temp = day.reading[0]
            min_temp = day.reading[2]
            
            date = self.record_list[i].date
            
            print("\033[39m", date, end = "")
            print("\033[36m", "*" * min_temp, end = "")
            print("\033[31m"+ "*" * max_temp, end = "")
            print("\033[39m", " ", max_temp, "-", min_temp)
        print("\033[39m")
            