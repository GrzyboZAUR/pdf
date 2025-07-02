# 🧩 PDF Merger Tool

Prosty skrypt w Pythonie do łączenia wielu plików PDF w jeden dokument.

## ✨ Co robi?

- Automatycznie scala wszystkie pliki `.pdf` z bieżącego folderu
- Tworzy foldery na podstawie daty (np. `07_Lipiec`)
- Nadaje plikowi nazwę wg wczorajszej daty (np. `27.07.pdf`)
- Zapisuje wynik do wybranego folderu docelowego
- Usuwa pliki źródłowe po scaleniu (z możliwością kontroli)
- Otwiera scalony plik automatycznie po zakończeniu

---

## 🛠️ Jak używać?

1. Umieść wszystkie pliki `.pdf` do scalenia w jednym folderze (np. `Pobrane`)
2. Uruchom skrypt w tym folderze
3. W pliku `pdf_merger.py` podaj ścieżkę, gdzie mają być **zapisywane** wyniki scalania:

folder_bazowy = r"D:\praca\listy"

## Przykładowe użycie:
- listy obecności w magazynie
- automatyzacja pracy biurowej

## Technologie:
- Python 3
- PyPDF2
- os, datetime
