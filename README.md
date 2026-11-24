# T8 GitHub Actions – kompletní demonstrační projekt

Testovací implementace všech kontrol T8 v osobním repozitáři. Data i notebooky
jsou demonstrační, nejde o skutečný produkční projekt squadu.

## Tým a role

T8 je Git guilda pro návrh automatických kontrol pull requestů. Člen A
zodpovídá za workflow, Gitleaks a Ruff; člen B za pravidla tabulek a README.
Předání jednotlivým squadům probíhá přes review a společný standard.

## Architektura a struktura workspace

Kontroly se spouští v GitHub Actions při každém pull requestu do main.
Demonstrační notebook je uložen ve složce fabric a skripty kontrol v
.github/scripts. Data Microsoft Fabric se během CI nenačítají.

## Konvence pojmenování

Tabulky vytvářené v Bronze začínají bronze_ a ve Silver silver_.
Názvy se píší malými písmeny a používají podtržítka. Technické výjimky
jsou definované ve sdíleném konfiguračním souboru.

## Datové zdroje a licence

Tento test nepoužívá externí datové zdroje ani cizí datové soubory.
Demonstrační názvy tabulek a ukázky Python kódu jsou vytvořené jen
pro ověření fungování CI a nevztahuje se na ně datová licence.

## Ingest a Bronze

Ukázkový Fabric notebook obsahuje metodu saveAsTable, která zapisuje
tabulku s názvem bronze_cestujici. Při CI se notebook pouze staticky
kontroluje a do žádného lakehouse se data skutečně nezapisují.

## Kontrola počtů řádků zdroj a Bronze

Protože se jedná o ukázkové řešení bez skutečných dat, nejsou k dispozici
počty zdrojových řádků. Kontrola správnosti názvů a čitelnosti kódu
probíhá nezávisle na počtech a přístupu do databáze.

## Silver a pravidla čištění

V demonstračním projektu Silver datová vrstva fyzicky nevzniká. Standard
pro squady vyžaduje silver_ prefix pro cílové tabulky a dokumentaci
čištění a transformací konkrétních datových sad.

## Kvalita dat (DQ)

Automatické kontroly T8 ověřují syntaxi a základní pravidla vývoje,
nikoliv kvalitu skutečných dat. Testování datových typů, NULL hodnot
a duplicit musí probíhat samostatně na úrovni jednotlivých squadů.

## Průběžný sběr dat a zdůvodnění kapacity

Tento test nespouští žádný pravidelný ingest ani nákladné Spark úlohy.
GitHub Actions se aktivuje až vytvořením nebo aktualizací PR do main,
takže není potřeba trvalý běh datové infrastruktury.

## Osobní údaje a pseudonymizace

V ukázkovém projektu nejsou osobní údaje klientů ani cestujících.
Tajné hodnoty a tokeny se nesmí ukládat do repozitáře; Gitleaks hledá
jejich nechtěný výskyt v Git historii.

