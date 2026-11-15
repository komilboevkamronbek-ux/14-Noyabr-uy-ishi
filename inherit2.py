#                     1-bo'lim
#                     1-masala
class User:
    def __init__(self, name, email, address):
        self.ism = name
        self.email = email
        self.address = address
        
    def get_name(self) -> str:
        return self.ism
    
    def get_email(self) -> str:
        return self.email
    
    def get_address(self) -> str:
        return self.address
    
    def set_address(self, new_address: str):
        if not isinstance(new_address, str) or not new_address.strip():
            raise ValueError("Manzil bo'sh bo'lmagan matn bo'lishi kerak")
        self.address = new_address
        
    def __str__(self) -> str:
        return f"User: {self.ism} <{self.email}>"
    
class Customer(User):
    def __init__(self, name, email, address,balance = 0):
        super().__init__(name,email,address)
        self.cart = []
        self.balans = balance
        
    def add_to_cart(self, product, qty, price):
        if qty > 0 and price >= 0:
            self.cart.append((product, qty, price))
            
    def clear_cart(self):
        self.cart.clear()
        
    def get_cart_total(self):
        return sum(qty*price for i, qty, price in self.cart)
            
    def checkout(self):
        total = self.get_cart_total()
        if self.balans >= total:
            self.balans -= total
            self.clear_cart()
            return True
        return False
    
    def __str__(self):
        return f"Costumer: {self.ism} (balance: {self.balans}) so'm"

class Seller(User):
    def __init__(self, name, email, address, rating = 0.0):
        super().__init__(name, email, address)
        self.products = {}
        self.rating = rating
        
    def add_product(self, name, qty):
        if qty>0:
            self.products[name] = self.products.get(name, 0) + qty
            
    def remove_product(self, name, qty):
        if name in self.products:
            del self.products[name]
            return True
        return False
    
    def update_stock(self, name, delta_qty):
        if name not in self.products:
            return False
        new_qty = self.products[name] + delta_qty
        if new_qty < 0:
            return False
        self.products[name] = new_qty
        return True
    
    def get_stock(self):
        return self.products.copy()
    
    def __str__(self):
        items = sum(self.products.values())
        return f"Seller: {self.get_name()} (Rating: {self.rating}, items: {items})"
    
c = Customer("Ali", "ali@mail.com", "Toshkent", balance=2_000_000)
c.add_to_cart("Keyboard", 1, 300_000)
c.add_to_cart("Mouse", 2, 150_000)
print(c.get_cart_total())     # 600000
print(c.checkout())           # True
print(c)                      # Customer: Ali (balance: 1400000 so‘m)

s = Seller("Gulbahor", "g@mail.com", "Samarqand", rating=4.8)
s.add_product("Keyboard", 10)
s.update_stock("Keyboard", -3)
print(s.get_stock())          # {'Keyboard': 7}
print(s)                      # Seller: Gulbahor (rating: 4.8, items: 7)
