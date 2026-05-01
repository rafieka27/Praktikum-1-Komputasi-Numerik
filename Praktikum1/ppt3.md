# PPT 3

## A. Kode Penuh 
```python
import tkinter as tk
from tkinter import messagebox
import sympy as sp

def hitung_secant():
    text_output.delete(1.0, tk.END)
    
    try:
        func_str = entry_func.get()
        x0 = float(entry_x0.get())
        x1 = float(entry_x1.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
        
        x = sp.symbols('x')
        expr = sp.sympify(func_str)
        f = sp.lambdify(x, expr, 'math')
        
        text_output.insert(tk.END, "Iter |    x0    |    x1    |    x2    |   f(x2)  |   Error  \n")
        text_output.insert(tk.END, "-"*65 + "\n")
        
        x2 = x1
        
        for i in range(max_iter):
            f_x0 = f(x0)
            f_x1 = f(x1)
            
            if f_x1 - f_x0 == 0:
                text_output.insert(tk.END, f"\n[PERINGATAN] Dihentikan: Pembagian dengan nol terdeteksi.")
                break
                
            x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
            error = abs(x2 - x1)
            f_x2 = f(x2)
            
            text_output.insert(tk.END, f"{i+1:^4} | {x0:8.4f} | {x1:8.4f} | {x2:8.4f} | {f_x2:8.4f} | {error:8.6f}\n")
            
            if error < tol:
                text_output.insert(tk.END, "-"*65 + "\n")
                text_output.insert(tk.END, f"HASIL: Akar ditemukan pada x = {x2:.6f}\n")
                return
                
            x0 = x1
            x1 = x2
            
        text_output.insert(tk.END, "-"*65 + "\n")
        text_output.insert(tk.END, f"HASIL: Iterasi maksimum tercapai. Akar hampiran: {x2:.6f}\n")
        
    except Exception as e:
        messagebox.showerror("Error Input", f"Cek kembali input Anda!\nPastikan format fungsi benar (Contoh: x**2 - 4).\nDetail Error: {e}")

root = tk.Tk()
root.title("Kalkulator Akar - Metode Secant")
root.geometry("550x450")
root.configure(padx=20, pady=20)

tk.Label(root, text="Pencarian Akar Persamaan (Metode Secant)", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

tk.Label(root, text="Fungsi f(x) :").grid(row=1, column=0, sticky="w")
entry_func = tk.Entry(root, width=30)
entry_func.grid(row=1, column=1, pady=5, sticky="w")
entry_func.insert(0, "x**3 - 5*x + 1")

tk.Label(root, text="Tebakan Awal (x0) :").grid(row=2, column=0, sticky="w")
entry_x0 = tk.Entry(root, width=15)
entry_x0.grid(row=2, column=1, pady=5, sticky="w")
entry_x0.insert(0, "0")

tk.Label(root, text="Tebakan Awal (x1) :").grid(row=3, column=0, sticky="w")
entry_x1 = tk.Entry(root, width=15)
entry_x1.grid(row=3, column=1, pady=5, sticky="w")
entry_x1.insert(0, "1")

tk.Label(root, text="Toleransi Error :").grid(row=4, column=0, sticky="w")
entry_tol = tk.Entry(root, width=15)
entry_tol.grid(row=4, column=1, pady=5, sticky="w")
entry_tol.insert(0, "0.0001")

tk.Label(root, text="Maksimal Iterasi :").grid(row=5, column=0, sticky="w")
entry_iter = tk.Entry(root, width=15)
entry_iter.grid(row=5, column=1, pady=5, sticky="w")
entry_iter.insert(0, "50")

btn_hitung = tk.Button(root, text="Hitung Akar", command=hitung_secant, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_hitung.grid(row=6, column=0, columnspan=2, pady=15)

text_output = tk.Text(root, height=12, width=65, font=("Courier", 9))
text_output.grid(row=7, column=0, columnspan=2)

root.mainloop()
```

## B. Langkah langkah kode

1. Deklarasi dan Import Library
   ```python
    import tkinter as tk
    from tkinter import messagebox
    import sympy as sp
   ```
-tkinter: Library standar Python untuk membuat antarmuka pengguna grafis (GUI) seperti jendela, tombol, dan kotak teks.
-messagebox: Modul dari tkinter untuk menampilkan jendela pop-up (seperti peringatan error).
-sympy: Library Python untuk komputasi matematika simbolik. Di sini digunakan untuk membaca input fungsi matematika berbentuk teks (string) dan mengubahnya  menjadi fungsi Python yang bisa dihitung.

2. Fungsi Inti: hitung_secant()
Fungsi ini adalah otak dari program, dieksekusi saat tombol "Hitung Akar" ditekan.

A. Persiapan dan Pengambilan Input
```python
    text_output.delete(1.0, tk.END)
    try:
    func_str = entry_func.get()
    x0 = float(entry_x0.get())
    x1 = float(entry_x1.get())
    tol = float(entry_tol.get())
    max_iter = int(entry_iter.get())
```
-Pertama, area teks output dibersihkan dari hasil sebelumnya.
-Blok try dimulai untuk menangani potensi error jika user memasukkan data yang tidak valid (misal: memasukkan huruf di kolom angka).
-Program mengambil nilai dari kolom-kolom input (fungsi, tebakan awal x0 dan x1, toleransi error, dan batas iterasi) dan mengubahnya ke tipe data yang        sesuai (float untuk desimal, int untuk bilangan bulat).

