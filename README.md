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
- Unzip ffmpeg (using for example https://www.7-zip.org/)
- Drag and drop the folder into good location (e.g. C:\Program Files\ffmpeg)
- Now add the directory (e.g. C:\Program Files\ffmpeg\bin\) to PATH so it can be found
- For Windows 10 right click 'This PC' then click:
 Properties > Advanced System Settings > Advanced tab > Environment Variables > System variables. Find the 'Path' variable, hit 'Edit' and add the directory with 'New'.
- ffmpeg should now run from the command line (for example try 'ffmpeg -version')
