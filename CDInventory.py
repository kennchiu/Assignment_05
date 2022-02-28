#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KChiu, 2022-Feb-27, Add codes to complete the CD Inventory program
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODone replace list of lists with list of dicts
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # TODone Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2] }
            lstTbl.append(dicRow)
        objFile.close()
    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['ID'], row['CD Title'], row['Artist'], sep = ', ')
    elif strChoice == 'd':
        # TODone Add functionality of deleting an entry
        # Creeate a list of all the CD IDs.
        id_lst = []
        for row in range(len(lstTbl)):
            row_id = lstTbl[row]['ID']
            id_lst.append(row_id)
        # Ask user which ID to be deleted based on ID number
        del_key = int(input('Which CD do you want to delete? \
                            \nPlease enter a CD ID: '))
        if del_key not in id_lst:
            # Raise an error if CD ID doesn't exist.
            print('Boooo! CD doesn\'t exist!')
            pass
        for row in range(len(lstTbl)):
            try:
                if lstTbl[row]['ID'] != del_key:
                    pass
                else:
                    del lstTbl[row]
            except:
                pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')