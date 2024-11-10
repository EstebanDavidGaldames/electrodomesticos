from electrodomesticos import Electrodomestico


def main():
    producto_1 = Electrodomestico('Aire acondicionado', 'PHILCO', 'PHS32H4ACN', 'Blanco', 'A')
    producto_2 = Electrodomestico('Aire acondicionado', 'BGH', 'Bsi65wcgt', 'Blanco', 'A')
    
    print('Objetos de tipo \'Electrodomestico\' instanciados:')
    print('\nPrimer producto creado:\n')
    print(f'{producto_1.get_name()}\n{producto_1.get_brand()}\n{producto_1.get_model()}\n{producto_1.get_color()}\n{producto_1.consumption}')
    print(producto_1.get_voltage())
    print(producto_1.purpose())
    print('\nSegundo producto creado:\n')
    print(f'{producto_2.get_name()}\n{producto_2.get_brand()}\n{producto_2.get_model()}\n{producto_2.get_color()}\n{producto_2.consumption}')
    print(producto_2.get_voltage())
    print(producto_2.purpose())


if __name__ == '__main__':
    main()
