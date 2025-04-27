from PyQt6.QtWidgets import QMessageBox


class AlertManager:
    @staticmethod
    def information(parent, title: str, message: str):
        QMessageBox.information(parent, title, message)

    @staticmethod
    def warning(parent, title: str, message: str):
        QMessageBox.warning(parent, title, message)

    @staticmethod
    def critical(parent, title: str, message: str):
        QMessageBox.critical(parent, title, message)

    @staticmethod
    def question(parent, title: str, message: str) -> bool:
        response = QMessageBox.question(
            parent,
            title,
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return response == QMessageBox.StandardButton.Yes
