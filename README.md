# PassCheck
This is a proof a concept for an app that will generate and check if a password has been cracked before

How it works:
The user inputs three words for their new passowrd, these words should be uncommon words as they are harder to crack with a dictonary. It then adds a random symbol in the middle of a word making it harder to brute force. These words are combined and then checked in the haveibeenpwned api (https://haveibeenpwned.com/API/v2).
