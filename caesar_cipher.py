import string

# Emoji theme mapping (A-Z)
EMOJI_LIST = [
    "😀", "🐱", "🌟", "🍀", "🚀", "🎈", "🍎", "🥑", "🍩", "🎉",
    "🔑", "🦁", "🌈", "🎵", "🐙", "🍕", "👑", "🌹", "⭐", "🍅",
    "☂️", "🦄", "🍉", "🛳️", "🍋", "⚡"
]

def caesar_shift(text, shift, theme='letters', decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    if theme == 'letters':
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                offset = (ord(char) - start + shift) % 26
                result += chr(start + offset)
            else:
                result += char
    elif theme == 'emoji':
        for char in text.upper():
            if char in string.ascii_uppercase:
                idx = (ord(char) - ord('A') + shift) % 26
                result += EMOJI_LIST[idx]
            else:
                result += char
    return result

def emoji_to_text(emoji_text, shift):
    reversed_map = {v: k for k, v in zip(string.ascii_uppercase, EMOJI_LIST)}
    result = ""
    for char in emoji_text:
        if char in EMOJI_LIST:
            idx = (EMOJI_LIST.index(char) - shift) % 26
            result += string.ascii_uppercase[idx]
        else:
            result += char
    return result

def main():
    print("Unique Caesar Cipher Tool!")
    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().lower()
    theme = input("Theme? (letters/emoji): ").strip().lower()
    shift = int(input("Enter shift value (1-25): "))
    message = input("Enter your message: ")

    if mode == 'e':
        if theme == 'letters':
            encrypted = caesar_shift(message, shift, theme='letters')
        elif theme == 'emoji':
            encrypted = caesar_shift(message, shift, theme='emoji')
        print(f"Encrypted message: {encrypted}")
    elif mode == 'd':
        if theme == 'letters':
            decrypted = caesar_shift(message, shift, theme='letters', decrypt=True)
        elif theme == 'emoji':
            decrypted = emoji_to_text(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()