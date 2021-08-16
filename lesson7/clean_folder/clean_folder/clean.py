import sys
from pathlib import Path
import shutil
import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_MUSICS = []
OGG_MUSICS = []
WAV_MUSICS = []
AMR_MUSICS = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "ZIP": ARCH,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_MUSICS,
    'OGG': OGG_MUSICS,
    'WAV': WAV_MUSICS,
    'AMR': AMR_MUSICS
}


for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()

def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_other(file, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)  # create folder ARCH
    ext = Path(file).suffix
    folder_for_arch = normalize(file.name.replace(ext, ""))
    archive_folder = target_folder / folder_for_arch
    archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()  # Если не успешно удаляем папку под  архив
        return
    file.unlink()  # Если успешно удаляем архив


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")

def normalize(name: str) -> str:
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name

def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in (
                    "JPEG", "JPG", "PNG", "SVG", "OTHER", "ARCH", 'AVI', 'MP4', 'MOV', 'MKV', 'DOC', 'DOCX', 'TXT',
                    'PDF', 'XLSX', 'PPTX', 'MP3', 'OGG', 'WAV', 'AMR'):
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

def main(folder):

    for file in scan.JPEG_IMAGES:
        handle_image(file, folder, "JPEG")

    for file in scan.JPG_IMAGES:
        handle_image(file, folder, "JPG")

    for file in scan.PNG_IMAGES:
        handle_image(file, folder, "PNG")

    for file in scan.SVG_IMAGES:
        handle_image(file, folder, "SVG")

    for file in scan.AVI_VIDEOS:
        handle_image(file, folder, "AVI")

    for file in scan.MP4_VIDEOS:
        handle_image(file, folder, "MP4")

    for file in scan.MOV_VIDEOS:
        handle_image(file, folder, "MOV")

    for file in scan.MKV_VIDEOS:
        handle_image(file, folder, "MKV")

    for file in scan.DOC_DOCUMENTS:
        handle_image(file, folder, "DOC")

    for file in scan.DOCX_DOCUMENTS:
        handle_image(file, folder, "DOCX")

    for file in scan.TXT_DOCUMENTS:
        handle_image(file, folder, "TXT")

    for file in scan.PDF_DOCUMENTS:
        handle_image(file, folder, "PDF")

    for file in scan.XLSX_DOCUMENTS:
        handle_image(file, folder, "XLSX")

    for file in scan.PPTX_DOCUMENTS:
        handle_image(file, folder, "PPTX")

    for file in scan.MP3_MUSICS:
        handle_image(file, folder, "MP3")

    for file in scan.OGG_MUSICS:
        handle_image(file, folder, "OGG")

    for file in scan.WAV_MUSICS:
        handle_image(file, folder, "WAV")

    for file in scan.AMR_MUSICS:
        handle_image(file, folder, "AMR")

    for file in scan.OTHER:
        handle_other(file, folder, "OTHER")

    for file in scan.ARCH:
        handle_archive(file, folder, "ARCH")

    for f in scan.FOLDERS:
        handle_folder(f)

if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())
    main(sort_folder.resolve())

