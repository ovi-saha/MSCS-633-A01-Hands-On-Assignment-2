# Import the qrcode module to generate QR codes
import qrcode

def generate_qr_code(url):
    """
    Generates a QR code from the given URL and saves it as an image file.

    Parameters:
        url (str): The URL to encode in the QR code.
    """

    # Create a QRCode object with specific settings:
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (can restore up to 30% of data if QR is damaged)
        box_size=10,  # Size of each box (pixel) in the QR code
        border=4,  # Thickness of the border (minimum is 4)
    )

    # Add the input URL to the QR code
    qr.add_data(url)

    # Optimize the QR code size to fit the input data
    qr.make(fit=True)

    # Generate the image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Define the output filename for the QR code image
    output_file = "qrcode_output.png"

    # Save the image to the current directory
    img.save(output_file)

    # Inform the user that the QR code has been successfully saved
    print(f"QR Code successfully saved as '{output_file}'.")

# Entry point of the program
if __name__ == "__main__":
    # Display a title in the console
    print("=== QR Code Generator ===")

    # Ask the user to enter a URL
    input_url = input("Enter the URL to generate QR code: ")

    # Call the function to generate the QR code
    generate_qr_code(input_url)

