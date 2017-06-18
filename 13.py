# http://www.pythonchallenge.com/pc/return/disproportional.html
import xmlrpclib

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

for m in server.system.listMethods():
    print m

print server.system.methodHelp('phone')
print server.phone('Bert')
