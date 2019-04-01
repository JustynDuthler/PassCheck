import hashlib
import requests
import sys

# get the user password from the command line
usrInput = input("Please type in Password:")
print(usrInput)

# hash the password with sha1 and print it out
encryptPass = hashlib.sha1()
encryptPass.update(usrInput.encode("utf8"))
encryptPass = encryptPass.hexdigest().upper()
print(encryptPass)

# request the information about all cracked hashes with the first
# five chars of the encoded password
pwndUrl = 'https://api.pwnedpasswords.com/range/'
firstFiveCharEncrypt = encryptPass[:5]
urlWithFiveChars = pwndUrl + firstFiveCharEncrypt
r = requests.get(urlWithFiveChars)
# get the last 10 chars of the hashed password to see if it cracked
lastTenCharEncrypt = encryptPass[-10:]
#print(lastTenCharEncrypt)
# remove all new lines in the text
allLines = r.text.split('\n')
for line in allLines:
    #print(line)
    crackedPass, count = line.split(':', 1) # spilt string into the hashed pass and the count
    #print(crackedPass)
    #print(count)
    # check if any of the returned cracked passwords are the one the usr inputed
    lineLastTen = crackedPass[-10:]
    #print(lineLastTen)
    if(lastTenCharEncrypt == lineLastTen):
        print(crackedPass)
        print(count)
        s = 'Your password has been cracked ' + count + 'times!'
        print(s)
        break
        
    
    



