# 3. Implement a random password generator in python.
# Everytime you run this program it should generate 8 character long password.
# The password should be of combination of  alphanumeric character and symbols like @#_- only

import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@','#','_','-']

rand_dig = random.choice(DIGITS)
rand_locase = random.choice(LOCASE_CHARACTERS)
rand_upcase = random.choice(UPCASE_CHARACTERS)
rand_punc = random.choice(SYMBOLS)

pass4_digs = rand_dig + rand_locase + rand_upcase + rand_punc

password_chars = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS
remain_pass = ''.join(random.choice(password_chars) for i in range(4))
password = pass4_digs + remain_pass
print(password)

temp_pass_list = [char for char in password]
random.shuffle(temp_pass_list)
final_password = ''.join(x for x in temp_pass_list)

print(final_password)