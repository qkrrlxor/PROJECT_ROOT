from trending_topic_scheduler import fetch_trending_topics
from script_generator import generate_script
from video_creator import create_video_from_script
from video_editor import add_subtitles, add_background_music
from youtube_uploader import upload_video_to_youtube
import schedule
import time
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
def main_workflow():
    # 1단계: 주제 찾기
    topics = fetch_trending_topics()
    if not topics:
        print("No trending topics found.")
        return

    # 2단계: 대본 생성
    for topic in topics:
        script = generate_script(topic)
        if script:
            print(f"Generated Script for '{topic}':\n{script}")
            # 3단계: 동영상 생성
            video_path = create_video_from_script(script, f"{topic}_video.mp4", "background.jpg")
            if video_path:
                print(f"Video created for '{topic}': {video_path}")
                # 4단계: 동영상 편집
                subtitles = [
                    {'text': "Hello, this is a subtitle for the topic.", 'start': 0, 'duration': 5},
                    {'text': "This is another subtitle.", 'start': 5, 'duration': 5}
                ]
                video_with_subtitles = add_subtitles(video_path, subtitles, f"{topic}_video_with_subtitles.mp4")
                if video_with_subtitles:
                    final_video_path = add_background_music(video_with_subtitles, "background_music.mp3", f"{topic}_video_final.mp4")
                    if final_video_path:
                        print(f"Final video for '{topic}' is ready: {final_video_path}")
                        # 5단계: 동영상 업로드
                        upload_video_to_youtube(final_video_path, f"{topic} - Video", "Description of the video", ["tag1", "tag2"])

def schedule_main_workflow():
    # 매일 특정 시간에 main_workflow 실행 스케줄링
    schedule.every().day.at("08:00").do(main_workflow)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_main_workflow()