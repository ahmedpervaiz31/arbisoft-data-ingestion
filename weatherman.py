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
            
            # IGNORE EMPTY READINGS 
            if sum(readings) == 0:
                continue
            
            # create record object
            record = Record(date, readings)
            # append into record_list
            self.record_list.append(record)  

# 3. Define a data structure for holding the calculations results.
# 4. Define a class for computing the calculations given the readings data structure.
class Calculations:  
    def __init__ (self, records: ParseRecords):
        self.record_list = records.record_list
    
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
        print("Max Temp: ", max_temp,
              "Min Temp: ", min_temp,
              "Most Humid: ", most_humid)
        
    def task2 (self):
        # average highest temperature, average lowest temperature, average mean humidity
        max_avg_temp = self.calculate.max(1)
        min_avg_temp = self.calculate.min(3)
        avg_humidity = self.calculate.avg(7)
        print("Max Avg Temp: ", max_avg_temp, 
              "Min Avg Temp: ", min_avg_temp, 
              "Average Humid: ", avg_humidity)
        
    def task3 (self):
        # bar chart of max and min temp of each day
        for i, day in enumerate(self.record_list):
            max_temp = day.record[1]
            min_temp = day.record[3]
            
            print(self.record_list[i].date, 
                  "\033[31m" + "*" * max_temp,
                  max_temp)
            
            print(self.record_list[i].date, 
                  "\033[36m" + "*" * min_temp,
                  min_temp)
                  
        print("\033[39m")
            
    def task4 (self):
        # bar chart with min and max
        for i, day in enumerate(self.record_list):
            max_temp = day.record[0]
            min_temp = day.record[1]
            
            print(self.record_list[i].date, 
                  "\033[36m" + "*" * min_temp, end = "")
            print("\033[31m" + "*" * max_temp, end = "")
            print(" ", max_temp, "-", min_temp)
        print("\033[39m")
            
class Engine:
    def __init__ (self, query):
        self.query = query
        
    def assemble_args(self):
        # reads and parses the agruments
        if len(self.query) < 4:
            print("Format: file path method files")
            return

        #possibilities:
# weatherman.py /path/to/files-dir -c 2011/03 -a 2011/3 -e 2011
# weatherman.py /path/to/files-dir -a 2005/6
# weatherman.py /path/to/files-dir -e 2002 2004

# if query is year then generate all files for the months
        # store the method alongside the month files (updated with path)
        # call ParseRecords on the files
        # call CreateReports on the method plus the record
        
        # stores path
        path = self.query[1]
        
        for i, word in enumerate(self.query):
            method = []
            file = []
            
            if word[0] == "-":
                method = word
                
                self.file_name_generator(path, file, i)
                
                record = ParseRecords(file)
                reports = CreateReports(record, method)
        
    def file_name_generator(self, path, file, i):
        for x in self.query [i+1:]:
            if x[0] == '-':
                # when approach another method then break
                break
            
            if '/' in x: 
                # both year and month passed
                terms = x.split('/')
                year = terms[0]
                month = terms[1]
                            
                month_abbr = datetime.date(int(year), int(month), 1).strftime('%b')        
                    
                file.append(path + "Murree_weather_"
                            + str(year) + "_"
                            + month_abbr + ".txt")
            else:
                # only year passed
                year = int(x)
                for month in range(1,13):
                    month_abbr = datetime.date(year, month, 1).strftime('%b')
                    file.append(path + "Murree_weather_"
                                + str(year) + "_"
                                + month_abbr + ".txt")

# 6. Define main for assembling the above and running the program.
def main():
    engine = Engine(sys.argv)
    engine.assemble_args()


if __name__ == "__main__":
    main()
