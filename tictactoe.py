def sum(a,b,c):
    return a+b+c

def printboard(first,second):
    zero='X' if first[0] else ('O' if second[0] else 0)
    one='X' if first[1] else ('O' if second[1] else 1)
    two='X' if first[2] else ('O' if second[2] else 2)
    three='X' if first[3] else ('O' if second[3] else 3)
    four='X' if first[4] else ('O' if second[4] else 4)
    five='X' if first[5] else ('O' if second[5] else 5)
    six='X' if first[6] else ('O' if second[6] else 6)
    seven='X' if first[7] else ('O' if second[7] else 7)
    eight='X' if first[8] else ('O' if second[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkwin(first,second):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[3,5,8],[0,4,8],[2,4,6],[2,5,8]]
    for win in wins:
        if(sum(first[win[0]],first[win[1]],first[win[2]])==3):
            print("X won")
            return 1
        if(sum(second[win[0]],second[win[1]],second[win[2]])==3):
            print("Y won")
            return 0
    return -1
    
c=0
print("Welcome to the TIC TAC TOE")
first=[0,0,0,0,0,0,0,0,0]
second=[0,0,0,0,0,0,0,0,0]
turn=1
while(True):
    printboard(first,second)
    if(turn==1):
        print("X's chance")
        value=int(input("enter the position for X "))
        first[value]=1
    else:
        print("O's chance")
        value=int(input("enter the position for O "))
        second[value]=1
    chwin=checkwin(first,second)
    if(chwin!=-1):
        print("Match Over")
        break
    turn=1-turn
    c=c+1
    if(c==9):
        print("draw")
        break