def PrintBoard(x,y):
    i=0
    j=0
    dashes=""
    while i < len(y):
        if(i+1!=len(y)):
            print("     {p}").format(p=i+1),
        else:
            print("     {p}").format(p=i+1)
        i+=1
        
    i=0    
    while i < len(y):
        dashes+="--------"
        i+=1
        
    i=0
    print(dashes)
    while i < len(x):
        print("{p}:").format(p=i+1),
        while j < len(y):
            temp=x[i][j]
            if(j+1!=len(y)):
                print(" | {t} |".format(t=temp)),
            else:
                print(" | {t} |".format(t=temp))
            j+=1
        i+=1
        print(dashes)
        j=0

def checkWin(x,y):
    
    if  (x[0][0]==y and x[0][1]==y and x[0][2]==y):
        return True
    elif(x[2][0]==y and x[2][1]==y and x[2][2]==y):
        return True
    elif(x[0][0]==y and x[1][0]==y and x[2][0]==y):
        return True
    elif(x[0][2]==y and x[1][2]==y and x[2][2]==y):
        return True
    elif(x[0][0]==y and x[1][1]==y and x[2][2]==y):
        return True
    elif(x[0][2]==y and x[1][1]==y and x[2][0]==y):
        return True
    elif(x[0][1]==y and x[1][1]==y and x[2][1]==y):
        return True
    elif(x[1][0]==y and x[1][1]==y and x[1][2]==y):
        return True
    else:return False
    

def FillBoard(rows,cols):
    global x
    i=0
    j=0
    while i < rows:
        x=x+[[]]
        j=0
        while j < cols:
            x[i]=x[i]+["_"]
            j+=1
        i+=1

        


choice="y"
while(choice=="y" or choice=="Y"):
    print("Let's Play :D ... ")
    x=[]
    FillBoard (3,3)
    PrintBoard(x,x[0])
    P2=True;
    P1=True;
    while(True):
        #Start Player One
        if(P2==True):
            P1=False
            print("Player One's Move: Adding (X)")
            m=input("Row: ")
            n=input("Col: ")
            if (m-1<len(x) and (n-1<len(x[0]))):
                if(x[m-1][n-1]!="O" and x[m-1][n-1]!="X"):
                    x[m-1][n-1]="X"
                    #clear_output()
                    PrintBoard(x,x[0])
                    if(checkWin(x,"X")==True):
                        break;
                    P1=True;
                else:
                    print("Position Is not Available")
            else:
                print("out Of range")


        #Start Player One
        if(P1==True):
            P2=False
            print("Player Two's Move: Adding (O)")
            m=input("Row: ")
            n=input("Col: ")
            if (m-1<len(x) and (n-1<len(x[0]))):
                if(x[m-1][n-1]!="O" and x[m-1][n-1]!="X"):
                    x[m-1][n-1]="O"
                    #clear_output()
                    PrintBoard(x,x[0])
                    if(checkWin(x,"O")==True):
                        break;
                    P2=True;
                else:
                    print("Position Is not Available")
            else:
                print("out Of range")

    if(P1==False and P2==True):
        print("player one wins")
    else:
        print("player Two wins")
    choice=raw_input("Do you want to play again? y/n")
    