import random
import os
os.system('clear')
names = ["culture","flag","mother","goat","father","habit","life","kite","fight","land","animal","india","gandhi","nature","pets","plant","computer","capture","rust","earth"]
key = [1,2,3,4,5]
plaintext = random.choice(names)
shift = random.choice(key)
ct = []
replaced = []
data = plaintext
def encrypt(plaintext,shift):
     for ch in plaintext.lower():
         if ch.isalpha():
             alphabet = ord(ch) + shift
             finalletter = chr(alphabet)
         ct.append(finalletter)
     ciphertext = ''.join(ct)
     print(ciphertext)
     return decrypt(ciphertext)
     clt = list(task)
def decrypt(ciphertext):
     ChangedPlainText = EncryptedText = ciphertext
     while ChangedPlainText != data:
         clt = list(ChangedPlainText)
         command = input("press 'enter' to continue/'end' to exit:")
         if command == "end":
             print("THE WORD IS " + data)
             return "YOU LOST TO GUESS THE WORD"
         else:
             count = 0
             a = input("replace at :")
             b = input("replace by :")
             p1 = int(input("enter position :")) - 1
             for ch in EncryptedText:
                 if ch == a:
                     count += 1
             if count == 0:
                 print("ERROR. THERE IS NO " + a + " IN CIPHERTEXT")
                 changedCipherText = ChangedPlainText
             elif count == 1:
                 if a in list(ChangedPlainText):
                     if b in list(data):
                         if data.index(b) == EncryptedText.index(a) and p1 == data.index(b):
                             clt.insert(p1,b)
                             clt.pop(p1+1)
                             changedCipherText = ''.join(clt)
                         else:
                             print("CORRECT LETTER BUT WRONG POSITION")
                             changedCipherText = ChangedPlainText
                     else:
                         print("WRONG GUESS")
                         changedCipherText = ChangedPlainText
             else:
                 p2 = int(input("enter second position"))
                 if a in list(ChangedPlainText):
                     if b in list(data):
                         if data.index(b) == EncryptedText.index(a) and p1 == data.index(b):
                             clt.insert(p1,b)
                             clt.pop(p1+1)
                             changedCipherText = ''.join(clt)
                             clt.insert(p2-1,b)
                             clt.pop(p2)
                             changedCipherText = ''.join(clt)
                         else:
                             print("CORRECT LETTER BUT WRONG POSITION")
                             changedCipherText = ChangedPlainText
                     else:
                         print("WRONG GUESS")
                         changedCipherText = ChangedPlainText
             ChangedPlainText = changedCipherText
             print(ChangedPlainText)
             replaced.append((a,b))
             print(replaced)
     return "YOU DECODED THE WORD"
print("                                   HI..!! WELCOME TO CIPHER SLATE                                  ")
print("START \nYour Cipher Word is:")
print(encrypt(plaintext,shift))
