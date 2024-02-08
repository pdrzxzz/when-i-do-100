def receiving_and_checking_inputs():
    user_name = input('enter your name: ')
    user_age = input('enter your age: ')

    checked = False
    # while age isnt an int
    while not checked:
        # check if age is an int
        try:
            int(user_age)
            if int(user_age) < 0:
                raise ValueError
            if int(user_age) > 100:
                print('Você precisa ter menos de 100 anos para usar esse programa.')
                quit()
            else:
                checked = True
        # if isnt an int, launch another input
        except ValueError:
            user_age = input('please enter an positive integer: ')
    return (user_name, int(user_age))

def calc(age):
    """receive one parameter 'age' and returns an int of how many years lack to 100 years"""
    actual_year = 2024
    return (actual_year + (100 - age))

def printing_year(name, age):
    year_that_makes_100 = calc(age)
    print(f'Você, {name} fará 100 anos no ano {year_that_makes_100}.')

printing_year(*receiving_and_checking_inputs())