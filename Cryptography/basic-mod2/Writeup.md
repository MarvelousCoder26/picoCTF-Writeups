**Description:**
A new modular challenge!
Download the message [here](https://artifacts.picoctf.net/c/499/message.txt).
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

**Explanation:**
Modular inverses are significantly more complicated, but there are many online tools to do all the math. Conveniently though, there is also a simple way to do this in python: pow(x, -1, p) where p is the number you are modding by. Let's rewrite our code from basic-mod1 to preform modular inverses instead of just mods. Also, the alphabet mapping is shifted by one for this challenge, but that's no big problem

**Solution**
Attached is a simple python script to open message.txt, convert all the numbers to integers, compute the modular inverses of all the numbers modded by 41, and map them to an alphabet which includes both decimal digits and an underscore. Remember that the flag has to be wrapped by picoCTF{...}.