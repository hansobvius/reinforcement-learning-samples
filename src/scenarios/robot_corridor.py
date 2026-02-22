import numpy as np
import time
import os

# --- PATH CONFIGURATION ---
# Define paths for data and models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

def train_model():
    # --- CONFIGURAÇÃO ---
    # 6 estados (pisos 0 a 5)
    # 2 ações (0: esquerda, 1: direita)
    TAMANHO_CORREDOR = 6 
    POSICAO_DIAMANTE = 5 
    
    # Caminho para o modelo salvo
    model_path = os.path.join(MODELS_DIR, 'q_table_corridor.npy')
    
    # Tenta carregar o cérebro se ele já existir, senão cria um novo
    if os.path.exists(model_path):
        print("🧠 Cérebro antigo encontrado! Carregando dados...")
        q_table = np.load(model_path)
    else:
        print("🆕 Nenhum cérebro antigo encontrado. Criando um novo com zeros...")
        # Criando a Tabela Q (Cérebro) com zeros
        # Linhas = Estados, Colunas = Ações
        q_table = np.zeros((TAMANHO_CORREDOR, 2)) 
    
    # Parâmetros de Aprendizado
    alpha = 0.5  # Taxa de aprendizado (quão rápido ele aceita novas verdades)
    gamma = 0.9  # Fator de desconto (visão de futuro)
    epsilon = 0.1 # Chance de fazer loucura (exploração)
    
    print("--- INÍCIO DO TREINO ---")
    
    # Vamos treinar por 10 episódios (tentativas)
    training_log = [] # List to store log data
    
    for episodio in range(10):
        estado_atual = 0 # Robô começa sempre na esquerda
        passos = 0
        game_over = False
        total_reward = 0
    
        print(f"\nEpisódio {episodio + 1}: Robô acordou no 0.")
    
        while not game_over:
            # 1. Escolher Ação (Estratégia do 'Epsilon-Greedy')
            if np.random.uniform(0, 1) < epsilon:
                acao = np.random.choice([0, 1]) # 10% de chance de agir aleatório
            else:
                acao = np.argmax(q_table[estado_atual]) # 90% de chance de usar o cérebro
    
            # 2. Executar Ação e ver o resultado
            # Se ação for 1 (direita), aumenta posição. Se 0 (esquerda), diminui.
            novo_estado = estado_atual + 1 if acao == 1 else estado_atual - 1
            
            # Regras de física (paredes)
            if novo_estado < 0:
                novo_estado = 0 # Bateu na parede esquerda
            elif novo_estado > 5:
                novo_estado = 5 # Não pode passar do diamante
    
            # 3. Definir Recompensa
            reward = 0
            if novo_estado == POSICAO_DIAMANTE:
                reward = 10 # ACHOU O DIAMANTE!
                game_over = True
            
            # 4. ATUALIZAR O CÉREBRO (A Mágica da Fórmula de Bellman simplificada)
            # Valor Antigo
            antigo_valor = q_table[estado_atual, acao]
            
            # O melhor valor do próximo estado (Olhando para o futuro)
            melhor_futuro = np.max(q_table[novo_estado])
            
            # Cálculo do novo valor
            novo_valor = antigo_valor + alpha * (reward + gamma * melhor_futuro - antigo_valor)
            
            # Escreve na tabela
            q_table[estado_atual, acao] = novo_valor
    
            # Move o robô fisicamente
            estado_atual = novo_estado
            passos += 1
            total_reward += reward
    
        # Log the episode data
        training_log.append(f"{episodio+1},{passos},{total_reward}\n")
        print(f"  -> Chegou no diamante em {passos} passos!")
    
    print("\n--- TREINO CONCLUÍDO ---")
    print("Veja o que a IA aprendeu (Tabela Q):")
    print("Linha = Piso (0 a 5) | Coluna 0 = Esq | Coluna 1 = Dir")
    print(q_table)
    
    # --- SAVING RESULTS ---
    # 1. Save the "Brain" (Model)
    np.save(model_path, q_table)
    print(f"\n[MODEL] Brain saved to: {model_path}")
    
    # 2. Save the Logs (Data)
    log_path = os.path.join(DATA_DIR, 'training_log.csv')
    with open(log_path, 'w') as f:
        f.write("Episode,Steps,TotalReward\n") # Header
        f.writelines(training_log)
    print(f"[DATA] Training logs saved to: {log_path}")

if __name__ == "__main__":
    train_model()
