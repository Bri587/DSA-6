 
# CHAPTER 6 EXERCISE 2

class InventoryHashTable:
    """
    Custom hash table for product inventory.

    """

    def __init__(self, size=10):
        self.size = size
        # create list of empty buckets
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Hash function:
        Sum ASCII codes of characters
        Then modulo by table size
        """
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def set_item(self, sku, name, quantity):
        """
        Add new product or update existing product
        """
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                item["name"] = name
                item["quantity"] = quantity
                return

        # if not found, append new product
        bucket.append({
            "sku": sku,
            "name": name,
            "quantity": quantity
        })

    def get_item(self, sku):
        """
        Return product dict if found, else None
        """
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                return item

        return None

    def remove_item(self, sku):
        """
        Remove product by SKU
        """
        index = self._hash(sku)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item["sku"] == sku:
                del bucket[i]
                return True

        return False

    def print_table(self):
        """
        Print hash table contents
        """
        print("\n=== Inventory Hash Table ===")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# FOR TESTING

inv = InventoryHashTable(size=7)

inv.set_item("A101", "USB Cable", 25)
inv.set_item("B205", "Keyboard", 12)
inv.set_item("C333", "Mouse", 18)
inv.set_item("A101", "USB Cable", 30)  # update existing item

inv.print_table()

print("Search B205:", inv.get_item("B205"))

print("Remove C333:", inv.remove_item("C333"))

inv.print_table()