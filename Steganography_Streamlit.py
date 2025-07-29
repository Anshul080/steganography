import streamlit as st
from PIL import Image
from stegano import lsb

# Set up the Streamlit app
st.set_page_config(page_title="Steganography Tool", layout="centered")
st.markdown(
    """
    <style>
    .main {
        background-color: #e6f7ff; /* Light blue background */
        color: #333333; /* Dark text color */
    }
    .sidebar .sidebar-content {
        background-color: #f0f0f0; /* Light gray sidebar background */
        color: #000000; /* Black text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title and Description
st.title("🔒 Steganography Tool")
st.subheader("Hide and Reveal Secret Messages in Images")
st.markdown("---")
st.markdown(
    """
    This tool allows you to:
    - **Hide a secret message** inside an image.
    - **Reveal a hidden message** from an image.
    """
)

# Sidebar for navigation
st.sidebar.header("Options")
option = st.sidebar.radio("Choose an action:", ["Hide Data", "Show Data"])

# File upload section
st.markdown("### 📤 Upload an Image")
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if option == "Hide Data":
        # Input for secret message
        st.markdown("### ✏️ Hide Data in Image")
        secret_message = st.text_area("Enter your secret message:")
        if st.button("🔐 Hide Message"):
            if secret_message:
                # Hide the message in the image
                output_image_path = "hidden_image.png"
                secret_image = lsb.hide(uploaded_file, secret_message)
                secret_image.save(output_image_path)
                st.success("✅ Message hidden successfully!")
                st.download_button(
                    label="📥 Download Image with Hidden Message",
                    data=open(output_image_path, "rb"),
                    file_name="hidden_image.png",
                    mime="image/png",
                )
            else:
                st.error("❌ Please enter a secret message.")

    elif option == "Show Data":
        # Extract hidden data from the image
        st.markdown("### 🔍 Reveal Hidden Data")
        if st.button("🔓 Reveal Message"):
            try:
                revealed_message = lsb.reveal(uploaded_file)
                if revealed_message:
                    st.success(f"✅ Hidden Message: {revealed_message}")
                else:
                    st.warning("⚠️ No hidden message found in the image.")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
else:
    st.info("📂 Please upload an image to get started.")

# Footer
st.markdown("---")
