leap_years = []
for i in range(2000, 2401):
    if i%4 == 0:
            if i%100 == 0:
                if i%400 == 0:
                    leap_years.append(i)
            else:
                leap_years.append(i)        
print(leap_years)
