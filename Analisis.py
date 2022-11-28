import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


questions = [
    'Campañas con mayor impacto a lo largo del año',
    'La relación entre el tipo de post y su alcance al pagar en Facebook',
    'Campañas que más atraen a usuarios nuevos',
    'Campañas que más generan interacciones entre los usuarios',
    'Evolución en el tiempo de las interacciones',
    'Conclusiones claves'
]

#PROJECT CONFIG
st.set_page_config(
    page_title='Estudio campañas de marketing'
)


#LOAD DATASET
df = pd.read_csv('newFacebookDataset.csv')

st.sidebar.info('Menú de navegación')

a, b = st.columns([2, 10])

with a:
    st.text("")
    st.image("logo.jpeg")
with b:
    st.title("Análisis")


idx = 0
st.subheader(questions[idx])
st.write('Campañas por tipo y categoría de post')
varToSum = 'Lifetime Engaged Users'
dfByCategoryAndType = df.groupby(['Type','CategoryType'])[varToSum].sum().reset_index()
plt.figure(figsize=(16,8))
fig, ax = plt.subplots()
sns.barplot(dfByCategoryAndType, x='Lifetime Engaged Users', y='Type', hue='CategoryType', ax=ax, palette='mako')
st.pyplot(fig)

st.write('insight')


###### NEW SECTION
idx += 1
st.subheader(questions[idx])
dfByPaidCampaign = df.groupby(['Paid'])[varToSum].sum().reset_index()

dfByPaidCampaignAndType = df.groupby(['Paid', 'Type'])[varToSum].sum().reset_index()
dfByPaidCampaignAndTypeCount = df.groupby(['Paid', 'Type'])[varToSum].count().reset_index()
dfByPaidCampaignAndTypeCount['Count'] = dfByPaidCampaignAndTypeCount[varToSum]
del dfByPaidCampaignAndTypeCount[varToSum]

dfByPaidCampaignAndType = pd.merge(dfByPaidCampaignAndType, dfByPaidCampaignAndTypeCount, how='left', left_on=['Paid', 'Type'], right_on=['Paid', 'Type'])
dfByPaidCampaignAndType['UsersPerPost'] = dfByPaidCampaignAndType[varToSum] / dfByPaidCampaignAndType.Count

plt.figure(figsize=(16,8))
fig, ax = plt.subplots()
sns.barplot(dfByPaidCampaignAndType, x='UsersPerPost', y='Type', hue='Paid', ax=ax, palette='mako')
st.pyplot(fig)

st.write('insight')

plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
ax = sns.scatterplot(data = dfByPaidCampaignAndType, x = 'UsersPerPost', y = 'Count', hue='Type', palette='mako')
for i in range(dfByPaidCampaignAndType.shape[0]):
    ax.text(dfByPaidCampaignAndType.UsersPerPost.iloc[i], dfByPaidCampaignAndType.Count.iloc[i], dfByPaidCampaignAndType.Paid.iloc[i], horizontalalignment='left', size='small', color='black', weight='semibold')
st.pyplot(fig)

st.write('insight')

####### new section
idx += 1
st.subheader(questions[idx])
varToExplore = 'Lifetime People who have liked your Page and engaged with your post'
grouping = ['Paid', 'Type', 'CategoryType']

dfByInteractionsNewPeople = df.groupby(grouping)[varToExplore].sum().reset_index()
dfByInteractionsNewPeopleCount = df.groupby(grouping)[varToExplore].count().reset_index()

dfByInteractionsNewPeopleCount['Count'] = dfByInteractionsNewPeopleCount[varToExplore]
del dfByInteractionsNewPeopleCount[varToExplore]

dfByInteractionsNewPeople = pd.merge(dfByInteractionsNewPeople, dfByInteractionsNewPeopleCount, how='left', left_on=['Paid', 'Type', 'CategoryType'], right_on=['Paid', 'Type', 'CategoryType'])


dfByInteractionsNewPeople['UsersPerPost'] = dfByInteractionsNewPeople[varToExplore] / dfByInteractionsNewPeople.Count
dfByInteractionsNewPeople.sort_values('UsersPerPost')


plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
ax = sns.barplot(dfByInteractionsNewPeople, x='UsersPerPost', y='Type', hue='CategoryType', ci=None, palette='mako')
st.pyplot(fig)

st.write('insight')

####### new section
idx += 1
st.subheader(questions[idx])
##
varToExplore = 'Lifetime Post reach by people who like your Page'
grouping = ['Paid', 'Type', 'CategoryType']

dfByInteractionsNewPeople = df.groupby(grouping)[varToExplore].sum().reset_index()
dfByInteractionsNewPeopleCount = df.groupby(grouping)[varToExplore].count().reset_index()

dfByInteractionsNewPeopleCount['Count'] = dfByInteractionsNewPeopleCount[varToExplore]
del dfByInteractionsNewPeopleCount[varToExplore]

dfByInteractionsNewPeople = pd.merge(dfByInteractionsNewPeople, dfByInteractionsNewPeopleCount, how='left', left_on=['Paid', 'Type', 'CategoryType'], right_on=['Paid', 'Type', 'CategoryType'])


dfByInteractionsNewPeople['UsersPerPost'] = dfByInteractionsNewPeople[varToExplore] / dfByInteractionsNewPeople.Count

plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
ax = sns.barplot(dfByInteractionsNewPeople, x='UsersPerPost', y='Type', hue='CategoryType', ci=None, palette='mako')
st.pyplot(fig)
st.write('insight')

####### new section
idx += 1
st.subheader(questions[idx])
varToExplore = 'Page total likes'
grouping = ['Post Month','Month', 'Paid']

dfByTimePaidVsFree = df.groupby(grouping)[varToExplore].count().reset_index()
dfByTimePaidVsFree['Count'] = dfByTimePaidVsFree[varToExplore]
del dfByTimePaidVsFree[varToExplore]

dfByTimePaidVsFreeMax = df.groupby(grouping)[varToExplore].max().reset_index()

dfByTimePaidVsFree = pd.merge(dfByTimePaidVsFree, dfByTimePaidVsFreeMax, how='left', left_on=grouping, right_on=grouping)


yField ='Page total likes'

fig, ax1 = plt.subplots(figsize=(12,8))
sns.lineplot(data=dfByTimePaidVsFree, x='Month', y=yField, ax= ax1, marker='o', palette='mako')
ax2 = ax1.twinx()
sns.barplot(dfByTimePaidVsFree, x='Month', y='Count', hue='Paid', alpha=0.6, palette='mako')
st.pyplot(fig)

dfByType = df[df['Post Month'] < 13]
grouping = ['Post Month', 'Month', 'Type']
varToExplore = 'like'
dfByType = dfByType.groupby(grouping)[varToExplore].count().reset_index()
dfByType = dfByType.rename(columns={'like': 'Count'})

fig, ax1 = plt.subplots()
plt.figure(figsize=(12,8))
sns.barplot(data=dfByType, x = 'Month', y='Count', hue='Type', ax=ax1, palette='mako')
st.pyplot(fig)

st.write('insight')

####### new section
idx += 1
st.subheader(questions[idx])
