# Dicionário de adjetivos gentílicos dos estados brasileiros
adjetivos_gentilicos = {
    "Acre": "acreano",
    "Alagoas": "alagoano",
    "Amapá": "amapaense",
    "Amazonas": "amazonense",
    "Bahia": "baiano",
    "Ceará": "cearense",
    "Distrito Federal": "brasiliense",
    "Espírito Santo": "capixaba",
    "Goiás": "goiano",
    "Maranhão": "maranhense",
    "Mato Grosso": "mato-grossense",
    "Mato Grosso do Sul": "sul-mato-grossense",
    "Minas Gerais": "mineiro",
    "Pará": "paraense",
    "Paraíba": "paraibano",
    "Paraná": "paranaense",
    "Pernambuco": "pernambucano",
    "Piauí": "piauiense",
    "Rio de Janeiro": "carioca",
    "Rio Grande do Norte": "potiguar",
    "Rio Grande do Sul": "gaúcho",
    "Rondônia": "rondoniano",
    "Roraima": "roraimense",
    "Santa Catarina": "catarinense",
    "São Paulo": "paulista",
    "Sergipe": "sergipano",
    "Tocantins": "tocantinense"
}

# Solicita ao usuário o estado de nascimento
estado = input("Estado onde nasceu: ").capitalize()

# Verifica se o estado está no dicionário
if estado in adjetivos_gentilicos:
    adjetivo = adjetivos_gentilicos[estado]
    print(f"Você é {adjetivo}!")
else:
    print("Você é de outro estado.")
