import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

class DailyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Catatan Harian")
        self.root.geometry("700x600")  # Ukuran jendela lebih besar untuk ruang yang lebih lega
        self.root.minsize(600, 400)    # Minimum ukuran jendela

        # Struktur data untuk menyimpan catatan
        self.notes = {}

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Gunakan tema untuk tampilan lebih modern
        style = ttk.Style()
        style.theme_use('clam')  # Tema yang lebih bersih

        # Menu Bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Keluar", command=self.exit_app)

        # Menu Bantuan
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bantuan", menu=help_menu)
        help_menu.add_command(label="Tentang", command=self.show_about)

        # Frame utama dengan padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        # Bagian Input Catatan
        input_frame = ttk.LabelFrame(main_frame, text="Buat Catatan Baru", padding="5")
        input_frame.pack(fill="x", pady=5)

        # Label dan Entry untuk Judul
        ttk.Label(input_frame, text="Judul Catatan:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.title_entry = ttk.Entry(input_frame, width=60)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        # Label dan Text untuk Isi Catatan
        ttk.Label(input_frame, text="Isi Catatan:").grid(row=1, column=0, sticky="nw", padx=5, pady=2)
        self.content_text = scrolledtext.ScrolledText(input_frame, height=6, width=60, wrap=tk.WORD)
        self.content_text.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        # Tombol Tambah Catatan
        ttk.Button(input_frame, text="Tambah Catatan", command=self.add_note).grid(row=2, column=1, pady=5, sticky="e")

        # Bagian Daftar Catatan
        listbox_frame = ttk.LabelFrame(main_frame, text="Daftar Catatan", padding="5")
        listbox_frame.pack(fill="both", expand=True, pady=5)

        # Listbox untuk Daftar Catatan dengan Scrollbar
        self.notes_listbox = tk.Listbox(listbox_frame, height=8, selectmode=tk.SINGLE)
        self.notes_listbox.pack(side="left", fill="both", expand=True, padx=5)
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=self.notes_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.notes_listbox.config(yscrollcommand=scrollbar.set)

        # Bind Listbox untuk menampilkan isi catatan
        self.notes_listbox.bind("<<ListboxSelect>>", self.show_note_content)

        # Bagian Detail Catatan
        detail_frame = ttk.LabelFrame(main_frame, text="Detail Catatan", padding="5")
        detail_frame.pack(fill="both", expand=True, pady=5)

        # Text area untuk menampilkan isi catatan (read-only)
        self.detail_text = scrolledtext.ScrolledText(detail_frame, height=6, width=60, wrap=tk.WORD, state="disabled")
        self.detail_text.pack(fill="both", padx=5, pady=5)

        # Tombol Hapus Catatan
        ttk.Button(main_frame, text="Hapus Catatan", command=self.delete_note).pack(pady=5, anchor="e")

        # Konfigurasi grid untuk responsivitas
        input_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)

    def add_note(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not title or not content:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
            return

        if title in self.notes:
            messagebox.showerror("Error", "Judul catatan sudah ada, gunakan judul lain!")
            return

        self.notes[title] = content
        self.notes_listbox.insert(tk.END, title)

        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")

    def show_note_content(self, event):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            selected_title = self.notes_listbox.get(selected_index)

            self.detail_text.config(state="normal")
            self.detail_text.delete("1.0", tk.END)
            self.detail_text.insert("1.0", self.notes[selected_title])
            self.detail_text.config(state="disabled")
        except IndexError:
            pass

    def delete_note(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            selected_title = self.notes_listbox.get(selected_index)

            if not messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus catatan '{selected_title}'?"):
                return

            del self.notes[selected_title]
            self.notes_listbox.delete(selected_index)

            self.detail_text.config(state="normal")
            self.detail_text.delete("1.0", tk.END)
            self.detail_text.config(state="disabled")

            messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
        except IndexError:
            messagebox.showerror("Error", "Pilih catatan yang ingin dihapus!")

    def exit_app(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.quit()

    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Catatan Harian\nVersi: 1.0\nDibuat oleh: [Nama Anda]")

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyNotesApp(root)
    root.mainloop()