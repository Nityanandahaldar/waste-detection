from pathlib import Path
import streamlit as st
import helper
import settings

st.set_page_config(
    page_title="Waste Detection",
)

st.sidebar.title("Detect Console")

model_path = Path(settings.DETECTION_MODEL)

st.title("Intelligent waste segregation system")
st.write("Start detecting objects in the webcam stream by clicking the button below. To stop the detection, click stop button in the top right corner of the webcam stream.")
st.markdown(
"""
<style>
    .stRecyclable {
        background-color: rgba(233,192,78,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
    }
    .stNonRecyclable {
        background-color: rgba(94,128,173,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        
    }
    .stHazardous {
        background-color: rgba(194,84,85,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
    }

</style>
""",
unsafe_allow_html=True
)

# st.sidebar.markdown(
#     f"<div class='stRecyclable'>Recyclable items:\n\n- plastic bottle</div>",
#     unsafe_allow_html=True
# )

# st.sidebar.markdown(
#     f"<div class='stNonRecyclable'>Non-Recyclable items:\n\n- scrap paper \n- plastic bag</div>",
#     unsafe_allow_html=True
# )

# st.sidebar.markdown(
#     f"<div class='stHazardous'>Hazardous items:\n\n- battery</div>",
#     unsafe_allow_html=True
# )
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
helper.play_webcam(model)

st.sidebar.markdown("This is a demo of the waste detection model.", unsafe_allow_html=True)

