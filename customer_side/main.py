import customer_side.customer_page
token = 1
def start(token):
    cus = customer_side.customer_page.Customer(token)
    cus.customer_login()



if  __name__ == '__main__':
    with open('order.json','w') as f :
        pass
    start(token)