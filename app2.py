import streamlit as st
import json
# from index import categorize
from searchpdf import search_pdf

SECRET = st.secrets["wetro_api_key"]
# Set page configuration
st.set_page_config(
    page_title="Check Approved List",
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
st.title("✨ Listing Validator")
st.markdown("### Validate listings From the Approved List")

# Create two columns for input
col1, col2 = st.columns([1, 2])

with col1:
    # st.subheader("Searching type")
    # rules = st.text_input(
    #     "Enter Search type",
    #     placeholder="Example: 123 Main St, City, Country"
    # )
    type =  st.selectbox(
        "Search by?",
        ("License Number", "Property Address", "Expiration Date", "Property Management Company", "Property Owner Name"),
    )

with col2:
    col11, col12 = st.columns([3,1])
    with col11:
        # st.subheader("Search")
        query = st.text_input(
            "Enter detail",
            placeholder="""Example: VRR-0000-0000"""
        )
    with col12:
        page = st.number_input(
            "Page Number",
            value=1
        )

# Add some helpful instructions
st.info("""
📝 **How to use:**
1. Select the what you want to search by, options are License Number, Property Address, Expiration Date, Property Management Company, Property Owner Name
2. Enter the information you want to search
3. If the result is plenty you will recieve 5 at once, change the pagination to get more details
3. Click 'Validate Listing' to check if the listing meets the requirements
""")

# Validate button
if st.button("Validate Listing", type="primary"):
    if type and query:
        with st.spinner("Responding..."):
            try:
                result = search_pdf(SECRET,type, query,page)
                
                # Display results in a nice format
                # if result['isValid']:
                #     st.success("Profile Validation Result")
                # else:
                #     st.error("Profile Validation Result")
                
                # Create three columns for results
                # res_col1, res_col2 = st.columns(2)
                
                # with res_col1:
                #     st.metric("Valid", "Yes" if result['isValid'] else "No")
                
                # with res_col2:
                #     st.metric("Likelihood", result['likelihood'])
                
                st.markdown("### Response")
                st.info(result)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in both the rules and profile fields.")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ by Wetrocloud"
) 