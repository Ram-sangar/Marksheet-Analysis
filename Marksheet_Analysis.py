import streamlit as st
import pandas as pd
import plotly.express as px
import base64 
import csv
import matplotlib.pyplot as plt
from io import StringIO, BytesIO
import math
import os

#heading
hide_st_style="""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)

def set_custom_style():
    st.markdown('<style>' + open('static/styles.css').read() + '</style>', unsafe_allow_html=True)
set_custom_style()
#DEPARTMENT

d=pd.read_csv('DEPARTMENT.csv')

dep=[]
for i in d.head(1):
     dep.append(i)
with st.sidebar:
       st.write("ST.JOSEPH'S COLLEGE(AUTONOMOUS)")
       select_dep=st.selectbox('Select the department :',dep)
       select_year= st.text_input(
        "Enter the year :" )
       select_class=st.selectbox('Select the class :',d[select_dep]) 
       select_Sem=st.selectbox('Select the Sem',[1,2,3,4,5,6])
       title = st.text_input(
        "Enter File Name 👇" )
       st.write('Your file Name is:',title)
a=[]
if(select_class!="" and select_dep!="Department" and select_year!="" and select_Sem!=""):
             #file
             df = pd.read_csv(f"{select_class} {select_year} Sem {select_Sem}.csv")
             
             for i in df.head(0):
                if(i.title()!='Sno' and i.title()!='Name' and i.title()!='Dno' and i.title()!='Department' and i.title()!='Class'):
                   a.append(i)
             groupby_column=st.selectbox('What would you like to analyse?',a)
             
             e=f=g=h=0
             for i in df[groupby_column]:
               if isinstance(i, (int, float)) and not math.isnan(i):
   
                 if(int(i)>=80 and int(i)<=100 ):
                     e+=1
                 elif(int(i)>=70 and int(i)<=89 ):
                     f+=1
                 elif(int(i)>=50 and int(i)<=69 ):
                     g+=1
                 elif(int(i)<50 ):
                     h+=1
                     
               #write csv
               
               folder_input = 'D:/streamlit/Department/Backup/'
               file_input =title+'.csv'

               with open( os.path.join(folder_input, file_input),  'w', newline='') as csvfile:
                  fieldnames = ['grade', 'count']
                  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                  writer.writeheader()
                  writer.writerow({'grade':'first class' , 'count': e})
                  writer.writerow({'grade':'second class' , 'count': f})
                  writer.writerow({'grade':'third class' , 'count': g})
                  writer.writerow({'grade':'failers' , 'count': h})
               def main():
              
                  #display
                col1, col2= st.columns([2,3])
                with col1:
                    st.subheader('Data')
                    data=pd.read_csv(r'D:/streamlit/Department/Backup/'+title+'.csv')
                    st.dataframe(data, width = 400,height=300)
                    def generate_csv():
                      df = pd.DataFrame(data)
                      return df
                    df = generate_csv()
                    #download
                    csv_data = df.to_csv(index=False)
                    st.download_button(label="Download CSV", data=csv_data, file_name=title+'.csv', mime='text/csv')
              
                with col2:
                    st.subheader('Bar Chart')
                    fig_bar = px.bar(data, x='grade', y='count', color='count')
                    st.plotly_chart(fig_bar)

else:
    st.write("Please select the Department and class.")
if st.button("Submit"):
    if __name__ == '__main__':
            main()     
