#Pokemon


Flame_Burst ="Flame Burst most commonly refers to a Fire-type move in the Pokémon\
 franchise, or—in literal terms—a sudden flare-up or explosion of fire"
Fly = "The pokemon goes up and attack in the second turn"
Flamethrower = "Flamethrower is a Fire-type Special move in the\
 Pokémon series that scorches a target with intense flames and has \
 a 10 percent chance to inflict a burn."
Swords_Dance = "Swords Dance is a Normal-type status move in Pokémon\
 that raises the user's Attack stat by two stages (sharply boosting it)."
Mega_x = [Flame_Burst, Fly,Flamethrower ,Swords_Dance]
Charizard = [Mega_x, "Mega Y", "Gigantamax"]
Charmander = ["Charmander","Charmeleon",Charizard]


Hydro_Pump = "is a high-power, special Water-type Pokémon move introduced\
 in Generation I that blasts the target with a huge volume of water under extreme pressure."
Mega_Evo= ["Surf",Hydro_Pump,"Flash Cannon","Blizzard"]
Blastoise = [Mega_Evo,"Gigantamax"]
Squirtle = ["Squirtle","Wartortle","Blastoise"]


Growth = " is a status move in Pokémon that boosts the user's Attack\
 and Special Attack stats by one stage each, or by two stages each during harsh sunlight"
Gigantamax = ["Earthquake","Solarbeam","Growth",""]
Venasaur = ["Mega", "Gigantamax"]
Bulbasaur = ["Bulbasaur","Ivysaur","Venasaur"]
Pokemon = {"Frog":Bulbasaur,"Lizard":Charmander,"Turtle":Squirtle}
print(Pokemon["Lizard"][2][0][0])