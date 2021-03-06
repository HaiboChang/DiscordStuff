
mapping = {
    'A': 'Ⲁ',
    'B': 'Ⲃ',
    'C': 'Ⲥ',
    'D': '𐌃',
    'E': 'Ⲉ',
    'F': '𐍆',
    'G': '𐌾',
    'H': 'Ⲏ',
    'I': 'Ⲓ',
    'J': 'Ⲓ',
    'K': 'Ⲕ',
    'L': 'Ⳑ',
    'M': 'Ⲙ',
    'N': 'Ⲛ',
    'O': 'Ⲟ',
    'P': 'Ⲣ',
    'Q': 'Ԛ',
    'R': '𐌺',
    'S': '𐍃',
    'T': '𐍄',
    'U': '𐌵',
    'V': '𐌵',
    'W': 'Ⲱ',
    'X': 'Ⲭ',
    'Y': 'Ⲩ',
    'Z': 'Ⲍ',
    'a': 'ⲁ',
    'b': 'ⲃ',
    'c': 'ⲥ',
    'd': 'ꝺ',
    'e': 'ⲉ',
    'f': 'ϝ',
    'g': 'ᵹ',
    'h': 'ⲏ',
    'i': 'ⲓ',
    'j': 'ⲓ',
    'k': 'ⲕ',
    'l': 'ⳑ',
    'm': 'ⲙ',
    'n': 'ⲛ',
    'o': 'ⲟ',
    'p': 'ⲣ',
    'q': 'ꝗ',
    'r': 'ꞃ',
    's': 'ⲋ',
    't': 'ⲧ',
    'u': 'ꭒ',
    'v': 'ꭒ',
    'w': 'ꭒꭒ',
    'x': 'ⲭ',
    'y': 'ⲩ',
    'z': 'ⲍ',
    ' ': ' '
}

def transliterate(text):
    for key in mapping.keys():
        text = text.replace(key, mapping[key])
    return text

print(transliterate("Hello world"))
