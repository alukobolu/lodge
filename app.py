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
    st.subheader("Rules & Requirements")
    rules = st.text_area(
        "Enter the rules and requirements",
        height=200,
        placeholder="Example:\n- Must be 18 or older\n- Must have valid email\n- Must have complete address"
    )

with col2:
    st.subheader("User Profile")
    profile = st.text_area(
        "Enter the user profile details",
        height=200,
        placeholder="""Example:
        Name: John Doe
        Age: 25
        Email: john@example.com
        Address: 123 Main St, City, Country
        Phone: +1-234-567-8900"""
    )

# Add some helpful instructions
st.info("""
📝 **How to use:**
1. Enter your rules/requirements on the left
2. Enter the user profile details as plain text on the right
3. Click 'Validate Profile' to check if the profile meets the requirements
""")

# Validate button
if st.button("Validate Profile", type="primary"):
    if rules and profile:
        with st.spinner("Validating profile..."):
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