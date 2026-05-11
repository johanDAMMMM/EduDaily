import customtkinter as ctk

# --- CONFIGURACIÓN DE NÚCLEO ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- PALETA DE COLORES ---
COLOR_BG = "#0F172A"
COLOR_CARD = "#1E293B"
COLOR_ACCENT = "#38BDF8"
COLOR_SUCCESS = "#10B981"
COLOR_ERROR = "#F43F5E"
COLOR_NAV = "#334155"
COLOR_TEXT = "#F8FAFC"

class EduDailyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Edu-Daily English V21.0 - Multi-Theme")
        self.geometry("950x1000")
        self.configure(fg_color=COLOR_BG)

        # --- DATASET MULTITEMÁTICO (10 ELEMENTOS POR NIVEL) ---
        self.db_study = {
            "Nivel 1 (A1 - Objetos y Lugares)": [
                ("Airport", "Aeropuerto", "ér-port"),
                ("House", "Casa", "háus"),
                ("Kitchen", "Cocina", "kí-chen"),
                ("Supermarket", "Supermercado", "sú-per-már-ket"),
                ("School", "Escuela", "scúl"),
                ("Ticket", "Boleto / Tiquete", "tí-ket"),
                ("Family", "Familia", "fá-mi-li"),
                ("Friend", "Amigo", "frend"),
                ("City", "Ciudad", "sí-ti"),
                ("Bread", "Pan", "bred")
            ],
            "Nivel 2 (A2 - Actividades Diarias)": [
                ("Breakfast", "Desayuno", "bréc-fast"),
                ("Shopping", "Ir de compras", "shó-pin"),
                ("Cleaning", "Limpieza", "clí-nin"),
                ("Working", "Trabajando", "uér-kin"),
                ("Traveling", "Viajando", "trá-ve-lin"),
                ("Cooking", "Cocinando", "cú-kin"),
                ("Sleeping", "Durmiendo", "slí-pin"),
                ("Meeting", "Reunión", "mí-tin"),
                ("Walking", "Caminando", "uó-kin"),
                ("Reading", "Leyendo", "rí-din")
            ],
            "Nivel 3 (B1 - Gramática Diaria)": [
                ("The coffee IS hot", "El café ESTÁ caliente (Uso de 'To Be')", "de có-fi is jot"),
                ("She EATS an apple", "Ella COME una manzana (Presente Simple - S)", "shi íts an á-pol"),
                ("I GO to the park", "Yo VOY al parque (Rutinaria)", "ai góu tu de párc"),
                ("The store IS open", "La tienda ESTÁ abierta (Estado)", "de stór is óu-pen"),
                ("They PLAY soccer", "Ellos JUEGAN fútbol (Plural)", "dei pléi só-quer"),
                ("My house IS big", "Mi casa ES grande", "mai háus is big"),
                ("The bus ARRIVES late", "El bus LLEGA tarde (3ra persona)", "de bas a-ráivs léit"),
                ("We BUY milk", "Nosotros COMPRAMOS leche", "ui bái milc"),
                ("You HAVE a car", "Tú TIENES un carro", "iú jav a car"),
                ("It IS a sunny day", "ES un día soleado", "it is a sá-ni déi")
            ],
            "Nivel 4 (B2 - Estructuras en Inglés)": [
                ("SHE DOES NOT LIKE milk", "A ella NO LE GUSTA la leche (Negación)", "shi das not láic milc"),
                ("DO YOU TRAVEL often?", "¿VIAJAS a menudo? (Pregunta)", "du iú trá-vel ó-fen"),
                ("THE HOUSE IS NOT clean", "La casa NO ESTÁ limpia", "de háus is not clin"),
                ("DOES HE WORK here?", "¿Él TRABAJA aquí? (Pregunta 3ra persona)", "das ji uerc jíer"),
                ("WE DO NOT HAVE time", "Nosotros NO TENEMOS tiempo", "ui du not jav táim"),
                ("IS THE COFFEE ready?", "¿ESTÁ el café listo? (Pregunta To Be)", "is de có-fi ré-di"),
                ("THEY ARE NOT at home", "Ellos NO ESTÁN en casa", "dei ar not at jóum"),
                ("DOES IT COST much?", "¿CUESTA esto mucho?", "das it cost mach"),
                ("THE ROOM IS tidy", "La habitación ESTÁ ordenada", "de rúm is tái-di"),
                ("I DO NOT EAT bread", "Yo NO COMO pan", "ai du not it bred")
            ]
        }

        self.db_quiz = {
            "Quiz A1": [
                {"q": "¿Cómo se dice 'Aeropuerto'?", "a": ["Airport", "Airplane", "Air", "Area"], "c": "Airport"},
                {"q": "Traducción de 'House':", "a": ["Casa", "Causa", "Cama", "Caja"], "c": "Casa"},
                {"q": "¿Qué es 'Kitchen'?", "a": ["Cocina", "Coche", "Cuchara", "Cena"], "c": "Cocina"},
                {"q": "Escriba 'Boleto':", "a": ["Ticket", "Tick", "Tacket", "Token"], "c": "Ticket"},
                {"q": "¿Qué es 'School'?", "a": ["Escuela", "Escalera", "Escudo", "Espejo"], "c": "Escuela"},
                {"q": "Traducción de 'City':", "a": ["Ciudad", "Cielo", "Cinta", "Cine"], "c": "Ciudad"},
                {"q": "¿Cómo se dice 'Familia'?", "a": ["Family", "Familiar", "Famous", "Farm"], "c": "Family"},
                {"q": "Significado de 'Bread':", "a": ["Pan", "Beso", "Brazo", "Brillo"], "c": "Pan"},
                {"q": "¿Qué es 'Supermarket'?", "a": ["Supermercado", "Mercado", "Tienda", "Mall"], "c": "Supermarket"},
                {"q": "Traducción de 'Friend':", "a": ["Amigo", "Frente", "Frío", "Fruta"], "c": "Amigo"}
            ],
            "Quiz A2": [
                {"q": "¿Cómo se dice 'Desayuno'?", "a": ["Breakfast", "Break", "Fast", "Bred"], "c": "Breakfast"},
                {"q": "Shopping refers to:", "a": ["Ir de compras", "Limpiar", "Caminar", "Leer"], "c": "Ir de compras"},
                {"q": "Traducción de 'Cleaning':", "a": ["Limpieza", "Cena", "Clase", "Clima"], "c": "Limpieza"},
                {"q": "¿Qué es 'Working'?", "a": ["Trabajando", "Caminando", "Jugando", "Leyendo"], "c": "Trabajando"},
                {"q": "Significado de 'Traveling':", "a": ["Viajando", "Trayendo", "Tratando", "Trotando"], "c": "Viajando"},
                {"q": "Traducción de 'Cooking':", "a": ["Cocinando", "Comiendo", "Corriendo", "Cortando"], "c": "Cocinando"},
                {"q": "¿Qué es 'Sleeping'?", "a": ["Durmiendo", "Soplando", "Saltando", "Saliendo"], "c": "Durmiendo"},
                {"q": "Traducción de 'Meeting':", "a": ["Reunión", "Mañana", "Miedo", "Medio"], "c": "Reunión"},
                {"q": "¿Qué es 'Walking'?", "a": ["Caminando", "Viendo", "Volando", "Viviendo"], "c": "Caminando"},
                {"q": "Significado de 'Reading':", "a": ["Leyendo", "Riendo", "Rayando", "Robando"], "c": "Leyendo"}
            ],
            "Quiz B1": [
                {"q": "The coffee ___ hot.", "a": ["is", "are", "am", "be"], "c": "is"},
                {"q": "She ___ an apple.", "a": ["eats", "eat", "eating", "eated"], "c": "eats"},
                {"q": "I ___ to the park.", "a": ["go", "goes", "going", "gone"], "c": "go"},
                {"q": "They ___ soccer.", "a": ["play", "plays", "playing", "played"], "c": "play"},
                {"q": "The bus ___ late.", "a": ["arrives", "arrive", "arriving", "arrived"], "c": "arrives"},
                {"q": "We ___ milk.", "a": ["buy", "buys", "buying", "bought"], "c": "buy"},
                {"q": "My house ___ big.", "a": ["is", "are", "am", "be"], "c": "is"},
                {"q": "The store ___ open.", "a": ["is", "are", "am", "be"], "c": "is"},
                {"q": "You ___ a car.", "a": ["have", "has", "having", "had"], "c": "have"},
                {"q": "It ___ a sunny day.", "a": ["is", "are", "am", "be"], "c": "is"}
            ],
            "Quiz B2 (No Spanish)": [
                {"q": "Which sentence is correct?", "a": ["Does he work here?", "Do he work here?", "Is he work here?", "He work here?"], "c": "Does he work here?"},
                {"q": "Negation of 'The house is clean':", "a": ["The house is not clean", "The house no is clean", "The house doesn't clean", "The house isn't be clean"], "c": "The house is not clean"},
                {"q": "Select the question:", "a": ["Do you travel often?", "You travel often?", "Are you travel often?", "Does you travel often?"], "c": "Do you travel often?"},
                {"q": "Negative form for 'I eat bread':", "a": ["I do not eat bread", "I no eat bread", "I am not eat bread", "I not eat bread"], "c": "I do not eat bread"},
                {"q": "Is the coffee ready?", "a": ["Yes, it is", "Yes, it does", "Yes, it are", "Yes, it am"], "c": "Yes, it is"},
                {"q": "Correct sentence for 'She':", "a": ["She does not like milk", "She do not like milk", "She is not like milk", "She no likes milk"], "c": "She does not like milk"},
                {"q": "The room ___ tidy.", "a": ["is", "are", "am", "be"], "c": "is"},
                {"q": "They ___ at home.", "a": ["are not", "is not", "am not", "not"], "c": "are not"},
                {"q": "___ it cost much?", "a": ["Does", "Do", "Is", "Are"], "c": "Does"},
                {"q": "We ___ time.", "a": ["do not have", "does not have", "no have", "are not have"], "c": "do not have"}
            ]
        }

        self.idx = 0
        self.active_data = []
        self.mode = ""
        self.score = 0
        self.locked = False

        self.setup_ui()

    def setup_ui(self):
        # HEADER
        self.hdr = ctk.CTkFrame(self, fg_color="transparent")
        self.hdr.pack(pady=20, fill="x")
        ctk.CTkLabel(self.hdr, text="EDU-DAILY ENGLISH", font=("Arial", 36, "bold"), text_color=COLOR_ACCENT).pack()
        ctk.CTkLabel(self.hdr, text="APRENDIZAJE COTIDIANO MULTITEMÁTICO", font=("Arial", 12), text_color=COLOR_NAV).pack()

        # MENÚ
        self.menu = ctk.CTkScrollableFrame(self, height=180, fg_color=COLOR_CARD, border_width=1, border_color=COLOR_NAV)
        self.menu.pack(pady=10, fill="x", padx=60)
        self.add_menu_group("LECCIONES DE VIDA", self.db_study, "study", COLOR_NAV)
        self.add_menu_group("EVALUACIONES", self.db_quiz, "quiz", "#0F172A")

        # NAVEGACIÓN
        self.nav = ctk.CTkFrame(self, fg_color="transparent")
        self.nav.pack(side="bottom", pady=30)
        self.btn_b = ctk.CTkButton(self.nav, text="⬅ ANTERIOR", width=250, height=75, fg_color=COLOR_NAV, font=("Arial", 16, "bold"), command=self.back)
        self.btn_n = ctk.CTkButton(self.nav, text="SIGUIENTE ➡", width=250, height=75, fg_color=COLOR_NAV, font=("Arial", 16, "bold"), command=self.next)

        # VISOR (CON SCROLL PARA RESPONSIVIDAD)
        self.view = ctk.CTkScrollableFrame(self, fg_color="#010409", corner_radius=25, border_width=2, border_color=COLOR_ACCENT)
        self.view.pack(pady=10, fill="both", expand=True, padx=60)

        self.txt = ctk.CTkLabel(self.view, text="LISTO PARA EMPEZAR\nSelecciona un tema común arriba.", font=("Arial", 22), text_color="#475569", wraplength=550)
        self.txt.pack(pady=50, padx=20)

        self.opts = ctk.CTkFrame(self.view, fg_color="transparent")
        self.opts.pack(fill="x", padx=40, pady=(0, 40))

    def add_menu_group(self, title, source, mode, color):
        ctk.CTkLabel(self.menu, text=title, font=("Arial", 11, "bold"), text_color=COLOR_ACCENT).pack(pady=5)
        for k in source.keys():
            ctk.CTkButton(self.menu, text=k, height=35, fg_color=color, command=lambda d=source[k], m=mode: self.load(d, m)).pack(pady=2, fill="x", padx=30)

    def load(self, data, mode):
        self.active_data = data
        self.mode = mode
        self.idx = 0
        self.score = 0
        self.locked = False
        self.clear_opts()
        if mode == "study":
            self.btn_b.grid(row=0, column=0, padx=15)
            self.btn_n.grid(row=0, column=1, padx=15)
            self.btn_n.configure(state="normal", text="SIGUIENTE ➡")
            self.show_study()
        else:
            self.btn_b.grid_forget()
            self.btn_n.grid_forget()
            self.show_quiz()

    def clear_opts(self):
        for w in self.opts.winfo_children(): w.destroy()

    def show_study(self):
        item = self.active_data[self.idx]
        msg = f"TEMA {self.idx + 1}/10\n\n{item[0]}\n━━━━━━━━━━━━━━━━\n{item[1]}\n━━━━━━━━━━━━━━━━\nPRONUNCIACIÓN: [{item[2]}]"
        self.txt.configure(text=msg, font=("Arial", 28, "bold"), text_color=COLOR_TEXT)

    def show_quiz(self):
        self.clear_opts()
        self.locked = False
        if self.idx < len(self.active_data):
            q = self.active_data[self.idx]
            self.txt.configure(text=f"PREGUNTA {self.idx + 1}/10\n\n{q['q']}", text_color=COLOR_ACCENT, font=("Arial", 26, "bold"))
            for a in q['a']:
                ctk.CTkButton(self.opts, text=a, height=60, fg_color=COLOR_CARD, font=("Arial", 16), command=lambda v=a: self.check(v)).pack(pady=5, fill="x")
        else:
            self.txt.configure(text=f"COMPLETADO\n\nRESULTADO: {self.score} / 10", text_color=COLOR_SUCCESS, font=("Arial", 32, "bold"))

    def check(self, val):
        if self.locked: return
        self.locked = True
        if val == self.active_data[self.idx]['c']:
            self.score += 1
            self.txt.configure(text="¡EXCELENTE! ✅", text_color=COLOR_SUCCESS)
            self.after(1000, self.auto)
        else:
            self.txt.configure(text="INTENTA DE NUEVO ❌\nRevisa la estructura.", text_color=COLOR_ERROR)
            self.clear_opts()
            ctk.CTkButton(self.opts, text="REINTENTAR", height=75, fg_color=COLOR_ERROR, font=("Arial", 18, "bold"), command=self.show_quiz).pack(pady=20, fill="x")

    def auto(self):
        self.idx += 1
        self.show_quiz()

    def next(self):
        if self.idx < len(self.active_data) - 1:
            self.idx += 1
            self.show_study()
        else:
            self.btn_n.configure(text="FIN", state="disabled")

    def back(self):
        if self.idx > 0:
            self.idx -= 1
            self.btn_n.configure(state="normal", text="SIGUIENTE ➡")
            self.show_study()

if __name__ == "__main__":
    app = EduDailyApp()
    app.mainloop()