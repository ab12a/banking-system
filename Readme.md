# Project Overview
This project is a simple yet robust banking system designed to simulate real-world banking operations. It uses file handling for account management and transaction logging, and incorporates features like password hashing and a user-friendly interface.

## 🛠️ Features
- **Account Creation**:  
  Generate unique account numbers and securely store user data.

- **Login System**:  
  Authenticate users with hashed passwords.

- **Core Banking Operations**:  
  - Deposit funds.  
  - Withdraw funds (with balance checks).  
  - View account balance.

- **Transaction Logging**:  
  Keep a record of deposits and withdrawals for accountability.

- **User-Friendly Interface**:  
  Includes motivational quotes, input validation, and clear instructions.

## 🗂️ Project Structure
```
BankingSystem/
│
├── accounts.json            # Store account details in JSON format
├── transactions.csv         # Log all transactions in CSV format
├── encryption.enc           # Store encrypted sensitive data (if applicable)
├── banking_system.py        # Main Python script
├── README.md                # Project documentation
└── .gitignore               # Git ignore file for Python-related exclusions
```

## ⚙️ Installation and Setup
1. **Clone the Repository**:  
   Copy the repository URL from GitHub and clone it to your local machine.

2. **Navigate to the Project Directory**:  
   Go to the folder where the repository has been cloned.

3. **Install Dependencies**:  
   Ensure that Python 3.7 or a higher version is installed on your system. No external libraries are required for this project.

4. **Run the Application**:  
   Run the main script by executing the appropriate command for your system to start the application.

## 💡 How to Use
1. Launch the application as instructed above.  
2. Follow the on-screen menu to:  
   - Create an account.  
   - Log in using your account number and password.  
   - Perform banking operations like deposits, withdrawals, or view your balance.

## 🗂️ Data Files
The project relies on structured data files for essential operations:

- **`accounts.json`**:  
  Stores account details, such as account numbers, names, and hashed passwords, in a structured JSON format.

- **`transactions.csv`**:  
  Logs all banking transactions (deposits and withdrawals) along with timestamps for accountability and transaction tracking.

- **`encryption.enc`**:  
  Used for securely storing encrypted sensitive data, if applicable.

### Handling Data Files
- If sensitive data is included in these files, exclude them from version control by adding their names to the `.gitignore` file.
- Provide templates or instructions for generating these files if required.

## 🛡️ Security Features
- Passwords are securely hashed using the `hashlib` library.  
- Sensitive data can be encrypted and stored in `.enc` files for enhanced security.  
- Files like `accounts.json` and `transactions.csv` can be migrated to a database for better security and scalability.

## 📈 Future Enhancements
- Integration with a database (e.g., SQLite) for improved data management.  
- Enhanced user authentication with multi-factor authentication (MFA).  
- GUI version for a more interactive experience.  
- Monthly account statement generation.

