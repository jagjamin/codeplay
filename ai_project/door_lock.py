import tkinter as tk
from tkinter import messagebox

# 초기 비밀번호 설정
password = "1234"
entered_password = ""
new_password = ""
confirm_password = ""
reset_mode = False
verify_mode = False
timeout = 10000  # 10초 (10000 밀리초)

def update_display():
    display_var.set("*" * len(entered_password))

def button_click(number):
    global entered_password, new_password, confirm_password, reset_mode, verify_mode, password
    entered_password += str(number)
    update_display()
    reset_timer()
    if verify_mode:
        if entered_password == password:
            verify_mode = False
            reset_mode = True
            entered_password = ""
            update_display()
            messagebox.showinfo("도어락", "새 비밀번호를 입력하세요.")
        elif len(entered_password) >= len(password):
            messagebox.showerror("도어락", "현재 비밀번호가 틀렸습니다!")
            verify_mode = False
            entered_password = ""
            update_display()
    elif reset_mode:
        if len(new_password) < 4:
            new_password += str(number)
        elif len(confirm_password) < 4:
            confirm_password += str(number)

def clear_display():
    global entered_password
    entered_password = ""
    update_display()
    reset_timer()

def unlock_door():
    global entered_password, password
    if password in entered_password[-len(password):]:
        messagebox.showinfo("도어락", "문이 열렸습니다!")
    else:
        messagebox.showerror("도어락", "비밀번호가 틀렸습니다!")
    clear_display()

def lock_door():
    messagebox.showinfo("도어락", "문이 잠겼습니다!")

def check_status():
    messagebox.showinfo("도어락", "문 상태를 확인하세요.")

def reset_password():
    global verify_mode
    verify_mode = True
    clear_display()
    messagebox.showinfo("도어락", "현재 비밀번호를 입력하세요.")

def confirm_reset_password():
    global new_password, confirm_password, reset_mode, password
    if reset_mode:
        password = new_password
        messagebox.showinfo("도어락", "비밀번호가 변경되었습니다!")
        reset_mode = False
        new_password = ""
        confirm_password = ""
    clear_display()

def reset_timer():
    root.after_cancel(timer)
    start_timer()

def start_timer():
    global timer
    timer = root.after(timeout, root.quit)

# GUI 설정
root = tk.Tk()
root.title("도어락 앱")

display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=("Helvetica", 24), bg="white", width=12, height=2)
display_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, command=lambda t=text: button_click(t), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_display, width=5, height=2)
clear_button.grid(row=4, column=0, padx=5, pady=5)

unlock_button = tk.Button(button_frame, text="Unlock", command=unlock_door, width=5, height=2)
unlock_button.grid(row=4, column=2, padx=5, pady=5)

lock_button = tk.Button(root, text="문 잠그기", command=lock_door)
lock_button.pack(pady=10)

status_button = tk.Button(root, text="상태 확인", command=check_status)
status_button.pack(pady=10)

reset_button = tk.Button(root, text="비밀번호 재설정", command=reset_password)
reset_button.pack(pady=10)

confirm_reset_button = tk.Button(root, text="비밀번호 재설정 확정", command=confirm_reset_password)
confirm_reset_button.pack(pady=10)

start_timer()
root.mainloop()