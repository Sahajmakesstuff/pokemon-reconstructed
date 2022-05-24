strengths = {
    "fire": [
        ["grass","steel","ice"],
        ["water","rock"]
    ], 
    "water": [
        ["fire","rock"],
        ["grass","electric"]
    ],
    "grass": [
        ["water","electric","rock"],
        ["fire","steel","ice"]
    ],
    "rock":[
        ["fire","ice"],
        ["water","grass","steel"]
    ],
    "steel":[
        ["rock","ice"],
        ["fire"]
    ],
    "ice":[
        ["grass"],
        ["fire","rock","steel"]
    ],
    "electric":[
        ["water"],
        ["grass"]
    ],
    "normal":[
        [],
        []
    ]
}

# attackingType = "fire"
# defendingType = "water"

# if defendingType in sw[attackingType][0]:
#     # more damage
# elif defendingType in sw[attackingType][1]:
#     #less damage
# else:
#     #neutral damage
    