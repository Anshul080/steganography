```markdown
# Steganography Tool

--------------------------------------------------------------------------------------------------------------------------------------------

## Installation
Install all the modules using requirements.txt
1. Clone the repository:
   ```bash
   git clone https://github.com/Anshul080/steganography.git
   ```
2. Navigate to the project directory:
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Tkinter Application (Steganography Tool.py):<br><br>

1. Select a PNG or JPEG image using the "Select Image" button.<br>
2. Enter a secret message in the text area.<br>
3. Click "Hide Data" to embed the message into the image (saved as `hidden_image.png`).<br>
4. Click "Show Data" to reveal a hidden message from the selected image.<br>
5. Click "Save Image" to create a new image (`secret_image.png`) with the entered message.<br><br>

NOTE: 1. An error message will appear if no image is selected before hiding or showing data.
      2. An error message will appear if no message is entered before hiding or saving.
      3. Ensure the image paths (e.g., `logo.jpg`, `logo1.png`) are correctly set or replace them with your own files.<br>

--------------------------------------------------------------------------------------------------------------------------------------------

### Streamlit Application (Steganography_Streamlit.py):<br><br>

1. Run the app:
   ```bash
   streamlit run Steganography_Streamlit.py
   ```
2. Upload a PNG or JPEG image using the file uploader.<br>
3. Choose "Hide Data" from the sidebar and enter a secret message, then click "Hide Message" to embed it (download `hidden_image.png`).<br>
4. Choose "Show Data" from the sidebar and click "Reveal Message" to extract any hidden message.<br><br>

NOTE: 1. An error message will appear if no image is uploaded.
      2. An error message will appear if no message is entered before hiding.
      3. A web browser is required to interact with the interface.<br>

--------------------------------------------------------------------------------------------------------------------------------------------

### RSA-Enhanced Application (Steganography_RSA.py):<br><br>

1. Run the app:
   ```bash
   streamlit run Steganography_RSA.py
   ```
2. Upload a PNG or JPEG image using the file uploader.<br>
3. Choose "Hide Data" from the sidebar, enter a secret message, and click "Hide Message" to encrypt and embed it (download `hidden_image.png`).<br>
4. Choose "Show Data" from the sidebar and click "Reveal Message" to decrypt and display the hidden message.<br><br>

NOTE: 1. An error message will appear if no image is uploaded.
      2. An error message will appear if no message is entered before hiding.
      3. A web browser is required to interact with the interface.<br>

--------------------------------------------------------------------------------------------------------------------------------------------

## Features:<br>

1. Supports PNG and JPEG image formats.<br>
2. Provides a graphical user interface for ease of use in the Tkinter app.<br>
3. RSA encryption option for enhanced security in the `Steganography_RSA.py` version.<br>
4. Option to download modified images with hidden messages in Streamlit apps.<br>

--------------------------------------------------------------------------------------------------------------------------------------------

<br>

## Errors:

#If no image is selected or uploaded, an error message will be displayed.<br>
#If no message is entered before hiding or saving, an error message will be displayed.<br>
#For Tkinter app, ensure image paths (e.g., `logo.jpg`, `logo1.png`) are valid or replace them.<br>

-------------------------------------------------------------------------------------------------------------------------------------------

```