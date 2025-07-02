import os
from datetime import datetime, timedelta
from PyPDF2 import PdfMerger

a = "a.pdf"
b = "b.pdf"
# c = "c.pdf"
merger = PdfMerger()
wczorajsza_data = datetime.now() - timedelta(days=1)
nazwa_miesiąca = wczorajsza_data.strftime("%m_%B")
folder_bazowy = r'C:\Users\bgrzybowski\Desktop\listy\magazyn\listy obecności\2025'
folder_miesiąca = os.path.join(folder_bazowy, nazwa_miesiąca)

if not os.path.exists(folder_miesiąca):
    os.makedirs(folder_miesiąca)
    print(f"📂 Utworzono folder: {folder_miesiąca}")
#ścieżka docelowego folderu:
folder_path = r"C:\Users\bgrzybowski\Desktop\listy\magazyn\listy obecności"
folder_zapisu = r"C:\Users\bgrzybowski\Desktop\listy\magazyn\listy obecności\2025\4"
file_names = [a,b]
# file_names = [a,b,c]
for file_name in file_names:
    file_path = os.path.join(folder_path,file_name)
    if os.path.exists(file_path):
        merger.append(file_path)
    else:
        print(f"Plik {file_name} nie istnieje. Sprawdź ścieżkę!")
# Tworzenie nazwy pliku: dzień.miesiąc.pdf

dzień = wczorajsza_data.day
miesiąc = wczorajsza_data.strftime("%m")
output_file = os.path.join(folder_miesiąca, f"{dzień}.{miesiąc}.pdf")


if len(merger.pages) > 0:  # Jeśli PyPDF2 dodało jakiekolwiek strony
    merger.write(output_file)
    merger.close()
    print(f"✅ Połączony plik zapisany jako: {output_file}")
    #zamyka pdfy przed usunięciem
   
    try:
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path) and file_path !=output_file:
                os.remove(file_path)
                print(f"🗑️ Usunięto: {file_path}")
    except PermissionError as e:
        print(f"❌ Nie można usunąć pliku {file_path}, bo jest otwarty. Musisz sam go skasować!.")
        # Otworzenie nowego pliku PDF
    os.startfile(output_file)

else:
    print("❌ Nie dodano żadnych plików! Sprawdź nazwy i ścieżki.")
