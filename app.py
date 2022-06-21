import streamlit as st
import streamlit_wordcloud as wordcloud
from PIL import Image
import pandas as pd
import base64
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components


st.set_page_config(layout="wide")

with st.sidebar:
    selected = option_menu("Main Menu", ["Objective & Technical Approach",
                                         'Perceptions of Immigrants Across Time',
                                         'Perceptions Across Minority Groups',
                                         'Hate Crime',
                                         'Interpretation'],
        default_index=0)
    selected


# Header Styling
st.markdown(""" <style> .header {
font-size:65px ; font-family: 'DIN condensed', 'American Typewriter';}
</style> """, unsafe_allow_html=True)

# Background Image

main_bg = "backgrounds/background_1.png"

@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover
    }}
    </style>
    '''
    return style

st.write(background_image_style(main_bg), unsafe_allow_html=True)

# Content Body

if selected == "Objective & Technical Approach":
    st.markdown('<p class="header">Objective & Technical Approach</p>',unsafe_allow_html=True)
    visualisation = 'https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/emevans97/39e062dd99a8a4d17c9a974bdbb25ad7/raw/8585d162f1d0afa337e3fed92450e6a829b028b2/unitensor.json'
    st.subheader("Objective")
    st.markdown('''
                The objective of this project was to use Natural Language Processing to analyse the attitudes of \
        key British right-wing publications to immigrants and minority groups. Specifically, to understand:
        - How immigrants have been portrayed across time
        - How portrayals vary across minority groups
        - How key events during peaks of hate crime offences were portrayed in the press
        ''')
    st.subheader("Technical Approach")
    st.write(f"1.3 million unique tweets made by The Sun, The Daily Mail and The Daily Express between 2008 and 2022 \
        were scraped and pre-processed. Top2Vec was used to identify themes in the data and RoBERTa \
        Base Emotion was used to identify sentiment and emotion. \n \n The TensorFlow \
        Embedding Projector below visualises Top2Vec and RoBERTa on a subset of the data used. Also\
        available [here]({visualisation}).")
    components.iframe(visualisation, scrolling=False, width=1200, height=800)
    st.subheader("Project Team")
    st.write("The project was completed in June 2022 by Jenna Tan, Ewan Evans, Humberto Vega Mendez and Ellis Latham.")


if selected == "Perceptions of Immigrants Across Time":
    st.markdown('<p class="header">Perceptions of Immigrants Across Time</p>',unsafe_allow_html=True)
    st.write("To analyse portrayals of immigrants in the right wing media, Top2Vec was used to identify \
            themes in tweets. \
            The wordclouds represent the most semantically similar words to \
            the selected search term, based on tweets made by The Sun, The Daily Mail UK, The Daily \
            Express and The Mail Online during the selected timeframe. ")
    st.markdown("""---""")
    option = st.selectbox('Please select a search term', ('Migrant', 'Refugee', 'Asylum (Seeker)'))
    options = ["2008", "2014-2017", "2017-2018", "2018-2020", "2022"]
    new = st.select_slider("Please Select Year Range", options=options)


    if new=="2008":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_1.png')
            st.image(image, use_column_width=True)
        if option=='Asylum (Seeker)':
            st.subheader('Search Term: Asylum (Seeker)')
            image = Image.open('data/asylum_1.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_1.png')
            st.image(image, use_column_width=True)
        if option=='Please Select an Option':
            st.write('No Option Selected!')


    elif new=="2014-2017":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_2.png')
            st.image(image, use_column_width=True)
        if option=='Asylum (Seeker)':
            st.subheader('Search Term: Asylum (Seeker)')
            image = Image.open('data/asylum_2.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_2.png')
            st.image(image, use_column_width=True)
        if option=='Please Select an Option':
            st.write('No Option Selected!')


    elif new=="2017-2018":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_3.png')
            st.image(image, use_column_width=True)
        if option=='Asylum (Seeker)':
            st.subheader('Search Term: Asylum (Seeker)')
            image = Image.open('data/asylum_3.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_3.png')
            st.image(image, use_column_width=True)
        if option=='Please Select an Option':
            st.write('No Option Selected!')

    elif new=='2018-2020':
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_4.png')
            st.image(image, use_column_width=True)

        if option== 'Asylum (Seeker)':
            st.subheader('Search Term: Asylum (Seeker)')
            image = Image.open('data/asylum_4.png')
            st.image(image, use_column_width=True)

        if option== 'Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_4.png')
            st.image(image, caption='Refugee 5', use_column_width=True)

        if option=='Please Select an Option':
            st.write('No Option Selected!')

    elif new=='2022':
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_5.png')
            st.image(image, use_column_width=True)

        if option== 'Asylum (Seeker)':
            st.subheader('Search Term: Asylum (Seeker)')
            image = Image.open('data/asylum_5.png')
            st.image(image, use_column_width=True)

        if option== 'Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_5.png')
            st.image(image, use_column_width=True)

        if option=='Please Select an Option':
            st.write('No Option Selected!')


if selected == "Perceptions Across Minority Groups":
    st.markdown('<p class="header">Perceptions Across Minority Groups</p>',unsafe_allow_html=True)
    st.write('''To analyse portrayals of minority groups in the right wing media, Top2Vec and RoBERTA were used to identify \
            themes and sentiment in tweets. \
            The wordclouds represent the most semantically similar words to \
        the selected search term, based on tweets made by The Sun, The Daily Mail UK, The Daily \
            Express and The Mail Online during the selected timeframe. The graphics represent the associated sentiment
            of the tweets, based on the selected search term. \n \n Data for Ukraine was \
                collected between January 2022 and June 2022, to reflect the timeframe of the on-going Ukrainian Crisis.
            ''')
    st.markdown("""---""")
    option = st.selectbox('Please select a search term',('Muslim', 'Syria', 'Ukraine'))
    slider = ["2008", "2014-2017", "2017-2018", "2018-2020", "2022"]
    new = st.select_slider("Please Select Year Range", options=slider)


    if new=="2008":
        if option=='Syria':
            st.subheader('Search Term: Syria')
            image = Image.open('data/syria_1.png')
            st.image(image, use_column_width=True)
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image = Image.open('data/muslim_1.png')
            st.image(image, use_column_width=True)


    elif new=="2014-2017":
        if option=='Syria':
            st.subheader('Search Term: Syria')
            image2 = Image.open('data/syria_2.png')
            st.image(image2, use_column_width=True)
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image2 = Image.open('data/muslim_2.png')
            st.image(image2, use_column_width=True)


    elif new=="2017-2018":
        if option=='Syria':
            st.subheader('Search Term: Syria')
            image3 = Image.open('data/syrian_3.png')
            st.image(image3, use_column_width=True)
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image3 = Image.open('data/muslim_3.png')
            st.image(image3, use_column_width=True)

    elif new=="2018-2020":
        if option=='Syria':
            st.subheader('Search Term: Syria')
            image3 = Image.open('data/syria_4.png')
            st.image(image3, use_column_width=True)
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image3 = Image.open('data/muslim_4.png')
            st.image(image3, use_column_width=True)

    elif new=="2022":
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image3 = Image.open('data/muslim_5.png')
            st.image(image3, use_column_width=True)
        if option=='Ukraine':
            st.subheader('Search Term: Ukraine')
            image = Image.open('data/Ukraine.png')
            st.image(image, use_column_width=True)


    col1,col2 = st.columns(2)

    with col1:


        if option=='Muslim' or option=='Ukraine' or option=='Syria':
            data_1 = pd.read_csv(f'data/{option}_data_1')
            data_2 = pd.read_csv(f'data/{option}_data_2')
            data_3 = pd.read_csv(f'data/{option}_data_3')
            data_4 = pd.read_csv(f'data/{option}_data_4')



        #3 Sentiment of Tweets over Time

        if option=='Muslim' or option=='Syria':
            fig_3 = px.line(data_3, x = 'Year', y=["Optimism", "Sadness", "Joy", "Anger"], title='Sentiment of Tweets Over Time',color_discrete_sequence=["yellow", "blue", "green", "red"])
            fig_3.update_layout(xaxis_range=[2008,2022])
            fig_3.update_layout(showlegend=True,legend_title='Emotion', title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})
            fig_3.update_xaxes(title='Year' )
            fig_3.update_yaxes( title='Number of tweets' )


        if option=='Ukraine':
            fig_3 = px.bar(data_3, x = 'Date', y='Optimism', title='Optimism Scores of Tweets Over Time',color_discrete_sequence=["green"])
            fig_3.update_layout(showlegend=False, title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})
            fig_3.update_xaxes(title='Date' )
            fig_3.update_yaxes( title='Optimism score' )
        st.plotly_chart(fig_3, use_container_width=True)

        #4 Positivity score by year, newspaper, likes

        if option=='Muslim':
            fig_4 = px.scatter(data_4, x="Date", y="Positive",
                               size="Like Count", color="Newspaper",
                               hover_name="Tweet", size_max=80, title = 'Positivity Score by Year, Newspaper and Number of Likes',)
            fig_4.update_yaxes(title='Positivity score' )
            fig_4.update_xaxes(title='Year' )
            fig_4.update_layout(title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})

        if option=='Syria':
            fig_4 = px.scatter(data_4, x="Date", y="Newspaper", color="Emotion",
                               hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["red", "yellow", "blue", "green"],
                               title = 'Tweets by Paper, Date, Emotion and Like Count')
            fig_4.update_layout(title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})

        if option=='Ukraine':
            fig_4 = px.scatter(data_3, x="Date", y="Newspaper", color="Emotion",
            hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["red", "yellow", "blue", "green"],
            title = 'Tweets by Paper, Date, Emotion and Like Count')
            fig_4.update_layout(title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})

        st.plotly_chart(fig_4, use_container_width=True)




    with col2:


            # 1: Sentiment Across Newspapers Over Time, 2011-2022

            if option=='Muslim' or option=='Syria':

                fig_1 = px.bar(data_1, y="Newspaper", x=['Positive','Neutral','Negative'], title="Sentiment Across Newspapers Over Time, 2011-2022", orientation='h', color_discrete_sequence=["green", "grey", "red"], animation_frame='year')
                fig_1.update_xaxes(showticklabels=False, title=None )
                fig_1.update_yaxes( title=None )
                fig_1.update_layout(legend_title='Sentiment',
                                    title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})

            if option=='Ukraine':
                fig_1 = px.bar(data_2, y="Newspaper", x=['Positive','Neutral','Negative'], title="Sentiment across Newspapers, Jan'22 - Jun'22",
                            color_discrete_sequence=["green", "grey", "red"],orientation='h')
                fig_1.update_xaxes(showticklabels=False, title=None )
                fig_1.update_yaxes( title=None )
                fig_1.update_layout(legend_title='Sentiment',
                                    title_font_family= "American Typewriter",
                                    title={
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})

            st.plotly_chart(fig_1, use_container_width=True)

            #2: Average Emotions Across Newspapers

            fig_2 = go.Figure()
            fig_2.add_trace(go.Scatterpolar(
                r=[data_2['Joy'].iloc[0], data_2['Optimism'].iloc[0],data_2['Anger'].iloc[0], data_2['Sadness'].iloc[0]],
                theta=['Joy','Optimism','Anger','Sadness'],
                name='Daily Express'
            ))
            fig_2.add_trace(go.Scatterpolar(
                r=[data_2['Joy'].iloc[1], data_2['Optimism'].iloc[1],data_2['Anger'].iloc[1], data_2['Sadness'].iloc[1]],
                theta=['Joy','Optimism','Anger','Sadness'],
                name='Daily Mail'
            ))
            fig_2.add_trace(go.Scatterpolar(
                r=[data_2['Joy'].iloc[2], data_2['Optimism'].iloc[2],data_2['Anger'].iloc[2], data_2['Sadness'].iloc[2]],
                theta=['Joy','Optimism','Anger','Sadness'],
                name='The Sun'
            ))

            fig_2.update_traces(fill='toself')
            fig_2.update_layout(legend_title='Newspaper',
                                    title_font_family= "American Typewriter",
                                    title={'text':'Average Emotion Across Newspapers, 2008-2022',
                                           'y':0.9,
                                           'x':0.5,
                                           'xanchor': 'center','yanchor': 'top'})
            st.plotly_chart(fig_2, use_container_width=True)



if selected == "Hate Crime":
    st.markdown('<p class="header">Hate Crime</p>',unsafe_allow_html=True)
    st.write('''The graph represents racially or religiously aggravated offenses in England \
        and Wales between 2015 and 2021. The wordclouds below represent the most semantically similar words to \
        select Twitter search terms, chosen to reflect key events at the peak of offences.\
        Tweets were made by The Sun, The Daily Mail UK, The Daily \
            Express and The Mail Online during the year of the event.
            ''')
    crime = pd.read_csv("data/hate_crime.csv")
    # Create figure
    fig = go.Figure()

    # Add hate crime
    fig.add_trace(go.Scatter(x=crime['Date'], y=crime['Total offences'], name='Hate Crime'))

    slider = ["EU Referendum", "Manchester Attacks", "Bank Robbers", "Chimpanzee", "Black Lives Matter"]
    new = st.select_slider("Please Select Event", options=slider)

    # Add text
    if new==slider[0]:
        #EU Referendum
        fig.add_annotation(
                x='2016-06-23',
                y=290,
                xref="x",
                yref="y",
                text="EU Referendum",showarrow=True, arrowhead=3,arrowcolor="red",
                font=dict(
                    size=14,
                    color="black"
                    ),
            ax=20,
                ay=-30,
                borderwidth=2,
                borderpad=4,
                bgcolor="white",
                opacity=0.8)

    if new==slider[1]:
        #Manchester Bombing
        fig.add_annotation(
                x='2017-05-22',
                y=300,
                xref="x",
                yref="y",
                text="Manchester Arena attacks",showarrow=True, arrowhead=3,arrowcolor="red",
                font=dict(
                    size=14,
                    color="black"
                    ),
            ax=20,
                ay=-30,
                borderwidth=2,
                borderpad=4,
                bgcolor="white",
                opacity=0.8)

    if new==slider[2]:
        #Bank Robbers
        fig.add_annotation(
                x='2018-08-06',
                y=330,
                xref="x",
                yref="y",
                text="Muslim women as 'bank robbers' article",showarrow=True, arrowhead=3,arrowcolor="red",
                font=dict(
                    size=14,
                    color="black"
                    ),
            ax=20,
                ay=-30,
                borderwidth=2,
                borderpad=4,
                bgcolor="white",
                opacity=0.8)

    if new==slider[3]:
        #Chimpanzee
        fig.add_annotation(
                x='2019-05-9',
                y=310,
                xref="x",
                yref="y",
                text="Royal baby as 'chimpanzee'", showarrow=True, arrowhead=1,arrowsize=1,
                arrowwidth=1,
                font=dict(
                    size=14,
                    color="black"
                    ),
                ax=20,
                ay=-30,
                borderwidth=2,
                borderpad=4,
                bgcolor="white",
                opacity=0.8, arrowcolor="red",)

    if new==slider[4]:
        #BLM
        fig.add_annotation(
                x='2020-05-28',
                y=325,
                xref="x",
                yref="y",
                text="Black Lives Matter protests",showarrow=True, arrowhead=3,arrowcolor="red",
                font=dict(
                    size=14,
                    color="black"
                    ),
            ax=20,
                ay=-30,
                borderwidth=2,
                borderpad=4,
                bgcolor="white",
                opacity=0.8

        )


    fig.update_layout(
        title={
        'text': "Racially or Religiously Aggravated Offences, England and Wales, 2015-2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, xaxis_title="Year", yaxis_title="Offences")

    st.plotly_chart(fig, use_container_width=True)



    #Wordclouds
    if new==slider[0]:
        st.subheader('Search Term: European')
        image = Image.open('data/european.png')
        st.image(image, use_column_width=True)

    elif new==slider[1]:
        st.subheader('Search Term: Manchester')
        image = Image.open('data/Manchester.png')
        st.image(image, use_column_width=True)

    elif new==slider[2]:
        st.subheader('Search Term: Muslim')
        image = Image.open('data/Muslim.png')
        st.image(image, use_column_width=True)

    elif new==slider[3]:
        st.subheader('Search Term: Black')
        image = Image.open('data/Black.png')
        st.image(image, use_column_width=True)

    elif new==slider[4]:
        st.subheader('Search Term: BLM (Black Lives Matter)')
        image = Image.open('data/BLM.png')
        st.image(image, use_column_width=True)



if selected == "Interpretation":
    st.markdown('<p class="header">Interpretation</p>',unsafe_allow_html=True)
    st.markdown('''
                The ring-wing publications analysed:
                - Produce headlines that refer to migrants and asylum seekers in semantically similar ways.
                - Refer to migrants, refugees and asylum seekers with language that have a semantic association to criminal activities. This association is particularly strong between 2014 and 2018.
                - Portrayed the identity of migrants, refugees and asylum seekers as almost exclusively Muslim between 2014 and 2018.
                - From 2018 onwards, softened the language on migrants, with more emotive words semantically associated to headlines.
                - Produce headlines on immigrants and minority groups where the primary emotions are anger and sadness. The sentiment of the headlines were overhwleming negative or neutral.
                ''')
