def pres(str1, str2):
    char_set = set(str2)
    for char in str1:
        if char not in char_set:
            return "No"
    return "Yes"
print("Enter number of test cases: ")
T = int(input())

for _ in range(T):
    input_str = input()
    str1, str2 = input_str.split()
    result = pres(str1, str2)
    print(result)