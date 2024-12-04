file_name = "input"

seeds_line = 0
seed_to_soil_line = 2
soil_to_fertilizer_line = 18
fertilizer_to_water_line = 40
water_to_light_line = 84
light_to_temperature_line = 126
temperature_to_humidity_line = 172
humidity_to_location_line = 181

with open(file_name, 'r') as f:
    lines = f.readlines()

# Get the seeds
seeds = lines[seeds_line].strip().split(':')[1]
seeds = seeds.split(" ")
seeds = [int(s) for s in seeds if s.isnumeric()]

# Get the seed_to_soil list
seed_to_soil = []
for line in lines[seed_to_soil_line+1:soil_to_fertilizer_line-1]:
    line = line.strip()
    nums = line.split(' ')
    seed_to_soil.append((int(nums[0]), int(nums[1]), int(nums[2])))
seed_to_soil = sorted(seed_to_soil, key=lambda x: x[1])

# Get the soil_to_fertilizer list
soil_to_fertilizer = []
for line in lines[soil_to_fertilizer_line+1:fertilizer_to_water_line-1]:
    line = line.strip()
    nums = line.split(' ')
    soil_to_fertilizer.append((int(nums[0]), int(nums[1]), int(nums[2])))
soil_to_fertilizer = sorted(soil_to_fertilizer, key=lambda x: x[1])

# Get the fertilizer_to_water list
fertilizer_to_water = []
for line in lines[fertilizer_to_water_line+1:water_to_light_line-1]:
    line = line.strip()
    nums = line.split(' ')
    fertilizer_to_water.append((int(nums[0]) , int(nums[1]) , int(nums[2])))
fertilizer_to_water = sorted(fertilizer_to_water, key=lambda x: x[1])

# Get the water_to_light list
water_to_light = []
for line in lines[water_to_light_line+1:light_to_temperature_line-1]:
    line = line.strip()
    nums = line.split(' ')
    water_to_light.append((int(nums[0]), int(nums[1]), int(nums[2])))
water_to_light = sorted(water_to_light, key=lambda x: x[1])

# Get the light_to_temperature list
light_to_temperature = []
for line in lines[light_to_temperature_line+1:temperature_to_humidity_line-1]:
    line = line.strip()
    nums = line.split(' ')
    light_to_temperature.append((int(nums[0]), int(nums[1]), int(nums[2])))
light_to_temperature = sorted(light_to_temperature, key=lambda x: x[1])

# Get the temperature_to_humidity list
temperature_to_humidity = []
for line in lines[temperature_to_humidity_line+1:humidity_to_location_line-1]:
    line = line.strip()
    nums = line.split(' ')
    temperature_to_humidity.append((int(nums[0]), int(nums[1]), int(nums[2])))
temperature_to_humidity = sorted(temperature_to_humidity, key=lambda x: x[1])

# Get the humidity_to_location list
humidity_to_location = []
for line in lines[humidity_to_location_line+1:]:
    line = line.strip()
    nums = line.split(' ')
    humidity_to_location.append((int(nums[0]), int(nums[1]), int(nums[2])))
humidity_to_location = sorted(humidity_to_location, key=lambda x: x[1])


def get_destination_unefficient(source, l):
    for d, s, r in l:
        if source in range(s, s+r+1):
            return d + (source - s)
    return source

# find the closest location
min_distance = None

for seed in seeds:
    # Get the good soil
    soil = get_destination_unefficient(seed, seed_to_soil)
    
    # Get the good fertilizer
    fertilizer = get_destination_unefficient(soil, soil_to_fertilizer)
    
    # Get the good water
    water = get_destination_unefficient(fertilizer, fertilizer_to_water)
    
    # Get the good light
    light = get_destination_unefficient(water, water_to_light)
    
    # Get the good temperature
    temperature = get_destination_unefficient(light, light_to_temperature)
    
    # Get the good humidity
    humidity = get_destination_unefficient(temperature, temperature_to_humidity)
    
    # Get the good location
    location = get_destination_unefficient(humidity, humidity_to_location)
    
    if min_distance == None or min_distance > location:
        min_distance = location

print("the closest location is :", min_distance)