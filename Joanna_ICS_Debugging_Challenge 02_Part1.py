print ('Hi! Welcome to the Mcdonalds! This is our options to order food!')

choices= {1:['1','Big Mac','4.49', 'No cheese', '2 layer of burgers'],
          2:['2','Small French Fries','1.49','No salt','fried potatoes'],
          3:['3','20 McNuggets','5.69','Spicy Buffalo','Chicken tenders'],
          4:['4','Shake','2.39','chocolate,straberry','icecream'],
          5:['5','Beverages','1.09','Coke,sprite','drinking'],
          6:['6','Hot N spicy McChicken','1.59','No Vegetables','Burgers with Chicken'],
          7:['7','Bacon Quarter Pounder with Cheese','5.39','No cheese','Burgers with beef and Bacon inside'],
          8:['8','southwest salad with crispy chicken','5.29','No dressing','Chicken and vegetables salad'],
          9:['9','Fruit & Yoguart Parfait','1.39','Yoguart with fresh fruits inside'],}

order={'ID':['Menu Item Name','Price','Modifications','short description']}

def show_menu():
    print('{:^11s}{:^30s}{:^5s}{:^20s}{:^40s}'.format('Menu Item #', 'Menu Item Name','Price', 'Modifications', 'Short Description'))
    print('-' * 100)
    for i in range (1,9):
        print('{:^11s}{:^30s}{:^5s}{:^20s}{:^40s}'.format(choices[i][0], choices[i][1], str(choices[i][2]), choices[i][3].replace('+', '').replace('-',''),choices[i][4]))
        print('-' * 100)
    print('Which food you want to order today! " ')
show_menu ()


import time

items_dict = {
    "Company_name": "Mcdonalds",
    "Local_Tax": "9.5",
    "Menu_items": [
        {
            "Menu_item_name": "Big Mac",
            "Price": "4.49",
            "Modifications": ["No Diced onions", "No Cheese"],
            "Short_description": "2 layers of burgers"
        },
        {
            "Menu_item_name": "Small French Fries",
            "Price": "1",
            "Modifications": ["No Salt"],
            "Short_description": "fries"
        },
        {
            "Menu_item_name": "20 McNuggets",
            "Price": "5.69",
            "Modifications": ["Honey Packet", "Ketchup Packet", "Spicy Buffalo"],
            "Short_description": "Chicken tenders"
        },
        {
            "Menu_item_name": "Shake",
            "Price": "2.39",
            "Modifications": ["Chocolate shake", "Straberry shake"],
            "Short_description": "like Ice cream"
        },
        {
            "Menu_item_name": "Beverages",
            "Price": "1.09",
            "Modifications": ["Coke", "Diet coke", "Sprite"],
            "Short_description": "all kinds of drinks"
        },
        {
            "Menu_item_name": "Hot N spicy McChicken",
            "Price": "1.59",
            "Modifications": ["No vegetables"],
            "Short_description": "Burgers with chicken"
        },
        {
            "Menu_item_name": "Bacon Quarter Pounder with Cheese",
            "Price": "5.39",
            "Modifications": ["No Cheese", "No Diced Onions"],
            "Short_description": "Burgers with beef and Bacon inside"
        },
        {
            "Menu_item_name": "Southwest Salad with crispy chicken",
            "Price": "5.29",
            "Modifications": ["No Dressing", "Ranch", "French Dressing"],
            "Short_description": "salad with vegetables, chicken"
        },
        {
            "Menu_item_name": "Fruit & Yoguart Parfait",
            "Price": "1.39",
            "Modifications": ['No sugars'],
            "Short_description": "Yoguart with fresh fruits inside"
        }]}


def print_order_item(dict_input):

    print("We have these items, please choose some items...")
    print("{:<3s}{}".format("No.", "Name"))
    items_name_list = []
    if "Menu_items" in dict_input:
        for idx, item in enumerate(dict_input["Menu_items"]):
            print("{:<3d}{}".format(idx + 1, item["Menu_item_name"]))


def print_current_order(orders):
    s1 = '---{:*^20s}----'.format('Your Orders :)')
    print(s1)
    print("{}, {}, {}, {}".format("No.", "Name", "Price", "Count"))
    for i in orders:
        print("{}, {}, {}, {}, {}".format(i, orders[i]['name'], orders[i]['price'], orders[i]['count'],
                                          orders[i]['modifications']))
    s1 = '---{:*^20s}----\n'.format('End')


if __name__ == '__main__':
    print_order_item(items_dict)
    orders = {}
    while True:
        print("Please input the operation you want to get:"
              "\n\t 1. add a item to the orders"
              "\n\t 2. delete a item from the orders"
              "\n\t 3. modify a item to the orders"
              "\n\t 4. ready to pay"
              "\n\t 5. restart"
              "\n\t 6. exit")
        choice = input("choice:")
        if choice == "1":
            nos = input("Please input the No. you want to order: ")
            no_count = input("Please input the count you want to order: ")

            name = items_dict["Menu_items"][int(nos) - 1]["Menu_item_name"]
            price = items_dict["Menu_items"][int(nos) - 1]["Price"]
            modifications = items_dict["Menu_items"][int(nos) - 1]["Modifications"]
            print("the type for the item you can choose are in below: ")
            print("{}   {}".format("No", "Type"))
            for nn, ite in enumerate(modifications):
                print("{}   {}".format(nn + 1, ite))
            modi_ch = input("Please choose a type for this item: ")

            if nos not in orders:
                orders[nos] = {}
            orders[nos]['name'] = name
            orders[nos]['count'] = int(no_count)
            orders[nos]['price'] = price
            orders[nos]['modifications'] = modifications[int(modi_ch) - 1]
            print_current_order(orders)
        elif choice == "2":
            nos = input("Please input the No. you want to remove: ")
            if nos in orders:
                del orders[nos]
            else:
                print("No item in the orders list")
            print_current_order(orders)
        elif choice == "3":
            nos = input("Please input the No. you want to modify: ")
            if nos in orders:
                new_count = input("Please input the No you want to adjust the quantities: ")
                orders[nos]['count'] = int(new_count)
            else:
                print("No item in the orders list")
            print_current_order(orders)
        elif choice == "4":
            cst = 0
            for i in orders:
                cst += float(orders[i]['price']) * orders[i]['count']
            total_cst = cst * (1 + (items_dict['Local_Tax']) / 100)
            print("The total cost including tax for the order is {} "
                  "\tPlease pay for the Orders. Thank you! ".format(total_cst))
            print_current_order(orders)
        elif choice == '5':
            orders.clear()
        elif choice == '6':
            t = time.time()
            write_content = ""
            write_content += "{}, {}, {}, {}, {}".format("No.", "Name", "Price", "Count", "Modification")
            for i in orders:
                write_content += "\n"
                write_content += "{}, {}, {}, {}, {}".format(i, orders[i]['name'], orders[i]['price'],
                                                             orders[i]['count'], orders[i]['modifications'])


            print("Your orders are all set!")
            print("Thank you for ordering today! Wish to see you next time:)")
            break
        else:
            print("Please input the valid choice!!!")