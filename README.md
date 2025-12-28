# User Authentication & CRUD System (Python + MySQL)

A **console-based User Authentication and CRUD application** built using **Python** and **MySQL**.  
This project demonstrates backend fundamentals such as database connectivity, authentication, and CRUD operations.

---

<img width="500" height="500" alt="Gemini_Generated_Image_5zehr55zehr55zeh" src="https://github.com/user-attachments/assets/a5f4853f-739e-46fd-8f99-16433f0afc55" />


## 📌 Features

- User Registration (Create)
- User Login & Authentication
- Update User Details
- Delete User Account
- Menu-driven CLI application
- MySQL Database integration

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Database:** MySQL  
- **Connector:** mysql-connector-python  

---

## 📂 Project Structure

.  
├── main.py  
└── README.md


---

## 🗄️ Database Schema

**Database Name:** `login_page_curd`  
**Table Name:** `cust_login_details`

```sql
CREATE TABLE cust_login_details (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_full_name VARCHAR(100),
    cust_address VARCHAR(255),
    cust_phone_number VARCHAR(15),
    cust_username VARCHAR(50) UNIQUE,
    cust_password VARCHAR(50)
);
```


## 🧩 Application Flow

1. Select an option from the main menu.
2. Based on the selection, the system performs one of the following operations:
   - Register a new user
   - Login using existing credentials
   - Update user details
   - Delete a user account
3. Authentication is mandatory for update and delete operations.
4. All database transactions are safely committed or rolled back in case of errors.

---

## 🔐 Authentication Logic
- Username is fetched from the database

- Password is validated against stored credentials

- Login succeeds only if credentials match



## 👤 Author

### Arghyajyoti Samui  
B.Tech – Electronics & Communication Engineering  
Python | MySQL | SAP Security (IAM)  
