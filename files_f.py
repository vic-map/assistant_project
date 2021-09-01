import shutil
import sys
from pathlib import Path

# Scan part begin
IMAGES = []
VIDEOS = []
DOCUMENTS = []
MUSIC = []
ARCH = []
OTHER = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": IMAGES,
    "JPG": IMAGES,
    "PNG": IMAGES,
    "SVG": IMAGES,
    "AVI": VIDEOS,
    "MP4": VIDEOS,
    "MOV": VIDEOS,
    "MKV": VIDEOS,
    "DOC": DOCUMENTS,
    "DOCX": DOCUMENTS,
    "TXT": DOCUMENTS,
    "PDF": DOCUMENTS,
    "XLSX": DOCUMENTS,
    "PPTX": DOCUMENTS,
    "MP3": MUSIC,
    "OGG": MUSIC,
    "WAV": MUSIC,
    "AMR": MUSIC,
    "ZIP": ARCH,
    "GZ": ARCH,
    "TAR": ARCH
}


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "JPG", "PNG", "SVG", "AVI", "MP4", "MOV", "MKV",
                                 "DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX", "MP3", "OGG",
                                 "WAV", "AMR", "ZIP", "GZ", "TAR", "OTHER"):
                FOLDERS.append(item)
                scan(item)
            continue

    extension = get_extension(item.name)
    new_name = folder / item.name
    if not extension:
        OTHER.append(new_name)
    else:
        try:
            current_container = REGISTERED_EXTENSIONS[extension]
            EXTENSION.add(extension)
            current_container.append(new_name)
        except KeyError:
            UNKNOWN.add(extension)
            OTHER.append(new_name)

# Scan part end
# Sort part begin


def handle_formats(file, root_folder: Path, dist: str):
    try:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        file.replace(target_folder / file.name)
    except FileNotFoundError:
        pass


def handle_other(file, root_folder, dist):
    try:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        file.replace(target_folder / file.name)
    except FileNotFoundError:
        pass


def handle_archive(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)  # create folder ARCH
    archive_folder = target_folder / file.name
    archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
    try:
        shutil.unpack_archive(str(file.resolve()),
                              str(archive_folder.resolve()))
    except FileNotFoundError:
        pass
    except OSError:
        pass
    except shutil.ReadError:
        archive_folder.rmdir()  # Если не успешно удаляем папку под  архив
        return
    file.unlink()  # Если успешно удаляем архив


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")


def main(folder):
    scan(folder)


for file in IMAGES:
    handle_formats(file, folder, "IMAGES")

for file in VIDEOS:
    handle_formats(file, folder, "VIDEOS")

for file in DOCUMENTS:
    handle_formats(file, folder, "DOCUMENTS")

for file in MUSIC:
    handle_formats(file, folder, "MUSIC")

for file in OTHER:
    handle_other(file, folder, "OTHER")

for file in ARCH:
    handle_archive(file, folder, "ARCH")

for f in FOLDERS:
    handle_folder(f)


# if __name__ == "__main__":
#     scan_path = sys.argv[1]
#     print(f"Start in folder: {scan_path}")

# search_folder = Path(scan_path)
# scan(search_folder)
# print(f"Images: {IMAGES}")
# print(f"Videos: {VIDEOS}")
# print(f"Documents: {DOCUMENTS}")
# print(f"Audios: {MUSIC}")
# print(f"Archives: {ARCH}")
# print(f"Unknown files: {OTHER}")
# print(f"There are file of types: {EXTENSION}")
# print(f"Unknown types of file: {UNKNOWN}")

# sort_folder = Path(scan_path)
# print(f"sort folder is: {sort_folder}")
# print(sort_folder.resolve())
# main(sort_folder.resolve())
