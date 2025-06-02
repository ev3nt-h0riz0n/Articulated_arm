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

Dodatkowa obsługa: 
Przycisk L - zaczyna się nauka na 5 sekund
Przycisk P - odtwarza nauczone już ruchy
Numpad:
<ul>
  <li>4 i 6 - lewo prawo</li>
  <li>2 i 8 - dół góra</li>
  <li> 7 i 9 - obrót talerza chwytaka</li>
</ul>

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
  
<br>
Patch 31.05.25 - dodano funkcję zamykania obu programów z poziomu panelu sterowania <br>
Patch 02.06.25 - dodano funkcję obrotu chwytaka numerkami numpada, dodano funkcję uczenia się ruchów L i P <br>

<h2>UKŁAD WSPÓŁRZĘDNYCH OPENGL </h2>
Z od ekranu <br>
Y w górę <br>
X w prawo <br>
Na potrzeby projektu przyjmijmy normalny układ wspolrzednych poza obliczeniami. W sensie w prezentacji tego wszystkiego (z - góra, x - prawo, y - od ekranu) lub ewentualnie tam podmienić x z y <br>

<h2>TO DO LIST</h2>
* Ogarnąć w jaki sposób wgrać teksturę/zrobić kocią łapkę  <br>
* Ogarnąć system kolizji!! WAŻNE<br> 
* MOŻLIWOŚĆ ZMIANY TRYBY OBSŁUGI RAMIENIA (CONTROL PANEL/MAIN)  <br>
* Dodać zmiany zakresu z poziomy panelu sterowania  <br>
* Dodać zamknięcie obu programów z poziomu panelu sterowania  <br>
* Dodać DropDown do zmiany na ustalone pozycje <br>
* Wykrywanie przedmiotu w pobliżu w celu uchwycenia go magnesem (na razie przedmiot jest przyciągany na milion kilometrów, a tak właściwie to się teleportuje) <br>
* Płynne przemieszczenie się efektora przy ruchu nauczonym i zmienieniu pozycji
