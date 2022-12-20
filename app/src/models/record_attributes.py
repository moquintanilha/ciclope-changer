class Record:
    def __init__(self, name: str, identifier: str, weight: int, ip_address: str):
        self.name = name
        self.identifier = identifier
        self.weight = weight
        self.ip_address = ip_address

    def record(self):
        print(self.identifier, self.weight, self.ip_address, self.name)
