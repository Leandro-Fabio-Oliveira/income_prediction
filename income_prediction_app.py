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
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        'Introduction',
        'Data Understanding',
        'Data Preparation',
        'Modeling',
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
        
        st.markdown("""
        Here, we did few changes in the dataset. First filled nan values in **job_tenure**
        with the mean, and next created a new variabel **log_income** that is the log of **income**
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown('## 06 - Modeling')
        
        st.markdown("""
        |    | 0                 | 1                | 2                   | 3         |
        |---:|:------------------|:-----------------|:--------------------|:----------|
        |  0 | Dep. Variable:    | log_renda        | R-squared:          | 0.342     |
        |  1 | Model:            | OLS              | Adj. R-squared:     | 0.341     |
        |  2 | Method:           | Least Squares    | F-statistic:        | 407.0     |
        |  3 | Date:             | Mon, 29 Sep 2025 | Prob (F-statistic): | 0.00      |
        |  4 | Time:             | 21:22:14         | Log-Likelihood:     | -11098.   |
        |  5 | No. Observations: | 10215            | AIC:                | 2.222e+04 |
        |  6 | Df Residuals:     | 10201            | BIC:                | 2.233e+04 |
        |  7 | Df Model:         | 13               |                     |           |
        |  8 | Covariance Type:  | nonrobust        |                     |           |
        """, unsafe_allow_html=True)
        
        st.markdown("""
        |  0 |                                 | coef    | std err | t      | P>|t| | [0.025 | 0.975] |
        |---:|:--------------------------------|:--------|:--------|:-------|:------|:-------|:-------|
        |  1 | Intercept                       | 7.1537  | 0.077   | 93.440 | 0.000 | 7.004  | 7.304  |
        |  2 | sexo[T.M]                       | 0.7900  | 0.017   | 47.359 | 0.000 | 0.757  | 0.823  |
        |  3 | posse_de_veiculo[T.True]        | 0.0421  | 0.016   | 2.658  | 0.008 | 0.011  | 0.073  |
        |  4 | posse_de_imovel[T.True]         | 0.0996  | 0.015   | 6.494  | 0.000 | 0.070  | 0.130  |
        |  5 | tipo_renda[T.Bolsista]          | 0.1122  | 0.272   | 0.413  | 0.680 | -0.421 | 0.645  |
        |  6 | tipo_renda[T.Empresário]        | 0.1377  | 0.018   | 7.649  | 0.000 | 0.102  | 0.173  |
        |  7 | tipo_renda[T.Pensionista]       | -0.2044 | 0.025   | -8.118 | 0.000 | -0.254 | -0.155 |
        |  8 | tipo_renda[T.Servidor público]  | 0.0560  | 0.027   | 2.100  | 0.036 | 0.004  | 0.108  |
        |  9 | educacao[T.Pós graduação]       | 0.0986  | 0.187   | 0.527  | 0.598 | -0.268 | 0.465  |
        | 10 | educacao[T.Secundário]          | -0.0481 | 0.068   | -0.710 | 0.478 | -0.181 | 0.085  |
        | 11 | educacao[T.Superior completo]   | 0.0832  | 0.068   | 1.219  | 0.223 | -0.051 | 0.217  |
        | 12 | educacao[T.Superior incompleto] | -0.0394 | 0.077   | -0.515 | 0.607 | -0.189 | 0.111  |
        | 13 | idade                           | 0.0054  | 0.001   | 6.221  | 0.000 | 0.004  | 0.007  |
        | 14 | tempo_emprego                   | 0.0613  | 0.001   | 49.060 | 0.000 | 0.059  | 0.064  |
        """, unsafe_allow_html=True)
    
    with tab5:
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