import os
from datetime import datetime, timedelta
from PyPDF2 import PdfMerger
import glob

# 1. Przygotowanie daty i folderu docelowego
wczorajsza_data = datetime.now() - timedelta(days=1)
nazwa_miesiaca = wczorajsza_data.strftime("%m_%B")  # np. '06_Czerwiec'
folder_bazowy = r'C:\ścieżka\do\pdf' #<- wprowadź ściżkę gdzie są zapisane pdfy. W tym miejscu powstanie folder docelowy.
folder_docelowy = os.path.join(folder_bazowy, nazwa_miesiaca)

if not os.path.exists(folder_docelowy):
    os.makedirs(folder_docelowy)
    print(f"Utworzono folder: {folder_docelowy}")

# 2. Zbieranie plików PDF z aktualnego folderu
pdf_files = glob.glob("*.pdf")
pdf_files.sort()

if not pdf_files:
    print("❌ Brak plików PDF do scalania!")
    exit()

# 3. Scalanie plików
merger = PdfMerger()

print("rozpoczynam scalanie:")
for pdf in pdf_files:
    print(f"+{pdf}")
    merger.append(pdf)

# 4. Tworzenie ścieżki do zapisu pliku:
nazwa_pliku = wczorajsza_data.strftime('%d.%m')+".pdf"
sciezka_docelowa = os.path.join(folder_docelowy, nazwa_pliku)

# 5. Zapis tylko jeśli są strony
if merger.pages:
    merger.write(sciezka_docelowa)
    merger.close()
    print(f"Połączony plik zapisany jako: {sciezka_docelowa}")

    # 6. Usuwanie plików źródłowych (zabezpieczone)
    try:
        for pdf in pdf_files:
            if os.path.abspath(pdf) != os.path.abspath(sciezka_docelowa):
                os.remove(pdf)
                print(f"Usunięto: {pdf}")
    except PermissionError as e:
        print(f"❌ Nie można usunąć pliku {pdf}, bo jest otwarty. Zamknij go i spróbuj ręcznie.")

    # 7. Otwieranie gotowego pliku
    try:
        os.startfile(sciezka_docelowa)
    except Exception as e:
        print(f"ℹ️ Nie udało się otworzyć pliku automatycznie: {e}")

else:
    print("❌ Nie dodano żadnych plików! Sprawdź nazwy i folder.")
