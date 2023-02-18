# coding: utf-8
#envoie des requêtes au serveur

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send("Hey my name is Olivier!")

print "Close"
socket.close()

#utiliser plutôt ici un threader
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1111))

print("Le nom du fichier que vous voulez récupérer:")
file_name = input(">> ") # utilisez raw_input() pour les anciennes versions python
s.send(file_name.encode())
file_name = 'data/%s' % (file_name,)
r = s.recv(9999999)
with open(file_name,'wb') as _file:
    _file.write(r)
print("Le fichier a été correctement copié dans : %s." % file_name)
