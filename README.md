
# Mein Projekt

## Einrichtung und Installation

Bevor Sie das Projekt ausführen können, müssen Sie sicherstellen, dass [Poetry](https://python-poetry.org/docs/) installiert ist.

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

## Das Projekt ausführen

Nachdem Sie alle Abhängigkeiten installiert haben, können Sie das Hauptskript des Projekts ausführen mit:

```bash
poetry Ontology_NLP.py
```

Viel Spaß beim Verwenden des Projekts!
