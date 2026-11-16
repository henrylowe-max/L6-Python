message = input("enter message to be encrypted: ")
key = input("enter key: ")
message1 = ""
encryptedMessage = ""
#invMessage = message[::-1]
while len(message1) < len(message):
    message1 = message1 + key


for i in range(len(message)):
    if message[i] == message1[i]:
        encryptedMessage = encryptedMessage + "0"
    else:
        encryptedMessage = encryptedMessage + "1"


print(f"the original message is: {message}")
print(f"the repeated key is {message1}")   
print(f"the encrypted message is: {encryptedMessage}")