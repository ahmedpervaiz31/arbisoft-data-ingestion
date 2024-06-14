from file_reader import FileReader
from record import WeatherRecord

# 2. Define a class for parsing the files and populating the records data structure with correct data types.
class ParseRecords:
    def __init__(self, filenames):
        self.record_list = []
        self.filenames = filenames
        
    def parser(self):
        file_reader = FileReader(self.filenames)
        file_data = file_reader.read_files()
        
        for file_content in file_data:
            self.populate(file_content)
        return self.record_list
    
    def is_valid_number(self, term):
        if not term:
            return 0

        valid_chars = set('0123456789.-')
        if any(char not in valid_chars for char in term):
            return 0
        
        if term.count('.') > 1:
            return 0
        
        if term.count('-') > 1 or (term.count('-') == 1 and term[0] != '-'):
            return 0
        
        return 1
    
    def populate(self, file_content): 
        # Skip the header line
        file_content = file_content[1:]  
        
        for line in file_content:
            terms = line.strip().split(",")
            
            date = terms[0]
            reading = []
            
            for term in terms[1:]:
                if self.is_valid_number(term):
                    reading.append(int(float(term)))
                else:
                    reading.append(0)
            
            # if null record
            if sum(reading) == 0:
                continue
            
            self.record_list.append(WeatherRecord(date, reading))