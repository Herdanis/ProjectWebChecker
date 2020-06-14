def getListFile(fileName):
    with open(fileName) as file:
        """
        1. fileName = File location
        Get List Data From txt File 
        """
        listFile = file.read()
        listFile = listFile.splitlines()
        return listFile
