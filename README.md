
# Pay_Django

Pay_Django is a Django-based web application that integrates the Paystack payment system to facilitate secure and reliable online payments. It provides features such as creating wallets, funding wallets, and viewing wallet balances.

## Features

- **Create Wallet**: Users can create a wallet associated with their account.
- **Fund Wallet**: Users can initiate payments to fund their wallet securely using the Paystack payment system.
- **View Wallet**: Users can check their wallet balance after successful transactions.
- **Paystack Integration**: The application seamlessly integrates the Paystack payment system to ensure secure online transactions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/pay_django.git
   cd pay_django
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:

   ```bash
   python manage.py migrate
   ```
6. Run the development server:

   ```bash
   python manage.py runserver
   ```
7. Open the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. **Create Wallet**: Navigate to the "Create Wallet" page and follow the instructions to create a wallet.
2. **Fund Wallet**: Visit the "Fund Wallet" page, enter the amount, and initiate the payment using the Paystack payment system.
3. **View Wallet**: Check your wallet balance on the "View Wallet" page after a successful transaction.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
