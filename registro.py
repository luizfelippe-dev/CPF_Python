import re

def main():
    input_value = input("Insira o CPF ou CNPJ: ")

    # Remove qualquer caractere que não seja número
    digits_only = re.sub(r'\D', '', input_value)

    # Verifica se é CPF ou CNPJ com base na quantidade de dígitos
    if len(digits_only) == 11:
        # Validação e formatação do CPF
        if is_valid_cpf(digits_only):
            formatted_cpf = format_cpf(digits_only)
            print("CPF formatado: " + formatted_cpf)
        else:
            print("Erro: CPF inválido.")
    elif len(digits_only) == 14:
        # Validação e formatação do CNPJ
        if is_valid_cnpj(digits_only):
            formatted_cnpj = format_cnpj(digits_only)
            print("CNPJ formatado: " + formatted_cnpj)
        else:
            print("Erro: CNPJ inválido.")
    else:
        print("Erro: Quantidade de dígitos inválida. Um CPF deve ter 11 dígitos e um CNPJ deve ter 14 dígitos.")

def is_valid_cpf(cpf):
    # Verifica se todos os dígitos são iguais (caso típico de CPF inválido)
    if cpf == cpf[0] * len(cpf):
        return False

    # Calcula os dígitos verificadores do CPF
    multiplicadores1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    temp_cpf = cpf[:9]
    soma = sum(int(temp_cpf[i]) * multiplicadores1[i] for i in range(9))

    resto = soma % 11
    digito = '0' if resto < 2 else str(11 - resto)

    temp_cpf += digito
    soma = sum(int(temp_cpf[i]) * multiplicadores2[i] for i in range(10))

    resto = soma % 11
    digito += '0' if resto < 2 else str(11 - resto)

    return cpf.endswith(digito)

def is_valid_cnpj(cnpj):
    # Verifica se todos os dígitos são iguais (caso típico de CNPJ inválido)
    if cnpj == cnpj[0] * len(cnpj):
        return False

    # Calcula os dígitos verificadores do CNPJ
    multiplicadores1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    temp_cnpj = cnpj[:12]
    soma = sum(int(temp_cnpj[i]) * multiplicadores1[i] for i in range(12))

    resto = soma % 11
    digito = '0' if resto < 2 else str(11 - resto)

    temp_cnpj += digito
    soma = sum(int(temp_cnpj[i]) * multiplicadores2[i] for i in range(13))

    resto = soma % 11
    digito += '0' if resto < 2 else str(11 - resto)

    return cnpj.endswith(digito)

def format_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def format_cnpj(cnpj):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

if __name__ == "__main__":
    main()
