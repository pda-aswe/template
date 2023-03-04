# template

## Allgemein
MQTT-Client läuft im Hintergrund als ein Thread. Wenn eine neue Nachricht empfangen wird 
Alle Pythonmodule die nicht Standardmäßig enthalten sind, müssen in die Datei requirements.txt geschrieben werden, damit automatisch ein lauffähiges Docker-Image erstellt werden kann. Alle Tests sollten in den tests Ordner eingefügt werden. Ein Docker-Image wird nur erstellt, wenn kein pytest fehlgeschlagen ist.

Request Response Erklären
Code erklären
MQTT erklären
Erklären wie man lokal MQTT zum laufen bekommt
Erklären wie man Service zu mainprojekt hinzufügt
Erklären das man service nicht umbedingt in Container braucht man kann es auch so lokal entwickeln.

Alle Repos müssen public erstellt werden, da sonst Actions und Speicherplatz eingeschränkt ist.

Alle benötigten Module sind in der Datei requirements.txt niedergeschrieben.
Mit `pip3 install -r requirements.txt` können diese installiert werden.

Installieren um die pytests auszuführen. Es wird nicht der das Standardtesttool unittest verwendet, da pytest sich gut in Github-Actions integrieren lassen und auch gleich noch eine Codecoverage ausgeben kann.
Tests können mittels `pytest` in der Konsole ausgeführt werden.

`pip3 install pytest`

Bei pytest ist nur die Vorraussetzung für Funktionen, dass diese am Anfang test_ stehen haben.
Auch die Datei muss mit test_ beginnen.

Mit `pytest --cov=.` Kann die Coverage über alle Dateien ausgewertet werden. Dafür muss `pip3 install pytest-cov` installiert werden.