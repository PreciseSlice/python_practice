def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == 'Charlotte':
    return 183
  elif city == 'Tampa':
    return 220
  elif city == 'Pittsburgh':
  	return 222
  else:
  	return 475
  
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days > 2 and days < 7:
    cost -= 20
  return cost
 
def trip_cost(city, days, spending_money):
  cost = 0
  cost += spending_money
  cost += rental_car_cost(days)
  cost += hotel_cost(days -1)
  cost += plane_ride_cost(city)
  
  return "$%s" % (cost)

print(trip_cost("Lost Angeles", 5, 600))
