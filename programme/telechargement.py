import urllib.request

def downloadfile():
    url = "https://www.football-data.co.uk/mmz4281/1920/data.zip"
    urllib.request.urlretrieve(url, "/Users/kurazul/Documents/Cours CESI/methodologie logicielle/tp/projet_methodologie_GLS/programme/telechargement/data.zip")
    print('Download succed')