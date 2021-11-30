travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(x, y, z):
    new_cunt = {}
    new_cunt["country"] = x
    new_cunt["visits"] = y
    new_cunt["cities"] = z
    # new_cunt = {
    #     "country": x,
    #     "visits": y,
    #     "cities": z
    # }
    travel_log.append(new_cunt)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
