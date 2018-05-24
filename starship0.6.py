
import time
import random
import os
import sys
import math
from math import atan2,degrees

def exiting():
	print(       "Exiting the system. Live long and prosper!")
	sys.exit()

def gameover():
	print(       "Game over.")
	sys.exit()

class Ship:
	def __init__(self, name, registry, type):
		self.captainname = 0
		self.name = name
		self.registry = registry
		self.type = type
		self.attack = 100
		self.defense = 100
		self.speed = 100
		self.warp = 6
		self.validwarp = ["1","2","3","4","5"]
		self.coord = [0,0]
		self.warpgrid = [426,518]
		self.homegrid = [426,518]
		self.experience = 2000
		self.inventory = ["Crate of food","Emergency rations","Small arms","Spare parts","Holodeck"]
		self.level = 1
		self.refined = 2500
		self.nextlevel = (2500)
		self.items = 0
		self.sheilds = 100
		self.hull = 100
		self.prime = Weapon("Photon Torpedo","Launcher",60)
		self.sec = Weapon("Phaser","Cannon",40)

	def displayloc(self):
		print("       Location = %s" % str(self.coord))

	def primary(self):
		print("       Primary weapon slot: = %s" % self.prime.name,self.prime.type,", damage: ",self.prime.damage)

	def displaywarploc(self):
		print("       New warp location = %s" % str(self.warpgrid))

	def distancehome(self):
		x = float(self.homegrid[1]-self.warpgrid[1])
		y = float(self.homegrid[0]-self.warpgrid[0])
		distance = math.sqrt(x**2+y**2) * 10
		print("       You are ",round(distance,2),"lightyears away.")

	def displaylevel(self):
		print("       Level is: %d" % self.level)

	def status(self):
		str(self.displayShip())
		str(self.displayStats())
		str(self.degrees())
		str(self.displaylevel())
		str(self.distancehome())
		str(self.chkf())

	def degrees(self):
		x = float(self.homegrid[1]-self.warpgrid[1])
		y = float(self.homegrid[0]-self.warpgrid[0])
		bearing = degrees(atan2(y,x))
		if bearing >= 0:
			print("       Bearing to home base is",round(bearing,2),"degrees.")
		else:
			bearingm = float(bearing + 360)
			print("       Bearing to home base is ",round(bearingm,2),"degrees.")

	def scan(self):
		print("       Initiating scan.")
		b = self.items
		if self.items >= 1:
			print("       Found %d counts of deuterium." % self.items)
			m = input("       Gather materials? y or n. ")
			if m.lower() == "y":
				self.mine()
				print("       20kg times %d added to cargo hold." % b)
			else:
				pass
		else:
			print("       No items in sector.")

	def chkf(self):
		print("       You have %d kg refined deuterium." % self.refined)

	def mine(self):
		num = self.items
		ref = input("       Mine all? y or n. ")
		if ref.lower() == "y":
			self.items -= self.items
			self.inventory += num * ["20kg deuterium"]
			self.items = 0
		else:
			pass

	def fuelref(self):
		num = int(self.inventory.count("20kg deuterium"))
		if "20kg deuterium" in self.inventory:
			print("       You have %d counts of gas." % num)
			ref = input("       Refine all? y or n: ")
			if ref == "y":
				self.refined += 500 * num
				input("       Refining...")
				print("       You now have %d kg refined deuterium." % self.refined)
				for i in range(num):
					self.inventory.remove("20kg deuterium")
			else:
				pass
		else:
			print("       Not enough raw fuel.")

	def levelup(self):
		self.level += 1
		self.nextlevel *= 1.25
		if self.warp <= 9:
			self.warp += 1
		self.attack *= 1.1
		self.defense *= 1.1
		self.speed *= 1.5
		self.experience *= 0
		warpp = str(self.warp - 1)
		self.validwarp.append(warpp)
		input("       Level up!")
		print("\n       You have reached level %d." % self.level)
		print("       Your attack is now %d.\n       Your defense is now %d.\n       Your speed is now %d.\n       Max warp: %d." % (self.attack,self.defense,self.speed,(int(self.warp)-1)))

	def checklevel(self):
		print("       You are currently at level %d" % self.level)
		print("       Current: %d" % self.experience)
		print("       Next lv: %d" % self.nextlevel)

	def chekin(self):
		print("       Inventory:")
		for item in self.inventory:
			print("      ",item)

	def move(self):
		validspeed = ["0","1","2","3","4","5","6","7","8","9"]
		while True:
			speed = input("       set impulse power, 1-9. ")
			if speed == "0":
				break
			elif speed in validspeed:
				query = input("       Move ship north, south, east, or west? ")
				en = random.randint(1,9)
				if query.lower() == "n":
					self.coord[1] += int(speed)
					print("       moved north.")
					print("       You are at %s" % str(self.coord))
					break
				elif query.lower() == "s":
					self.coord[1] -= int(speed)
					print("       moved south.")
					print("       You are at %s" % str(self.coord))
					break
				elif query.lower() == "e":
					self.coord[0] += int(speed)
					print("       moved east.")
					print("       You are at %s" % str(self.coord))
					break
				elif query.lower() == "w":
					self.coord[0] -= int(speed)
					print("       moved west.")
					print("       You are at %s" % str(self.coord))
					break
				else:
					print("       error")
			else:
				print("       error, set impulse 1-9.")

	def displayStats(self):
		print("       Total attack = %d" % self.attack)
		print("       Total defense = %d" % self.defense)
		print("       Total speed = %d" % self.speed)
		print("       Total warp = warp factor %s" % (int(self.warp)-1))

	def displayShip(self):
		print("       Name: U.S.S. %s, Registry: N.C.C. %s, Type: %s" % (self.name,self.registry,self.type))

	def regensh(self):
		print("       Shieilds at %d" % self.sheilds)
		re = input("       regenerate?")
		if re == "y":
			input("       Regenerating shield...")
			input("       ...")
			input("       ...")
			input("       Done.")
			self.sheilds = 100
		else:
			pass

	def starfleet(self):
		input("       Contacting starfleet command. Please wait.")
		input("       ..")
		input("       communications established.")

		if self.level >= 2:
			print("       Admiral: 'Captain, congratulations on reaching this stage.")
			print("      ",mission1.name,mission1.message,"     ",mission1.sector)


		else:
			print("       Admiral: 'Captain! Your level is not high enough.")

	def warpspeed(self):
		if self.refined >= 500:
			wspeed = input("       Set warp factor, 0-max(%d). " % ((self.warp)-1))
			if wspeed in self.validwarp:
				print("       Tuning warp intermix ratio for warp %d." % int(wspeed))
				query = input("       Warp to sector north, south, east, or west?")
				if query.lower() == "n":
					self.warpgrid[1] += int(wspeed)
					print("       Warped north.")
					self.coord = [5,5]
				elif query.lower() == "s":
					self.warpgrid[1] -= int(wspeed)
					print("       Warped south.")
					self.coord = [5,5]
				elif query.lower() == "e":
					self.warpgrid[0] += int(wspeed)
					print("       Warped east.")
					self.coord = [5,5]
				elif query.lower() == "w":
					self.warpgrid[0] -= int(wspeed)
					print("       Warped west.")
					self.coord = [5,5]
				else:
					print("       error")
					self.warpspeed()
				self.displaywarploc()
				self.refined -= 500
				a = random.randint(0,5)
				self.items = 0
				self.items += a
				self.encounter()
			else:
				print("       error.")
				q = input("       Quit, or Warp?")
				if q.lower() == "w":
					self.warpspeed()
				else:
					pass
		else:
			print("       not enough fuel.")

	def encounter(self):
		chance = random.randint(0,4)
		skirm2 = Alien("War Frigate","Romulan")
		skirm1 = Alien("Kvort","Klingon")
		safe = Alien("cruiser","Vulcan")
		alienw1 = Weapon("Disruptor","Cannon",30)
		alienw2 = Weapon("Polaron Disruptor","Energy pulse,",60)

		if chance == 3:
			input("       Tactical: 'Sir, We have encountered an alien ship.'\n")
			hostile = random.randint(1,99)
			if hostile % 2 == 0:
				print("       They are non-hostile,sir.")
				print("       Vessel is a",safe.race,safe.name,"class")
				pass
			else:
				chance2 = random.randint(0,2)
				if chance2 == 1:
					skirm = skirm1
					alienw = alienw1
					skirm.sec = alienw1
					skirm.prime = alienw1
					skirm.level = self.level
				else:
					skirm = skirm2
					alienw = alienw2
					skirm.sec = alienw2
					skirm.prime = alienw2
					skirm.level = self.level
				print("       Ship is hostile, sir, a",skirm.race,skirm.name,"class")
				print("       Weapons are",alienw.name,alienw.type,"with damage",alienw.damage)
				x = float(skirm.coord[0]-self.coord[0])
				y = float(skirm.coord[1]-self.coord[1])
				distance = math.sqrt(x**2+y**2) * 1000.00
				bearing = degrees(atan2(y,x))
				print("       You are",round(distance,2),"km away.")
				if bearing >= 0:
					print("       The bogey is bearing",round(bearing,2),"degrees.")
				else:
					bearingm = float(bearing + 360)
					print("       The bogey is bearing",round(bearingm,2),"degrees.")
				f = input("       fight?")

				if f.lower() == "n":
					usr.move()
				if f.lower() == "y":
					input("       You are fighting enemy spacecraft.\n       sheilds and weapons to full.")
					while True:
						if self.hull > 0:
							query2 = input("       (pha)sers,(pho)tons,(b)oth?")
							if query2.lower() == "pha":
								print("       Firing phasers")
								if skirm.sheilds <= 0:
									skirm.hull -= self.sec.damage

									if skirm.hull <= 0:
										break
									else:
										print("       Enemy hull down to %d" % skirm.hull)
								elif skirm.sheilds > 0:
									skirm.sheilds -= self.sec.damage
									print("       Their sheilds are down to %d" % skirm.sheilds)
							elif query2.lower() == "pho":
								print("       Firing photons")
								if skirm.sheilds <= 0:
									skirm.hull -= self.prime.damage

									if skirm.hull <= 0:
										break
									else:
										print("       Enemy hull down to %d" % skirm.hull)
								elif skirm.sheilds > 0:
									skirm.sheilds -= self.prime.damage
									print("       Their sheilds are down to %d" % skirm.sheilds)
							elif query2.lower() == "b":
								print("       Firing both")
								if skirm.sheilds <= 0:
									skirm.hull -= self.sec.damage
									skirm.hull -= self.prime.damage
									if skirm.hull <= 0:
										("       You won.")
										break
									else:
										print("       Enemy hull down to %d" % skirm.hull)
										continue
								elif skirm.sheilds > 0:
									skirm.sheilds -= self.sec.damage
									skirm.sheilds -= self.prime.damage
									print("       Enemy sheilds down to %d" % skirm.sheilds)

							else:
								print("       We didnt attack!")
							input("       Enemy attacks!")
							while True:
								ranroll = random.randint(1,99)
								if ranroll % 2 == 0:
									print("       Enemy firing primaries!")
									if self.sheilds > 0:
										self.sheilds -= skirm.prime.damage
										print("       Sheilds down to %d" % self.sheilds)


									elif self.sheilds <= 0:
										self.hull -= skirm.prime.damage
										print("       Hull down to %d" % self.hull)
										if self.hull <= 0:
											print("       You were destroyed!")
											gameover()
										break
									break
								else:
									print("       Enemy firing secondaries!")
									if self.sheilds > 0:
										self.sheilds -= skirm.sec.damage
										print("       Sheilds down to %d" % self.sheilds)

									elif self.sheilds <= 0:
										self.hull -= skirm.sec.damage
										print("       Hull down to %d" % self.hull)
										if self.hull <= 0:
											print("       You were destroyed!")
											gameover()
										break
									break
					print("       You Win.")
					exp = skirm.level*500
					print("       Gain:",exp,"points\n")
					self.experience += skirm.level*500
					if self.experience >= self.nextlevel:
							self.levelup()
				else:
					print("       Not a valid input.")
					usr.move()
