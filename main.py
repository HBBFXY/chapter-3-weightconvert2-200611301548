initial_earth_weight = 60  
lunar_ratio = 0.165  
print()
for year in range(1, 11):
    earth_weight = initial_earth_weight + 0.5 * year
    lunar_weight = earth_weight * lunar_ratio
    print(f"{year}\t{earth_weight:.2f}\t\t{lunar_weight:.2f}")
