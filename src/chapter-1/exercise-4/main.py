# Sum of the first n positive integers

def main():
    try:
        n = int(input())
    except:
        return print("Invalid positive integer")

    if n < 0:
        return print("Invalid positive integer")

    sum = n * (n + 1) // 2
    print(f"The sum of the first {n} positive integers is {sum}")

if __name__ == "__main__":
    main()