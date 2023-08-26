#importing libarires

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st 
#Diagnosing data 
dt=pd.read_csv("c:\Users\Assiu Tech\Desktop\streamlit\superstore_final_dataset (1).csv"encoding="latin-1")


df=dt[dt.Sales<14000]
df['Order_Date']=pd.to_datetime(df['Order_Date'])
df['Ship_Date']=pd.to_datetime(df['Ship_Date'])
 
date_city=df[['Order_Date','City']]
date_city=date_city.set_index("Order_Date")
date_city=date_city.City.resample(rule='1m').nunique()

df2_sales=df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)


date_customer=df[['Order_Date','Customer_ID']]
date_customer=date_customer.set_index("Order_Date")
date_customer=date_customer.Customer_ID.resample(rule='1m').nunique()

ship_sales=df.groupby('Ship_Mode')['Sales'].sum()

Segment_sales=df.groupby('Segment')['Sales'].sum()

Category_sales=df.groupby('Category')['Sales'].sum()

cust_sale=df.groupby("Customer_Name")['Sales'].sum().sort_values(ascending=False).head(10)


#Code

st.markdown('''
# **The EDA App**


**Credit:** App built  by [ziad ahmed](https://www.linkedin.com/in/ziad-ahmed-061828238/) 

---
''')
dt=pd.read_csv("d:\Data\datasets2\market sales\superstore_final_dataset (1).csv",encoding="latin-1")
st.title("Analyzig the data of  superstore sales in Usa 🛍️")
st.markdown(" Hey there welcome to the superstore sales analysis app. we will discover togher the time that sales increase in and the highest state and city sales, and  the increasing of customers over time  through nice graphs .  ")

bt1=st.button("show data")
if bt1:
       st.dataframe(dt.sample(5))

#plots
st.title("flow of sales over different time of years")
df_sales=df.groupby("Order_Date")['Sales'].sum()
fig=px.line(data_frame=df_sales,y="Sales")
st.plotly_chart(fig)
st.markdown("it seems that our sales increase in the last five months of the year.  ")

#plot
st.title("the number of  cities we deal with every month over years")

fig2=px.line(data_frame=date_city,title=' No of cities',labels={'value':'No of cities'})
st.plotly_chart(fig2)

#plot
st.title("the top 10 cities sale")
fig3=px.bar(data_frame=df2_sales,text_auto=True,y="Sales",title='top 10 cities sale')
st.plotly_chart(fig3)

st.markdown("looks like that New york and Los angeles are the two highest cities in sales ")

#plot
st.title("Growth of customers over time")
fig4=px.line(data_frame=date_customer,title='growth of cutomers',labels={'value':'no of customers'})
st.plotly_chart(fig4)
#plot
st.title("Sales over ship mode")
fig5=px.bar(data_frame=ship_sales,text_auto=True,title='sales over ship modes')
st.plotly_chart(fig5)

st.markdown("seems that most of our customers like to ship in standard class.  ")

#plot
st.title("sales over segment types")
fig6=px.bar(data_frame=Segment_sales,text_auto=True,title='sales over segment types')
st.plotly_chart(fig6)
st.markdown("Regular customers seem to make the most profit not coporates. ")

#plot
st.title("sales over our Categories")
fig7=px.bar(data_frame=Category_sales,text_auto=True,title='sales over categories')
st.plotly_chart(fig7)
st.markdown("seems taht our categories close to each other but technology are the  higest  sale.")

#plot
st.title("Top 10 cutomers make the highest sale")
f=px.bar(data_frame=cust_sale,text_auto=True,title='no of orders',labels={'value':'Fequency'})
st.plotly_chart(f)
st.markdown("look that Raymond buch make 15k then tom Ashbrook make 14.5k  ")
