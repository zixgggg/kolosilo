import sys
from PyQt6 import QtWidgets,QtWebEngineWidgets,QtCore
"""
class AppClass(QtWidgets.QApplication):
    def __init__(self,arg):
        super().__init__(arg)
        #self.QtWidgets.QApplication(arg)
app =AppClass(sys.argv)
"""
app =QtWidgets.QApplication(sys.argv)
class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("koloso")
window=WindowClass()
#window=QtWidgets.QWidget()
#window.setWindowTitle("retumilo")
#index="https://www.google.com"
index_page="https://www.google.com"
#browser=QtWebEngineWidgets.QWebEngineView(parent=window)
#browser.load(QtCore.QUrl(index_page))
google="https://www.google.com/search?q="
duckduckgo="https://duckduckgo.com/?q="
bing="https://www.bing.com/search?q="
class WebViewClass(QtWebEngineWidgets.QWebEngineView):
    def __init__(self,url):
        super().__init__()
        self.load(QtCore.QUrl(url))
webview=WebViewClass(index_page)

class BarClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hide()
        self.back_page_button=QtWidgets.QPushButton("back")
        #back_page_button.setGeometry(0,0,100,50)
        self.forward_page_button=QtWidgets.QPushButton("forward")
        self.reload_page_button=QtWidgets.QPushButton("reload")
        self.enter_page_button=QtWidgets.QPushButton("enter")
        self.search_input_line=QtWidgets.QLineEdit()
        self.search_input_line.setPlaceholderText("search")
        #url_input_line=QtWidgets.QLineEdit()
        #input_line.setText("a")
        
        self.close_bar_rbutton=QtWidgets.QRadioButton("bar")
        self.close_bar_rbutton.clicked.connect(lambda:self.setVisible(not self.isVisible()))
        self.back_page_button.clicked.connect(webview.back)
        self.forward_page_button.clicked.connect(webview.forward)
        self.reload_page_button.clicked.connect(webview.reload)
        self.enter_page_button.clicked.connect(lambda:webview.load(QtCore.QUrl(google+self.search_input_line.displayText())))
        #self.search_input_line.returnPressed.connect(lambda:webview.load(QtCore.QUrl(google+self.search_input_line.displayText())))
        self.search_input_line.returnPressed.connect(self.enter_page_button.click)
        

        self.back_page_button.setFixedSize(50,20)
        self.forward_page_button.setFixedSize(50,20)
        self.reload_page_button.setFixedSize(50,20)
        self.enter_page_button.setFixedSize(50,20)
        self.search_input_line.setFixedSize(150,20)

        bar_layout=QtWidgets.QVBoxLayout()
        page_button_layout=QtWidgets.QHBoxLayout()
        search_line_layout=QtWidgets.QHBoxLayout()
        
        #b_layout.addWidget(back_page_button,alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        page_button_layout.addWidget(self.back_page_button)
        page_button_layout.addWidget(self.forward_page_button)
        page_button_layout.addWidget(self.reload_page_button)
        page_button_layout.addStretch()
        bar_layout.addLayout(page_button_layout)
        #back_page_button.hide()
        
        search_line_layout.addWidget(self.search_input_line)
        search_line_layout.addWidget(self.enter_page_button)
        search_line_layout.addStretch()
        bar_layout.addLayout(search_line_layout)
        bar_layout.addStretch()
        self.setLayout(bar_layout)
bar=BarClass()
class PageTabClass(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setUsesScrollButtons(True)
        self.setElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.setStyleSheet("""QTabBar::tab{max-width:150px; min-width:150px}""")
        self.tabCloseRequested.connect(self.close_tab)
        webview.titleChanged.connect(lambda:self.setTabText(self.currentIndex(),webview.title()))
        self.addTab(webview,webview.title())
        a=QtWidgets.QLabel("123")
        self.addTab(a,"aa")
        self.show()
    def close_tab(self,index):
        current_webpage=self.widget(index)
        current_webpage.deleteLater()
        self.removeTab(index)
        if self.count()==0:
            sys.exit()
    def add_new_tab(self):
        webpage=WebViewClass(index_page)
        self.addTab(webpage,webview.title())
#tab=QtWidgets.QTabWidget(window)
tab=PageTabClass()
main_layout=QtWidgets.QVBoxLayout()
main_layout.setContentsMargins(0, 0, 0, 0) # 去掉外邊框
#main_layout.addLayout(bar_layout)
main_layout.addWidget(bar)
main_layout.addWidget(bar.close_bar_rbutton)
new_tab_button=QtWidgets.QPushButton("new tab")
new_tab_button.clicked.connect(tab.add_new_tab)
main_layout.addWidget(new_tab_button)
#main_layout.addWidget(browser,stretch=1)
main_layout.addWidget(tab,stretch=1)
window.setLayout(main_layout)
window.move(0,0)
window.resize(800,600)
window.show()
sys.exit(app.exec())
