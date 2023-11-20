import colorsys
import os

# Define color variables
start_color_hsl = (0, 50, 50)  # HSL
end_color_hsl = (276, 75, 75)  # HSL

# Define shadow parameters
depth = 10
blur = 1
slope = 4  # Slope angle for the shadow offsets
offset_factor = 1  # Overall shadow thickness

filename = 'shadow.css'  # Filename for the CSS output

# Convert HSL to RGB
rgb_start = colorsys.hls_to_rgb(
    start_color_hsl[0] / 360, start_color_hsl[1] / 100, start_color_hsl[2] / 100)
rgb_end = colorsys.hls_to_rgb(
    end_color_hsl[0] / 360, end_color_hsl[1] / 100, end_color_hsl[2] / 100)

# Generate color gradient using the provided function


def generate_gradient(start, end, steps):
    gradient = []
    for i in range(steps):
        r = start[0] + (end[0] - start[0]) * i / steps
        g = start[1] + (end[1] - start[1]) * i / steps
        b = start[2] + (end[2] - start[2]) * i / steps
        gradient.append((r, g, b))
    return gradient


gradient = generate_gradient(rgb_start, rgb_end, depth)

# Generate CSS and write to file
if os.path.exists(filename):
    os.remove(filename)

with open(filename, 'w') as f:
    f.write('* { text-shadow: \n')  # Start of the text-shadow property

    for i in range(depth):
        # Convert RGB to HEX
        hex_color = '#{:02x}{:02x}{:02x}'.format(
            int(gradient[i][0] * 255), int(gradient[i][1] * 255), int(gradient[i][2] * 255))

        # Calculate y-offset based on slope and offset factor
        y_offset = slope * i * offset_factor

        # Generate CSS text for the shadow
        shadow_text = f'  {i}px {y_offset}px {blur}px {
            hex_color}, -{i}px {y_offset}px {blur}px {hex_color}'

        # Add newlines and commas based on position
        # If the last shadow, add semicolon and a shadow with x 0
        if i == depth - 1:
            shadow_text += f',\n  0px {y_offset}px {blur}px {hex_color};\n'
        else:
            shadow_text += ',\n'

        # Write the shadow text to the file
        f.write(shadow_text)

    f.write('};')  # End of the text-shadow property
