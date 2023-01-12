#Given the following dictionary of nations and their respective population, find the nation with the closest population to South Korea and print the difference in population between the two nations.

population = {
	'Korea' : 51000000,
	'Russia': 144000000,
	'China': 140000000,
	'Japan': 126000000,
	'England' : 66000000 }

closest_nation = None
min_diff = float('inf')
for nation, pop in population.items():
    if nation != "Korea":
        diff = abs(population['Korea'] - pop)
        if diff < min_diff:
            min_diff = diff
            closest_nation = nation
print(closest_nation, min_diff)
