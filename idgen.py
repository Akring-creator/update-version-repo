import random
import string
import time

def generate_id():
# Hari / waktu
    waktu = [
        "senin","selasa","rabu","kamis","jumat","sabtu","minggu",
        "pagi","siang","sore","malam","subuh"
    ]

    # Kota / tempat
    tempat = [
        "jakarta","bandung","surabaya","medan","bali","bogor","depok",
        "bekasi","semarang","makassar","palembang","padang","yogyakarta",
        "malang","solo","aceh","papua","lombok","kupang","manado"
    ]

    # Hewan
    hewan = [
        "kucing","anjing","domba","singa","gajah","harimau","elang",
        "ular","kuda","ayam","bebek","kambing","ikan","hiu","paus",
        "burung","merpati","cicak","katak","kelinci"
    ]

    # Teknologi / benda
    benda = [
        "laptop","komputer","server","router","switch","tablet","printer",
        "monitor","keyboard","mouse","scanner","kamera","drone","sensor",
        "modem","flashdisk","harddisk","chip","prosesor","database"
    ]

    # Sifat / kata unik
    sifat = [
        "cepat","lambat","cerdas","kuat","ringan","gelap","terang",
        "dingin","panas","tajam","halus","kasar","tinggi","rendah",
        "liar","tenang","aktif","pasif","unik","acak"
    ]

    # Gabungkan semua kata
    words = waktu + tempat + hewan + benda + sifat
    words_part = "-".join(random.sample(words, 3))
    time_part = format(int(time.time()), 'x')  # hex timestamp biar pendek
    rand_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    
    return f"{words_part}-{time_part}-{rand_part}"

print(generate_id())