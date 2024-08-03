from database.db_setup import init_db
from interface import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
