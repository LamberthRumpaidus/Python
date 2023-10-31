import random

karakter = ["seorang penyihir", "seorang ksatria",
            "sebuah naga", "seorang pria", "seorang kurcaci"]
tempat = ["hutan gelap", "kastil berhantu",
          "pantai yang cerah", "gua yang dalam", "gunung mistis"]
aksi = ["menemukan harta karun", "bertarung dengan monster",
        "menemukan rahasia", "menyelamatkan putri", "memecahkan teka-teki"]

karakter = random.choice(karakter)
tempat = random.choice(tempat)
aksi = random.choice(aksi)

cerita = f"Suatu hari, {karakter} sedang berjalan di {tempat}. Tiba-tiba, {karakter} {aksi}. Dan begitulah, petualangan terus berlanjut..."

print(cerita)
