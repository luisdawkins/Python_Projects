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