class Mission:
	def __init__(self,name,message,sector):
		self.name = name
		self.message = message
		self.sector = sector


mish1 = ("""
       Captain, congratulations on reaching this stage. You are now at
       a clearance level high enough to receive this breifing. We have
       received a strange reading from following sector:
""")

mission1 = Mission("Investigate anomily.",mish1,"446,538")


class Weapon:
	def __init__(self, name, type, damage):
		self.name = name
		self.type = type
		self.damage = int(damage)


class Alien:
	def __init__(self, name, race):
		self.name = name
		self.race = race
		self.attack = 90*1.1
		self.defence = 90*1.1
		self.prime = 0
		self.sec = 0
#		self.prime = Weapon("Energy","Projectile",30)
#		self.sec = Weapon("Energy","Beam",20)
		self.sheilds = 100
		self.hull = 100
		self.speed = 98
		self.level = 1
		self.coord =[random.randint(1,20),random.randint(1,20)]


input("\n       Welcome to Warp Speed!\n       This is version 0.5...")

input("""
							by:   speedbird2992 2018
							sto:      trek47_voyager
                                     .                                 ............
                        *                                         .,/(#%%%######*
                                                           .,/(##(/****,*,,,,,,,**
                                                 .     ,/#(/***,,,***,,,,,,,,,,*/.
    *                                             .,**,,,,,***,,,*,,,,,,,,,,,**,
                                     *         ,*,,...,*,,,,,,,,,,*,,,,,*,,**.
              .                            .,,.....,,*/*,.,,,,,,,,,,,***,,.
                                         ,,,,**////(/.,....,,,*,,*****,.
                              .,,*//*,,,,... ...........,,,,,******.
               ..,*/(##/*,..         .... .. ............,,,***.
 (*,,**///**,...                    .... .., ............,/#*
                                   ..        ........,,,,,(%#, ,***
                                      ...  ..     ..,#&@%.,##(**,*.
              warp                             .... .(*..,,...*(/**,.
               speed                         ,*/,     .*,,,****/*
                                 .          .,.,*   ........,..
                                           .,..,.  ........
                                             . ....*(

     The United Federation of Planets is at war with the klingon empire! Patrol 
     sectors of deep space and keep the enemy occupied as starfleet plans for a 
     greater mission... to boldly go where no one has gone before.
""")


