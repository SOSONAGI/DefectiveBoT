# Author -> Avratanu Biswas 
# Youtube video ->
# Blog -> 

import streamlit as st
import base64

from openai import OpenAI
import os

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")


st.set_page_config(page_title="마감하자 이미지 비전 분석!", layout="centered", initial_sidebar_state="collapsed")
# Streamlit page setup
st.title("하자 이미지 분석 전문가 🤖")

api_key = st.secrets["OPENAI_API_KEY"]
# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# File uploader allows user to add their own image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    with st.expander("Image", expanded = True):
        st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

# Toggle for showing additional details input
show_details = st.toggle("Add details about the image", value=False)

if show_details:
    # Text input for additional details about the image, shown only if toggle is True
    additional_details = st.text_area(
        "Add any additional details or context about the image here:",
        disabled=not show_details
    )

# Button to trigger the analysis
analyze_button = st.button("하자 이미지 분석!", type="secondary")

# Check if an image has been uploaded, if the API key is available, and if the button has been pressed
if uploaded_file is not None and api_key and analyze_button:

    with st.spinner("Analysing the image ..."):
        # Encode the image
        base64_image = encode_image(uploaded_file)
    
        # Optimized prompt for additional clarity and detail
        prompt_text = (
            "당신은 마감하자 이미지를 전문적으로 분석하는 데 능숙한 챗봇입니다. 사용자가 제공하는 이미지를 면밀히 검토하고, 그 이미지에서 발견되는 마감하자들에 대해 상세히 설명해주세요."
            "도배 하자의 종류는 총 19 가지로 구분되며, 각 하자 유형에 대한 정의와 해결 방법을 알고 있어야 합니다."
            "가구수정, 걸레받이수정, 곰팡이, 꼬임, 녹오염, 들뜸, 면불량, 몰딩수정, 문틀창틀수정, 반점, 석고수정, 오염, 오타공, 울음, 이음부불량, 터짐, 틈새과다, 피스, 훼손로서 총 19 분류의 하자 입니다."
            "각 하자 유형의 해결 방안에 대한 정보는 아래를 참고해 주시기 바랍니다."
            "걸레받이수정: 걸레받이와 벽지 사이에 발생한 틈새 벌어짐을 말합니다. 걸레받이는 벽지옆면과 바닥재를 이을 때 쓰는 자재를 말하며 해당 부위 주변에 발생한 하자를 말하며, 이를 해결하기 위해서는 해당 부위만 봉합하거나 별도 작업이 어려우며, 개인이 혼자서 해결하기 어렵습니다. 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "곰팡이: 벽지면이나 몰딩과 벽지사이에 발생한 푸른색 곰팡이를 말합니다. 습하거나 누수가 발생하고 오랜 시간이 지나 발생하는 하자 유형을 말합니다. 이를 해결하기 위해서는  이를 해결하기 위해서는 해당 부위만 봉합하거나 별도 작업이 어려우며, 개인이 혼자서 해결하기 어렵습니다. 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "꼬임: 벽지면에 풀과의 접착 불량에 따라 울음과 비슷한 형식으로 하자가 발생하나, 용어대로 꼬인 형태로 발생하는 하자를 말하며, 해당 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "녹오염: 벽지면에 발생한 갈색의 점 형태를 말합니다. 통상 못이나 피스에 누수에 따라 녹슬어서 해당 녹슨 부분이 벽지면에 발생한 부분을 말하며, 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "들뜸: 벽지면과 몰딩 또는 가구 사이에 발생한 틈을 말합니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "면불량: 벽지면에 생긴 불규칙한 흠집, 구멍, 자국 등을 말합니다. 이는 훼손 및 일반 오염도 포함될 수 있습니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "몰딩수정: 벽지면과 몰딩 사이에서 발생한 손상을 말합니다. 몰딩은 통상 벽지 옆면 및 천장을 이을 때 붙이는 것을 말하며, 해당 부위에서 발생하는 하자를 말합니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "반점: 벽지면에 발생한 푸른색 또는 빨간색의 점을 말하며, 곰팡이와는 다르게 재생지로 제작된 석고보드와  풀접착에 따라 발생하는 하자로서, 녹오염 및 곰팡이와 색상이 다릅니다. 반점 하자는 그 부위가 극히 극미하게 발생한 경우 벽지색과 같은 붓팬으로 간단하게 터치업 작업으로 셀프로 시공이 가능하며, 매우 간단한 작업입니다. 허나, 그 하자의 부위가 매우 크다면 붓팬으로 터치업이 가능하나 기존 벽지면 색깔과 이질적으로 보이게 됨으로, 그 하자량이 상당할 경우 전문가와 상담하여 해결하거나, sosohajalab.com에 문의 또는 전문가 매칭 앱인 숨고를 통해 해결하시는 것을 추천드립니다."
            "오염: 벽지면에 발생한 다양한 색상의 선 또는 랜덤한 형태의 모양을 말합니다. 이는 반점 및 곰팡이와는 다른 유형의 하자이며, 제3자에 의해 발생한 사례가 많은 하자 입니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "오타공: 벽지면에 검은 구멍이 생긴 것을 말합니다. 통상 거실 천장의 등 주변에 많이 발생합니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "울음: 벽지면에 길 형태의 타원으로 기포처럼 발생한 것을 말합니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "이음부불량: 벽지면과 벽지면 사이가 벌어진 것을 말합니다. 간단하게 벽지 전용 풀을 구매 후 소량으로 벌어진 부위에 도포하면 간단하게 해결할 수 있으나, 그 부위가 매우 클 경우에는 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "틈새과다: 벽지면과 몰딩 사이에 과도한 틈새가 발생한 것을 말합니다. 하자 부위가 매우 극미할 경우 벽지 전용 풀을 사용해 개인이 혼자 벌어진 틈새를 매울수 있으나 그 부위가 매우 큰 경우 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "훼손: 벽지면 자체의 손상 및 벽지면과 몰딩에서 발생한 훼손을 말하며, 벽지 하자 중 일반 오염과 더불어 가장 많은 유형의 하자입니다. 하자 해결을 위해서는 해당 부위만 따로 부착하는 것은 어려우며, 전체 벽지 면갈이를 해야합니다. 이는 개인이 셀프로 하기 어려운 작업이며, 이를 해결하기 위해서는 전문가와 상담하여 해결하는 것이 가장 현명한 방법입니다. Sosohajalab.co.kr에 문의하시거나, 전문가 연결 앱인 숨고를 추천 드립니다."
            "다른 마감하자인 마루 바닥재, 대리석, 시트지, 도장면 등은 당신의 전문적 지식과 도배(벽지) 하자의 유사성을 참고해서 답변해 주시기 바랍니다."
            "각 하자의 특징과 이것이 왜 문제가 되는지를 간단하고 명확하게 설명해주세요. 또한, 이러한 하자를 어떻게 해결할 수 있는지에 대한 조언도 제공해주시기 바랍니다." 
            "굵은 글씨체로 이미지에 대한 간략한 설명을 캡션 형태로 추가해주세요. 이 설명은 비전문가도 쉽게 이해할 수 있도록 작성해주세요."
        )
    
        if show_details and additional_details:
            prompt_text += (
                f"\n\nAdditional Context Provided by the User:\n{additional_details}"
            )
    
        # Create the payload for the completion request
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ]
    
        # Make the request to the OpenAI API
        try:
            # Without Stream
            
            # response = client.chat.completions.create(
            #     model="gpt-4-vision-preview", messages=messages, max_tokens=500, stream=False
            # )
    
            # Stream the response
            full_response = ""
            message_placeholder = st.empty()
            for completion in client.chat.completions.create(
                model="gpt-4-vision-preview", messages=messages, 
                max_tokens=1200, stream=True
            ):
                # Check if there is content to display
                if completion.choices[0].delta.content is not None:
                    full_response += completion.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            # Final update to placeholder after the stream ends
            message_placeholder.markdown(full_response)
    
            # Display the response in the app
            # st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    # Warnings for user action required
    if not uploaded_file and analyze_button:
        st.warning("Please upload an image.")
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
