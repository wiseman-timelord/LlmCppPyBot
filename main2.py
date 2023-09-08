from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import yaml
import os

class Watcher:
    DIRECTORY_TO_WATCH = "./data"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def process(event):
        if event.src_path.endswith("config.yaml"):
            display_interface()

    def on_modified(self, event):
        self.process(event)

def read_yaml(file_path='./data/config.yaml'):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading config.yaml: {e}")
        return None

def display_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 89)
    print("                                   Dialogue Display")
    print("=" * 89)
    data = read_yaml()
    if data:
        human_name = data.get('human_name', "Empty")
        model_name = data.get('model_name', "Empty")
        model_current = data.get('model_current', "Empty")
        model_emotion = data.get('model_emotion', "Empty")
        session_history = data.get('session_history', "Empty")
        human_current = data.get('human_current', "Empty")
    
    print(f" {human_name}'s Input")
    print("-" * 89)
    print(f" {human_current}\n\n")
    print("=-" * 44)
    print(f" {model_name}'s Response")
    print("-" * 89)
    print(f" {model_current}\n\n")
    print("=-" * 44)
    print(f" {model_name}'s State")
    print("-" * 89)
    print(f" {model_emotion}\n\n")  
    print("=-" * 44)
    print(" Event History")
    print("-" * 89)
    print(f" {session_history}\n\n")
    print("=" * 89)
    print("\n Listening for changes in ./data/config.yaml...")

if __name__ == '__main__':
    display_interface()
    w = Watcher()
    w.run()