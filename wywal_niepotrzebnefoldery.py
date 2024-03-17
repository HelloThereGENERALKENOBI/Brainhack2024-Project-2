import os
import shutil


def flatten_directory_for_tsv(source_dir, target_dir):
    """
    Przenosi wszystkie pliki .tsv z katalogu źródłowego i jego podkatalogów do jednego katalogu docelowego.

    :param source_dir: Ścieżka do katalogu źródłowego.
    :param target_dir: Ścieżka do katalogu docelowego.
    """
    # Sprawdzenie, czy katalog docelowy istnieje; jeśli nie, zostanie utworzony.
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".tsv"):  # Sprawdzenie, czy plik ma rozszerzenie .tsv
                # Tworzenie pełnej ścieżki do pliku źródłowego i docelowego
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)

                # Sprawdzenie, czy plik o takiej samej nazwie już istnieje w katalogu docelowym
                if os.path.exists(target_file):
                    # Dodanie prefiksu do nazwy pliku, aby uniknąć nadpisania
                    basename, extension = os.path.splitext(file)
                    counter = 1
                    new_target_file = os.path.join(
                        target_dir, f"{basename}_{counter}{extension}"
                    )
                    while os.path.exists(new_target_file):
                        counter += 1
                        new_target_file = os.path.join(
                            target_dir, f"{basename}_{counter}{extension}"
                        )
                    target_file = new_target_file

                # Przeniesienie pliku do katalogu docelowego
                shutil.move(source_file, target_file)


# Przykład użycia
source_dir = "RawData"  # Ścieżka do katalogu źródłowego
target_dir = "RawDataAleBezFolderow"  # Ścieżka do katalogu docelowego

flatten_directory_for_tsv(source_dir, target_dir)
