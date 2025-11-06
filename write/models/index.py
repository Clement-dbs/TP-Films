import csv
def last_index():
    with open('write/data/movies.csv',encoding='utf-8') as f:
        reader = csv.reader(f)
        last_row = None
        for row in reader:
            last_row = row 
            print(row)

    if last_row:
        return int(last_row[0])
