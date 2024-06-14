import datetime
import os
from create_reports import CreateReports
from record_collection import RecordCollection

class Engine:
    def __init__ (self, query):
        self.query = query
        
    def check_method(self):
        valid_methods = ['-a', '-e', '-b', '-c']
        for word in self.query:
            if word[0] == '-' and word not in valid_methods:
                print("Use correct method:", str(valid_methods))
                return 0
        if not any(word[0] == '-' for word in self.query):
            print("No method given")
            return 0
        return 1
    
    def check_path(self):
        user_path = self.query[1]
        if user_path not in str(range (0,10)) and user_path[0] != '-':
            if not os.path.exists(user_path):
                print("Path does not exist.")
                return 0
            
            index = len(user_path) - 1
            if user_path[index] != '/':
                user_path += '/'
                print("Fixed path")
                self.query[1] = user_path
        else:
            # if no path given then initialise it to ""
            temp_query = self.query[0] + "" 
            for query in self.query[2:]:
                temp_query = temp_query + query
            self.query = temp_query
            print("No path given - automatically assumed")
        return 1
            
    def check_date(self):
        valid_chars = set('0123456789/')
        found_date = 0

        for word in self.query:
            if all(char in valid_chars for char in word):
                found_date = 1
                break

        if not found_date:
            print("No date given")
            return 0
        
        for word in self.query:
            # didnt find a number
            if not word.isdigit() or '/' not in word:
                continue
            
            # if date is YYYY or YYYY/M or YYYY/MM
            if len(word) not in [4, 6, 7]:
                print(word)
                print("Date format wrong")
                return 0
            
            year = ""
            #YYYY/MM
            if '/' in word:
                slash_index = word.index('/')
                
                year = word[:slash_index]
                month = word[slash_index + 1:]
                
                if int(month) > 12 or int(month) < 0:
                    print("More than 12 or less than 0 month not possible")
                    return 0 
                
            #YYYY
            else:
                year = word
                                
            curr_year = datetime.datetime.now().year
                
            if int(year) > curr_year or int(year) < 0:
                print("Year is incorrect")
                return 0
        return 1
            
    def check_validity_args(self):      
        if not self.check_method() or not self.check_path() or not self.check_date():
            return 0
        
        return 1
    
    def assemble_args(self):
        # reads and parses the agruments
        # if query is year then generate all files for the months
        # store the method and the path/month filename
        # call ParseRecords on the files
        # call CreateReports on the method plus the record
        
        if not self.check_validity_args():
            return
        
        for i, word in enumerate(self.query):
            method = []
            files = []
            
            if word[0] != "-":
                continue
            
            method = word
                
            path = self.query[1]
            files = self.file_name_generator(path, i)
                
            record_collection = RecordCollection(files)
            record_list = record_collection.get_record()
            reports = CreateReports(record_list, method)
        
    def file_name_generator(self, path, i):
        files = []
        for x in self.query[i + 1:]:
            # if approach another method then break
            if x[0] == '-':
                break
            
            #if YYYY/MM
            if '/' in x: 
                year, month = x.split('/')
                month_abbr = datetime.date(int(year), int(month), 1).strftime('%b')        
                files.append(path + f"Murree_weather_{year}_{month_abbr}.txt")
            else:
                year = int(x)
                files.extend([path + f"Murree_weather_{year}_{datetime.date(year, month, 1).strftime('%b')}.txt" 
                              for month in range(1, 13)])
        return files

