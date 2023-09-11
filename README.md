
# OWL NLP

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

Im Anschluss muss über den "Select OWL File" Button die AI4PD.owl Datei ausgewählt werden.

Danach kann über das "Input Text" Feld eine Eingabe vorgenommen werden. 
Über "Process Text" wird der eingegeben Text mit Hilfe von NLP analysiert und falls über OpenThesaurus Synonyme für die im Code festgelegten Worte gefunden werden, werden diese ersetzt.

Zuletzt kann über den Button "Execute" die Query gestartet werden. 


Viel Spaß beim Verwenden des Projekts!
