# Python Languauge Utilities

This library provides utilities to use features of other languages in Python.

This fork contains some improvements on top the the [original repo](https://github.com/ehsan-keshavarzian/pythonlangutil).

## Usage:

### Access Modifiers:
- Identify a variable as private:
    ```python
    from pythonlangutil.access_modifiers import private_variable
        
    class PrivateVariableTest(object):
        def __init__(self):
            self.id = "123"
            
        @private_variable('id')
        def __setattr__(self, *args, **kwargs):
            return object.__setattr__(self, *args, **kwargs)
        
        def insider(self):
            self.id = "321"
    ```
- Identify a method as private:
    ```python
   from pythonlangutil.access_modifiers import private_function
    
   class PrivateFunctionTest(object):
      def __init__(self):
          pass
      
      @private_function
      def private_method(self):
          return 'called from inside my own class'
      
      def insider(self):
          return self.private_method()
    ```

### Method Overloading:   
```python
   class OverloadTest():
       def __init__(self):
           self.male_pref = "Mr. %s"
           self.female_pref = "Ms. %s"
           self.general_pref = "Dear %s"
       
       @Overload
       @signature(str, bool)
       def my_method(self, name, male):
           if male:
               return self.male_pref % name 
           return self.female_pref % name
   
       @my_method.overload
       @signature(str)
       def my_method(self, name):
           return self.general_pref % name
       
       @my_method.overload
       @signature(int, str)
       def my_method(self, times, name):
           return "\n".join([self.general_pref % name for i in range(times)])
```

### Singleton pattern:
It prevents the instantiation of the class. The only instance of the class will be accessible through get_instance() method which will be added to class automatically.
```python
   from pythonlangutil.singleton import Singleton

   @Singleton()
   class SingletonTest():
       def __init__(self):
           pass
```