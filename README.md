# KI-Modelle im Vergleich · TechGarden Frankfurt

**Build. Code. Ship.**

Was können aktuelle KI-Modelle wirklich? Hier sammeln wir bei den TechGarden-Treffen in Frankfurt Tests und Ergebnisse: offene und geschlossene, europäische und nicht-europäische Modelle, an echten Aufgaben.

*English below.*

## Worum es geht

Über KI-Modelle wird viel behauptet. Wir probieren selbst aus und halten fest, was wir sehen:

- **Qualität:** Stimmt die Antwort? Ist sie brauchbar?
- **Tempo:** Wie lange dauert es bis zur Antwort?
- **Kosten:** Was kostet eine Anfrage?
- **Daten:** Wo läuft das Modell, und wohin gehen die Daten?

## Die Modelle

|  | Offen (Gewichte herunterladbar) | Geschlossen (nur über Anbieter) |
|---|---|---|
| **Europäisch** | z. B. Mistral (offene Modelle) | z. B. Mistral (große Modelle), Aleph Alpha |
| **Nicht-europäisch** | z. B. Llama, Qwen, DeepSeek, GLM | z. B. GPT, Claude, Gemini |

Die Liste ist ein Startpunkt. Jedes Modell, das jemand testen möchte, ist willkommen.

## So machst du mit

1. Such dir eine Aufgabe aus [`aufgaben/`](aufgaben/) oder bring eine eigene mit.
2. Stell dieselbe Aufgabe an zwei oder mehr Modelle.
3. Trag deine Ergebnisse in [`ergebnisse/ergebnisse.csv`](ergebnisse/ergebnisse.csv) ein, eine Zeile pro Modell und Aufgabe.
4. Längere Antworten, Skripte oder Notizen legst du als eigene Datei in `ergebnisse/` ab, zum Beispiel `ergebnisse/2026-11-12_dein-name_aufgabe-01.md`.
5. Pull Request stellen, fertig.

Ausprobieren kannst du die Modelle im Browser-Chat, über eine API oder lokal, zum Beispiel mit [Ollama](https://ollama.com) oder [LM Studio](https://lmstudio.ai).

## Spielregeln

- **Nur öffentliche Daten.** Keine vertraulichen Firmendaten, keine personenbezogenen Daten.
- **Keine API-Schlüssel oder Passwörter** im Repository, auch nicht in Skripten.
- **Genau notieren:** Modellname und Version, Datum, Zugang (Chat, API, lokal) und wichtige Einstellungen. Ohne diese Angaben lassen sich Ergebnisse nicht vergleichen.
- **Ehrlich bleiben:** Auch schlechte Ergebnisse und Fehler gehören in die Tabelle.
- Jeder ist willkommen, niemand muss Profi sein.

## Ordner

| Ordner | Inhalt |
|---|---|
| `aufgaben/` | Testaufgaben zum Ausprobieren |
| `ergebnisse/` | Ergebnistabelle und ausführliche Ergebnisse |
| `folien/` | Folien der Impulse bei den Treffen |

## Treffen

TechGarden-Treffen finden alle zwei Wochen donnerstags von 18 bis 21 Uhr in Frankfurt statt.

- **Erstes Treffen:** Donnerstag, 12. November 2026. Anmeldung: https://luma.com/ezi3o5tc
- Website: https://techgarden-frankfurt.de

## Lizenz

[MIT](LICENSE). Ergebnisse und Texte dürfen frei genutzt werden, mit Hinweis auf dieses Repository.

---

## English

**Comparing AI models · TechGarden Frankfurt.** At our meetups in Frankfurt we test open and closed, European and non-European AI models on real tasks and collect the results here: quality, speed, cost and where the data goes.

**How to contribute:** pick a task from `aufgaben/` or bring your own, run it on two or more models, add one line per model and task to `ergebnisse/ergebnisse.csv`, and open a pull request. Public data only, no API keys in the repository, always note model, version, date and access method.

Meetups every other Thursday, 6–9 pm, in Frankfurt. First meetup: 12 November 2026, https://luma.com/ezi3o5tc
