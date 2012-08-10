def hotelCost(days):
    return 140*days

def planeRideCost(city):
    # Instead of using a conditional chain for this, can you
    # rewrite it using a Python dictionary data structure?
    if city == "Charlotte":
        return 183 
    if city == "Tampa":
        return 220 
    if city == "Pittsburgh": 
        return 222
    if city == "Los Angeles":
        return 475

def rentalCarCost(days):
    cost = days*40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost 
   
# Your indentation levels above differ from the level below.
# While the code will still work, that's bad form.  Pick a level and
# stick to it across all function internals, etc.  I suggest either 2
# or 4 spaces, using actual spaces not TAB characters.

def tripCost(city,days, spendingMoney):
	# The change above will have to be adjusted for here of course.
	return spendingMoney + rentalCarCost(days) + hotelCost(days) + planeRideCost(city)

print tripCost("Pittsburgh",7,600)
