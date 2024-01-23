import fitz  # PyMuPDF
import os

def split_pdf_to_images(pdf_path, output_folder, dpi=300):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the page
        zoom = dpi / 72  # Calculate zoom factor for desired DPI
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)  # Render page to an image pixmap with higher resolution

        # Define the output image path
        output_image_path = output_folder / f"page_{page_num + 1}.png"


        # Save the image
        pix.save(output_image_path)

    # Close the document
    doc.close()

