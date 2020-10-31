# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:28:27 2020

@author: jbrav
"""
msg = (input('What is your message? '))
if not msg.isalpha():
    print('Not a string')
    exit()
dig = int((input('What is your shift integer? ')))
def cCipher(a, b):
    enc = ""
    for i in a:
        ltr = ord(i)
        xltr = (ltr + b)
        cltr = chr(xltr)
        enc = enc + cltr
    print(enc)
    return

cCipher(msg, dig)












''' # The below is the trail to completion.
msg = (input('What is your message? '))

if not msg.isalpha():
    print('Not a string')
    break

dig = int((input('What is your shift integer? ')))

def cCipher(a, b):
    enc = ""
    for i in a:
        ltr = ord(i)
        xltr = (ltr + b)
        cltr = chr(xltr)
        enc = enc + cltr
    print(enc)
    return

cCipher(msg, dig)


###
msg = (input('What is your message? '))
dig = int((input('What is your shift integer? ')))

def cCipher(a, b):
     for i in a:
        enc = ""
        ltr = ord(i)
        xltr = (ltr + b)
        cltr = chr(xltr)
        enc1 = enc + cltr
        print(enc1)
        return

print(cCipher(msg, dig))
###


enc = ""
msg = (input('What is your message? '))
dig = int((input('What is your shift integer? ')))
for i in msg:
    ltr = ord(i)
    xltr = (ltr + dig)
    cltr = chr(xltr)
    enc = enc + cltr


print(enc)

'''
