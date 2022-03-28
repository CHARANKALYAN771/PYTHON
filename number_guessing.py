
def fun(i):
        x=int(input("gues a value :"))

        if x==1 or x==2 or x==3 or  x==4 or x==5:
            print("u won the game:")
            
        else:
            print("nope! bettre luck nxt tym u have ",3-i,"left")
            if 3-i==0:
                print("u have one last chance")
            while i<3 and i>=0:
                i+=1
                fun(i)
                

def main():
     
     i=1
    #  while(i<=3):
     fun(i)
        #  i+=1

main()