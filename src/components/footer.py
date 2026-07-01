import streamlit as st


def footer_home():
    logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY1ingS_pNNMRDHXmwX4K6yyjR5jf3wMdIEbb46IDTsQ&s=10"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        
        <img src="{logo_url}" style="
            height:45px;
            width:auto;
            display:block;
            margin-top:-4px;
        ">
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY1ingS_pNNMRDHXmwX4K6yyjR5jf3wMdIEbb46IDTsQ&s=10"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:45px; margin-top:-5px;' />
        </div>
                
                """, unsafe_allow_html=True)
