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
    # check if money is there
    print(account_1)
    # user log in, create transaction, make transaction, transaction is is validated by admin, transaction is logged

    # create transaction means user have someone's account and transfer money from
    # his account to someone's else account
    # controller.create_transaction(account owner, source acc, dest acc, amount)
    transaction_1 = controller.create_transaction(customer, account_1, account_2, 200.0)

    # admin can check account validity
    controller.check_transaction_validity(admin, transaction_1)
    # admin can complete transaction, only if transaction is already verified, but any completion will
    # have make additional prior verification
    controller.complete_transaction(admin, transaction_1)

    # user is allowed to modify his transaction
    transaction_2 = controller.create_transaction(customer, account_1, account_2, 300.0)
    controller.modify_transaction(customer, transaction_2, account_1, account_2, 350.0)

    # transaction logged


    # check user
    # print(customer)
    # transaction means
