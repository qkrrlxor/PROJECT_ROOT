from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os

def create_video():
    video_path = "output_video.mp4"
    # 비디오 생성 코드
    return video_path

def text_to_speech(text, output_audio_path):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_audio_path)
        print(f"Audio saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Failed to convert text to speech: {e}")
        return None

def create_video_from_script(script, output_video_path, background_image_path):
    try:
        audio_path = text_to_speech(script, "output_audio.mp3")
        if audio_path is None:
            return None

        image_clip = ImageClip(background_image_path, duration=10)
        audio_clip = AudioFileClip(audio_path)

        video_clip = image_clip.set_audio(audio_clip)
        video_clip.write_videofile(output_video_path, fps=24)
        print(f"Video saved to {output_video_path}")

        if os.path.exists(audio_path):
            os.remove(audio_path)

        return output_video_path
    except Exception as e:
        print(f"Failed to create video: {e}")
        return None

if __name__ == "__main__":
    script = "This is a test script for the video."
    background_image_path = "background.jpg"
    output_video_path = "output_video.mp4"

    create_video_from_script(script, output_video_path, background_image_path)
