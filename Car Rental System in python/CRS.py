import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Car class
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.is_available = True

    def __str__(self):
        return f"{self.year} {self.color} {self.model}"

# Rental History class
class RentalHistory:
    def __init__(self, car_model, date, rental_amount):
        self.car_model = car_model
        self.date = date
        self.rental_amount = rental_amount  # Added rental amount

# Admin class
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_car(self, car, system):
        system.all_cars.append(car)  # Add car to global list
        messagebox.showinfo("Success", f"Car '{car}' added successfully!")  # Use str method for better output

# Customer class
class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.rented_cars = []
        self.rental_history = []

    def rent_car(self, car, rental_amount):
        if car.is_available:
            self.rented_cars.append(car)
            car.is_available = False
            rental_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.rental_history.append(RentalHistory(car.model, rental_date, rental_amount))  # Include rental amount
            messagebox.showinfo("Success", f"Car '{car}' rented successfully! Amount: {rental_amount}")  # Use str method for better output
        else:
            messagebox.showerror("Error", f"Car '{car}' is not available.")

    def return_car(self, car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            car.is_available = True
            messagebox.showinfo("Success", f"Car '{car}' returned successfully!")  # Use str method for better output
        else:
            messagebox.showerror("Error", f"You haven't rented car '{car}'.")

# Car Rental System class
class CarRentalSystem:
    def __init__(self):
        self.customers = {}
        self.admins = {}
        self.all_cars = []  # Global list of all cars

    def register_admin(self, username, password):
        self.admins[username] = Admin(username, password)

    def register_customer(self, username, password):
        self.customers[username] = Customer(username, password)

    def login_admin(self, username, password):
        if username in self.admins and self.admins[username].password == password:
            return self.admins[username]
        else:
            return None

    def login_customer(self, username, password):
        if username in self.customers and self.customers[username].password == password:
            return self.customers[username]
        else:
            return None

    def search_car(self, model):
        for car in self.all_cars:  # Search in global list of all cars
            if car.model.lower() == model.lower():
                return car
        return None

# Tkinter GUI
class CarRentalApp:
    def __init__(self, root):
        self.system = CarRentalSystem()
        self.system.register_admin("admin1", "admin123")
        self.system.register_customer("cust1", "cust123")

        self.root = root
        self.root.title("Car Rental System")
        self.root.geometry("400x400")

        self.setup_main_menu()

    def setup_main_menu(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Car Rental System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.admin_login_button = tk.Button(self.root, text="Admin Login", command=self.admin_login_screen)
        self.admin_login_button.pack(pady=10)

        self.customer_login_button = tk.Button(self.root, text="Customer Login", command=self.customer_login_screen)
        self.customer_login_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Customer Register", command=self.customer_register_screen)
        self.register_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def admin_login_screen(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Admin Login", font=("Arial", 16))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.admin_login)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        admin = self.system.login_admin(username, password)

        if admin:
            self.admin_dashboard(admin)
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    def admin_dashboard(self, admin):
        self.clear_screen()
        self.label = tk.Label(self.root, text=f"Welcome, {admin.username}", font=("Arial", 16))
        self.label.pack(pady=10)

        self.add_car_button = tk.Button(self.root, text="Add Car", command=lambda: self.add_car_screen(admin))
        self.add_car_button.pack(pady=10)

        self.update_car_button = tk.Button(self.root, text="Update Car", command=lambda: self.update_car_screen(admin))
        self.update_car_button.pack(pady=10)

        self.view_rented_cars_button = tk.Button(self.root, text="View Rented Cars", command=lambda: self.display_rented_cars(admin))
        self.view_rented_cars_button.pack(pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.clear_screen)
        self.logout_button.pack(pady=10)

        self.main_menu_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.main_menu_button.pack(pady=10)

    def add_car_screen(self, admin):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Add Car", font=("Arial", 16))
        self.label.pack(pady=10)

        self.car_model_label = tk.Label(self.root, text="Car Model:")
        self.car_model_label.pack()
        self.car_model_entry = tk.Entry(self.root)
        self.car_model_entry.pack()

        self.car_year_label = tk.Label(self.root, text="Year:")
        self.car_year_label.pack()
        self.car_year_entry = tk.Entry(self.root)
        self.car_year_entry.pack()

        self.car_color_label = tk.Label(self.root, text="Color:")
        self.car_color_label.pack()
        self.car_color_entry = tk.Entry(self.root)
        self.car_color_entry.pack()

        self.add_car_button = tk.Button(self.root, text="Add Car", command=lambda: self.add_car(admin))
        self.add_car_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def add_car(self, admin):
        car_model = self.car_model_entry.get()
        year = self.car_year_entry.get()
        color = self.car_color_entry.get()
        
        if car_model and year and color:
            try:
                year = int(year)  # Convert year to int
                car = Car(car_model, year, color)
                admin.add_car(car, self.system)  # Add to global list
                self.admin_dashboard(admin)
            except ValueError:
                messagebox.showerror("Error", "Year must be a valid number.")
        else:
            messagebox.showerror("Error", "All fields must be filled out.")

    def update_car_screen(self, admin):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Update Car", font=("Arial", 16))
        self.label.pack(pady=10)

        self.car_model_label = tk.Label(self.root, text="Car Model to Update:")
        self.car_model_label.pack()
        self.car_model_entry = tk.Entry(self.root)
        self.car_model_entry.pack()

        self.new_model_label = tk.Label(self.root, text="New Car Model:")
        self.new_model_label.pack()
        self.new_model_entry = tk.Entry(self.root)
        self.new_model_entry.pack()

        self.update_car_button = tk.Button(self.root, text="Update Car", command=lambda: self.update_car(admin))
        self.update_car_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def update_car(self, admin):
        old_model = self.car_model_entry.get()
        new_model = self.new_model_entry.get()
        car = self.system.search_car(old_model)

        if car:
            car.model = new_model  # Update model
            messagebox.showinfo("Success", f"Car updated to '{car}'")
            self.admin_dashboard(admin)
        else:
            messagebox.showerror("Error", f"Car '{old_model}' not found.")

    def display_rented_cars(self, admin):
        self.clear_screen()
        rented_cars_text = "\n".join(str(car) for car in self.system.all_cars if not car.is_available)

        if rented_cars_text:
            self.label = tk.Label(self.root, text="Rented Cars:", font=("Arial", 16))
            self.label.pack(pady=10)

            self.rented_cars_label = tk.Label(self.root, text=rented_cars_text)
            self.rented_cars_label.pack(pady=10)
        else:
            self.label = tk.Label(self.root, text="No cars are currently rented.", font=("Arial", 16))
            self.label.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def customer_login_screen(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Customer Login", font=("Arial", 16))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.customer_login)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def customer_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        customer = self.system.login_customer(username, password)

        if customer:
            self.customer_dashboard(customer)
        else:
            messagebox.showerror("Error", "Invalid customer credentials")

    def customer_dashboard(self, customer):
        self.clear_screen()
        self.label = tk.Label(self.root, text=f"Welcome, {customer.username}", font=("Arial", 16))
        self.label.pack(pady=10)

        self.rent_car_button = tk.Button(self.root, text="Rent Car", command=lambda: self.rent_car_screen(customer))
        self.rent_car_button.pack(pady=10)

        self.return_car_button = tk.Button(self.root, text="Return Car", command=lambda: self.return_car_screen(customer))
        self.return_car_button.pack(pady=10)

        self.view_rental_history_button = tk.Button(self.root, text="View Rental History", command=lambda: self.view_rental_history(customer))
        self.view_rental_history_button.pack(pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.clear_screen)
        self.logout_button.pack(pady=10)

        self.main_menu_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.main_menu_button.pack(pady=10)

    def rent_car_screen(self, customer):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Rent Car", font=("Arial", 16))
        self.label.pack(pady=10)

        self.car_model_label = tk.Label(self.root, text="Car Model:")
        self.car_model_label.pack()
        self.car_model_entry = tk.Entry(self.root)
        self.car_model_entry.pack()

        self.rental_amount_label = tk.Label(self.root, text="Rental Amount:")
        self.rental_amount_label.pack()
        self.rental_amount_entry = tk.Entry(self.root)
        self.rental_amount_entry.pack()

        self.rent_button = tk.Button(self.root, text="Rent", command=lambda: self.rent_car(customer))
        self.rent_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def rent_car(self, customer):
        car_model = self.car_model_entry.get()
        rental_amount = self.rental_amount_entry.get()

        if car_model and rental_amount:
            try:
                rental_amount = float(rental_amount)  # Convert to float
                car = self.system.search_car(car_model)

                if car:
                    customer.rent_car(car, rental_amount)  # Pass rental amount to rent function
                    self.customer_dashboard(customer)
                else:
                    messagebox.showerror("Error", f"Car '{car_model}' not found.")
            except ValueError:
                messagebox.showerror("Error", "Rental amount must be a valid number.")
        else:
            messagebox.showerror("Error", "All fields must be filled out.")

    def return_car_screen(self, customer):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Return Car", font=("Arial", 16))
        self.label.pack(pady=10)

        self.car_model_label = tk.Label(self.root, text="Car Model:")
        self.car_model_label.pack()
        self.car_model_entry = tk.Entry(self.root)
        self.car_model_entry.pack()

        self.return_button = tk.Button(self.root, text="Return", command=lambda: self.return_car(customer))
        self.return_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def return_car(self, customer):
        car_model = self.car_model_entry.get()
        car = self.system.search_car(car_model)

        if car:
            customer.return_car(car)
            self.customer_dashboard(customer)
        else:
            messagebox.showerror("Error", f"Car '{car_model}' not found.")

    def view_rental_history(self, customer):
        self.clear_screen()
        history_text = "\n".join(f"{record.date} - {record.car_model} - Amount: {record.rental_amount}" for record in customer.rental_history)

        if history_text:
            self.label = tk.Label(self.root, text="Rental History:", font=("Arial", 16))
            self.label.pack(pady=10)

            self.history_label = tk.Label(self.root, text=history_text)
            self.history_label.pack(pady=10)
        else:
            self.label = tk.Label(self.root, text="No rental history available.", font=("Arial", 16))
            self.label.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def customer_register_screen(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Customer Registration", font=("Arial", 16))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self.root, text="Register", command=self.register_customer)
        self.register_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Return to Main Menu", command=self.setup_main_menu)
        self.back_button.pack(pady=10)

    def register_customer(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.system.register_customer(username, password)
            messagebox.showinfo("Success", "Customer registered successfully!")
            self.setup_main_menu()
        else:
            messagebox.showerror("Error", "All fields must be filled out.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalApp(root)
    root.mainloop()