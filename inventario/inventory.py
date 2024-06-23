import csv

class Inventory:
    def __init__(self, filename="inventory.csv"):
        self.filename = filename
        self.inventory = {}
        self.load_inventory()

    def add_product(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
        self.save_inventory()

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            self.save_inventory()

    def modify_quantity(self, name, new_quantity):
        if name in self.inventory:
            self.inventory[name] = new_quantity
            self.save_inventory()

    def get_inventory(self):
        return self.inventory

    def save_inventory(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, quantity in self.inventory.items():
                writer.writerow([name, quantity])

    def load_inventory(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, quantity = row
                    self.inventory[name] = int(quantity)
        except FileNotFoundError:
            # Handle case where file doesn't exist yet (e.g., on first run)
            pass

    def split_inventory(self):
        above_five = []
        below_five = []
        for name, quantity in self.inventory.items():
            if quantity >= 5:
                above_five.append((name, quantity))
            else:
                below_five.append((name, quantity))
        return above_five, below_five
