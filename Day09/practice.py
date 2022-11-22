prog_01={
    "Name":"Mehul",
    "PRN":"119A3006"
}

print(prog_01["Name"])

#Adding new items


prog_01["city"]="Akola"

print(prog_01)

#Wipe out a dictionary

# prog_01={}

# print(prog_01)

#IF we loop thru the dictionary we will get only keys and not the values


#Nesting Dictionary

# Nesting Dictionary with a list


travel_log={
    "France":["Paris","Liitle","Dijon"],
    "Germany":["Berlin","Hamburg"]
}

travel_log1={
    "France":{"Cities_Visited":["Paris","Liitle","Dijon"]},
}