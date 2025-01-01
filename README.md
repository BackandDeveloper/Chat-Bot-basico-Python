Chatbot em Python
Este projeto é um chatbot simples desenvolvido em Python que responde a perguntas básicas. Ele pode ser expandido e personalizado conforme necessário.

Funcionalidades
Responde a perguntas básicas como saudações, nome, estado e capacidades.

Fácil de expandir com novas perguntas e respostas.

Como Usar
Clone este repositório para o seu ambiente local.

Certifique-se de ter o Python instalado em sua máquina.

Execute o script chatbot.py para iniciar o chatbot.

bash
git clone https://github.com/SeuUsuario/SeuRepositorio.git
cd SeuRepositorio
python chatbot.py
Estrutura do Código
O código principal está no arquivo chatbot.py. Ele contém uma função chatbot_response que mapeia as entradas do usuário para respostas predefinidas e uma função main que gerencia a interação com o usuário.

python
import random

def chatbot_response(user_input):
    responses = {
        "olá": "Olá! Como posso ajudar você hoje?",
        "qual é o seu nome?": "Eu sou um chatbot criado para responder suas perguntas.",
        "como você está?": "Estou bem, obrigado por perguntar! E você?",
        "o que você pode fazer?": "Posso responder perguntas básicas e ajudar com informações gerais.",
        "adeus": "Até logo! Tenha um ótimo dia!"
    }
    
    return responses.get(user_input.lower(), "Desculpe, não entendi sua pergunta. Pode reformular?")

def main():
    print("Bem-vindo ao chatbot! Digite 'adeus' para sair.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "adeus":
            print("Chatbot: Até logo! Tenha um ótimo dia!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e novas funcionalidades.
