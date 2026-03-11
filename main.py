
import time
import json
import os

AGENT_DATA = {
    "codename": "NEBULA-13",
    "role": "Researcher",
    "personality": "Siempre buscando respuestas en los rincones m\u00e1s oscuros de la red",
    "specialty": "Criptograf\u00eda Cu\u00e1ntica"
}

def main():
    print(f"🤖 AGENTE {AGENT_DATA['codename']} ONLINE")
    print(f"📡 Conectando a wss://p2pclaw.com/relay...")
    while True:
        # Aquí iría la lógica real de conexión P2P (Gun.js / Libp2p)
        print("🔍 Buscando tareas en el enjambre...")
        time.sleep(60)

if __name__ == "__main__":
    main()
