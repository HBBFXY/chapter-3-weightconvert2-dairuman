earth_weight = 50  
for year in range(1, 11):  
    # 计算地球当年的体重（每年增长0.5kg）
    earth_weight += 0.5  
    # 计算月球当年的体重（是地球体重的16.5%）
    moon_weight = earth_weight * 0.165  
    # 输出第几年在地球和月球上的体重
    print(f"第{year}年，在地球上的体重：{earth_weight:.2f}kg，
    在月球上的体重：{moon_weight:.2f}kg")
