Car Rental System - README
Project Overview
The Car Rental System is a Python-based desktop application built using the Tkinter library for the graphical user interface (GUI). The system allows administrators to manage a fleet of cars and customers to rent available cars. It keeps track of rental history, rental amounts, and the availability of cars, providing a simple yet efficient solution for car rental management.

Features
Admin Features:
Login: Admin can log in with a username and password.
Add Car: Admin can add new cars to the system by providing details like the model, year, and color.
Update Car: Admin can update the model of an existing car.
View Rented Cars: Admin can view all currently rented cars.
Logout: Admin can safely log out from the system.

Customer Features:
Register: New customers can register with a username and password.

Login: Customers can log in using their credentials.
Rent a Car: Customers can search for available cars and rent them by specifying a rental amount.
Return a Car: Customers can return rented cars to make them available for others.
View Rental History: Customers can view their rental history, including dates and rental amounts.
Logout: Customers can safely log out from the system.

Technologies Used:
Python: The programming language used for the back-end logic.
Tkinter: Python’s standard GUI library used to build the application interface.
datetime: Used for capturing rental dates and times.


How to Run the Project
1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
 3. Clone the repository or download the source code.
4. Navigate to the project directory and run the following command:
 5. The Car Rental System GUI will launch.

SCREENSHOTS (How it runs):
•	Initial GUI :
 ![image](https://github.com/user-attachments/assets/b7355862-b51f-464d-a15c-7900bc844d40)


•	Admin Login : 
 ![image](https://github.com/user-attachments/assets/6ed0d149-3dbe-4e02-b28c-1a1ca094fabb)
 ![image](https://github.com/user-attachments/assets/fe9bb7c6-3627-4725-9bac-7fc12525b8e4)
 ![image](https://github.com/user-attachments/assets/4059fa74-08af-427e-bb60-18c89864aad6)
 

•	Customer Login:
 
![image](https://github.com/user-attachments/assets/4ea2be83-e207-4474-8682-726f3c614060)
![image](https://github.com/user-attachments/assets/45b5b58f-0c05-44a7-bf67-7cbb3aafd122)
![image](https://github.com/user-attachments/assets/b6f48d4c-f048-4533-95b7-22d3d12d4ceb)


•	Customer Register: 
 
![image](https://github.com/user-attachments/assets/84a7d81f-1a11-4489-a6df-21ab8d50e497)

Usage Instructions:
Admin Access: The default admin credentials are:
Username: admin1
Password: admin123

Customer Access: A default customer is pre-registered:
Username: cust1
Password: cust123

After logging in, use the available buttons to perform actions like renting a car, returning it, or viewing the rental history.

Project Structure:
Car Class: Represents each car with details like model, year, and color.
Customer Class: Handles customer functionalities like renting and returning cars.
Admin Class: Admins manage car information within the system.
CarRentalSystem Class: Central system managing all admins, customers, and cars.
RentalHistory Class: Logs the rental history with rental dates and amounts.
CarRentalApp Class: Handles the Tkinter GUI, allowing user interactions with the system.

Future Enhancements
Payment Integration: Add payment gateway for online transactions.
Car Availability Filters: Enhance the car search feature with filters (e.g., by year, model, or rental price).
Extended Reporting: Provide detailed reports for admins on rental trends and earnings.

License
This project is open-source and available under the MIT License.

