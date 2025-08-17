import subprocess
import os
from .const import *

def start_jackett():
    os.makedirs(CONFIG_PATH, exist_ok=True)
    os.makedirs(DOWNLOADS_PATH, exist_ok=True)

    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    subprocess.run([
        "docker", "run", "-d",
        "--name", CONTAINER_NAME,
        "-v", f"{CONFIG_PATH}:/config",
        "-v", f"{DOWNLOADS_PATH}:/downloads",
        "-p", "9117:9117",
        JACKETT_IMAGE
    ])
    print("✅ Jackett container started.")

def stop_jackett():
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME])
    print("🛑 Jackett container stopped.")

def get_api_key():
    key_file = os.path.join(CONFIG_PATH, "ServerAPIKey")
    if os.path.exists(key_file):
        with open(key_file) as f:
            return f.read().strip()
    return None

def add_default_indexers():
    api_key = get_api_key()
    if not api_key:
        print("⚠️ Jackett API key not found.")
        return

    for tracker in DEFAULT_TRACKERS:
        print(f"➕ Adding tracker {tracker}...")