B. Parsing Fungsi Matematika
```python
    x = sp.symbols('x')
    expr = sp.sympify(func_str)
    f = sp.lambdify(x, expr, 'math')
```
-Mendefinisikan x sebagai simbol matematika.
-sp.sympify: Mengubah teks input (misal "x3 - 5*x + 1") menjadi ekspresi matematika yang dipahami SymPy.
-sp.lambdify: Mengubah ekspresi SymPy tersebut menjadi fungsi Python biasa (f) yang sangat cepat dihitung saat kita memasukkan nilai x.

C. Iterasi Metode Secant
```python
for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            text_output.insert(tk.END, f"\n[PERINGATAN] Dihentikan: Pembagian dengan nol terdeteksi.")
            break
```

-Program melakukan perulangan maksimal sebanyak max_iter.
-Menghitung nilai fungsi pada titik x0 dan x1.
-Validasi: Jika $f(x_1) - f(x_0) = 0$, program akan berhenti (break). Ini penting untuk mencegah error Division by Zero (pembagian dengan nol) pada rumus     Secant di langkah berikutnya.

D. Rumus Secant dan Evaluasi
```python
x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        error = abs(x2 - x1)
        f_x2 = f(x2)
```

Ini adalah penerapan langsung dari rumus Metode Secant untuk mencari titik baru (x2):


- <img width="400" height="100" alt="image" src="https://github.com/user-attachments/assets/ba684777-2475-410f-b30c-d3d10fdd5cf4" />

-error dihitung dari selisih absolut antara nilai x baru (x2) dan x sebelumnya (x1).
-Tabel hasil kemudian dicetak ke layar untuk setiap iterasi.

E. Kondisi Berhenti (Stop Criteria)
```python
if error < tol:
            text_output.insert(tk.END, f"HASIL: Akar ditemukan pada x = {x2:.6f}\n")
            return
            
        x0 = x1
        x1 = x2
```

-Jika nilai error sudah lebih kecil dari toleransi (tol), berarti nilai x2 sudah cukup akurat. Program mencetak hasil akhir dan keluar dari fungsi (return).
-jika belum akurat, nilai digeser: x0 menjadi x1, dan x1 menjadi x2 untuk iterasi selanjutnya

F. Penanganan Error
```python
except Exception as e:
    messagebox.showerror("Error Input", f"Cek kembali input Anda!\n...")
```
Jika di bagian mana pun dalam blok try terjadi kesalahan (misalnya typo penulisan rumus), program tidak akan crash, melainkan memunculkan pop-up peringatan dari messagebox.

3. Pembuatan Antarmuka (GUI)
```python
root = tk.Tk()
root.title("Kalkulator Akar - Metode Secant")
root.geometry("550x450")
```
Bagian ini menginisialisasi jendela utama aplikasi, mengatur judul, dan ukuran jendelanya (550x450 piksel).

4.Pembuatan Komponen GUI (Label, Entry, Button)
```python
tk.Label(root, text="Fungsi f(x) :").grid(row=1, column=0, sticky="w")
entry_func = tk.Entry(root, width=30)
entry_func.grid(row=1, column=1, pady=5, sticky="w")
entry_func.insert(0, "x**3 - 5*x + 1")
# ... (kode label dan entry lainnya untuk x0, x1, tol, max_iter)
```
-tk.Label: Membuat teks statis (seperti judul atau nama kolom).
-tk.Entry: Membuat kolom input teks satu baris.
-grid(): Adalah metode penataan letak (layout). Bayangkan jendela sebagai tabel Excel; kita menempatkan komponen di baris (row) dan kolom (column) -         tertentu. sticky="w" berarti komponen menempel di sisi kiri (West).
-insert(0, "..."): Memberikan nilai default pada kolom input agar pengguna tidak perlu mengetik dari awal saat mencoba.

5.Tombol dan Teks Output
```python
btn_hitung = tk.Button(root, text="Hitung Akar", command=hitung_secant, ...)
text_output = tk.Text(root, height=12, width=65, font=("Courier", 9))
```
-Tombol dikaitkan dengan parameter command=hitung_secant. Artinya, saat diklik, fungsi yang kita bahas di bagian 2 akan berjalan.
-tk.Text adalah area teks multi-baris tempat tabel iterasi dan hasil akhir akan ditampilkan. Menggunakan font Courier (monospace) agar tabel bisa rata dan rapi.
```python
root.mainloop()
```
Baris terakhir ini sangat penting. Ini memberitahu Python untuk menjalankan aplikasi dan terus mendengarkan interaksi pengguna (seperti klik tombol) sampai jendela ditutup.


## Screenshoot
-<img width="659" height="637" alt="image" src="https://github.com/user-attachments/assets/5a240fe9-5323-4f78-9717-e81a85786ef0" />
