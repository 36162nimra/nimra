import tkinter as tk
from tkinter import messagebox   # to show pop-up messages

# Function that runs when we click "submit"
def submit_form():
    # Get data from all fields
    fname = entry_fname.get()
    lname = entry_lname.get()
    addr_state = address_state.get()  # will be "Temporary" or "Permanent"
    address = text_address.get("1.0", tk.END).strip()  # get text from line 1, char 0 till END
    hobbies = []
    if hobby_cricket.get():
        hobbies.append("Cricket")
    if hobby_football.get():
        hobbies.append("Football")

    # Prepare a summary of the form
    summary = f"""
    First Name: {fname}
    Last Name: {lname}
    Address State: {addr_state}
    Address: {address}
    Hobbies: {", ".join(hobbies) if hobbies else "None"}
    """

    messagebox.showinfo("Form Submitted", summary)

# Create the main window
root = tk.Tk()
root.title("Personal Details")
root.geometry("500x400")
root.configure(bg="white")

# ---------- First Name ----------
lbl_fname = tk.Label(root, text="First Name", bg="#eaffea")
lbl_fname.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_fname = tk.Entry(root, width=40)
entry_fname.grid(row=0, column=1, padx=10, pady=5)

# ---------- Last Name ----------
lbl_lname = tk.Label(root, text="Last Name", bg="#eaffea")
lbl_lname.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_lname = tk.Entry(root, width=40)
entry_lname.grid(row=1, column=1, padx=10, pady=5)

# ---------- Address State (Radio Buttons) ----------
lbl_addr_state = tk.Label(root, text="Address State", bg="#eaffea")
lbl_addr_state.grid(row=2, column=0, sticky="w", padx=10, pady=5)

address_state = tk.StringVar(value="Temporary")  # default is Temporary
radio_temp = tk.Radiobutton(root, text="Temporary", variable=address_state, value="Temporary")
radio_perm = tk.Radiobutton(root, text="Permanent", variable=address_state, value="Permanent")
radio_temp.grid(row=2, column=1, sticky="w", padx=10)
radio_perm.grid(row=2, column=1, sticky="e", padx=10)

# ---------- Address (Text box) ----------
lbl_address = tk.Label(root, text="Address", bg="#eaffea")
lbl_address.grid(row=3, column=0, sticky="nw", padx=10, pady=5)
text_address = tk.Text(root, width=30, height=4)
text_address.grid(row=3, column=1, padx=10, pady=5)

# ---------- Hobbies (Checkboxes) ----------
lbl_hobbies = tk.Label(root, text="Hobbies", bg="#eaffea")
lbl_hobbies.grid(row=4, column=0, sticky="w", padx=10, pady=5)

hobby_cricket = tk.BooleanVar()
hobby_football = tk.BooleanVar()
chk_cricket = tk.Checkbutton(root, text="Cricket", variable=hobby_cricket)
chk_football = tk.Checkbutton(root, text="Football", variable=hobby_football)
chk_cricket.grid(row=4, column=1, sticky="w", padx=10)
chk_football.grid(row=4, column=1, sticky="e", padx=10)

# ---------- Submit Button ----------
btn_submit = tk.Button(root, text="submit", command=submit_form, bg="#eaffea")
btn_submit.grid(row=5, column=1, pady=20)

# Start the window
root.mainloop()

