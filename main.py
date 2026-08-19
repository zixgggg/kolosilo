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
        self.setWindowTitle("kolosilo")
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
    

class PageTabClass(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setUsesScrollButtons(True)
        self.setElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.setStyleSheet("""QTabBar::tab{max-width:150px; min-width:150px}""")
        self.tabCloseRequested.connect(self.close_tab)
        
        self.add_new_tab()
        
        a=QtWidgets.QLabel("123")
        self.addTab(a,"aa")
        self.show()
    def close_tab(self,index):
        current_webview=self.widget(index)
        current_webview.deleteLater()
        self.removeTab(index)
        if self.count()==0:
            sys.exit()
    def update_url_box(self):
        if isinstance(self.currentWidget(),WebViewClass)==False:
            bar.url_box.setText("")
        else:
            bar.url_box.setText(self.currentWidget().url().toString())
    def add_new_tab(self):
        webview=WebViewClass(index_page)
        self.addTab(webview,webview.title())
        webview.titleChanged.connect(lambda:self.setTabText(self.indexOf(webview),webview.title()))
        webview.iconChanged.connect(lambda:self.setTabIcon(self.indexOf(webview),webview.icon()))
        #webview.urlChanged.connect(lambda:bar.url_input_line.setText(self.currentWidget().url().toString()))
        webview.urlChanged.connect(self.update_url_box)
        self.currentChanged.connect(self.update_url_box)
tab=PageTabClass()

def current_webview():
    widget=tab.currentWidget()
    if isinstance(widget,WebViewClass):
        return widget
    else:
        return None
class BarClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #self.hide()
        self.back_page_button=QtWidgets.QPushButton("back")
        #back_page_button.setGeometry(0,0,100,50)
        self.forward_page_button=QtWidgets.QPushButton("forward")
        self.reload_page_button=QtWidgets.QPushButton("reload")
        self.enter_page_button=QtWidgets.QPushButton("enter")
        self.url_box=QtWidgets.QLineEdit()
        self.url_box.setPlaceholderText("URL (https:// , file://...)")
        #url_input_line=QtWidgets.QLineEdit()
        #input_line.setText("a")
        self.toggle_tab_cb=QtWidgets.QCheckBox("tab")
        self.new_tab_button=QtWidgets.QPushButton("new tab")
        
        
        self.toggle_bar_cb=QtWidgets.QCheckBox("bar")
        #self.close_bar_rbutton.clicked.connect(lambda:self.setVisible(not self.isVisible()))
        self.toggle_bar_cb.toggled.connect(self.setVisible)
        self.back_page_button.clicked.connect(lambda:current_webview() and current_webview().back())
        self.forward_page_button.clicked.connect(lambda:current_webview() and current_webview().forward())
        self.reload_page_button.clicked.connect(lambda:current_webview() and current_webview().reload())
        self.enter_page_button.clicked.connect(lambda:current_webview() and current_webview().load(QtCore.QUrl(self.url_box.text())))
        #self.search_input_line.returnPressed.connect(lambda:webview.load(QtCore.QUrl(google+self.search_input_line.displayText())))
        self.url_box.returnPressed.connect(self.enter_page_button.click)
        """
        def toggle_tab():
            if self.toggle_tab_button.isChecked()==True:
                tab.tabBar().setVisible(True)
            else:
                tab.tabBar().setVisible(False)
        """
        self.toggle_tab_cb.toggled.connect(tab.tabBar().setVisible)
        #self.toggle_tab_button.clicked.connect(lambda:tab.tabBar().setVisible(not tab.tabBar().isVisible()))
        self.new_tab_button.clicked.connect(tab.add_new_tab)
        self.show()
        if tab.tabBar().isVisible()==True:
            self.toggle_tab_cb.setChecked(True)
        if self.isVisible()==True:
            self.toggle_bar_cb.setChecked(True)
        

        self.back_page_button.setFixedSize(50,20)
        self.forward_page_button.setFixedSize(50,20)
        self.reload_page_button.setFixedSize(50,20)
        self.enter_page_button.setFixedSize(50,20)
        self.url_box.setFixedSize(1000,20)
        self.toggle_tab_cb.setFixedSize(50,20)
        self.new_tab_button.setFixedSize(50,20)


        bar_layout=QtWidgets.QVBoxLayout()
        page_button_layout=QtWidgets.QHBoxLayout()
        #b_layout.addWidget(back_page_button,alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        page_button_layout.addWidget(self.back_page_button)
        page_button_layout.addWidget(self.forward_page_button)
        page_button_layout.addWidget(self.reload_page_button)
        page_button_layout.addWidget(self.url_box)
        page_button_layout.addWidget(self.enter_page_button)
        page_button_layout.addStretch()
        #page_button_layout.addWidget(self.toggle_tab_button)
        page_button_layout.addWidget(self.new_tab_button)
        
        bar_layout.addLayout(page_button_layout)
        #back_page_button.hide()
        
        
        bar_layout.addStretch()
        self.setLayout(bar_layout)
bar=BarClass()
if tab.tabBar().isVisible()==True:
    bar.toggle_tab_cb.setChecked(True)
if bar.isVisible()==True:
    bar.toggle_bar_cb.setChecked(True)
main_layout=QtWidgets.QVBoxLayout()
main_layout.setContentsMargins(0, 0, 0, 0) # 去掉外邊框
#main_layout.addLayout(bar_layout)
main_layout.addWidget(bar)
#main_layout.addWidget(bar.toggle_tab_button)
#main_layout.addWidget(bar.close_bar_rbutton)
#main_layout.addWidget(browser,stretch=1)
tab_and_bar_status=QtWidgets.QHBoxLayout()
tab_and_bar_status.addWidget(bar.toggle_tab_cb)
tab_and_bar_status.addWidget(bar.toggle_bar_cb)
main_layout.addLayout(tab_and_bar_status)
main_layout.addWidget(tab,stretch=1)
window.setLayout(main_layout)
window.move(0,0)
window.resize(800,600)
window.show()
sys.exit(app.exec())
