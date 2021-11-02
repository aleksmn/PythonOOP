class Customer:

    # Constructor
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

# Create customer      

c = Customer("Caleb", "Gold")
print(f"Customer {c.name} created. Membership: {c.membership_type}.")


# Create list of customers

customers = [Customer("Caleb", "Gold"), 
             Customer("Brad", "Bronze")]

print(customers[1].name, customers[1].membership_type)