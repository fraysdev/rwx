from pathlib import Path

from PySide6.QtCore import QObject, Property, Signal, Slot, QUrl, QMimeDatabase


class File(QObject):
    nameChanged = Signal()
    contentChanged = Signal()
    errorChanged = Signal()

    _mimeDb = QMimeDatabase()

    def __init__(self):
        super().__init__()
        self._path = ""
        self._name = ""
        self._content = ""
        self._error = ""

    @Property(str, notify=nameChanged)
    def name(self):
        return self._name

    @Property(str, notify=contentChanged)
    def content(self):
        return self._content

    @Property(str, notify=errorChanged)
    def error(self):
        return self._error

    @Slot(QUrl, result=bool)
    def openFile(self, url: QUrl) -> bool:
        filepath = Path(url.toLocalFile())
        self._path = filepath.as_uri()

        try:
            content = filepath.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            self._update(filepath.name, "", str(e))
            return False

        self._update(filepath.name, content, "")
        return True

    @Slot(result=str)
    def getMimeType(self) -> str:
        mimeType = self._mimeDb.mimeTypeForUrl(self._path)
        return mimeType.name()

    def _update(self, name, content, error):
        self._name = name
        self._content = content
        self._error = error

        self.nameChanged.emit()
        self.contentChanged.emit()
        self.errorChanged.emit()

