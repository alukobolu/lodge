import streamlit as st
import json
from index import categorize

SECRET = st.secrets["wetro_api_key"]
# Set page configuration
st.set_page_config(
    page_title="Profile Validator",
    page_icon="✅",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("✨ Profile Validator")
st.markdown("### Validate user profiles against specific rules")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Listing Address")
    rules = st.text_input(
        "Enter the listing address",
        placeholder="Example: 123 Main St, City, Country"
    )

with col2:
    st.subheader("Airbnb Listing")
    profile = st.text_input(
        "Enter the airbnb listing details",
        placeholder="""Example: https://www.airbnb.com/rooms/000000"""
    )

# Add some helpful instructions
st.info("""
📝 **How to use:**
1. Enter the listing address on the left
2. Enter the airbnb listing url on the right
3. Click 'Validate Listing' to check if the listing meets the requirements
""")

# Validate button
if st.button("Validate Listing", type="primary"):
    if rules and profile:
        with st.spinner("Validating listing..."):
            try:
                result = categorize(SECRET,rules, profile)
                
                # Display results in a nice format
                if result['isValid']:
                    st.success("Profile Validation Result")
                else:
                    st.error("Profile Validation Result")
                
                # Create three columns for results
                res_col1, res_col2 = st.columns(2)
                
                with res_col1:
                    st.metric("Valid", "Yes" if result['isValid'] else "No")
                
                with res_col2:
                    st.metric("Likelihood", result['likelihood'])
                
                st.markdown("### Explanation")
                st.info(result['reasonExplanation'])
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in both the rules and profile fields.")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ by Wetrocloud"
) 