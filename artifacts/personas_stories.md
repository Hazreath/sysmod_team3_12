# Personas
Steven Doe (steven.doe@mail.com):
Steven Doe is our first persona. He has nothing special.  
He has always good balance, no problem with the bank whatsoever.  
He represents the classic user of our app.  

Dees Ortografia (canotwrit.lol):
Dees Ortografia has some spelling problems
She represents our users that have trouble writing correct data.

Stacy Partigirl (stacy69@party.us):
Stacy Partigirl is THE party girl. She's really easygoing but has trouble  
managing her account balance. She is, as a result, often broke.  
She represents our customer with a balance of more-or-less zero.  

Trevor Philips (trev69@thug.us):
Trevor is a well know redneck. He is constantly dealing with the police, and
is often in jail. Therefore, his account has been disabled for the time being.
He represents (ex ?)users with a disabled account.

Stacy's landlord (landlord@moni.us): 
This persona is Stacy's unlucky landlord, and he often have an argument with her concerning her payment delays.
He has been added in this document for funny scenario purposes, and he is so unimportant that he does not have a name.
Poor landlord !

John Cena (john@cena.us):
Famous catcher/actor. Yes he uses our bank.
As his famous catchphrase says, "You can't see me !".
In fact, we cannot even see his account in our databases.
He represents non-existing users.

Stonks Boi (admin@stonks.eu):
The administrator.
Has access to admin console, and has unlimited amount of (your) money.
He represents the admin.

# Use cases
## Account creation
### Normal
Stonks uses the console to create Steven Doe user(and therefore account).  
Success.
### Bad email
Stonks uses the console to create Dees Ortografia user. Fails as the email
format is not correct.

## Seed money
### Normal
Stonks seeds 20€ to Steven Doe. Success
### Account does not exists
Stonks seeds 20€ to John Cena. It fails as his user data is nowhere to be found.

## LogIn
### Normal
Steven enters his credentials, and log in.
### Mail format and amount coherence
Dees enters her credentials, and tries to login, but her mail has not correct format.
### User does not exists
John Cena logs in using his accounts info, but he still does not exists, so he has an error.

## Transactions
### Normal
Steven is going to Stacy's party and wants to contribute.
He logs into the website, goes to New Transaction.
He sends 50€ to her account. Success.

### Mail format and amount coherence
Dees logs into the website to make a transfer to Steven.
She goes to new transfer, and make the transfer. It fails, as
the mail she specified was not even an email, and the balance is not a number.

### Account does not exists
Steven wants to transfer 20€ to John Cena to get the tickets to his next show.
He logs in, goes to New Transaction, and then make the transfer.
It fails, as destination account does not exists.

### Insufficient balance
Stacy cannot accept Steven's generosity and wants to give him 60€.
She logs in, goes to new tranfer, makes the transfer, but is given an error,
since she does not have enough money.

### Account disabled
Steven wants to send 50€ to Trevor to purchase a new cowboy hat.
He logs in, goes to new transfer, and makes the transfer.
It fails, as Trevor's account is disabled.

## Account does not exits
John Cena is feeling generous and wants to do a transfer of 800€ to Stacy,
to fuel his party expenses.
He logs into the website

## Modify Transaction
### Normal
Steven feels like he didn't contribute enough to Stacy's last party, and wants to make a 100€ payment instead of 50€.
He goes to modify transfer, select the corresponding transfer, and change the amount. Success.

### Bad amount
Dees wants to do the same, but she has an error since she entered "on undrèd"
in the amount input.

### Not enough money
Stacy wants to modify his tranfer to the generous Steven, as she wants to repay him. It fails as she does not have sufficient balance.

## Delete Transaction
### Normal
Stacy is short on money and has payed her rent to her landlord, who she hates. She needs some funding for tonight party, so she decided to cancel this transfer (Stonks Bank denies any responsibility in this decision making !).
She logs in, goes to her status page, and deny the tranfer.

### Not enough money in dest account
Same scenario than previous scenario, but this time her landlord
is broke (because she never pay her rents maybe ?).
She logs in, goes to her status page, and deny the tranfer. I t fails as landlord's account has not enough fund.
