**Description:**
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message [here](https://artifacts.picoctf.net/c/393/message.txt).
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

**Explaination:**
This challenge requires a knowledge of the modulus operator (%) which simply return the remained of one interger divided by another. The message contains a list of numbers, which must be modded by 37 before they correspond to letters in the alphabet.

**Solution:**
Attached is a simple python script to open message.txt, convert all the numbers to integers, mod all the numbers by 37, and map them to an alphabet which includes both decimal digits and an underscore. Remember that the flag has to be wrapped by picoCTF{...}.

