import time

def catalan_recursive(n):
    result = 0
    if n <= 1:
        return 1
    else:
        for i in range(n):
            result += catalan_recursive(i) * catalan_recursive(n - i - 1)
        return result

# Mengukur waktu eksekusi
start_time = time.time()
result = catalan_recursive(0)
end_time = time.time()

# Menampilkan hasil dan waktu eksekusi
print(f'Output: {result}')  # Output: 42
print(f'Waktu eksekusi: {end_time - start_time} detik')
