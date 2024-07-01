import random
import os
import items
import asciiart

itemlist1 = [items.item3, items.item5, items.item11, items.item12]
itemlist2 = [items.item7, items.item9, items.item16, items.item17]
itemlist3 = [items.item4, items.item6, items.item16, items.item18]
itemlist4 = [items.item8, items.item10, items.item14,items.item15]  

dinodollars = 0
c = 1
luckmin = 0
luckmax = 100
luckbonus = 0
power = 100
maxheart = 100
gearequiped = [items.item2]
weaponequiped = [items.item1]
key = 0

spoonlist = ["potato spoon"]
foodlist = ["Go back"]
foodstats = [0]
weaponlist =[]
gearlist = []

def shop(shopmoney):
  x = 0
  y = 0
  global key
  print("===============================")
  print("Welcome to the Dino Shop!")
  print("===============================")
  print("[ 1 ] Plastic spoon - 6 dino dollars - 10 digs")
  print("[ 2 ] Wooden spoon - 12 dino dollars - 15 digs")
  print("[ 3 ] Silver spoon - 20 dino dollars - 20 digs")
  print("[ 4 ] Gold spoon - 35 dino dollars - 25 digs")
  print("[ 5 ] Dreamer's spoon - 40 dino dollars - 30 digs")
  print("[ 6 ] Pyramid Key - 5 dino dollars (WILL BE LOST AT END OF RUN)")
  print("[ 7 ] go back")
  print("")
  print("You have:",shopmoney, "dino dollars.")
  print("")
  print("What would you like to buy?")
  x = (input("> "))
  if x == "1":
    if shopmoney >= 6:
      y = 6
      spoonlist.append("plastic spoon")
    else: 
      print("Not enough money")
      input("> ")
  elif x == "2":
    if shopmoney >= 12:
      y = 12
      spoonlist.append("wooden spoon")
    else:
      print("Not enough money")
      input("> ")
  elif x == "3":
    if shopmoney >= 20:
      y = 20
      spoonlist.append("silver spoon")
    else:
      print("Not enough money")
      input("> ")
  elif x == "4":
    if shopmoney >= 35:
      y = 35
      spoonlist.append("gold spoon")
    else:
      print("Not enough money")
      input("> ")
  elif x == "5":
    if shopmoney >= 40:
      y = 40
      spoonlist.append("dreamer's spoon")
    else:
      print("Not enough money")
      input("> ")
  elif x == "6":
    if shopmoney >= 5:
      key = key + 1
      y = 5
    else:
      print("Not enough money")
      input("> ")
  else:
    y = 0
  shopmoney = shopmoney - y
  clearConsole()
  return shopmoney, key

def spoon(spoontype):
  print("Select your spoon:")
  print("")
  spoonlen = len(spoontype)
  y = 0
  while y < spoonlen:
    print("[",y + 1,"]",spoontype[0+y])
    y = y + 1
  spoonequip = 0
  try:
    spoonequip = int(input("> "))
  except (NameError, SyntaxError, ValueError, IndexError):
    print("I'll just assume that means you want a potato spoon!")
    input("> ")
    clearConsole()
    return "potato spoon"
  if spoonequip > spoonlen:
    print("I'll just assume that means you want a potato spoon!")
    input("> ")
    clearConsole()
    return "potato spoon"
  spoonidx = spoonequip - 1
  spoon = spoonlist[spoonequip-1]
  if spoonidx >= 1:
    spoonlist.pop(spoonidx)
  clearConsole()
  return spoon

def luckfun(luckmin,luckmax,luckbonus):
  uniluck = 0
  uniluck = random.randint(luckmin,luckmax)
  #print(uniluck)
  uniluck = uniluck + luckbonus
  #print(unil)
  return uniluck

