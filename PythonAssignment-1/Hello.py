


mylist = ['dasd','sdasd','adsasa']
mylist.append('xsd')
mylist.append('xsdssdd')
mylist.append('xsdssdd')
for value in mylist:
    if(value.find('s') == 1):
        mylist.remove(value)

print(mylist)


