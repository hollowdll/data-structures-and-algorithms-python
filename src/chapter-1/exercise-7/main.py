# Custom encoder

def custom_encoder(text: str) -> list[int]:
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for char in text.lower():
        positions.append(reference_string.find(char))

    return positions

def main():
    text = 'My house is beautiful'
    print(custom_encoder(text))

if __name__ == "__main__":
    main()