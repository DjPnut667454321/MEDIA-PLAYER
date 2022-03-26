from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,\
   QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys

class Window(QWidget):
    def __init__(self):
       super().__init__()

       self.setWindowIcon(QIcon("player.ico"))
       self.setWindowTitle("DJ P-NUT KAROKE")
       self.setGeometry(350,100, 700,500)

       p = self.palette()
       p.setColor(QPalette.Window, Qt.GlobalColor.red)
       self.setPalette(p)

       self.create_player()


    def create_player(self):

       self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

       videoWidget = QVideoWidget()


       self.openBtn = QPushButton('Open video')
       self.openBtn.clicked.connect(self.open_file)



       self.playBtn = QPushButton()
       self.playBtn.setEnabled(False)
       self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
       self.playBtn.clicked.connect(self.play_video)

       self.slider = QSlider(Qt.Horizontal)
       self.slider.setRange(0,0)


       hbox = QHBoxLayout()
       hbox.setContentsMargins(0,0,0,0)

       hbox.addWidget(self.openBtn)
       hbox.addWidget(self.playBtn)
       hbox.addWidget(self.slider)



       vbox = QVBoxLayout()
       vbox.addWidget(videoWidget)

       vbox.addLayout(hbox)
        
        
       self.setLayout(vbox)




    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName (self,"Open Video")

        if filename != '':
           self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
           self.playBtn.setEnabled(True)




    def play_video(self):
       if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
          self.mediaPlayer.pause

       else:
          self.mediaPlayer.play()














app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())