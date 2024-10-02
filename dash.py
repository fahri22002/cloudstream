

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


payment_summary = pd.read_csv("payment_summary.csv")
state_income = pd.read_csv("state_income.csv")

st.header('Fahri Collection Dashboard :sparkles:')


col1, col2 = st.columns([3, 3])  

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
payment_summary.columns = ['payment_type', 'payment_value']

plt.figure(figsize=(14, 8))  

sns.barplot(
    y="payment_value", 
    x="payment_type",
    data=payment_summary,
    palette=colors
)
plt.title("Total Payment Value by Payment Type in BRL", loc="center", fontsize=20)  
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=16)  
plt.tick_params(axis='y', labelsize=16)  


st.pyplot(plt)  

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(40, 20))  

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
state_income.columns = ["customer_state", "payment_value"]
fz = 30
sns.barplot(x="payment_value", y="customer_state", data=state_income.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Revenue Performance by The Best States", loc="center", fontsize=fz*1.5)  
ax[0].tick_params(axis='y', labelsize=fz)  
ax[0].tick_params(axis='x', labelsize=fz)  

sns.barplot(x="payment_value", y="customer_state", data=state_income.sort_values(by="payment_value", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Revenue Performance by The Worst States", loc="center", fontsize=fz*1.5)  
ax[1].tick_params(axis='y', labelsize=fz)  
ax[1].tick_params(axis='x', labelsize=fz)  

plt.suptitle("Revenue Performance by The Best and Worst States in BRL", fontsize=fz*2)  


st.pyplot(fig)  
