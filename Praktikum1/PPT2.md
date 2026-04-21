# PPT 2

## A. Kode Penuh 

```python
import math
import numpy as np
import matplotlib.pyplot as plt

def make_function(expr):
    def f(x):
        return eval(expr, {"__builtins__": {}}, {"x": x, "math": math, "np": np})

    return f
def regula_falsi(f, a, b, tol=1e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Interval tidak valid!")
        return None
    print("\nIterasi | a      | b      | c      | f(c)")
    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i:<7} | {a:.4f} | {b:.4f} | {c:.4f} | {f(c):.4f}")
        if abs(f(c)) < tol:
            print(f"\nAkar ditemukan: {c:.4f}")
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("\nMaks iterasi tercapai.")
    return c
expr = input("Masukkan f(x): ")
f = make_function(expr)

a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))

root = regula_falsi(f, a, b)

if root is not None:
    x_vals = np.linspace(a - 2, b + 2, 200)
    y_vals = [f(x) for x in x_vals]

    plt.axhline(0)
    plt.axvline(0)
    plt.plot(x_vals, y_vals, label=f"f(x) = {expr}")
    plt.scatter(root, f(root), color='red', label="Akar")
    plt.legend()
    plt.grid()
    plt.title("Regula Falsi")
    plt.show()
```

## B. Langkah-langkah 

1. Fungsi make_function(expr)
   ```python
   def make_function(expr):
    def f(x):
        return eval(expr, {"__builtins__": {}}, {"x": x, "math": math, "np": np})
    return f
   ```
    User input fungsi dalam bentuk string, contoh:
     ```
     x**3 - 6*x**2 + 11*x - 6
     ```
    eval() mengubah string jadi fungsi nyata

2. Fungsi regula_falsi
   ```python
   def regula_falsi(f, a, b, tol=1e-4, max_iter=100):
   ```
    Parameter:

    ```f``` -> fungsi

    ```a, b``` -> interval awal

    ```tol``` -> toleransi error

    ```max_iter``` -> batas iterasi

3. Validasi Interval
   ```python
   if f(a) * f(b) >= 0:
    print("Interval tidak valid!")
    return None
   ```
    Regula Falsi membutuhkan f(a).f(b) < 0

4. Loop Iterasi
   ```python
    for i in range(1, max_iter + 1):
   ```
    Ulang sampai:

    akar sudah didapatkan atau max iterasi

5. Rumus Regula Falsi
   ```python
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
   ```
    cari titik potong garis antara (a,f(a)) dan (b,f(b)) ke sumbu x

6. Cek Konvergensi
   ```python
   if abs(f(c)) < tol:
    print(f"\nAkar ditemukan: {c:.4f}")
    return c
   ```
    Dianggap Mendekati Akar

7. Update Interval
   ```python
    if f(a) * f(c) < 0:
    b = c
      else:
    a = c
   ```
    - Kalau a < akar < c -> Geser b
    - kalau b < akar < c -> Geser a

8. Input
   ```python
   expr = input("Masukkan f(x): ")
    f = make_function(expr)

    a = float(input("Masukkan a: "))
    b = float(input("Masukkan b: "))
   ```

9. Menjalankan Metode Regula Falsi
   ```python
    root = regula_falsi(f, a, b)
   ```

10. Visualisasi Grafik
    ```python
    x_vals = np.linspace(a - 2, b + 2, 200)
    y_vals = [f(x) for x in x_vals]
    ```
    Membuat 200 titik dari range

    a. Membuat Garis Bantu Sumbu X dan Y
    ```python
    plt.axhline(0)
    plt.axvline(0)
    ```

    b. Plot Fungsi
    ```python
    plt.plot(x_vals, y_vals)
    ```

    c.Menandai Akar
    ```python
    plt.scatter(root, f(root), color='red')
    ```

## C. Screenshot 

<img width="1068" height="831" alt="Screenshot 2026-04-22 at 01 12 42" src="https://github.com/user-attachments/assets/8d5fd54f-22eb-438f-8d3d-a0887f41ba22" />
<img width="1440" height="900" alt="Screenshot 2026-04-22 at 01 13 22" src="https://github.com/user-attachments/assets/974d3a29-3491-4ad8-8572-5a57897e61f7" />

# PPT3

## A. Full Code

## B. Langkah Langkah

## C. Screenshoot



