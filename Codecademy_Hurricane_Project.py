#!/usr/bin/env python
# coding: utf-8

# In[36]:


# %load C:\Matthew\Documents\script.py
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_list(lst):
    updated_list = []
    for item in lst:
        if 'B' in item:
            updated_list.append(float(item[0:-1])*1000000000)
        if 'M' in item:
            updated_list.append(float(item[0:-1])*1000000)
        else:
            updated_list.append(item)
    return updated_list  

update_list(damages);

# write your construct hurricane dictionary function here:

hurricanes = {}
for i in range(len(names)):
    hurricanes[names[i]] = {"Name":names[i], "Month": months[i], "Year":years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected":areas_affected[i], "Damage":damages[i], "Deaths": deaths[i]}

# write your construct hurricane by year dictionary function here:

hurricane_by_year = {}

for hurricane in hurricanes.values():
    current_year = hurricane["Year"]
    hurricane_by_year[current_year] = hurricane

# write your count affected areas function here:

def count_areas(dictionary):
    affected_areas = {}
    for cane in dictionary.values():
        count = 0
        for place in cane["Areas Affected"]:
            count += 1
            affected_areas[place] = count
    return affected_areas

hurricane_count = count_areas(hurricanes)

# write your find most affected area function here:

max_area_count = 0
most_affected_area = ""
for i in range(len(hurricane_count)):
    area_counts = list(hurricane_count.values())
    area = list(hurricane_count.keys())
    if area_counts[i] > max_area_count:
        max_area_count = area_counts[i]
        most_affected_area = area[i]

    


# write your greatest number of deaths function here:

max_deaths = 0
most_death_hurricane = ""
for hurricane in hurricanes.values():
    if hurricane["Deaths"] > max_deaths:
        max_deaths = hurricane["Deaths"]
        most_death_hurricane = hurricane["Name"]





# write your catgeorize by mortality function here:
zero_list = []
one_list = []
two_list = []
three_list = []
four_list = []
for hurricane in hurricanes.values():
    if hurricane["Deaths"] > 10000:
        four_list.append(hurricane)
    elif hurricane["Deaths"] > 1000:
        three_list.append(hurricane)
    elif hurricane["Deaths"] > 500:
        two_list.append(hurricane)
    elif hurricane["Deaths"] > 100:
        one_list.append(hurricane)
    elif hurricane["Deaths"] >= 0:
        zero_list.append(hurricane)
mortality_list = {0:one_list, 1:one_list, 2:two_list, 3:three_list, 4:four_list}


# write your greatest damage function here:

max_damage = 0
most_damage_hurricane = ""
for hurricane in hurricanes.values():
    hurricane_value = 0
    if 'M' in hurricane["Damage"]:
        hurricane_value = float(hurricane["Damage"][0:-1])*1000000
    if 'B' in hurricane["Damage"]:
        hurricane_value = float(hurricane["Damage"][0:-1])*1000000000
    if hurricane_value > max_damage:
        max_damage = hurricane_value
        most_damage_hurricane =  hurricane["Name"]

# write your catgeorize by damage function here:
damage_zero_list = []
damage_one_list = []
damage_two_list = []
damage_three_list = []
damage_four_list = []
for hurricane in hurricanes.values():
    hurricane_value = -1
    if 'M' in hurricane["Damage"]:
        hurricane_value = float(hurricane["Damage"][0:-1])*1000000
    if 'B' in hurricane["Damage"]:
        hurricane_value = float(hurricane["Damage"][0:-1])*1000000000
    if hurricane_value > 50000000000:
        damage_four_list.append(hurricane)
    elif hurricane_value > 10000000000:
        damage_three_list.append(hurricane)
    elif hurricane_value > 1000000000:
        damage_two_list.append(hurricane)
    elif hurricane_value > 100000000:
        damage_one_list.append(hurricane)
    elif hurricane_value >= 0:
        damage_zero_list.append(hurricane)
damage_scale = {0:damage_zero_list, 1:damage_one_list, 2:damage_two_list, 3:damage_three_list, 4:damage_four_list}
print(damage_scale)


# In[ ]:




