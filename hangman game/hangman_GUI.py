import tkinter as tk
from tkinter import messagebox

import hangman_game as hg

class hangman_game:
    def __init__(self):
    
        self.word_secret = hg.chosen_word
        self.life = hg.lives
        self.memory_game = hg.correct_letters
        
        self.windown = tk.Tk()
        self.windown.title("WELCOME HANGMAN GAME")
        self.windown.geometry("400x550")
        self.windown.config(bg="#2c3e50")
        
        # Crear los componentes visuales
        self.create_widgets()
        self.upgrade_GUI()
        
    def create_widgets(self):
        # Título del juego
        self.lbl_title = tk.Label(self.windown, text="HANGMAN GAME", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.lbl_title.pack(pady=10)
        
        # El dibujo del ahorcado (Usa Courier para que el arte ASCII de LIFE_STAGE no se deforme)
        self.lbl_stage = tk.Label(self.windown, text="", font=("Courier", 12), bg="#2c3e50", fg="#e74c3c", justify="left")
        self.lbl_stage.pack(pady=10)
        
        # Espacio para mostrar la palabra oculta (_ _ _ _)
        self.lbl_word = tk.Label(self.windown, text="", font=("Arial", 22, "bold"), bg="#2c3e50", fg="#2ecc71")
        self.lbl_word.pack(pady=15)
        
        # Vidas restantes
        self.lbl_lives = tk.Label(self.windown, text="", font=("Arial", 12), bg="#2c3e50", fg="#f1c40f")
        self.lbl_lives.pack(pady=5)
        
        # Contenedor para la entrada de texto
        frame_input = tk.Frame(self.windown, bg="#2c3e50")
        frame_input.pack(pady=20)
        
        lbl_instruction = tk.Label(frame_input, text="Enter a letter", font=("Arial", 11), bg="#2c3e50", fg="#ecf0f1")
        lbl_instruction.pack(side="left", padx=5)
        
        self.ENTER = tk.Entry(frame_input, width=5, font=("Arial", 12, "bold"), justify="center")
        self.ENTER.pack(side="left", padx=5)
        self.ENTER.bind("<Return>", lambda event: self.game_process()) # Enviar con Enter
        
        btn_SEND = tk.Button(frame_input, text="attempt", command=self.game_process, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
        btn_SEND.pack(side="left", padx=5)

    def upgrade_GUI(self):
        # Replicamos tu lógica para construir la palabra con guiones bajos o letras descubiertas
        display = ""
        for letter in self.word_secret:
            if letter in self.memory_game:
                display += letter + " "
            else:
                display += "_"
                
        # Actualizamos los elementos de la pantalla con tus datos y tus librerías de arte
        self.lbl_word.config(text=display)
        self.lbl_lives.config(text=f"remaining lives: {self.life}")
        self.lbl_stage.config(text=hg.LIFE_STAGE[self.life])
        
        # Comprobar si ganó
        if "_" not in display:
            messagebox.showinfo("¡CONGRATULATIONS!", "***********YOU WIN***********")
            self.windown.destroy()

    def game_process(self):
        guess = self.ENTER.get().lower().strip()
        self.ENTER.delete(0, tk.END) # Limpiar la caja de texto
        
        # Validar entrada
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("WARNING", "Incorrect command, please enter a letter")
            return
            
        # Al igual que en tu código: revisar si la letra ya se había puesto
        if guess in self.memory_game:
            messagebox.showinfo("ATTENTION","You already posted this letter :)")
            return
            
        # Tu lógica de acierto o fallo
        if guess in self.word_secret:
            # Añadir a letras correctas
            for letter in self.word_secret:
                if letter == guess:
                    self.memory_game.append(guess)
        else:
            self.life -= 1
            
        # Actualizar la ventana con los cambios
        self.upgrade_GUI()
        
        # Comprobar si perdió
        if self.life == 0:
            messagebox.showerror("GAME OVER", f"*********YOU LOSE*********\nLa palabra era: {self.word_secret}")
            self.windown.destroy()

    def running(self):
        self.windown.mainloop()

if __name__ == "__main__":
    app = hangman_game()
    app.running()