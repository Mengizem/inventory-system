
import json

# Creating Dictionary to store data
products = {101: {"name": "item1", "unit_unit_price": 230, "quantity_on_hand": 10},
                      102: {"name": "item2", "unit_price": 250, "quantity_on_hand": 100},
                      103: {"name": "item3", "unit_price": 500, "quantity_on_hand": 200},
                      104: {"name": "item4", "unit_price": 20, "quantity_on_hand": 50},
                      105: {"name": "item5", "unit_price": 700, "quantity_on_hand": 100},
                      106: {"name": "item6", "unit_price": 33, "quantity_on_hand": 56},
                      107: {"name": "item7", "unit_price": 765, "quantity_on_hand": 70},
                      108: {"name": "item8", "unit_price": 764, "quantity_on_hand": 90},
                      109: {"name": "item9", "unit_price": 87, "quantity_on_hand": 50},
                      110: {"name": "item10", "unit_price": 24, "quantity_on_hand": 60},
                      }

js = json.dumps(products)
inventoryItemFile = open("inventory.json", 'w')
inventoryItemFile.truncate(0)
inventoryItemFile.write(js)
inventoryItemFile.close()