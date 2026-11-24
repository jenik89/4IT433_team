"""Minimalni ukazka Python kodu pro kontrolu Ruff v projektu 4IT433."""


def normalize_table_name(name: str) -> str:
    """Vrat nazev tabulky malymi pismeny bez okolnich mezer."""
    return name.strip().lower()


if __name__ == "__main__":
    print(normalize_table_name(" CESTUJICI "))
