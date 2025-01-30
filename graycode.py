def gray(number):
    code = number[0]
    for b in range(1, len(number)):
        code += str(int(number[b])^int(number[b-1])) # XOR between the current and previous bits
    return code

def main():
    number = input("Enter your number: ")
    choice = input("Is your number expressed in the binary numeral system? (y/n) ").lower()

    if choice == 'n':
        if number.isdigit():
            number = format(int(number), '04b') # converts to binary 
        else:
            print("Enter a valid decimal number.")
            exit()
    
    print(f"({gray(number)})GRAY")

if __name__ == "__main__":
    main()
