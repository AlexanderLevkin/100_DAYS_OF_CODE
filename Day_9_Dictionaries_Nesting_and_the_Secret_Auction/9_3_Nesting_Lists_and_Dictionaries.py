# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a Lists in a Dictionary
# travel_log = {
#     "France ": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# Dictionary in Dictionary
travel = {"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": {"Berlin": 12,
                                                                                             "Hamburg": 10,
                                                                                             "Stuttgart": 9}},
          "France": {"cities_visited": ["Paris", "Lille", "Dijon"]}
          }

print(travel)

# Nesting Dictionary in a list
travel = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
print(travel[0])
