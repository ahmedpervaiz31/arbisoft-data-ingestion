from parse_records import ParseRecords

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

        