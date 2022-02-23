def limpa_str_numerica(s):
    ns = ""
    for digito in s:
        if digito in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            ns += digito
    return ns


def verifica_cpf(cpf):
    cpf = limpa_str_numerica(cpf)
    pesos1 = (10, 9, 8, 7, 6, 5, 4, 3, 2)
    pesos2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    soma1 = 0
    soma2 = 0
    if not len(cpf) == 11:
        return False
    for i in range(9):
        soma1 += int(cpf[i]) * pesos1[i]
    for i in range(10):
        soma2 += int(cpf[i]) * pesos2[i]
    valido1 = (cpf[9] == str(11 - (soma1 % 11))) or (cpf[9] == "0" and soma1 % 11 < 2)
    valido2 = (cpf[10] == str(11 - (soma2 % 11))) or (cpf[10] == "0" and soma2 % 11 < 2)
    valido3 = False
    digito2 = cpf[0]
    for digito in cpf:
        if digito != digito2:
            valido3 = True
        digito2 = digito
    return (valido1) and (valido2) and (valido3)


def verifica_cnpj(cnpj):
    cnpj = limpa_str_numerica(cnpj)
    pesos1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    pesos2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    soma1 = 0
    soma2 = 0
    if not len(cnpj) == 14:
        return False
    for i in range(12):
        soma1 += int(cnpj[i]) * pesos1[i]
    for i in range(13):
        soma2 += int(cnpj[i]) * pesos2[i]
    valido1 = (cnpj[12] == str(11 - (soma1 % 11))) or (
        cnpj[12] == "0" and soma1 % 11 < 2
    )
    valido2 = (cnpj[13] == str(11 - (soma2 % 11))) or (
        cnpj[13] == "0" and soma2 % 11 < 2
    )
    valido3 = False
    digito2 = cnpj[0]
    for digito in cnpj:
        if digito != digito2:
            valido3 = True
        digito2 = digito
    return (valido1) and (valido2) and (valido3)


def normaliza_cpf(cpf):
    cpf = limpa_str_numerica(cpf)
    return (
        cpf[0]
        + cpf[1]
        + cpf[2]
        + "."
        + cpf[3]
        + cpf[4]
        + cpf[5]
        + "."
        + cpf[6]
        + cpf[7]
        + cpf[8]
        + "-"
        + cpf[9]
        + cpf[10]
    )


def normaliza_cnpj(cnpj):
    cnpj = limpa_str_numerica(cnpj)
    return (
        cnpj[0]
        + cnpj[1]
        + "."
        + cnpj[2]
        + cnpj[3]
        + cnpj[4]
        + "."
        + cnpj[5]
        + cnpj[6]
        + cnpj[7]
        + "/"
        + cnpj[8]
        + cnpj[9]
        + cnpj[10]
        + cnpj[11]
        + "-"
        + cnpj[12]
        + cnpj[13]
    )


def normaliza_nome_arquivo(instance, nome_arquivo):
    default = "default.jpg"
    id = instance["id"]
    extensoes3 = (".png", ".gif", ".jpg")
    extensoes4 = (".jpeg", ".webp")
    extensao = ""
    if nome_arquivo[-4:] in extensoes3:
        extensao = nome_arquivo[-4:]
    elif nome_arquivo[-5:] in extensoes4:
        extensao = nome_arquivo[-5:]
    else:
        return default
    nome_arquivo = "usuario_" + str(id) + extensao
    return nome_arquivo
