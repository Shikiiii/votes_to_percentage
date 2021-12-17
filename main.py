keepCounting = True
numbers = []

while keepCounting:
    num = input("Enter the number of votes for this choice. Enter \"end\" once done entering them all.")
    
    if num == "end":
        keepCounting = False
        continue
    
    try:
        _ = int(num)
    except:
        print("Invalid number! Please try again.")
        continue
    
    numbers.append(int(num))
    
total = 0
for i in numbers:
    total += i

toConvert = float(total / 100)

option = 1
for i in numbers:
    print(f"Option {option} | {round(i/toConvert)}%")
    option += 1
