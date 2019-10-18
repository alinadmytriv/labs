from math import pi

# --------------------------------------------------------------------------------------------
# SRP - Single Responsibility Principle
class Customer:
    """
    Create a customer.
    """
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

class GetCustomer(Customer):
    """
    Get details about the customer.
    """
    def get_name(self):
        return self.name

    def get_mobile(self):
        return self.mobile

def customers():
    """
    the function which create a customer &
    output his name and mobiles
    """
    c1 = Customer("Katya", "0678543289")
    db1 = GetCustomer(c1.name, c1.mobile)
    print(db1.get_name() + " " + db1.get_mobile())

# --------------------------------------------------------------------------------------------
# OCP - Open-Closed Principle
class Discount:
    """
    create a discount for customer
    """
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_customer(self):
        return self.customer

    def get_discount(self):
        return self.price * 0.2

class VIPcustomer(Discount):
    """
    to extend the method get_discount() from class Discount
    for VIP-customer to increase the discount by 2 times
    """
    def get_discount(self):
        return super().get_discount() * 2

def discounts():
    """
    the function which create a vip-customer &
    output this customer and his discount
    """
    d1 = VIPcustomer("customer2", 1000)
    print(d1.get_customer() + " - " + str(d1.get_discount()))

# --------------------------------------------------------------------------------------------
# LSP - Liskov Substitution Principle
class Plants:
    """
    create a plant
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Flowerpot(Plants):
    """
    methods for houseplants - volume of their pots
    """
    def rectangular_pot_shape(self, width, length, height):
        return width*length*height

    def round_pot_shape(self, height, radius):
        return pi*(radius**2)*height

class CultivatedPlants(Plants):
    """
    methods for cultivated plants - volume of their pit
    """
    def pit_shape(self, radius, height):
        return pi*(radius**2)*height

def plants():
    """
    the function which create the plants
    and find for them the shape of their pot/pits
    """
    f1 = Flowerpot("violet")
    f2 = CultivatedPlants("bush")
    print("Name - " + str(f1.name) + " Shape of the pot - " + str(f1.rectangular_pot_shape(2, 3, 4)))
    print("Name - " + str(f2.name) + " Shape of the pit - " + str(f2.pit_shape(2, 3)))


# --------------------------------------------------------------------------------------------
# ISP - Interface Segregation Principle
class Shape:
    """
    class that has the method - draw() for all different shapes
    """
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    """
    use the super method and draw only shape of circle
    """
    def draw(self):
        print("Draw circle")

class Square(Shape):
    """
    use the super method and draw only shape of square
    """
    def draw(self):
        print("Draw square")

def shapes():
    """
    create different shapes
    output their method - draw()
    """
    sh1 = Circle()
    sh2 = Square()
    sh1.draw()
    sh2.draw()

# the function which calls functions which show the soli(d) principles
if __name__ == '__main__':
    customers() # SRP
    discounts() # OCP
    plants() # LSP
    shapes() # ISP
