import sys
from PyQt6 import QtWidgets,QtWebEngineWidgets,QtCore
app =QtWidgets.QApplication(sys.argv)

window=QtWidgets.QWidget()
window.setWindowTitle("retumilo")
#index="https://www.google.com"
index="https://www.google.com"
browser=QtWebEngineWidgets.QWebEngineView(parent=window)
browser.load(QtCore.QUrl(index))

bar=QtWidgets.QWidget()
bar.hide()
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

main_layout=QtWidgets.QVBoxLayout()
main_layout.setContentsMargins(0, 0, 0, 0) # 去掉外邊框
#main_layout.addLayout(bar_layout)
main_layout.addWidget(bar)
main_layout.addWidget(close_bar_rbutton)
main_layout.addWidget(browser,stretch=1)
window.setLayout(main_layout)
window.move(0,0)
window.resize(800,600)
window.show()
tab=QtWidgets.QTabWidget()
tab.setTabsClosable(True)
#tab.setChangeCurrentOnDrag(True)
#tab.tabBar().setChangeCurrentOnDrag(True)
tab.setMovable(True)
tab.setUsesScrollButtons(True)
tab.setElideMode(QtCore.Qt.TextElideMode.ElideRight)
tab.setStyleSheet("""QTabBar::tab{max-width:150px; min-width:150px}""")
def close_tab():
    tab.removeTab(tab.currentIndex())
    if tab.count()==0:
        sys.exit()
#tab.tabCloseRequested.connect(lambda:tab.removeTab(tab.currentIndex()))
tab.tabCloseRequested.connect(close_tab)
t=browser.title()
browser.titleChanged.connect(lambda:tab.setTabText(tab.currentIndex(),browser.title()))
tab.addTab(window,t)
a=QtWidgets.QLabel("123")
tab.addTab(a,"aa")
tab.show()
sys.exit(app.exec())
