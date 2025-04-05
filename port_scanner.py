
import os 
import socket
import threading

os.system('clear')  # Efface l'écran du terminal
# Couleurs terminal

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[93m"

# Nouveau banner personnalisé
banner = """===========================================
||   ‎𝚵𝚳𝚸𝚵𝚪𝚯𝚪 𝐒𝐔𝐊𝐔𝚴𝚫 NETWORK SECURITY SCAN   ||
||     Analyse des ports TCP/IP            ||
||     Script pour usage éthique           ||
===========================================
"""

# Affichage de la bannière
print(f"{RED}{banner}")

# Texte auteur
print(f"""{CYAN}Script By ‎𝚵𝚳𝚸𝚵𝚪𝚯𝚪 𝐒𝐔𝐊𝐔𝚴𝚫
Fonction : Analyse de sécurité réseau
Utilisation : Scanner les ports ouverts d'une cible
""")

# Fonction de scan d’un port
def scanner_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"{CYAN}Port {port} est OUVERT sur {ip}")
        with open("resultats_scan.txt", "a") as f:
            f.write(f"Port {port} ouvert sur {ip}\n")
    else:
        print(f"{RED}Port {port} est fermé sur {ip}")
    sock.close()

# Fonction avec multithreading
def scanner_ports(ip, ports):
    print(f"{GREEN}Scan en cours sur {ip}...\n")
    threads = []

    for port in ports:
        thread = threading.Thread(target=scanner_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Exécution
try:
    ip = input(f"{WHITE}Entrez l'adresse IP à scanner : ")
    start_port = int(input("Port de début : "))
    end_port = int(input("Port de fin : "))
    ports = list(range(start_port, end_port + 1))

    scanner_ports(ip, ports)

    print(f"{GREEN}\nScan terminé. Résultats sauvegardés dans 'resultats_scan.txt'.")

except KeyboardInterrupt:
    print(f"\n{RED}Scan interrompu par l'utilisateur.")
except Exception as e:
    print(f"{RED}Erreur : {e}")

