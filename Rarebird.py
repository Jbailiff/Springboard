# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:19:03 2020

@author: jbrav
"""

rarebirds = {
    'gold-crested toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True},
    'pearlescent kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': True},
    'four-metre hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False},
    'giant eagle' : {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True},
    'ancient vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False},
}
codes = { 
    '001' : 0,
    '010' : 1,
    '011' : 2,
    '100' : 3,
    '101' : 4,
    '110' : 5,
    '111' : 6,
}
for k in rarebirds:
    rarebirds[k]['seen'] = False
birdlocation = ['In the canopy directly above our heads.','Between my 6 and 9 o’clock above.','Between my 9 and 12 o’clock above.','Between my 12 and 3 o’clock above.','Between my 3 and 6 o’clock above.','In a nest on the ground.','Right behind you.']
actions = ['Back Away', 'Cover our Heads', 'Take a Photograph']

for k, v in rarebirds.items():
    if v['Aggressive'] == True:
        print(k) 
print(actions[1])

for k, v in rarebirds.items():
    if v['Endangered'] == True: 
        print(k)
print(actions[0])

for k, v in codes.items():
    print(str(k) + ' ' + 'Means ' + birdlocation[v]) 
    
encounter = False
while encounter != True:
    sighting = input('What do you see?').lower()
    rarebirdsList = list(rarebirds.keys())

    if sighting in rarebirdsList:
        print("this is one of the birds we're looking for!")
        encounter = True
    else:
        print("that's not one of the birds we're looking for.")
        continue
    
    code = str(input('Where do you see it? Input the correct code'))
    location = birdlocation[(codes[code])]
    print("So you have seen a", sighting, location, "My goodness.")

    s = rarebirds[sighting]['Aggressive']
    e = rarebirds[sighting]['Endangered']

    if s == True:
        print('Aggressive! We need to ' + actions[0] + ", " + actions[1] + " and " + actions[2] + ' of the ' + sighting + ' at ' + location)

    elif e == True:
        print('Endangered! We need to ' + actions[0] + " and " + actions[2] + 'of the ' + sighting + ' at ' + location)
    else: 
            print('we need to ' + actions[2] + ' of the '  + sighting + ' at ' + location)
    



#print(rarebirdslist)
   



   



