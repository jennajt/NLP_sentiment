# imports
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Data
data_1 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Ukr_data_1')
data_2 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Ukr_data_2')
data_3 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Ukr_data_3')
data_4 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Ukr_data_3') #same dataset as data_3

#1 Ukr: Average Emotions Across Newspapers
def fig_1(data_1):

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[data_1['Joy'].iloc[0], data_1['Optimism'].iloc[0],data_1['Anger'].iloc[0], data_1['Sadness'].iloc[0]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='Daily Express'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[data_1['Joy'].iloc[1], data_1['Optimism'].iloc[1],data_1['Anger'].iloc[1], data_1['Sadness'].iloc[1]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='Daily Mail'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[data_1['Joy'].iloc[2], data_1['Optimism'].iloc[2],data_1['Anger'].iloc[2], data_1['Sadness'].iloc[2]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='The Sun'
    ))
    fig.update_traces(fill='toself')
    fig.update_layout(legend_title='Newspaper', title="Average Emotion Across Newspapers, Jan'22 - Jun'22")
    fig.show()

# 2: Ukr: Sentiment Across Newspapers Over Time, 2011-2022
def fig_2(data_2):

    fig = px.bar(data_2, y="Newspaper", x=['Positive','Neutral','Negative'], title="Sentiment across Newspapers, Jan'22 - Jun'22",
                color_discrete_sequence=["green", "grey", "red"],orientation='h')
    fig.update_xaxes(showticklabels=False, title=None )
    fig.update_yaxes( title=None )
    fig.update_layout(legend_title='Sentiment')

    fig.show()

#3: Ukr: Tweets by paper, date, emotion and likes
def fig_3(data_3):
    fig = px.scatter(data_3, x="Date", y="Newspaper", color="Emotion",
                 hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["green", "red", "blue", "grey"],
                 title = 'Tweets by Paper, Date, Emotion and Like Count'
                 )

    fig.show()

#4 Optimism over time
def fig_4(data_4):
    fig = px.bar(data_4, x = 'Date', y='Optimism', title='Optimism Scores of Tweets Over Time',color_discrete_sequence=["green"])
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title='Date' )
    fig.update_yaxes( title='Optimism score' )
    fig.show()

fig_1(data_1)
fig_2(data_2)
fig_3(data_3)
fig_4(data_4)
