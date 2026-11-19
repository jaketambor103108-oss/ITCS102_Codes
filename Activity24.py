#dictionary
#key, value

Pokemon = {"Frog":"Bulbasaur","Lizard":"Charmander","Turtle":"Squirtle","Rat":"Pikachu","Puppy":"Eevee"}

print(Pokemon["Lizard"])

#traversing dictionary

for x, y in Pokemon.items():
    print("Key is ",x," The value is ", y)