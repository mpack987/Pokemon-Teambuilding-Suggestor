attackingDict = {'bug': {'bug': 1.0, 'dark': 2.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 0.5, 'fire': 0.5, 'flying': 0.5, 'ghost': 0.5, 'grass': 2.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 0.5, 'psychic': 2.0, 'rock': 1.0, 'steel': 0.5, 'water': 1.0},
                  'dark': {'bug': 1.0, 'dark': 0.5, 'dragon': 1.0, 'electric': 1.0, 'fairy': 0.5, 
                          'fighting': 0.5, 'fire': 1.0, 'flying': 1.0, 'ghost': 2.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 2.0, 'rock': 1.0, 'steel': 1.0, 'water': 1.0},
                  'dragon': {'bug': 1.0, 'dark': 1.0, 'dragon': 2.0, 'electric': 1.0, 'fairy': 0.0, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 1.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 1.0, 'steel': 0.5, 'water': 1.0},
                  'electric': {'bug': 1.0, 'dark': 1.0, 'dragon': 0.5, 'electric': 0.5, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 2.0, 'ghost': 1.0, 'grass': 0.5, 
                          'ground': 0.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 1.0, 'steel': 1.0, 'water': 2.0},
                  'fairy': {'bug': 1.0, 'dark': 2.0, 'dragon': 2.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 2.0, 'fire': 0.5, 'flying': 1.0, 'ghost': 1.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 0.5, 'psychic': 1.0, 'rock': 1.0, 'steel': 0.5, 'water': 1.0},
                  'fighting': {'bug': 0.5, 'dark': 2.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 0.5, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 0.5, 'ghost': 0.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 2.0, 'normal': 2.0, 'poison': 0.5, 'psychic': 0.5, 'rock': 2.0, 'steel': 2.0, 'water': 1.0},        
                  'fire': {'bug': 2.0, 'dark': 1.0, 'dragon': 0.5, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 0.5, 'flying': 1.0, 'ghost': 1.0, 'grass': 2.0, 
                          'ground': 1.0, 'ice': 2.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 0.5, 'steel': 2.0, 'water': 0.5},
                  'flying': {'bug': 2.0, 'dark': 1.0, 'dragon': 1.0, 'electric': 0.5, 'fairy': 1.0, 
                          'fighting': 2.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 1.0, 'grass': 2.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 0.5, 'steel': 0.5, 'water': 1.0},
                  'ghost': {'bug': 0.5, 'dark': 0.5, 'dragon': 1.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 2.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 0.0, 'poison': 1.0, 'psychic': 2.0, 'rock': 1.0, 'steel': 1.0, 'water': 1.0},
                  'grass': {'bug': 0.5, 'dark': 1.0, 'dragon': 0.5, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 0.5, 'flying': 0.5, 'ghost': 1.0, 'grass': 0.5, 
                          'ground': 2.0, 'ice': 1.0, 'normal': 1.0, 'poison': 0.5, 'psychic': 1.0, 'rock': 2.0, 'steel': 0.5, 'water': 2.0},
                  'ground': {'bug': 0.5, 'dark': 1.0, 'dragon': 1.0, 'electric': 2.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 2.0, 'flying': 0.0, 'ghost': 1.0, 'grass': 0.5, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 2.0, 'psychic': 1.0, 'rock': 2.0, 'steel': 2.0, 'water': 1.0},
                  'ice': {'bug': 1.0, 'dark': 1.0, 'dragon': 2.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 0.5, 'fire': 0.5, 'flying': 2.0, 'ghost': 1.0, 'grass': 2.0, 
                          'ground': 2.0, 'ice': 0.5, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 1.0, 'steel': 0.5, 'water': 0.5},
                  'normal': {'bug': 1.0, 'dark': 1.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 0.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 0.5, 'steel': 0.5, 'water': 1.0},
                  'poison': {'bug': 1.0, 'dark': 1.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 2.0, 
                          'fighting': 1.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 0.5, 'grass': 2.0, 
                          'ground': 0.5, 'ice': 1.0, 'normal': 1.0, 'poison': 0.5, 'psychic': 1.0, 'rock': 0.5, 'steel': 0.0, 'water': 1.0},
                  'psychic': {'bug': 1.0, 'dark': 0.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 2.0, 'fire': 1.0, 'flying': 1.0, 'ghost': 1.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 2.0, 'psychic': 0.5, 'rock': 1.0, 'steel': 0.5, 'water': 1.0},
                  'rock': {'bug': 2.0, 'dark': 1.0, 'dragon': 1.0, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 0.5, 'fire': 2.0, 'flying': 2.0, 'ghost': 1.0, 'grass': 0.5, 
                          'ground': 0.5, 'ice': 2.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 1.0, 'steel': 0.5, 'water': 1.0},
                  'steel': {'bug': 1.0, 'dark': 1.0, 'dragon': 1.0, 'electric': 0.5, 'fairy': 2.0, 
                          'fighting': 1.0, 'fire': 0.5, 'flying': 1.0, 'ghost': 1.0, 'grass': 1.0, 
                          'ground': 1.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 2.0, 'steel': 0.5, 'water': 0.5},
                  'water': {'bug': 1.0, 'dark': 1.0, 'dragon': 0.5, 'electric': 1.0, 'fairy': 1.0, 
                          'fighting': 1.0, 'fire': 2.0, 'flying': 1.0, 'ghost': 1.0, 'grass': 0.5, 
                          'ground': 2.0, 'ice': 1.0, 'normal': 1.0, 'poison': 1.0, 'psychic': 1.0, 'rock': 2.0, 'steel': 1.0, 'water': 0.5}}

class Pokemon:
  def __init__(self, name, type1, type2, hp, atk, df, spA, spD, spd):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
    self.atk = atk
    self.df = df
    self.spA = spA
    self.spD = spD 
    self.spd = spd

