from record import Record

# 2. Define a class for parsing the files and populating the readings data structure with correct data types.
class ParseRecords:
    def __init__ (self, filenames):
        self.record_list = []
        for file in filenames:
            try: 
                with open(file, "r") as f:
                    self.populate(f)
            except:
                print("File", file, "does not exist.")
            
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
                if term:
                    reading = int(float(term))
                    readings.append(reading)
                else:
                    readings.append(0)
            
            # IGNORE EMPTY READINGS 
            if sum(readings) == 0:
                continue
            
            # create record object
            record = Record(date, readings)
            # append into record_list
            self.record_list.append(record)  
