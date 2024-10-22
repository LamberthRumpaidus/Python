import tkinter as tk


class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")

        # Entry untuk menampilkan input
        self.entry = tk.Entry(root, font=("Arial", 16), justify='right')
        self.entry.pack(fill=tk.BOTH, ipadx=8)

        # Frame untuk tombol
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Tombol angka dan operasi
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '%', 'AC', 'Del'
        ]

        row_val = 0
        col_val = 0

        # Membuat tombol dan menambahkan ke grid
        for button in buttons:
            b = tk.Button(self.button_frame, text=button, command=lambda value=button: self.on_button_click(
                value), font=("Arial", 16), width=5)
            b.grid(row=row_val, column=col_val, padx=5, pady=5)

            col_val += 1
            if col_val > 3:  # Ubah baris setiap 4 kolom
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        if value == "=":
            try:
                expression = self.entry.get()
                # Menangani persentase
                if "%" in expression:
                    parts = expression.split("%")
                    base = float(parts[0]) if parts[0] else 1
                    if len(parts) > 1:
                        percent_value = float(parts[1]) / 100
                        expression = f"{base} * {percent_value}"
                    else:
                        expression = str(base / 100)

                # Hitung ekspresi
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error: Div/0")
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                print(e)  # Tampilkan kesalahan di konsol untuk debugging
        elif value == "AC":
            self.reset()
        elif value == "Del":
            self.delete()
        else:
            self.entry.insert(tk.END, value)

    def reset(self):
        self.entry.delete(0, tk.END)

    def delete(self):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text[:-1])


if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = Kalkulator(root)
    root.mainloop()
