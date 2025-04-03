import tkinter as tk
from tkinter import ttk
import trending_topic_scheduler

class TrendingTopicSchedulerUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Trending Topic Scheduler")
        self.label.pack(pady=10)
        
        self.schedule_button = ttk.Button(self, text="Fetch Trending Topics", command=self.fetch_topics)
        self.schedule_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def fetch_topics(self):
        topics = trending_topic_scheduler.fetch_trending_topics()
        self.result_label.config(text="\n".join(topics))