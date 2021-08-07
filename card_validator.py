# takes in string representation of a card number
def calculate_sum(number):
    total = 0
    loc = 2
    for digit in range(len(number)-2,-1,-1):
        if loc % 2 == 0:
            x = int(number[digit]) * 2
            if x > 9:
                num_string = str(x)
                add1 = int(num_string[0])
                add2 = int(num_string[1])
                y = add1 + add2
                total += y
            else:
                total += x
        else:
            total += int(number[digit])
        loc += 1
    return total


# takes in an int sum of 15 values
def calculate_checksum_control(sum):
    return 10 - (sum%10)

def credit_card_check(card_number):
    total = calculate_sum(str(card_number))
    control = calculate_checksum_control(total)
    checksum_value = int(card_number) % 10
    return checksum_value == control

import getpass

card_number = getpass.getpass("Card No: ")

print(credit_card_check(card_number))