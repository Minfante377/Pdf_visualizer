from PyQt5.QtWidgets import QPushButton, QApplication, QFileDialog, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5 import QtCore
from popplerqt5 import Poppler
import sys
from pdf import PDFWidget 
class App(QApplication):

    def __init__(self,sys_arg):
        super(App, self).__init__(sys_arg)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("PDF Visualizer")
        browse_button = QPushButton('Browse...')
        browse_button.clicked.connect(self.browse)
        previous_button = QPushButton('Previous')
        previous_button.clicked.connect(self.previous_page)
        next_button = QPushButton('Next')
        next_button.clicked.connect(self.next_page)
        desktops = QApplication.desktop()
        self.file = None
        self.geometry = desktops.screenGeometry(desktops.screenNumber())
        self.pdf_visualizer = PDFWidget(self.file, geometry = self.geometry)
        self.page_number = 0
        self.num_pages = 1
        dark_button = QPushButton('Dark Mode')
        dark_button.clicked.connect(self.toogle)
        buttons_layout.addWidget(browse_button)
        buttons_layout.addWidget(previous_button)
        buttons_layout.addWidget(next_button)
        buttons_layout.addWidget(dark_button)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.pdf_visualizer)
        self.main_window.setCentralWidget(QWidget(self.main_window))
        self.main_window.centralWidget().setLayout(layout)
        self.main_window.show()

    def browse(self, button):
        self.file, _ = QFileDialog.getOpenFileName(self.main_window, ' Single File', QtCore.QDir.rootPath(), '*.pdf')
        print(self.file)
        if self.file: 
            desktops = QApplication.desktop()
            self.geometry = desktops.screenGeometry(desktops.screenNumber())
            self.page_number = 0
            self.pdf_visualizer.load_file(self.file, self.geometry)

    def next_page(self,button):
        self.num_pages = self.pdf_visualizer.get_count()
        print(self.num_pages)
        if self.page_number > self.num_pages - 1:
            return
        self.page_number = self.page_number + 1
        self.pdf_visualizer.change_page(self.page_number)
    
    def previous_page(self,button):
        if self.page_number > 0:
            self.page_number = self.page_number - 1
        self.pdf_visualizer.change_page(self.page_number)
    
    def toogle(self,button):
        self.pdf_visualizer.toogle()
        self.pdf_visualizer.change_page(self.page_number)


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

