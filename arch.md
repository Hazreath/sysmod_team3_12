## Patterns

### Strategy & Factory
Take a look at the file `auth_factory.py`. This is the Factory creating our Authentication system.

Behind the scenes, we use the Strategy design pattern to implement our Authentication.
Take a look at the Interface `Auth` and then one of the implementation `JwtAuth`.
Thanks to this design pattern, we can change our Authentication implementation easily, because the Factory returns an `Auth` object (which implements the interface).


So if we want to change our implementation, we just have to change our authentication factory:
- create a new algorithm which implements the interface Auth.
- change the Auth factory to instantiate our new class (from the previous step).
- Tada! The whole system now uses the new implementation. Easy right?


For the `JwtAuth` we also use a singleton to create the configuration and to inject this configuration when we instantiate our `JwtAuth` class.


Thanks to this, we ensure that through the whole system we have the **same** configuration for our Authentication system.
