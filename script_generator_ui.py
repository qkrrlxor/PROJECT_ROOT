import tkinter as tk
from tkinter import ttk
import script_generator

class ScriptGeneratorUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Enter Topic:")
        self.label.pack(pady=10)
        
        self.topic_entry = ttk.Entry(self)
        self.topic_entry.pack(pady=10)
        
        self.generate_button = ttk.Button(self, text="Generate Script", command=self.generate_script)
        self.generate_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def generate_script(self):
        topic = self.topic_entry.get()
        script = script_generator.generate_script(topic)
        self.result_label.config(text=script)