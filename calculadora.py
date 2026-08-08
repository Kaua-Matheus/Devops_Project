CUPOM_PERCENTUAIS = {
    "DEVOPS10": 10,
    "BOASVINDAS5": 5,
}


def obter_desconto_do_cupom(cupom):
    if cupom is None:
        return 0

    codigo = cupom.strip().upper()

    if codigo not in CUPOM_PERCENTUAIS:
        raise ValueError("Cupom promocional inválido")

    return CUPOM_PERCENTUAIS[codigo]


def calcular_total(itens, desconto_percentual=0, cupom=None):
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    desconto_total = desconto_percentual + obter_desconto_do_cupom(cupom)
    desconto_total = min(desconto_total, 100)

    total = subtotal * (1 - desconto_total / 100)

    return round(total, 2)