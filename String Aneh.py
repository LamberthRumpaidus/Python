import random
import string

panjang = 10  # Anda dapat mengubah ini untuk menghasilkan string dengan panjang yang berbeda
string_unik = ''.join(random.choice(string.ascii_letters)
                      for _ in range(panjang))

print(string_unik)
