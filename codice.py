# Presentazione Iniziale
'''
Nel presente progetto, ho analizzato un dataset contenente circa 130.000 recensioni di vini. L'obiettivo è sviluppare una strategia per un marketplace che colleghi piccoli produttori locali con acquirenti globali, 
mettendo in risalto l'unicità e la qualità dei loro prodotti. L'analisi dei dati è stata suddivisa in varie fasi: pulizia e preparazione, esplorazione delle caratteristiche dei vini e delle cantine, e analisi delle 
relazioni tra punteggi e prezzi.
'''

import pandas as pd                 # Libreria per la gestione e manipolazione dei dati
import matplotlib.pyplot as plt     # Libreria per la creazione di grafici
import seaborn as sns               # Libreria per visualizzazioni avanzate basate su Matplotlib

# Funzione per aggiungere etichette in grassetto sui barplot (valori con una cifra decimale)
def grassetto(): 
    for p in ax.patches:                                              # Per ogni barra (patch) presente nel grafico (barplot)
        ax.annotate(f'{p.get_height():.2f}',                          # Aggiunge un'etichetta di testo con il valore dell'altezza della barra, formattato con due cifre decimali
                (p.get_x() + p.get_width() / 2., p.get_height()),     # Posiziona l'etichetta al centro orizzontale della barra (calcolando la metà della larghezza) e leggermente sopra l'altezza della barra
                ha='center', va='baseline',                           # Centra il testo orizzontalmente ('ha' = horizontal alignment) e lo allinea alla base della barra verticalmente ('va' = vertical alignment)
                fontsize=8, color='black', fontweight='bold')         # Definisce la dimensione del testo (8), il colore del testo (nero), e rende il testo in grassetto ('bold')

# Funzione per aggiungere etichette in grassetto sui barplot (valori interi)
def grassetto2():
  for p in ax.patches:                                                # Per ogni barra (patch) presente nel grafico (barplot)
    ax.annotate(f'{int(p.get_height())}',                             # Aggiunge un'etichetta di testo con il valore dell'altezza della barra, formattato con un numero intero
                (p.get_x() + p.get_width() / 2., p.get_height()),     # Posiziona l'etichetta al centro orizzontale della barra (calcolando la metà della larghezza) e leggermente sopra l'altezza della barra
                ha='center', va='baseline',                           # Centra il testo orizzontalmente ('ha' = horizontal alignment) e lo allinea alla base della barra verticalmente ('va' = vertical alignment)
                fontsize=8, color='black', fontweight='bold')         # Definisce la dimensione del testo (8), il colore del testo (nero), e rende il testo in grassetto ('bold')

# Funzione per aggiungere etichette in grassetto sui barplot orizzontali
def grassetto_Oriz():
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.2f}', (p.get_width() + 1, p.get_y() + p.get_height() / 2), 
                    ha='center', va='center', color='black', fontsize=12, fontweight='bold')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lettura del dataset di recensioni sui vini
df = pd.read_csv(r'C:\Users\alessandro\Desktop\file famiglia\Alessandro\Corso Start2Impact\06 - Data Manipulation and Visualization V\winemag-data-130k-v2.csv')

# Pulizia dei dati: rimozione dei duplicati e dei valori nulli per le colonne essenziali ('price', 'points', 'variety', 'country')
df_clean = df.drop_duplicates().dropna(subset=['price', 'points', 'variety', 'country'])

# Statistiche descrittive per i prezzi dei vini
price_mean = round(df_clean['price'].mean(), 2)                     # Media dei prezzi
price_median = round(df_clean['price'].median(), 2)                 # Mediana dei prezzi
price_var = round(df_clean['price'].var(), 2)                       # Varianza dei prezzi

# Statistiche descrittive per i punteggi dei vini
points_mean = round(df_clean['points'].mean(), 2)                   # Media dei punteggi
points_median = round(df_clean['points'].median(), 2)               # Mediana dei punteggi
points_var = round(df_clean['points'].var(), 2)                     # Varianza dei punteggi 

