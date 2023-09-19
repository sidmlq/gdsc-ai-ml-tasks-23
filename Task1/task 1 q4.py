def shortintl(givenstr):
    current = givenstr
    while len(current)>=2 and ((current[0] == '1' and current[len(current) - 1] == '0') or (current[0] == '0' and current[len(current) - 1] == '1')):
        current = current[1:len(current) - 1]
    return len(current)

T = int(input("Enter the number of test cases:"))
for _ in range(T):
    input_str = input()
    result = shortintl(input_str)
    print(result)
