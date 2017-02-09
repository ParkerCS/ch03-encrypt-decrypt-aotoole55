# MODULES AND LIBRARIES
'''
For this assignment, we will practice the use of imports to encrypt and decrypt messages.
The functions are already contained in the files.  Your job is to use them to encrypt and decrypt strings.  Good luck
'''

import encryption_key

import decode

import encode

#1 Decrypt this message using imports from the decode.py and encryption_key.py.  Make the result print in a friendly format that is easy for the user to understand. (10pt)
print("Problem 1")

encrypted_message = "¿®ªªÈÙ®ÏT¤ÕEÓ¹âeCíÉÁÏº¢¡i¸ºÇ¿"

message1 = decode.decode(encryption_key.key, encrypted_message)

print(message1)

#2 Encrypt your name and print the encrypted result.  Make the result print in a friendly format that is easy for the user to understand. (5pt)
print("\n Problem 2")

encrypted_name = "Austin Phillips O'Toole"


message2 = encode.encode(encryption_key.key, encrypted_name)

print("The encrypted name is \"" + message2 + "\"")

#3 Decrypt the encrypted code from part 2 to ensure that it worked properly and print the result.  Make the result print in a friendly format that is easy for the user to understand. (5pt)

print("\n Problem 3")

message3 = decode.decode(encryption_key.key, message2)

print("The decrypted name is: ", message3)