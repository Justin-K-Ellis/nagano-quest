# NAGANO QUEST - Created by Justin K. Ellis

from sys import exit

oneOrTwo = "Choose 1 or 2 > "

def welcomeToNagano():
	print "Welcome to Nagano, %s, the roof of Japan!" % name
	print "You can visit one of these four locations!"
	print "1. Nagano City"
	print "2. Ueda"
	print "3. Matsumoto"
	print "4. Da souf\n"

	while True:
		choice = raw_input("Choose 1, 2, 3, or 4 > ")

		if choice == "1":
			naganoCity()
		elif choice == "2":
			ueda()
		elif choice == "3":
			matsumoto()
		elif choice == "4":
			daSouf()
		else:
			print "wut"


def naganoCity():
	print "Welcome to Nagano City, the capital of the prefecture."
	print "There's a lot to do here, in this bustling metropolis of the inaka,"
	print "but in my experience, the top choices are:\n"
	print "1. Zenkouji, the largest temple in Nagano, or"
	print "2. Starbucks\n"

	while True:
		choiceNagano = raw_input(oneOrTwo)

		if choiceNagano == "1":
			zenkouji()
		elif choiceNagano == "2":
			starbucks()
		else:
			print "wut"


def ueda():
	print "Welcome to Ueda, home of the famous samurai, Sanada Yukimura."
	print "To be honest, there isn't that much to do here.\n"
	print "I'd suggest:"
	print "1. Ueda Castle, the former fortress of Sanada."
	print "2. A bar we'll call 'KK'.\n"

	while True:
		choiceUeda = raw_input(oneOrTwo)

		if choiceUeda == "1":
			uedaCastle()
		elif choiceUeda == "2":
			kK()
		else:
			print "wut"


def matsumoto():
	print "Here we are in Matsumoto, the jewel of Nagano!"
	print "Matsumoto is by far the most cultured city in the prefecture,"
	print "So I can easily recommend either,\n"
	print "1. The castle, or"
	print "2. The city museum.\n"

	while True:
		choiceMatsumoto = raw_input(oneOrTwo)

		if choiceMatsumoto == "1":
			matsumotoCastle()
		elif choiceMatsumoto == "2":
			museum()
		else:
			print "wut"


def daSouf():
	print "Not much is known about southern Nagano."
	print "Mostly legends, really."
	print "What has been confirmed about this expanse of"
	print "forests and mountains is the existence of\n"
	print "1. Kiso Valley"
	print "2. Iida or Iina\n"

	while True:
		choiceDasouf = raw_input(oneOrTwo)

		if choiceDasouf == "1":
			kiso()
		elif choiceDasouf == "2":
			iidaIina()
		else:
			print "wut"


def zenkouji():
	print "Ah, Zenkouji."
	print "A massive Buddhist temple complex dominates the top of a"
	print "hill in the middle of the city. Here you can either progress on"
	print "path to enlightenment by traveling beneath the temple in a pitch"
	print "black tunnel, or get ice cream. Yes, the temple has an ice cream"
	print "shop. Really."
	print "So which will it be?\n"
	print "1. The tunnel"
	print "2. Ice cream!\n"

	while True:
		choiceZenkouji = raw_input(oneOrTwo)

		if choiceZenkouji == "1":
			print "You remove your shoes and enter the central temple (after buying a ticket!). From there you"
			print "decend into the tunnel beneath the alter. It is a winding path, cast in perfect, primordial darkness."
			print "Yet the story goes that somewhere in the darkness is a room where the first image of the Buddha"
			print "brought to Japan is kept. You lightly drag your fingers across the right wall until"
			print "Suddenly! A bronze handle!\n"
			goodEnd("You found enlightenment!\n")
		elif choiceZenkouji == "2":
			print "Well, the ice cream was good, but really, you could have gotten that anywhere."
			badEnd("Seems like kind of a waste.\n")
		else:
			print "wut"


def starbucks():
	print "Well, it's Starbucks. Same as any other Starbucks in Japan,"
	print "same as any Starbucks anywhere. It's fine though, no matter"
	print "what those snobs say. Since you apparently have some free time,"
	print "you can either:\n"
	print "1. Space out, or"
	print "2. Play a game called 'Nagano Quest'\n"
	
	while True:
		choiceStarbucks = raw_input(oneOrTwo)

		if choiceStarbucks == "1":
			print "........."
			badEnd("Well, that was a waste of your vacation.\n")
		elif choiceStarbucks == "2":
			welcomeToNagano()
		else:
			print "wut"


