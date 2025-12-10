#Simple looking class
class Restaurant():
  name = ""
  category = ""
  rating = ""
  delivery = ""

#Create instance of the restaurant class
bobs_burgers = Restaurant()

#Assign values to the following attributes
bobs_burgers.name = "Bob\'s Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))

# Write code below 💖
class City:
    #__init__ and the self argument are used to initialize classes and make assigning instance variables more efficient
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

Home = City("Troy", "United States", 70000, ["Somerset Mall", "Big Beaver"])
Travel = City("Chicago", "United States", 3000000, ["Al Capone's House", "The Bean", "Pizza Parlor"])

print(vars(Home))
print(vars(Travel))
