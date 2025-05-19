from user_repository import UserRepository

if __name__ == "__main__":
    repo = UserRepository(UserRepository.House.MARVEL)

    id_nuevo = repo.insert(
        hero="Spider-Man",
        name="Peter Parker",
        year=1962,
        bio="Un adolescente neoyorquino con poderes arácnidos.",
        items=["telarañas", "traje"],
        images=["spiderman1.jpg", "spiderman2.jpg"]
    )

    print("Documento insertado con ID:", id_nuevo)
