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
        
        for i in range(max_iter):
            f_x0 = f(x0)
            f_x1 = f(x1)
            
            if f_x1 - f_x0 == 0:
                text_output.insert(tk.END, f"\n[!] Dihentikan: Pembagian dengan nol terdeteksi.")
                break
                
            x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
            error = abs(x2 - x1)
            f_x2 = f(x2)
            
            text_output.insert(tk.END, f"{i+1:^4} | {x0:8.4f} | {x1:8.4f} | {x2:8.4f} | {f_x2:8.4f} | {error:8.6f}\n")
            
            if error < tol:
                text_output.insert(tk.END, "-"*65 + "\n")
                text_output.insert(tk.END, f"✅ AKAR DITEMUKAN: {x2:.6f}\n")
                return
                
            x0 = x1
            x1 = x2
            
        text_output.insert(tk.END, "-"*65 + "\n")
        text_output.insert(tk.END, f"❌ Iterasi maksimum tercapai. Akar hampiran: {x2:.6f}\n")
        
    except Exception as e:
        messagebox.showerror("Error Input", f"Cek kembali input Anda!\nPastikan format fungsi benar (Contoh: x**2 - 4 bukan x^2 - 4).\nDetail Error: {e}")

root = tk.Tk()
root.title("Kalkulator Akar - Metode Secant")
root.geometry("550x450")
root.configure(padx=20, pady=20)

tk.Label(root, text="Pencarian Akar Persamaan (Metode Secant)", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

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