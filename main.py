# 假设当前在地球上的体重（单位：千克）
current_weight = 60
# 每年体重增长（单位：千克）
annual_growth = 0.5
# 月球上体重是地球上的比例
moon_ratio = 0.165

print("未来10年地球和月球上的体重变化：")
for year in range(1, 11):
    earth_weight = current_weight + annual_growth * year
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球上体重 {earth_weight:.2f} 千克，月球上体重 {moon_weight:.2f} 千克")
