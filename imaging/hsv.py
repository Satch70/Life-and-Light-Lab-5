import cv2
import os

# Assuming 'imaging' is in the current working directory, adjust if it's located elsewhere
base_dir = os.path.join(os.getcwd(), 'imaging')

# Define the directories relative to the base directory
input_dir = os.path.join(base_dir, 'photos')
output_dir = os.path.join(base_dir, 'hsv_processed')

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

        # Convert the image to HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Split the HSV components
        h, s, v = cv2.split(hsv_image)

        # Convert each component to a 3-channel grayscale image for visualization
        h_gray = cv2.merge([h, h, h])
        s_gray = cv2.merge([s, s, s])
        v_gray = cv2.merge([v, v, v])

        # Save the Hue component grayscale image
        h_output_path = os.path.join(output_dir, f'hue_{filename}')
        cv2.imwrite(h_output_path, h_gray)

        # Save the Saturation component grayscale image
        s_output_path = os.path.join(output_dir, f'saturation_{filename}')
        cv2.imwrite(s_output_path, s_gray)

        # Save the Value component grayscale image
        v_output_path = os.path.join(output_dir, f'value_{filename}')
        cv2.imwrite(v_output_path, v_gray)

print("Processing completed.")
