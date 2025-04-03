import tkinter as tk
from tkinter import ttk
import video_creator

class VideoCreatorUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Video Creator")
        self.label.pack(pady=10)
        
        self.create_button = ttk.Button(self, text="Create Video", command=self.create_video)
        self.create_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def create_video(self):
        video_path = video_creator.create_video()
        self.result_label.config(text=f"Video created: {video_path}")