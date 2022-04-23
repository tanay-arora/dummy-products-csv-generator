import csv

with open('./subcategory.csv' ,'w', newline='')as file:
    writer=csv.writer(file)
    writer.writerow([{"title":"","slug":""}])