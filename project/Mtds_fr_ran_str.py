# Methods for find random and strings of alphabet and digit and punctuation

import random   # this is for find random value from any thing i.e range , choice , etc
import string   # this is use for play with letters , digit, and punctuation


ran = random.randint(1,5)   # radnom form 1 to 5 , start and end both included
ran1 = random.randrange(1,5) # random from 1 to 5, start is include but end is exclude
ran2 = random.choice("abcde")  # random from this word 




str1 = string.ascii_letters  # this is for all alphabets form a to z and A to Z
str2 = string.ascii_lowercase  # this is for all alphabets form a to z
str3 = string.ascii_uppercase # this is for all  alphabets form A to Z
str4 = string.punctuation  # this is for all special character
str5 = string.digits  # this is for all 0 to 9 digits but not in a int form it is in a string form


print(ran1)
