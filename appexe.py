from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Aplikasi Input Data Digital Forensik')
root.geometry("500x300")

main_frame = Frame(root)
main_frame.pack(fill="both", expand=1)

main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill="both", expand=1)

main_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
main_scrollbar.pack(side=LEFT, fill=Y, expand=1)

main_canvas.configure(yscrollcommand=main_scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))

second_frame = Frame(main_canvas)

main_canvas.create_window((0, 0), window=second_frame, anchor='nw')

kolom1 = LabelFrame(second_frame, text="Drive Model")
kolom2 = LabelFrame(second_frame, text="Drive Serial Number")
kolom3 = LabelFrame(second_frame, text="Source Data Size")
kolom4 = LabelFrame(second_frame, text="Sector Count")
kolom5 = LabelFrame(second_frame, text="MD5 Checksum")
kolom6 = LabelFrame(second_frame, text="SHA5 Checksum")
kolom7 = LabelFrame(second_frame, text="Jumlah Temuan")
kolom8 = LabelFrame(second_frame, text="Jenis Temuan")

kolom1.pack(fill="both", expand='yes', padx=20, pady=20)
kolom2.pack(fill="both", expand='yes', padx=20, pady=20)
kolom3.pack(fill="both", expand='yes', padx=20, pady=20)
kolom4.pack(fill="both", expand='yes', padx=20, pady=20)
kolom5.pack(fill="both", expand='yes', padx=20, pady=20)
kolom6.pack(fill="both", expand='yes', padx=20, pady=20)
kolom7.pack(fill="both", expand='yes', padx=20, pady=20)
kolom8.pack(fill="both", expand='yes', padx=20, pady=20)

v_drive_model = StringVar()
v_drive_serial_number = StringVar()
v_source_data_size = StringVar()
v_sector_count = StringVar()
v_md5_checksum = StringVar()
v_sha5_checksum = StringVar()
v_jumlah_temuan = StringVar()
v_jenis_temuan = StringVar()

drive_model = Entry(kolom1, textvariable=v_drive_model)
drive_model.grid(row=1, column=1, columnspan=2, sticky="w", padx=2, pady=4)

drive_serial_number = Entry(kolom2, textvariable=v_drive_serial_number)
drive_serial_number.grid(row=2, column=1, columnspan=2, sticky="w", padx=2, pady=4)

source_data_size = Entry(kolom3, textvariable=v_source_data_size)
source_data_size.grid(row=3, column=1, columnspan=2, sticky="w", padx=2, pady=4)

sector_count = Entry(kolom4, textvariable=v_sector_count)
sector_count.grid(row=4, column=1, columnspan=2, sticky="w", padx=2, pady=4)

md5_checksum = Entry(kolom5, textvariable=v_md5_checksum)
md5_checksum.grid(row=5, column=1, columnspan=2, sticky="w", padx=2, pady=4)

sha5_checksum = Entry(kolom6, textvariable=v_sha5_checksum)
sha5_checksum.grid(row=6, column=1, columnspan=2, sticky="w", padx=2, pady=4)

jumlah_temuan = Entry(kolom7, textvariable=v_jumlah_temuan)
jumlah_temuan.grid(row=7, column=1, columnspan=2, sticky="w", padx=2, pady=4)

jenis_temuan = Entry(kolom8, textvariable=v_jenis_temuan)
jenis_temuan.grid(row=8, column=1, columnspan=2, sticky="w", padx=2, pady=4)

root.mainloop()

