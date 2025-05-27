# ATM Simulation System

This project is a Python-based ATM Simulation System built using the Model-View-Controller (MVC) architecture. It provides a graphical user interface (GUI) using Tkinter and simulates basic ATM functionalities.

## Features

- **User Login:** Log in using your account number and PIN.
- **Balance Inquiry:** Check your current account balance.
- **Withdraw Money:** Withdraw money from your account (requires PIN validation).
- **Deposit Money:** Deposit money into your account.
- **Create New Account:** Register a new user account.
- **Profile Settings:** Update your name and PIN.

## Project Structure

```
OOMD project/
├── main.py
├── model/
│   └── atm_model.py
├── view/
│   └── atm_view.py
└── controller/
    └── atm_controller.py
```

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Prajwal7Dalawai/OOMD-Project_ATM_simulation.git
   cd OOMD project
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```

3. **Sample User Credentials:**
   - Account Number: `1234`, PIN: `5678` (John Doe, $1000 balance)
   - Account Number: `5678`, PIN: `1234` (Jane Smith, $2000 balance)

## Usage

- **Login:** Enter your account number and PIN to log in.
- **Create New Account:** Click "Create New Account" on the login screen to register.
- **Main Menu:** After logging in, you can perform various operations like checking balance, withdrawing, depositing, and updating your profile.
- **Withdraw:** Enter the amount and your PIN to withdraw money.
- **Deposit:** Enter the amount to deposit money.
- **Profile Settings:** Update your name or PIN from the main menu.

## Error Handling

The system includes error handling for:
- Invalid login credentials
- Insufficient funds
- Invalid amounts
- Missing input fields
- Incorrect PIN during withdrawal

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License. 