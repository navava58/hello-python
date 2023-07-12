import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

# Kết nối tới database với username, password và tên database tương ứng
db = mysql.connect(
    host="localhost",
    user="anhnn91",
    password="nhat1998",
    database="anhnn91"
)

window = tk.Tk()
window.title("Insert Data to MySQL")
window.geometry("400x300")

# Lấy tất cả các table trong database
cursor = db.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Tạo Label và Entry để nhập tên table cần insert
table_label = tk.Label(window, text="Tên table:")
table_label.grid(column=0, row=0)

table_entry = tk.Entry(window)
table_entry.grid(column=1, row=0)


# Tạo các Label và Entry để nhập dữ liệu cần insert
data_labels = []
data_entries = []
for i in range(2):
    l = tk.Label(window, text=f"Data {i+1}")
    l.grid(column=0, row=i+1)
    data_labels.append(l)

    e = tk.Entry(window)
    e.grid(column=1, row=i+1)
    data_entries.append(e)


# Tạo hàm insert_data để insert dữ liệu vào database
def insert_data():
    # Lấy tên table từ Entry
    table_name = table_entry.get()

    # Lấy dữ liệu từ các Entry và kiểm tra tính hợp lệ
    data = []
    for e in data_entries:
        if e.get().strip() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return

        try:
            #value = str.strip((e.get()))
            value = str(e.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ")
            return

        data.append(value)

    # Tạo câu lệnh SQL và thực thi truy vấn
    sql = f"INSERT INTO {table_name} VALUES ({','.join(str(d) for d in data)})"
    cursor = db.cursor()
    cursor.execute(sql)

    # Lưu các thay đổi vào database
    db.commit()

    messagebox.showinfo("Thành công", "Insert dữ liệu thành công!")


# Tạo button để insert dữ liệu
insert_button = tk.Button(window, text="Insert", command=insert_data)
insert_button.grid(column=1, row=4)

window.mainloop()
