import tkinter as tk
from tkinter import ttk, messagebox
from ui.script_generator_ui import ScriptGeneratorUI
from ui.trending_topic_scheduler_ui import TrendingTopicSchedulerUI
from ui.video_creator_ui import VideoCreatorUI
from ui.video_editor_ui import VideoEditorUI
from ui.youtube_uploader_ui import YouTubeUploaderUI
import script_generator
import trending_topic_scheduler
import video_creator
import video_editor
import youtube_uploader

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Management Tool")
        self.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")
        
        self.script_generator_ui = ScriptGeneratorUI(self.tabs)
        self.tabs.add(self.script_generator_ui, text="Script Generator")
        
        self.trending_topic_scheduler_ui = TrendingTopicSchedulerUI(self.tabs)
        self.tabs.add(self.trending_topic_scheduler_ui, text="Trending Topic Scheduler")
        
        self.video_creator_ui = VideoCreatorUI(self.tabs)
        self.tabs.add(self.video_creator_ui, text="Video Creator")
        
        self.video_editor_ui = VideoEditorUI(self.tabs)
        self.tabs.add(self.video_editor_ui, text="Video Editor")
        
        self.youtube_uploader_ui = YouTubeUploaderUI(self.tabs)
        self.tabs.add(self.youtube_uploader_ui, text="YouTube Uploader")
        
        # Upload Type Selection
        self.upload_type_label = ttk.Label(self, text="Upload Type:")
        self.upload_type_label.pack(pady=5)
        
        self.upload_type_var = tk.StringVar(value="regular")
        self.upload_type_regular = ttk.Radiobutton(self, text="Regular Video", variable=self.upload_type_var, value="regular")
        self.upload_type_regular.pack(pady=5)
        
        self.upload_type_shorts = ttk.Radiobutton(self, text="YouTube Shorts", variable=self.upload_type_var, value="shorts")
        self.upload_type_shorts.pack(pady=5)
        
        # Video Length Input
        self.video_length_label = ttk.Label(self, text="Video Length (seconds):")
        self.video_length_label.pack(pady=5)
        
        self.video_length_entry = ttk.Entry(self)
        self.video_length_entry.pack(pady=5)
        
        # Topic Input
        self.topic_label = ttk.Label(self, text="Topic (leave blank for auto):")
        self.topic_label.pack(pady=5)
        
        self.topic_entry = ttk.Entry(self)
        self.topic_entry.pack(pady=5)
        
        # Start Button
        self.start_button = ttk.Button(self, text="Start", command=self.start_process)
        self.start_button.pack(pady=10)

    def start_process(self):
        # Get user inputs
        upload_type = self.upload_type_var.get()
        video_length = self.video_length_entry.get()
        topic = self.topic_entry.get()
        
        if not video_length.isdigit():
            messagebox.showerror("Input Error", "Video length must be a number.")
            return
        
        video_length = int(video_length)
        
        if not topic:
            topic = "Auto-generated Topic"  # 자동 생성된 주제
        
        try:
            # Step 1: Generate Script
            script = script_generator.generate_script(topic)
            
            # Step 2: Fetch Trending Topics (Optional)
            trending_topics = trending_topic_scheduler.fetch_trending_topics()
            
            # Step 3: Create Video
            video_path = video_creator.create_video(script, length=video_length)
            
            # Step 4: Edit Video
            edited_video_path = video_editor.edit_video(video_path)
            
            # Step 5: Upload Video
            if upload_type == "regular":
                video_id = youtube_uploader.upload_video(edited_video_path, "Video Title", "Video Description", ["tag1", "tag2"])
            elif upload_type == "shorts":
                video_id = youtube_uploader.upload_shorts(edited_video_path, "Shorts Title", "Shorts Description", ["shorts", "video"])
            
            # Display the result
            messagebox.showinfo("Process Completed", f"Video uploaded to YouTube: {video_id}")
        except Exception as e:
            messagebox.showerror("Process Error", str(e))

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()