# Base SwSh Pokedex
Rillaboom = Pokemon('Rillaboom', 'grass', 'none', 100, 125, 90, 60, 70, 85)
Cinderace = Pokemon('Cinderace', 'fire', 'none', 80, 116, 75, 65, 75, 119)
Inteleon = Pokemon('Inteleon', 'water', 'none', 70, 85, 65, 125, 65, 120)
Orbeetle = Pokemon('Orbeetle', 'bug', 'psychic', 60, 45, 110, 80, 120, 90)
Butterfree = Pokemon('Butterfree', 'bug', 'flying', 60, 45, 50, 90, 80, 70)
Vikavolt = Pokemon('Vikavolt', 'bug', 'electric', 77, 70, 90, 145, 75, 43)
Noctowl = Pokemon('Noctowl', 'normal', 'flying', 100, 50, 50, 86, 96, 70)
Corviknight = Pokemon('Corviknight', 'flying', 'steel', 98, 87, 105, 53, 85, 67)
Greedent = Pokemon('Greedent', 'normal', 'none', 120, 95, 95, 55, 75, 20)
Unfezant = Pokemon('Unfezant', 'normal', 'flying', 80, 115, 80, 65, 55, 93)
Thievul = Pokemon('Thievul', 'dark', 'none', 70, 58, 58, 87, 92, 90)
Obstagoon = Pokemon('Obstagoon', 'normal', 'dark', 93, 90, 101, 60, 81, 95)
Dubwool = Pokemon('Dubwool', 'normal', 'none', 72, 80, 100, 60, 90, 88)
Ludicolo = Pokemon('Ludicolo', 'water', 'grass', 80, 70, 70, 90, 100, 70)
Shiftry = Pokemon('Shiftry', 'grass', 'dark', 90, 100, 60, 90, 60, 80)
Drednaw = Pokemon('Drednaw', 'water', 'rock', 90, 115, 90, 48, 68, 74)
Liepard = Pokemon('Liepard', 'dark', 'none', 64, 88, 50, 88, 50, 106)
Boltund = Pokemon('Boltund', 'electric', 'none', 69, 90, 60, 90, 60, 121)
Diggersby = Pokemon('Diggersby', 'normal', 'ground', 85, 56, 77, 50, 77, 78)
Cinccino = Pokemon('Cinccino', 'normal', 'none', 75, 95, 60, 65, 60, 115)
Tsareena = Pokemon('Tsareena', 'grass', 'none', 72, 120, 98, 50, 98, 72)
Vileplume = Pokemon('Vileplume', 'grass', 'poison', 75, 80, 85, 110, 90, 50)
Bellossom = Pokemon('Bellossom', 'grass', 'none', 75, 80, 95, 90, 100, 50)
Roserade = Pokemon('Roserade', 'grass', 'poison', 60, 70, 65, 125, 105, 90)
Pelipper = Pokemon('Pelipper', 'water', 'flying', 60, 50, 100, 95, 70, 65)
Galvantula = Pokemon('Galvantula', 'bug', 'electric', 70, 77, 60, 97, 60, 108)
Manectric = Pokemon('Manectric', 'electric', 'none', 70, 75, 60, 105, 60, 105)
Ninetales = Pokemon('Ninetales', 'fire', 'none', 73, 76, 75, 81, 100, 100)
Arcanine = Pokemon('Arcanine', 'fire', 'none', 90, 110, 80, 100, 80, 95)
Vanilluxe = Pokemon('Vanilluxe', 'ice', 'none', 71, 95, 85, 110, 95, 79)
Mamoswine = Pokemon('Mamoswine', 'ice', 'ground', 110, 130, 80, 70, 60, 80)
Delibird = Pokemon('Delibird', 'ice', 'flying', 45, 55, 45, 65, 45, 75)
Glalie = Pokemon('Glalie', 'ice', 'none', 80, 80, 80, 80, 80, 80)
Froslass = Pokemon('Froslass', 'ice', 'ghost', 70, 80, 70, 80, 70, 110)
Claydol = Pokemon('Claydol', 'ground', 'psychic', 60, 70, 105, 70, 120, 75)
Mudsdale = Pokemon('Mudsdale', 'ground', 'none', 100, 125, 100, 55, 85, 35)
Crustle = Pokemon('Crustle', 'bug', 'rock', 70, 105, 125, 65, 72, 45)
Golurk = Pokemon('Golurk', 'ground', 'ghost', 89, 124, 80, 55, 80, 55)
Musharna = Pokemon('Musharna', 'psychic', 'none', 116, 55, 85, 107, 95, 29)
Xatu = Pokemon('Xatu', 'psychic', 'flying', 65, 75, 70, 95, 70, 95)
Bewear = Pokemon('Bewear', 'normal', 'fighting', 120, 125, 80, 55, 60, 60)
Abomasnow = Pokemon('Abomasnow', 'grass', 'ice', 90, 92, 75, 92, 85, 60)
Kingler = Pokemon('Kingler', 'water', 'none', 55, 130, 115, 50, 50, 75)
Quagsire = Pokemon('Quagsire', 'water', 'ground', 95, 85, 85, 65, 65, 35)
Crawdaunt = Pokemon('Crawdaunt', 'water', 'dark', 63, 120, 85, 90, 55, 55)
Ninjask = Pokemon('Ninjask', 'bug', 'flying', 61, 90, 45, 50, 50, 160)
Shedinja = Pokemon('Shedinja', 'bug', 'ghost', 1, 90, 45, 30, 30, 40)
Hitmonlee = Pokemon('Hitmonlee', 'fighting', 'none', 50, 120, 53, 35, 110, 87)
Hitmonchan = Pokemon('Hitmonchan', 'fighting', 'none', 50, 105, 79, 35, 110, 76)
Hitmontop = Pokemon('Hitmontop', 'fighting', 'none', 50, 95, 95, 35, 110, 70)
Pangoro = Pokemon('Pangoro', 'fighting', 'dark', 95, 124, 78, 69, 71, 58)
Klinklang = Pokemon('Klinklang', 'steel', 'none', 60, 100, 115, 70, 85, 90)
Vespiquen = Pokemon('Vespiquen', 'bug', 'flying', 70, 80, 102, 80, 102, 40)
Bronzong = Pokemon('Bronzong', 'steel', 'psychic', 67, 89, 116, 79, 116, 33)
Gardevoir = Pokemon('Gardevoir', 'psychic', 'fairy', 68, 65, 65, 125, 115, 80)
Gallade = Pokemon('Gallade', 'psychic', 'fighting', 68, 125, 65, 65, 115, 80)
Drifblim = Pokemon('Drifblim', 'ghost', 'flying', 150, 80, 44, 90, 54, 80)
Eldegoss = Pokemon('Eldegoss', 'grass', 'none', 60, 50, 90, 80, 120, 60)
Cherrim = Pokemon('Cherrim', 'grass', 'none', 70, 60, 70, 87, 78, 85)
Skuntank = Pokemon('Skuntank', 'poison', 'dark', 103, 93, 67, 71, 61, 84)
Seismitoad = Pokemon('Seismitoad', 'water', 'ground', 105, 95, 75, 85, 75, 74)
Dusclops = Pokemon('Dusclops', 'ghost', 'none', 40, 70, 130, 60, 130, 25)
Dusknoir = Pokemon('Dusknoir', 'ghost', 'none', 45, 100, 135, 65, 135, 45)
Machamp = Pokemon('Machamp', 'fighting', 'none', 90, 130, 80, 65, 85, 55)
Gengar = Pokemon('Gengar', 'ghost', 'poison', 60, 65, 60, 130, 75, 110)
Gyarados = Pokemon('Gyarados', 'water', 'flying', 95, 125, 79, 60, 100, 81)
Seaking = Pokemon('Seaking', 'water', 'none', 80, 92, 65, 65, 80, 68)
Octillery = Pokemon('Octillery', 'water', 'none', 75, 105, 75, 105, 75, 45)
Cloyster = Pokemon('Cloyster', 'water', 'ice', 50, 95, 180, 85, 45, 70)
Milotic = Pokemon('Milotic', 'water', 'none', 95, 60, 79, 100, 125, 81)
Basculin = Pokemon('Basculin', 'water', 'none', 70, 92, 65, 80, 55, 98)
Wishiwashi = Pokemon('Wishiwashi', 'water', 'none', 45, 140, 130, 140, 135, 30)
Pyukumuku = Pokemon('Pyukumuku', 'water', 'none', 55, 60, 130, 30, 130, 5)
Garbodor = Pokemon('Garbodor', 'poison', 'none', 80, 95, 82, 60, 82, 75)
Centiskorch = Pokemon('Centiskorch', 'fire', 'bug', 50, 65, 45, 50, 50, 45)
Coalossal = Pokemon('Coalossal', 'rock', 'fire', 110, 80, 120, 80, 90, 30)
Dugtrio = Pokemon('Dugtrio', 'ground', 'none', 35, 100, 50, 50, 70, 120)
Excadrill = Pokemon('Excadrill', 'ground', 'steel', 110, 130, 60, 50, 65, 88)
Gigalith = Pokemon('Gigalith', 'rock', 'none', 85, 135, 130, 60, 80, 25)
Conkeldurr = Pokemon('Conkeldurr', 'fighting', 'none', 105, 140, 95, 55, 65, 45)
Swoobat = Pokemon('Swoobat', 'psychic', 'flying', 67, 57, 55, 77, 55, 114)
Noivern = Pokemon('Noivern', 'flying', 'dragon', 85, 70, 80, 97, 80, 123)
Steelix = Pokemon('Steelix', 'steel', 'ground', 75, 85, 200, 55, 65, 30)
Barraskewda = Pokemon('Barraskewda', 'water', 'none', 61, 123, 60, 60, 50, 136)
Perrserker = Pokemon('Perrserker', 'steel', 'none', 70, 110, 100, 50, 60, 50)
Persian = Pokemon('Persian', 'normal', 'none', 65, 70, 60, 65, 65, 115)
Alcremie = Pokemon('Alcremie', 'fairy', 'none', 65, 60, 75, 110, 121, 64)
Ribombee = Pokemon('Ribombee', 'bug', 'fairy', 60, 55, 60, 95, 70, 124)
Ferrothorn = Pokemon('Ferrothorn', 'grass', 'steel', 74, 94, 131, 54, 116, 20)
Gourgeist = Pokemon('Gourgeist', 'ghost', 'grass', 65, 90, 122, 58, 75, 84)
Raichu = Pokemon('Raichu', 'electric', 'none', 60, 90, 55, 90, 80, 110)
Vaporeon = Pokemon('Vaporeon', 'water', 'none', 130, 65, 60, 110, 95, 65)
Jolteon = Pokemon('Jolteon', 'electric', 'none', 65, 65, 60, 110, 95, 130)
Flareon = Pokemon('Flareon', 'fire', 'none', 65, 130, 60, 95, 110, 65)
Espeon = Pokemon('Espeon', 'psychic', 'none', 65, 65, 60, 130, 95, 110)
Umbreon = Pokemon('Umbreon', 'dark', 'none', 95, 65, 110, 60, 130, 65)
Leafeon = Pokemon('Leafeon', 'grass', 'none', 65, 110, 130, 60, 65, 95)
Glaceon = Pokemon('Glaceon', 'ice', 'none', 65, 60, 110, 130, 95, 65)
Sylveon = Pokemon('Sylveon', 'fairy', 'none', 95, 65, 65, 110, 130, 60)
Flapple = Pokemon('Flapple', 'grass', 'dragon', 70, 110, 80, 95, 60, 70)
Appletun = Pokemon('Appletun', 'grass', 'dragon', 110, 85, 80, 100, 80, 30)
Meowstic = Pokemon('Meowstic', 'psychic', 'none', 74, 48, 76, 83, 81, 104)
Slurpuff = Pokemon('Slurpuff', 'fairy', 'none', 82, 80, 86, 85, 75, 72)
Aromatisse = Pokemon('Aromatisse', 'fairy', 'none', 101, 72, 72, 99, 89, 29)
Araquanid = Pokemon('Araquanid', 'water', 'bug', 68, 70, 92, 50, 132, 42)
Wobbuffet = Pokemon('Wobbuffet', 'psychic', 'none', 190, 33, 58, 33, 58, 33)
Sirfetchd = Pokemon('Sirfetchd', 'fighting', 'none', 62, 135, 95, 68, 82, 65)
Lanturn = Pokemon('Lanturn', 'water', 'electric', 125, 58, 58, 76, 76, 67)
Toxicroak = Pokemon('Toxicroak', 'poison', 'fighting', 83, 106, 65, 86, 65, 85)
Scrafty = Pokemon('Scrafty', 'dark', 'fighting', 65, 90, 115, 45, 115, 58)
Stunfisk_Galar = Pokemon('Stunfisk_Galar', 'ground', 'steel', 109, 81, 99, 66, 84, 32)
Shuckle = Pokemon('Shuckle', 'bug', 'rock', 20, 10, 230, 10, 230, 5)
Whiscash = Pokemon('Whiscash', 'water', 'ground', 110, 78, 73, 76, 71, 60)
Gastrodon = Pokemon('Gastrodon', 'water', 'ground', 111, 83, 68, 92, 82, 39)
Golisopod = Pokemon('Golisopod', 'bug', 'water', 75, 125, 140, 60, 90, 40)
Barbaracle = Pokemon('Barbaracle', 'rock', 'water', 72, 105, 115, 54, 86, 68)
Corsola_Galar = Pokemon('Corsola_Galar', 'ghost', 'none', 60, 55, 100, 65, 100, 30)
Cursola = Pokemon('Cursola', 'ghost', 'none', 60, 95, 50, 145, 130, 30)
Grimmsnarl = Pokemon('Grimmsnarl', 'dark', 'fairy', 95, 120, 65, 95, 75, 60)
Hatterene = Pokemon('Hatterene', 'psychic', 'fairy', 57, 90, 95, 136, 103, 29)
Salazzle = Pokemon('Salazzle', 'poison', 'fire', 68, 64, 60, 111, 60, 117)
Bisharp = Pokemon('Bisharp', 'dark', 'steel', 65, 125, 100, 60, 70, 70)
Throh = Pokemon('Throh', 'fighting', 'none', 120, 100, 85, 30, 85, 45)
Sawk = Pokemon('Sawk', 'fighting', 'none', 75, 125, 75, 30, 75, 85)
Weezing_Galar = Pokemon('Weezing_Galar', 'poison', 'fairy', 65, 90, 120, 85, 70, 60)
Sudowoodo = Pokemon('Sudowoodo', 'rock', 'none', 70, 100, 115, 30, 65, 30)
Clefable = Pokemon('Clefable', 'fairy', 'none', 95, 70, 73, 95, 90, 60)
Togekiss = Pokemon('Togekiss', 'fairy', 'flying', 85, 50, 95, 120, 115, 80)
Snorlax = Pokemon('Snorlax', 'normal', 'none', 160, 110, 65, 65, 110, 30)
Whimsicott = Pokemon('Whimsicott', 'grass', 'fairy', 60, 67, 85, 77, 75, 116)
Rhyperior = Pokemon('Rhyperior', 'ground', 'rock', 115, 140, 130, 55, 55, 40)
Gothitelle = Pokemon('Gothitelle', 'psychic', 'none', 70, 55, 95, 95, 110, 65)
Reuniclus = Pokemon('Reuniclus', 'psychic', 'none', 110, 65, 75, 125, 85, 30)
Escavalier = Pokemon('Escavalier', 'bug', 'steel', 70, 135, 105, 60, 105, 20)
Accelgor = Pokemon('Accelgor', 'bug', 'none', 80, 70, 40, 100, 60, 145)
Beheeyem = Pokemon('Beheeyem', 'psychic', 'none', 75, 75, 75, 125, 95, 40)
Beartic = Pokemon('Beartic', 'ice', 'none', 95, 130, 80, 70, 80, 50)
Braviary = Pokemon('Braviary', 'normal', 'flying', 100, 123, 75, 57, 75, 80)
Mandibuzz = Pokemon('Mandibuzz', 'dark', 'flying', 110, 65, 105, 55, 95, 80)
Drapion = Pokemon('Drapion', 'poison', 'dark', 70, 90, 110, 60, 75, 95)
Chandelure = Pokemon('Chandelure', 'ghost', 'fire', 60, 55, 90, 145, 90, 80)
Malamar = Pokemon('Malamar', 'dark', 'psychic', 86, 92, 88, 68, 75, 73)
Weavile = Pokemon('Weavile', 'dark', 'ice', 70, 120, 65, 45, 85, 125)
Sableye = Pokemon('Sableye', 'dark', 'ghost', 50, 75, 75, 65, 65, 50)
Mawile = Pokemon('Mawile', 'steel', 'fairy', 50, 85, 85, 55, 55, 50)
Maractus = Pokemon('Maractus', 'grass', 'none', 75, 86, 67, 106, 67, 60)
Sigilyph = Pokemon('Sigilyph', 'psychic', 'flying', 72, 58, 80, 103, 80, 97)
Lucario = Pokemon('Lucario', 'fighting', 'steel', 70, 110, 70, 115, 70, 90)
Torkoal = Pokemon('Torkoal', 'fire', 'none', 70, 85, 140, 85, 80, 20)
Mimikyu = Pokemon('Mimikyu', 'ghost', 'fairy', 55, 90, 80, 50, 105, 96)
Copperajah = Pokemon('Copperajah', 'steel', 'none', 122, 130, 69, 80, 69, 30)
Qwilfish = Pokemon('Qwilfish', 'water', 'poison', 65, 95, 85, 55, 55, 85)
Jellicent = Pokemon('Jellicent', 'water', 'ghost', 100, 60, 70, 85, 105, 60)
Toxapex = Pokemon('Toxapex', 'poison', 'water', 50, 63, 152, 53, 142, 35)
Cramorant = Pokemon('Cramorant', 'flying', 'water', 70, 85, 55, 85, 95, 85)
Toxtricity = Pokemon('Toxtricity', 'electric', 'poison', 75, 98, 70, 114, 70, 75)
Sandaconda = Pokemon('Sandaconda', 'ground', 'none', 72, 107, 125, 65, 70, 71)
Hippowdon = Pokemon('Hippowdon', 'ground', 'none', 108, 112, 118, 68, 72, 47)
Durant = Pokemon('Durant', 'bug', 'steel', 58, 109, 112, 48, 48, 109)
Heatmor = Pokemon('Heatmor', 'fire', 'none', 85, 97, 66, 105, 66, 65)
Heliolisk = Pokemon('Heliolisk', 'electric', 'normal', 62, 55, 52, 109, 94, 109)
Hawlucha = Pokemon('Hawlucha', 'fighting', 'flying', 78, 92, 75, 74, 63, 118)
Flygon = Pokemon('Flygon', 'ground', 'dragon', 80, 100, 80, 80, 80, 100)
Haxorus = Pokemon('Haxorus', 'dragon', 'none', 76, 147, 90, 60, 70, 97)
Runerigus = Pokemon('Runerigus', 'ground', 'ghost', 58, 95, 145, 50, 105, 30)
Cofagrigus = Pokemon('Cofagrigus', 'ghost', 'none', 58, 50, 145, 95, 105, 30)
Aegislash = Pokemon('Aegislash', 'steel', 'ghost', 60, 50, 140, 50, 140, 60)
Rapidash_Galar = Pokemon('Rapidash_Galar', 'psychic', 'fairy', 65, 100, 70, 80, 80, 105)
Polteageist = Pokemon('Polteageist', 'ghost', 'none', 60, 65, 65, 134, 114, 70)
Trevenant = Pokemon('Trevenant', 'ghost', 'grass', 85, 110, 76, 65, 82, 56)
Shiinotic = Pokemon('Shiinotic', 'grass', 'fairy', 60, 45, 80, 90, 100, 30)
Oranguru = Pokemon('Oranguru', 'normal', 'psychic', 90, 60, 80, 90, 110, 60)
Passimian = Pokemon('Passimian', 'fighting', 'none', 100, 120, 90, 40, 60, 80)
Morpeko = Pokemon('Morpeko', 'electric', 'dark', 58, 95, 58, 70, 58, 97)
Falinks = Pokemon('Falinks', 'fighting', 'none', 65, 100, 100, 70, 60, 75)
Drampa = Pokemon('Drampa', 'normal', 'dragon', 78, 60, 85, 135, 91, 36)
Turtonator = Pokemon('Turtonator', 'fire', 'dragon', 60, 78, 135, 91, 85, 36)
Togedemaru = Pokemon('Togedemaru', 'electric', 'steel', 65, 98, 63, 40, 73, 96)
Frosmoth = Pokemon('Frosmoth', 'ice', 'bug', 70, 65, 60, 125, 90, 65)
Grapploct = Pokemon('Grapploct', 'fighting', 'none', 80, 118, 90, 70, 80, 42)
Pincurchin = Pokemon('Pincurchin', 'electric', 'none', 48, 101, 95, 91, 85, 15)
Mantine = Pokemon('Mantine', 'water', 'flying', 85, 40, 70, 80, 140, 70)
Wailord = Pokemon('Wailord', 'water', 'none', 170, 90, 45, 90, 45, 60)
Avalugg = Pokemon('Avalugg', 'ice', 'none', 95, 117, 184, 44, 46, 28)
Dhelmise = Pokemon('Dhelmise', 'ghost', 'grass', 70, 131, 100, 86, 90, 40)
Lapras = Pokemon('Lapras', 'water', 'ice', 130, 85, 80, 85, 95, 60)
Lunatone = Pokemon('Lunatone', 'rock', 'psychic', 90, 95, 85, 55, 65, 70)
Solrock = Pokemon('Solrock', 'rock', 'psychic', 90, 95, 85, 55, 65, 70)
MrMime_Galar = Pokemon('MrMime_Galar', 'ice', 'psychic', 50, 65, 65, 90, 90, 100)
MrRime = Pokemon('MrRime', 'ice', 'psychic', 80, 85, 75, 110, 100, 70)
Darmanitan_Galar = Pokemon('Darmanitan_Galar', 'ice', 'none', 105, 140, 55, 30, 55, 95)
Stonjourner = Pokemon('Stonjourner', 'rock', 'none', 100, 125, 125, 20, 20, 70)
Eiscue = Pokemon('Eiscue', 'ice', 'none', 75, 80, 110, 65, 90, 50)
Duraludon = Pokemon('Duraludon', 'steel', 'dragon', 70, 95, 115, 120, 50, 85)
Rotom = Pokemon('Rotom', 'electric', 'ghost', 50, 50, 77, 95, 77, 91)
Rotom_Mow = Pokemon('Rotom_Mow', 'electric', 'grass', 50, 50, 77, 95, 77, 91)
Rotom_Fan = Pokemon('Rotom_Fan', 'electric', 'flying', 50, 50, 77, 95, 77, 91)
Rotom_Fridge = Pokemon('Rotom_Fridge', 'electric', 'ice', 50, 50, 77, 95, 77, 91)
Rotom_Wash = Pokemon('Rotom_Wash', 'electric', 'water', 50, 50, 77, 95, 77, 91)
Rotom_Heat = Pokemon('Rotom_Heat', 'electric', 'fire', 50, 50, 77, 95, 77, 91)
Ditto = Pokemon('Ditto', 'normal', 'none', 48, 48, 48, 48, 48, 48)
Dracozolt = Pokemon('Dracozolt', 'electric', 'dragon', 90, 100, 90, 80, 70, 75)
Arctozolt = Pokemon('Arctozolt', 'electric', 'ice', 90, 100, 90, 90, 80, 55)
Dracovish = Pokemon('Dracovish', 'water', 'dragon', 90, 90, 100, 70, 80, 75)
Arctovish = Pokemon('Arctovish', 'water', 'ice', 90, 90, 100, 80, 90, 55)
Charizard = Pokemon('Charizard', 'fire', 'flying', 78, 84, 78, 109, 85, 100)
Silvally = Pokemon('Silvally', 'normal', 'none', 95, 95, 95, 95, 95, 95)
Tyranitar = Pokemon('Tyranitar', 'rock', 'dark', 100, 134, 110, 95, 100, 61)
Hydreigon = Pokemon('Hydreigon', 'dark', 'dragon', 92, 105, 90, 125, 90, 98)
Goodra = Pokemon('Goodra', 'dragon', 'none', 90, 100, 70, 110, 150, 80)
Kommo_o = Pokemon('Kommo_o', 'dragon', 'fighting', 75, 110, 125, 100, 105, 85)
Dragapult = Pokemon('Dragapult', 'dragon', 'ghost', 88, 120, 75, 100, 75, 142)

