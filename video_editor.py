from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import os

def edit_video(video_path):
    # video_path를 사용하여 비디오를 편집하는 로직을 여기에 작성합니다.
    edited_video_path = f"edited_{video_path}"
    
    # 예제 편집 로직 (실제 편집 로직으로 대체 필요)
    if os.path.exists(video_path):
        with open(video_path, 'rb') as original_file:
            with open(edited_video_path, 'wb') as edited_file:
                edited_file.write(original_file.read())
    
    return edited_video_path

def add_subtitles(video_path, subtitles, output_path):
    try:
        video = VideoFileClip(video_path)

        # 자막을 추가할 시간과 텍스트 정보
        subtitle_clips = []
        for subtitle in subtitles:
            text_clip = TextClip(subtitle['text'], fontsize=24, color='white', bg_color='black')
            text_clip = text_clip.set_position(('center', 'bottom')).set_duration(subtitle['duration']).set_start(subtitle['start'])
            subtitle_clips.append(text_clip)

        # 자막을 비디오 위에 추가
        final_video = CompositeVideoClip([video] + subtitle_clips)
        final_video.write_videofile(output_path, codec='libx264')
        print(f"Video with subtitles saved to {output_path}")

        return output_path
    except Exception as e:
        print(f"Failed to add subtitles: {e}")
        return None

def add_background_music(video_path, music_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(music_path).subclip(0, video.duration)
        final_video = video.set_audio(audio)
        final_video.write_videofile(output_path, codec='libx264')
        print(f"Video with background music saved to {output_path}")

        return output_path
    except Exception as e:
        print(f"Failed to add background music: {e}")
        return None

if __name__ == "__main__":
    video_path = "output_video.mp4"  # 입력 비디오 경로
    output_path_with_subtitles = "output_video_with_subtitles.mp4"  # 자막이 포함된 비디오 경로
    output_path_final = "output_video_final.mp4"  # 최종 비디오 경로
    music_path = "background_music.mp3"  # 배경 음악 경로

    # 예시 자막 데이터
    subtitles = [
        {'text': "Hello, this is a test subtitle.", 'start': 0, 'duration': 5},
        {'text': "This is another subtitle.", 'start': 5, 'duration': 5}
    ]

    # 자막 추가
    video_with_subtitles = add_subtitles(video_path, subtitles, output_path_with_subtitles)

    # 배경 음악 추가
    if video_with_subtitles:
        add_background_music(video_with_subtitles, music_path, output_path_final)