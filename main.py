from src.types import OllivanderShop, NormalItem, Sulfuras, Conjured, Backstage

items = [
    NormalItem("Iron Sword", 10, 30),
    NormalItem("Leather Armor", 5, 20),
    Sulfuras(),
    Conjured("Conjured Mana Cake", 3, 6),
    Backstage("Backstage pass to a TAFKAL80ETC concert", 15, 20),
]

shop = OllivanderShop()

for item in items:
    shop.addItem(item)

shop.nextDay()
