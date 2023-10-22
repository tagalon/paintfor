# Import required libraries
import streamlit as st
import requests 
import openai
import json
from translate import format_langs, translate_text, split_string
from data import fields

external_stylesheets = ["styles.css"]

print(translate_text, format_langs())

def unpack(arg):
    data = {}
    for element in arg:
        data[element["Name"]] = element["RGB"]
    names, colors = data.keys(), data.values()
    return names, colors

css = r'''
    <style>
        [data-testid="stForm"] {border: 0px}
    </style>
'''
st.markdown(css, unsafe_allow_html=True)

def translate_texts(args):
    translated = [translate_text(x, st.session_state.selected_lang) for x in args]
    return translated

# Streamlit app
def main():
    select_q = 'Select your language'
    if 'selected_lang' not in st.session_state:
        st.session_state.selected_lang = 'English'
    # select_q = translate_text(select_q, st.session_state.selected_lang)
    selected_lang = st.selectbox(select_q, format_langs(), index=format_langs().index(st.session_state.selected_lang))
    st.session_state.selected_lang = selected_lang

    title = "Your Comprehensive Guide to Picking the Best Paint!"
    # title = translate_text(title, st.session_state.selected_lang)
    st.title("🎨" + title + "🎨")

    with st.form(key='paint_form'):
        form_intro = "Answer the questions below and get a personalized paint recommendation!"
        # form_intro = translate_text(form_intro, st.session_state.selected_lang)
        st.write(form_intro)

        q1 = "Where will you paint?"
        # q1 = translate_text(q1, st.session_state.selected_lang)
        st.header("1. "+q1)
        q1_arg = ['Indoors (like your bedroom or kitchen)', 'Outdoors (like the outside of your house or a fence)']

        # q1_arg = translate_texts(q1_arg)
        location = st.radio('', q1_arg)
        
        q1_why = "Why? Paints are made differently for inside and outside. Outdoor paints are tou3_leagh and can handle rain and sun, while indoor paints are usually smoother and cleaner."
        # q1_why = translate_text(title, st.session_state.selected_lang)
        st.write(q1_why)

        q2 = "What are you painting on?"
        # q2 = translate_text(q2, st.session_state.selected_lang)
        st.header("2. "+q2)
        q2_arg = ['Wood', 'Metal', 'Wall (like drywall or plaster)', 'Brick or Stone']
        # q2_arg = translate_texts(q2_arg)
        surface = st.radio('', q2_arg)

        q2_why = "[🔗Check out this link for more about surfaces and paints!](https://www.thespruce.com/choosing-the-right-type-of-paint-for-all-types-of-materials-1821166)"
        # q2_why = translate_text(q2_why, st.session_state.selected_lang)
        st.write(q2_why)
        
        q3 = "Shiny or Not Shiny?"
        # q3 = translate_text(q3, st.session_state.selected_lang)
        st.header("3. "+q3)
        q3_arg = ['Super Shiny (Gloss)', 'A Little Shiny (Semi-Gloss or Satin)', 'Not Really Shiny (Eggshell or Matte)']
        # q3_arg = translate_texts(q3_arg)
        sheen = st.radio('', q3_arg)
        q3_why = "Why? The shininess (or 'sheen') changes how the paint looks and feels. For example, a shiny paint might be easier to clean but will show more bumps and mistakes."
        # q3_why = translate_text(q3_why, st.session_state.selected_lang)
        st.write(q3_why)
        q3_learn = "[🔗Learn about paint finishes here!](https://www.bhg.com/decorating/paint/how-tos/choosing-paint-finish/)"
        # q3_learn = translate_text(q3_learn, st.session_state.selected_lang)
        st.write(q3_learn)

        names, colors = unpack(fields)
        q4 = "What colors do you LOVE?"
        # q4 = translate_text(q4, st.session_state.selected_lang)
        st.header("4. "+q4)
        q4_detail = "You can select more than one color."
        # q4_detail = translate_text(q4_detail, st.session_state.selected_lang)
        st.write(q4_detail)
        q4_choose = 'Pick Your Colors'
        # q4_choose = translate_text(q4_choose, st.session_state.selected_lang)
        colors = st.multiselect(q4_choose, options=names)
        q4_response = f"You picked {colors}! The color sets the mood! Bright colors might make you happy and energetic, while soft colors might feel calming."
        # q4_response = translate_text(q4_response, st.session_state.selected_lang)
        st.write(q4_response)

        q4_learn = "[🔗Find cool color ideas here!](https://www.sherwin-williams.com/visualizer#/active)"
        # q4_learn = translate_text(q4_learn, st.session_state.selected_lang)
        st.write(q4_learn)

        
        q5 = "Is the place busy or messy?"
        # q5 = translate_text(q5, st.session_state.selected_lang)
        st.header("5. "+q5)
        q5_arg = ['Yes, like a kitchen or playroom.', 'No, like a bedroom or living room.']
        # q5_arg = translate_texts(q5_arg)
        messy = st.radio('', q5_arg)
        q5_why = "Why? Busy places might need paint that's easy to clean. If you get spaghetti sauce on the wall, you'll want to clean it off easily!"
        # q5_why = translate_text(q5_why, st.session_state.selected_lang)
        st.write(q5_why)

        q6 = "Do you want your paint to be super safe for the environment?"
        # q6  = translate_text(q6, st.session_state.selected_lang)
        st.header("6. " +q6)
        q6_arg = ['Yes', "It's okay if it's not."]
        # q6_arg = translate_texts(q6_arg)
        eco_friendly = st.radio('', q6_arg)
        q6_why = "Why? Some paints have fewer chemicals, which is good for our planet! They're called 'low-VOC' paints."
        # q6_why = translate_text(q6_why, st.session_state.selected_lang)
        st.write(q6_why)
        q6_learn = "[🔗Learn about safe paints here!](https://www.epa.gov/indoor-air-quality-iaq/what-are-volatile-organic-compounds-vocs)"
        # q6_learn = translate_text(q6_learn, st.session_state.selected_lang)
        st.write(q6_learn)

        q7 = "Do you need a primer?"
        # q7 = translate_text(q7, st.session_state.selected_lang)
        st.header("7. " +q7) 
        primer_needed = st.radio('', ['Yes', 'No', "I'm not sure."])
        q7_why = "Sometimes, before the real color, you put a special paint called 'primer.' It's like getting the wall ready for its new color!"
        # q7_why = translate_text(q7_why, st.session_state.selected_lang)
        st.write(q7_why)
        q7_why_2 = "Why? Primer helps the real color look even better and stick properly."
        # q7_why_2 = translate_text(q7_why_2, st.session_state.selected_lang)
        st.write(q7_why_2)


        # t_label = translate_text('Get Recommendation', st.session_state.selected_lang)
        submit_button = st.form_submit_button(label='Get Recommendation')
        translate_arg = st.session_state.selected_lang
        if submit_button:
            st.subheader("🎨 Here's the best paint for you! 🎨")
            # Logic for personalized recommendationgit 
            # Display the recommendation
            prompt = generate_enriched_prompt(location, surface, sheen, colors, messy, eco_friendly, primer_needed)
            if prompt:
                with st.spinner(f'Generating your own guide!'):
                    response = get_response_from_chatgpt(prompt, selected_lang)
                    # response = translate_text(response, translate_arg)
                    st.markdown("""<script>
                                document.addEventListener('copy', function(e){
                                e.clipboardData.setData('text/plain', 'Copying not allowed!');
                                e.preventDefault();
                                });
                                document.addEventListener('cut', function(e){
                                e.clipboardData.setData('text/plain', 'Cutting not allowed!');
                                e.preventDefault();
                                });
                                document.addEventListener('paste', function(e){
                                e.preventDefault();
                                }); </script> """, unsafe_allow_html=True)
                    st.write(response)
                    

