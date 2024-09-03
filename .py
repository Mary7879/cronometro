import time
import threading

class Cronometro:
    def __init__(self):
        self.tempo_decorrido = 0
        self.ativo = False
        self.thread = None

    def iniciar(self):
        if not self.ativo:
            self.ativo = True
            self.thread = threading.Thread(target=self._executar)
            self.thread.start()
        else:
            print("O cronômetro já está em execução.")

    def parar(self):
        if self.ativo:
            self.ativo = False
            self.thread.join()
        else:
            print("O cronômetro já está parado.")

    def resetar(self):
        self.tempo_decorrido = 0
        if self.ativo:
            self.parar()
            self.iniciar()

    def _executar(self):
        inicio = time.time()
        while self.ativo:
            time.sleep(1)
            self.tempo_decorrido = time.time() - inicio
            self._mostrar_tempo()

    def _mostrar_tempo(self):
        minutos, segundos = divmod(int(self.tempo_decorrido), 60)
        horas, minutos = divmod(minutos, 60)
        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
        print(f"\r{tempo_formatado}", end='')

# Exemplo de uso
if __name__ == "__main__":
    cronometro = Cronometro()
    
    try:
        print("Pressione Enter para iniciar o cronômetro.")
        input()
        cronometro.iniciar()
        
        print("\nPressione Enter para parar o cronômetro.")
        input()
        cronometro.parar()

        print("\nPressione Enter para reiniciar o cronômetro.")
        input()
        cronometro.resetar()

        print("\nPressione Enter para parar o cronômetro e sair.")
        input()
        cronometro.parar()

    except KeyboardInterrupt:
        cronometro.parar()
        print("\nCronômetro interrompido.")


