import streamlit as st
import streamlit_wordcloud as wordcloud
from PIL import Image
import pandas as pd
import emoji
import plotly.express as px
import plotly.graph_objects as go
#from Muslim_Plotly import muslim_fig_1

st.set_page_config(layout="wide")


def page2():
    st.markdown('1. Background')
    st.sidebar.markdown('Page 1')
    st.header("Background")
    st.subheader("Text on the Motivation for the Project")
    st.write('''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, (...)
    ''')


def page3():
    st.markdown('2. Overall Perceptions of Foreigners')
    st.sidebar.markdown('Page 2')
    st.header("Perceptions of Immigrants in the Press")
    options = ["2008-2014", "2014-2017", "2017-2018", "2018-2020", "2020-2022"]
    new = st.select_slider("Please Select Year Range", options=options)
    option = st.selectbox('Which type of foreign persons?',('Please Select', 'Asylum', 'Migrant', 'Refugee'))

    if new=="2008-2014":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_1.png')
            st.image(image, use_column_width=True)
        if option=='Asylum':
            st.subheader('Search Term: Asylum')
            image = Image.open('data/asylum_1.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_1.png')
            st.image(image, use_column_width=True)
        if option=='Please Select':
            st.write('Please Select a Foreign Type :pray:')


    elif new=="2014-2017":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_2.png')
            st.image(image, use_column_width=True)
        if option=='Asylum':
            st.subheader('Search Term: Asylum')
            image = Image.open('data/asylum_2.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_2.png')
            st.image(image, use_column_width=True)
        if option=='Please Select':
            st.write('Please Select a Foreign Type :pray:')


    elif new=="2017-2018":
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_3.png')
            st.image(image, use_column_width=True)
        if option=='Asylum':
            st.subheader('Search Term: Asylum')
            image = Image.open('data/asylum_3.png')
            st.image(image, use_column_width=True)
        if option=='Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_3.png')
            st.image(image, use_column_width=True)
        if option=='Please Select':
            st.write('Please Select a Foreign Type :pray:')

    elif new=='2018-2020':
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_4.png')
            st.image(image, use_column_width=True)

        if option== 'Asylum':
            st.subheader('Search Term: Asylum')
            image = Image.open('data/asylum_4.png')
            st.image(image, use_column_width=True)

        if option== 'Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_4.png')
            st.image(image, caption='Refugee 5', use_column_width=True)

        if option=='Please Select':
            st.write('Please Select a Foreign Type :pray:')

    elif new=='2020-2022':
        if option=='Migrant':
            st.subheader('Search Term: Migrant')
            image = Image.open('data/migrant_5.png')
            st.image(image, use_column_width=True)

        if option== 'Asylum':
            st.subheader('Search Term: Asylum')
            image = Image.open('data/asylum_5.png')
            st.image(image, use_column_width=True)

        if option== 'Refugee':
            st.subheader('Search Term: Refugee')
            image = Image.open('data/refugee_5.png')
            st.image(image, use_column_width=True)

        if option=='Please Select':
            st.write('Please Select a Foreign Type :pray:')



    st.subheader("Interpretation Text Here")
    st.write('''Interpretation Text Here!''')







