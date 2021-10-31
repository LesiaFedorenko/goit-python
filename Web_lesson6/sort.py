import sys
from pathlib import Path
import shutil
import scan
from normalize import normalize
import asyncio
import time


async def handle_file(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


async def handle_archive(file: Path, root_folder: Path, dist):
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


async def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")


async def main(folder):
    scan.scan(folder)

    for file in scan.JPEG_IMAGES:
        await handle_file(file, folder, "JPEG")

    for file in scan.JPG_IMAGES:
        await handle_file(file, folder, "JPG")

    for file in scan.PNG_IMAGES:
        await handle_file(file, folder, "PNG")

    for file in scan.SVG_IMAGES:
        await handle_file(file, folder, "SVG")

    for file in scan.AVI_VIDEOS:
        await handle_file(file, folder, "AVI")

    for file in scan.MP4_VIDEOS:
        await handle_file(file, folder, "MP4")

    for file in scan.MOV_VIDEOS:
        await handle_file(file, folder, "MOV")

    for file in scan.MKV_VIDEOS:
        await handle_file(file, folder, "MKV")

    for file in scan.DOC_DOCUMENTS:
        await handle_file(file, folder, "DOC")

    for file in scan.DOCX_DOCUMENTS:
        await handle_file(file, folder, "DOCX")

    for file in scan.TXT_DOCUMENTS:
        await handle_file(file, folder, "TXT")

    for file in scan.PDF_DOCUMENTS:
        await handle_file(file, folder, "PDF")

    for file in scan.XLSX_DOCUMENTS:
        await handle_file(file, folder, "XLSX")

    for file in scan.PPTX_DOCUMENTS:
        await handle_file(file, folder, "PPTX")

    for file in scan.MP3_MUSICS:
        await handle_file(file, folder, "MP3")

    for file in scan.OGG_MUSICS:
        await handle_file(file, folder, "OGG")

    for file in scan.WAV_MUSICS:
        await handle_file(file, folder, "WAV")

    for file in scan.AMR_MUSICS:
        await handle_file(file, folder, "AMR")

    for file in scan.OTHER:
        await handle_file(file, folder, "OTHER")

    for file in scan.ARCH:
        await handle_archive(file, folder, "ARCH")

    for f in scan.FOLDERS:
        await handle_folder(f)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")
    start = time.time()

    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())
    event_loop=asyncio.get_event_loop()

    event_loop.run_until_complete(main(sort_folder.resolve()))
    end = time.time() - start
    print(end)
