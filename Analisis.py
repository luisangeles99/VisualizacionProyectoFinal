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
ax.set_xlabel('Total de usuarios únicos que dieron click al post')
ax.set_ylabel('Tipos')
st.pyplot(fig)

st.write('Gráfico general en que se puede observar la cantidad de usuarios que dan click y su tipo de publicación')
st.write('Resalta que para las fotos y el estado son dónde más clicks se dan, aunque esto se debe al volumen de este tipo de posts.')


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
ax.set_xlabel('Total de usuarios únicos que dieron click al post')
ax.set_ylabel('Tipos')
st.pyplot(fig)

st.write('Si observamos ahora el número usuarios que dan click por post nos damos cuenta que los mejores son estados y videos')
st.write('Se puede observar que pagar por publicidad en posts si potencia la cantidad de usuarios que dan click; expecto en links.')

plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
ax = sns.scatterplot(data = dfByPaidCampaignAndType, x = 'UsersPerPost', y = 'Count', hue='Type', palette='mako')
ax.set_xlabel('Total de usuarios únicos que dieron click al post')
ax.set_ylabel('Cantidad de posts')
for i in range(dfByPaidCampaignAndType.shape[0]):
    ax.text(dfByPaidCampaignAndType.UsersPerPost.iloc[i], dfByPaidCampaignAndType.Count.iloc[i], dfByPaidCampaignAndType.Paid.iloc[i], horizontalalignment='left', size='small', color='black', weight='semibold')

st.pyplot(fig)

st.write('Este gráfico muestra como en todos los tipos de posts se potencia la cantidad de clicks menos en links.')
st.write('La zona deseada es la mayor cantidad de usuarios dando click y menos posts, ubicada en la esquina inferior derecha.')

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
ax.set_xlabel('Total de usuarios únicos que ven el post y dan like a la página')
ax.set_ylabel('Tipos')
st.pyplot(fig)

st.write('Se puede observar que en la atracción, los estados y los videos son los que más personas nuevas atraen.')
st.write('Para estrategias de atracción lo mejor es publicar posts de este tipo')

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
ax.set_xlabel('Total de usuarios únicos que ven el post y ya tenían like')
ax.set_ylabel('Tipos')
st.pyplot(fig)
st.write('En este caso vemos como todos los tipos de posts aumentan, en especial los de links. A los usuarios les interesan más ya que ya conocen la marca.')
st.write('Los videos son los que más vistas reciben.')

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
ax1.set_xlabel('Meses')
ax1.set_ylabel('Cantidad de likes a fin de mes')
ax2 = ax1.twinx()

sns.barplot(dfByTimePaidVsFree, x='Month', y='Count', hue='Paid', alpha=0.6, palette='mako')
ax2.set_ylabel('Cantidad de posts en el mes')
st.pyplot(fig)

st.write('En el gráfico podemos observar la relación entre la cantidad de likes y la cantidad de posts por mes.')
st.write('Se nota que al aumentar los posts de paga la tendencia sube.')
st.write('De julio a agosto la tendencia disminuye su crecimiento y vemos como la cantidad de posts también.')

dfByType = df[df['Post Month'] < 13]
grouping = ['Post Month', 'Month', 'Type']
varToExplore = 'like'
dfByType = dfByType.groupby(grouping)[varToExplore].count().reset_index()
dfByType = dfByType.rename(columns={'like': 'Count'})

fig, ax1 = plt.subplots()
plt.figure(figsize=(12,8))
sns.barplot(data=dfByType, x = 'Month', y='Count', hue='Type', ax=ax1, palette='mako')
ax1.set_xlabel('Meses')
ax1.set_ylabel('Cantidad de posts')
st.pyplot(fig)

st.write('Se puede observar los videos y los estados disminuyeron, estos son los elementos que atraen a los nuevos clientes.')
st.write('Se confirma que los análisis anteriores son correctos.')

####### new section
idx += 1
st.subheader(questions[idx])
