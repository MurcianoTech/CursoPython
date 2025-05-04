class Person:
    _name: str
    _lastname:str

    def __init__(self, name, lastname):
        self._name = name
        self._lastname = lastname

class Client(Person):
    __accountNumber: str
    __balance: float

    def __init__(self, name: str, lastname: str, acoountNumber: str, balance: float):
        super().__init__(name, lastname)

        self.__accountNumber = acoountNumber
        self.__balance = balance

    def __str__(self) -> str:
        return f"""
            Número de cuenta -> {self.__accountNumber}
            Balance -> {self.__balance}
        """

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f"Se ha depositado en la cuenta {amount}")

    def withdraw(self, amount: float) -> None:
        self.__balance -= amount
        print(f"Se ha retirado de la cuenta {amount}")

def createClient() -> Client:
    return Client('Alejandro', 'Valenzuela', '1234567', 0.0)

def init(client: Client) -> None:
    print("""
    Elige alguna de estas opciones
        [1] Depositar dinero
        [2] Retirar dinero
        [3] Consultar estado cuenta
        [4] Salir 
    """)

    option = int(input('Introduce la acción a realizar'))

    match(option):
        case 1:
            amount = float(input('Introduce la cantidad a depositar'))
            client.deposit(amount)
            print(client)
        case 2:
            amount = float(input('Introduce la cantidad a retirar'))
            client.withdraw(amount)
            print(client)
        case 3:
            print(client)
        case 4:
            exit()

client = createClient()

while True:
    init(client)
