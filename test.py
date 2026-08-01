import sys
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget


class TestBrowser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1024, 768)

        self.tab = QTabWidget(self)
        self.tab.setIconSize(QSize(16, 16))  # 確保 Tab 繪製圖示
        self.setCentralWidget(self.tab)

        self.add_new_tab("https://www.google.com")

    def add_new_tab(self, url):
        browser = QWebEngineView()

        # 1. 強制開啟圖示自動載入
        browser.settings().setAttribute(
            QWebEngineSettings.WebAttribute.AutoLoadIconsForPage, True
        )

        browser.setUrl(QUrl(url))
        self.tab.addTab(browser, "載入中...")

        # 2. 帶有 Debug 輸出的圖示綁定
        browser.iconChanged.connect(
            lambda icon, b=browser: self.update_icon(icon, b)
        )

    def update_icon(self, icon, b):
        idx = self.tab.indexOf(b)
        print(f"[Debug] 抓到 Icon！Tab 索引: {idx}, 是否無效: {icon.isNull()}")
        if idx != -1 and not icon.isNull():
            self.tab.setTabIcon(idx, icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestBrowser()
    win.show()
    sys.exit(app.exec())
