a. Alla pressione del bottone “Crea Grafo” si crei un grafo semplice, pesato e non orientato i cui vertici siano 
tutti i geni essenziali (tabella genes, campo Essential).
b. Un arco collega due geni diversi solo se tale coppia (indipendentemente dall’ordine) appare nella tabella 
interactions. Si ignorino gli archi di tipo “cappio”, cioè le connessioni di un gene con se stesso.
c. Per definire il peso dell’arco si parta dalla correlazione fra i geni (tabella interactions, campo Expression_Corr) 
e si consideri il peso
• pari al valore assoluto di tale correlazione se i due geni non appartengono allo stesso cromosoma 
(campo Chromosome della tabella genes)
• pari al doppio del valore assoluto di tale correlazione se i due geni appartengono allo stesso cromosoma.
d. Permettere all’utente di selezionare dal menù a tendina uno dei geni (g) presenti nel grafo.
e. Alla pressione del bottone “Geni Adiacenti” stampare l’elenco dei geni adiacenti a quello selezionato ed il 
relativo peso, in ordine decrescente di peso.
