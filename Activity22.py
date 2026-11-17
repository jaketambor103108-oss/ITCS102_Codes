#anime

anime_type = ["Isekai", "Scifi", "Adventure", "Romance"]
anime_title = []

while True:
    ans = input("Do you watch anime (Yes/No)?")

    if ans.lower() == 'yes':
        print("What type of anime do you watch? select from the list")
        for x in anime_type:
            print(x)

        a_type = input("type >")

        title = input("What is the title of the anime? ")
        anime_title.append(title)
        continue
    else:
        print("Thank you!!!")
        break