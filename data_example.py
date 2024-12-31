import matplotlib.pyplot as plt
from tifffile import imread

import ffmpeg

# get data:
data = imread('data.tif')
print('-> data.shape =', data.shape)
time_points, y_px, x_px = data.shape

# make folder for images:
folder = 'data_example'
directory = ffmpeg._make_directory(folder)

# make images with scale bar and text using matplotlib:
fig = plt.figure()

# set size, margins, space, max intensity and dpi:
x_inch = 6
y_inch = x_inch * y_px / x_px
xmargin, ymargin, space = 0.15, 0.1, 0.03
vmax = 2250
plt.figure(figsize=(x_inch, y_inch), dpi=100)

# loop over images adding scale bar and text:
for i in range(time_points):
    image = data[i, :, :]
    image[130:700, 30:40] = vmax # add white scale bar
    angle = i * 10
    print('-> projection angle = %02i'%angle)
    plt.clf()
    plt.imshow(image, cmap='CMRmap', vmin=0, vmax=vmax)
    plt.axis('off')
    plt.figtext(xmargin, ymargin + 3 * space,
                'scale bar = 100' + r'$\mu$m', # raw string aviods '\' warning
                color='white', family='monospace')
    plt.figtext(xmargin, ymargin + 2 * space,
                'Objective = 40x0.95 air',
                color='white', family='monospace')
    plt.figtext(xmargin, ymargin + space,
                'projection angle =%3sdeg'%('%i'%angle),
                color='yellow', family='monospace')
    plt.savefig(folder + '/img%06i.png'%i, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# make gif:
ffmpeg.images_to_gif(folder=folder, start=0, stop=time_points, fps=5, scale=1,
                     output='data.gif')
