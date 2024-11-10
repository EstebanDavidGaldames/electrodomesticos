class Electrodomestico:
    current = 'AC'
    frequency = '50 Hz'
    electrical_voltage = '220 V'

    def __init__(self, name, brand, model, color, efficiency):
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color
        self.efficiency = efficiency

    @property
    def consumption(self):
        if self.efficiency == 'A+++' or 'A++' or 'A+' or 'A' or 'B' or 'C':
            return f'Bajo comsumo ({self.efficiency})'
        elif self.efficiency == 'D' or 'E':
            return f'Consumo medio ({self.efficiency})'
        else:
            return f'Alto consumo ({self.efficiency})'
    
    @classmethod
    def get_voltage(cls):
        return f'{cls.electrical_voltage} - {cls.current} {cls.frequency}'
    
    @staticmethod
    def purpose():
        return f'Mejora su calidad de vida'
    
    def get_name(self):
        return f'Electrodoméstico: {self.name}'
    
    def get_brand(self):
        return f'Marca: {self.brand}'
    
    def get_model(self):
        return f'Modelo: {self.model}'
    
    def get_color(self):
        return f'Color: {self.color}'
