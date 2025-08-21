import string
import random

chars = string.ascii_letters + string.digits
length = 12  # or whatever length you want
long = 100
for _ in range(long):
    random_password = ''.join(random.choices(chars, k=length))
    file = f"{random_password}.txt"
    with open(file, 'w') as f:
        f.write(random_password)
    print('Simulated virus has been created as', file)