# Isle of Armor Additions
Slowbro_Galar = Pokemon('Slowbro_Galar', 'poison', 'psychic', 95, 100, 95, 100, 70, 30)
Slowking = Pokemon('Slowking', 'water', 'psychic', 95, 75, 80, 100, 110, 30)
Lopunny = Pokemon('Lopunny', 'normal', 'none', 65, 76, 84, 54, 96, 105)
Chansey = Pokemon('Chansey', 'normal', 'none', 250, 5, 5, 35, 105, 50)
Blissey = Pokemon('Blissey', 'normal', 'none', 255, 10, 10, 75, 135, 55)
Wigglytuff = Pokemon('Wiggleytuff', 'normal', 'fairy', 140, 70, 45, 85, 50, 45)
Lurantis = Pokemon('Lurantis', 'grass', 'none', 70, 105, 90, 80, 90, 45)
Talonflame = Pokemon('Talonflame', 'fire', 'flying', 78, 81, 71, 74, 69, 126)
Luxray = Pokemon('Luxray', 'electric', 'none', 80, 120, 79, 95, 79, 70)
Klefki = Pokemon('Klefki', 'steel', 'fairy', 57, 80, 91, 80, 87, 75)
Alakazam = Pokemon('Alakazam', 'psychic', 'none', 55, 50, 45, 135, 95, 120)
Tentacool = Pokemon('Tentacool', 'water', 'poison', 80, 70, 65, 80, 120, 100)
Dunsparce = Pokemon('Dunsparce', 'normal', 'none', 100, 70, 70, 65, 65, 45)
Bouffalant = Pokemon('Bouffalant', 'normal', 'none', 95, 110, 95, 40, 95, 55)
Lickilicky = Pokemon('Lickilicky', 'normal', 'none', 110, 85, 95, 80, 95, 50)
Druddigon = Pokemon('Druddigon', 'dragon', 'none', 77, 120, 90, 60, 90, 48)
Venusaur = Pokemon('Venusaur', 'grass', 'poison', 80, 82, 83, 100, 100, 80)
Blastoise = Pokemon('Blastoise', 'water', 'none', 79, 83, 100, 85, 105, 78)
Scolipede = Pokemon('Scolipede', 'bug', 'poison', 60, 100, 89, 55, 69, 112)
Amoongus = Pokemon('Amoongus', 'grass', 'poison', 114, 85, 70, 85, 80, 30)
Tangrowth = Pokemon('Tangrowth', 'grass', 'none', 100, 100, 125, 110, 50, 50)
Zoroark = Pokemon('Zoroark', 'dark', 'none', 60, 105, 60, 120, 60, 105)
Starmie = Pokemon('Starmie', 'water', 'psychic', 60, 75, 85, 100, 85, 115)
Urshifu_Single = Pokemon('Urshifu_Single', 'fighting', 'dark', 100, 130, 100, 63, 60, 97)
Urshifu_Rapid = Pokemon('Urshifu_Rapid', 'fighting', 'water', 100, 130, 100, 63, 60, 97)
Emolga = Pokemon('Emolga', 'electric', 'flying', 55, 75, 60, 75, 60, 103)
Dedenne = Pokemon('Dedenne', 'electric', 'fairy', 67, 58, 57, 81, 67, 101)
Magnezone = Pokemon('Magnezone', 'electric', 'steel', 70, 70, 115, 130, 90, 60)
Sharpedo = Pokemon('Sharpedo', 'water', 'dark', 70, 120, 40, 95, 40, 95)
Stoutland = Pokemon('Stoutland', 'normal', 'none', 85, 110, 90, 45, 90, 80)
Tauros = Pokemon('Tauros', 'normal', 'none', 75, 100, 95, 40, 70, 110)
Miltank = Pokemon('Miltank', 'normal', 'none', 95, 80, 105, 40, 70, 100)
Scyther = Pokemon('Scyther', 'bug', 'flying', 70, 110, 80, 55, 80, 105)
Scizor = Pokemon('Scizor', 'bug', 'steel', 70, 130, 100, 55, 80, 65)
Pinsir = Pokemon('Pinsir', 'bug', 'none', 65, 125, 100, 55, 70, 85)
Heracross = Pokemon('Heracross', 'bug', 'fighting', 80, 125, 75, 40, 95, 85)
Palossand = Pokemon('Palossand', 'ghost', 'ground', 85, 75, 110, 100, 75, 35)
Azumarill = Pokemon('Azumarill', 'water', 'fairy', 100, 50, 80, 60, 80, 50)
Poliwrath = Pokemon('Poliwrath', 'water', 'fighting', 90, 95, 95, 70, 90, 70)
Politoed = Pokemon('Politoed', 'water', 'none', 90, 75, 75, 90, 100, 70)
Golduck = Pokemon('Golduck', 'water', 'none', 80, 82, 78, 95, 80, 85)
Exploud = Pokemon('Exploud', 'normal', 'none', 104, 91, 63, 91, 73, 68)
Skarmory = Pokemon('Skarmory', 'steel', 'flying', 65, 80, 140, 40, 70, 70)
Lycanroc_Midday = Pokemon('Lycanroc_Midday', 'rock', 'none', 75, 115, 65, 55, 65, 112)
Lycanroc_Midnight = Pokemon('Lycanroc_Midnight', 'rock', 'none', 85, 115, 75, 55, 75, 82)
Lycanroc_Dusk = Pokemon('Lycanroc_Dusk', 'rock', 'none', 75, 117, 65, 55, 65, 110)
Mienshao = Pokemon('Mienshao', 'fighting', 'none', 65, 125, 60, 95, 60, 105)
Sandslash = Pokemon('Sandslash', 'ground', 'none', 75, 100, 110, 45, 55, 65)
Marowak = Pokemon('Marowak', 'ground', 'none', 60, 80, 110, 50, 80, 45)
Kangaskhan = Pokemon('Kangaskhan', 'normal', 'none', 105, 95, 80, 40, 80, 90)
Krookodile = Pokemon('Krookodile', 'ground', 'dark', 95, 117, 80, 65, 70, 92)
Volcarona = Pokemon('Volcarona', 'bug', 'fire', 85, 60, 65, 135, 105, 100)
Dragalge = Pokemon('Dragalge', 'poison', 'dragon', 65, 75, 90, 97, 123, 44)
Clawitzer = Pokemon('Clawitzer', 'water', 'none', 71, 73, 88, 120, 89, 59)
Kingdra = Pokemon('Kingdra', 'water', 'dragon', 75, 95, 95, 95, 95, 85)
Lilligant = Pokemon('Lilligant', 'grass', 'none', 70, 60, 75, 110, 75, 90)
Exeggutor = Pokemon('Exeggutor', 'grass', 'psychic', 95, 95, 85, 125, 75, 55)
Porygon2 = Pokemon('Porygon2', 'normal', 'none', 85, 80, 90, 105, 95, 60)
Porygon_Z = Pokemon('Porygon_Z', 'normal', 'none', 85, 80, 70, 135, 75, 90)
Decidueye = Pokemon('Decidueye', 'grass', 'ghost', 78, 107, 75, 100, 100, 70)
Incineroar = Pokemon('Incineroar', 'fire', 'dark', 95, 115, 90, 80, 90, 60)
Primarina = Pokemon('Primarina', 'water', 'fairy', 80, 74, 74, 126, 116, 60)
Raichu_Alolan = Pokemon('Raichu_Alolan', 'electric', 'psychic', 60, 85, 50, 95, 85, 110)
Sandslash_Alolan = Pokemon('Sandslash', 'ice', 'steel', 75, 100, 120, 25, 65, 65)
Ninetales_Alolan = Pokemon('Ninetales_Alolan', 'ice', 'fairy', 73, 67, 75, 81, 100, 109)
Dugtrio_Alolan = Pokemon('Dugtrio_Alolan', 'ground', 'steel', 35, 100, 60, 50, 70, 110)
Persian_Alolan = Pokemon('Persian_Alolan', 'dark', 'none', 65, 60, 60, 75, 65, 115)
Exeggutor_Alolan = Pokemon('Exeggutor_Alolan', 'grass', 'dragon', 95, 105, 85, 125, 75, 45)
Marowak_Alolan = Pokemon('Marowak_Alolan', 'fire', 'ghost', 60, 80, 110, 50, 80, 45)
Rapidash = Pokemon('Rapidash', 'psychic', 'fairy', 65, 100, 70, 80, 80, 105)
Corsola = Pokemon('Corsola', 'water', 'rock', 65, 55, 95, 65, 95, 35)
Linoone = Pokemon('Linoone', 'normal', 'none', 78, 70, 61, 50, 61, 100)
Dramanitan = Pokemon('Darmanitan', 'fire', 'none', 105, 140, 55, 30, 55, 95)
Stunfisk = Pokemon('Stunfisk', 'ground', 'electric', 109, 66, 84, 81, 99, 32)

