
def hotel_cost (nights):
    return 140*nights

def plane_ride_cost(city):
    if city == "New York City":
        return 183
    
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh == city":
        return 222
    elif "Melborne == city":
          return 400

def rental_car_cost(days):
            if days>=7:
                return 40* days - 50 
            elif days>=3:
                return 40* days-20
            else: 
                return 40*days
            
def trip_cost(city, Days, night):
                return plane_ride_cost(city) + rental_car_cost(Days) + hotel_cost(night)
            
print("Total Cost of the trip:",trip_cost ("Melborne",7,6))