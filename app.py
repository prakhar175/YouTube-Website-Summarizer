import validators # type: ignore
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader

st.set_page_config(page_title="Summarization from YT|Website")
st.title("Summarization using Langchain")
st.subheader("Summarize URL")
options=['Llama-4','Mistral','Gemma 2','Llama-3.3']
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 200px !important;
        }
        [data-testid="stSidebar"] > div:first-child {
            width: 200px !important;
        }
    </style>
""", unsafe_allow_html=True)
with st.sidebar:
    groq_api_key=st.text_input("Groq API KEY",value="",type='password')
model=st.selectbox(label='Select the Model', options=options)
generic_url=st.text_input(label="Enter URL",label_visibility='collapsed',placeholder="Enter URL")

def checker(groq_api_key,generic_url):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide this info")
    elif not validators.url(generic_url):
        st.error("NOT a valid URL")
    else:
        return True     
prompt_temp="""
    Provide the summary of the following content in maximum of 300 words.
    Content: {text}
"""          
prompt=PromptTemplate(input_variables=['text'],template=prompt_temp)

if st.button("Summarize"):
    if not checker(groq_api_key,generic_url):
        st.stop()
    try:
        with st.spinner("waiting . . ."):
            if 'youtube.com' in generic_url:
                loader=YoutubeLoader.from_youtube_url(generic_url)
            else:
                loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"},encoding="utf-8")
            docs=loader.load()
            if not docs:
                st.warning("No captions found for this video. Please use another video with subtitles.")
                st.stop()
            if model =='Llama-4':
                llm=ChatGroq(model='meta-llama/llama-4-maverick-17b-128e-instruct')
            elif model == 'Mistral':
                llm =ChatGroq(model='mistral-saba-24b')
            elif model == 'Gemma 2':
                llm = ChatGroq(model='gemma2-9b-it')
            else:
                llm=ChatGroq(model='llama3-70b-8192')
            chain=load_summarize_chain(prompt=prompt,llm=llm,chain_type='stuff')
            output_summary=chain.invoke({'input_documents':docs})
            
            st.success(output_summary['output_text'])
    except Exception as e:
        st.exception(f"Exception:{e}")
        

