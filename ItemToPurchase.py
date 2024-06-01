class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.item_total = float(f'{(self.item_price * self.item_quantity):2f}')
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}")

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item) # Adds item name to cart items

    def remove_item(self, item_name):
        removed = False
        print("Trying to remove:", item_name)  # Debugging statement
        for item in self.cart_items[:]:  # Iterate over a copy of the list
            print("Item in cart:", item.item_name)  # Debugging statement
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f'{item_name} removed from cart.')
                removed = True
                break
        if not removed:
            print('\nItem not found in cart. Nothing removed.\n')

    def modify_item(self, ItemToPurchase):
        for cart_item in self.cart_items: # For every cart item in the list
            if cart_item == ItemToPurchase.item_name: # If a cart item name is also a name in ItemToPurchase
                if ItemToPurchase.item_price != 0.0:
                    cart_item.item_price = ItemToPurchase.item_price # Modifies item price
                if ItemToPurchase.item_quantity != 0.0:
                    cart_item.item_quantity = ItemToPurchase.item_quantity # Modifies item quantity
                if ItemToPurchase.item_description != '':
                    cart_item.item_description = ItemToPurchase.item_description # Modifies item description
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
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items:', self.get_num_items_in_cart())
            for item in self.cart_items:
                print('{n} {q} @ ${p:.2f} = ${t:.2f}'.format(n = item.item_name, p = item.item_price, q = item.item_quantity, t = item.item_total))
            print(f'Total: ${self.get_cost_of_cart():.2f}')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            print('{n}: {d}'.format(n = item.item_name, d = item.item_description))

def print_menu(ShoppingCart):
    selection = ''

    while selection != 'q':
        print('\nMENU\n')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        selection = input('\nChoose an option: \n')
        if selection == 'a':
            # Get input for item information from user
            name = input('Item name: \n')
            price = float(input('Item price: \n'))
            quantity = int(input('Item quantity: \n'))
            description = input('Item description: \n')

            item = ItemToPurchase(name, price, quantity, description)  # Creates ItemToPurchase with input info
            ShoppingCart.add_item(item)
        if selection == 'r':
            item = input('Item name: \n')
            ShoppingCart.remove_item(item)
        if selection == 'c':
            item = input('Item name: \n')
            for cart_item in self.cart_items:  # For every cart item in the list
                if cart_item == item.item_name:  # If a cart item name is also a name in ItemToPurchase
                    if item.item_quantity != 0.0:
                        new_quantity = int(input('Enter new quantity: '))
                        cart_item.item_quantity = new_quantity  # Modifies item quantity
                    break
                else:
                    print('Item not found in cart. Nothing modified.')
        if selection == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_descriptions()
        if selection == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()
        else:
            print('Please enter a valid menu option')

####

# Get customer input for name and date
name = input('Customer name: ')
date = input('Current date: ')

ShoppingCart = ShoppingCart(name, date)

print_menu(ShoppingCart)