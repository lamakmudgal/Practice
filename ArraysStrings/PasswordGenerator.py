import random
import string
characters = string.ascii_lowercase+string.ascii_uppercase + "0123456789" +"!@#$%^&*"
specialcharacter = "!@#$%^&*"
#stringsmallcase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#stringlargecase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = "".join(random.choice(characters) for _ in range(8))
print(password)