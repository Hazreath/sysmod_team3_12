from controller import Controller

if __name__ == '__main__':
    controller = Controller()
    # we always ask controller to do something, so to create admin
    admin = controller.create_admin('Peter')
    # to create some customer
    customer = controller.create_customer('John')
    # only admin can create accounts, so we use this object, create account for customer
    account_1 = controller.create_account(admin, customer, True, 1000.0)
    # now create account for admin himself
    account_2 = controller.create_account(admin, admin, True, 2000.0)
    # only admin can seed money to account
    controller.seed_money_to_account(admin, account_1, 500.0)
    #check if money is there
    print(account_1.balance)