def dig(spoon,luckmin,luckmax,luckbonus,power,maxheart):
  print("You have arrived at floor: 1")
  print("Welcome to the GRAINS section")
  heart = maxheart
  dinosfound = 0
  global key
  luckydino = 0
  if spoon == "potato spoon":
    digs = 5
  elif spoon == "plastic spoon":
    digs = 10
  elif spoon == "wooden spoon":
    digs = 15
  elif spoon == "silver spoon":
    digs = 20
  elif spoon == "gold spoon":
    digs = 25
  elif spoon == "dreamer's spoon":
    digs = 30
  floor = 1
  print("[1] to use a pyramid key")
  print("[2] to dig")
  print("[3] to end the dig")
  print("[4] to use food")
  while digs > 0:
    x = input("Dig?: ")
    if x == "1":
      if key >= 1:
        key = key - 1
        floor = floor + 1
        luckydino = luckydino + 2
        print("You have arived at floor:", floor)
        if floor == 2:
          print("Welcome to the FRUITS and VEGTABLES section")
        elif floor == 3:
          print("Welcome to the MEAT section")
        elif floor == 4:
          print("Welcome to the SUGAR section")
        else:
          print("Are you ready to fight the final boss?")
          print("[1] Yes")
          print("[2] No")
          answer = input("> ")
          if answer == "1":
            print("You have entered the last room of the pyramid")
            print("(???) - You think you can beat us?")
            input("> ")
            print("(???) - Minions attack!")
            input(">")
            heart = battle(power,5,heart)
            if heart > 0:
              print("(???) - You beat them?")
              input("> ")
              print("(UNBREADTWINS) - NOW FIGHT US!!!")
              input("> ")
              heart = battle(power,6,heart)
              if heart > 0:
                dinosfound = dinosfound + 10
                print("(UNBREADTWINS) - How could you beat us?!?!")
                input("> ")
                print("UNBREADTWINS grow sad")
                print(" You got 10 dinodollars!")
                input("> ")
                print(asciiart.milkshakebunny)
                print("YOU WIN!!!!!")
                print("Congrats!")
                input("> ")
                return dinosfound
              else:
                print("You lost",dinosfound,"dinodollars!")
                print("UNBREADTWINS - Pathetic. ")
                input("> ")
                clearConsole()
                return 0
            else:
              print("You lost",dinosfound,"dinodollars!")
              print("(BREADBROS) - We won?!?")
              input("> ")
              clearConsole()
              return 0
          else:
            key = 1
      else:
        print("You don't have a pyramid key")
    elif x == "2":
      digs = digs - 1
      luck = luckfun(luckmin,luckmax,luckbonus)
      print("=================")
      print("digs left:", digs)
      print("Keys:", key)
      print("=================")
      #print("luck rolled:", luck)
      #print(luckmin,luckmax)
      #print(maxheart, heart)
      if luck >= 95:
        if key == 1:
          itemloot(floor)
        else:
          print("You got a pyramid key!")
          key = 1
      elif luck >= 90:
        itemloot(floor)
      elif luck >= 80:
        foodloot(floor)
      elif luck >= 55 - luckydino:
        print("You found a dino dollar")
        dinosfound = dinosfound + 1
      elif luck <= 30:
        heart = battle(power,floor,heart) 
        if heart <= 0:
          print("You lost",dinosfound,"dinodollars!")
          input("You lose: ")
          clearConsole()
          return 0
        else:
          print("You won and got 1 dino dollar!")
          dinosfound = dinosfound + 1
      else:
        print("You found nothing")
    elif x == "3":
      input("Dig ended!:")
      clearConsole()
      return dinosfound
    elif x == "4":
      heart = foodpick(heart)
      if heart > maxheart:
        heart = maxheart
      print("You have", heart,"heart")
    else:
      print("Please use the correct commands!")
  input("Run done!: ")
  clearConsole()
  return dinosfound

def battle(power,floor,heart):
  global maxheart
  if floor == 1:
    enemylist = ["PORCUPIE","BUN BUNNY","S.S. SNAKE"]
    enemystats =[random.randint(65,75),random.randint(85,105),random.randint(95,110)]
  elif floor == 2:
    enemylist = ["CELERY", "GINGER", "CILANTRO","SPROUT BUNNY"]
    enemystats =[random.randint(100,120),random.randint(140,160),random.randint(190,210),random.randint(230,240)]
  elif floor == 3:
    enemylist = ["RABBIT?","CHICKEN?","ANGRY ORANGE JOE"]
    enemystats =[random.randint(200,220),random.randint(150,170),random.randint(230,240)]
  elif floor == 4:
    enemylist = ["NOTORIOUS CHIP","SWEET POTATO","CUPCAKE BUNNY"]
    enemystats =[random.randint(250,260),random.randint(230,235),random.randint(160,170)]
  elif floor == 5:
    enemylist = ["SLICE, SOURDOUG and SESAME"]
    enemystats = [100]
  else:
    enemylist = ["UNBREADTWINS"]
    enemystats = [300]
  x = len(enemylist) - 1
  enemyindex = random.randint(0,x)
  print("You encountered a", enemylist[enemyindex]+"!")
  print("It has", enemystats[enemyindex],"power.")
  print("You have", power,"power.")
  heart = heart - (enemystats[enemyindex]/power)*50
  heart = int(heart)
  print("You lost", int((enemystats[enemyindex]/power)*50) ,"heart")
  print("You have", heart, "heart")
  return heart

