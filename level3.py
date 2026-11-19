stories = ("1.Space Adventure", "2.Cooking Class Disaster")

print("===WELCOME TO MAD LIBS===")
print("Choose a story template.")
print(stories[0],"\n",stories[1])
option = (input("Enter 1 for Space Adventure, 2 for Cooking Class Disaster: "))
if option == "1":
  print("\n--- Enter the following words ---")
  name = input("Enter a hero's name: ")
  place = input("Enter a place: ")
  food = input("Enter a food item: ")
  adjective = input("Enter an adjective: ")
  animal = input("Enter an animal: ")
  verb = input("Enter a verb(action): ")
  noun = input("Enter a noun(object): ")
  plural_noun = input("Enter a plural noun: ")

  story = f"""
  =====================================================
            THE GALACTIC MISSION
  =====================================================
 Captain {name} landed the spaceship on Planet {place}.
 The atmosphere smelled like {food}, and the ground was
 covered in {adjective} rocks.

 Suddenly, a wild {animal} appeared and began to {verb}
 near the command engine! 

 Captain {name} grabbed a nearby {noun} and shouted,
 "Hold on to your {plural_noun}, we are going home!"
  =====================================================

"""
  print(story)
else:
  print("Invalid choice. Please selct again.")