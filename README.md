Automação de Braço Robótico com Comunicação Serial
Este projeto permite controlar um braço robótico via comunicação serial (RS-232), realizando tarefas de automação como pegar e colocar peças em locais específicos. O código foi desenvolvido para ser executado em um ambiente com Python e comunicação serial, sendo compatível com sistemas Windows e Linux.

Requisitos
Python 3.x
Biblioteca pyserial para comunicação serial
Porta serial disponível no sistema (exemplo: COM3 no Windows ou /dev/ttyUSB0 no Linux)
Para instalar o pyserial, execute o comando:

bash
Copiar código
pip install pyserial
Descrição do Código
Principais Funções
inicializar_robô()

Estabelece a conexão com o braço robótico através da porta serial especificada.
Configura a taxa de transmissão (baud rate) e o tempo limite para a comunicação.
mover_para_posicao(x, y, z)

Envia um comando para o braço robótico se mover para uma posição específica no espaço 3D (x, y, z).
Aguarda 2 segundos para garantir que o movimento seja completado.
pegar_peca()

Envia um comando para o robô pegar uma peça da esteira.
A comunicação é realizada pela porta serial, e o robô aguarda 1 segundo para o processo de captura.
colocar_peca(x, y, z)

Envia o comando para o robô mover-se para uma posição de destino e soltar a peça.
processo_producao()

Controla o ciclo contínuo de pegar e colocar peças em locais pré-determinados.
O processo inclui mover o robô para as posições de pegar e de colocar a peça, executando esses comandos de maneira sequencial.
Estrutura do Código
Configuração de Porta Serial:
A porta serial e a taxa de transmissão são configuráveis nas variáveis PORTA_SERIAL e BAUD_RATE. Certifique-se de ajustar o valor de PORTA_SERIAL de acordo com o seu sistema operacional (ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux).

Loop Principal:
O loop principal executa o processo de automação repetidamente, com uma pausa de 5 segundos entre os ciclos.

Como Usar
Conecte o Braço Robótico à porta serial especificada.
Execute o Código:
Inicie o script Python diretamente no terminal ou via IDE de sua preferência. O programa irá automaticamente tentar estabelecer a conexão com o robô e executar o processo de automação.
bash
Copiar código
python automacao_robô.py
Monitoramento:
O status da conexão e as ações do robô (mover, pegar, colocar) serão exibidos no terminal.
Exemplo de Saída
plaintext
Copiar código
Conexão com o braço robótico estabelecida.
Pegando peça da esteira...
Movendo para: X=100, Y=200, Z=50
Colocando a peça em: X=300, Y=400, Z=50
Considerações
Certifique-se de que o braço robótico está configurado para aceitar os comandos recebidos pela porta serial.
A taxa de transmissão (baud rate) deve ser compatível entre o computador e o robô.
O código foi desenvolvido para funcionar em ciclos contínuos; ajuste conforme necessário para o seu caso de uso.
