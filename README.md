
# OWL NLP GUI-Anwendung

Diese Anwendung ermöglicht die Verarbeitung und Analyse von RDF-Graphen (Resource Description Framework) in OWL (Web Ontology Language) und die Erstellung von SPARQL-Abfragen (SPARQL Protocol and RDF Query Language) durch natürliche Spracheingabe und GUI-Interaktion.

## Einrichtung und Installation

Bevor Sie das Programm ausführen können, müssen Sie sicherstellen, dass [Poetry](https://python-poetry.org/docs/) installiert ist.

### Installation von Poetry

Wenn Sie Poetry noch nicht installiert haben, können Sie es mit dem folgenden Befehl installieren:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Projekt-Abhängigkeiten installieren

Navigieren Sie zum Projektordner in Ihrem Terminal und führen Sie den folgenden Befehl aus, um die Python-Abhängigkeiten zu installieren:

```bash
poetry install
```

### SpaCy-Modell installieren

Nachdem Sie die Python-Abhängigkeiten installiert haben, müssen Sie das SpaCy-Sprachmodell installieren. Führen Sie den folgenden Befehl aus, um das Modell zu installieren:

```bash
poetry run python install_models.py
```

## Das Programm ausführen

Nachdem Sie alle Abhängigkeiten installiert haben, können Sie das Hauptskript des Programm ausführen mit:

```bash
poetry run python Ontology_NLP.py
```

## Das Programm benutzen

1. **Laden einer OWL-Datei:**
   - Verwenden Sie den "OWL-Datei auswählen" Button, um eine OWL-Datei zu laden. 

2. **Natürliche Spracheingabe verarbeiten:**
   - Geben Sie Text im "Input Text" Feld ein und klicken Sie auf "Text verarbeiten". 
   - Die Anwendung analysiert den Text und generiert eine SPARQL-Abfrage basierend auf NLP (Natural Language Processing). Falls über OpenThesaurus Synonyme für die im Code festgelegten Worte gefunden werden, werden diese ersetzt.

3. **SPARQL-Abfrage erstellen und ausführen:**
   - Erstellen Sie eine SPARQL-Abfrage über das GUI, indem Sie Werte aus den Dropdown-Menüs auswählen und auf "Zur Abfrage hinzufügen" klicken.
   - Führen Sie die Abfrage durch Klicken auf "Abfrage ausführen" aus.

4. **Erhaltene Ergebnisse:**
   - Die Ergebnisse der Abfrage werden im "Ergebnisse der Abfrage" Feld angezeigt.

5. **Zusätzliche Funktionen:**
   - Nutzen Sie die "Reset" Funktion, um alle Eingabefelder zurückzusetzen.
   - Für Hilfestellungen zur SPARQL-Syntax klicken Sie auf "SPARQL Syntax".


Viel Spaß beim Verwenden des Projekts!
