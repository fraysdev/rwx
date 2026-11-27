import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from src.file import File

def main():
    app = QGuiApplication(sys.argv)
    app.setApplicationName("rwx")

    file = File()
    if len(sys.argv) > 1:
        file.openFile(QUrl.fromLocalFile(str(Path(sys.argv[1]).resolve())))

    engine = QQmlApplicationEngine()
    engine.setInitialProperties({ "file": file })
    engine.load(Path(__file__).resolve().parent / "main.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
