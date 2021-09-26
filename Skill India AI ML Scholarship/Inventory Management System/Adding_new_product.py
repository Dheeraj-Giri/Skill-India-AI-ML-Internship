import json
# Read the data from the json file. : 

fd = open("record.json",'r')
r = fd.read()
fd.close()

record = json.loads(r)

# Add New Item into Inventory : 

prod_id = str(input("Enter product id : \n"))
name = str(input("Enter name : \n"))
pr = int(input("Enter price : \n"))
qn = int(input("Enter quantity : \n"))

record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(record)

# write the record into json file
fd = open("record.json",'w')
fd.write(js)
fd.close() 