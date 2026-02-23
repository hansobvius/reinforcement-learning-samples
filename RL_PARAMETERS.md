# Parâmetros de Aprendizado por Reforço

Em Aprendizado por Reforço (Reinforcement Learning), o agente (nosso robô) aprende por tentativa e erro. Para que ele aprenda de forma eficiente usando algoritmos como o Q-Learning, usamos três parâmetros matemáticos principais: **Alpha ($\alpha$)**, **Gamma ($\gamma$)** e **Epsilon ($\epsilon$)**.

Abaixo estão as explicações do que cada um deles faz, com analogias para facilitar o entendimento.

---

## 1. Alpha ($\alpha$) - A Taxa de Aprendizado
**O que é na prática:** Define o quanto o agente confia na **nova informação** que acabou de descobrir em comparação com o que ele **já sabia** antes.
* Se fosse **0**: O agente é teimoso. Ele nunca aprende nada novo e fica preso apenas na sua primeira impressão.
* Se fosse **1**: O agente tem "memória curta". Ele esquece tudo o que aprendeu no passado e só considera a última coisa que aconteceu.
* **No valor comum (ex: 0.5):** É um meio-termo. Quando o agente descobre algo novo, ele atualiza a tabela de conhecimento misturando 50% do conhecimento antigo com 50% da descoberta recente.

> **Analogia:** Imagine que o GPS diz que o caminho para o trabalho leva 30 minutos. Hoje você pegou trânsito e levou 50 minutos. Se o seu Alpha for alto, amanhã você já sai achando que a viagem demora 50 minutos sempre. Se for um Alpha equilibrado, você pensa: *"Bom, a média agora deve ser uns 40 minutos"*.

---

## 2. Gamma ($\gamma$) - O Fator de Desconto (Visão de Futuro)
**O que é na prática:** Define o quanto o agente se importa com as **recompensas de longo prazo** versus as **recompensas imediatas**.
* Se fosse **0**: O agente é imediatista. Ele só liga para o benefício do passo exato que está dando agora. Não consegue planejar nada para o futuro.
* Se for próximo de **1 (ex: 0.9 ou 0.99)**: O agente é estrategista. Ele aceita dar alguns passos sem ganhar nada (ou até perder alguns pontos iniciais) se souber que lá no final vai obter a recompensa principal.
* **No valor comum (ex: 0.9):** Dá ao agente uma excelente visão de longo prazo. Ele vai preferir um caminho que leve até o objetivo final mesmo que dê trabalho chegar até lá.

> **Analogia:** Você quer emagrecer. A recompensa imediata (Gamma = 0) é comer um pedaço de bolo agora. A recompensa futura (Gamma = 0.9) é ter saúde e atingir seu peso ideal daqui a alguns meses. Um Gamma alto faz o agente "resistir ao bolo" pelo objetivo maior.

---

## 3. Epsilon ($\epsilon$) - A Taxa de Exploração
**O que é na prática:** É a porcentagem de vezes que o agente vai ignorar o conhecimento obtido e escolher uma **ação completamente aleatória**. Isso resolve o dilema entre *Explorar* (descobrir coisas novas) e *Explotar* (usar o que já sabe que funciona).
* Se fosse **0**: O agente só faria o caminho que ele já conhece. O perigo disso é ele descobrir um caminho "nota 6" e passar a vida inteira repetindo ele, sem nunca tentar ver se existia um atalho "nota 10" do lado.
* Se fosse **1**: O agente agiria como se estivesse bêbado, andando para qualquer lado 100% do tempo.
* **No valor comum (ex: 0.1):** Em 90% das vezes, o agente vai olhar sua tabela de aprendizado e tomar a melhor decisão inteligente. Mas em 10% das vezes (0.1), ele vai "jogar os dados" e tentar um movimento aleatório. Essa "loucura" garante que ele eventualmente explore o cenário inteiro e não fique preso em caminhos sub-ótimos. Em ambientes complexos, é comum fazer o Epsilon decair ao longo do tempo (começar explorando muito e no fim focar no caminho encontrado).

> **Analogia:** Imagine que você vai a uma sorveteria. Você sabe que o sorvete de chocolate é muito bom (Explotação). Mas e se o de pistache for incrível e você nunca provou? Com Epsilon 0.1, em 9 em cada 10 idas à sorveteria você pede chocolate, mas 1 vez você arrisca um sabor aleatório (Exploração) só para ver se descobre um novo favorito.
