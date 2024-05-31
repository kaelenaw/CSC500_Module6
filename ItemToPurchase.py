class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    def print_item_cost(self):
        self.item_total = float(f'{(self.item_price * self.item_quantity):2f}')
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}")

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self,item):
        if item in self.cart_items:
            self.cart_items.remove(item)
        else:
            print('\nItem not found in cart. Nothing removed.\n')

    def modify_item(self, ItemToPurchase):
        for cart_item in self.cart_items:
            if cart_item == self.item_name:
                if ItemToPurchase.item_price != 0.0:
                    cart_item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0.0:
                    cart_item.item_quantity = ItemToPurchase.item_quantity
                break
            else:
                print('Item not found in cart. Nothing modified.')
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print('{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items:', self.get_num_items_in_cart)
            for item in self.cart_items:
                print('{n} {q} @ ${p:.2f} = {t:.2f}\n'.format(n = item.item_name, p = item.item_price, q = item.item_quantity, t = item.item_total))
            print(self.get_cost_of_cart)

    def print_descriptions(self):
        print('{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        print('Item Descriptions')
        for item in self.cart_items:
            print('{n}: {d}\n'.format(n = item.item_name, d = item.item_description))

# Get user input for item1 information
print('Item 1\n')
item1_name = input('Item name: \n')
item1_price = float(input('Item price: \n'))
item1_quantity = int(input('Item quantity: \n'))

# creates item1 from inputs
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
item1.print_item_cost()

# Get user input for item2 information
print('\nItem 2\n')
item2_name = input('Item name: \n')
item2_price = float(input('Item price: \n'))
item2_quantity = int(input('Item quantity: \n'))

# creates item2 from inputs
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
item2.print_item_cost()

# determines bill total
total = item1.item_total + item2.item_total

# prints out item information and costs as receipt
print('\nTOTAL COST')
print('{n} {q} @ ${p:.2f} = {t:.2f}\n'.format(n = item1_name, p = item1_price, q = item1_quantity, t = item1.item_total))
print('{n} {q} @ ${p:.2f} = {t:.2f}\n'.format(n = item2_name, p = item2_price, q = item2_quantity, t = item2.item_total))
print('Total: ${:.2f}'.format(total))
