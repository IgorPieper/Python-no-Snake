def main_menu():
    while True:
        print("Morse Code Translator")
        print("======================")
        print("1. Translate text to Morse code")
        print("2. Translate Morse code to text")
        print("3. Exit")
        choice = input("Please select an option (1, 2, or 3): ")

        if choice == '1':
            text = input("Enter the text to be translated into Morse code: ")
            morse_translation = text_to_morse(text)
            print("Morse Code:", morse_translation)
        elif choice == '2':
            morse_input = input("Enter the Morse code to be translated into text (use '/' to separate words): ")
            text_translation = morse_to_text(morse_input)
            print("Text Translation:", text_translation)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 'Ą': '.-.-', 'Ć': '-.-..', 'Ę': '..-..',
    'Ł': '.-..-', 'Ń': '--.--', 'Ó': '---.', 'Ś': '...-...-', 'Ź': '--..-.',
    'Ż': '--..-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += '? '
    return morse_code.strip()

def morse_to_text(morse):
    text = ''
    morse_words = morse.split(' / ')
    for morse_word in morse_words:
        for morse_char in morse_word.split():
            if morse_char in reverse_morse_code_dict:
                text += reverse_morse_code_dict[morse_char]
            else:
                text += '?'
        text += ' '
    return text.strip()

main_menu()
