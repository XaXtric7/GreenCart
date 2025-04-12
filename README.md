# 🌿 Greencart

**Greencart** is a blockchain-powered platform that facilitates the **trading of surplus green energy** between sellers and buyers. It enables energy producers to sell excess clean energy, while buyers can securely purchase verified green energy through a transparent and decentralized system. A government agency handles **storage and delivery logistics** for efficient energy distribution. 🌍⚡

---

## 📚 Table of Contents

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Technology Stack](#-technology-stack)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [🌐 Site Preview](#-site-preview)
- [📽️ PPT for Hackathon](#-ppt-for-hackathon)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## 📖 Overview

Greencart empowers green energy producers to **monetize their surplus energy** and supports buyers in **directly accessing renewable energy**. Every transaction is secured using **blockchain technology**, ensuring **transparency** and **tamper-proof records**. Delivery and physical energy management are overseen by a **government agency**, maintaining regulatory compliance and trust.

---

## ✨ Features

- 🧾 **Seller Platform**: Register as an energy producer and list surplus energy for sale.
- 🛒 **Buyer Platform**: Browse listings and purchase available green energy.
- 🔗 **Blockchain Integration**: Secure and immutable transaction records.
- 🏢 **Government Agency Integration**: Manages logistics for energy storage and delivery.
- 🗃️ **Data Storage**: All data is stored in an SQL database.
- 💻 **User Interface**: Built with HTML, CSS, and JavaScript for a clean and intuitive experience.

---

## 🛠️ Technology Stack

- 🐍 **Backend**: Python (handles logic, routing, and database ops)
- 🧮 **Database**: MySQL / SQL (for user and transaction data)
- 🔐 **Blockchain**: Ensures secure, traceable transactions
- 🎨 **Frontend**: HTML, CSS, JavaScript
- 🏢 **Government Role**: Oversees physical energy logistics and compliance

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/XaXtric7/GreeenCart.git
```

### 2. Navigate to the Project Directory

```bash
cd greencart
```

### 3. Install and Verify `pip`

```bash
python -m ensurepip --upgrade
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip --version
```

### 4. SQL Commands (in MySQL shell)

```sql
USE project;
SELECT * FROM contributions;
SELECT * FROM purchases;
```

### 5. Install Required Python Packages

```bash
pip install Flask Flask-MySQLdb
pip install mysql-connector-python
pip install flask-cors
```

### 6. Set Up SQL Database

- Create a new database (e.g., `project`) and configure your credentials in `app.py`.

### 7. Run the Application

```bash
python app.py
```

---

## 🚀 Usage

1. 🧑‍🌾 **Sellers**: Register, list energy, set price.
2. 🧑‍💼 **Buyers**: Browse listings, purchase energy.
3. 🔒 **Blockchain**: Handles secure transactions.
4. 🏗️ **Delivery**: Managed by the government agency post-transaction.

---

## 🌐 Site Preview

![GreenCart gif](https://github.com/user-attachments/assets/917d066a-71f0-4fee-951a-56aa628a8160)

---

## 📽️ PPT for Hackathon

📁 [Download Presentation - Tech4Tomorrow_hackathon.pptx](https://github.com/user-attachments/files/17082889/Tech4Tommorow_hackathon.pptx)  
💫 _Includes morph transitions for smooth visuals._

---

## 🤝 Contributing

We welcome all contributions! 🛠️  
Follow these steps:

1. 🍴 Fork this repository
2. 🌿 Create a new branch (`feature/your-feature-name`)
3. ✅ Commit your changes
4. 🚀 Push to your branch
5. 🔁 Open a Pull Request

---

## 📄 License

Licensed under the [MIT License](LICENSE) 📝  
Feel free to use and modify with attribution.

---

## 📬 Contact

Got questions or ideas? Reach out to us!

- 👨‍💻 [Amish Mathur (amishmathur1)](https://github.com/amishmathur1)
- 👨‍💻 [Ansh (PikachuGX)](https://github.com/PikachuGX)
- 👨‍💻 [Sarthak Dharmik (XaXtric7)](https://github.com/XaXtric7)
