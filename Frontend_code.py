import tkinter as tk
from tkinter import messagebox
import mysql.connector

profession_var = None

def login():
    global profession_var  
    try:
        # Establish connection to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sid123",
            database="pharma"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Could not connect to MySQL: {err}")
        return
    
    cursor = conn.cursor()

    username = username_entry.get().strip()  # Strip spaces
    password = password_entry.get().strip()  # Strip spaces
    profession = profession_var.get()

    # Ensure all fields are filled in
    if not username or not password or not profession:
        messagebox.showerror("Login Failed", "All fields are required.")
        return
    
    cursor.execute("SELECT * FROM User WHERE Username=%s AND Password=%s AND UserType=%s", (username, password, profession))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login", f"Login successful as {profession}")
        # Redirect to the appropriate dashboard
        if profession == "Doctor":
            doctor_dashboard()
        elif profession == "Pharmacist":
            pharmacist_dashboard()
        elif profession == "Nurse":
            nurse_dashboard()
        else:
            other_profession_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username, password, or profession.")

    cursor.close()
    conn.close()


def signup():
    global profession_var  
    signup_window = tk.Tk()
    signup_window.title("Signup")
    signup_window.geometry("400x250")
    signup_window.configure(bg="#f0f0f0")

    tk.Label(signup_window, text="Username:", bg="#f0f0f0", fg="#333").pack(pady=5)
    username_entry = tk.Entry(signup_window, bg="#fff", fg="#333", relief=tk.FLAT)
    username_entry.pack(pady=5)

    tk.Label(signup_window, text="Password:", bg="#f0f0f0", fg="#333").pack(pady=5)
    password_entry = tk.Entry(signup_window, show="*", bg="#fff", fg="#333", relief=tk.FLAT)
    password_entry.pack(pady=5)

    tk.Label(signup_window, text="Profession:", bg="#f0f0f0", fg="#333").pack(pady=5)
    profession_var = tk.StringVar()
    profession_var.set("Doctor")  # Default value
    profession_option = tk.OptionMenu(signup_window, profession_var, "Doctor", "Pharmacist", "Nurse", "Other")
    profession_option.configure(bg="#fff", fg="#333", relief=tk.FLAT, width=20)  # Increased width
    profession_option.pack(pady=5)

    def signup_attempt():
        new_username = username_entry.get().strip()
        new_password = password_entry.get().strip()
        profession = profession_var.get()

        if not new_username or not new_password or not profession:
            messagebox.showerror("Signup Failed", "All fields are required.")
            return

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sid123",
            database="pharma"
        )
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM User WHERE Username=%s", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Signup Failed", "Username already exists.")
            cursor.close()
            conn.close()
            return
        
        # Insert the new user
        cursor.execute("INSERT INTO User (Username, Password, UserType) VALUES (%s, %s, %s)", (new_username, new_password, profession))
        conn.commit()

        messagebox.showinfo("Success", f"Signup Successful! Profession: {profession}")

        cursor.close()
        conn.close()
        signup_window.destroy()  

    signup_button = tk.Button(signup_window, text="Signup", command=signup_attempt, bg="#007bff", fg="#fff", relief=tk.FLAT)
    signup_button.pack(pady=10)

    signup_window.mainloop()


