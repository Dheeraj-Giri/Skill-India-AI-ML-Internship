import json

fd = open("record.json",'r')
r = fd.read()
fd.close()

records = json.loads(r)


# Taking  input what user want to purches : 
ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))

print("==============================")
print("Product          : ", records[ui_prod]['name'])
print("Price            : ", records[ui_prod]['pr'])
print("==============================")
print("Billing Amount   : ", records[ui_prod]['pr'] * ui_quant)
print("==============================")
print("Thank you for purchasing product...")
print("Have a good day ")

records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant




# update the inventory after the purchesing : 
js = json.dumps(records)

fd = open("record.json",'w')
fd.write(js)
fd.close()

{'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}

sales = {1 : {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant},
         2 : {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant},
         3 : {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}}

sale = json.dumps(sales)