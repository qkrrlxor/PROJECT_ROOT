from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os

# Step 1: Convert text to speech
def create_video(script, length=60):
    # script와 length를 사용하여 비디오를 생성하는 로직을 여기에 작성합니다.
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

# Step 2: Create a video from a script
def create_video_from_script(script, output_video_path, background_image_path):
    try:
        # Convert script to speech
        audio_path = text_to_speech(script, "output_audio.mp3")
        if audio_path is None:
            return None

        # Load background image and audio
        image_clip = ImageClip(background_image_path, duration=10)  # Adjust duration as needed
        audio_clip = AudioFileClip(audio_path)

        # Set audio to the image
        video_clip = image_clip.set_audio(audio_clip)

        # Save the final video
        video_clip.write_videofile(output_video_path, fps=24)
        print(f"Video saved to {output_video_path}")

        # Clean up temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

        return output_video_path
    except Exception as e:
        print(f"Failed to create video: {e}")
        return None

# Step 3: Main function to execute the video creation process
if __name__ == "__main__":
    script = "This is a test script for the video."  # Sample script
    background_image_path = "background.jpg"  # Path to background image
    output_video_path = "output_video.mp4"  # Path to output video

    create_video_from_script(script, output_video_path, background_image_path)