# Storytelling sulle statistiche di base
print(f"Prezzo medio dei vini: {price_mean:.2f}$, con una mediana di {price_median:.2f}$. "
      f"La varianza ci mostra una certa variabilità nei prezzi, suggerendo la presenza di vini sia molto economici che di alta fascia.\n"
      f"Il punteggio medio assegnato ai vini è {points_mean:.2f}, con una mediana di {points_median:.2f}. "
      f"Anche qui, la varianza riflette che ci sono vini con punteggi eccezionali, ma anche alcuni con valutazioni più basse.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling basato sull'immagine dei prezzi medi dei vini per paese
print("\n Prezzo Medio dei Vini per Paese \n"
      "Nel grafico dei prezzi medi dei vini per paese, possiamo notare una significativa variabilità tra le nazioni.\n"
      "\n1. Paesi con i prezzi più elevati:\n"
      "Il paese che si distingue maggiormente è la Svizzera, con un prezzo medio per bottiglia di vino che arriva a 85.29$. "
      "Questo valore è sorprendentemente alto rispetto a tutti gli altri paesi, suggerendo che in Svizzera il mercato del vino "
      "è dominato da bottiglie di alta fascia, probabilmente per via della qualità superiore, della produzione limitata o dei costi di importazione.\n"
      "Altri paesi con prezzi medi elevati includono Inghilterra (51.68$), Germania (42.26$) e Francia (41.14$), che riflettono "
      "la produzione di vini di alta qualità e la loro fama internazionale. \n"
      "\n2. Paesi con prezzi intermedi:\n"
      "Tra questi, troviamo paesi come l'Australia, l'Italia e gli Stati Uniti, con prezzi medi tra i 35$ e i 39$.\n"
      "Questi paesi offrono una grande varietà di vini, dai più economici a quelli di lusso.\n"
      "\n3. Paesi con prezzi più bassi:\n"
      "Dall'altra parte dello spettro, vediamo paesi come l'Ucraina, con un prezzo medio di 9.21$, seguita dalla Romania e la Slovacchia, con prezzi attorno ai 15-16$.\n"
      "Questi paesi producono vini accessibili, probabilmente destinati principalmente al consumo interno. Paesi emergenti come la Cina e l'India "
      "presentano anch'essi prezzi relativamente bassi, riflettendo mercati vinicoli in crescita.\n"
      "\n4. Paesi emergenti:\n"
      "Infine, mercati come il Libano (30.69$) e la Israele (31.77$) stanno iniziando a farsi notare sul mercato vinicolo internazionale."
      "I loro prezzi medi indicano un crescente interesse per i loro vini unici, con tradizioni vinicole che risalgono a secoli fa.\n")

# Visualizzazione: barplot del prezzo medio dei vini per paese 
plt.figure(figsize=(18, 7))                                                                                                # Imposta le dimensioni della figura
ax = sns.barplot(x='country', y='price', data=df_clean, estimator='mean', errorbar=None, hue='country', palette='pastel')  # Crea il barplot con prezzo medio per paese
plt.title('Prezzo Medio dei Vini per Paese')                                                                               # Titolo del grafico
plt.xticks(rotation=90)                                                                                                    # Ruota le etichette dell'asse X per una migliore leggibilità
plt.ylabel('Prezzo Medio ($)')                                                                                             # Etichetta asse Y
grassetto()                                                                                                                # Aggiunge etichette in grassetto con i valori sui barplot
plt.show()                                                                                                                 # Mostra il grafico

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling basato sull'immagine dei prezzi medi per le principali varietà di vino
print("\nPrezzo Medio dei Vini per le Principali Varietà\n"
      "Nel grafico, vengono visualizzati i prezzi medi per le dieci varietà di vino più comuni.\n"
      "\n1. Varietà con i prezzi più elevati:\n"
      "Le varietà di vino con i prezzi medi più alti includono il Pinot Noir (47.53$), il Cabernet Sauvignon (47.94$) e il Bordeaux-style Red Blend (47.21$).\n"
      "Questi risultati riflettono la domanda di vini premium associati a queste varietà, spesso legati a processi di produzione complessi o a regioni viticole di pregio.\n"
      "Queste varietà sono apprezzate a livello globale per la loro qualità e complessità, il che spiega i prezzi più elevati.\n"
      "\n2. Varietà con prezzi intermedi:\n"
      "Tra le varietà con prezzi intermedi troviamo il Red Blend (35.89$), il Syrah (39.14$) e lo Chardonnay (34.52$).\n"
      "Queste varietà sono molto diffuse, con ampie fasce di prezzo che vanno dai vini da tavola a quelli di alta qualità. Tuttavia, la loro versatilità e popolarità portano a una media di prezzo leggermente inferiore rispetto ai vini più pregiati.\n"
      "\n3. Varietà con prezzi più bassi:\n"
      "Infine, varietà come il Merlot (29.54$), il Sauvignon Blanc (20.23$) e il Rosé (18.51$) presentano prezzi medi più bassi.\n"
      "Il Rosé, in particolare, ha il prezzo medio più basso, probabilmente a causa della sua produzione più economica e del suo consumo spesso stagionale.\n"
      "Anche il Merlot, nonostante la sua popolarità, ha un prezzo medio inferiore rispetto a varietà più costose come il Pinot Noir e il Cabernet Sauvignon, riflettendo una maggiore disponibilità e accessibilità di questa varietà.\n")

# Visualizzazione: barplot orizzontale del prezzo medio per le principali varietà di vino
plt.figure(figsize=(10, 9))                                                                                                           # Imposta la dimensione del grafico
ax = sns.barplot(y='variety', x='price', data=df_clean[df_clean['variety'].isin(df_clean['variety'].value_counts().head(10).index)],
                  estimator='mean', errorbar=None, color='#FFCC80')                                                                   # Filtra le 10 varietà di vino più frequenti e crea un barplot per visualizzare il prezzo medio
plt.title('Prezzo Medio dei Vini per le Principali Varietà')                                                                          # Titolo del grafico
plt.xlabel('Prezzo Medio ($)')                                                                                                        # Etichetta dell'asse X
plt.ylabel('Varietà di Vino')                                                                                                         # Etichetta dell'asse Y
grassetto_Oriz()                                                                                                                      # Aggiunge etichette in grassetto con i valori sui barplot
plt.show()                                                                                                                            # Mostra il grafico

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Esplorazione delle varietà di vino più rappresentate nel dataset
top_varieties = df_clean['variety'].value_counts().head(10)                                                                # 'value_counts()' conta il numero di occorrenze di ciascuna varietà di vino nel dataset 'df_clean' e 'head(10)' restituisce le prime 10 varietà più comuni.
print("\nLe varietà di vino più rappresentate nel nostro campione sono:\n", top_varieties)                                 # Stampa il risultato delle 10 varietà di vino più rappresentate

# Storytelling sulle varietà di vino più rappresentate nel dataset
print("\nNotiamo che il Pinot Noir, con 12,785 referenze, è la varietà più rappresentata nel mercato, "
    "seguito da Chardonnay e Cabernet Sauvignon. La presenza predominante del Pinot Noir indica che questo vino "
    "è uno dei più richiesti dai consumatori, suggerendo una preferenza per prodotti di alta rotazione. "
    "Queste varietà offrono un'ampia gamma di prezzi e qualità, evidenziando la diversità delle scelte disponibili.")

# Visualizzazione: barplot per la frequenza delle varietà di vino più rappresentate 
plt.figure(figsize=(10, 6))                                                     # Imposta la dimensione della figura
ax = top_varieties.plot(kind='bar', color='skyblue')                            # Crea un grafico a barre per le varietà di vino più rappresentate
plt.title('Le 10 Varietà di Vino più Rappresentate')                            # Titolo del grafico
plt.xlabel('Varietà')                                                           # Etichetta dell'asse X
plt.ylabel('Numero di referenze')                                               # Etichetta dell'asse Y
plt.xticks(rotation=90)                                                         # Ruota le etichette dell'asse X
grassetto2()                                                                    # Aggiunge etichette in grassetto con valori numerici interi
plt.show()                                                                      # Mostra il grafico

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Esplorazione dei vini che sono outlier: quelli con prezzi superiori a 500$ o punteggi sopra i 98 punti
outlier_vini = df_clean[(df_clean['price'] > 500) | (df_clean['points'] > 98)]                                      # Viene creato un nuovo DataFrame 'outlier_vini' contenente solo le righe del dataset pulito in cui: - Il prezzo del vino ('price') è maggiore di 500$, oppure il punteggio del vino ('points') è maggiore di 98 mentre l'operatore | (OR) assicura che venga selezionata una riga se soddisfa almeno una delle due condizioni.
print("\nAnalizzando i vini considerati outlier, cioè quelli con prezzi sopra i 500$ o punteggi sopra i 98 punti, "
      "troviamo le seguenti etichette uniche:\n", outlier_vini[['title', 'variety', 'price', 'points']])            # Stampa un messaggio che spiega il contenuto dei vini filtrati, seguita dalla visualizzazione delle colonne 'title', 'variety', 'price', e 'points' del DataFrame filtrato

# Storytelling sugli outlier
print("\nQuesti vini fuori dal comune, con prezzi elevati o punteggi eccezionali, spesso rappresentano etichette di nicchia "
      "o riserve speciali, che potrebbero attirare collezionisti e intenditori. Mantenere referenze di questo tipo potrebbe "
      "valorizzare l'offerta di un marketplace, rendendolo più esclusivo.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Distribuzione dei vini per country (primi 10 paesi)
country_distribution = df_clean['country'].value_counts().head(10)    # Colonna del DataFrame pulito ('df_clean') che indica il paese di origine dei vini 'value_counts()': Conta quante volte ciascun paese compare nella colonna 'country', ovvero quanti vini provengono da ciascun paese, infine seleziona i primi 10 paesi con il maggior numero di vini (in ordine decrescente).
print("\nDistribuzione dei vini per paese:\n", country_distribution)  # Stampa un messaggio che introduce la distribuzione dei vini per paese.

# Storytelling sulla distribuzione dei vini per country
print("\nIl grafico illustra la distribuzione dei vini per paese, con il numero di referenze per ciascuno.\n "
    "Gli Stati Uniti dominano la scena con 54.265 referenze, distaccandosi nettamente dagli altri paesi.\n "
    "La Francia e l'Italia seguono rispettivamente con 17.776 e 16.914 referenze, sottolineando la loro fama mondiale nel settore vinicolo.\n "
    "La Spagna si piazza al quarto posto con 6.573 referenze, mentre il Portogallo ne conta 4.875.\n "
    "Altri paesi produttori come il Cile, l'Argentina, l'Austria, l'Australia e la Germania registrano un numero inferiore di referenze, rispettivamente con 4.415, 3.756, 2.799, 2.294 e 2.120.\n"
    "Il grafico evidenzia chiaramente il predominio degli Stati Uniti nel mercato, seguiti dai tradizionali paesi europei noti per la produzione vinicola.\n" )

#= Visualizzazione: barplot per la distribuzione dei vini per paese 
plt.figure(figsize=(10, 6))                                     # Imposta la dimensione del grafico
ax= country_distribution.plot(kind='bar', color='lightgreen')   # Crea un barplot per la distribuzione dei vini per paese
plt.title('Distribuzione dei Vini per Paese')                   # Titolo del grafico
plt.xlabel('Paese')                                             # Etichetta dell'asse X
plt.ylabel('Numero di referenze')                               # Etichetta dell'asse Y
plt.xticks(rotation=90)                                         # Ruota le etichette dell'asse X
grassetto2()                                                    # Aggiunge etichette in grassetto con i valori
plt.show()                                                      # Mostra il grafico

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling sulla Heatmap di correlazione tra prezzo e punteggio
print ("\nCorrelazione tra Punteggio e Prezzo (0.42) \n"
        "Questo valore è situato nella parte superiore destra della heatmap ed "
        "indica una correlazione positiva moderata tra il punteggio e il prezzo. Ciò significa che, in generale, vini con punteggi più elevati tendono ad avere un prezzo maggiore. Tuttavia, non è una correlazione forte, " 
        "il che suggerisce che ci sono altri fattori che influenzano il prezzo oltre al punteggio, ovvero la presenza di vini con punteggi alti ma prezzi bassi.\n"
        "\nCorrelazione tra Prezzo e Prezzo (1):\n"
        "Questa è una correlazione perfetta, come ci si aspetterebbe, dato che stiamo confrontando la variabile con se stessa. È indicata nella parte diagonale dell'heatmap e serve principalmente come punto di riferimento. \n" 
        "\nCorrelazione tra Punteggio e Punteggio (1):\n"
        "Analogamente, questa è una correlazione perfetta, indicata nella parte diagonale opposta. Anche in questo caso, è il risultato atteso. \n"
        "\nCorrelazione tra Price e Points (0.42):\n"
        "Questo valore è situato nella parte inferiore sinistra della heatmap ed è una rappresentazione simmetrica della correlazione tra punteggio e prezzo, confermando i risultati precedenti. ")

# Heatmap di correlazione tra prezzo e punteggio
plt.figure(figsize=(10, 6))                                                   # Crea una nuova figura con dimensioni 10x6 pollici per la heatmap
correlation_matrix = df_clean[['price', 'points']].corr()                     # Calcola la matrice di correlazione tra 'price' e 'points'
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)  # Genera una heatmap utilizzando la matrice di correlazione - 'annot=True': Visualizza i valori numerici delle correlazioni all'interno della heatmap - 'cmap="coolwarm"': Utilizza la mappa di colori "coolwarm" per distinguere visivamente le correlazioni - 'linewidths=0.5': Definisce lo spessore delle linee che separano le celle della heatmap
plt.title('Heatmap di correlazione tra prezzo e punteggio')                   # Aggiunge il titolo alla heatmap
plt.show()                                                                    # Mostra la heatmap

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling sul Plot per la distribuzione del prezzo del vino
print ( "\nLa distribuzione dei prezzi dei vini mostra una chiara distribuzione asimmetrica positiva. La maggior parte dei vini si trova nella fascia di prezzo bassa, al di sotto dei 100$, con una "
        "concentrazione molto alta in questa gamma.\n"
        "\n- Osservazioni principali: \n La coda lunga a destra indica la presenza di vini che hanno prezzi molto più alti, probabilmente etichette premium o di nicchia, ma sono una parte estremamente ridotta del dataset."
        " Questi valori sono considerati outlier rispetto alla maggior parte dei dati.\n"
        "\n- Mediana vs Media: In un contesto come questo, la mediana è più indicativa della centralità del prezzo rispetto alla media. Infatti, poiché la media è influenzata dagli outlier (i vini molto costosi), essa" 
        "potrebbe risultare più alta della mediana, distorcendo così l'interpretazione del prezzo tipico.\n"
        "\n- Conclusione: Il mercato del vino sembra dominato da vini di fascia medio-bassa. L'analisi dei vini di fascia alta potrebbe richiedere un approfondimento separato, poiché potrebbero essere prodotti "
        "destinati a un pubblico specifico.")

# Plot per la distribuzione del prezzo del vino
plt.figure(figsize=(10, 6))                                 # Crea una nuova figura con dimensioni 10x6 pollici per il grafico della distribuzione del prezzo
sns.histplot(df_clean['price'], bins=50, kde=True)          # Crea un istogramma della distribuzione del prezzo - 'bins=50': Definisce il numero di bin (intervalli) nell'istogramma - 'kde=True': Aggiunge una linea di densità kernel (Kernel Density Estimation) per una rappresentazione più fluida della distribuzione
plt.title('Distribuzione del prezzo del vino')              # Aggiunge il titolo al grafico
plt.xlabel('Prezzo ($)')                                    # Etichetta per l'asse X (Prezzo in dollari)
plt.ylabel('Frequenza')                                     # Etichetta per l'asse Y (Frequenza dei prezzi)
plt.show()                                                  # Mostra il grafico dell'istogramma

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling sul Plot per la distribuzione dei punteggi dei vini
print ( "\nLa distribuzione dei punteggi dei vini, segue una distribuzione quasi normale con un leggero spostamento verso destra.\n"
        "- Osservazioni principali: \n La maggior parte dei vini ha un punteggio tra 85 e 92, con un picco visibile attorno a 88. Questa distribuzione suggerisce che la maggior parte dei vini recensiti ha una qualità "
        "che rientra nella fascia medio-alta. I vini con punteggi estremamente bassi (< 85) o estremamente alti (> 95) sono relativamente rari.\n"
        "- Conclusioni: \n La concentrazione dei vini nella fascia tra 85 e 92 indica che il mercato tende a recensire vini di una certa qualità standard. Tuttavia, sarebbe utile esplorare in che modo il punteggio "
        " incide sul prezzo e se ci sono correlazioni tra punteggio e le varietà o le regioni di produzione.\n")

# Plot per la distribuzione dei punteggi dei vini
plt.figure(figsize=(10, 6))                                   # Crea una nuova figura con dimensioni 10x6 pollici per il grafico della distribuzione dei punteggi
ax = sns.histplot(df_clean['points'], bins=50, kde=True)      # Crea un istogramma della distribuzione dei punteggi dei vini - 'bins=50': Definisce il numero di bin (intervalli) per il punteggio - 'kde=True': Aggiunge una linea di densità kernel per rappresentare in modo fluido la distribuzione dei punteggi
plt.title('Distribuzione dei punteggi dei vini')              # Aggiunge il titolo al grafico
plt.xlabel('Punteggio')                                       # Etichetta per l'asse X (Punteggio)
plt.ylabel('Frequenza')                                       # Etichetta per l'asse Y (Frequenza dei punteggi)
plt.show()                                                    # Mostra il grafico dell'istogramma

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Storytelling sul Boxplot con overlay di punti per i punteggi dei vini per paese
print(
    "\nIl grafico boxplot rappresenta la distribuzione dei punteggi dei vini per paese, con un overlay di punti che mostra i dati effettivi.\n "
    "Ogni boxplot indica la distribuzione del punteggio dei vini per ciascun paese, evidenziando la mediana, l'intervallo interquartile e gli eventuali outlier.\n "
    "Si osserva una notevole variabilità nei punteggi tra i diversi paesi. Ad esempio, i vini di paesi come il Portogallo, la Francia, l'Italia e gli Stati Uniti tendono a mostrare punteggi medi elevati, con valori che raggiungono spesso i 95 punti o più. \n "
    "Paesi come la Svizzera, il Libano, e il Brasile mostrano boxplot con punteggi medi più bassi e un intervallo più ampio, indicando una maggiore variabilità nella qualità dei vini prodotti. \n"
    "L'overlay di punti neri sovrapposti ai boxplot aiuta a visualizzare la distribuzione reale dei punteggi, rendendo evidente che alcuni paesi, come il Cile e la Spagna, presentano punteggi che si concentrano in una gamma specifica, mentre altri paesi come la Georgia o l'India mostrano una dispersione più ampia. \n")

# Boxplot con overlay di punti per i punteggi dei vini per paese
plt.figure(figsize=(14, 7))                                                               # Crea una nuova figura con dimensioni 14x7 pollici per il boxplot
sns.boxplot(x='country', y='points', data=df_clean, showfliers=False)                     # Crea un boxplot per visualizzare la distribuzione dei punteggi per paese - 'x="country"': Assegna l'asse X ai paesi (variabile 'country') - 'y="points"': Assegna l'asse Y ai punteggi (variabile 'points') - 'showfliers=False': Nasconde i punti outlier per evitare che dominino la visualizzazione
sns.stripplot(x='country', y='points', data=df_clean, color='black', alpha=0.5, size=3)   # Aggiunge i punti reali dei punteggi sopra il boxplot - 'color="black"': Imposta il colore dei punti in nero - 'alpha=0.5': Imposta la trasparenza dei punti per migliorare la visibilità - 'size=3': Imposta la dimensione dei punti a 3
plt.title('Distribuzione dei Punteggi dei Vini per Paese con Overlay di Punti')           # Aggiunge il titolo al grafico
plt.xticks(rotation=90)                                                                   # Ruota le etichette sull'asse X di 45 gradi per renderle leggibili
plt.ylabel('Punteggio')                                                                   # Etichetta per l'asse Y (Punteggio)
plt.xlabel('Paese')                                                                       # Etichetta per l'asse X (Paese)
plt.show()                                                                                # Mostra il boxplot con i punti sovrapposti

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Conclusioni e Raccomandazioni per il Marketplace di Vini

'''

1. Posizionamento del Marketplace
        L'obiettivo del marketplace sarà quello di connettere piccoli produttori locali con acquirenti globali, enfatizzando l'unicità e la qualità dei loro vini. Dato l'interesse crescente per i vini artigianali e 
        biologici, il marketplace si posizionerà come una piattaforma che valorizza la storia e l'autenticità dietro ogni etichetta.
2. Varietà di Offerta
        L'analisi dei dati ha rivelato che il Pinot Noir, il Chardonnay e il Cabernet Sauvignon sono le varietà più rappresentate e richieste. Pertanto, il marketplace dovrebbe assicurarsi di avere una selezione 
        equilibrata di queste varietà, insieme a vini di nicchia provenienti da regioni meno note, come il Portogallo, per attrarre intenditori e collezionisti.
3. Strategia di Prezzo
        La maggior parte dei vini si colloca nella fascia di prezzo medio-bassa, con una concentrazione significativa al di sotto dei 100$. Si raccomanda di:
        Stabilire diverse fasce di prezzo: Offrire vini a prezzi accessibili accanto a opzioni premium per attrarre un pubblico più ampio.
        Evidenziare i vini outlier: I vini con punteggi elevati o prezzi sopra i 500$ dovrebbero essere ben pubblicizzati come prodotti esclusivi, in grado di attirare collezionisti e intenditori.
4. Analisi del Mercato
        L'analisi ha mostrato una correlazione positiva tra prezzo e punteggio (0.42). Questo suggerisce che i vini di alta qualità tendono ad avere prezzi superiori, ma non è sempre garantito. Pertanto:
        Educazione del cliente: Creare contenuti che aiutino gli acquirenti a comprendere il valore dei vini, inclusi fattori come la varietà, la regione, e le pratiche di produzione.
        Recensioni e valutazioni: Includere recensioni dettagliate da esperti e utenti per rafforzare la fiducia del consumatore e migliorare l'esperienza d'acquisto.
5. Target di Clientela
        Focalizzarsi su diverse categorie di clienti:
            Appassionati di vino: Offrire vini di alta qualità e informazioni dettagliate sulle varietà e le pratiche di produzione.
            Collezionisti:        Creare una sezione dedicata ai vini rari e costosi, con opzioni di acquisto limitate o esclusive.
            Nuovi acquirenti:     Fornire guide e consigli per i principianti, con sezioni di vini a prezzi accessibili e abbinamenti suggeriti.
6. Promozione e Marketing
        Utilizzare strategie di marketing mirate per attrarre diversi segmenti di clientela:
            Collaborazioni con influencer:  Coinvolgere esperti e appassionati di vino per promuovere il marketplace sui social media.
            Eventi di degustazione online:  Organizzare eventi virtuali per presentare vini selezionati e interagire direttamente con i clienti.
            Contenuti educativi:            Creare blog e video che esplorano le varietà di vino, le tecniche di degustazione e le tendenze del settore.
7. Analisi dei Dati
        Implementare strumenti di analisi per monitorare le vendite, le recensioni dei clienti e le tendenze del mercato:
            Raccolta di feedback:           Utilizzare sondaggi e recensioni per migliorare continuamente l'offerta e l'esperienza del cliente.
            Aggiornamenti dell'inventario:  Monitorare le vendite per adattare l'inventario in base alla domanda e alle tendenze emergenti.

Conclusione Finale
Un marketplace dedicato ai vini dovrebbe mirare a creare un ambiente dove i produttori locali possano mostrare la loro unicità e qualità, mentre gli acquirenti possono scoprire e apprezzare un'ampia gamma di vini. 
La chiave per il successo sarà un equilibrio tra varietà, prezzo, e promozione, supportato da un'analisi continua del mercato e delle preferenze dei consumatori. Con queste strategie, il marketplace non solo 
attrarrà clienti, ma contribuirà anche a valorizzare il patrimonio vitivinicolo locale.

'''
