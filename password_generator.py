import random

# Character shuffle
def shuffle(string):
    charList = list(string)
    random.shuffle(charList)
    return ''.join(charList)

# Main function
# upper case characters
uppercaseChar1=chr(random.randint(65,90))
uppercaseChar2=chr(random.randint(65,90))
# lower case characters
lowercaseChar1=chr(random.randint(97,122))
lowercaseChar2=chr(random.randint(97,122))
lowercaseChar3=chr(random.randint(97,122))
lowercaseChar4=chr(random.randint(97,122))
# numbers
randomNum1=chr(random.randint(48,57))
randomNum2=chr(random.randint(48,57))
# symbols
randomSym1=chr(random.randint(33,47))
randomSym2=chr(random.randint(33,47))

# Generate password randomly
password = uppercaseChar1 + uppercaseChar2 + lowercaseChar1 + lowercaseChar2 + lowercaseChar3 + lowercaseChar4 + randomNum1 + randomNum2 + randomSym1 + randomSym2
password = shuffle(password)
# password output
print(password)