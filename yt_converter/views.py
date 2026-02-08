from django.shortcuts import render
import yt_dlp
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse

# Create your views here.

@login_required
def converter_view(request):
    if request.method == 'GET':
        return render(request, 'yt_converter/converter.html')

    url = request.POST.get('link')
    def generate_messages(url):
        yield """
        <style>
            body { background: #1e1e1e; color: #d4d4d4; font-family: 'Consolas', monospace; padding: 20px; line-height: 1.6; }
            .info { color: #569cd6; }
            .success { color: #4ec9b0; font-weight: bold; }
            .process { color: #ce9178; }
            hr { border: 0; border-top: 1px solid #333; margin: 15px 0; }
        </style>
        <h3>Conversion status</h3>
        """
        options = {
            'format': 'bestaudio/best',
            'restrictfilenames': True,
            'ffmpeg_location': r'ffmpeg\bin\ffmpeg.exe',
            'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'converted_music/user_{request.user}/%(title)s.%(ext)s'
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                yield "<p class='info'>Downloading information from YouTube...</p>"
                info = ydl.extract_info(url, download=False)

                items = info.get('entries', [info])
                count = len(items)
                yield f"<p class='info'>Tracks detected: {count}</p><hr>"

                for i, item in enumerate(items, 1):
                    yield f"<p class='process'>[{i}/{count}] Processing: <strong>{item['title']}</strong>...</p>"

                    video_url = item.get('webpage_url') or url
                    ydl.download([video_url])
                    
                    yield f"<p class='success'>✅ Ready!</p>"
                    yield "<script>window.scrollTo(0,document.body.scrollHeight);</script>"

                yield "<hr><h2 class='success'>All songs have been converted!</h2>"
                yield "<a href='/' style='color: #569cd6;'>Return to main page</a>"

        except Exception as e:
            yield f"<p style='color: #f44747;'>❌ An error occurred: {str(e)}</p>"


    return StreamingHttpResponse(generate_messages(url))