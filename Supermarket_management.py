from datetime import datetime
name = input("Enter Your Name : ")
print()
#available items in shop
list = '''
    Rice       Rs 20/Kg
    Sugar      Rs 30/Kg
    Salt       Rs 20/Kg
    Milk       Rs 50/liter
    Oil        Rs 120/Kg
    Paneer     Rs 110/Kg
    Boost      Rs 299/Kg
    Colgate    Rs 85/Kg
'''
price = 0
pricelist=[]
Total_price=0
Final_Price=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items = {
    'Rice':20,
    'Sugar':30,
    'Salt':20,
    'Milk':50,
    'Oil':120,
    'Paneer':110,
    'Boost':299,
    'Colgate':85
}
option = int(input("For List Of Items press 1 : "))
if option==1:
    print(list)
for i in range(len(items)):
    input1=int(input("If You Want To Buy Press 1 OR 2 For Exit : "))
    if input1==2:
        break
    if input1==1:
        item = input("Enter Your Items : ")
        quantity = int(input("Enter Quantity : "))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,price))
            Total_price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (Total_price*5)/100
            Final_Price=gst+Total_price
        else :
            print("You Entered Item Is Corrently Not Available")
    else :
        print("You Entered Wrong Number")
    inp=input("Can I Bill The Items Yes or No : ")
    if inp=='yes':
        pass
        if Final_Price!=0:
            print(30*"=","Super Market",30*"=")
            print(30*" ","***Eluru***")
            print("Name :",name,25*" ","Date :",datetime.now())
            print(75*"-")
            print("S.No ",8*" ","Items",8*" ","Quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,12*" ",ilist[i],11*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalPrice:','Rs',Total_price)
            print("GST Amount: ",49*" ",'Rs',gst)
            print(75*"-")
            print(50*" ","FinalPrice:",'Rs',Final_Price)
            print(75*"-")
            print(20*" ","*******Thanks For Shopping*******")
            print(75*"-")
    elif inp=='no':
        print("Thanks For Visiting......")
        break

