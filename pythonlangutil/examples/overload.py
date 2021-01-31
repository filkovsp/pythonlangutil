from pythonlangutil.overload import Overload, signature
from collections import Callable


class OverloadTest():
    def __init__(self):
        self.male_pref = "Mr. %s"
        self.female_pref = "Ms. %s"
        self.general_pref = "Dear %s"
    
    @Overload
    @signature(str, bool)
    def my_method(self, name:str, male:bool) -> str:
        if male:
            return self.male_pref % name 
        return self.female_pref % name

    @my_method.overload
    @signature(str)
    def my_method(self, name:str) -> str:
        return self.general_pref % name
    
    @my_method.overload
    @signature(int, str)
    def my_method(self, times, name):
        return "\n".join([self.general_pref % name for i in range(times)])
    
    @my_method.overload
    @signature(Callable, str)
    def my_method(self, f:Callable, name:str) -> None:
        f(name)