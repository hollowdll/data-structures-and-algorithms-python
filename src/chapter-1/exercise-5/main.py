# Count vowels

def main():
    s = input().lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for c in s:
        if c in vowels:
            vowel_count += 1

    print(f'Number of vowels: {vowel_count}')

if __name__ == "__main__":
    main()