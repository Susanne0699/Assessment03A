"""
Upper and Lower
"""
my_string = input(">> Enter a phrase: ")

def count_upper_lower(my_string: str) -> str:
    for letter in my_string:
        my_string += 1
        if letter.isupper(): return letter
        elif letter.islower(): return letter

print(">> No. of Upper case characters:", my_string.isupper())
print(">> No. of Lower case characters:", my_string.islower())

count_upper_lower()
"""
Check 33
"""

my_list = int(input(">> Enter several numbers: "))
def has_33(my_list) -> int:
    for index in range(0, len(my_list)):
        while my_list == [3, 3]: return True
        if my_list != [3, 3]: return False

has_33()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(count_upper_lower())

