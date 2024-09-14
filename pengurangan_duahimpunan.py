def kurang_himpunan(himpunan1, himpunan2):
    hasil = himpunan1 - himpunan2
    return hasil
    
himpunan_a = {10, 20, 30}
himpunan_b = {2, 5}

hasil_bagian = kurang_himpunan(himpunan_a, himpunan_b)
print(hasil_bagian)
