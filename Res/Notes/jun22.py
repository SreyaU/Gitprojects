# x = int(input("Enter a number: "))
# if x==0:
#     print("You entered zero!")
# elif x < 0:
#     print("You entered a negative number!")
# else:
#     print("You entered a positive number!")

# for i in range(1,21):
#     if (i % 2) == 0:
#         print(i)
#     else:
#         continue

# sum = 0
# i = 0
# while (i < 101):
#     sum += i
#     i += 1
# print("sum is ",sum)

# def is_even(n):
#     if (n % 2) == 0:
#         return True
#         # print("return is ", return)
#     else:
#         return False
#         # print("return is ", return)

# print(is_even(4))
# print(is_even(9))

# def reverse_string(strinput):
#     rev_strOut = strinput[::-1]
#     print("inputStr: ", strinput)
#     print("outputStr: ", rev_strOut)

# reverse_string("cat")

# def remove_duplicates(lst):
#     uniq_lst = []
#     for num in lst:
#         if num not in uniq_lst:
#             uniq_lst.append(num)
#     return  uniq_lst

# print(remove_duplicates([1,2,2,3,4,4,5]))

# list_of_squares = []
# i=1
# while i <= 10:
#     list_of_squares.append(pow(i,2))
#     i +=1
# print(list_of_squares)    

# list_of_squares = [i**2 for i in range(1,11)]
# print(list_of_squares)   

# def char_count_function(strInput):
#     count_dict = {}
#     for i in strInput: 
#         if i not in count_dict.keys():
#             newkey = i
#             count_dict[newkey] = '1'
#         elif i in count_dict.keys():
#             keyval = i
#             cnt_val = count_dict[keyval]
#             intcntv = int(cnt_val)
#             newval = intcntv + 1
#             count_dict[keyval] = newval
#     return count_dict

# def char_count_function(strInput):
#     count_dict = {}
#     for i in strInput: 
#         if i in count_dict:
#             count_dict[i] +=1
#         else:
#             count_dict[i] = 1
#     return count_dict
# print(char_count_function("hello"))

# file = open("sample.txt","r")
# lines = file.readlines()
# print(len(lines))

# with open("sample.txt", "r") as file:
#     lines = file.readlines()
#     print(len(lines))

# def multiply_all(*args):
#     result = 1
#     for num in args:
#         if isinstance(num, (int,float)):
#             result *= num
#         else:
#             raise TypeError("only numbers allowed")
#     return result

# print(multiply_all(1,2,3,4))

# def build_profile(**kwargs):
#     if not kwargs:
#         raise ValueError("No profile added")
#     else:
#         return kwargs
    
# profile = build_profile(Name="Sreya", Age="24", Jobrole="WLAN Test Engineer")
# print(profile)

# def send_email(to, *attachments, **meta):
#     print(f"sending mail to : {to}")
#     if attachments:
#         print("attachments:")
#         for i, file in enumerate(attachments,1):
#             print(f"{i}.{file}")
#     else:
#         print("no attachments")
#     if meta:
#         for key,value in meta.items():
#             print(f"{key}:{value}")
#     else:
#         print("no metadata")

# send_email("sreyau@gmail.com","report.pdf","log.txt","summary.xls",subject="System status", priority="high")

# tempList = [10, 0, 30, 100]
# F = list(map(lambda c:c* 9/5 + 32, tempList))
# print(F)

# num = [1,2,3,4,5,6,7,8,9,10]
# Odd = list(map((lambda n : n**3) ,filter(lambda n : n % 2 !=0, num)))
# print(Odd)

# teststr = ["I", "cat", "Elephant","Mosquito", "pen"]
# char5list = list(filter(lambda x : len(x) > 5, teststr))
# print(char5list)

# def clean_emails(emails):
#     valid_mailid = list(map(lambda mailid : mailid.lower(),filter(lambda mailid : '@' in mailid,emails)))
#     return print(valid_mailid)

# emails = ["sreyartrjui.com","sreyau7@gmail.com"]
# clean_emails(emails)

# from functools import reduce
# nums = [1,2,3,4,5,6]
# sum = 0
# result = reduce(sum=+num ,list(lambda num : num % 2 == 0))
# print(result)


# import re
# valid = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
# test="asdfghh@fghjk.com , @asdf , sdfgh.com ,sdfgh@"
# emails = re.findall(valid,test)
# print(emails)

# log="User1 used 2345678906788975, User2 used 3456789012385464"
# ids=re.compile(r"(\d{16})")
# maskLog = re.sub(ids,"****REDACTED****",log)
# print(maskLog)

# def check_productCode(product_code):
#     valid = re.compile(r"(^[A-Z]{3}\-\d{4})")
#     match = re.fullmatch(valid,product_code)
#     if match:
#         print(match.group())
#     else:
#         print("no match found")
# check_productCode("ABC-124")

# text="sdf;l,fghj,g;jhgfkg;hg"
# match=re.split(r"[,;]",text)
# print(match)

# log="asdfglkj dfghu xfgh 09:34, sdfghj bjh 23:06, sdfghj df 03:45"
# timestmp=re.compile(r"(\d{2}\:\d{2})")
# timelogs=re.findall(timestmp,log)
# print(timelogs)

# print("hI SREYA!! Welcome back")

#Abstraction is used - class, method, private attribute
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.__base_salary = base_salary

#     @abstractmethod
#     def calculate_salary(self):
#         pass
#     def get_base_salary(self):
#         return self.__base_salary

# #inheritance is used, method of superclass used here and polymorphism used
# class Manager(Employee):
#     def __init__(self, name, base_salary, team_size):
#         super().__init__(name, base_salary)
#         self.team_size = team_size
#     def calculate_salary(self):
#         return self.get_base_salary() + (self.team_size*500)
    
# class Developer(Employee):
#     def __init__(self, name, base_salary, bonus):
#         super().__init__(name, base_salary)
#         self.bonus = bonus
#     def calculate_salary(self):
#         return self.get_base_salary() + self.bonus

# #create objects
# dev = Developer("Alice", 50000, 8000)
# mgr = Manager("Bob", 60000, 5)

# # Polymorphic function
# def print_salary(employee):
#     print(f"{employee.name}'s salary: {employee.calculate_salary()}")

# print_salary(dev)  # Alice's salary: 58000
# print_salary(mgr)

# def echo():
#     while True:
#         x = yield  # Generator pauses and waits for a value
#         print(f"Received: {x}")

# gen = echo()
# next(gen)          # Start the generator
# gen.send("hello")  # Output: Received: hello

# def add_to_list(val, lst=[]):
#     lst.append(val)
#     return lst

# print(add_to_list(1))
# print(add_to_list(2))

class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # pass

    def show_details(self):
        # Instance method
        return self.name, self.salary, Employee.company_name
        # pass

    @classmethod
    def set_company(cls, new_name):
        # Class method
        Employee.company_name = new_name
        # pass

    @staticmethod
    def is_high_salary(amount):
        # Static method
        if amount >= 45000:
            return True
        else:
            return False
        # pass


# 🧪 Try it out
emp1 = Employee("Alice", 90000)

emp1.show_details()                # Instance method
print(Employee.company_name)       # Show default company
emp1.set_company("InnoTech")       # Class method via instance
print(Employee.company_name)       # Confirm it's changed

print(Employee.is_high_salary(95000))  # Static method via class ✅
print(emp1.is_high_salary(40000))      # Static method via instance ✅
