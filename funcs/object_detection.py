import streamlit as st
from streamlit_webrtc import webrtc_streamer

def app():
    st.title('Object Detection')
    
    st.write('Use your camera to detect object and estimate depth.')
    
    # Use camera
    use_camera = st.checkbox('Use Camera')
    
    if use_camera:
        # Capture and process video frames for gesture detection
        webrtc_streamer(key="sample", sendback_audio=False, rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})