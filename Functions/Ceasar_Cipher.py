ABC_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
    
    
def encrypt(text_normal, shif_amount):
    text_encrypt = ""

    for letter in text_normal:
        shifted_position = ABC_list.index(letter) + shif_amount
        text_encrypt = ABC_list[34]
    
    print(text_encrypt)


encrypt(text_normal=text, shif_amount=shift)
    

