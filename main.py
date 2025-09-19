current_weight = 60
annual_growth = 0.5
moon_ratio = 0.165
print()
for year in range(1, 11):
    earth_weight = current_weight + annual_growth * year
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球上体重 {earth_weight:.2f} 千克，月球上体重 {moon_weight:.2f} 千克")
