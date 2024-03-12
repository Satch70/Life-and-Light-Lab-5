import cv2
import os
import numpy as np

# Assuming 'imaging' is in the current working directory, adjust if it's located elsewhere
base_dir = os.path.join(os.getcwd(), 'imaging')

# Define the directories relative to the base directory
input_dir = os.path.join(base_dir, 'photos')
output_dir = os.path.join(base_dir, 'rgb_processed')

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Construct the full file path
        filepath = os.path.join(input_dir, filename)

        # Load the image
        image = cv2.imread(filepath)

        # Split the RGB components
        b, g, r = cv2.split(image)

        # Create color versions for each component
        r_color = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
        g_color = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
        b_color = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])

        # Convert each component to a 3-channel grayscale image for visualization
        r_gray = cv2.merge([r, r, r])
        g_gray = cv2.merge([g, g, g])
        b_gray = cv2.merge([b, b, b])

        # Save the color and grayscale versions for each component
        for component, color_img, gray_img in zip(['red', 'green', 'blue'], [r_color, g_color, b_color], [r_gray, g_gray, b_gray]):
            color_output_path = os.path.join(output_dir, f'{component}_color_{filename}')
            gray_output_path = os.path.join(output_dir, f'{component}_gray_{filename}')
            
            cv2.imwrite(color_output_path, color_img)
            cv2.imwrite(gray_output_path, gray_img)

print("Processing completed.")