def page4():
    st.markdown('3. Perceptions Across Minority Groups')
    st.sidebar.markdown('Page 3')
    st.header("Perceptions Across Minority Groups")
    option = st.selectbox('Which minority group would you like to see?',('Ukraine', 'Syria', 'Muslim'))
    slider = ["2008-2014", "2014-2017", "2017-2018", "2018-2020", "2020-2022"]
    new = st.select_slider("Please Select Year Range", options=slider)


    if option=='Ukraine':
        st.subheader('Search Term: Ukraine')
        image = Image.open('data/Ukraine.png')
        st.image(image, use_column_width=True)

    if new=="2008-2014":
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

    elif new=="2020-2022":
        if option=='Muslim':
            st.subheader('Search Term: Muslim')
            image3 = Image.open('data/muslim_5.png')
            st.image(image3, use_column_width=True)


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
            fig_3.update_layout(showlegend=True,legend_title='Emotion')
            fig_3.update_xaxes(title='Year' )
            fig_3.update_yaxes( title='Number of tweets' )


        if option=='Ukraine':
            fig_3 = px.bar(data_3, x = 'Date', y='Optimism', title='Optimism Scores of Tweets Over Time',color_discrete_sequence=["green"])
            fig_3.update_layout(showlegend=False)
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

        if option=='Syria':
            fig_4 = px.scatter(data_4, x="Date", y="Newspaper", color="Emotion",
                               hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["red", "yellow", "blue", "green"],
                               title = 'Tweets by Paper, Date, Emotion and Like Count')

        if option=='Ukraine':
            fig_4 = px.scatter(data_3, x="Date", y="Newspaper", color="Emotion",
            hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["red", "yellow", "blue", "green"],
            title = 'Tweets by Paper, Date, Emotion and Like Count')

        st.plotly_chart(fig_4, use_container_width=True)

        st.subheader("Interpretation Text Here")
        st.write('''Interpretation Text Here!''')

    with col2:


            # 1: Sentiment Across Newspapers Over Time, 2011-2022

            if option=='Muslim' or option=='Syria':

                fig_1 = px.bar(data_1, y="Newspaper", x=['Positive','Neutral','Negative'], title="Sentiment Across Newspapers Over Time, 2011-2022", orientation='h', color_discrete_sequence=["green", "grey", "red"], animation_frame='year')
                fig_1.update_xaxes(showticklabels=False, title=None )
                fig_1.update_yaxes( title=None )
                fig_1.update_layout(legend_title='Sentiment')

            if option=='Ukraine':
                fig_1 = px.bar(data_2, y="Newspaper", x=['Positive','Neutral','Negative'], title="Sentiment across Newspapers, Jan'22 - Jun'22",
                            color_discrete_sequence=["green", "grey", "red"],orientation='h')
                fig_1.update_xaxes(showticklabels=False, title=None )
                fig_1.update_yaxes( title=None )
                fig_1.update_layout(legend_title='Sentiment')

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
            fig_2.update_layout(legend_title='Newspaper', title='Average Emotion Across Newspapers, 2008-2022')
            st.plotly_chart(fig_2, use_container_width=True)



def page5():
    st.markdown('4. Hate Crime and Socio-Economic Events')
    st.sidebar.markdown('Page 4')
    slider = ["2008-2014", "2014-2017", "2017-2018", "2018-2020", "2020-2022"]
    new = st.select_slider("Please Select Year Range", options=slider)
    crime = pd.read_csv("data/hate_crime.csv",engine='python')
    # Create figure
    fig = go.Figure()

    # Add hate crime
    fig.add_trace(go.Scatter(x=crime['Date'], y=crime['Total offences'], name='Hate Crime'))

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

    if new==slider[3]:
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
        'text': "Racially or Religiously Aggravated Offences, England and Wales",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, xaxis_title="Year", yaxis_title="Offences")

    st.plotly_chart(fig, use_container_width=True)

    #Wordclouds
    if new=="2008-2014":
        image = Image.open('data/european.png')
        st.image(image, use_column_width=True)

    elif new=="2014-2017":
        image = Image.open('data/Manchester.png')
        st.image(image, use_column_width=True)

    elif new=="2017-2018":
        image = Image.open('data/Muslim.png')
        st.image(image, use_column_width=True)

    elif new=="2018-2020":
        image = Image.open('data/Black.png')
        st.image(image, use_column_width=True)

    elif new=="2020-2022":
        image = Image.open('data/BLM.png')
        st.image(image, use_column_width=True)



page_names_to_funcs = {
    "Background": page2,
    "Overall Perception of Immigrants": page3,
    "Perceptions Across Minority Groups": page4,
    "Relationship with Hate Crime & Key Socio-economic Events": page5}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
