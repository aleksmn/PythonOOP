class User:
    def log(self):
        print(self)

class Customer(User):

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        print("changing membership, calculating costs...")
        self.membership_type = new_membership

    def __str__(self):
        return f"Customer: {self.name}; membership: {self.membership_type}."

    def __repr__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

customers = [Customer("Caleb", "Gold"), 
             Customer("Brad", "Bronze"),
             Customer("John", "Silver")]

customers[0].log()
