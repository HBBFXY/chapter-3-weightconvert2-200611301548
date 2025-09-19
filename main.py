# 假设初始地球体重为50kg
initial_weight = 50
lunar_ratio = 0.165

for year in range(1, 11):
    earth_weight = initial_weight + 0.5 * year
    lunar_weight = earth_weight * lunar_ratio
    print(f"第{year}年，地球体重：{earth_weight:.2f}kg，月球体重：{lunar_weight:.2f}kg")