tt_str = input('     What is the name of your starship?... ')

a = tt_str.title()

valid = ['sci','tact','eng']

smenu = """
            ---------------------------
           |'sci'  for     science ship|        Choose your class of vessel
           |'eng'  for engineering ship|        Ships will develop powerful
           |'tact' for    tactical ship|        weapons based on class type
            ---------------------------
   """

print(smenu)

while True:
	c = input("       ")
	if c in valid:
		break
	else:
		print("       Please enter a valid option.")
		c
if c == "eng":
	d = "Engineering"
elif c == "tact":
	d = "Tactical"
elif c == "sci":
	d = "Science"

if a.lower() == "enterprise":
	input("\n       Welcome, Captain Kirk!\n       The Enterprise's 5 year mission: to explore strange new worlds.")
	b = 1701
	usr = Ship(a,b,d)
	usr.captainname = "Kirk"
else:
	capt = input("       What is your name?")
	captn = capt.title()
	b = random.randint(29999,59999)
	input("\n       Welcome, Captain %s!\n       The %s's mission: to defend and protect the values of peace." % (captn,a))
	usr = Ship(a,b,d)
	usr.captainname = captn

print(" ")
input("       Explore space, gather fuel, and level up.\n       When you reach level 3, contact starfleet.")
print(" ")
usr.displayShip()
print("       Captain in command: %s" % usr.captainname)
usr.displayStats()
usr.displayloc()
usr.displaywarploc()
usr.primary()

