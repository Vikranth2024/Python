leap_years = []

for year in range(2000, 2401):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)

print(leap_years)
