import cv2 
import matplotlib.pyplot as plt


# Load an image from file as function
def load_image(image_path):
    image = cv2.imread(image_path)
    return image

# Display an image as function
def display_image(image, title="Image"):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")

# grayscale an image as function
def grayscale_image(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img_gray


# Save an image as function
def save_image(image, output_path):
    cv2.imwrite(output_path, image)


# flip an image as function 
def flip_image(image):
    flipped_image = cv2.flip(image, 1)  # 1: Horizontal flip
    return flipped_image


# rotate an image as function
def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image


if __name__ == "__main__":
    # Load an image from file
    img = load_image("uet.png")

    # Display the image
    display_image(img, "Original Image")
    plt.show()
    
    # Convert the image to grayscale
    img_gray = grayscale_image(img)

    # Display the grayscale image
    display_image(img_gray, "Grayscale Image")
    plt.show()

    # Save the grayscale image
    save_image(img_gray, "images/lena_gray.jpg")

    # Flip the grayscale image
    img_gray_flipped = flip_image(img_gray)

    # Display the flipped grayscale image
    display_image(img_gray_flipped, "Flipped Grayscale Image")
    plt.show()

    # Rotate the grayscale image
    img_gray_rotated = rotate_image(img_gray, 70)

    # Display the rotated grayscale image
    display_image(img_gray_rotated, "Rotated Grayscale Image")
    plt.show()

    # Save the rotated grayscale image
    save_image(img_gray_rotated, "images/lena_gray_rotated.jpg")

    img_flipped = flip_image(img)
    img_rotated = rotate_image(img, 70)
    save_image(img_flipped, "./uet_flipped.jpg")
    save_image(img_rotated, "./uet_rotated.jpg")
    