def info(maxheart,power):
  global luckbonus
  global key
  print("=========================================")
  print("Here is everything you need to know!")
  print("=========================================")
  print("")
  print("In the food pyramid there is digging, fighting and much more!")
  print("You can find only one pyramid key at a time.")
  print("You can use a pyramid key to move up to the next floor.")
  print("Each floor has stonger enemies and more loot.")
  print("Battles are fought with power. Heart is lost after battles but can be increased back to the maximum through eating food or ending the dig.")
  print("Power can be increased by equiping items.")
  print("Luck can also be increased by equiping items.")
  print("Staying on a floor after getting a pyramid key increases the chance for items.")
  print("")
  print("You currently have", maxheart,"maximun heart,",luckbonus, "luck and", power,"power.")
  print("")
  print("Food:")
  foodlen = len(foodlist) - 1
  y = 0
  x = 1
  while y < foodlen:
    if foodlen > 0:
      print(foodlist[x],": restores",foodstats[x],"heart")
    else:
      print("None")
    y = y + 1
    x = x + 1
  print("")
  print("Keys:", key)
  print("")
  print("[ 1 ] go back")
  x = input("> ")
  clearConsole()
  
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def foodpick(heart):
  print("You have", heart, "out of",maxheart,"heart.")
  print("What food would you like to use:")
  print("")
  foodlen = len(foodlist)
  y = 0
  while y < foodlen:
    print("[",y + 1,"]",foodlist[0+y],": restores",foodstats[0+y],"heart")
    y = y + 1
  try:
    x = int(input("> "))
  except (NameError, SyntaxError, ValueError, IndexError):
    print("Please use the correct commands!")
    return heart
  if x > foodlen:
    input("Please use the correct commands!")
  elif x > 1:
    heart = heart + foodstats[x-1]
    foodlist.pop(x-1)
    foodstats.pop(x-1)
  return heart

def foodloot(floor):
  if floor == 1:
    foundfood = ["Tofu","Candy","Smores","Bread" ]
    foundfoodstats = [1,5,10,20]
  elif floor == 2:
    foundfood = ["Bread","Tomato","Hot Dog","Non-hostile Celery"]
    foundfoodstats = [20,20,40,30]
  elif floor == 3:
    foundfood = ["Pizza Slice","Cheese Burger","Chocolate","Hot Dog"]
    foundfoodstats = [90,100,60,40]
  else:
    foundfood = ["Donut","Dino Nugs","Sno Cone","Mari's Cookies"]
    foundfoodstats = [60,120,150,500]
  foodindex = random.randint(0,3)
  foodlist.append(foundfood[foodindex])
  foodstats.append(foundfoodstats[foodindex])
  print("You found:",foundfood[foodindex])

def weaponpick():
  global dinodollars
  global weaponequiped
  lenweap = len(weaponlist)
  lenequiped = len(weaponequiped)
  y = 0
  print("Charm equiped:")
  if lenequiped > 0:
    (print(weaponequiped[0].name,"-",weaponequiped[0].desc))
  else:
    print("Nothing")
  print("Equip charms:")
  while y < lenweap:
    print("[",y+1,"]",weaponlist[y].name,"-", weaponlist[y].desc)
    y = y + 1
  print("[", y+1 ,"] Sell (all items sell for 1 DD)")
  print("[", y+2 ,"] Go back")
  try:
    selectweapon = int(input("> "))
  except (NameError, SyntaxError, ValueError, IndexError):
    selectweapon = 9999
    input("Please use the correct commands!")
  if selectweapon == y + 1:
    try:
      selectsell = int(input("Which number of item would you like to sell?: "))
    except (NameError, SyntaxError, ValueError, IndexError):
      selectsell = 9999
    if selectsell <= lenweap:
      print("Sold:", weaponlist[selectsell - 1].name)
      del weaponlist[selectsell - 1]
      dinodollars = dinodollars + 1
      input("> ")
    else: 
      print("You can't sell that")
      input("> ")
  elif selectweapon <= lenweap:
    weaponlist.append(weaponequiped[0])
    del weaponequiped[0]
    weaponequiped.insert(0,weaponlist[selectweapon-1])
    del weaponlist[selectweapon-1]
    print("Equiped:", weaponequiped[0].name)
    input("> ")
  clearConsole()
  return dinodollars

