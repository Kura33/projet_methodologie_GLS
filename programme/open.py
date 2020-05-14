import csv
import glob
import pandas as pd

def open():
    list_file = glob.glob('**/*.csv', recursive="true")
    for i in range(len(list_file)):
        data_frame=pd.read_csv(list_file[i])
        print(data_frame[['Date', 'HomeTeam', 'AwayTeam']])

