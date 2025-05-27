class ATMModel:
    def __init__(self):
        # Sample user data (in-memory storage)
        self.users = {
            "1234": {
                "pin": "5678",
                "balance": 1000.0,
                "name": "John Doe"
            },
            "5678": {
                "pin": "1234",
                "balance": 2000.0,
                "name": "Jane Smith"
            }
        }
        self.current_user = None

    def validate_user(self, account_number, pin):
        """Validate user credentials"""
        if account_number in self.users and self.users[account_number]["pin"] == pin:
            self.current_user = account_number
            return True
        return False

    def get_balance(self):
        """Get current user's balance"""
        if self.current_user:
            return self.users[self.current_user]["balance"]
        return None

    def withdraw(self, amount, pin):
        """Withdraw money from account"""
        if not self.current_user:
            return False, "No user logged in"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        if self.users[self.current_user]["pin"] != pin:
            return False, "Incorrect PIN"
        
        if amount > self.users[self.current_user]["balance"]:
            return False, "Insufficient funds"
        
        self.users[self.current_user]["balance"] -= amount
        return True, f"Withdrawn ${amount:.2f}"

    def deposit(self, amount):
        """Deposit money to account"""
        if not self.current_user:
            return False, "No user logged in"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        self.users[self.current_user]["balance"] += amount
        return True, f"Deposited ${amount:.2f}"

    def get_user_name(self):
        """Get current user's name"""
        if self.current_user:
            return self.users[self.current_user]["name"]
        return None

    def logout(self):
        """Logout current user"""
        self.current_user = None

    def register_user(self, account_number, pin, name):
        """Register a new user account"""
        if account_number in self.users:
            return False, "Account number already exists"
        self.users[account_number] = {
            "pin": pin,
            "balance": 0.0,
            "name": name
        }
        return True, "Account created successfully"

    def update_user_details(self, name=None, pin=None):
        """Update current user's name and/or PIN"""
        if not self.current_user:
            return False, "No user logged in"
        if name:
            self.users[self.current_user]["name"] = name
        if pin:
            self.users[self.current_user]["pin"] = pin
        return True, "Profile updated successfully" 