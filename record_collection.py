from parse_records import ParseRecords

class RecordCollection:
    def __init__(self, filenames):
        self.record_list = []
        self.filenames = filenames
        self.add_record()
    
    def add_record(self):
        parse_records = ParseRecords(self.filenames)
        self.record_list = parse_records.parser()
    
    def get_record(self):
        return self.record_list

