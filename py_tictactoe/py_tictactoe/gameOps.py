import os
import random as r

feedback = {
    'welcome':'Welcome to Tic Tac Toe!',
    'invalid':'Invalid selection made!',
    'finish':'Good bye!',
    'taken': 'Sorry! Position already taken'
    }

validplaychars = ['x','o']
boardvalues = ['?']*9
rowrange = [1,2,3]

def getPlayChar():
    playchar = input('Enter a play char:')
    return playchar.lower()

def choosePosition():
    position = input('Enter a position to play - E.g T1 or m2 or B3 :')
    return position

def getCompSelection():
    col = r.randint(0,2)
    row = r.randint(0,2)
    print(col)
    print(row)

    colsel = ''
    rowsel = 0
    compselect = ''

    if col == 0:
        colsel = 't'
    elif col ==1:
        colsel = 'm'
    else:
        colsel = 'b'
   
    if row == 0:
        rowsel = '1'
    elif row == 1:
        rowsel == '2'
    else:
        rowsel = '3'
    
    compsel = str(colsel) + str(rowsel)
    return compsel

def returnBoardPosition(pos):
    retpos = 0
    row = pos[0]
    col = int(pos[1])
    if col in rowrange:
        if row.lower() == 't':    
            retpos = int(pos[1]) - 1
        elif row.lower() == 'm':
            retpos = 3+int(pos[1]) - 1
        elif pos[0].lower() == 'b':
            retpos = 6+int(pos[1]) - 1
    return retpos

def getBoardChar(pos):
    return boardvalues[pos]

def displayGameChars(userchar):
    if userchar == 'x':
        print (f'User = {validplaychars[0]} - Computer = {validplaychars[1]}')
    else:
        print (f'User = {validplaychars[1]} - Computer = {validplaychars[0]}')

def returnOpponentChar(char):
    if char.lower() == 'x': 
        return 'O' 
    else: 
        return 'X'
       
def printboard():
   # os.system('cls')
    print('   1 2 3')
    print('  +-----+')
    print(f'T |{boardvalues[0]}|{boardvalues[1]}|{boardvalues[2]}|')
    print('  +-----+')
    print(f'M |{boardvalues[3]}|{boardvalues[4]}|{boardvalues[5]}|')
    print('  +-----+')
    print(f'B |{boardvalues[6]}|{boardvalues[7]}|{boardvalues[8]}|')
    print('  +-----+')

