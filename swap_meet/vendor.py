class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            return new_item
        return False
    
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, their_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in their_vendor.inventory:
            self.add(their_item)
            their_vendor.add(my_item)
            self.remove(my_item)
            their_vendor.remove(their_item)
            return True
        return False