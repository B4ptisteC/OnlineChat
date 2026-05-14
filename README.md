# Online Chat 💬

Ce projet a été développé avec `Voutouz` durant l'été entre la classe de première et de terminale. L'idée était de pouvoir s'envoyer des messages à travers une application faite par nous-mêmes. Ainsi est né OnlineChat ! De nombreuses versions ont été créées au fil du temps, celle-ci étant la plus aboutie de nos efforts.

## 🎯 Fonctionnalités

- **Chat en temps réel** : Communication instantanée entre utilisateurs grâce à WebSockets
- **Authentification** : Système de login simple avec mot de passe
- **Serveurs multiples** : Accès à différents canaux de chat facile à déployer. (Général, Lycée, etc.)
- **Suivi des utilisateurs** : Affichage du nombre de membres connectés
- **Interface responsive** : Design moderne
- **Horodatage** : Chaque message inclut l'heure et la zone horaire

## 📋 Prérequis

- Python 3.7+
- pip (gestionnaire de paquets Python)

## 🚀 Installation

1. **Clonez ou téléchargez le projet**

2. **Installez les dépendances**
   ```bash
   pip install flask flask-socketio python-socketio python-engineio
   ```

3. **Générez les certificats SSL**
   ```bash
   openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```

   ou

   ```bash
   "C:\Program Files\OpenSSL-Win64\bin\openssl" req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```

🔗 Lien d’installation d’OpenSSL sous Windows : https://slproweb.com/products/Win32OpenSSL.html



5. **Lancez l'application**
   ```bash
   python app.py
   ```

6. **Accédez à l'application**
   - Ouvrez votre navigateur et allez à `https://localhost:5001`

## 🔐 Identifiants

- **Mot de passe** : `pass`

## 🛠️ Utilisation

1. **Connexion** : Entrez le mot de passe sur la page de login
2. **Navigation** : Choisissez un serveur depuis la page d'accueil
3. **Envoi de messages** : Tapez votre message et appuyez sur Entrée ou cliquez sur l'icône d'envoi
4. **Déconnexion** : Cliquez sur le bouton "Se déconnecter"
   
## 📸 Screenshots

<div align="center">

<img width="1374" height="782" alt="image" src="https://github.com/user-attachments/assets/20b817e1-e957-426c-b89c-38c23592bc75" />

**Page de Login**

<img width="1306" height="748" alt="image" src="https://github.com/user-attachments/assets/5b9bfb74-f351-48f3-a5bd-1555f85b4781" />

**Page d'accueil**

<img width="1364" height="831" alt="image" src="https://github.com/user-attachments/assets/b3308269-c5a9-4801-a38b-a4579af977f8" />

**Chat en temps réel**

</div>

## 🎨 Caractéristiques techniques

- **Backend** : Flask avec Flask-SocketIO pour WebSockets
- **Frontend** : HTML5, CSS3, Bootstrap 4
- **Communication** : Socket.IO pour la transmission en temps réel
- **Sécurité** : Sessions Flask, HTTPS avec certificats SSL

## 📝 Notes

- Les messages incluent automatiquement l'heure et la zone horaire
- Le compteur de membres connectés se met à jour en temps réel
- Le chat utilise le broadcast pour que tous les utilisateurs reçoivent les messages


## ⚠️ Avertissements

- Cette application utilise un certificat SSL auto-signé pour le développement local
- Le mot de passe est stocké en dur dans le code (à usage développement uniquement)

## 👥 Créateurs

Créé par [**B4ptisteC**](https://github.com/B4ptisteC) et [**VOUTOUZ**](https://github.com/VoutouZ)