menuhelp = """
       .=======================================================================.
      | (  M   )    engage impulse engines || ( Lev )     current level and xp  |
      | (  W   )    warp to nearby sectors || (  F  )  refined warp fuel check  |
      | ( Deg  )      bearing to home base || (  I  )      check fuel quantity  |
      | (  D   )   distance from home base || (  L  )     galactic coordinates  |
      | (Status)        full status report || (  H  )          list menu items  |
      | (  R   ) refine raw deuterium fuel || (  SS )       regenerate shields  |
      | (  S   )     scan for raw hydrogen || ( End )            back to shell  |
      | (  C   )         contact starfleet || ( ) ( )                           |
       '======================================================================='
"""
time.sleep(3)
print(menuhelp)

while True:
	choice = input("       What would you like to do?\n       ")
	if choice.lower() == "m":
		usr.move()
	elif choice.lower() == "deg":
		usr.degrees()
	elif choice.lower() == "ss":
		usr.regensh()
	elif choice.lower() == "lev":
		usr.checklevel()
	elif choice.lower() == "status":
		usr.status()
	elif choice.lower() == "d":
		usr.distancehome()
	elif choice.lower() == "r":
		usr.fuelref()
	elif choice.lower() == "l":
		usr.displaywarploc()
	elif choice.lower() == "f":
		usr.chkf()
	elif choice.lower() == "h":
		print(menuhelp)
	elif choice.lower() == "i":
		usr.chekin()
	elif choice.lower() == "s":
		usr.scan()
	elif choice.lower() == "end":
		exiting()
	elif choice.lower() == "w":
		usr.warpspeed()
	elif choice.lower() == "c":
		usr.starfleet()



