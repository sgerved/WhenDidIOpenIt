import Item
from datetime import date

def main():
    print("Main")
    Item.createTables()
    owner_steff = Item.Owner(name='Steffen')
    owner_steff.save()
    item = Item.Item(owner=owner_steff, name='Mælk', date=date(2016, 9, 25))
    item.save()
    item2 = Item.Item(owner=owner_steff, name='Ost', date=date(2016, 9, 25))
    item2.save()

if __name__ == "__main__": main()