# Etude de la propagation d'une rumeur sur un réseau

## Premiere installation

### installer uv :

sur macOS et Linux : 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

sur Windows : 
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Récupérer le dossier

```bash
git clone https://github.com/cyberoctav/rumeur-reseau.git
cd rumeur-reseau
uv sync
```

## Utilisation 

- git pull          récupérer le travail des autres
- uv run pytest     vérifier que rien n'est cassé
- git add / commit  enregistrer
- git push          publier

## Lancer le code 
```bash
uv run python mon_script.py
```

## Règles dépot

Travailler sur une branche. Pour la créer : 
```bash
git switch -c nom_branche  
```
			     
Lancer les tests avant de pousser pour être sûr que tout passe
