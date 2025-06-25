countries = ["Turkey", "Russia", "Azerbaijan", "Greece", "Georgia", "Germany", "Switzerland"]
asia = countries[:3] + [countries[4]]
europe = [countries[3]] + countries[5:]

print("Asian countries:", asia)
print("European countries:", europe)

search = input("Which country would you like to check the continent of? ").title()

if search in europe:
    print(f"{search} is a European country.")
elif search in asia:
    print(f"{search} is an Asian country.")
else:
    print(f"{search} is not in the list.")

add_country = input("Would you like to add your own country and classify it? ").lower()

if add_country == "yes":
    user_country = input("Enter the country name: ").title()
    user_continent = input("Select the continent (Asia or Europe): ").lower()

    if user_continent == "europe":
        europe.append(user_country)
    elif user_continent == "asia":
        asia.append(user_country)
else:
    print("Exiting the application...")

remove_country = input("Would you like to remove a country? ").lower()

if remove_country == "yes":
    to_remove = input("Enter the name of the country to remove: ").title()

    if to_remove in europe:
        europe.remove(to_remove)
        print(f"{to_remove} has been removed from the Europe list.")
    elif to_remove in asia:
        asia.remove(to_remove)
        print(f"{to_remove} has been removed from the Asia list.")
    else:
        print(f"{to_remove} was not found in any list.")

show_lists = input("Would you like to see the final state of the lists? ").lower()

if show_lists == "yes":
    print(f"European countries: {europe}")
    print(f"Asian countries: {asia}")
else:
    print("Exiting the application...")
