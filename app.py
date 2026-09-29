# ---- TOP OF FILE ----
import streamlit as st
from agents.host_agent import host_agent
from utils.media_utils import generate_custom_invite_image, generate_voice_invitation
from tools.location import get_cities_by_country
from utils.media_utils import generate_custom_invite_image, generate_voice_invitation
from utils.export_pdf import generate_pdf 
from utils.decor_image import generate_decor_image
from dotenv import load_dotenv
import os
load_dotenv()
st.set_page_config(page_title="AI Event Planner", layout="centered")

# ---- HEADER ----
st.title("🎉 AI Event Planner")
st.markdown("Plan weddings, meetups, and more — powered by multi-agent orchestration using **Google ADK**.")

#
with st.container():
    st.markdown("### 🌍 Event Basics")
    event_type = st.selectbox("Event Type", ["Wedding", "Birthday", "Corporate", "Anniversary"])

    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Country", ["AE", "US", "IN", "UK"])
    with col2:
        city_data = get_cities_by_country(country)
        city_list = city_data.get("cities", [])
        city = st.selectbox("City", city_list if city_list else ["Dubai"], key=f"city_selector_{country}")

# ---- SECTION: Event Details Form ----
with st.form("event_form"):
    st.markdown("### 📝 Event Details")
    col1, col2 = st.columns(2)
    with col1:
        guests = st.number_input("Number of Guests", min_value=10, value=100)
        budget = st.number_input("Total Budget (AED)", min_value=1000, value=5000)
    with col2:
        theme = st.selectbox("Event Theme", ["Boho Chic", "Modern Minimalist"])
        cuisine = st.selectbox(
            "Cuisine Preference",
            ["Lebanese", "Indian", "Italian", "BBQ", "Vegetarian", "Vegan", "Other"]
        )
        start_time = st.time_input("Event Start Time")

    submitted = st.form_submit_button("🧠 Plan My Event")

# ---- AGENT TRIGGER ----
if submitted:
    st.markdown("## ⏳ Generating your event plan...")

    input_data = {
        "event_type": event_type,
        "location": city,
        "guests": guests,
        "budget": budget,
        "theme": theme,
        "cuisine": cuisine,
        "start_time": str(start_time)
    }

    response = host_agent.run(input_data)

    st.markdown("## 📋 Your Event Plan")

    # VENUE
    st.markdown("### 🏛️ Venue Suggestions")
    venue_info = response.get("venue", {}).get("venues", [])
    if venue_info:
        for v in venue_info:
            name = v["name"]
            location = v["location"]
            st.markdown(f"**{name}** ({location})  \nCapacity: {v['capacity']} guests – Price: {v['price']} AED")
    else:
        st.info("No venue suggestions found.")

    # CATERING
    st.markdown("### 🍽️ Catering Options")
    catering_info = response.get("catering", {}).get("options", [])
    if catering_info:
        for c in catering_info:
            opts = ', '.join(c['dietary_options'])
            st.markdown(f"**{c['vendor']}**  \nMenu: {c['menu_type']} – {c['cost_per_person']} AED per person  \nOptions: {opts}")
    else:
        st.info("No catering info found.")

    # DECOR
    # st.markdown("### 🎨 Decor Theme")
    # decor_info = response.get("decor", {}).get("design", {})
    # if decor_info:
    #     colors = ', '.join(decor_info.get("recommended_colors", []))
    #     elements = ', '.join(decor_info.get("decor_elements", []))
    #     st.markdown(f"**Theme:** {decor_info.get('theme')}  \n**Colors:** {colors}  \n**Elements:** {elements}")
    # else:
    #     st.info("No decor theme found.")
        
    # Decor Preview Image
    st.markdown("### 🖼️ Decor Visual Preview")
    with st.spinner("Generating decor theme..."):
        try:
            decor_image = generate_decor_image(theme, event_type)
            st.image(decor_image, caption=f"{theme} Decor Concept", use_container_width=True)
            st.download_button(
                label="📥 Download Decor Visual",
                data=decor_image,
                file_name="decor_visual.png",
                mime="image/png"
            )
        except Exception as e:
            st.error(f"Decor generation failed: {str(e)}")


    # INVITE TEXT
    st.markdown("### 💌 Invitation Text")
    invite = response.get("invite", "No invite text")
    st.code(invite, language="text")

    # INVITE IMAGE
    if invite:
        st.markdown("### 🖼️ Invitation Card with Accurate Text")
        with st.spinner("Generating your custom invitation..."):
            image_bytes = generate_custom_invite_image(invite, theme)
        if image_bytes:
            st.image(image_bytes, caption="Personalized Card", use_container_width=True)
            st.download_button(
                label="📥 Download Invitation Card",
                data=image_bytes,
                file_name="invitation_card.png",
                mime="image/png"
            )
        else:
            st.error("Image generation failed.")

    # SCHEDULE
    st.markdown("### 🕒 Schedule")
    schedule = response.get("schedule", {}).get("schedule", [])
    if schedule:
        for item in schedule:
            st.markdown(f"- 🕓 {item['time']}: {item['activity']}")
    else:
        st.info("No schedule available.")

    # SPONSORS
    st.markdown("### 🤝 Sponsorship Ideas")
    sponsors = response.get("sponsors", {}).get("recommendations", [])
    if sponsors:
        for s in sponsors:
            st.markdown(f"**{s['brand']}** – _{s['match']}_  \n💬 {s['pitch']}")
    else:
        st.info("No sponsorship suggestions found.")

    # VOICE
    audio_url = response.get("audio_url")
    if audio_url:
        st.markdown("### 🔊 Voice Invitation")
        with st.spinner("🎤 Generating voice invitation..."):
            try:
                audio_data = generate_voice_invitation(invite)
                st.audio(audio_data, format="audio/mp3", start_time=0)
                st.download_button(
                    label="⬇️ Download Voice Invitation",
                    data=audio_data,
                    file_name="invitation_voice.mp3",
                    mime="audio/mpeg"
                )
            except Exception as e:
                st.error(f"Voice generation failed: {str(e)}")
    # Export button
    st.markdown("### 📄 Export")
    pdf_bytes = generate_pdf({**input_data, **response})
    st.download_button(
        label="📥 Download Full Plan (PDF)",
        data=pdf_bytes,
        file_name="event_plan_summary.pdf",
        mime="application/pdf"
    )
