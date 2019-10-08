import pprint

def coin_estimator():
    coin_dict = {"Toonie": (200, 6.92, 25), "Loonie": (100, 6.27, 25), "Quarter": (25, 4.4, 40), "Dime": (10, 1.75, 50), "Nickel": (5, 3.95, 40), "Cent": (1, 2.35, 50)}
    total_amount = {}
    weight_mod = weight_check()
    for coin_name, coin_info in coin_dict.items():
        while True:
            try:
                total_weight = float(input("Please enter the total weight of {}s: ".format(coin_name))) * weight_mod
                break
            except ValueError:
                print("\nThat was not a correct number value.")
        if total_weight > 0:
            total_amount[coin_name] = {}
            total_amount[coin_name]["wrappers"] = round((total_weight / coin_info[1]) / coin_info[2])
            total_amount[coin_name]["amount"] = round(total_weight / coin_info[1])
            total_amount[coin_name]["value"] = round(((total_weight / coin_info[1]) * coin_info[0]) / 100) if ((total_weight / coin_info[1]) * coin_info[0]) > 100 else round(((total_weight / coin_info[1]) * coin_info[0]))
        else:
            pass
    return total_amount

def weight_check():
    weight_input = input("Would you like your weight type set to pounds(p) or grams(g)? \n")
    weight_type = weight_input[:4]
    weight_mod = 1
    if weight_type == 'g' or weight_type == "gram":
        pass
    elif weight_type == 'p' or weight_type == 'poun':
        weight_mod = 453.592
    else:
        print("I'm sorry, I don't understand")
        weight_check()
    return weight_mod

pprint.pprint(coin_estimator())