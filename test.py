mantees = [ {'name': 'Geeks', 'age': 4, 'class': 'Geeks4'}, {'name': 'Geekos', 'age': 7, 'class': 'Geeks6'}, {'name': 'Geekosy', 'age': 9, 'class': 'Geeks6'} ]

def example4 (mantees):
    oldest_mantees = 'No mantee here!'

    for mantee1 in mantees:
        for mantee2 in mantees:
            if mantee1['age'] < mantee2['age']:
                oldest_mantees = mantee2['name']
            
            else:
                oldest_mantees = mantee1['name']

    return oldest_mantees 
print (example4(mantees))