def uedaCastle():
	print "Here we find ourselves at the beautiful and expansive Ueda Castle!"
	print "(Shame the cherry blossoms aren't in season.)"
	print "What do you mean 'Where's the castle'?"
	print "Oh, right. The central keep was destroyed long ago...."
	print "If you want to see a traditional castle with the tower and all"
	print "You'll have to go to Matsumoto. Otherwise we can just hang out"
	print "in Ueda and hit that bar. What do you say?\n"
	print "1. Go to Matsumoto."
	print "2. Go that bar.\n"

	while True:
		choiceUedaCastle = raw_input(oneOrTwo)

		if choiceUedaCastle == "1":
			matsumoto()
		elif choiceUedaCastle == "2":
			kK()
		else:
			print "wut"


def kK():
	print "You wait around until eight at night before heading to a bar we'll call 'KK'."
	print "You step into the dimly lit bar, a decent looking place, but clearly something"
	print "of a dive. There doesn't seem to be anyone here yet, save for the bartender."
	print "He is a meaty Japanese man sporting a mustache. He looks up from his smartphone"
	print "and grunts at you. What do you do?\n"
	print "1. Leave."
	print "2. Stay and talk to the man.\n"

	while True:
		choiceKK = raw_input(oneOrTwo)

		if choiceKK == "1":
			print "You turn around and head back out the door. You don't really know any other places"
			print "though, so you go back to your hotel.\n"
			badEnd("What an exciting night out!\n")
		elif choiceKK == "2":
			print "You decided to stay and start talking to the gruff bartender."
			print "He asks to take your order, but you realize you don't have much"
			print "cash on you. Lucky for you, he offers you '%s prices' and gets you" % name
			print "your drinks for cheap and you get hammered. He seems to take a"
			print "perverse pleasure in seeing you get wasted.\n"
			badEnd("You wake up the next morning with a terrible hangover.\n")
		else:
			print "wut"


def matsumotoCastle():
	print "Here we are at Matsumoto Castle, the finest castle in the land!"
	print "It's dark form rises from its pedestal of stone, towering over"
	print "the shallow moat, its image reflected in the water."
	print "Now what?\n"
	print "1. Go to the station area."
	print "2. Visit the museum.\n"

	while True:
		choiceMatsumotoCastle = raw_input(oneOrTwo)

		if choiceMatsumotoCastle == "1":
			print "You head back down to the station area. You can either wait"
			print "around for night and go out, or go back to Nagano City."
			print "What do you do?\n"
			print "1. Stay out."
			print "2. Go to Nagano City.\n"

			choiceStation = raw_input(oneOrTwo)

			if choiceStation == "1":
				stayOut()
			elif choiceStation == "2":
				naganoCity()
			else:
				print "wut"

		elif choiceMatsumotoCastle == "2":
			museum()
		else:
			print "wut"


def museum():
	print "You arrive at Matsumoto City Museum."
	print "Outside there are huge, colorful sculptures depicting polka dotted tulips."
	print "Don't see that every day."
	print "You buy your ticket and see a variety of fine arts in the small but"
	print "tasteful museum, including more polka dots that you ever thought you"
	print "would see in your entire life.\n"
	goodEnd("You are now more cultured.\n")


def stayOut():
	print "You decide to spend a night out on the town!"
	print "You decided to hit the takoyaki standing bar for a first round,"
	print "but this 'first round' turns into five or six rounds after meeting a"
	print "group of random Japanese people who ended up pulling you off to"
	print "drunken karaoke.\n"
	goodEnd("Now that's an authentic Japanese experience.\n")


def kiso():
	print "So here we are, the Kiso Valley!"
	print "A cool mountain river cuts between shear forest covered mountains,"
	print "and the small towns that line the valley seem to be little more than"
	print "decoration. Winding through the mountain paths is the Nakasendou, the"
	print "ancient path from medieval Tokyo to Kyoto.\n"
	goodEnd("Hey, that wasn't so bad.\n")


def iidaIina():
	print "Here you are in either Iida or Iina."
	print "(I honestly can't remember which, it's all the same to me.)"
	print "There's nothing to do down here, so you should probably"
	print "reevaluate your decisions on this little adventure.\n"
	print "1. Reevaluate.\n"

	while True:
		choiceIidaIina = raw_input("There really is only one choice to make.\n")

		if choiceIidaIina == "1":
			welcomeToNagano()
		else:
			badEnd("I said there was only one choice.\n")


def goodEnd(why):
	print why, "Well done, %s." % name
	exit(0)

def badEnd(why):
	print why, "Too bad, %s." % name
	exit(0)

print "Welcome to NAGANO QUEST!"
print "Begin your journey into Shinanokuni."
print "First, what's your name?"
name = raw_input("> ")

welcomeToNagano()