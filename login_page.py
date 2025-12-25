import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Welcome",
    database="login_page_curd")
cur_obj=conn_obj.cursor()

#To register new users
def register_user():
    cust_full_name = input("Enter Full Name: ")
    cust_address = input("Enter Address: ")
    cust_phone_number = input("Enter Phone Number: ")
    cust_username = input("Set Username: ")
    cust_password = input("Set Password: ")
    data_entry_sql(cust_full_name, cust_address, cust_phone_number, cust_username, cust_password)


#Define function data_entry_sql
def data_entry_sql(cust_full_name,cust_address,cust_phone_number,cust_username,cust_password):
    # Build the query with user-provided name using LIKE operator
    sql = "insert into cust_login_details (cust_full_name,cust_address,cust_phone_number,cust_username,cust_password) values (%s,%s,%s,%s,%s)"
    data = (cust_full_name,cust_address,cust_phone_number,cust_username,cust_password)

    try:
        cur_obj.execute(sql, data)
        print("NEW CUSTOMER ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from Database: ", e)
        conn_obj.rollback()


# Authenticate User
def authenticate (cust_details_db, cust_password) :
    if cust_details_db:
        pwd_from_db = cust_details_db[5]
        # print(pwd_from_db)
        if pwd_from_db == cust_password:
            return True
        else:
            return False
    else:
        return False


# To help user to login
def loggin_user(cust_username, cust_password):
    cust_details_db=data_retrieve(cust_username)
    authenticated_user = authenticate(cust_details_db, cust_password)
    if authenticated_user:
        print("You've Logged in Successfully")
    else:
        print("Wrong Credentials")
        options = input("Want to Register? \nY to Yes \nPress any other key to continue -> ").upper()
        match options:
            case "Y":
                register_user()


#Define function data_retrieve
def data_retrieve(cust_username):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    query = f"select * from cust_login_details where cust_username=\"{cust_username}\""

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone() # limit 1 in SQL
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result


# To Update User Details
def update_details(cust_username, cust_password):
    # print("Inside update")
    cust_details = data_retrieve(cust_username)
    user_authinticated = authenticate(cust_details, cust_password)
    sql_query = ""
    if user_authinticated:
        update_option = input("Enter the Option you want to Update-> \n1. Name\n2. Address \n3. Phone Number\n4.All Details ")
        match update_option:
            case "1":
                old_name = cust_details[1]
                print(f"Old Name {old_name}")
                new_name = input("Enter the New Name -> ")
                sql_query = f"update cust_login_details set cust_full_name=\"{new_name}\" where cust_username = \"{cust_username}\""

            case "2":
                old_address = cust_details[2]
                print(f"Old Address {old_address}")
                new_address = input("Enter the New Address -> ")
                sql_query = f"update cust_login_details set cust_address=\"{new_address}\" where cust_username = \"{cust_username}\""
            case "3":
                old_phone_number = cust_details[3]
                print(f"Old Phone Number {old_phone_number}")
                new_phone_number = input("Enter the New Phone Number -> ")
                sql_query = f"update cust_login_details set cust_phone_number=\"{new_phone_number}\" where cust_username = \"{cust_username}\""
            case "4":
                new_name = input("Enter the New Name -> ")
                new_address = input("Enter the New Address -> ")
                new_phone_number = input("Enter the New Phone Number -> ")
                sql_query = f"update cust_login_details set cust_full_name=\"{new_name}\", cust_address=\"{new_address}\", cust_phone_number=\"{new_phone_number}\" where cust_username = \"{cust_username}\""
            case default:
                print("Enter Correct Option from the provided list")
        try:
            cur_obj.execute(sql_query)
            print("User details updated successfully")
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from Database: ", e)
            conn_obj.rollback()
    else:
        print("User Authentication Failed")


# To Delete User Details
def delete_user_details(cust_username, cust_password):
    cust_details = data_retrieve(cust_username)
    user_authinticated = authenticate(cust_details, cust_password)
    cid = None
    if user_authinticated:
        cid = cust_details[0]
    sql_query = f"delete from cust_login_details where cust_id = {cid};"
    try:
        cur_obj.execute(sql_query)
        print("User details updated successfully")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from Database: ", e)
        conn_obj.rollback()

#Main Function
def main():
    print("Select from below options -> ")
    choice = input("1. Register for New User \n2. Login for Existing User \n3. Update Details \n4. Delete Data\n")

    match (choice):
        case "1":
            print("Register ->")
            register_user()

        case "2":
            print("Login ->")
            cust_username = input("Enter Username: ")
            cust_password = input("Enter Password: ")
            loggin_user(cust_username, cust_password)
        case "3":
            print("Update Details ->")
            cust_username = input("Enter Username: ")
            cust_password = input("Enter Password: ")
            update_details(cust_username, cust_password)
        case "4":
            print("Delete Details -> ")
            cust_username = input("Enter Username: ")
            cust_password = input("Enter Password: ")
            delete_user_details(cust_username, cust_password)

        case default:
            print("Select from given options")

    conn_obj.close()

main()
