# T8 · GitHub Actions – návod

Tento repozitář je testovací prostředí pro git guildu T8 (nikoliv repozitář squadu).
Workflow najdete v `.github/workflows/pr-checks.yml`.

## Automatické kontroly

1. **Ruff** spouští `ruff check .` nad běžnými `.py`, `.ipynb` a
   soubory `fabric/**/notebook-content.py`, do kterých Microsoft Fabric exportuje notebooky.
2. **Gitleaks** kontroluje historii Git na nechtěně zveřejněné klíče, tokeny
   nebo hesla. Používáme CLI přes Docker, nikoliv placenou GitHub Action.

Kontroly se spouštějí při pull requestu do `main`.

## Specifika Fabric notebooků

Microsoft Fabric zapisuje více buněk notebooku do jednoho `notebook-content.py`.
Proto pro tyto soubory v `pyproject.toml` ignorujeme výhradně `E402`
(import nemusí být na začátku souboru). Další pravidla Ruff zůstávají aktivní.

## Demonstrační pull requesty

- PR #1: platné soubory, kontroly mají projít.
- PR #2: `examples/intentional_ruff_error.py` s nedefinovanou proměnnou,
  Ruff má hlásit `F821`.

## Předání guildě

Zkopírujte `.github/workflows/pr-checks.yml` a `pyproject.toml` do
relevantního repozitáře. Po dohodě s druhým členem T8 doplňte kontrolu
prefixů vytvářených tabulek a sekcí README. Před označením kontrol za
povinné nejprve ověřte jejich kompatibilitu s notebooky všech squadů.
