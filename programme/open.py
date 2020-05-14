import csv
with open('F1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['HomeTeam'], ":", row['FTHG'], "|",row['AwayTeam'], ':', row['FTAG'])