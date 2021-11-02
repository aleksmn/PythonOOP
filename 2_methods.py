class Customer:

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        # Custom functionality
        print("changing membership, calculating costs...")
        self.membership_type = new_membership

    def __str__(self):
        return f"Customer: {self.name}; membership: {self.membership_type}."

    def __repr__(self):
        return self.name

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


# Create list of customers

customers = [Customer("Caleb", "Gold"), 
             Customer("Brad", "Bronze"),
             Customer("John", "Silver")]


# Update 
customers[1].update_membership("Gold")
print(customers[1].name, customers[1].membership_type)

# Print object with __str__ method
print(customers[0])

# Print with __repr__ method
print(customers)

# Print All
Customer.print_all_customers(customers)

# Check equality

customers = [Customer("Caleb", "Gold"), 
             Customer("Caleb", "Bronze")]

print(customers[0] == customers[1])