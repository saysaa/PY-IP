import socket
import tkinter as tk

def get_local_ip():
    try:
        # Créer une socket de type IPv4 et UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connexion à une adresse IP publique (ici, Google DNS) pour obtenir l'IP locale
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Erreur: {e}"

def show_local_ip():
    ip = get_local_ip()
    ip_label.config(text=f"Votre adresse IP locale est : {ip}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("PY-iP")
root.geometry("600x450")
root.configure(bg="black")

# Créer un titre en rouge
title_label = tk.Label(root, text="PY-iP", font=("Arial", 24, "bold"), bg="black", fg="red")
title_label.pack(pady=(20, 5))

# Créer un sous-titre en jaune
subtitle_label = tk.Label(root, text="Saysaa - 0.1.0", font=("Arial", 12), bg="black", fg="yellow")
subtitle_label.pack(pady=(0, 20))

# Créer un label pour afficher l'adresse IP
ip_label = tk.Label(root, text="", font=("Arial", 16), bg="black", fg="white")
ip_label.pack(pady=20)

# Créer un bouton pour obtenir l'adresse IP
button = tk.Button(root, text="Obtenir mon IP Locale", command=show_local_ip, bg="purple", fg="white", font=("Arial", 14))
button.pack(pady=20)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
