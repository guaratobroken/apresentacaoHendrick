import serial
import time

# Configurações do porto serial (substitua conforme necessário)
PORTA_SERIAL = 'COM3'  # Ou '/dev/ttyUSB0' no Linux
BAUD_RATE = 9600

# Função para inicializar a comunicação com o microcontrolador
def inicializar_robô():
    try:
        # Abrir a porta serial
        robô = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
        print("Conexão com o braço robótico estabelecida.")
        return robô
    except Exception as e:
        print(f"Erro ao conectar com o robô: {e}")
        return None

# Função para mover o braço robótico até uma posição (x, y, z)
def mover_para_posicao(robô, x, y, z):
    if robô is not None:
        comando = f'MOVER {x} {y} {z}\n'  # Comando para mover o robô para as coordenadas x, y, z
        robô.write(comando.encode())  # Enviar o comando via serial
        print(f"Movendo para: X={x}, Y={y}, Z={z}")
        time.sleep(2)  # Aguardar 2 segundos para o movimento ser realizado
    else:
        print("Erro: Não há comunicação com o robô.")

# Função para pegar a peça da esteira
def pegar_peca(robô):
    if robô is not None:
        print("Pegando peça da esteira...")
        robô.write(b'PEGAR\n')  # Comando para acionar o garfo ou pinça do robô
        time.sleep(1)  # Aguardar o tempo necessário para pegar a peça
    else:
        print("Erro: Não há comunicação com o robô.")

# Função para colocar a peça em um local específico
def colocar_peca(robô, x, y, z):
    if robô is not None:
        print(f"Colocando a peça em: X={x}, Y={y}, Z={z}")
        mover_para_posicao(robô, x, y, z)  # Mover para a posição de destino
        robô.write(b'COLOCAR\n')  # Comando para soltar a peça
        time.sleep(1)  # Aguardar o tempo necessário para soltar a peça
    else:
        print("Erro: Não há comunicação com o robô.")

# Função principal do processo de automação
def processo_producao(robô):
    # Defina as coordenadas de destino
    destino_pegada = (100, 200, 50)  # Posição para pegar a peça
    destino_colocacao = (300, 400, 50)  # Posição para colocar a peça

    # Iniciar processo de pegar e colocar peças
    pegar_peca(robô)
    mover_para_posicao(robô, *destino_pegada)
    colocar_peca(robô, *destino_colocacao)

if __name__ == "__main__":
    robô = inicializar_robô()
    
    if robô:
        while True:
            processo_producao(robô)  # Processo contínuo para pegar e colocar peças
            time.sleep(5)  # Aguarda 5 segundos antes do próximo ciclo
