import tkinter as tk
from tkinter import messagebox

class ATMView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("ATM System")
        self.root.geometry("400x300")
        self.setup_login_window()

    def setup_login_window(self):
        """Setup the login window"""
        self.clear_window()
        
        # Account Number
        tk.Label(self.root, text="Account Number:").pack(pady=5)
        self.account_entry = tk.Entry(self.root)
        self.account_entry.pack(pady=5)
        
        # PIN
        tk.Label(self.root, text="PIN:").pack(pady=5)
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=5)
        
        # Login Button
        tk.Button(self.root, text="Login", command=self.controller.handle_login).pack(pady=10)
        # Register Button
        tk.Button(self.root, text="Create New Account", command=self.setup_register_window).pack(pady=5)

    def setup_register_window(self):
        """Setup the registration window"""
        self.clear_window()
        tk.Label(self.root, text="Create New Account").pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack(pady=2)
        self.reg_account_entry = tk.Entry(self.root)
        self.reg_account_entry.pack(pady=2)
        tk.Label(self.root, text="PIN:").pack(pady=2)
        self.reg_pin_entry = tk.Entry(self.root, show="*")
        self.reg_pin_entry.pack(pady=2)
        tk.Label(self.root, text="Name:").pack(pady=2)
        self.reg_name_entry = tk.Entry(self.root)
        self.reg_name_entry.pack(pady=2)
        tk.Button(self.root, text="Register", command=self.controller.handle_register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.setup_login_window).pack(pady=2)

    def setup_main_menu(self):
        """Setup the main menu window"""
        self.clear_window()
        
        # Welcome Message
        user_name = self.controller.get_user_name()
        tk.Label(self.root, text=f"Welcome, {user_name}").pack(pady=10)
        
        # Menu Buttons
        tk.Button(self.root, text="Balance Inquiry", command=self.controller.show_balance).pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", command=self.controller.show_withdraw).pack(pady=5)
        tk.Button(self.root, text="Deposit Money", command=self.controller.show_deposit).pack(pady=5)
        tk.Button(self.root, text="Profile Settings", command=self.setup_profile_settings_window).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.controller.handle_logout).pack(pady=5)

    def setup_withdraw_window(self):
        """Setup the withdraw window"""
        self.clear_window()
        
        tk.Label(self.root, text="Enter amount to withdraw:").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)
        
        tk.Label(self.root, text="Enter PIN:").pack(pady=5)
        self.withdraw_pin_entry = tk.Entry(self.root, show="*")
        self.withdraw_pin_entry.pack(pady=5)
        
        tk.Button(self.root, text="Withdraw", command=self.controller.handle_withdraw).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.setup_main_menu).pack(pady=5)

    def setup_deposit_window(self):
        """Setup the deposit window"""
        self.clear_window()
        
        tk.Label(self.root, text="Enter amount to deposit:").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)
        
        tk.Button(self.root, text="Deposit", command=self.controller.handle_deposit).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.setup_main_menu).pack(pady=5)

    def setup_profile_settings_window(self):
        """Setup the profile settings window"""
        self.clear_window()
        tk.Label(self.root, text="Profile Settings").pack(pady=10)
        tk.Label(self.root, text="Change Name:").pack(pady=2)
        self.profile_name_entry = tk.Entry(self.root)
        self.profile_name_entry.insert(0, self.controller.get_user_name())
        self.profile_name_entry.pack(pady=2)
        tk.Label(self.root, text="Change PIN:").pack(pady=2)
        self.profile_pin_entry = tk.Entry(self.root, show="*")
        self.profile_pin_entry.pack(pady=2)
        tk.Button(self.root, text="Save Changes", command=self.controller.handle_profile_update).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.setup_main_menu).pack(pady=2)

    def show_balance(self, balance):
        """Show balance window"""
        self.clear_window()
        
        tk.Label(self.root, text=f"Current Balance: ${balance:.2f}").pack(pady=20)
        tk.Button(self.root, text="Back", command=self.setup_main_menu).pack(pady=5)

    def show_error(self, message):
        """Show error message"""
        messagebox.showerror("Error", message)

    def show_success(self, message):
        """Show success message"""
        messagebox.showinfo("Success", message)

    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def get_account_number(self):
        """Get account number from entry"""
        return self.account_entry.get()

    def get_pin(self):
        """Get PIN from entry"""
        return self.pin_entry.get()

    def get_amount(self):
        """Get amount from entry"""
        try:
            return float(self.amount_entry.get())
        except ValueError:
            return 0

    def get_register_details(self):
        """Get registration details from entries"""
        return (
            self.reg_account_entry.get(),
            self.reg_pin_entry.get(),
            self.reg_name_entry.get()
        )

    def get_profile_details(self):
        """Get profile details from entries"""
        return (
            self.profile_name_entry.get(),
            self.profile_pin_entry.get()
        )

    def get_withdraw_pin(self):
        """Get PIN from withdraw window entry"""
        return self.withdraw_pin_entry.get()

    def run(self):
        """Start the application"""
        self.root.mainloop() 