pokedex = [Rillaboom ,  Cinderace ,  Inteleon ,  Orbeetle ,  Butterfree ,  Vikavolt ,  Noctowl ,  Corviknight ,  Greedent ,
           Unfezant ,  Thievul ,  Obstagoon ,  Dubwool ,  Ludicolo ,  Shiftry ,  Drednaw ,  Liepard ,  Boltund ,  Diggersby ,
           Cinccino ,  Tsareena ,  Vileplume ,  Bellossom ,  Roserade ,  Pelipper ,  Galvantula ,  Manectric ,  Ninetales ,  Arcanine ,
           Vanilluxe ,  Mamoswine ,  Delibird ,  Glalie ,  Froslass ,  Claydol ,  Mudsdale ,  Crustle ,  Golurk ,  Musharna ,  Xatu ,
           Bewear ,  Abomasnow ,  Kingler ,  Quagsire ,  Crawdaunt ,  Ninjask ,  Shedinja ,  Hitmonlee ,  Hitmonchan ,  Hitmontop ,
           Pangoro ,  Klinklang ,  Vespiquen ,  Bronzong ,  Gardevoir ,  Gallade ,  Drifblim ,  Eldegoss ,  Cherrim ,  Skuntank ,
           Seismitoad ,  Dusclops ,  Dusknoir ,  Machamp ,  Gengar ,  Gyarados ,  Seaking ,  Octillery ,  Cloyster ,  Milotic ,
           Basculin ,  Wishiwashi ,  Pyukumuku ,  Garbodor ,  Centiskorch ,  Coalossal ,  Dugtrio ,  Excadrill ,  Gigalith ,
           Conkeldurr ,  Swoobat ,  Noivern ,  Steelix ,  Barraskewda ,  Perrserker ,  Persian ,  Alcremie ,  Ribombee ,
           Ferrothorn ,  Gourgeist ,  Raichu ,  Vaporeon ,  Jolteon ,  Flareon ,  Espeon ,  Umbreon ,  Leafeon ,  Glaceon ,
           Sylveon ,  Flapple ,  Appletun ,  Meowstic ,  Slurpuff ,  Aromatisse ,  Araquanid ,  Wobbuffet ,  Sirfetchd ,  Lanturn ,
           Toxicroak ,  Scrafty ,  Stunfisk_Galar ,  Shuckle ,  Whiscash ,  Gastrodon ,  Golisopod ,  Barbaracle ,  Corsola_Galar ,
           Cursola ,  Grimmsnarl ,  Hatterene ,  Salazzle ,  Bisharp ,  Throh ,  Sawk ,  Weezing_Galar ,  Sudowoodo ,  Clefable ,
           Togekiss ,  Snorlax ,  Whimsicott ,  Rhyperior ,  Gothitelle ,  Reuniclus ,  Escavalier ,  Accelgor ,  Beheeyem ,  Beartic ,
           Braviary ,  Mandibuzz ,  Drapion ,  Chandelure ,  Malamar ,  Weavile ,  Sableye ,  Mawile ,  Maractus ,  Sigilyph ,  Lucario ,
           Torkoal ,  Mimikyu ,  Copperajah ,  Qwilfish ,  Jellicent ,  Toxapex ,  Cramorant ,  Toxtricity ,  Sandaconda ,  Hippowdon ,
           Durant ,  Heatmor ,  Heliolisk ,  Hawlucha ,  Flygon ,  Haxorus ,  Runerigus ,  Cofagrigus ,  Aegislash ,  Rapidash_Galar ,
           Polteageist ,  Trevenant ,  Shiinotic ,  Oranguru ,  Passimian ,  Morpeko ,  Falinks ,  Drampa ,  Turtonator ,  Togedemaru ,
           Frosmoth ,  Grapploct ,  Pincurchin ,  Mantine ,  Wailord ,  Avalugg ,  Dhelmise ,  Lapras ,  Lunatone ,  Solrock ,  MrMime_Galar ,
           MrRime ,  Darmanitan_Galar ,  Stonjourner ,  Eiscue ,  Duraludon ,  Rotom ,  Rotom_Mow ,  Rotom_Fan ,  Rotom_Fridge ,
           Rotom_Wash ,  Rotom_Heat ,  Ditto ,  Dracozolt ,  Arctozolt ,  Dracovish ,  Arctovish ,  Charizard ,  Silvally ,  Tyranitar ,
           Hydreigon ,  Goodra ,  Kommo_o ,  Dragapult ,  Slowbro_Galar ,  Slowking ,  Lopunny ,  Chansey ,  Blissey ,  Wigglytuff ,
           Lurantis ,  Talonflame ,  Luxray ,  Klefki ,  Alakazam ,  Tentacool ,  Dunsparce ,  Bouffalant ,  Lickilicky ,  Druddigon ,
           Venusaur ,  Blastoise ,  Scolipede ,  Amoongus ,  Tangrowth ,  Zoroark ,  Starmie ,  Urshifu_Single ,  Urshifu_Rapid ,
           Emolga ,  Dedenne ,  Magnezone ,  Sharpedo ,  Stoutland ,  Tauros ,  Miltank ,  Scyther ,  Scizor ,  Pinsir ,  Heracross ,
           Palossand ,  Azumarill ,  Poliwrath ,  Politoed ,  Golduck ,  Exploud ,  Skarmory ,  Lycanroc_Midday ,  Lycanroc_Midnight ,
           Lycanroc_Dusk ,  Mienshao ,  Sandslash ,  Marowak ,  Kangaskhan ,  Krookodile ,  Volcarona ,  Dragalge ,  Clawitzer ,  Kingdra ,
           Lilligant ,  Exeggutor ,  Porygon2 ,  Porygon_Z ,  Decidueye ,  Incineroar ,  Primarina ,  Raichu_Alolan ,  Sandslash_Alolan ,
           Ninetales_Alolan ,  Dugtrio_Alolan ,  Persian_Alolan ,  Exeggutor_Alolan ,  Marowak_Alolan ,  Rapidash ,  Corsola ,  Linoone ,
           Dramanitan ,  Stunfisk]

