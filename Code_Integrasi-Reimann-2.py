import math
import time

def f(x):
    return 4 / (1 + x**2)

def integrasi_reimann(f, a, b, N):
    h = (b - a) / N
    x = [a + i * h for i in range(N+1)]
    y = [f(xi) for xi in x]
    return h * sum(y)

def uji_integrasi_reimann():
    N_variasi = [10, 100, 1000, 10000]
    referensi_pi = 3.14159265358979323846

    for N in N_variasi:
        waktu_mulai = time.time()
        pi_approx = integrasi_reimann(f, 0, 1, N)
        waktu_selesai = time.time()
        error_rms = math.sqrt((referensi_pi - pi_approx) ** 2)
        waktu_eksekusi = waktu_selesai - waktu_mulai
        print(f"N = {N}: Pi Aproksimasi = {pi_approx:.12f}, Error RMS = {error_rms:.12f}, Waktu Eksekusi = {waktu_eksekusi:.6f} seconds")

uji_integrasi_reimann()