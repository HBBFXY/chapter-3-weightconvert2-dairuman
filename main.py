weight=input ("在地球上的体重为:")
for year in range(1, 11):  
    earth_weight = 0.5*year+weight  
    moon_weight = earth_weight * 0.165  
    print("第{year}年，在地球上的体重：{earth_weight:.2f}kg，
    在月球上的体重：{moon_weight:.2f}kg")