def gearpick():
  global dinodollars
  global gearequiped
  lengear = len(gearlist)
  lenequiped = len(gearequiped)
  y = 0
  print("Charm equiped:")
  if lenequiped > 0:
    (print(gearequiped[0].name,"-",gearequiped[0].desc))
  else:
    print("Nothing")
  print("Equip charms:")
  while y < lengear:
    print("[", y+1 ,"]",gearlist[y].name,"-", gearlist[y].desc)
    y = y + 1
  print("[", y+1 ,"] Sell (all items sell for 1 DD)")
  print("[", y+2 ,"] Go back")
  try:
    selectgear = int(input("> "))
  except (NameError, SyntaxError, ValueError, IndexError):
    selectgear = 9999
    input("Please use the correct commands!")
  if selectgear == y + 1:
    try:
      selectsell = int(input("Which number of item would you like to sell?: "))
    except (NameError, SyntaxError, ValueError, IndexError):
      selectsell = 9999
    if selectsell <= lengear:
      print("Sold:", gearlist[selectsell - 1].name)
      del gearlist[selectsell - 1]
      dinodollars = dinodollars + 1
      input("> ")
    else: 
      print("You can't sell that")
      input("> ")
  elif selectgear <= lengear:
    gearlist.append(gearequiped[0])
    del gearequiped[0]
    gearequiped.insert(0,gearlist[selectgear-1])
    del gearlist[selectgear-1]
    print("Equiped:", gearequiped[0].name)
    input("> ")
  clearConsole()
  return dinodollars
  
def itemloot(floor):
  if floor == 1:
    itemlist = itemlist1
  elif floor == 2:
    itemlist = itemlist2
  elif floor == 3:
    itemlist = itemlist3
  else:
    itemlist = itemlist4
  y = len(itemlist)
  x = random.randint(0,y-1)
  print("You found:",itemlist[x].name)
  if itemlist[x].type == "weapon":
    weaponlist.append(itemlist[x])
  else:
    gearlist.append(itemlist[x])

def universalstats():
  global luckmin
  global luckmax
  global luckbonus
  global power
  global maxheart
  
  baseluckmin = 0
  baseluckmax = 100
  baseluckbonus = 0
  basepower = 100
  basemaxheart = 100
  
  luckmin = baseluckmin + gearequiped[0].luckmin + weaponequiped[0].luckmin
  luckmax = baseluckmax + gearequiped[0].luckmax + weaponequiped[0].luckmax
  luckbonus = baseluckbonus + gearequiped[0].luck + weaponequiped[0].luck
  power = basepower + gearequiped[0].power + weaponequiped[0].power
  maxheart = basemaxheart + gearequiped[0].maxheart + weaponequiped[0].maxheart

  return luckmin, luckmax, luckbonus, power, maxheart

universalstats()

while c == 1:
  select = 0
  heart = maxheart
  while select not in range(1,5):
    luckmin, luckmax, luckbonus, power, maxheart = universalstats()
    print("===============================================")
    print("  _____ _____ _   _  ____    _____ _____ _____ ")
    print(" |  __ \_   _| \ | |/ __ \  |  __ \_   _/ ____|")
    print(" | |  | || | |  \| | |  | | | |  | || || |  __ ")
    print(" | |  | || | | . ` | |  | | | |  | || || | |_ |")
    print(" | |__| || |_| |\  | |__| | | |__| || || |__| |")
    print(" |_____/_____|_| \_|\____/  |_____/_____\_____|")
    print("===============================================")  
    print("[ 1 ] Dig")
    print("[ 2 ] Store")
    print("[ 3 ] Weapons")
    print("[ 4 ] Charms")
    print("[ 5 ] Info")
    select = (input("> "))
    clearConsole()
    if select == "1":
      spoonmain = spoon(spoonlist)
      dinodollars = dinodollars + dig(spoonmain,luckmin,luckmax,luckbonus,power,maxheart)
      key = 0
    elif select == "2":
      dinodollars, key = shop(dinodollars)
    elif select == "3":
      weaponpick()
    elif select == "4":
      dinodollars = gearpick()
    elif select == "5":
      info(maxheart,power) 
    elif select == "6":
      print(asciiart.cupcakebunny)