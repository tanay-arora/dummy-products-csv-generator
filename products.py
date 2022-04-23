import csv
import random

number=299
brandlength=100
description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus in lacinia libero. Nulla sit amet convallis nunc. Vivamus sed ultricies sem."
featuredImage=["not assigned","products/test/test.jpg", "products/test/test_31KTRso.jpg", "products/test/test_qRkvR6t.jpg", "products/test/test_fBPlGwn.jpg", "products/test/test_7fr8juG.jpg", "products/test/test.webp", "products/test/test_bNKGkSY.webp", "products/test/test_JAWzTel.webp", "products/test/test_cyHq7Qh.webp", "products/test/test_VtlklVW.webp", "products/test/test_XTWljcQ.jpg", "products/test/test_13lxXId.jpg", "products/test/test_KUx2OxV.jpg", "products/test/test_Jo25JkP.jpg", "products/test/test_aLBH1dT.jpg", "products/test/test_RJMLKMW.webp", "products/test/test_hcdpXA9.jpg", "products/test/test_s4JtHCr.webp", "products/test/test_QgEvjJW.jpg", "products/test/test_lQN8p36.jpg" ]

numList=[
    {"id":1,"subId":[
        1,2,3,4,5,6,7,8,9,10
    ]},
    {"id":3,"subId":[
        11,12,13,14,15,16,17,18,19,20
    ]},
    {"id":4,"subId":[
        21,22,23,24,25,26,27,28,29,30
    ]},
    {"id":5,"subId":[
        31,32,33,34,35,36
    ]},
    {"id":6,"subId":[
        37,38,39,40,41,42
    ]},
    {"id":7,"subId":[
        43,44,45,46,47,48
    ]},
    {"id":8,"subId":[
        49,50,51,52,53,54,55
    ]},
    {"id":10,"subId":[
        56,57,58,59,60,61,62,63,64
    ]},
    {"id":11,"subId":[
        65,66,67,68,69,70,71,72
    ]},
    {"id":15,"subId":[
        73,74,75,76,77
    ]},
    {"id":17,"subId":[
        86,87,88,89,90,91,92,93,94,95,96,97
    ]},
    {"id":18,"subId":[
        98,99,100
    ]},
    {"id":19,"subId":[
        83,84,85
    ]},
]

with open('./products.csv','w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(["id", "product_id",	"title",	"brand",	"category",	"subcategory",	"description",	"image",	"slug",	"variations",	"offers",	"is_active",	"keyspecs",	"timestamp",	"origin",	"images"	])
    x=0
    y=30
    z=5
    id=0
    for cat in numList:
        category=str(cat["id"])
        for subcat in (cat["subId"]):
            subcategory=str(subcat)
            for i in range(1,12):
                if(x>=20):
                    x=0
                if(y>=int(number)):
                    y=30
                if(z>=25):
                    z=10
                x=x+1
                z=z+5
                id=id+1
                brand=random.randint(1,int(brandlength))
                variation=str(y+1)+','+str(y+2)+','+str(y+3)
                y=y+3
                images=str(z)+','+str(z+1)+','+str(z+2)+','+str(z+3)+','+str(z+4)+','
                if(id<100 and id%2==0):
                    offers=random.randint(1,30)
                else:
                    offers=""
                writer.writerow([id,"PRDCT"+str(id),"test product "+str(id),brand, category,	subcategory,	description , str(featuredImage[x]),'' , variation,offers,"1", "2,4,5",'' ,	"IN",	images ])
        