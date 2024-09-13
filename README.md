# Greencart

Greencart is a platform designed to facilitate the trading of surplus green energy between sellers and buyers. The platform connects sellers who generate more green energy than they need with buyers looking to purchase it, with all transactions securely managed through blockchain technology and a government agency responsible for storage and delivery logistics.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

Greencart allows green energy producers to sell their surplus energy, contributing to the sustainability of energy markets. Buyers can purchase energy directly from sellers via the platform, and all transactions are handled through blockchain to ensure transparency and security. A government agency oversees the physical storage and delivery of the energy to ensure compliance and reliability.

## Features

- **Seller Platform**: Allows users to register as energy producers and list their surplus energy for sale.
- **Buyer Platform**: Buyers can register and purchase energy from available sellers.
- **Blockchain Integration**: All transactions are securely recorded using blockchain technology for transparency.
- **Energy Management**: A government agency manages energy storage and delivery logistics.
- **Data Storage**: Transaction and user data are stored in an SQL database.
- **User Interface**: Built with HTML, CSS, and JavaScript for an intuitive user experience.

## Technology Stack

- **Backend**: Python (for managing transactions, user accounts, and database operations)
- **Database**: SQL (to store transaction and user data)
- **Blockchain**: Implemented to securely track and verify transactions
- **Frontend**: HTML, CSS, JavaScript (for the user interface)
- **Government Agency**: Handles energy storage and delivery

## Installation

1. Clone the repository:

   ```bash
   https://github.com/XaXtric7/GreeenCart.git
   ```

2. Navigate to the project directory:

   ```bash
   cd greencart
   ```

3. Installing and verifying pip:

   ```bash
   python -m ensurepip --upgrade
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python get-pip.py
   pip --version
   *run in cmd*
   ```

4. Commands to run in SQL cmd:

   ```bash
   use project
   Select * from contributions;
   Select * from purchases;
   *To view tables*
   ```

5. Install the required Python packages:

   ```bash
   python -m pip show Flask
   pip install Flask Flask-MySQLdb
   pip install mysql-connector-python
   pip install flask-cors
   ```

6. Set up the SQL database (e.g., MySQL, PostgreSQL):

   - Create a new database and configure the connection details in the backend settings.

7. Run the application:
   ```bash
   python app.py
   ```

## Usage

1. **For Sellers**: Register, list your surplus energy, and set your prices.
2. **For Buyers**: Browse available energy listings, choose a seller, and purchase energy.
3. **Blockchain**: All transactions are recorded in a blockchain to ensure security and transparency.
4. **Delivery**: The government agency manages the delivery process once a transaction is completed.

## Site Preview

```bash
   ![GreenCart gif](https://github.com/user-attachments/assets/74059085-5661-43a5-9ab9-6a52a7934111)
```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact the project team:

- [Amish Mathur (Amishmathur1)](https://github.com/amishmathur1)
- [Ansh (PikachuGX)](https://github.com/PikachuGX)
- [Sarthak Dharmik (XaXtric7)](https://github.com/XaXtric7)
