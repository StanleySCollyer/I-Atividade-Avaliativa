from tkinter import *
import random
import threading

# Lista inicializa com o primeiro elemento = 0
lista = [0]

class CleanBot(Frame):
    def __init__(self, master):
        self.positionsave = ""
        self.EnergyLevel = 100
        self.contArmazenamento = 0
        super().__init__(master)
        self.timer = ""

        # Mensagem de Boas Vindas na tela
        Label(master, text="Bem-Vindo ao teste BotClean", font=("times", 16)).place(relx=0, rely=0.10, relwidth=1)

        # Informações do bot
        self.Battery = Label(master, text=f"Bateria {self.EnergyLevel}%", font=("times", 12))
        self.Battery.place(relx=0.05, rely=0.25)

        self.ArmazenamentoBot = Label(master, text=f"Armazenamento {self.contArmazenamento}/10", font=("times", 12))
        self.ArmazenamentoBot.place(relx=0.4, rely=0.25)

        self.StatusBot = Label(master, text=f"Bot Desligado", font=("times", 12))
        self.StatusBot.place(relx=0.75, rely=0.25)

        self.StatusBotColor = Label(master, bg="#E34444", font=("times", 12))
        self.StatusBotColor.place(relx=0.92, rely=0.265, relwidth=0.02, relheight=0.02)

        # Botões de comando
        Button(master, text="Gerar Campo", font=("times",16), command=self.GenerateMap).place(relx=0.75,rely=0.40, relwidth=0.2)
        Button(master, text="Iniciar Bot", font=("times", 16), command=self.iteracao_bot).place(relx=0.75, rely=0.55, relwidth=0.2)
        Button(master, text="Finalizar Bot", font=("times", 16), command=self.RestartMap).place(relx=0.75, rely=0.70,relwidth=0.2)

        # Frame do jogo
        self.Frame_Rectangle = Frame(master, bg='#FFF', bd='4')
        self.Frame_Rectangle.place(relx=0.05, rely=0.30, relwidth=0.60, relheight=0.60)

        # Primeira Linha do jogo
        self.loc1 = Label(self.Frame_Rectangle, text="", bg="#000", relief="sunken", bd=3)
        self.loc1.grid(row=0, column=0, sticky="nsew")

        self.loc2 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc2.grid(row=0, column=1, sticky="nsew")

        self.loc3 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc3.grid(row=0, column=2, sticky="nsew")

        self.loc4 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc4.grid(row=0, column=3, sticky="nsew")

        # Segunda Linha do jogo
        self.loc5 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc5.grid(row=1, column=0, sticky="nsew")

        self.loc6 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc6.grid(row=1, column=1, sticky="nsew")

        self.loc7 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc7.grid(row=1, column=2, sticky="nsew")

        self.loc8 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc8.grid(row=1, column=3, sticky="nsew")

        # Terceira Linha do jogo
        self.loc9 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc9.grid(row=2, column=0, sticky="nsew")

        self.loc10 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc10.grid(row=2, column=1, sticky="nsew")

        self.loc11 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc11.grid(row=2, column=2, sticky="nsew")

        self.loc12 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc12.grid(row=2, column=3, sticky="nsew")

        # Quarta Linha do jogo
        self.loc13 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc13.grid(row=3, column=0, sticky="nsew")

        self.loc14 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc14.grid(row=3, column=1, sticky="nsew")

        self.loc15 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc15.grid(row=3, column=2, sticky="nsew")

        self.loc16 = Label(self.Frame_Rectangle, text="", bg="#fff", relief="sunken", bd=3)
        self.loc16.grid(row=3, column=3, sticky="nsew")

        # Configuração para expansão da célula do grid
        self.Frame_Rectangle.grid_rowconfigure(0, weight=1)
        self.Frame_Rectangle.grid_rowconfigure(1, weight=1)
        self.Frame_Rectangle.grid_rowconfigure(2, weight=1)
        self.Frame_Rectangle.grid_rowconfigure(3, weight=1)

        self.Frame_Rectangle.grid_columnconfigure(0, weight=1)
        self.Frame_Rectangle.grid_columnconfigure(1, weight=1)
        self.Frame_Rectangle.grid_columnconfigure(2, weight=1)
        self.Frame_Rectangle.grid_columnconfigure(3, weight=1)

    # Função para gerar mapa de sujeira
    def GenerateMap(self):
        lista.clear()

        # Adiciona 16 elementos aleatórios (0 ou 1)
        for _ in range(16):
            lista.append(random.randint(0, 1))

        loc_labels = [
            self.loc1, self.loc2, self.loc3, self.loc4,
            self.loc5, self.loc6, self.loc7, self.loc8,
            self.loc9, self.loc10, self.loc11, self.loc12,
            self.loc13, self.loc14, self.loc15, self.loc16
        ]

        lista.clear()

        # Gera um número aleatório de 1 a 14
        num_numbers_to_store = random.randint(1, 14)

        # Adiciona 'num_numbers_to_store' números aleatórios de 1 a 15 na lista
        for _ in range(num_numbers_to_store):
            random_number = random.randint(1, 15)
            while random_number in lista:
                random_number = random.randint(1, 15)
            lista.append(random_number)

        for i, label in enumerate(loc_labels):
            if i + 1 in lista:  # Verifica se a posição está na lista
                label['bg'] = "#959595"
            else:
                label['bg'] = "#fff"

        self.loc1['bg'] = "orange"

    # Função para Movimentar o bot (Simulado de sensor e camera para detecção de sujeira)
      def CondicionalMoviment(self):
        # Simulado de controle de passos
        positions_to_check = [
            (1, 2, 6),
            (2, 3, 7),
            (3, 4, 8),
            (4, 3, 2),
            (6, 7, 11),
            (7, 8, 12),
            (8, 7, 6),
            (10, 11, 15),
            (11, 12, 16),
            (12, 11, 10),
            (13, 14, 15),
            (14, 15, 16),
            (15, 11, 7),
            (16, 12, 8),
        ]

        for pos1, pos2, pos3 in positions_to_check:
            if self.loc_dict[f'loc{pos1}']['bg'] == "yellow" and self.loc_dict[f'loc{pos2}']['bg'] == "#959595":
                self.Dischargebattery(2)
                self.FillStorage()
                if self.contArmazenamento == 10:
                    self.positionsave = pos2
                self.loc_dict[f'loc{pos1}']['bg'] = "#fff"
                self.loc_dict[f'loc{pos2}']['bg'] = "yellow"
                return self.iteracao_bot()
            elif self.loc_dict[f'loc{pos1}']['bg'] == "yellow" and self.loc_dict[f'loc{pos3}']['bg'] == "#959595":
                self.Dischargebattery(2)
                self.FillStorage()
                if self.contArmazenamento == 10:
                    self.positionsave = pos3
                self.loc_dict[f'loc{pos1}']['bg'] = "#fff"
                self.loc_dict[f'loc{pos3}']['bg'] = "yellow"
                return self.iteracao_bot()
            elif self.loc_dict[f'loc{pos1}']['bg'] == "yellow" and self.loc_dict[f'loc{pos2}']['bg'] == "#959595":
                self.Dischargebattery(2)
                if self.contArmazenamento == 10:
                    self.positionsave = pos2
                self.loc_dict[f'loc{pos1}']['bg'] = "#fff"
                self.loc_dict[f'loc{pos2}']['bg'] = "yellow"
                return self.iteracao_bot()

    # Função para movimentar e limpar o armazenamento do bot
    def ClearStorage(self, num):
        position = str(num)

        if position == '8':
            if self.loc8['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc8['bg'] = "#fff"
                self.loc7["bg"] = "yellow"
            elif self.loc7['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc7['bg'] = "#fff"
                self.loc6['bg'] = "yellow"
            elif self.loc6['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc6['bg'] = "#fff"
                self.loc2['bg'] = "yellow"
            elif self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1['bg'] = "yellow"
                self.contArmazenamento = 0
        if position == '7':
            if self.loc7['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc7['bg'] = "#fff"
                self.loc6['bg'] = "yellow"
            elif self.loc6['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc6['bg'] = "#fff"
                self.loc2['bg'] = "yellow"
            elif self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1['bg'] = "yellow"
                self.contArmazenamento = 0
        if position == '6':
            if self.loc6['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc6['bg'] = "#fff"
                self.loc2['bg'] = "yellow"
            elif self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1["bg"] = "yellow"
                self.contArmazenamento = 0
        if position == '4':
            if self.loc4['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc4['bg'] = "#fff"
                self.loc3['bg'] = "yellow"
            elif self.loc3['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc3['bg'] = "#fff"
                self.loc2['bg'] = "yellow"
            elif self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1['bg'] = "yellow"
                self.contArmazenamento = 0
        if position == '3':
            if self.loc3['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc3['bg'] = "#fff"
                self.loc2['bg'] = "yellow"
            elif self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1['bg'] = "yellow"
                self.contArmazenamento = 0
        if position == '2':
            if self.loc2['bg'] == "yellow":
                self.Dischargebattery(1)
                self.loc2['bg'] = "#fff"
                self.loc1['bg'] = "yellow"
                self.contArmazenamento = 0

        if self.contArmazenamento == 0:
            self.ArmazenamentoBot['text'] = f"Armazenamento {self.contArmazenamento}/10"
        return self.iteracao_bot()

    # Função para Finalizar o jogo
    def RestartMap(self):
        try:
            self.timer.cancel()
            self.timer2.cancel()
        except:
            pass

        self.loc1['bg'] = "#000"
        self.loc2['bg'] = "#fff"
        self.loc3['bg'] = "#fff"
        self.loc4['bg'] = "#fff"
        self.loc5['bg'] = "#fff"
        self.loc6['bg'] = "#fff"
        self.loc7['bg'] = "#fff"
        self.loc8['bg'] = "#fff"
        self.loc9['bg'] = "#fff"
        self.loc10['bg'] = "#fff"
        self.loc11['bg'] = "#fff"
        self.loc12['bg'] = "#fff"
        self.loc13['bg'] = "#fff"
        self.loc14['bg'] = "#fff"
        self.loc15['bg'] = "#fff"
        self.loc16['bg'] = "#fff"

        self.EnergyLevel = 100
        self.contArmazenamento = 0
        self.Battery['text'] = f"Bateria {self.EnergyLevel}%"
        self.ArmazenamentoBot['text'] = f"Armazenamento {self.contArmazenamento}/10"

        self.StatusBot['text'] = "Bot Desligado"
        self.StatusBotColor['bg'] = "#E34444"

    # Função para diminuir a bateria do bot de acordo com o uso
    def Dischargebattery(self, Lossnumber):
        self.EnergyLevel -= Lossnumber
        self.Battery['text'] = f"Bateria {self.EnergyLevel}%"

    # Função para preencher o armazenamento
    def FillStorage(self):
        self.contArmazenamento = self.contArmazenamento + 1
        self.ArmazenamentoBot['text'] = f"Armazenamento {self.contArmazenamento}/10"

    # Função que determina se o bot deve limpar o mapa ou esvaziar o armazenamento
    def iteracao_bot(self):
        self.StatusBot['text'] = "Bot Ligado"
        self.StatusBotColor['bg'] = "LimeGreen"
        if self.contArmazenamento == 10:
            try:
                self.timer.cancel()
                self.timer2.cancel()
            except:
                pass
            self.timer2 = threading.Timer(1, lambda: self.ClearStorage(self.positionsave))
            self.timer2.start()
        if self.contArmazenamento < 10:
            try:
                self.timer.cancel()
                self.timer2.cancel()
            except:
                pass
            self.timer = threading.Timer(1, self.CondicionalMoviment)
            self.timer.start()