def doctor_dashboard():
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Doctor Dashboard")
    doctor_window.geometry("600x400")
    doctor_window.configure(bg="#f0f0f0")

    tk.Label(doctor_window, text="Doctor Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(doctor_window, text="Patient Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(doctor_window, text="Patient Name:", bg="#f0f0f0").pack(pady=2)
    patient_name_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    patient_name_entry.pack(pady=2)

    tk.Label(doctor_window, text="Date of Birth:", bg="#f0f0f0").pack(pady=2)
    dob_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    dob_entry.pack(pady=2)

    tk.Label(doctor_window, text="Gender:", bg="#f0f0f0").pack(pady=2)
    gender_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    gender_entry.pack(pady=2)

    tk.Label(doctor_window, text="Address:", bg="#f0f0f0").pack(pady=2)
    address_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    address_entry.pack(pady=2)

    tk.Label(doctor_window, text="Contact Number:", bg="#f0f0f0").pack(pady=2)
    contact_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    contact_entry.pack(pady=2)

    tk.Label(doctor_window, text="Prescription ID:", bg="#f0f0f0").pack(pady=2)
    prescription_id_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    prescription_id_entry.pack(pady=2)

    view_prescription_button = tk.Button(doctor_window, text="View Prescription", bg="#007bff", fg="#fff", relief=tk.FLAT)
    view_prescription_button.pack(pady=10)

    tk.Label(doctor_window, text="Prescription Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(doctor_window, text="Prescription ID:", bg="#f0f0f0").pack(pady=2)
    prescription_id_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    prescription_id_entry.pack(pady=2)

    tk.Label(doctor_window, text="Date Prescribed:", bg="#f0f0f0").pack(pady=2)
    date_prescribed_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    date_prescribed_entry.pack(pady=2)

    tk.Label(doctor_window, text="Medicine:", bg="#f0f0f0").pack(pady=2)
    medicine_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    medicine_entry.pack(pady=2)

    tk.Label(doctor_window, text="Dosage:", bg="#f0f0f0").pack(pady=2)
    dosage_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    dosage_entry.pack(pady=2)

    tk.Label(doctor_window, text="Duration:", bg="#f0f0f0").pack(pady=2)
    duration_entry = tk.Entry(doctor_window, bg="#fff", relief=tk.FLAT)
    duration_entry.pack(pady=2)

    prescribe_button = tk.Button(doctor_window, text="Prescribe Medicine", bg="#007bff", fg="#fff", relief=tk.FLAT)
    prescribe_button.pack(pady=10)

def inventory_dashboard():
    inventory_window = tk.Toplevel(root)
    inventory_window.title("Inventory Dashboard")
    inventory_window.geometry("600x400")
    inventory_window.configure(bg="#f0f0f0")

    tk.Label(inventory_window, text="Inventory Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(inventory_window, text="View Inventory Items", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    # Define how to fetch and display inventory data
    def view_inventory():
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sid123",
            database="pharma"
        )
        cursor = conn.cursor()

        # Fetch all inventory items
        cursor.execute("SELECT * FROM inventory")
        inventory_items = cursor.fetchall()

        # Clear existing content if any
        inventory_list.delete(0, tk.END)

        # Add inventory items to the list
        for item in inventory_items:
            inventory_list.insert(tk.END, f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Expiry Date: {item[3]}")

        cursor.close()
        conn.close()

    # Create a listbox to display inventory items
    inventory_list = tk.Listbox(inventory_window, bg="#fff", relief=tk.FLAT, height=10)
    inventory_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    view_inventory_button = tk.Button(inventory_window, text="View Inventory", command=view_inventory, bg="#007bff", fg="#fff", relief=tk.FLAT)
    view_inventory_button.pack(pady=10)

def pharmacist_dashboard():
    pharmacist_window = tk.Toplevel(root)
    pharmacist_window.title("Pharmacist Dashboard")
    pharmacist_window.geometry("600x400")
    pharmacist_window.configure(bg="#f0f0f0")

    tk.Label(pharmacist_window, text="Pharmacist Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(pharmacist_window, text="Medicine Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(pharmacist_window, text="Medicine Name:", bg="#f0f0f0").pack(pady=2)
    medicine_name_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    medicine_name_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Description:", bg="#f0f0f0").pack(pady=2)
    description_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    description_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Manufacturer:", bg="#f0f0f0").pack(pady=2)
    manufacturer_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    manufacturer_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Unit Price:", bg="#f0f0f0").pack(pady=2)
    unit_price_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    unit_price_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Quantity:", bg="#f0f0f0").pack(pady=2)
    quantity_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    quantity_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Expiry Date:", bg="#f0f0f0").pack(pady=2)
    expiry_date_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    expiry_date_entry.pack(pady=2)

    add_medicine_button = tk.Button(pharmacist_window, text="Add Medicine to Inventory", bg="#007bff", fg="#fff", relief=tk.FLAT)
    add_medicine_button.pack(pady=10)

    tk.Label(pharmacist_window, text="Inventory Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(pharmacist_window, text="Medicine Name:", bg="#f0f0f0").pack(pady=2)
    inventory_name_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    inventory_name_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Quantity:", bg="#f0f0f0").pack(pady=2)
    inventory_quantity_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    inventory_quantity_entry.pack(pady=2)

    tk.Label(pharmacist_window, text="Expiry Date:", bg="#f0f0f0").pack(pady=2)
    inventory_expiry_date_entry = tk.Entry(pharmacist_window, bg="#fff", relief=tk.FLAT)
    inventory_expiry_date_entry.pack(pady=2)

    view_inventory_button = tk.Button(pharmacist_window, text="View Inventory", bg="#007bff", fg="#fff", relief=tk.FLAT)
    view_inventory_button.pack(pady=10)

# Function to create Nurse Dashboard
def nurse_dashboard():
    nurse_window = tk.Toplevel(root)
    nurse_window.title("Nurse Dashboard")
    nurse_window.geometry("600x400")
    nurse_window.configure(bg="#f0f0f0")

    tk.Label(nurse_window, text="Nurse Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(nurse_window, text="Patient Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(nurse_window, text="Patient Name:", bg="#f0f0f0").pack(pady=2)
    patient_name_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    patient_name_entry.pack(pady=2)

    tk.Label(nurse_window, text="Date of Birth:", bg="#f0f0f0").pack(pady=2)
    dob_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    dob_entry.pack(pady=2)

    tk.Label(nurse_window, text="Gender:", bg="#f0f0f0").pack(pady=2)
    gender_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    gender_entry.pack(pady=2)

    tk.Label(nurse_window, text="Address:", bg="#f0f0f0").pack(pady=2)
    address_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    address_entry.pack(pady=2)

    tk.Label(nurse_window, text="Contact Number:", bg="#f0f0f0").pack(pady=2)
    contact_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    contact_entry.pack(pady=2)

    tk.Label(nurse_window, text="Prescription ID:", bg="#f0f0f0").pack(pady=2)
    prescription_id_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    prescription_id_entry.pack(pady=2)

    view_prescription_button = tk.Button(nurse_window, text="View Prescription", bg="#007bff", fg="#fff", relief=tk.FLAT)
    view_prescription_button.pack(pady=10)

    tk.Label(nurse_window, text="Prescription Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(nurse_window, text="Prescription ID:", bg="#f0f0f0").pack(pady=2)
    prescription_id_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    prescription_id_entry.pack(pady=2)

    tk.Label(nurse_window, text="Date Prescribed:", bg="#f0f0f0").pack(pady=2)
    date_prescribed_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    date_prescribed_entry.pack(pady=2)

    tk.Label(nurse_window, text="Medicine:", bg="#f0f0f0").pack(pady=2)
    medicine_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    medicine_entry.pack(pady=2)

    tk.Label(nurse_window, text="Dosage:", bg="#f0f0f0").pack(pady=2)
    dosage_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    dosage_entry.pack(pady=2)

    tk.Label(nurse_window, text="Duration:", bg="#f0f0f0").pack(pady=2)
    duration_entry = tk.Entry(nurse_window, bg="#fff", relief=tk.FLAT)
    duration_entry.pack(pady=2)

    administer_button = tk.Button(nurse_window, text="Administer Medicine", bg="#007bff", fg="#fff", relief=tk.FLAT)
    administer_button.pack(pady=10)


def other_profession_dashboard():
    other_profession_window = tk.Toplevel(root)
    other_profession_window.title("Other Profession Dashboard")
    other_profession_window.geometry("600x400")
    other_profession_window.configure(bg="#f0f0f0")

    tk.Label(other_profession_window, text="Other Profession Dashboard", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(other_profession_window, text="Tasks or Information", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)

    tk.Label(other_profession_window, text="Task 1:", bg="#f0f0f0").pack(pady=2)
    task1_entry = tk.Entry(other_profession_window, bg="#fff", relief=tk.FLAT)
    task1_entry.pack(pady=2)

    tk.Label(other_profession_window, text="Task 2:", bg="#f0f0f0").pack(pady=2)
    task2_entry = tk.Entry(other_profession_window, bg="#fff", relief=tk.FLAT)
    task2_entry.pack(pady=2)

    tk.Label(other_profession_window, text="Task 3:", bg="#f0f0f0").pack(pady=2)
    task3_entry = tk.Entry(other_profession_window, bg="#fff", relief=tk.FLAT)
    task3_entry.pack(pady=2)

    perform_action_button = tk.Button(other_profession_window, text="Perform Action", bg="#007bff", fg="#fff", relief=tk.FLAT)
    perform_action_button.pack(pady=10)

root = tk.Tk()
root.title("Pharmacy Management System")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

login_frame = tk.Frame(root, bg="#f0f0f0")
login_frame.pack(pady=20)

tk.Label(login_frame, text="Username:", bg="#f0f0f0", fg="#333").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_frame, bg="#fff", fg="#333", relief=tk.FLAT)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(login_frame, text="Password:", bg="#f0f0f0", fg="#333").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_frame, show="*", bg="#fff", fg="#333", relief=tk.FLAT)
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login, bg="#28a745", fg="#fff", relief=tk.FLAT)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

# Signup Frame
signup_frame = tk.Frame(root, bg="#f0f0f0")
signup_frame.pack(pady=20)

signup_button = tk.Button(signup_frame, text="Signup", command=signup, bg="#007bff", fg="#fff", relief=tk.FLAT)
signup_button.pack(pady=5)
# Start the application
root.mainloop()