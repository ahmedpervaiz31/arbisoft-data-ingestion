from create_reports import CreateReports
from parse_records import ParseRecords
import datetime

class Engine:
    def __init__ (self, query):
        self.query = query
        
    def assemble_args(self):
        # reads and parses the agruments
        # if query is year then generate all files for the months
        # store the method and the path/month filename
        # call ParseRecords on the files
        # call CreateReports on the method plus the record
        
        if len(self.query) < 4:
            print("Format: file path method files")
            return

        # stores path and checks if it ends with '/' otherwise inserted
        path = self.check_path(self.query[1])
        
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

    def check_path(self, path):
        size = len(path)
        if path[size-1] != '/':
            path += '/'
        return path