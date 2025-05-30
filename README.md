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
Projekt wymaga uruchomienia dwóch terminali (Terminal -> split terminal lub ctrl+shift+5). Z jednego uruchamiamy main.py z drugiego controls_window.py. Tymczasowo NIE MOŻNA ruchem ramienia z poziomu main.py (zjebałem ale to kwestia suwaków [z lekka nie dojebane]). Można main.py zamknąć naciskają ecs. Jeżeli sterowanie nie działa proszę je tymczasowo zakomentować u siebie (jeśli zmiana portu nie podziała). W razie dalszych problemów proszę kontaktować się z działem obsługi klienta (nie odpisze ci lol).

<h2>Szybkie FAQ</h2>
1. Czy da się użyć Pygame i OpenGL w jednym oknie?
* Nie kurwa nie da się
2. Czy można użyć OpenGL do zrobienia GUI w tym samym oknie?
* Raczej tak
3. Czy GUI z pomocą OpenGL działa?
Ni chuja, wszystko się jebało
4. Czy aktualnie wszystki działa?
Poza końcówką robota przechodzącą przez podłogę to tak, wszystko działa
5. Czy zrobienie cieni jest proste?
Ani trochę, udało mi się wyświetlić część- wszystko w złym miejscu i pod złym kątem


Ogólnie to zacząłem projekt już coś tam kminić. ChatGPT mówi, że pygame jest spoko programem, żeby wyświetlało się okno. 
Narysowałem na razie podstawę do robota, dwa segmenty i staw + w miarę opisałem co się dzieje. Idk czy na bieżąco powinniśmy robić dokumentacje, pewnie tak, ale chuj wie w jaki sposób.
W każdym razie coś poszło do przodu, ale coś czuje, że plan z latającą rakietą może być marny XDD. Z wyglądem kociej łapki może jeszcze przejdzie,
tylko zastanawiam się jak to zrobić, żeby cała tekstura się ruszała. ALbo jak w ogole wykreslic ta teksture lapy XDD

Z przechodzeniem na konkretne koordynaty mam plan, żeby pozycjonowanie przechodziło po kolei od największych stopni swobody, czyli moduł obrotowy przy podstawie, potem łokieć, itd, bo przechodzenie samej końcówki na dobre koordynaty może być dosyć problematyczne.

Jako, że wykorzystałem świcenie światła (żeby rozróżnic, że to jest w 3D przez cienie), to nie da się zmieniać kolorów obiektu przez  glColor3f tylko
trzeba ustawić konkretny rodzaj materiały, odbicie itd itp ://.

<h2> OBRÓT SEGMENTÓW: </h2>
Segment pierwszy ma zakres ruchu 0-360 stopni zgodnie z wymaganiami z zadania. Drugi i trzeci segment mają zakres 90 stopni.

<h2>UKŁAD WSPÓŁRZĘDNYCH OPENGL </h2>
Z w od ekranu
Y w górę
X w prawo

<h2>TO DO LIST</h2>
* Ogarnąć w jaki sposób wgrać teksturę/zrobić kocią łapkę/n
* Ogarnąć sysem kolicji i pobieranie globalnej lokalizacji ramienia, żeby móc je przesuwać
* MOŻLIWOŚĆ ZMIANY TRYBY OBSŁUGI RAMIENIA (CONTROL PANEL/MAIN)
* Dodać zmiany zakresu z poziomy panelu sterowania
* Dodać zamknięcie obu programów z poziomu panelu sterowania
