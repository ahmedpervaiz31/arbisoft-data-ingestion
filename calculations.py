# 3. Define a data structure for holding the calculations results.
# 4. Define a class for computing the calculations given the records data structure.
class Calculations:  
    def __init__ (self, records):
        self.record_list = records
    
    def max_record(self, index):
        return max(rec.reading[index] for rec in self.record_list)

    def min_record(self, index):
        return min(rec.reading[index] for rec in self.record_list)    
    
    def avg_record(self, index):
        total = 0
        count = 0
        for record in self.record_list:
            if len(record.reading) > index:
                total += record.reading[index]
                count += 1
        return total/count if count > 0 else 0

        