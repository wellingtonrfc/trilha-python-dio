def exibir_extrato(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print("========= Informe a conta =========")
    conta_encontrada = False
    for conta in contas.keys():
        if usuarios[cpf] == contas[conta]['usuario']:
            print(conta)
            conta_encontrada = True
    if not conta_encontrada:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = input("=>")
    print()
    print("================ EXTRATO ===============")
    print(contas[conta]['extrato'] if contas[conta]['extrato'] else "Ainda não foram realizadas movimentações.")
    print()
    print(f"Saldo:{'\033[1;32m' if contas[conta]['saldo']>0 else '\033[1;31m'} R$ {contas[conta]['saldo']:.2f}\033[0m")
    print("=========================================")
    return (usuarios,contas)
def depositar(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print("========= Informe a conta =========")
    conta_encontrada = False
    for conta in contas.keys():
        if usuarios[cpf] == contas[conta]['cpf']:
            print(conta)
            conta_encontrada = True
    if not conta_encontrada:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = input("=>")
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
        return (usuarios,contas)
    if valor>=0:
        contas[conta]['saldo'] += valor
        contas[conta]['extrato'] += f"\033[1;32mDepósito: R$ {valor:.2f}\033[0m\n"
        print(f"\033[1;32mDepósito de {valor:0.2f} na conta {conta}realizado com sucesso!\033[0m")
    return (usuarios,contas)
def sacar(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print("========= Informe a conta =========")
    conta_encontrada = False
    for conta in contas.keys():
        if usuarios[cpf] == contas[conta]['cpf']:
            print(conta)
            conta_encontrada = True
    if not conta_encontrada:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = input("=>")
    if contas[conta]['numero_saques']>=3:
        print("\033[1;31mOperação falhou! Número máximo de saques excedido.\033[0m")
        return (usuarios,contas)
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
        return (usuarios,contas)
    
    if valor>limite:
        print("\033[1;31mOperação falhou! O valor do saque excede o limite.\033[0m")
    elif valor>contas[conta]['saldo']:
        print("\033[1;31mOperação falhou! Você não tem saldo suficiente.\033[0m")
    elif valor>0:
        contas[conta]['saldo'] -= valor
        contas[conta]['numero_saques'] += 1
        contas[conta]['extrato'] += f"\033[1;31mSaque: R$ {valor:.2f}\033[0m\n"
        print("\033[1;32mSaque realizado com sucesso!\033[0m")
    else:
        print("\033[1;31mOperação falhou! O valor informado é inválido.\033[0m")
    return (usuarios,contas)
def criar_usuario(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF (somente número): ")

    if cpf in usuarios.keys():
        print("\n\033[1;31m@@@ Já existe usuário com esse CPF! @@@\033[0m")
        return (usuarios,contas)

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    
    print("\033[1;32m=== Usuário criado com sucesso! ===\033[0m")
    
    return (usuarios,contas)
def criar_conta(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios.keys():
        print("\n\033[1;32m@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@\033[0m")
        return (usuarios,contas)
    conta = len(contas.keys()) + 1
    contas[f"{conta}"] = {"agencia": agencia,"cpf": cpf,"saldo":0,"numero_saques":0,"extrato":""}
    print(f"\n\033[1;32m=== Conta {conta} para o usuário {usuarios[cpf]['nome']} criada com sucesso! ===\033[0m")
    
    return (usuarios,contas)
def listar_contas(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(contas) == 0:
        print("\033[1;31m@@@ Nenhuma conta encontrada! @@@\033[0m")
        return (usuarios,contas)
    saida = "=" * 100
    for conta in contas.keys():
        saida = f"{saida}\nAgência:\033[1;32m{contas[conta]['agencia']}\033[0m"
        saida = f"{saida}\nC/C:\033[1;32m{conta}\033[0m"
        saida = f"{saida}\nTitular:\033[1;32m{usuarios[contas[conta]['cpf']]['nome']}\033[0m"
        saida = f"{saida}\n{'=' * 100}"
    print(saida)
    return (usuarios,contas)
operacoes = {
    "d": {
        "mensagem":"[d] \033[1;32m Depositaar\033[0m",
        "executar":depositar
    },
    "s": {
        "mensagem":"[s] \033[1;31m Sacar\033[0m",
        "executar":sacar
    },
    "e": {
        "mensagem":"[e] \033[1;34m Extrato\033[0m",
        "executar":exibir_extrato
    },
    "nc": {
        "mensagem":"[nc] \033[1;32mNova conta\033[0m",
        "executar":criar_conta
    },
    "lc": {
        "mensagem":"[lc] \033[1;34mListar contas\033[0m",
        "executar":listar_contas
    },
    "nu": {
        "mensagem":"[nu] \033[1;32mNovo usuário\033[0m",
        "executar":criar_usuario
    },
    "q": {
        "mensagem":"[q] Sair"
    }
}

if __name__ == "__main__":
    LIMITE_SAQUES = 3
    LIMITE_SAQUE = 500
    AGENCIA = "0001"
    usuarios = {}
    contas = {}

    while True:
        menu = f"================ MENU ================\n{'\n'.join([op['mensagem'] for op in operacoes.values()])}\n=> "
        try:
            opcao = input(menu)
            if opcao == "q":
                print("Saindo...")
                break
            elif opcao == '':
                print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m")
            else:
                print(f"Opção selecionada:{opcao}")
                usuarios , contas = operacoes[opcao]['executar'](usuarios=usuarios,contas=contas,agencia=AGENCIA,limite=LIMITE_SAQUE)
        except KeyboardInterrupt:
            print("\nExecução cancelada.")
            break
        except KeyError as error_key:
            print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m")
            print(error_key)
            
