import QtQuick 2.0

Rectangle {
    id: stack_frame
    width: 180
    height: 250
    Grid {
        columns: 1
        spacing: 10
        StackItem {text: "Test2"}
        StackItem {text: "Test3"}
        StackItem {text: "Test1"}
        StackItem {text: "Test4"}
    }
}