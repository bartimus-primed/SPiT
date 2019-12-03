import QtQuick 2.0

Item {
    id: main_stack
    width: 200
    height: 1000
    Grid {
        columns: 1
        spacing: 10
        StackFrame {}
        StackFrame {}
    }
}