from zipfile import ZipFile

def dezip(fileName):

    file = fileName

    with ZipFile(file, 'r') as zip: 
        # extraire tous les fichiers vers un autre répertoire
        zip.extractall('data')