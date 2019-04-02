import hashlib
import requests
import random, string
import sys


print('Type in three uncommon words to use in your password. These words can',
        'include your favorite band, snack, etc! Please enter words with a space inbetween')

# get the user password from the command line
usrInput = input()
print(usrInput)
firstWord, secondWord, thirdWord = usrInput.split()

#place a random character in the middle of the second word
random = random.choice(string.punctuation)
#print(random)
middleOfString = int(len(secondWord) / 2)
#print(middleOfString)
secondWord = secondWord[:middleOfString] + random + secondWord[middleOfString:]
#print(secondWord)

# combine words to create a new password
newPassword = firstWord + secondWord + thirdWord
print('Your new password is: ' + newPassword)

# hash the password with sha1 and print it out
encryptPass = hashlib.sha1()
encryptPass.update(newPassword.encode("utf8"))
encryptPass = encryptPass.hexdigest().upper()
#print(encryptPass)

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
        print('Your password has been cracked!')
        break
    else:
        print('Your password has not been cracked! Good choice!')         
        break
 



