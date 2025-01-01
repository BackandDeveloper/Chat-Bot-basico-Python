#1: usuário executa o script.
#2: chatbot exibe uma mensagem de boas-vindas.
#3: usuário digita uma pergunta ou saudação.
#4: chatbot responde com base no dicionário de respostas predefinidas.
#5: loop continua até que o usuário digite 'adeus', momento em que o chatbot encerra a interação.

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
