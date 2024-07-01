class Item:
  def __init__(self, name, desc, power, maxheart, luck, luckmax, luckmin, type):
    self.name = name
    self.desc = desc
    self.power = power
    self.maxheart = maxheart
    self.luck = luck
    self.luckmax = luckmax
    self.luckmin = luckmin
    self.type = type

item1 = Item("Rusty Knife", "Increases power by 25.", 25, 0, 0, 0, 0, "weapon")
item2 = Item("Four Leaf Clover", "Increases luck by 5.", 0, 0, 5, 0, 0, "gear")

item3 = Item("Stuffed Toy","Increases power by 30.", 30, 0, 0, 0, 0, "weapon") #1
item4 = Item("Comet Hammer","Increases power by 50.", 50, 0, 0, 0, 0, "weapon") #3
item5 = Item("Rubber Ball","Increases power by 20 and luck by 4.", 20, 0, 4, 0, 0, "weapon") #1
item6 = Item("Meteor Ball","Increases power by 40 and luck by 8.", 40, 0, 8, 0, 0, "weapon") #3
item7 = Item("Spatula","Increases power by 15 and heart by 20.", 15, 20, 0, 0, 0, "weapon") #2
item8 = Item("Baking Pan","Increases power by 30 and heart by 40.", 30, 40, 0, 0, 0, "weapon") #4
item9 = Item("LOL Sword","Increases power by 45 and heart by 15 but reduces luck by 6.", 45, 15, -6, 0, 0, "weapon") #2
item10 = Item("Red Knife","Increases power by 70 but reduces heart by 20", 70, -20, 0, 0, 0, "weapon") #4

item11 = Item("Back Pack", "Increases power and heart by 5 and luck by 3", 5, 5, 3, 0, 0, "gear") #1
item12 = Item("Wish Bone", "Increases luck by 6", 0, 0, 6, 0, 0,"gear") #1
item13 = Item("Rake", "Increases enemy spawns but increases power and heart by 30", 30, 30, 0, 0, -10, "gear") #3
item14 = Item("Contract","Decreases heart by 50 but increases power by 70", -50, 70, 0, 0, 0, "gear") #4
item15 = Item("Chimera Key Chain", "Increases luck by 20 but decreases power and heart by 20", -20, -20, 20, 0, 0, "gear") #4
item16 = Item("Cool Glasses", "Halves enemy spawns but also halves key spawns", 0, 0,0,-3,15,"gear") #2
item17 = Item("Bread Phones","Increases heart by 20", 0, 20, 0, 0, 0, "gear") #2
item18 = Item("Hector JR","Increases power by 20 and heart by 20 and increases luck by 8", 20, 20, 8, 0, 0, "gear") #3