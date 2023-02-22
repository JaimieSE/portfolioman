import requests 
from PIL import Image
import streamlit as st




#pictures added stuff
image_doit = Image.open(r"C:\Users\June\Desktop\Python\Images\photo_6314201979752133422_y.jpg")
image_Figma1 = Image.open(r"C:\Users\June\Desktop\Python\Images\Starting page.png")
image_cat = Image.open(r"C:\Users\June\Downloads\photo_6316453779565818721_y.jpg")
image_Figma2 = Image.open(r"C:\Users\June\Desktop\Python\Images\iPhone 14 Pro - 1.png")
image_figma3 = Image.open(r"C:\Users\June\Desktop\Python\Images\iPhone 14 Pro - 3.png")
image_figma4 = Image.open(r"C:\Users\June\Desktop\Python\Images\iPhone 14 Pro - 4.png")
image_figma5 = Image.open(r"C:\Users\June\Desktop\Python\Images\iPhone 14 Pro - 5.png")
image_figma6 = Image.open(r"C:\Users\June\Desktop\Python\Images\iPhone 14 Pro - 6.png")
image_happy = Image.open(r"C:\Users\June\Desktop\Python\Images\111-1110771_thumbs-up-emoji-meme-hd-png-download.png")



st.set_page_config(page_title="Portfolio", page_icon=":smirk_cat:", layout="wide")

st.header("A Student Trying Her Best In This World")
st.write("_scroll all the way down for a little for fun thingy i made_")
#sidebar thingss
with st.container():
 with st.sidebar:
   menu = ["About Me","About Project"]
   choice = st.sidebar.selectbox("Additional Info!",menu)
   if choice == "About Project":
     st.subheader("What I used")
     st.write("I used Streamlit and coded using Visual Studio Code. I had Pycharm and Anaconda installed but I felt that VSC was the easiest platform to use as someone with zero experience at all")
     st.subheader("These are the websites I used as learning material")
     st.write("[The Streamlit Tutorials itself](https://docs.streamlit.io/)")
     st.write("[This life saving youtube channel](https://www.youtube.com/@CodingIsFun/featured)")
     st.write("Reddit forums")
     st.write("[This forum too](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/)")
     st.write("[Stack Overflow](https://stackoverflow.com/)")
     st.subheader("What I learnt")
     """The basic terminology of certain things such as "file path", "root directory" etc. I have learnt the basics of coding and can now code a simple blog on my own from scratch
     without guidance! More importantly, I realised that I actually **enjoyed** coding despite the warnings given to me by my peers :smirk_cat:"""
     st.subheader("What I hope to improve on")
     """My goal by the end of this month (February) is to be able to create a simple finance calculator and maybe expand into other languages, i.e HTML and C++"""
     st.image(image_happy)
   else:
    st.header("About me")
    st.image(image_cat)
    """My name is Jaimie, some call me James for short. I'm a fresh junior college graduate. Unsurprisingly, I enjoy
    watching shows and spending time with people, like many others do. However, that's not all I do with my spare time. On quiet days, I can and will spend my days cooped up in my room
    watching documentaries about anything and everything that comes to mind. As an extremely curious person who values knowledge as power, I value the art of questioning and exploring.
    """
    st.subheader("Random facts about me (why not)")
    """
   - I had 13 years of dance experience
   - Completed 4 grades of abacus
   - **LOVE** music (I cannot emphasize this enough)
   - I can type at 130wpm 
   - Massive Eater
   - Wants a dog and cat
    """







st.write("---")
st.subheader("A Brief Introduction to this 'passion project'")
st.write("##")
text_column, image_column = st.columns ((2, 1))
with text_column:

  st.write(
    """Its not often that I get the opportunity to explore my interests, with the heavy workloads and expectations to keep up, it wasn't easy to set aside time to think of what 
I was truly passionate about. There was a moment in time where I was determined to pursue medicine, then astrophysics. Slowly after, I was introduced to the latest craze of 
computing which really expanded my perspective of the world. So I realised that it was time to act on my feelings, which is what this passion project is about. I apologise if this 
website appears to be lackluster - it is my first time doing a hands on coding project with the help of youtube tutorials, online forums and hours of troubleshooting by exploring 
every function!"""
)





#PROJECT INTRODUCTION
with st.container():


 with st.container():
  st.write("---")
  st.subheader("Some of the issues I faced (and resolved) on my own")
  st.write("For one instance:")

code = '''image.open("spongebob.png")'''
st.code(code, language='python') 
st.write("I spent 2 hours trying to figure out how to insert pictures")
codes = '''image.open("File path of spongebob.png")'''
st.code(codes, language='python')
st.write('I thought this would work, but errors kept popping up, so I did further tampering :sob:')
coding = '''image.open(r"File Path of spongebob.png")'''
st.code(coding, language='python')

