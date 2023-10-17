# Sum a collection of numbers

def main():
    sum = 0.0

    while True:
        num = 0.0
        try:
            num = float(input())
        except:
            print("That wasn't a number.")
            continue

        if num == 0:
            return print(f"The grand total is {sum}")
        
        sum += num
        print(f"The total is now {sum}")

if __name__ == "__main__":
    main()