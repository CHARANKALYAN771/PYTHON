c= input("enter the name:")
a=input("enter the address:")
p=int(input("enter ph no. :"))
lquant=[]
lprice=[]
litem=[]
a=20
j=0
from datetime import date
k=1
while(k!=0):
    #for i in range(0,n+1):
        j=0
        q= input("enter the item name:")
        litem.append(q)
        w=int(input("enter the quant:"))
        lquant.append(w)
        e=int(input("enter the price"))
        lprice.append(e)
        j=j+1
        k=int(input(" 1 for new item , 0 for end "))  
total=sum(lprice)


print()
print()
n=j
def output(n):
    for i in range(0,n+1):
        print(i+1," "*a , litem[i]," "*(a+2-len(litem[i])) , lquant[i] ," "*(a+7) , lprice[i])
cd=date.today()

#####################################################   main pro:   ##############################################

print("*"*100)
ck = "charan kalyan "
print(ck.center(100," "))
print("nama      :",c)
print("address   :",a)
print("phone no. :", p)
print(date.today())
# print(cd.strftime("%Y"),cd.strftime("%B"),cd.strftime("%H"),cd.strftime("%M"),cd.strftime("%S"))
print()
print("SN0."+" "*a+"ITEM"+" "*a+" QUANTITY"+" "*a+"PRICE")
output(n)
print()
print(" "*71,"total:",total)
print("*"*100)
