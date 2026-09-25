import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv('../online_retail_germany.csv')
basket = (df.groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

basket_sets = basket.applymap(lambda x: 1 if x >= 1 else 0)
frequent_itemsets = apriori(basket_sets, min_support=0.06, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0)
print('--- Top 5 Association Rules (Germany Retail) ---')
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())