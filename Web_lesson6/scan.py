import sys
from pathlib import Path

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


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    search_folder = Path(scan_path)
    scan(search_folder)
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Videos avi: {AVI_VIDEOS}")
    print(f"Videos mp4: {MP4_VIDEOS}")
    print(f"Videos mov: {MOV_VIDEOS}")
    print(f"Videos mkv: {MKV_VIDEOS}")
    print(f"Documents doc: {DOC_DOCUMENTS}")
    print(f"Documents docx: {DOCX_DOCUMENTS}")
    print(f"Documents txt: {TXT_DOCUMENTS}")
    print(f"Documents pdf: {PDF_DOCUMENTS}")
    print(f"Documents xlsx: {XLSX_DOCUMENTS}")
    print(f"Documents pptx: {PPTX_DOCUMENTS}")
    print(f"Musics mp3: {MP3_MUSICS}")
    print(f"Musics ogg: {OGG_MUSICS}")
    print(f"Musics wav: {WAV_MUSICS}")
    print(f"Musics amr: {AMR_MUSICS}")
    print(f"Archives: {ARCH}")
    print(f"Unknown files: {OTHER}")
    print(f"There are file of types: {EXTENSION}")
    print(f"Unknown types of file: {UNKNOWN}")
