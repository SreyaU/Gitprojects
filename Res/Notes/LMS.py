'''🔸 1. Library Management System
Problem:
Design a system to manage books, members, and borrowing logic.

Requirements:
A base class LibraryItem with common attributes like title, author, and item_id.

Subclasses Book, Magazine, DVD each with different borrow_duration.

Method is_overdue() that returns True if the item is overdue.

Members should be able to borrow multiple items.

📌 Concepts: Inheritance, Polymorphism, Abstraction, Encapsulation'''

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC):
    def __init__(self,title,author,item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        #not initilaizing till borrow , so val=none
        self.borrow_date = None

    def borrow_item(self,borrow_date):
        self.borrow_date = borrow_date

    @abstractmethod
    def is_overdue(self,current_date):
        pass

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.item_id})"

class Book(LibraryItem):

    borrow_duration_days = 14

    def is_overdue(self,current_date):
        if not self.borrow_date:
            return False
        return (current_date - self.borrow_date).days > self.borrow_duration_days

class Magazine(LibraryItem):
    borrow_duration_days = 7
    def is_overdue(self,current_date):
        if not self.borrow_date:
            return False
        return (current_date - self.borrow_date).days > self.borrow_duration_days
    
    
class DVD(LibraryItem):
    borrow_duration_days = 3
    def is_overdue(self,current_date):
        if not self.borrow_date:
            return False
        return (current_date - self.borrow_date).days > self.borrow_duration_days
   

class Member:
    def __init__(self,name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []
    
    def borrow_item(self,item, borrow_date):
        item.borrow_item(borrow_date)
        self.borrowed_items.append(item)
    
    def list_borrowed_items(self):
        if not self.borrowed_items:
            print(f"{self.name} has not borrowed any items.")
        else:
            print(f"{self.name}'s borrowed items:")
            for item in self.borrowed_items:
                print(f"  - {item}")

    def list_overdue_items(self,current_date):
        print(f"Checking overdue items for {self.name} on {current_date.strftime('%Y-%m-%d')}:")
        overdue_items = [item for item in self.borrowed_items if item.is_overdue(current_date)]
        if not overdue_items:
            print("  No overdue items.")
        else:
            for item in overdue_items:
                print(f"{item} is overdue.")



