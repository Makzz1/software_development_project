# Problem statement
A hotel wants to develop a system to manage their take-away service. The system should maintain the menu of the day. From the customer end, the system should be able to assign tokens for the registered orders and display the bill amount. The order should be confirmed
after receiving the payment and send a notification to the customer and the hotel manager.Appending the order should be disabled after payment. From the hotel manager's end, orderwise and item-wise lists should be displayed. Orders with 3 or less than 3 items can be given
higher priority. The availability of a food item should be updated to the manager and the customer (during ordering). When the order is ready, a notification should be sent to thecustomer for collecting their order.

# About code
the code has two parts were one is for customer end and the other is for kitchen end.
The customer side is for the user to place their order and to collect details about them to ensure that the ordedr reach them safely.

The kitchen/Admin end is used by the admin to check the order,about the menu,update the menu and to ensure the avalaiblity of a item in the menu
.It enables the admin to modify the menu according each day or leave them to stay as it is. It also enable the admin to check the order and to indicate the user via mail about their being ready


****
# Customer side code:
# main.py:
To start the customer side program this program is being used

# customer.py:
In this the customer detail are being collected so that later we can send them about the details of their order and also give theem the status about the order

# menu_customer.py:
In this page the customer can place their order,check for availablity , confirm their order and also can modify their order.
When they finised their order they can pay in this pay and a mail would to send to them to confirm that we reveied their order.

# our_queue.py:
This  is modified priority queue done with linked list to maintain their time complexity.This sorts the order item according to their no.of.orders and by  the rule FirstInFirstOut.
The queue gives priority to smaller order and arrage them in the queue
Each order node has a move attribute which helps us not to push the bigger too behind
***
*IMPORTANT*

To run the code in kitchen side:
start with login page

To run the code in customer side:
start with the main
****

# KITCHEN END

# login page:
This page contains the login details of the manager (The username is 'admin' and the password is '123456')

# admin_entry_page:
This page contains the things which the admin would want to work with,like display menu items, update menu items and to access and remove the pending orders

# menu_kitchen:
This page stores the list of available and non-available menu items. They are stored in text boxes and the manager would be able to view the menu but not make any changes.

# update_orders:
This page contains the code to update menu items , with functions such as add, delete and update an already existing menu item. The manager can be able to access this and make changes in the menu based on the change in the price ,availability ,etc.
It makes use csv files to read the menu items

# order_display:
This page displays the orders placed by the customer and sorts them according to  the priority , when the manager presses done, the order which is in the top , will be ready and a notification will be sent to the customer.

****
# DATABASE USED:

The application uses csv files for storing menu items and json file for storing the orders

breakfast.csv ,lunch.csv , dinner.csv - stores the respective menu items
order.json - stores respective orders placed by the customer ain priority order
email.csv - stores the name and email address of the customer for notification purposes


# VERSION CONTROL:
https://github.com/Makzz1/software_development_project.git

# CONTACT:

For any questions or suggestions, please contact:

Krithika S

Lakshaya M

Likitha Vutukuru

Maghizhvanban ES

Email :

krithika2310705@ssn.edu.in

lakshaya2310715@ssn.edu.in

likitha2310936@ssn.edu.in

maghizhvanban2310135@ssn.edu.in


