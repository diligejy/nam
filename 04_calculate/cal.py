
operator = ["+", "-", "*", "/", "="]
user_input = "5 + 5 * 10"

string_list = []

for i, s in enumerate(user_input):
    print(i,s)
    if s in operator:
        