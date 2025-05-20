from user_repository import UserRepository

if __name__ == "__main__":
    repo = UserRepository(UserRepository.House.MARVEL)

    # id_nuevo = repo.insert(
    #     hero="Spider-Man",
    #     name="Peter Parker",
    #     year=1962,
    #     bio="Un adolescente neoyorquino con poderes arácnidos.",
    #     items=["telarañas", "traje"],
    #     images=["spiderman1.jpg", "spiderman2.jpg"]
    # )

    # print("Documento insertado con ID:", id_nuevo)

    # resultado = repo.get_hero_by_name("Spider-Man")
    # print(resultado)
    # resultado2 = repo.get_hero_by_id(resultado)
    # print(resultado2)

    # actualizacion = repo.update_hero(resultado,
    #     "Spider-Man",
    #     "Peter Parker",
    #     1962,
    #     "Joven huérfano nativo de Forest Hills, Queens, en Nueva York, que vive con sus tíos May y Ben. Durante su etapa como estudiante de la ficticia Midtown High School, es mordido por una araña radiactiva en una exhibición científica y «adquiere la agilidad y la fuerza proporcional de un arácnido».",
    #     ["telarañas", "traje"],
    #     ["spiderman1.jpg", "spiderman2.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Spider-Man.jpg/1920px-Spider-Man.jpg"]
    # )
    #print(actualizacion)

    # heroe_a_borrar = repo.insert_hero(
    #     hero="Spoder-Mon",
    #     name="Pedro Estacionador",
    #     year=2691,
    #     bio="Un anciano santafesino con poderes de mosquito.",
    #     items=["telarañas", "traje"],
    #     images=["spiderman1.jpg", "spiderman2.jpg"]
    # )
    # print("Documento insertado con ID:", heroe_a_borrar)

    # resultado = repo.get_hero_by_name("Spoder-Mon")
    # resultado2 = repo.get_hero_by_id(resultado)
    # print(resultado2)
    # print(repo.delete_hero(resultado))
    # resultado2 = repo.get_hero_by_id(resultado)
    # print("\nSi se borró, ahora no hay nada: ", resultado2)