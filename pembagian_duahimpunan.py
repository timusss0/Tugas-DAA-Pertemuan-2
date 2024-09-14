def bagi_himpunan(himpunan1, himpunan2):
    hasil = set()
    for a in himpunan1:
        for b in himpunan2:
            if b != 0: 
                hasil.add(a / b)
    return hasil


himpunan_a = {10, 20, 30}
himpunan_b = {2, 5}

hasil_bagian = bagi_himpunan(himpunan_a, himpunan_b)
print(hasil_bagian)
