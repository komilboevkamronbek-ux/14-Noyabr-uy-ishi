#                     1-bo'lim
#                     1-masala
# class User:
#     def __init__(self, name, email, address):
#         self.ism = name
#         self.email = email
#         self.address = address
        
#     def get_name(self) -> str:
#         return self.ism
    
#     def get_email(self) -> str:
#         return self.email
    
#     def get_address(self) -> str:
#         return self.address
    
#     def set_address(self, new_address: str):
#         if not isinstance(new_address, str) or not new_address.strip():
#             raise ValueError("Manzil bo'sh bo'lmagan matn bo'lishi kerak")
#         self.address = new_address
        
#     def __str__(self) -> str:
#         return f"User: {self.ism} <{self.email}>"
    
# class Customer(User):
#     def __init__(self, name, email, address,balance = 0):
#         super().__init__(name,email,address)
#         self.cart = []
#         self.balans = balance
        
#     def add_to_cart(self, product, qty, price):
#         if qty > 0 and price >= 0:
#             self.cart.append((product, qty, price))
            
#     def clear_cart(self):
#         self.cart.clear()
        
#     def get_cart_total(self):
#         return sum(qty*price for i, qty, price in self.cart)
            
#     def checkout(self):
#         total = self.get_cart_total()
#         if self.balans >= total:
#             self.balans -= total
#             self.clear_cart()
#             return True
#         return False
    
#     def __str__(self):
#         return f"Costumer: {self.ism} (balance: {self.balans}) so'm"

# class Seller(User):
#     def __init__(self, name, email, address, rating = 0.0):
#         super().__init__(name, email, address)
#         self.products = {}
#         self.rating = rating
        
#     def add_product(self, name, qty):
#         if qty>0:
#             self.products[name] = self.products.get(name, 0) + qty
            
#     def remove_product(self, name, qty):
#         if name in self.products:
#             del self.products[name]
#             return True
#         return False
    
#     def update_stock(self, name, delta_qty):
#         if name not in self.products:
#             return False
#         new_qty = self.products[name] + delta_qty
#         if new_qty < 0:
#             return False
#         self.products[name] = new_qty
#         return True
    
#     def get_stock(self):
#         return self.products.copy()
    
#     def __str__(self):
#         items = sum(self.products.values())
#         return f"Seller: {self.get_name()} (Rating: {self.rating}, items: {items})"
    
# c = Customer("Ali", "ali@mail.com", "Toshkent", balance=2_000_000)
# c.add_to_cart("Keyboard", 1, 300_000)
# c.add_to_cart("Mouse", 2, 150_000)
# print(c.get_cart_total())     # 600000
# print(c.checkout())           # True
# print(c)                      # Customer: Ali (balance: 1400000 so‘m)

# s = Seller("Gulbahor", "g@mail.com", "Samarqand", rating=4.8)
# s.add_product("Keyboard", 10)
# s.update_stock("Keyboard", -3)
# print(s.get_stock())          # {'Keyboard': 7}
# print(s)                      # Seller: Gulbahor (rating: 4.8, items: 7)

#                    2-masala

# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number
        
#     def get_name(self):
#         return self.name
    
#     def get_id(self):
#         return self.id_number
    
#     def __str__(self):
#         return f"Person: {self.name} (#{self.id_number})"
    
# class Patient(Person):
#     def __init__(self, name, id_number):
#         super().__init__(name, id_number)
#         self.diagnoses = []
#         self.bill = 0
        
#     def add_diagnosis(self, text:str):
#         self.diagnoses.append(text)
    
#     def add_charge(self, amount: int):
#         if amount <= 0:
#             raise ValueError("Summa musbat bo'lishi kerak")
#         self.bill += amount
    
#     def pay(self, amount: int):
#         if amount <= 0:
#             return False
#         if amount >= self.bill:
#             self.bill = 0
#         else:
#             self.bill -= amount
#         return True
    
#     def get_balance(self):
#         return self.bill
    
#     def print_history(self):
#         print(f"Bemor: {self.name} (#{self.id_number})")
#         print("Tashxislar tarixi:")
#         for i, r in enumerate(self.diagnoses, start=1):
#             print(f" {i} {r}")
#         print(f"Qarzdorlik: {self.bill}")
        
# class Doctor(Person):
#     def __init__(self, name, id_number, specialty):
#         super().__init__(name, id_number)
#         self.schedule = {}
#         self.specialty = specialty
        
#     def add_slot(self, day:str,time:str):
#         slots = self.schedule.setdefault(day,[])
#         if time not in slots:
#             slots.append(time)
            
#     def book_slot(self, day:str, time:str):
#         if time in self.schedule.get(day,[]):
#             self.schedule[day].remove(time)
#             return True
#         return False
            
#     def available_slots(self, day:str):
#         return self.schedule.get(day,[]).copy()
    
#     def __str__(self):
#         return f"Dr.name: {self.name}({self.specialty})"   
        
# p = Patient("Aziz", "AB1234567")
# p.add_diagnosis("ORVI")
# p.add_charge(150_000)
# p.add_charge(80_000)
# print(p.get_balance())  # 230000
# p.pay(100_000)
# print(p.get_balance())  # 130000
# p.print_history()

# d = Doctor("Gulrux", "CD7654321", specialty="Cardiologist")
# d.add_slot("Mon", "09:00")
# d.add_slot("Mon", "09:30")
# print(d.book_slot("Mon", "09:00"))  # True
# print(d.book_slot("Mon", "09:00"))  # False
# print(d.available_slots("Mon"))     # ["09:30"]
# print(d) # Dr.Gulrux (Cardiologist)
         
#                    3-masala
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
        
    def get_title(self):
        return self.title
    
    def get_teacher(self):
        return self.teacher
    
    def enroll(self, student_name:str):
        if student_name not in self.students:
            self.students.append(student_name)
            return True
        return False    
    
    def drop(self, student_name:str):
        if student_name in self.students:
            self.students.remove(student_name)
            return True
        return False
    
    def __str__(self):
        return f"Course: {self.title} ({self.teacher})"
    
class OnlineCourse(Course):
    def __init__(self, title, teacher, url, max_students):
        super().__init__(title, teacher)
        self.url = url
        self.max_students = max_students
    
    def enroll(self, student_name:str):
        if len(self.students) >= self.max_students:
            return False
        return super().enroll(student_name)
    
    def get_room(self):
        return f"Virtual: {self.url}"
    
class OfflineCourse(Course):
    def __init__(self, title, teacher, room, capacity):
        super().__init__(title, teacher)
        self.room = room
        self.capacity = capacity
        
    def enroll(self, student_name: str):
        if len(self.students) >= self.capacity:
            return False
        return super().enroll(student_name)
    
    def get_room(self):
        return f"Room: {self.room}"
        
o = OnlineCourse("Python Basics", "Guzal", url="https://nt.uz/py", max_students=2)
print(o.enroll("Ali"))      # True
print(o.enroll("Vali"))     # True
print(o.enroll("Karim"))    # False (to‘ldi)
print(o.get_room())         # Virtual: https://nt.uz/py

f = OfflineCourse("Algorithms", "Dilshod", room="B-203", capacity=1)
print(f.enroll("Soliha"))   # True
print(f.enroll("Nodir"))    # False
print(f.get_room())         # Room: B-203
print(f)
