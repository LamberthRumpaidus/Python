import random

kata_benda = ["kucing", "anjing", "rumah", "keju", "mobil"]
kata_kerja = ["melompat", "berlari", "terbang", "makan", "berputar"]
kata_sifat = ["merah", "keras", "dingin", "bahagia", "gelap"]

kata_benda = random.choice(kata_benda)
kata_kerja = random.choice(kata_kerja)
kata_sifat = random.choice(kata_sifat)

kalimat = f"{kata_benda} {kata_sifat} {kata_kerja}."

print(kalimat)
