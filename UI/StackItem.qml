import QtQuick 2.0

Rectangle {
    id: stack_item
    width: 150
    height: 100
    color: "green"
    property alias text: stack_item_text.text
    Text {
        id: stack_item_text
    }
}