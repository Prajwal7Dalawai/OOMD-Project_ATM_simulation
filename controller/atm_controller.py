class ATMController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_login(self):
        """Handle login button click"""
        account_number = self.view.get_account_number()
        pin = self.view.get_pin()

        if not account_number or not pin:
            self.view.show_error("Please enter both account number and PIN")
            return

        if self.model.validate_user(account_number, pin):
            self.view.setup_main_menu()
        else:
            self.view.show_error("Invalid account number or PIN")

    def handle_logout(self):
        """Handle logout button click"""
        self.model.logout()
        self.view.setup_login_window()

    def show_balance(self):
        """Show current balance"""
        balance = self.model.get_balance()
        if balance is not None:
            self.view.show_balance(balance)
        else:
            self.view.show_error("Error retrieving balance")

    def show_withdraw(self):
        """Show withdraw window"""
        self.view.setup_withdraw_window()

    def show_deposit(self):
        """Show deposit window"""
        self.view.setup_deposit_window()

    def handle_withdraw(self):
        """Handle withdraw button click"""
        amount = self.view.get_amount()
        pin = self.view.get_withdraw_pin()
        if amount <= 0:
            self.view.show_error("Please enter a valid amount")
            return
        if not pin:
            self.view.show_error("Please enter your PIN")
            return
        success, message = self.model.withdraw(amount, pin)
        if success:
            self.view.show_success(message)
            self.view.setup_main_menu()
        else:
            self.view.show_error(message)

    def handle_deposit(self):
        """Handle deposit button click"""
        amount = self.view.get_amount()
        if amount <= 0:
            self.view.show_error("Please enter a valid amount")
            return

        success, message = self.model.deposit(amount)
        if success:
            self.view.show_success(message)
            self.view.setup_main_menu()
        else:
            self.view.show_error(message)

    def get_user_name(self):
        """Get current user's name"""
        return self.model.get_user_name()

    def handle_register(self):
        """Handle registration button click"""
        account_number, pin, name = self.view.get_register_details()
        if not account_number or not pin or not name:
            self.view.show_error("Please fill in all fields")
            return
        success, message = self.model.register_user(account_number, pin, name)
        if success:
            self.view.show_success(message)
            self.view.setup_login_window()
        else:
            self.view.show_error(message)

    def handle_profile_update(self):
        """Handle profile update button click"""
        name, pin = self.view.get_profile_details()
        if not name and not pin:
            self.view.show_error("Please enter a new name or PIN")
            return
        # Only update fields that are not empty
        update_name = name if name else None
        update_pin = pin if pin else None
        success, message = self.model.update_user_details(name=update_name, pin=update_pin)
        if success:
            self.view.show_success(message)
            self.view.setup_main_menu()
        else:
            self.view.show_error(message) 