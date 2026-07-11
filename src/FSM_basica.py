import time

estado_atual = "REPOUSO"

print("=== INICIANDO BULBATECH ===")
print("Gatilhos válidos: ativar | sinal_alto | sinal_baixo | parar | erro | reset")

while True:
    print(f"\n[STATUS] Robô atualmente em: {estado_atual}")

    evento = input("Simule um evento/gatilho: ").strip().lower()

    if estado_atual == 'REPOUSO':
        if evento == 'ativar':
            estado_atual = 'PROCURANDO'
            print(f"\n[ACTION] Ativando procura por objeto")
        else:
            print(f"\n[ACTION] Nenhuma ação, mantendo {estado_atual}")
    elif estado_atual == 'PROCURANDO':
        if evento == 'sinal_alto':
            estado_atual = 'DETECTADO'
            print(f"\n[STATUS] Objeto identificado")
        elif evento in ['parar', 'reset']:
            estado_atual = 'REPOUSO'
            print(f"\n[ACTION] Operação cancelada, aguardando comandos.")
        elif evento == 'erro':
            estado_atual = 'ERRO'
            print(f"\n[STATUS] Timeout na procura ou erro inusitado")
    elif estado_atual == 'DETECTADO':
        if evento == 'sinal_baixo':
            estado_atual = 'PROCURANDO'
            print(f"\n[STATUS] Objeto saiu do campo de visão, retornando à {estado_atual}.")
        elif evento in ['parar', 'reset']:
            estado_atual = 'REPOUSO'
            print(f"\n[ACTION] Operação cancelada, aguardando comandos.")
        elif evento == 'erro':
            estado_atual = 'ERRO'
            print(f"\n[STATUS] Timeout na procura ou erro inusitado")
    elif estado_atual == 'ERRO':        
        if evento == 'reset':
            estado_atual = 'REPOUSO'
            print(f"\n[ACTION] Operação cancelada, aguardando comandos.")
    time.sleep(1)