#post trauma resolution fr
with st.container():
 TT_column, IM_column = st.columns((2,3))
with TT_column:
 st.write("Turns out, I only had to add an 'r' to the front of it :confused:")
 st.write("Frustrating, yet _strangely_ rewarding")
 st.write("Unfortunately, this was one of the easier hurdles I faced, but this journey was very fulfillig")
 
with IM_column:
 st.image(image_doit, width= 300, caption= "my parents walking in on me troubleshooting")
 
st.write("---")

#Talking about the other passion projects I did lol

st.header("My Other Projects!")
st.subheader("Figma App Design")
st.write("This was a design project that I undertook to try my hand at visualising an application that I have **yet** have the ability to actually create.")
st.write("To see the whole design in action, you can click [here](https://www.figma.com/proto/howzl49kutxqNl7auywbI5/Project1?node-id=1%3A2&starting-point-node-id=1%3A2) to view")

st.write("---")
#putting the figma stuff now i guess 
with st.container():
   Figma_column, Exp_column, Figma2_column = st.columns((2, 3, 2))

with Figma_column:
 st.image(image_Figma1, caption ="first page of app")

with Exp_column:
  st.subheader("Introduction Page")
  """The goal of this app is to locate nearby Cafes around you as there are often many self-made Cafes around us that goes unnoticed due to their secluded location or lack of 
  public exposure in general. Moreover, cafe hopping hobbyists may find this application useful as it could save them tons of research timings."""
  st.write("**Upon signing up for the application**, the user will be directed to the application privacy policy page, as shown at the right")

with Figma2_column:
  st.image(image_Figma2, caption= "logging in as a new user")


with st.container(): 
  figma3_column, exp2_column, figma4_column = st.columns((2, 3, 2))

with figma3_column:
  st.image(image_figma3, caption ="assuming you're on iphone, this will be the prompt")

with figma4_column:
  st.image(image_figma4, caption= "Page to choose preference from")

with exp2_column:
  st.subheader("Preferences")
  """After agreeing to the privacy policies, the user will be redirected to a page to fill up preferences, allowing the user to further narrow down their desired 
 choices. This makes it more efficient to locate the type of cafe within their device's 3km radii."""

with st.container():
  figma5_column, exp3_column, figma6_column = st.columns((2,3,2))
  
with figma5_column:
  st.image(image_figma5, caption = "how the interface would look like")

with figma6_column:
  st.image(image_figma6, caption = "another example of choosing another preference" )

with exp3_column:
  st.subheader("Interface")
  """These are two examples of how the screens would look like after picking two difference prefences, in this case would be others and ice cream. The options are set by nearest 
  to you by default, which could be changed by clicking 'sort by'. The estimated distance of the cafes would be displayed together with the address. The cafe ratings are taken by
  google map reviews. Again, this is unfortunately just a hypothetical app that I have designed."""


st.write("Thats mostly it for my mini app design side project")   

st.write("---")

st.subheader("Here are some random extra codes that I was experimenting with - and worked. ")
"""It might not be relevant in my introduction but its a little section to display the new things I learnt over these few days :smiley:"""

with st.form(key='form1'):
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last name")
    dob = st.date_input("Date of birth")
    age = st.slider("How young are you?", 0, 130, 25)
    st.write("This form doesnt do anything")
    submit_button= st.form_submit_button(label='SignUp')

with st.form(key="form2"):
  st.subheader("This one gives opinions on your coffee taste:")
  name = st.text_input("How may I address you sir/ma'am/lad/youngin?")
  coffepref = st.selectbox("Coffee Preferences",["Latte", "Espresso", "Americano", "Macchiato", "Mocha", "Frappecino"])
  if coffepref == "Macchiato":
     st.write("You", name, "have an **exceptional, phenomenal, professional, amazing** taste")
  if coffepref == "Latte":
    st.write("You're taking the safest option, can't blame you, the world is too unpredictable these days, stay safe", name)
  if coffepref == "Espresso":
    st.write("I think you're overworked or sleep deprived. I refuse to believe that there are people who genuinely enjoys the taste of pure raw coffee beans. Go get some sleep", name)
  submit = st.form_submit_button(label = "Get judged today!")
  if coffepref == "Americano":
    st.write("Okay, you're not too bad. You are a just very neutral person", name, "and there is absolutely nothing wrong with that.")
  if coffepref == "Mocha":
    st.write(name, "just get milo.")
  if coffepref == "Frappecino":
    st.write(name, "I hope you can imagine the disappointment in my eyes. I was hoping no one chose this option but you just had to be special. No further comment, I wish you happiness.")

st.write("**_THIS IS A JOKE GUYS, I RESPECT ALL COFFEE PREFERENCES!_** :gray[except for frappecino enjoyers]")

st.balloons()