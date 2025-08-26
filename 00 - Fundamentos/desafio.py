def extrato(saldo:float,operacoes:int,extrato:str,limite:float) -> None:
    print()
    print("================ EXTRATO ===============")
    print(extrato if extrato else "Ainda não foram realizadas movimentações.")
    print()
    print(f"Saldo:{'\033[1;32m' if saldo>0 else '\033[1;31m'} R$ {saldo:.2f}\033[0m")
    print("=========================================")
    return (saldo,operacoes,extrato)
def deposito(saldo:float,operacoes:int,extrato:str,limite:float) -> float:
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
        return (saldo,operacoes,extrato)
    if valor>=0:
        saldo += valor
        extrato += f"\033[1;32mDepósito: R$ {valor:.2f}\033[0m\n"
        print("\033[1;32mDepósito realizado com sucesso!\033[0m")
    return (saldo,operacoes,extrato)
def saque(saldo:float,operacoes:int,extrato:str,limite:float) -> float:
    if operacoes>=3:
        print("\033[1;31mOperação falhou! Número máximo de saques excedido.\033[0m")
    else:
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
            return (saldo,operacoes,extrato)
        
        if valor>limite:
            print("\033[1;31mOperação falhou! O valor do saque excede o limite.\033[0m")
        elif valor>saldo:
            print("\033[1;31mOperação falhou! Você não tem saldo suficiente.\033[0m")
        elif valor>0:
            saldo -= valor
            operacoes += 1
            extrato += f"\033[1;31mSaque: R$ {valor:.2f}\033[0m\n"
            print("\033[1;32mSaque realizado com sucesso!\033[0m")
        else:
            print("\033[1;31mOperação falhou! O valor informado é inválido.\033[0m")
    return (saldo,operacoes,extrato)

operacoes = {
    "d": {
        "mensagem":"[d] \033[1;32mDepósito\033[0m",
        "executar":deposito
    },
    "s": {
        "mensagem":"[s] \033[1;31mSaque\033[0m",
        "executar":saque
    },
    "e": {
        "mensagem":"[e] \033[1;34mExtrato\033[0m",
        "executar":extrato
    },
    "q": {
        "mensagem":"[q] Sair"
    }
}

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
if __name__ == "__main__":
    while True:
        menu = f"==== MENU ====\n{'\n'.join([op['mensagem'] for op in operacoes.values()])}\n==============\nselecione uma opção: "
        try:
            opcao = input(menu)
            if opcao == "q":
                print("Saindo...")
                break
            else:
                saldo,numero_saques, extrato = operacoes[opcao]['executar'](saldo,numero_saques,extrato,limite)
        except KeyboardInterrupt:
            print("\nExecução cancelada.")
            break
        except KeyError:
            print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m")
