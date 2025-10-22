# from mini_api import get_user_profile, login, logout

# print(get_user_profile(101))
# login()
# print(get_user_profile(101))    
# print(get_user_profile(101))
# logout()

class FileProcessingError(Exception):
    pass
class DataValidationError(Exception):
    pass
class APIRequestError(Exception):
    pass

def read_file(filename):
    try:
        with open (filename,'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise FileProcessingError (f"File '{filename}' not found.")

def validate_data(data):
    if not data.startswith("VALID"):
        raise DataValidationError("data does not start with 'VALID'.")

def send_to_api(data):
    success = False
    if not success:
        raise APIRequestError("API request failed with status code 500.")
    
def process_data_pipeline(filename):
    try:
        data = read_file(filename)
        validate_data(data)
        send_to_api(data)
        print("✔️ Data processed and sent to API successfully.")
    except FileProcessingError as fpe:
        print("File error:", fpe)
    except DataValidationError as dve:
        print("data error:", dve)
    except APIRequestError as APIe:
        print("api error:", APIe)

process_data_pipeline("input.txt")