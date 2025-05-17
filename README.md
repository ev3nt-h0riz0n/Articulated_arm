<h1> Articulated_arm </h1>
Repozytorium w celach przechowywania plików związanych z projektem z obiektówki - Animacja robota articulated_arm

**Jak postawić program? Jak każdy typowy program na PS'ach**
* Przejdź w Visual Code do folderu z programem
* Postaw venva: python -m venv venv
* Aktywuj venva .\venv\Scripts\activate
* Włącz dobry interpreter pythona z venva
* pip install pyopengl pygame
na razie tylko te biblioteki wykorzystałem

Ogólnie to zacząłem projekt już coś tam kminić. ChatGPT mówi, że pygame jest spoko programem, żeby wyświetlało się okno. 
Narysowałem na razie podstawę do robota, dwa segmenty i staw + w miarę opisałem co się dzieje. Idk czy na bieżąco powinniśmy robić dokumentacje, pewnie tak, ale chuj wie w jaki sposób.
W każdym razie coś poszło do przodu, ale coś czuje, że plan z latającą rakietą może być marny XDD. Z wyglądem kociej łapki może jeszcze przejdzie,
tylko zastanawiam się jak to zrobić, żeby cała tekstura się ruszała. ALbo jak w ogole wykreslic ta teksture lapy XDD

Z przechodzeniem na konkretne koordynaty mam plan, żeby pozycjonowanie przechodziło po kolei od największych stopni swobody, czyli moduł obrotowy przy podstawie, potem łokieć, itd, bo przechodzenie samej końcówki na dobre koordynaty może być dosyć problematyczne.

Jako, że wykorzystałem świcenie światła (żeby rozróżnic, że to jest w 3D przez cienie), to nie da się zmieniać kolorów obiektu przez  glColor3f tylko
trzeba ustawić konkretny rodzaj materiały, odbicie itd itp ://.

<h2> OBRÓT SEGMENTÓW: </h2>
Segment pierwszy ma zakres ruchu 0-360 stopni zgodnie z wymaganiami z zadania
Co do drugiego segmentu wraz z stawem nie wiem jeszcze jaki dokładnie dobrać zakres ruchów

<h2>UKŁAD WSPÓŁRZĘDNYCH OPENGL M/h2>
Z w od ekranu
Y w górę
X w prawo
