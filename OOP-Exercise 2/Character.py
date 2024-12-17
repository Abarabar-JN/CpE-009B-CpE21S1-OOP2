class Character():
  def __init__(self, username):
    self._username = username
    self._hp = 100
    self._mana = 100
    self._damage = 5
    self._str = 0
    self._vit = 0
    self._int = 0
    self._agi = 0
  def getUsername(self):
   return self._username
  def setUsername(self, new_username):
    self._username = new_username
  def getHp(self):
    return self._hp
  def setHp(self, new_hp):
    self._hp = new_hp
  def getDamage(self):
   return self._damage
  def setDamage(self, new_damage):
    self._damage = new_damage
  def getStr(self):
   return self._str
  def setStr(self, new_str):
    self._str = new_str
  def getVit(self):
   return self._vit
  def setVit(self, new_vit):
   self._vit = new_vit
  def getInt(self):
   return self._int
  def setInt(self, new_int):
   self._int = new_int
  def getAgi(self):
   return self._agi
  def setAgi(self, new_agi):
   self._agi = new_agi
  def reduceHp(self, damage_amount):
   self._hp = self._hp - damage_amount
  def addHp (self, heal_amount):
   self._hp = self._hp + heal_amount

character1 = Character("Your Username")
print(character1._username)
print(character1.getUsername())

