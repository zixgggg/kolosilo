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
        self.setWindowTitle("retumilo")
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
        self.close_bar_rbutton.clicked.connect(lambda:self.setVisible(not bar.isVisible()))
        self.back_page_button.clicked.connect(webviwe.back)
        self.forward_page_button.clicked.connect(webviwe.forward)
        self.reload_page_button.clicked.connect(webviwe.reload)
        self.enter_page_button.clicked.connect(lambda:webviwe(google+search_input_line.displayText()))

        self.back_page_button.setFixedSize(50,20)
        self.forward_page_button.setFixedSize(50,20)
        self.reload_page_button.setFixedSize(50,20)
        self.enter_page_button.setFixedSize(50,20)
        self.search_input_line.setFixedSize(150,20)

        bar_layout=QtWidgets.QVBoxLayout()
        page_button_layout=QtWidgets.QHBoxLayout()
        search_line_layout=QtWidgets.QHBoxLayout()
        
        #b_layout.addWidget(back_page_button,alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        page_button_layout.addWidget(back_page_button)
        page_button_layout.addWidget(forward_page_button)
        page_button_layout.addWidget(reload_page_button)
        page_button_layout.addStretch()
        bar_layout.addLayout(page_button_layout)
        #back_page_button.hide()
        
        search_line_layout.addWidget(search_input_line)
        search_line_layout.addWidget(enter_page_button)
        search_line_layout.addStretch()
        bar_layout.addLayout(search_line_layout)
        bar_layout.addStretch()
        self.setLayout(bar_layout)
bar=QtWidgets.QWidget()
bar.hide()
"""
class BackPageButtonClass(QtWidgets.QPushButton):
    def __init__(self,text,parent)
        super().__init__()
        self.setText(text)
"""
back_page_button=QtWidgets.QPushButton("back",parent=bar)
#back_page_button.setGeometry(0,0,100,50)
forward_page_button=QtWidgets.QPushButton("forward",parent=bar)
reload_page_button=QtWidgets.QPushButton("reload",parent=bar)
enter_page_button=QtWidgets.QPushButton("enter",parent=bar)
search_input_line=QtWidgets.QLineEdit(parent=bar)
search_input_line.setPlaceholderText("search")
#url_input_line=QtWidgets.QLineEdit()
#input_line.setText("a")
def toggle_bar():
    """
    if bar.isVisible()==True:
        bar.hide()
    """
    bar.setVisible(not bar.isVisible())
close_bar_rbutton=QtWidgets.QRadioButton("bar")
close_bar_rbutton.clicked.connect(toggle_bar)


back_page_button.clicked.connect(browser.back)
forward_page_button.clicked.connect(browser.forward)
reload_page_button.clicked.connect(browser.reload)
google="https://www.google.com/search?q="
duckduckgo="https://duckduckgo.com/?q="
bing="https://www.bing.com/search?q="
def load_page(engine,q):
    browser.load(QtCore.QUrl(engine+q))
enter_page_button.clicked.connect(lambda:load_page(google,search_input_line.displayText()))
enter_page_button.clicked.connect(webviwe(google+search_input_line.displayText()))
search_input_line.returnPressed.connect(lambda:load_page(google,search_input_line.displayText()))
#url_input_line.returnPressed.connect(lambda:load_page(google,input_line.displayText()))

back_page_button.setFixedSize(50,20)
forward_page_button.setFixedSize(50,20)
reload_page_button.setFixedSize(50,20)
enter_page_button.setFixedSize(50,20)
search_input_line.setFixedSize(150,20)

bar_layout=QtWidgets.QVBoxLayout()
page_button_layout=QtWidgets.QHBoxLayout()
search_line_layout=QtWidgets.QHBoxLayout()

#b_layout.addWidget(back_page_button,alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
page_button_layout.addWidget(back_page_button)
page_button_layout.addWidget(forward_page_button)
page_button_layout.addWidget(reload_page_button)
page_button_layout.addStretch()
bar_layout.addLayout(page_button_layout)
#back_page_button.hide()

search_line_layout.addWidget(search_input_line)
search_line_layout.addWidget(enter_page_button)
search_line_layout.addStretch()
bar_layout.addLayout(search_line_layout)
bar_layout.addStretch()
bar.setLayout(bar_layout)

tab=QtWidgets.QTabWidget(window)
tab.setTabsClosable(True)
#tab.setChangeCurrentOnDrag(True)
#tab.tabBar().setChangeCurrentOnDrag(True)
#tab.tabBar().hide()
tab.setMovable(True)
tab.setUsesScrollButtons(True)
#tab.setTabBarAutoHide(True)
tab.setElideMode(QtCore.Qt.TextElideMode.ElideRight)
tab.setStyleSheet("""QTabBar::tab{max-width:150px; min-width:150px}""")

def update_icon(icon,b):
    #tab.setTabIcon(tab.indexOf(browser),browser.icon())
    tab.setTabIcon(tab.indexOf(b),icon)
#    if not icon.isNull()==True:
#        tab.setTabIcon(tab.indexOf(b),icon)
"""
def update_icon( icon, b):
    idx = tab.indexOf(b)
    print(f"[Debug] 抓到 Icon！Tab 索引: {idx}, 是否無效: {icon.isNull()}")
    if idx != -1 and not icon.isNull():
        tab.setTabIcon(idx, icon)
"""
#browser.iconChanged.connect(lambda icon,b=browser: update_icon(icon,b))
browser.iconChanged.connect(lambda icon,b=browser:tab.setTabIcon(tab.indexOf(b),icon))
def close_tab(index):
    current_browser=tab.widget(index)
    current_browser.deleteLater()
    tab.removeTab(index)
    if tab.count()==0:
        sys.exit()
#tab.tabCloseRequested.connect(lambda:tab.removeTab(tab.currentIndex()))
tab.tabCloseRequested.connect(close_tab)
title=browser.title()
browser.titleChanged.connect(lambda:tab.setTabText(tab.currentIndex(),browser.title()))
tab.addTab(browser,title)
a=QtWidgets.QLabel("123")
tab.addTab(a,"aa")
tab.show()
main_layout=QtWidgets.QVBoxLayout()
main_layout.setContentsMargins(0, 0, 0, 0) # 去掉外邊框
#main_layout.addLayout(bar_layout)
main_layout.addWidget(bar)
main_layout.addWidget(close_bar_rbutton)
new_tab_button=QtWidgets.QPushButton("new tab")
def add_new_tab():
    b=QtWebEngineWidgets.QWebEngineView()
    tab.addTab(b,title)
new_tab_button.clicked.connect(add_new_tab)
main_layout.addWidget(new_tab_button)
#main_layout.addWidget(browser,stretch=1)
main_layout.addWidget(tab,stretch=1)
window.setLayout(main_layout)
window.move(0,0)
window.resize(800,600)
window.show()
sys.exit(app.exec())
