
#  Application CRM interne pour EpicEvents

Cette API Restful utilisant Django ORM est utilisée pour la gestion de relation clients entités de l'entreprise EpicEvents.

L'application permet essentiellement aux utilisateurs de transformer des prospect en client, de créer des contrats sur les clients et enfin de créer des événement sur les contrats.

Pour utiliser cette API, il est conseillé de se référer à sa [documentation](https://documenter.getpostman.com/view/15611753/UVCCd3QC).

## Prérequis

1. Installer [Python 3](https://www.python.org/downloads/).

2. Télécharger l'application via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/MaeRiz/OC_P12_EpicEvents/archive/refs/heads/master.zip).
```bash
git clone https://github.com/MaeRiz/OC_P12_EpicEvents.git
```

3. Créer un environnement virtuel et l'activer :
```cmd
python3 -m venv env
env\Scripts\activate
```

4. installer les modules :
```cmd
pip install -r requirements.txt
```

5. Faire les migrations:
```cmd
softdesk\manage.py makemigrations
softdesk\manage.py migrate
```
## Utilisation
### Lancer le serveur [Django](https://www.djangoproject.com/):
```cmd
softdesk\manage.py runserver
```
### Accès administrateur
- L'accès administrateur se fait a partir de l'adresse suivante: [localhost:8000/admin/](http://localhost:8000/admin/)
- Les administrateurs ont accès à tous les modèles.

### Accès utilisateur
- L'accès des utilisateurs (commercial / support) se fait via des points de terminaison de l'API.
- Les points de terminaison peuvent être testés avec l'application [Postman](https://www.postman.com/).