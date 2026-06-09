ABC_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_Cipher(original_text, shift_amount, encode_or_decode):
    text_save = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter not in ABC_list:
            text_save += letter
        else:
            position = ABC_list.index(letter)
            new_position = position + shift_amount
            text_save += ABC_list[new_position]
            
            print(f"Here is the {encode_or_decode}d result: {text_save}")

try:
    selection_encrypt = input("Do you want to enter the encoding menu 'Yes/No'?:\n").lower()
    

    if any(char.isdigit() for char in selection_encrypt):
        raise ValueError("Numbers are not allowed")
    

    if selection_encrypt == "yes":
         should_continue = True


         while should_continue:
             direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

             if any(char.isdigit() for char in direction):
                 raise ValueError("Numbers are not allowed")
             
             text = input("Type your message:\n").lower()
             
             if any(value.isdigit() for value in text):
                 raise ValueError("Numbers are not allowed")
             

             shift = int(input("Type the shift number:\n"))
    
             shift = shift % 26

    
             caesar_Cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)
        
             restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
             if restart == "no":
                 should_continue = False
                 print("Goodbye!")
    
    
    else: 
         should_continue = False
         print("Goobye")
    
    
except ValueError as e: 
    print(f"\nNumbers are not allowed")
  
