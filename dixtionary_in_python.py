#create dictionary 
car= {"brand":"renault", "model":"megane", "year":2017}
car_2 = dict(brand="dacia", model="logan", year=2022)
print(car["brand"])
print(car.get("brand"))
print(car.keys())
print(car.values())
print(car.items())
car["model"] = "scenic"
print(car.values())
car["brand"]= "fiat"
car["model"]= "megane"
car["year"] = 2020
print(car.items())
car= {"brand":"renault", "model":"megane", "year":2017}
car_2 = dict(brand="dacia", model="logan", year=2022)
car.update(car_2)
print(car)