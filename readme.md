# Simple ATM System

## Overview:
This **Simple ATM System** is a simple command-line interface application written in Python. It allows users to perform basic banking operations such as logging in, creating an account, depositing money, withdrawing money, transferring funds to other accounts, checking balance, and changing PIN.

## Features:
1. **User Authentication:** Users can log in securely using their user ID and PIN.
2. **Account Creation:** New users can create an account with a unique user ID and PIN.
3. **Deposit:** Users can deposit money into their account.
4. **Withdrawal:** Users can withdraw money from their account, provided they have sufficient funds.
5. **Transfer:** Users can transfer money to other users' accounts.
6. **Transaction History:** Users can view their transaction history, including deposits, withdrawals, and transfers.
7. **Balance Inquiry:** Users can check their current account balance.
8. **PIN Change:** Users can change their PIN for added security.

## File Structure:
- `atm.py`: The main Python script containing the classes `User` and `ATM`, as well as the `main()` function to run the ATM system.
- `users.json`: A JSON file used to store user data, including user IDs, PINs, and account balances.

## Usage:
1. **Running the Program:**
   - Ensure you have Python installed on your system.
   - Execute the `atm.py` script in a Python environment.
   - Follow the prompts to navigate through the ATM system.

2. **Logging In:**
   - Existing users can log in using their user ID and PIN.
   - If authentication is successful, users can perform banking operations.

3. **Creating an Account:**
   - New users can create an account by providing a desired user ID and PIN.
   - User IDs must be unique.

4. **Operations:**
   - Once logged in, users can choose from various operations listed in the menu.
   - Operations include deposit, withdrawal, transfer, transaction history display, balance inquiry, and PIN change.

5. **Exiting the Program:**
   - Users can exit the program by selecting the appropriate option from the main menu.

<table align="center">
  <tr>
    <td><img src="screenshots/atm.jpg" alt="Index Page" width="800" height="1800"/></td>
  </tr>
  
</table>

## Data Persistence:
- User data is stored in a JSON file named `users.json`.
- User accounts and their associated information are loaded from and saved to this file to ensure data persistence between sessions.

## Security:
- User PINs are securely stored and authenticated before allowing access to account information or transactions.
- PIN change functionality is provided for users to update their PINs as needed.

## Error Handling:
- The system includes error handling to manage invalid inputs, insufficient funds, and other exceptional scenarios.

## Getting Started:
To get started with the **Simple ATM System**, follow these steps:
1. Ensure you have Python installed on your system.
2. Download or clone this repository containing the ```atm.py``` script.
3. Open a terminal or command prompt and navigate to the directory where ```atm.py``` is located.
4. Run the ```atm.py``` script by executing the command ```python atm.py```.
5. Follow the prompts to navigate through the ATM system and perform banking operations.


## Contributing<a name="contributing"></a>

I welcome contributions to enhance this repo. Feel free to open issues or submit pull requests.

## License<a name="license"></a>

This project is licensed under the [MIT License](LICENSE).

Thank you for using this repo! Feel free to reach out with any questions or feedback.

<em style="color: #ff66b2; font-weight: bold;">✨ --- Designed & made with Love by Shib Kumar Saraf ✨</em>
