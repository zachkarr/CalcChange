# CalcChange - by Zach Karr

print('Welcome to the Change Calculator!')

choice = input('Do you have any change? (Y/N): ')

grand_total = 0
total_dollars = 0
total_cents = 0


def get_coin(coin_type):
    coin = -1
    while coin < 0:
        try:
            coin = int(input("How many " + coin_type + " do you have? \n"))
            if coin < 0:
                print("Coin values must be a positive number only! Please re-enter a valid value: ")
        except ValueError:
            print("Please enter an integer value only:\n")
            coin = -1
    return coin


while choice.upper().startswith('Y'):
    half_dollars = get_coin("Half-Dollars")
    quarters = get_coin("Quarters")
    dimes = get_coin("Dimes")
    nickles = get_coin("Nickels")
    pennies = get_coin("Pennies")

    total_val = half_dollars * 50 + quarters * 25 + dimes * 10 + nickles * 5 + pennies

    grand_total += total_val
    total_dollars = grand_total // 100
    total_cents = grand_total % 100

    print('You have ' + str(total_val) + " cents.")

    dollars = total_val // 100
    cents = total_val % 100

    print("Which is " + str(dollars) + " dollars and " + str(cents) + " cents.")
    choice = input("Do you have more change? (Y/N):\n")

print('Thanks for using the Change Calculator!\n\nYou had a total of ' + str(grand_total) + ' cents\nwhich is ' + str(
    total_dollars) + " dollars and " + str(total_cents) + ' cents.')
