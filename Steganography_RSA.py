import streamlit as st
from PIL import Image
from stegano import lsb
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization

# Set up the Streamlit app
st.set_page_config(page_title="Steganography Tool with RSA", layout="centered")
st.title("Steganography Tool with RSA Encryption")

# Generate RSA keys
@st.cache_resource
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

private_key, public_key = generate_keys()

# Sidebar for navigation
st.sidebar.header("Options")
option = st.sidebar.radio("Choose an action:", ["Hide Data", "Show Data"])

# File upload section
st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if option == "Hide Data":
        # Input for secret message
        st.header("Hide Data in Image")
        secret_message = st.text_area("Enter your secret message:")
        if st.button("Hide Message"):
            if secret_message:
                # Encrypt the message using RSA
                encrypted_message = public_key.encrypt(
                    secret_message.encode(),
                    OAEP(mgf=MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
                )
  # Debugging line
                # Hide the encrypted message in the image
                output_image_path = "hidden_image.png"
                secret_image = lsb.hide(uploaded_file, encrypted_message.hex())
                secret_image.save(output_image_path)
                st.success("Message encrypted and hidden successfully!")
                st.download_button(
                    label="Download Image with Hidden Message",
                    data=open(output_image_path, "rb"),
                    file_name="hidden_image.png",
                    mime="image/png",
                )
            else:
                st.error("Please enter a secret message.")

    elif option == "Show Data":
        # Extract hidden data from the image
        st.header("Reveal Hidden Data")
        if st.button("Reveal Message"):
            try:
                hidden_message = lsb.reveal(uploaded_file)
                if hidden_message:
                    # Decrypt the message using RSA
                    decrypted_message = private_key.decrypt(
                        bytes.fromhex(hidden_message),
                        OAEP(mgf=MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
                    )
                    st.success(f"Hidden Message: {decrypted_message.decode()}")
                else:
                    st.warning("No hidden message found in the image.")
            except Exception as e:
                st.error(f"An error occurred: {e}")