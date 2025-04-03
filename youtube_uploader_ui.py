import tkinter as tk
from tkinter import ttk
import youtube_uploader

class YouTubeUploaderUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="YouTube Uploader")
        self.label.pack(pady=10)
        
        self.upload_button = ttk.Button(self, text="Upload Video", command=self.upload_video)
        self.upload_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def upload_video(self):
        video_id = youtube_uploader.upload_video()
        self.result_label.config(text=f"Video uploaded to YouTube: {video_id}")