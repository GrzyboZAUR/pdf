# PDF Merger Tool 🧩

Ten prosty skrypt łączy pliki PDF w jeden dokument, automatycznie tworząc foldery według daty oraz usuwając pliki źródłowe po scaleniu.
Przed pierwszym użyciem należy uzupełnić ścieżkę gdzie są pliki .pdf. Nowo powstały folder powstanie w tym samym folderze. 
Skrypt musi zostać uruchomiony w folderze gdzie znajdują się pliki pdf.

## Funkcje:
- scalanie plików PDF (z użyciem PyPDF2)
- tworzenie folderów na podstawie daty (np. `04_Kwiecień`)
- nadawanie plikom nazw według daty (np. `27.04.pdf`)
- automatyczne usuwanie plików źródłowych
- otwieranie gotowego pliku PDF po zakończeniu

## Przykładowe użycie:
- listy obecności w magazynie
- automatyzacja pracy biurowej

## Technologie:
- Python 3
- PyPDF2
- os, datetime
