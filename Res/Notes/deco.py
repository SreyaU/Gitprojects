###Android Automation training DAY1 - 
# decorators/wrappers/
# ###
# print("Ready to learn android automation!!!")
import time
from functools import wraps

def authorize():
    

def  give_duration(method):
    @wraps(method)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = method(**args,**kwargs)
        duration = time.time() - start
        print(f"The method {method.__name__} took {duration:.9f} seconds")
        return result
    return wrapper

def simple_decorator(method):
    @wraps(method)
    def wrapper(*args,**kwargs):
        print("Calling the method {method.__name__} with {args}")
        return method(*args,**kwargs)
    return  wrapper

@give_duration
@simple_decorator
@authorize()
def give_squares(n):
    time.sleep(3)
    return [x*x for x in range(1,n+1)]

@give_duration
@simple_decorator
def just_print():
    print("Nothing here")