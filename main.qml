import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

import "modules/text"

ApplicationWindow {
    width: 800
    height: 450
    visible: true
    title: (file.name || "untitled") + " | " + file.getMimeType() + " | rwx"

    required property var file

    Editor {
        anchors.fill: parent
        text: file.content
    }
}
