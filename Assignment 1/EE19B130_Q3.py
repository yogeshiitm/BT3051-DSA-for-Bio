"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q3. Diet planner
"""
# def diet_check():



def all_combinations(menu):
	if(len(menu)==0): #base
		return [[]]

	last_item = menu[-1]
	result_without_last = all_combinations(menu[:-1]) #recursion
	result_with_last = [lst + [last_item] for lst in result_without_last]

	return result_without_last + result_with_last


def print_diet_checked_combinations(menu):
	combinations = all_combinations(menu)
	for lst in combinations:
		carbs=0;fats=0;proteins=0;vitamins=0;minerals=0
		for item in lst:
			carbs += menu_dict[item]["carbs"]
			fats += menu_dict[item]["fats"]
			proteins += menu_dict[item]["proteins"]
			vitamins += menu_dict[item]["vitamins"]
			minerals += menu_dict[item]["minerals"]

		if(carbs<=300 and fats<=150 and proteins>80 and proteins<=500 and vitamins>10 and vitamins<=100 and minerals>10 and minerals<=50):
			print(tuple(lst))


menu_dict = {
	"Rice": {"carbs":195,"fats":12,"proteins":12,"vitamins":5,"minerals":7},
	"Veg Curry": {"carbs":50,"fats":36,"proteins":42,"vitamins":23,"minerals":3},
	"Cheese Burger": {"carbs":203,"fats":95,"proteins":150,"vitamins":63,"minerals":27},
	"Potato Chips": {"carbs":78,"fats":78,"proteins":25,"vitamins":14,"minerals":12},
	"Roti": {"carbs":76,"fats":20,"proteins":34,"vitamins":14,"minerals":6},
	"Soft Drink": {"carbs":98,"fats":7,"proteins":8,"vitamins":9,"minerals":21}
}


menu_list = ["Rice", "Veg Curry", "Cheese Burger", "Potato Chips", "Roti", "Soft Drink"]
print_diet_checked_combinations(menu_list)