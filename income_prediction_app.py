#_____LOADING_PACKAGES_/_INITIAL_CONFIG:______________________________________
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import time

import analyses as als

sns.set_style('dark')


#_____MAIN_APP:_______________________________________________________________
def main_app():
    st.title('Income Prediction - EDA') # Title
    
    # Developed By
    st.markdown("""
    *Developed by [Leandro Fabio de Oliveira](https://leandrofabioportfolio.streamlit.app/)*
    """, unsafe_allow_html=True)
    
    # Tabs creation
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        'Introduction',
        'Data Understanding',
        'Data Preparation',
        'Modeling',
        'Evaluation',
        'Deployment'
        ])
    
    # TAB_1_Introduction
    with tab1:
        st.markdown('## 01 - Introduction')
        st.markdown("""
        As part of the Data Science course from [EBAC](https://ebaconline.com.br/)
        (Escola Britânica de Artes Criativas e Tecnologia), this project aims
        to perform an Exploratory Data Analysis (EDA) and develop a model
        focused on predicting customer income.
        """, unsafe_allow_html=True)
        
        st.markdown('## 02 - CRISP-DM Method')
        
        st.markdown("""
        We will use the CRISP-DM methodology (Cross-Industry Standard Process
        for Data Mining), which consists of six phases:<br>
        """, unsafe_allow_html=True)
        
        # Create containers
        col1, col2, colvoid = st.columns([1,3,1])
        
        # Load CRISP-DM image
        with col1:
            st.image("./images/crispdm.png", use_container_width=True)
        
        # CRISP-DM description
        with col2:
            st.markdown("""            
            • **Business Understanding** - Clarify the project’s objectives
            and requirements from a business perspective by identifying key
            goals and defining the problem to be solved.<br>
            
            • **Data Understanding** - Gather, explore, and examine data to
            assess its relevance to the problem.<br>
            
            • **Data Preparation** - Clean, construct, integrate, and format
            the data to prepare it for modeling.<br>
            
            • **Modeling** - Choose, train, and optimize model algorithms
            using the prepared data.<br>
            
            • **Evaluation** - Evaluate the model’s performance using metrics
            like as accuracy, precision, and recall to determine if it
            effectively solves the business problem.<br>
            
            • **Deployment** - Implement the final model.
            """, unsafe_allow_html=True)
        
        # Business Understanding
        st.markdown('## 03 - Business Understanding')
        st.markdown("""
        Income prediction is a crucial task for financial companies, helping
        drive strategic decisions such as **credit analysis**, **risk analysis**
        and **customer segmentation**. Improving overall operational efficiency
        and profitability.
        """, unsafe_allow_html=True)
    
    # TAB_2_Data_Understanding
    with tab2:
        st.markdown('## 04 - Data Understanding')
        
        st.markdown("""
        Let's take a look at our data structure. Below is the data dictionary:
        """)
        
        # Expander
        with st.expander('### 04.01 - Data Dictionary'):
            st.markdown("""
            | Variable                | Description                                                                                                                                        | Data Type    |
            | ----------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------| ------------:|
            | **date_ref**            | The reference date                                                                                                                                 | Date         |
            | **customer_id**         | Customer ID                                                                                                                                        | Int          |
            | **sex**                 | Customer's gender:<br>• **F** = Female <br>• **M** = Male                                                                                          | Categorical  |
            | **car_owner**           | Indicates if the customer owns a vehicle                                                                                                           | Bool         |
            | **house_owner**         | Indicates if the customer owns a house                                                                                                             | Bool         |
            | **n_children**          | Number of children the customer has                                                                                                                | Int          |
            | **income_type**         | Income type categories include: <br> • Businessperson<br> • Salaried<br> • Public servant<br> • Pensioner<br> • Scholarship recipient              | Categorical  |
            | **education**           | Education level:<br> • Primary school<br> • Secondary school<br> • Incomplete higher education<br> • Higher education<br> • Postgraduate education | Categorical  |
            | **marital_status**      | Marital status:<br> • Single<br> • Civil union<br> • Married<br> • Separated<br> • Widowed                                                         | Categorical  |
            | **residence_type**      | Type of residence:<br> • House<br> • Government housing<br> • Living with parents<br> • Rented<br> • Communal housing<br> • Studio apartment       | Categorical  |
            | **age**                 | Customer's age (in years)                                                                                                                          | Int          |
            | **job_tenure**          | Customer's tenure at current job (in years)                                                                                                        | Float        |
            | **people_in_household** | Number of people in the customer's household                                                                                                       | Float        |
            | **income**              | Income in BRL (Brazilian Real)                                                                                                                     | Float        |
            """, unsafe_allow_html=True)
        
        # Start of analisys
        st.markdown("""
        Now, we will divide Data Understanding into a few steps:<br>
        
        • **Univariate analysis** - This involves analyzing each variable
        individually, looking for its distribution in the dataset.<br>
        
        • **Bivariate analysis** - It compares two variables to understand the
        relationship between them. It's important because it allows us to
        identify patterns and correlations. Here, we are going to compare some
        variables with our target, income.
        """, unsafe_allow_html=True)
        
        st.markdown('*<br>Click the arrows to switch between variable analyses*', unsafe_allow_html=True)
        
        # Structure to save atual analysis
        if "n_als" not in st.session_state:
            st.session_state.n_als = 1
        
        # Creates the analisys dict 
        analysis_to_show = {
            1: als.income_type_analysis,
            2: als.gender_analysis,
            3: als.car_owner_analysis,
            4: als.house_owner_analysis,
            5: als.number_children_analysis,
            6: als.education_analysis,
            7: als.marital_status_analysis,
            8: als.residence_type_analysis,
            9: als.age_analysis,
            10: als.job_tenure_analysis
            }
        
        # Create the buttons back, forward and the space of the analisys
        uni1, uni2, uni3 = st.columns([1, 10, 1])
        
        # Preevious Analysis
        with uni1:
            st.button('←', on_click=previous_analysis)
        
        # Display Analysis
        with uni2:
            # Loading
            with st.spinner('Wait for it...'):
                time.sleep(2)
            
            # Showing analysis
            analysis_to_show[st.session_state.n_als](df)
        
        # Next Analysis
        with uni3:
            st.button('→', on_click=next_analysis)
    
    with tab3:
        st.markdown('## 05 - Data Preparation')
    
    with tab4:
        st.markdown('## 06 - Modeling')
    
    with tab5:
        st.markdown('## 07 - Evaluation')
    
    with tab6:
        st.markdown('## 08 - Deployment')
    
    
    
    
    
    
    
    

def previous_analysis():
    st.session_state.n_als = 10 if st.session_state.n_als == 1 else st.session_state.n_als - 1

def next_analysis():
    st.session_state.n_als = 1 if st.session_state.n_als == 10 else st.session_state.n_als + 1



#_____LOAD_DATA________________________________________________________
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# loading data
df = load_data('./data/previsao_de_renda.csv')
df.drop(columns=['Unnamed: 0', 'id_cliente', 'data_ref'], inplace=True)
df.drop_duplicates(keep='first', inplace=True)


#_____RUNNING_APP:____________________________________________________________
if __name__ == "__main__":
    main_app()