#  Project: Mini API Simulation with Authentication & Caching
# Simulate an API-like system with user authentication and response caching using decorators.

import functools
import time

# Step 1: Simulate a session (global dictionary)
SESSION = {"is_authenticated" : False}
CACHE ={}

# Step 2: Write a login() and logout() function
def login():
    SESSION["is_authenticated"] = True
    print("Logged In")

def logout():
    SESSION["is_authenticated"] = False
    print("Logged Out")

#  Step 3: Create a decorator called authenticate_user
def authenticate_user(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not SESSION["is_authenticated"]:
            return "Unauthorized"
        else:
            return func(*args,**kwargs)
    return wrapper

# Step 4: Create another decorator cache_result
def cache_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = f"{func.__name__}_{args}_{kwargs}"
        if cache_key in CACHE:
            print("Returning from cache")
            return CACHE[cache_key]
        else:
            result = func(*args,**kwargs)
            CACHE[cache_key] = result
            print("Caching new result")
            return result
    return wrapper

# Step 5: Create dummy API functions
# Step 6: Try calling the APIs
@authenticate_user
@cache_result
def get_user_profile(user_id):
    time.sleep(2)  # Simulate DB delay
    return {"user_id": user_id, "name": "Alice", "email": "alice@example.com"}
    
#  Step 7 (Optional): Add a rate limiter decorator