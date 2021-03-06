# Group 3_12 : Architecture Report

## USE MANUAL AND HOW TO SETUP
You can find all the setup instructions in [this file](doc.md) (it is a small setup).
You have to run the webserver (```localhost:8000```) and then go to login.html 
(in the /web folder).  
To be able to use all features, you have to create at least two accounts
and seed money to one. To do so, you have to use our admin console.

We also provided a documentation for our API, available at ```localhost:8000/docs```. 

### Admin console : command list
Get list of commands :  
```python console.py --help```

Create an account :  
```python console.py create_user <email> <password>```

Seed money to an account :  
```python console.py create_seed_transaction <id_receiver> <amount>```

Create a transaction between two accounts :  
```python console.py create_transaction <id_author> <id_receiver> <amount>```

Enable or disable an account:  
```python console.py enable_account <id_receiver> <true/false>```

Undo a specific transaction:  
```python console.py undo_transaction <id_transaction>```

 


## ARTIFACTS
You can find in the following chapter all of the artifacts we used, and also
our architecture choices.  

### User stories and personas
All of the user stories we used throught the project are referenced in [this document](artifacts/personas_stories.md)


### Event Storming
This is the first artifact we have done for the project.  
It has helped a lot by giving us a main guidelines, which has helped making stories and other diagrams.  
Our miro has been a cloud-based working environment, we sketched a lot of the diagram there.  
If you're interested in the making-of of some of our artifacts, you can follow this link to
[our Miro.](https://miro.com/welcomeonboard/sFgH6nnijWVtJbfmW1rD0PuaAmTvR6zvUhoxmFfej7kj44MFtsuRSqiUCUAFxMZy)  
Here is our 
![our event storming](artifacts/Event_Storming_3_12.jpg) (Miro based)

### Use Cases Diagram
![Our use case diagram](artifacts/use_case.png)

### Class Diagram
First, we started by doing a basic model class diagram.
![Model Class Diagram](artifacts/model_class_diagram.PNG).  
Later on, we designed the global bank application architecture.
![Bank Application Class Diagram](artifacts/bank_class_diagram_dp.png)


### Objects Diagram
We have made 3 objects diagrams :  
User creation:
![User creation](artifacts/obj_1.png)  
Money seeding:
![Money seeding](artifacts/obj_2.png)  
Transaction
![Transaction](artifacts/obj_3.png)  
### Sequence Diagram
![Sequence Diagram](artifacts/sequence.png)

### Component Diagram
![Component Diagram](artifacts/component.png)

### Deployment Diagram
![User creation](artifacts/deployment.png)

## OUR ARCHITECTURE AND DESIGN PATTERNS

All the design patters that are in the technologies we chose to use are detailled in [this file](arch.md).  
In the Class diagram, you can also see that we're using MVC to allow the users to interact with our data throught views,
and to ensure our scalability.  

## SIGNIFICANT ARCHITECTURAL CHANGES THROUGH THE PROJECT

For the main part, we sticked to our initial conception.  
But during the development, we found that we forgot to integrate the **modified**
attribute to Transaction, to prevent users from modifying/cancelling the same task
several times.  
That is the major change that we had to make during the development.
