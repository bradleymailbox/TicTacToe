import gameOps as ga

print (range(1,3))
print(ga.feedback['welcome'])
userchar = ga.getPlayChar()

while userchar.lower() not in ga.validplaychars:
      print(ga.feedback['invalid'])
      userchar = ga.getPlayChar()
ga.displayGameChars(userchar)
ga.printboard()

winner = False
while winner == False:
    pos = ga.choosePosition()
    actpos = ga.returnBoardPosition(pos)
    if ga.getBoardChar(actpos) == '?':
        ga.boardvalues[actpos] = userchar
        print(ga.boardvalues)
        compsel = ''
        while compsel == '':
            compsel = ga.getCompSelection()           
            if ga.returnBoardPosition(compsel) == '?':
                print (f'Computer selected {compsel}')
                actpos = ga.returnBoardPosition(compsel)
                ga.boardvalues[actpos] = ga.returnOpponentChar(userchar)
                break
            else:
                compsel = ''
        ga.printboard()
    else:
        print(ga.feedback['taken'])





