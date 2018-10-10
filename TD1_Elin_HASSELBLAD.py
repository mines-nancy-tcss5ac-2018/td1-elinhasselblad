#TD1 Elin HASSELBLAD

#Project Euler probl�me 16:
#pour r�soudre le probl�me on utilise power_digit_sum(1000)
#le r�ponse est 1366
def power_digit_sum(n):
    product = 2 ** n
    list = [int(d) for d in str(product)]
    return(sum(list))

assert power_digit_sum(15)==26

#Project Euler probl�me 22:
#pour r�soudre le probl�me on utilise name_scores()
#le r�ponse est 871198282
with open('euler22_names.txt') as f:
    list_of_names= f.read().split(',')

def alphabetical_order():
    alphabetical_list = sorted(list_of_names)
    return(alphabetical_list)

def alphabetical_value(name):
    letter_values = [ord(letter)-64 for letter in list(name) if letter != '"']
    return(sum(letter_values))

def name_scores():
    thelist = alphabetical_order()
    name_values = [alphabetical_value(name)*(thelist.index(name)+1) for name in thelist]
    return(sum(name_values))

assert alphabetical_value('"COLIN"') == 53

#Project Euler probl�me 55
#pour r�soudre le prol�me on utilise Lychrel()
#le r�ponse est 249
def reverse(n):
    reverse = 0
    while n > 0:
        reminder = n % 10
        reverse = (reverse*10) + reminder
        n = n//10
    return(reverse)

def find_Lychrel():
    list_of_Lychrel = []
    for i in range(1,10000):
        new_number = i + reverse(i)
        it = 1
        while new_number != reverse(new_number) and it <= 50:
            new_number = new_number + reverse(new_number)
            it += 1
            if it == 51 and new_number != reverse(new_number):
                list_of_Lychrel = list_of_Lychrel + [new_number]
    return(list_of_Lychrel)

def Lychrel():
    number_of_Lychrel = len(find_Lychrel())
    return(number_of_Lychrel)

assert 47 not in find_Lychrel()
assert 349 not in find_Lychrel()