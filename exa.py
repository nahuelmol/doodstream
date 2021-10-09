import argparse
import os.path
import sys

from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QFileDialog, QWidget
from PyQt5.QtWidgets import QLabel, QStyle, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPalette

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from random import choice

def main():
	class MainWindow(QWidget):
		def __init__(self):
			super().__init__()

			self.setWindowTitle("Player")
			self.setGeometry(350,100,700,500)

			self.create_player()

		def create_player(self):

			self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

			self.videowidget = QVideoWidget()

			self.toOpen = QPushButton("Open the video")
			self.toOpen.clicked.connect(self.open_file)

			self.playBTN 	= QPushButton()
			self.playBTN.setEnabled(False)
			self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
			self.playBTN.clicked.connect(self.play_video)

			self.slider = QSlider(Qt.Horizontal)
			self.slider.setRange(0,0)


			hbox = QHBoxLayout()
			hbox.setContentsMargins(0,0,0,0)
			hbox.addWidget(self.toOpen)
			hbox.addWidget(self.playBTN)
			hbox.addWidget(self.slider)

			vbox = QVBoxLayout() 
			vbox.addWidget(self.videowidget)
			vbox.addLayout(hbox)

			self.mediaPlayer.setVideoOutput(self.videowidget)

			self.setLayout(vbox)

		def open_file(self):
			filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
			try:
				if filename != '':
					print(filename)
					file_path = QUrl.fromLocalFile(filename)
					print(file_path)
					print(QUrl("file:///" + filename))
					self.mediaPlayer.setMedia(QMediaContent(QUrl(file_path)))
					self.playBTN.setEnabled(True)
			except Exception as e:
				raise 'error: '+e
				

		def play_video(self):
			print(self.mediaPlayer.state())
			#if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			#	self.mediaPlayer.pause()
			#else:
			self.mediaPlayer.play()

		def mediastate_changed(self, state):
			if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
				self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
			else:
				self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

		def position_changed(self, position):
			self.slider.setValue(position)

		def duration_changed(self, duration):
			self.slider.setRange(0, duration)

	app = QApplication(sys.argv)
	
	window1 = MainWindow()
	window1.show()
	
	app.exec()
	
if __name__ == '__main__':
	main()