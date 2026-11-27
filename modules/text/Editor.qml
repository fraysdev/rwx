import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    id: root

    property string text: "Hello, world\nFileSystemModel.readFile(root.currentFilePath)"
    property int lineCount: editor.text.split("\n").length

    color: "transparent"

    RowLayout {
        anchors.fill: parent

        Flickable {
            id: lnumFlickable

            Layout.fillHeight: true
            Layout.preferredWidth:
                fontMetrics.averageCharacterWidth * Math.max(Math.floor(Math.log10(root.lineCount))+1, 3) + 10

            interactive: false
            contentY: editorFlickable.contentY

            Label {
                anchors.right: parent.right
                rightPadding: 10
                horizontalAlignment: Text.AlignRight
                font: editor.font

                text: {
                    let lnum = "";
                    for (let i = 1; i <= root.lineCount; i++) {
                        lnum += i + "\n";
                    }

                    return lnum.trim();
                }
            }
        }

        Flickable {
            id: editorFlickable

            Layout.fillHeight: true
            Layout.fillWidth: true

            boundsBehavior: Flickable.StopAtBounds

            TextArea.flickable: TextArea {
                id: editor

                topPadding: 0
                leftPadding: 0

                antialiasing: true
                background: null
                focus: false
                renderType: Text.QtRendering
                selectByMouse: true

                font.family: "monospace"
                text: root.text
                textFormat: TextEdit.PlainText
            }

            FontMetrics {
                id: fontMetrics
                font: editor.font
            }
        }
    }
}
