def exibir_extrato(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(usuarios.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhum usuário cadastrado.\033[0m")
        return (usuarios,contas)
    if len(contas.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhuma conta cadastrada.\033[0m")
        return (usuarios,contas)
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print(f"{'=' * 15} Selecione  a conta {'=' * 15}")
    contas_usuario = []
    for conta in contas.keys():
        if cpf == contas[conta]['cpf']:
            contas_usuario.append(conta)
            print(f"{len(contas_usuario)} - {conta}")
            
    if len(contas_usuario) == 0:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = int(input("=>"))
    print()
    print(f"{'=' * 13} EXTRATO da conta {contas_usuario[conta-1]} {'=' * 13}")
    print(contas[contas_usuario[conta-1]]['extrato'] if contas[contas_usuario[conta-1]]['extrato'] else "Ainda não foram realizadas movimentações.")
    print(f"Saldo:{'\033[1;32m' if contas[contas_usuario[conta-1]]['saldo']>0 else '\033[1;31m'} R${contas[contas_usuario[conta-1]]['saldo']:.2f}\033[0m")
    print("=" * 50)
    return (usuarios,contas)
def depositar(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(usuarios.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhum usuário cadastrado.\033[0m")
        return (usuarios,contas)
    if len(contas.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhuma conta cadastrada.\033[0m")
        return (usuarios,contas)
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print(f"{'=' * 16}  Informe a conta {'=' * 16}")
    contas_usuario = []
    for conta in contas.keys():
        if cpf == contas[conta]['cpf']:
            contas_usuario.append(conta)
            print(f"{len(contas_usuario)} - {conta}")
            
    if len(contas_usuario) == 0:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = int(input("=>"))
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
        return (usuarios,contas)
    if valor>=0:
        contas[contas_usuario[conta-1]]['saldo'] += valor
        contas[contas_usuario[conta-1]]['extrato'] += f"\033[1;32mDepósito: R${valor:.2f}\033[0m\n"
        print(f"\033[1;32mDepósito de R${valor:0.2f} na conta {contas_usuario[conta-1]} realizado com sucesso!\033[0m")
    return (usuarios,contas)
def sacar(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(usuarios.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhum usuário cadastrado.\033[0m")
        return (usuarios,contas)
    if len(contas.keys()) == 0:
        print("\033[1;31mOperação falhou! Nenhuma conta cadastrada.\033[0m")
        return (usuarios,contas)
    cpf = input("Informe o CPF (somente número): ")
    if cpf not in usuarios.keys():
        print("\033[1;31mOperação falhou! Usuário não encontrado.\033[0m")
        return (usuarios,contas)
    print(f"{'=' * 16} Informe a conta {'=' * 16}")
    contas_usuario = []
    for conta in contas.keys():
        if cpf == contas[conta]['cpf']:
            contas_usuario.append(conta)
            print(f"{len(contas_usuario)} - {conta}")
            
    if len(contas_usuario) == 0:
        print(f"\033[1;31mOperação falhou! Nenhuma conta encontrada para o usuário {usuarios[cpf]['nome']}.\033[0m")
        return (usuarios,contas)
    conta = int(input("=>"))
    if contas[contas_usuario[conta-1]]['numero_saques']>=3:
        print("\033[1;31mOperação falhou! Número máximo de saques excedido.\033[0m")
        return (usuarios,contas)
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("\033[1;31mOperação falhou! O valor informado não é numérico.\033[0m")
        return (usuarios,contas)
    
    if valor>limite:
        print("\033[1;31mOperação falhou! O valor do saque excede o limite.\033[0m")
    elif valor>contas[contas_usuario[conta-1]]['saldo']:
        print("\033[1;31mOperação falhou! Você não tem saldo suficiente.\033[0m")
    elif valor>0:
        contas[contas_usuario[conta-1]]['saldo'] -= valor
        contas[contas_usuario[conta-1]]['numero_saques'] += 1
        contas[contas_usuario[conta-1]]['extrato'] += f"\033[1;31mSaque: R${valor:.2f}\033[0m\n"
        print(f"\033[1;32mSaque de R${valor:0.2f} da conta {contas_usuario[conta-1]} realizado com sucesso!\033[0m")
    else:
        print("\033[1;31mOperação falhou! O valor informado é inválido.\033[0m")
    return (usuarios,contas)
def criar_usuario(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF (somente número): ")

    if cpf in usuarios.keys():
        print(f"\n\033[1;31m{'@' * 9} Já existe usuário com esse CPF {'@' * 9}\033[0m")
        return (usuarios,contas)

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    
    print(f"\033[1;32m{'=' * 16} Usuário criado com sucesso {'=' * 16}\033[0m")
    
    return (usuarios,contas)
def criar_conta(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios.keys():
        print(f"\n\033[1;31m@@ Usuário não encontrado, nenhuma conta criada @@\033[0m")
        return (usuarios,contas)
    conta = f"{len(contas.keys()) + 1:05d}"
    contas[f"{conta}"] = {"agencia": agencia,"cpf": cpf,"saldo":0,"numero_saques":0,"extrato":""}
    print(f"\n\033[1;32m=== Conta {conta} criada para o usuário {usuarios[cpf]['nome']} ===\033[0m")
    
    return (usuarios,contas)
def listar_contas(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(contas) == 0:
        print(f"\033[1;31m{'@' * 12} Nenhuma conta encontrada {'@' * 12}\033[0m")
        return (usuarios,contas)
    saida = "=" * 50
    for conta in contas.keys():
        saida = f"{saida}\nAgência:\033[1;32m{contas[conta]['agencia']}\033[0m"
        saida = f"{saida}\nC/C:\033[1;32m{conta}\033[0m"
        saida = f"{saida}\nTitular:\033[1;32m{usuarios[contas[conta]['cpf']]['nome']}\033[0m"
        saida = f"{saida}\n{'=' * 50}"
    print(saida)
    return (usuarios,contas)
def listar_usuarios(*,usuarios:dict,contas:dict,agencia:str,limite:float) -> tuple:
    if len(usuarios) == 0:
        print(f"\033[1;31m{'@' * 11} Nenhum usuário cadastrado! {'@' * 11}\033[0m")
        return (usuarios,contas)
    saida = "=" * 50
    for usuario in usuarios.keys():
        saida = f"{saida}\nCPF:\033[1;32m{usuario}\033[0m"
        saida = f"{saida}\nNome:\033[1;32m{usuarios[usuario]['nome']}\033[0m"
        saida = f"{saida}\nData de nascimento:\033[1;32m{usuarios[usuario]['data_nascimento']}\033[0m"
        saida = f"{saida}\nEndereço:\033[1;32m{usuarios[usuario]['endereco']}\033[0m"
        saida = f"{saida}\n{'=' * 50}"
    print(saida)
    return (usuarios,contas)
operacoes = {
    "d": {
        "mensagem":"[d] \033[1;32m Depositar\033[0m",
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
    "nu": {
        "mensagem":"[nu] \033[1;32mNovo usuário\033[0m",
        "executar":criar_usuario
    },
    "nc": {
        "mensagem":"[nc] \033[1;32mNova conta\033[0m",
        "executar":criar_conta
    },
    "lu": {
        "mensagem":"[lu] \033[1;34mListar usuários\033[0m",
        "executar":listar_usuarios
    },
    "lc": {
        "mensagem":"[lc] \033[1;34mListar contas\033[0m",
        "executar":listar_contas
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
        menu = f"{'=' * 22} MENU {'=' * 22}\n{'\n'.join([op['mensagem'] for op in operacoes.values()])}\n=> "
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
            
