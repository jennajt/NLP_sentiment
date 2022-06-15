# imports
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Data
data_1 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Syria_data_1')
data_2 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Syria_data_2')
data_3 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Syria_data_3')
data_4 = pd.read_csv('/Users/jennatan/code/jennajt/NLP_sentiment/data/2_Syria_data_4')

# 1: Syria: Sentiment Across Newspapers Over Time, 2011-2022
def fig_1(data_1):
   fig = px.bar(data_1, y="Newspaper", x=['Positive','Neutral','Negative'],
                title="Sentiment Across Newspapers Over Time, 2011-2022",orientation='h',
                color_discrete_sequence=["green", "grey", "red"], animation_frame='year')
   fig.update_xaxes(showticklabels=False, title=None )
   fig.update_yaxes( title=None )
   fig.update_layout(legend_title='Sentiment')
   fig.show()

#2: Syria: Average Emotions Across Newspapers
def fig_2(data_2):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[data_2['Joy'].iloc[0], data_2['Optimism'].iloc[0],data_2['Anger'].iloc[0], data_2['Sadness'].iloc[0]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='Daily Express'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[data_2['Joy'].iloc[1], data_2['Optimism'].iloc[1],data_2['Anger'].iloc[1], data_2['Sadness'].iloc[1]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='Daily Mail'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[data_2['Joy'].iloc[2], data_2['Optimism'].iloc[2],data_2['Anger'].iloc[2], data_2['Sadness'].iloc[2]],
        theta=['Joy','Optimism','Anger','Sadness'],
        name='The Sun'
    ))

    fig.update_traces(fill='toself')
    fig.update_layout(legend_title='Newspaper', title='Average Emotion Across Newspapers, 2012-2022')
    fig.show()


#3 Sentiment of Tweets over Time
def fig_3(data_3):
    fig = px.line(data_3, x = 'Year', y=["Optimism", "Sadness", "Joy", "Anger"], title='Sentiment of Tweets Over Time, 2010-2022',
    color_discrete_sequence=["yellow", "blue", "green", "red"])
    fig.update_layout(xaxis_range=[2010,2022])
    fig.update_layout(showlegend=True,legend_title='Emotion')
    fig.update_xaxes(title='Year' )
    fig.update_yaxes( title='Number of tweets' )
    fig.show()

#4 Tweets by paper,date emotion and like count
def fig_4(data_4):
    fig = px.scatter(data_4, x="Date", y="Newspaper", color="Emotion",
                 hover_name="Tweet", size = "Like Count",size_max=100, color_discrete_sequence=["red", "yellow", "blue", "green"],
                 title = 'Tweets by Paper, Date, Emotion and Like Count'
                 )

    fig.show()

fig_1(data_1)
fig_2(data_2)
fig_3(data_3)
fig_4(data_4)
