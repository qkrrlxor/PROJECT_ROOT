import tkinter as tk
from tkinter import ttk
import video_editor

class VideoEditorUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Video Editor")
        self.label.pack(pady=10)
        
        self.edit_button = ttk.Button(self, text="Edit Video", command=self.edit_video)
        self.edit_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def edit_video(self):
        video_path = video_editor.edit_video()
        self.result_label.config(text=f"Video edited: {video_path}")