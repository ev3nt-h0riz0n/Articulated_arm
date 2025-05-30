<h1> Articulated_arm </h1>
Repozytorium w celach przechowywania plików związanych z projektem z obiektówki - Animacja robota articulated_arm

**Jak postawić program? Jak każdy typowy program na PS'ach**
* Przejdź w Visual Code do folderu z programem
* Postaw venva: python -m venv venv
* Aktywuj venva .\venv\Scripts\activate
* Włącz dobry interpreter pythona z venva
* pip install pyopengl pygame
na razie tylko te biblioteki wykorzystałem

<h2>TYMCZASOWA OBSŁUGA PROGRAMU</h2>
Projekt wymaga uruchomienia dwóch terminali (Terminal -> split terminal lub ctrl+shift+5). Z jednego uruchamiamy main.py z drugiego controls_window.py. Tymczasowo NIE MOŻNA ruszać ramienia z poziomu main.py (zjebałem ale to kwestia suwaków [z lekka nie dojebane]). Można main.py zamknąć naciskają ecs. Jeżeli sterowanie nie działa proszę je tymczasowo zakomentować u siebie (jeśli zmiana portu nie podziała). W razie dalszych problemów proszę kontaktować się z działem obsługi klienta (nie odpisze ci lol).

<h2>Szybkie FAQ</h2>

**1.Czy da się wyświetlić Pygame i OpenGL w jednym oknie?**  <br>
Nie kurwa nie da się  <br>

**2. Czy można użyć OpenGL do zrobienia GUI w tym samym oknie?**  <br>
Raczej tak  <br>

**3. Czy GUI z pomocą OpenGL działa?**  <br>
Ni chuja, wszystko się jebało  <br>

**4. Czy aktualnie wszystki działa?**  <br>
Poza końcówką robota przechodzącą przez podłogę to tak, wszystko działa <br> 
<i> Skróć cylinder 3 segmentu do 0.4 w articulated_arm.py + zmień w main.py w gltranslatef ostatnią wartośc na 0.55 (jeśli jest inna) lub pobierz nowe articulated_arm.py z repozytorium</i>

**5. Czy zrobienie cieni jest proste?**  <br>
Ani trochę, udało mi się wyświetlić część- wszystko w złym miejscu i pod złym kątem <br>  
**6. Czym jest FreeSimpleGUI?** <br>
Tym samym co PythonSimpleGUI tylko darmowe z GitHuba (tak to pewnie kradzież, ale ukraść złodziejowi - to nie kradzież)
  
<h2>wiadomość Dodo</h2>  
UWAGA WIELKI UPDATE (nie) <br>
Masz nowe dwa pliki - Surroundings i Coordinates. Do surroundings przeniosłem wszystkie obiekty typu ściany, "rakieta", światło itd, jako, że to po prostu należy do otoczenia. W koordynatach chyba jasne, że na razie znajduje się obliczanie koordynatów i potem dodam przemieszczanie się ramienia do konkretnych. Funfact aktualnie to będziemy robić na robotyce określanie pozycji i ustawianie kątów 8)). <br>
Także usuń sobie z pliku Articulated_arm te ściany, cokolwiek tam masz i przenieś do nowego pliku lub skorzystaj z mojego. Nie zmieniałem Ci innych plikow tutaj, bo nie mam GUI wgrane (well), a nie chce plątąc, więc musisz sam sobie pozmieniać sadly. <br>
A i jesli chcesz zeby ci wyswietlalo koordynaty w konsoli to po prostu wywolaj funkcje position(rot1,rot2,rot3)
<h2> OBRÓT SEGMENTÓW: </h2>
Segment pierwszy ma zakres ruchu 0-360 stopni zgodnie z wymaganiami z zadania. Drugi i trzeci segment mają zakres 90 stopni.

<h2>UKŁAD WSPÓŁRZĘDNYCH OPENGL </h2>
Z od ekranu
Y w górę
X w prawo
Na potrzeby projektu przyjmijmy normalny układ wspolrzednych poza obliczeniami. W sensie w prezentacji tego wszystkiego (z - góra, x - prawo, y - od ekranu) lub ewentualnie tam podmienić x z y

<h2>TO DO LIST</h2>
* Ogarnąć w jaki sposób wgrać teksturę/zrobić kocią łapkę  <br>
* Ogarnąć sysem kolicji i pobieranie globalnej lokalizacji ramienia, żeby móc je przesuwać  <br>
* MOŻLIWOŚĆ ZMIANY TRYBY OBSŁUGI RAMIENIA (CONTROL PANEL/MAIN)  <br>
* Dodać zmiany zakresu z poziomy panelu sterowania  <br>
* Dodać zamknięcie obu programów z poziomu panelu sterowania  <br>
