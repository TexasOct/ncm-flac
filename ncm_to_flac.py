# Python scrip to trans ncm to flac
import os
import pyinotify
import time

# Prepare the file path
NCM_converter_path = "/home/texas/NCMconverter"
files_path = "/home/texas/Music/CloudMusic"
target_type = ".ncm"

# System command
cmd = f"./NCMconverter -o {files_path} {files_path}/*.ncm"
rm = f"rm {files_path}/*{target_type}"

# Listen the files_path
events = pyinotify.IN_MOVED_TO
watcher = pyinotify.WatchManager()


class EventHandler(pyinotify.ProcessEvent):
    # Trans the .ncm to .flac
    def process_IN_MOVED_TO(self, event):
        if any(name.endswith(target_type) for name in os.listdir(files_path)):
            print("get start")
            os.chdir(NCM_converter_path)
            os.system(cmd)
            time.sleep(60)
            os.system(rm)
            print("Transfer complete!")


if __name__ == '__main__':
    handler = EventHandler()
    watcher.add_watch(f'{files_path}', events, rec=True)
    notifier = pyinotify.Notifier(watcher, handler)
    notifier.loop()
