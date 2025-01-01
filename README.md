# ffmpeg
Basic video editing in Python with ffmpeg.
## Quick start:
If you already have Python and ffmpeg installed then download the repository and run:
- **'ffmpeg.py'** to test various video and image coversions using _'input.mp4'_.
- **'data_example.py'** to convert _'data.tif'_ to a .gif with scale bar and text.

![social_preview](https://github.com/amsikking/ffmpeg/blob/main/social_preview.png)

## Download:
Check download options here: https://ffmpeg.org/download.html
- For windows these builds from gyan.dev have worked: https://www.gyan.dev/ffmpeg/builds/
- For example: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z

## Install:
- Unzip (using for example https://www.7-zip.org/)
- Drag and drop folder into good location (for example C:\Program Files\ffmpeg\)
- Find ffmpeg.exe (should be in C:\Program Files\ffmpeg\bin\ffmpeg.exe)
- Now add directory (C:\Program Files\ffmpeg\bin\) to PATH so it can be found
- For Windows 10 right click 'This PC' then click:
 Properties > Advanced System Settings > Advanced tab > Environment Variables. Add the directory...
- ffmpeg should now run from the command line (for example try 'ffmpeg -version')
