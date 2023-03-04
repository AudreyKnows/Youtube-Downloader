from pytube import YouTube
import streamlit as st
import os
import re


directory= 'downloads/'
if not os.path.exists(directory):
    os.makedirs(directory)
    
st.set_page_config(page_title="Audrey Knows cloud ", page_icon=":cloud:", layout="wide", )     
st.subheader("Youtube Downloaderstreamlit run main.py")
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://drey-knows-cloud.s3.amazonaws.com/still-life-photography-shot-lemon-slices-falling-water-making-big-splash.jpg")
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)
         
st.cache(allow_output_mutation=True)
def get_info(url):
    yt = YouTube(url)
    streams= yt.streams.filter(progressive= True, type= 'video')
    details= {}
    details["image"]= yt.thumbnail_url
    details["streams"]= streams
    details["title"]= yt.title
    details["length"]= yt.length
    itag, resolutions, vformat, frate = ([] for i in range(4))
    for i in streams:
        res= re.search(r'(\d+)p', str(i))
        typ= re.search(r'video/(\w+)', str(i))
        fps= re.search(r'(\d+)fps', str(i))
        tag= re.search(r'(\d+)',str(i))
        itag.append(str(i)[tag.start():tag.end()])
        resolutions.append(str(i)[res.start():res.end()])
        vformat.append(str(i)[typ.start():typ.end()])
        frate.append(str(i)[fps.start():fps.end()])
    details["resolutions"]= resolutions
    details["itag"]= itag
    details["fps"]= frate
    details["format"]= vformat
    return details
    
st.title("YouTube Downloader 🍋")
url = st.text_input("Paste URL here 🍋", placeholder='https://www.youtube.com/')
if url:
    v_info= get_info(url)
    col1, col2= st.columns([1,1.5], gap="small")
    with st.container():
        with col1:            
            st.image(v_info["image"])   
        with col2:
            st.subheader("Video Details 🍋")
            res_inp = st.selectbox('__Select Resolution__', v_info["resolutions"])
            id = v_info["resolutions"].index(res_inp)            
            st.write(f"__Title:__ {v_info['title']}")
            st.write(f"__Length:__ {v_info['length']} sec")
            st.write(f"__Resolution:__ {v_info['resolutions'][id]}")
            st.write(f"__Frame Rate:__ {v_info['fps'][id]}")
            st.write(f"__Format:__ {v_info['format'][id]}")
            file_name = st.text_input('__Save as 🌱__', placeholder = v_info['title'])
            if file_name:        
                if file_name != v_info['title']:
                    file_name+=".mp4"
            else:
                file_name = v_info['title'] + ".mp4" 
                
        button = st.button("Download 🍋")
        if button:
            with st.spinner('Downloading🍃🍃🍃'):
                try:
                    ds = v_info["streams"].get_by_itag(v_info['itag'][id])
                    ds.download(filename= file_name, output_path= "downloads/")
                    st.success('Download Complete', icon="🌳")       
                    st.balloons()
                except:
                    st.error('Error: Save with a different name!', icon="⚠")