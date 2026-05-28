import customtkinter as ctk
import secrets as sec
import string
import pyperclip


ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("blue")

class password_suggestion(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("Password suggestion")
        self.geometry("380x280")
        self.attributes("-topmost", True) 
        self.resizable(False, False)
        self.password = self.secret_password()

        self.label = ctk.CTkLabel(self, text="Use suggested password ", font=("Arial", 12))
        self.label.pack(pady=(15, 5))

        self.entry = ctk.CTkEntry(self, width=250, justify="center", font=("Consolas", 16))
        self.entry.insert(0, self.password)
        self.entry.configure(state="readonly") 
        self.entry.pack(pady=5)

        self.btn = ctk.CTkButton(self, text="Use password", command=self.copy_and_close)
        self.btn.pack(pady=10)

        self.btn_generar = ctk.CTkButton(self, text="Change password", command=self.generated_password)
        self.btn_generar.pack(pady=10)



    def secret_password(self):
        letters = string.ascii_letters
        numbers = string.digits
        symbols = "!@#$%^&*()-_=+"
        password_created = letters + numbers + symbols

        password_length = 12

        password_list = [
             sec.choice(letters),
             sec.choice(numbers),
             sec.choice(symbols)
        ]


        for _ in range(password_length - len(password_list)):
             password_list.append(sec.choice(password_created))
    
        sec.SystemRandom().shuffle(password_list)
        password_final = "".join(password_list)

        
        pyperclip.copy(password_final)
    
    
        print("======================================")
        print("      PASSWORD SAVED       ")
        print("======================================")
        print(f"\nSuggested password: {password_final}")
        print("\n Check your clipboard")

        return password_final

    def copy_and_close(self):
         pyperclip.copy(self.password)
         print("Password copied to clipboard")
         self.destroy() 
    
    def generated_password(self):
         self.password = self.secret_password()
         self.entry.configure(state="normal")
         self.entry.delete(0, "end")
         self.entry.insert(0, self.password)
         self.entry.configure(state ="readonly")

    
if __name__== "__main__":
    app = password_suggestion()
    app.mainloop()