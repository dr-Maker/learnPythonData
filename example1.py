def run():
    poblacion_paises = {
        "Argentina": 45764,
        "Brasil": 76985,
        "Chile": 19267,
    }

    # print(poblacion_paises["Chile"])

    # print("Paises")
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # print("Poblacion")
    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais , poblacion in poblacion_paises.items():
        print("El pais : "+ pais+" tiene una poblacion "+ str(poblacion) + "M de personas" )


if __name__ == "__main__":
    run()
