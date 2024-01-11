import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from windows_toasts import Toast, ToastDisplayImage, WindowsToaster
source_directory = r'E:\Downloads'
extension_to_directory = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".doc": "Word",
    ".docx": "Word",
    ".ppt": "PowerPoint",
    ".pptx": "PowerPoint",
    ".xlsx": "Excel",
    ".xls": "Excel",
    ".csv": "Excel",
    ".exe": "EXEs",
    ".txt": "Texts",
    ".log": "Texts",
    ".md": "Texts",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".msi": "MSIs",
    ".iso": "ISOs",
    ".zip": "ZIPs",
    ".rar": "ZIPs",
    ".tar": "ZIPs",
    ".tgz": "ZIPs",
    ".gz": "ZIPs",
    "7z": "ZIPs",
}

script_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = './assets/43-1024-3077657304.png'
absolute_image_path = os.path.join(script_directory, relative_path)

toaster = WindowsToaster('Organizo')
newToast = Toast()

newToast.AddImage(ToastDisplayImage.fromPath(absolute_image_path))


class OnMyWatch:
    watchDirectory = "E:\Downloads"

    def __init__(self):
        self.observer = Observer()
        self.handler = Handler()

    def process_existing_files(self):
        for file_name in os.listdir(self.watchDirectory):
            file_path = os.path.join(self.watchDirectory, file_name)
            if os.path.isfile(file_path):
                self.handler.moveFiles(file_path)

    def run(self):
        event_handler = Handler()
        self.process_existing_files()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=False)
        self.observer.start()
        newToast.text_fields = [
            "MyOrganizer has been Initiliazed Successfully"]
        toaster.show_toast(newToast)
        try:
            while True:
                continue
        except:
            self.observer.stop()
            newToast.text_fields = [
                "MyOrganizer has been Stopped Successfully"]
            toaster.show_toast(newToast)
            print("Observer Stopped")
        self.observer.join()


class Handler(FileSystemEventHandler):
    def moveFiles(self, f):
        print(f)
        if f.lower().endswith('.tmp'):
            print(f"Skipping temporary file - {f}")
            return
        file_name = os.path.basename(f)
        moved = False
        for extension, directory in extension_to_directory.items():
            if file_name.lower().endswith(extension):
                destination_path = os.path.join(
                    f'E:\Downloads\{directory}', file_name)
                try:
                    base, ext = os.path.splitext(file_name)
                    counter = 1
                    destination_file = f"{base}{ext}"
                    destination_path = os.path.join(
                        f'E:\Downloads\{directory}', destination_file)
                    while os.path.isfile(destination_path):
                        destination_file = f"{base}({counter}){ext}"
                        destination_path = os.path.join(
                            f'E:\Downloads\{directory}', destination_file)
                        counter += 1
                    shutil.move(f, destination_path)
                    moved = True
                    break
                except FileNotFoundError as e:
                    print(
                        f"File not found: {f}")
                    time.sleep(1)
                    return
                except PermissionError:
                    print(f"File '{f}' is in use, waiting...")
                    time.sleep(1)
                if moved:
                    break

        if not moved:
            self.handle_unrecognized_files(f)

        newToast.text_fields = [
            f"File '{file_name}' has been moved to '{directory if moved else 'Trash'}' Folder"]
        toaster.show_toast(newToast)
        print("Migration Completed")

    def handle_unrecognized_files(self, f):
        file_name = os.path.basename(f)
        base, ext = os.path.splitext(file_name)
        destination_file = f"{base}{ext}"
        destination_path = os.path.join(
            f'E:\Downloads\Trash', destination_file)
        try:
            counter = 1
            while os.path.isfile(destination_path):
                destination_file = f"{base}({counter}){ext}"
                destination_path = os.path.join(
                    f'E:\Downloads\Trash', destination_file)
                counter += 1
            shutil.move(f, destination_path)
        except FileNotFoundError as e:
            print(f"File not found: {f}")
            time.sleep(1)
        except PermissionError:
            print(f"File '{file_name}' is in use, waiting...")
            time.sleep(1)

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created' or event.event_type == 'modified':
            if not event.src_path.lower().endswith('.tmp'):
                print(f"Received event - {event.src_path}")
                print(event.event_type)
                self.moveFiles(event.src_path)


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