def howEffective(attacker = Pokemon, defender = Pokemon):
  print(attacker.name + ' vs ' + defender.name + ':')
  if defender.type2 == 'none':
    print('%s: %.2f' % (attacker.type1, attackingDict[attacker.type1][defender.type1]))
  else:
    print('%s: %.2f' % (attacker.type1, attackingDict[attacker.type1][defender.type1] * attackingDict[attacker.type1][defender.type2]))
  if not attacker.type2 == 'none':
    if defender.type2 == 'none':
      print('%s: %.2f' % (attacker.type2, attackingDict[attacker.type2][defender.type1]))
    else:
      print('%s: %.2f' % (attacker.type2, attackingDict[attacker.type2][defender.type1] * attackingDict[attacker.type2][defender.type2]))

class Team:
  def __init__(self, name):
    self.name = name
  members = []

# Computes a list of scores that represents the need for each type
def calcTeamTypeScore(team = Team):
  typeScore = {'bug': 0.0, 'dark': 0.0, 'dragon': 0.0, 'electric': 0.0, 'fairy': 0.0, 
                          'fighting': 0.0, 'fire': 0.0, 'flying': 0.0, 'ghost': 0.0, 'grass': 0.0, 'ground': 0.0, 'ice': 0.0, 'normal': 0.0, 'poison': 0.0, 'psychic': 0.0, 'rock': 0.0, 'steel': 0.0, 'water': 0.0}
  for atkType in attackingDict:
    for defType in attackingDict:
      currScore = attackingDict[atkType][defType]
      # (TEMPORARILY COMMENTED OUT)If a type is super-effective against a type a team member already
      # covers, reduce that type's score
      for i in team.members:
        memberScore1 = attackingDict[i.type1][defType]
        if (i.type1 == atkType):
          typeScore[atkType] -= 1.0
        if (memberScore1 == currScore and currScore == 2.0):
          typeScore[atkType] -= currScore
        if (memberScore1 < 1.0) and (currScore > 1.0):
          typeScore[atkType] += currScore
        if (memberScore1 > 1.0) and (currScore < 1.0):
          typeScore[atkType] -= currScore
        # Type 2 Offense
        if not i.type2 == 'none':
          memberScore2 = attackingDict[i.type2][defType]
          if (i.type2 == atkType):
            typeScore[atkType] -= 1.0
          if (memberScore2 == currScore and currScore == 2.0):
            typeScore[atkType] -= currScore
          if (memberScore1 < 1.0) and (currScore > 1.0):
            typeScore[atkType] += currScore
          if (memberScore1 > 1.0) and (currScore < 1.0):
            typeScore[atkType] -= currScore
        # Calculate defensive scoring
        memberDefScore = attackingDict[atkType][i.type1]
        if not i.type2 == 'none':
            memberDefScore += attackingDict[atkType][i.type2]
        if (memberDefScore < 1.0) and (currScore > 1.0):
          typeScore[defType] -= currScore
        if (memberDefScore > 1.0) and (currScore < 1.0):
          typeScore[defType] += currScore
  # TODO: Lower score if offensive typing is already 
  # covered and increase score if team is weak to 
  return typeScore

def calcBestType(table):
  bestScore = table['bug']
  bestType = 'bug'
  for i in table:
    if table[i] > bestScore:
      bestScore = table[i]
      bestType = i
  return bestType

def calcPokemonScore(table, pokemon = Pokemon):
  if pokemon.type2 == 'none':
    return table[pokemon.type1]
  else:
    return table[pokemon.type1] + table[pokemon.type2]

def calcBestAddition(table, team = Team):
  for i in pokedex:
    if i not in team.members:
      bestScore = calcPokemonScore(table, i)
      bestPokemon = i
      break
  for i in pokedex:
    if i not in team.members:
      currScore = calcPokemonScore(table, i)
      if currScore > bestScore:
        bestScore = currScore
        bestPokemon = i
  return bestPokemon

#howEffective(Rillaboom, Inteleon)
team1 = Team('team1')
team1.members.append(Hydreigon)
team1.members.append(Mawile)
team1.members.append(Rhyperior)
team1.members.append(Salazzle)
team1.members.append(Ludicolo)
table = calcTeamTypeScore(team1)
print(calcTeamTypeScore(team1))
print(calcBestAddition(table, team1).name)
