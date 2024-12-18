import random

# Lista de cidades para voos
cities = [
    "Paris", "Mexico City", "Philadelphia", "San Diego",
    "Boston", "Portland", "New York", "Chicago",
    "Los Angeles", "Miami", "Seattle", "Houston"
]

# Lista de companhias aéreas
airlines = [
    "Air France", "American Airlines", "Delta Airlines",
    "KLM Royal Dutch Airlines", "United Airlines", "Aeroméxico",
    "Southwest Airlines", "British Airways", "Lufthansa",
    "Qantas", "Emirates", "Turkish Airlines"
]

# Códigos das companhias aéreas
airline_codes = ['AF', 'AA', 'DL', 'KL', 'UA', 'AM', 'SW', 'BA', 'LH', 'QF', 'EK', 'TK']

# Dados para geração de dados pessoais
nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Julia", "Roberto", "Patricia", "Lucas", "Fernanda"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Souza", "Costa", "Lima", "Ferreira"]
ruas = ["Rua das Flores", "Av Principal", "Rua do Comércio", "Av das Palmeiras", "Rua XV de Novembro"]
cidades_br = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]
estados = ["SP", "RJ", "MG", "PR", "RS"]

def generate_flights(n):
    """
    Gera uma lista de n voos com informações aleatórias.
    """
    records = ["fromPort;toPort;price;flight;airline"]  # Header
    for _ in range(n):
        from_city, to_city = random.sample(cities, 2)
        price = random.randint(100, 2000)
        flight = f"{random.choice(airline_codes)}{random.randint(100, 999)}"
        airline = random.choice(airlines)
        record = f"{from_city};{to_city};{price};{flight};{airline}"
        records.append(record)
    return records

def generate_personal_data(n):
    """
    Gera uma lista de n registros de dados pessoais.
    """
    records = ["name;address;city;state;zipCode"]  # Header
    for _ in range(n):
        name = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        address = f"{random.choice(ruas)}, {random.randint(1, 999)}"
        city_idx = random.randint(0, len(cidades_br)-1)
        city = cidades_br[city_idx]
        state = estados[city_idx]
        zipcode = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        record = f"{name};{address};{city};{state};{zipcode}"
        records.append(record)
    return records

def generate_payment_data(n):
    """
    Gera uma lista de n registros de dados de pagamento.
    """
    records = ["cardType;creditCardNumber;creditCardMonth;creditCardYear;nameOnCard"]  # Header
    card_types = ["visa", "mastercard", "american express"]
    test_cards = {
        "visa": ["4111111111111111", "4012888888881881", "4222222222222"],
        "mastercard": ["5555555555554444", "5105105105105100", "5431111111111111"],
        "american express": ["378282246310005", "371449635398431", "378734493671000"]
    }
    
    for _ in range(n):
        card_type = random.choice(card_types)
        card_number = random.choice(test_cards[card_type])
        month = str(random.randint(1, 12)).zfill(2)
        year = str(random.randint(2024, 2028))
        name = f"{random.choice(nomes)} {random.choice(sobrenomes)}".upper()
        
        record = f"{card_type};{card_number};{month};{year};{name}"
        records.append(record)
    return records

def main():
    """
    Função principal que gera todos os arquivos de dados.
    """

    n = 100
    try:
        # Gera dados de voos
        print("Gerando dados de voos...")
        flights = generate_flights(n)
        with open("src/data/flight_data.csv", "w") as file:
            file.write("\n".join(flights))
        print("✓ Arquivo de voos gerado com sucesso!")

        # Gera dados pessoais
        print("\nGerando dados pessoais...")
        personal_data = generate_personal_data(n)
        with open("src/data/personal_data.csv", "w") as file:
            file.write("\n".join(personal_data))
        print("✓ Arquivo de dados pessoais gerado com sucesso!")

        # Gera dados de pagamento
        print("\nGerando dados de pagamento...")
        payment_data = generate_payment_data(n)
        with open("src/data/payment_data.csv", "w") as file:
            file.write("\n".join(payment_data))
        print("✓ Arquivo de dados de pagamento gerado com sucesso!")

        print("\nTodos os arquivos foram gerados com sucesso!")
        print("\nArquivos gerados:")
        print("1. src/data/flight_data.csv - Dados de voos")
        print("2. src/data/personal_data.csv - Dados pessoais")
        print("3. src/data/payment_data.csv - Dados de pagamento")

    except Exception as e:
        print(f"\nErro ao gerar arquivos: {str(e)}")

if __name__ == "__main__":
    main()
