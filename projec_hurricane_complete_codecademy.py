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

conversion = {"M": 1000000, "B": 1000000000}

def convert(list1, constant, dictionary1):
    temp = []
    for datum in list1:
        if datum == constant:
            temp.append(datum)
        else:
            for key in dictionary1.keys():
                if datum[-1] == key:
                    temp.append(float(datum.strip(datum[-1])) * dictionary1[key])
    return temp

damages_converted = convert(damages, "Damages not recorded", conversion)

# write your construct hurricane dictionary function here:

def hurricane_dictionary(name, month, year, wind, area, damage, death):
    temp = {}
    for index in range(len(name)):
        temp.update({name[index]: {"Name": name[index], "Month": month[index], "Year": year[index], "Max Sustained Wind": wind[index], "Areas Affected": area[index], "Damage": damage[index], "Death": death[index]}})
    return temp

hurricane_dictionary_by_name = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)

# write your construct hurricane by year dictionary function here:

def convert_dictionary_by_year(current_dictionary):
    temp_dict = {}
    for hurricane_name, data in current_dictionary.items():
        for key, value in data.items():
            temp_dict.update({data.get("Year"): data})
    return temp_dict

hurricane_by_year = convert_dictionary_by_year(hurricane_dictionary_by_name)

def hurricane_dictionary_year(name, month, year, wind, area, damage, death):
    temp = {}
    for index in range(len(year)):
        temp.update({year[index]: {"Name": name[index], "Month": month[index], "Year": year[index], "Max Sustained Wind": wind[index], "Areas Affected": area[index], "Damage": damage[index], "Death": death[index]}})
    return temp

hurricane_dictionary_by_year = hurricane_dictionary_year(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)

# write your count affected areas function here:

def area_count_using_list(area):
    temp_flat_list_of_areas = [name_of_location for sublist in area for name_of_location in sublist]
    temp_dict = {}
    for name_of_location in temp_flat_list_of_areas:
        if not name_of_location in temp_dict:
            temp_dict.update({name_of_location: temp_flat_list_of_areas.count(name_of_location)})
    return temp_dict

affected_area_counted = area_count_using_list(areas_affected)


def count_area_with_dictionary(dictionary1, key):
    temp_dict = {}
    for main_key, data in dictionary1.items():
        for sub_key, value in data.items():
            if sub_key == key:
                for name_of_location in value:
                    if not name_of_location in temp_dict:
                        temp_dict[name_of_location] = 1
                    else:
                        temp_dict[name_of_location] = temp_dict[name_of_location] + 1
    return temp_dict

counted_areas_affected_using_dictionary = count_area_with_dictionary(hurricane_dictionary_by_name, "Areas Affected")

# write your find most affected area function here:

def most_area_affected(dictionary1):
    temp_result = ["Temporary location", 0]
    for key, value in dictionary1.items():
        if value > temp_result[1]:
            temp_result[0] = key
            temp_result[1] = value
        else:
            continue
    return temp_result

most_hit_area = most_area_affected(counted_areas_affected_using_dictionary)

# write your greatest number of deaths function here:

def greatest_death(dictionary1, key):
    temp_result = ["Name of hurricane", 0]
    for main_key, data in dictionary1.items():
        for sub_key, value in data.items():
            if sub_key == key:
                if value > temp_result[1]:
                    temp_result[0] = main_key
                    temp_result[1] = value
                else:
                    continue
    return temp_result

the_greatest_death = greatest_death(hurricane_dictionary_by_name, "Death")

# write your catgeorize by mortality function here:



def scalling_hurricane(dictionary1, key):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    temp_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for main_key, data in dictionary1.items():
        for sub_key, value in data.items():
            if sub_key == key:
                if value == mortality_scale[0]:
                    temp_scale[0].append(main_key)
                elif value <= mortality_scale[1]:
                    temp_scale[1].append(main_key)
                elif value <= mortality_scale[2]:
                    temp_scale[2].append(main_key)
                elif value <= mortality_scale[3]:
                    temp_scale[3].append(main_key)
                elif value <= mortality_scale[4]:
                    temp_scale[4].append(main_key)
                else:
                    temp_scale[5].append(main_key)
    return temp_scale

hurricane_mortality_scale = scalling_hurricane(hurricane_dictionary_by_name, "Death")


# write your greatest damage function here:

def greatest_damage(dictionary1, key):
    temp_result = ["Name of hurricane", 0]
    for main_key, data in dictionary1.items():
        for sub_key, value in data.items():
            if sub_key == key:
                if value == "Damages not recorded":
                    continue
                if value > temp_result[1]:
                    temp_result[0] = main_key
                    temp_result[1] = value
                else:
                    continue
    return temp_result

hurricane_with_greatest_damage = greatest_damage(hurricane_dictionary_by_name, "Damage")

def scalling_hurricane_by_damages(dictionary1, key):
    damage_scale = {0: 0,
                   1: 100000000,
                   2: 1000000000,
                   3: 10000000000,
                   4: 50000000000}
    temp_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], "Damages not recorded":[]}
    for main_key, data in dictionary1.items():
        for sub_key, value in data.items():
            if sub_key == key:
                if value == "Damages not recorded":
                    temp_scale["Damages not recorded"].append(main_key)
                elif value == damage_scale[0]:
                    temp_scale[0].append(main_key)
                elif value <= damage_scale[1]:
                    temp_scale[1].append(main_key)
                elif value <= damage_scale[2]:
                    temp_scale[2].append(main_key)
                elif value <= damage_scale[3]:
                    temp_scale[3].append(main_key)
                elif value <= damage_scale[4]:
                    temp_scale[4].append(main_key)
                else:
                    temp_scale[5].append(main_key)
    return temp_scale

hurricane_category_by_damage = scalling_hurricane_by_damages(hurricane_dictionary_by_name, "Damage")
print(hurricane_category_by_damage)

# write your catgeorize by damage function here:

