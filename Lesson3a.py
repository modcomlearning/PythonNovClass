
phone ={
    "ram":"4gb",
    "color":"blue",
    "cost": 12000,
    "os":"Android"
}

print(phone)
print(type(phone))
del phone['os']
phone['ram'] = "8gb"
phone['model'] = "Infinix"
print(phone)

try:
    print(phone['color'])

except Exception as error:
    print("Error Occured ", error)
