from flask import Flask
import socket
import os

app = Flask(__name__)

NOM = "Khadija"
PRENOM_NOM = "Khadidjiatou_THIAM"  # personnalise avec ton vrai nom si besoin
VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <html>
        <head><title>Projet GitOps - {PRENOM_NOM}</title></head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>Bonjour, je suis {NOM} 👋</h1>
            <h2>Plateforme GitOps observable sur Kubernetes</h2>
            <p>Version de l'application : <b>{VERSION}</b></p>
            <p>Pod : <code>{hostname}</code></p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok", "user": NOM}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
