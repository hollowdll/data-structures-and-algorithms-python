# Squares

def main():
    n = int(input())
    my_dict = {}
    
    for num in range(1, n+1):
        my_dict[num] = num ** 2

    print(my_dict)

if __name__ == "__main__":
    main()