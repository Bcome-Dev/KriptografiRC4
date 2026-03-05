def siapkan_array_kunci(password):
    array_kunci = []
    for i in range(256):
        array_kunci.append(i)
        
    j = 0
    panjang_pass = len(password)
    
    for i in range(256):
        angka_password = ord(password[i % panjang_pass])
        j = (j + array_kunci[i] + angka_password) % 256
        array_kunci[i], array_kunci[j] = array_kunci[j], array_kunci[i]
        
    return array_kunci

def proses_rc4(password, data_angka):
    array_kunci = siapkan_array_kunci(password)
    
    i = 0
    j = 0
    hasil_akhir = []
    
    for angka in data_angka:
        i = (i + 1) % 256
        j = (j + array_kunci[i]) % 256
        
        array_kunci[i], array_kunci[j] = array_kunci[j], array_kunci[i]
        kunci_xor = array_kunci[(array_kunci[i] + array_kunci[j]) % 256]
        
        angka_acak = angka ^ kunci_xor
        hasil_akhir.append(angka_acak)
        
    return hasil_akhir

if __name__ == '__main__':
    print("=== DEMO RC4 ===")
    
    pesan_asli = input("Masukkan pesan rahasia: ")
    password = input("Masukkan password: ")
    
    print("\n[1] Mengubah teks asli jadi daftar angka...")
    pesan_angka = []
    for huruf in pesan_asli:
        pesan_angka.append(ord(huruf))
        
    print(f"Pesan menjadi: {pesan_angka}")
    
    input("\n[Tekan Enter untuk mulai ENKRIPSI...]")
    hasil_enkripsi = proses_rc4(password, pesan_angka)
    print(f"Hasil Ciphertext (Angka Acak) : {hasil_enkripsi}")
    
    input("\n[Tekan Enter untuk mulai DEKRIPSI...]")
    print("Membuka pesan menggunakan kunci yang sama...")
    hasil_dekripsi = proses_rc4(password, hasil_enkripsi)
    
    print("\n[3] Mengubah kembali angka jadi teks...")
    pesan_kembali = ""
    for angka in hasil_dekripsi:
        pesan_kembali += chr(angka)
        
    print(f"Hasil Akhir: '{pesan_kembali}'")
