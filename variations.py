import csv
import random
print('enter your number')
n=input('_ ')
with open('./variations.csv','w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(["id","value","order_limit","stock_left","is_main","is_offer","points","mrp","price","discount_price","discount_percentage"	])

    for i in range(1,int(n)):
        if(i<=150):
            offer=1
        else:
            offer=""
        if(i%2==0):
            mrp=random.randint(20,1000)
            price=random.randint(12,mrp)
            discount_price=random.randint(6,price)
            weight=random.randint(1,5)
            writer.writerow([i,str(weight)+"KG",str(random.randint(1,15)),str(random.randint(0,40)),"0",offer,str(random.randint(0,5)),str(mrp),str(price),str(discount_price),])
        elif(i%2!=0):
            mrp=random.randint(1500,6000)
            price=random.randint(1200,mrp)
            discount_price=random.randint(1000,price)
            weight=random.randint(6,20)
            writer.writerow([i,str(weight)+"KG",str(random.randint(1,15)),str(random.randint(0,40)),"0",offer,str(random.randint(0,5)),str(mrp),str(price),str(discount_price),])