def generate_enriched_prompt(location, surface, sheen, colors, messy, eco_friendly, primer_needed):
    base_prompt = "Provide a comprehensive guide for a user looking to paint a project. Here are the details:\n"

    location_detail = f"- **Location**: {location}\n"
    surface_detail = f"- **Surface**: {surface}\n"
    sheen_detail = f"- **Finish/Sheen**: {sheen}\n"
    color_detail = f"- **Chosen Colors**: {', '.join(colors)}\n"
    messy_detail = f"- **Area Type**: {'Busy/messy area' if messy.startswith('Yes') else 'Standard area'}\n"
    eco_detail = f"- **Environmental Concern**: {'Yes' if eco_friendly.startswith('Yes') else 'No'}\n"
    primer_detail = f"- **Primer Concern**: {primer_needed}\n"

    prompt = base_prompt + location_detail + surface_detail + sheen_detail + color_detail + messy_detail + eco_detail + primer_detail

    return prompt

def get_response_from_chatgpt(prompt, lang=None):
    # Set up the endpoint and headers
    endpoint_url = "https://api.openai.com/v1/chat/completions"
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json",
   }

    print(headers)

    # Define the request payload
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
        {"role": "system", "content": "You are a profesional paint specialist."},
        {"role": "user", "content": prompt}],
        "max_tokens": 2000,  # adjust this as needed
    }

    # Make the API request
    response = requests.post(endpoint_url, headers=headers, data=json.dumps(data))
    response_str = response.content.decode("utf-8")
    response_data = json.loads(response_str)
    # Extract the response text
    response_text = response_data['choices'][0]['message']['content']
    write(response_text)
    if lang:
        response_text = translate_text(response_text, lang)
    return response_text

# Example usage


prompt = """
Provide a comprehensive guide for a user looking to paint a project. Here are the details:
- **Location**: Indoors (like your bedroom or kitchen)
- **Surface**: Wood
- **Finish/Sheen**: Super Shiny (Gloss)
- **Chosen Colors**: Blue, Red
- **Area Type**: Busy/messy area
- **Environmental Concern**: Yes
- **Primer Concern**: I'm not sure.
Include how to paint horizontal & verticla surfaces
"""

# Sample user responses for testing
user_responses = {
    'location': 'Indoors (like your bedroom or kitchen)',
    'surface': 'Wood',
    'sheen': 'Super Shiny (Gloss)',
    'colors': ['Blue', 'Red'],
    'messy': 'Yes, like a kitchen or playroom.',
    'eco_friendly': 'Yes',
    'primer_needed': "I'm not sure."
}
def write(arg):
    with open("response.txt", "w") as f:
        f.write(arg)

# Generate the enriched prompt for ChatGPT
# Run the Streamlit app
if __name__ == '__main__':
    main()

