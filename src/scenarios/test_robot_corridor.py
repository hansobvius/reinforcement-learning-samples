import numpy as np
import os
import time

# --- PATH CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODELS_DIR, 'q_table_corridor.npy')

def test_model():
    print("--- TESTE DO ROBÔ NO CORREDOR ---")
    
    # 1. Verifica se o modelo treinado existe
    if not os.path.exists(MODEL_PATH):
        print(f"\n❌ ERRO: O cérebro (modelo) não foi encontrado no caminho:")
        print(f"   {MODEL_PATH}")
        print("👉 Você precisa rodar o script de treinamento ('robot_corridor.py') primeiro.")
        return

    print("🧠 Cérebro encontrado! Carregando dados...")
    q_table = np.load(MODEL_PATH)
    
    print("\n[ Tabela Q carregada ]")
    print(q_table)

    print("\n--- INICIANDO SIMULAÇÃO ---")
    TAMANHO_CORREDOR = 6
    POSICAO_DIAMANTE = 5

    estado_atual = 0  # Robô sempre começa na posição 0
    passos = 0
    max_passos = 10   # Limite de passos para evitar loops infinitos
    
    # Função para desenhar o corredor no terminal
    def desenhar_corredor(pos_robo):
        corredor = ["_"] * TAMANHO_CORREDOR
        corredor[POSICAO_DIAMANTE] = "💎"
        if pos_robo == POSICAO_DIAMANTE:
             corredor[pos_robo] = "🤖💎"
        else:
             corredor[pos_robo] = "🤖"
        return " ".join(corredor)

    print(f"Início : {desenhar_corredor(estado_atual)}")

    # 2. Roda a simulação apenas USANDO a Tabela Q (sem fator aleatório)
    while estado_atual != POSICAO_DIAMANTE and passos < max_passos:
        passos += 1
        
        # A Mágica do Teste: Pegar sempre a melhor ação da Tabela Q
        # 0 = Esquerda, 1 = Direita
        acao = np.argmax(q_table[estado_atual])
        
        if acao == 1:
            nome_acao = "Direita ->"
            novo_estado = estado_atual + 1
        else:
            nome_acao = "<- Esquerda"
            novo_estado = estado_atual - 1

        # Bloqueio das paredes
        if novo_estado < 0:
            novo_estado = 0
        elif novo_estado > 5:
            novo_estado = 5

        estado_atual = novo_estado
        
        time.sleep(0.6) # Atraso para visualização
        print(f"Passo {passos}: {nome_acao.ljust(12)} | {desenhar_corredor(estado_atual)}")

    if estado_atual == POSICAO_DIAMANTE:
        print(f"\n✅ SUCESSO! O robô lembrou de tudo e chegou ao diamante em {passos} passos!")
    else:
        print(f"\n❌ FALHA! O robô não chegou ao diamante. O treinamento precisa de mais episódios.")

if __name__ == "__main__":
    test_model()
