import numpy as np
array = [1,2,3,4,5,6,7,8,9]
currentPlayer = "X"
def changer(ay):
    string = ""
    div3 = 0
    for x in ay:
        div3 += 1
        string += str(x) + ' '
        if div3 % 3 == 0:
            string += "\n"
    return string

def checker(ay):
    #for x in ay:
    check = np.reshape(ay,(3,3))
    if "['X' 'X' 'X']" in ((str(check.diagonal())),str((np.diagonal(np.fliplr(check)))), str(check[:,0]), str(check[:,1]), str(check[:,2]), str(check[0]), str(check[1]), str(check[2])):
        return False
    if "['O' 'O' 'O']" in (str((check.diagonal())),str((np.diagonal(np.fliplr(check)))), str(check[:,0]), str(check[:,1]), str(check[:,2]), str(check[0]), str(check[1]), str(check[2])):
        return False
    if not (bool(set(array).intersection([1,2,3,4,5,6,7,8,9]))):
        return "Tie"
    else:
        return True # for now
check = True
print("Player One:")
while check:
    while True:
        try:
            ans = int(input('Where do you want to place your ' + currentPlayer + '?\n' + changer(array)))
        except ValueError:
            print("This is an incorrect number. Try again.")
        else:
            if ans > 9 or ans < 1:
                print("Please type a number between 1 and 9.")
            else:
                if not isinstance(array[ans - 1], int):
                    print("This has already been claimed.")
                else:
                    break
    array[ans-1] = currentPlayer
    print(changer(array))
    check = checker(array)
    if check == True:
        if currentPlayer == "X":
            currentPlayer = "O"
            print("Player Two:")
        else:
            currentPlayer = "X"
            print("Player One:")
    else:
        if check == "Tie":
            print("It's a tie!")
            check = False
        else:
            if currentPlayer == "X":
                print("X wins!")
            else:
                print("O wins!")