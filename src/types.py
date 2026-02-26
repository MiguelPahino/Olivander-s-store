class OllivanderShop():

    def __init__(self,items):
        self.items = items

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()
    
class Interfaz():
    def updateQuality(self):
        pass


class Item:
    def __init__(self, name, quality, sellIn):
        self.name = name
        self.quality= quality
        self.sellIn = sellIn
    
    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self,quality):
        self._quality = max(0,min(50,quality))


        
class NormalItem(Interfaz,Item):
    def setSellIn(self):
        self.sellIn -= 1

    def setQuality(self,quantity):
        self.quality -= quantity
        
    def updateQuality(self):
        self.setSellIn()
        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        

        
class Sulfuras(Interfaz):
    def __init__(self):
        self.name = "Sulfuras"
        self.quality = 80
        self.sellIn = 0

class Conjured(NormalItem):
    pass

class Backstage(NormalItem):
    pass
class AgedBrie(NormalItem):
    def updateQuality(self):
        self.setSellIn(1)
        self.setQualityQuality(-1)
    

if __name__ == "__main__":

    elixir = NormalItem("elixir",60,20)
    print(elixir.quality)