# T8 – předání automatických kontrol do guildy

Zdroj standardních skriptů a seznamu sekcí: [společný repozitář guild](https://github.com/krystofjelinek/4IT433-git-guild).

## Čtyři kontroly

- **Gitleaks:** prohledává celou Git historii na tajné údaje; oficiální Gitleaks CLI v Dockeru.
- **Ruff:** prochází Python, Fabric-exportované notebooky `notebook-content.py` a Jupyter notebooky.
- **Prefixy tabulek:** využívá existující `.github/scripts/check_table_names.py` a `.github/pr-checks.toml`.
- **README:** využívá existující `.github/scripts/check_readme_sections.py` a jeho povinné sekce.

V CI navíc běží čtyři pozitivní/negativní jednotkové testy kontrol tabulek a README.

## Rozdíl mezi repozitáři

Společný repozitář guild neobsahuje složku `fabric/` a nemá README squadu.
Proto se kontroly tabulek a projektového README spustí nad reálnými soubory
pouze v repozitáři s `fabric/`; v metodickém repozitáři ověřují jejich
funkčnost automatizované jednotkové testy.

## Přenos do společného repozitáře

- Doplnit `ruff`, `table-names`, `readme` a `checker-tests` jobs do existujícího
  `.github/workflows/pr-checks.yml`. Zachovat současné CI změny ostatních členů.
- Přidat `pyproject.toml` a `tests/test_ci_checks.py`.
- Stávající skripty a pravidla již ve společném repozitáři jsou; není potřeba je nahrazovat.
- Před zapnutím jako required status checks je vhodné sjednotit povolené
  provozní prefixy: `log_` ve standardu T8 vs. `ops_` v šabloně T7.

## Demonstrační PR

Pozitivní PR ukazuje úspěch všech jobů. Negativní PR obsahuje vytvoření
`cestujici` bez prefixu a odstraněnou povinnou sekci README; oba kontrolní
joby mají skončit FAIL. Záporný PR se nikdy nemerguje.

Pravidla platí pro *vytváření/zápis* tabulek. Pouhé čtení `dbo.CESTUJICI`
nesmí vyvolat chybu. Kontrola Gitleaks nikdy nevyžaduje vkládání skutečných klíčů.
