import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def gender_analysis(df: pd.DataFrame):
    # Variable Title
    st.markdown('### Gender Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='sexo')
    
    # Plot config
    plt.title('Gender Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('F = Female | M = Male')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Histogram analysis
    st.markdown("""
    Approximately two-thirds of the dataset consists of women.
    """)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating pointplot
    sns.pointplot(data=df,
                  y='renda',
                  x='sexo',
                  color='red',
                  label='Mean')
                  
    sns.pointplot(data=df,
                  y='renda',
                  x='sexo',
                  estimator='median',
                  label='Median')
    
    # Plot config
    plt.title('Mean and Median Income by Gender')
    plt.ylabel('Income')
    plt.xlabel('F = Female | M = Male')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Pointplot analysis
    st.markdown("""
    The dataset shows us that men have a higher income compared to women.
    """)


def car_owner_analysis(df: pd.DataFrame):
    # Adjusting to bool
    df['posse_de_veiculo'] = df['posse_de_veiculo'].map({
        True: 'True', False: 'False'})
    
    # Variable Title
    st.markdown('### Car Owner Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='posse_de_veiculo', bins=2)
    
    # Plot config
    plt.title('Car Owner Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('False = Is not a car owner | True = Is a car owner')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    60% of the dataset do not own a car.
    """)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating pointplot
    sns.pointplot(data=df,
                  y='renda',
                  x='posse_de_veiculo',
                  color='red',
                  label='Mean')
    
    sns.pointplot(data=df,
                  y='renda',
                  x='posse_de_veiculo',
                  estimator='median',
                  label='Median')
    
    # Plot config
    plt.title('Mean and Median Income by Car Ownership')
    plt.ylabel('Income')
    plt.xlabel('False = Is not a car owner | True = Is a car owner')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Pointplot analysis
    st.markdown("""
    Another insight: customers who own a car have a higher income.
    """)


def house_owner_analysis(df: pd.DataFrame):
    # Adjusting to bool
    df['posse_de_imovel'] = df['posse_de_imovel'].map({
        True: 'True', False: 'False'})
    
    # Variable Title
    st.markdown('### House Owner Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='posse_de_imovel', bins=2)
    
    # Plot config
    plt.title('House Owner Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('False = Is not a house owner | True = Is a house owner')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    As in the gender analysis, two-thirds of the dataset do not own a house.
    """)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating pointplot
    sns.pointplot(data=df,
                  y='renda',
                  x='posse_de_imovel',
                  color='red',
                  label='Mean')
    
    sns.pointplot(data=df,
                  y='renda',
                  x='posse_de_imovel',
                  estimator='median',
                  label='Median')
    
    # Plot config
    plt.title('Mean and Median Income by House Ownership')
    plt.ylabel('Income')
    plt.xlabel('False = Is not a house owner | True = Is a house owner')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Pointplot analysis
    st.markdown("""
    The dataset shows us that **house ownership** does not discriminate against
    the customer's income.
    """, unsafe_allow_html=True)


def number_children_analysis(df: pd.DataFrame):
    # Variable Title
    st.markdown('### Number of Children Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='qtd_filhos', element='step', discrete=True)
    
    # Plot config
    plt.title('Number of Children Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('Numbere of Children')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    Most customers do not have children, and among those who do, the most
    common number is around 1 or 2. This reflects contemporary family
    structures.
    """)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating lineplot
    sns.lineplot(data=df, x='qtd_filhos', y='renda')
    
    # Plot config
    plt.title('Income by Number of Children')
    plt.ylabel('Income')
    plt.xlabel('Number of Children')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Pointplot analysis
    st.markdown("""
    There is no clear pattern here that helps us understand the customer's
    **income**.
    """, unsafe_allow_html=True)


def income_type_analysis(df: pd.DataFrame):
    # Translating
    df['tipo_renda'] = df['tipo_renda'].map({
       'Empresário': 'Businessperson',
       'Assalariado': 'Salaried',
       'Servidor público': 'Public servant',
       'Pensionista': 'Pensioner',
       'Bolsista': 'Scholarship recipient'})
    
    # Variable Title
    st.markdown('### Income Type Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, y='tipo_renda', element='step', discrete=True)
    
    # Plot config
    plt.title('Income Type Distribution')
    plt.ylabel('')
    plt.xlabel('Frequency')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    What catches my attention here is that there are only a few customers
    whose income comes from **scholarships**. This could potentially distort
    the model.
    """, unsafe_allow_html=True)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating barplot
    sns.barplot(data=df, x='renda', y='tipo_renda')
    
    # Plot config
    plt.title('Mean Income by Income Type')
    plt.ylabel('')
    plt.xlabel('Income')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    As mentioned before, the dataset contains only a few **scholarship
    recipients**, which causes the variable to have a large confidence
    interval, leading to a potential distortion in the model.
    **Public Servant** and **Pensioner** show distinct differences in
    **Income**, while **Businessperson** and **Salaried** individuals do not.
    
    Therefore, this variable does not seem to help the model predict customer's
    **Income**
    """, unsafe_allow_html=True)


def education_analysis(df: pd.DataFrame):
    # Translating
    df['educacao'] = df['educacao'].map({
       'Primário': 'Primary school',
       'Secundário': 'Secondary school',
       'Superior incompleto': 'Incomplete higher education',
       'Superior completo': 'Higher education',
       'Pós-graduação': 'Postgraduate education'})
    
    # Variable Title
    st.markdown('### Education Level Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, y='educacao', element='step', discrete=True)
    
    # Plot config
    plt.title('Education Level Distribution')
    plt.ylabel('')
    plt.xlabel('Frequency')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    Most of customers has **Secondary School** or **Higher education**.
    """, unsafe_allow_html=True)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating barplot
    sns.barplot(data=df, x='renda', y='educacao')
    
    # Plot config
    plt.title('Mean Income by Education Level')
    plt.ylabel('')
    plt.xlabel('Income')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    If we consider the confidence interval, this variable does not help to
    explain the customer's **Income**.
    """, unsafe_allow_html=True)


def marital_status_analysis(df: pd.DataFrame):
    # Translating
    df['estado_civil'] = df['estado_civil'].map({
       'Solteiro': 'Single',
       'União': 'Civil union',
       'Casado': 'Married',
       'Separado': 'Separated',
       'Viúvo': 'Widowed'})
    
    # Variable Title
    st.markdown('### Marital Status Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, y='estado_civil', element='step', discrete=True)
    
    # Plot config
    plt.title('Marital Status Distribution')
    plt.ylabel('')
    plt.xlabel('Frequency')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    It is very clear that most of the customers are **married**, followed by
    **single** ones. Other marital statuses are well distributed.
    """, unsafe_allow_html=True)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating barplot
    sns.barplot(data=df, x='renda', y='estado_civil')
    
    # Plot config
    plt.title('Mean Income by Education Level')
    plt.ylabel('')
    plt.xlabel('Income')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    **Single**, **Civil Union** and **Separated** are very close to each
    other, which can make modeling difficult.
    """, unsafe_allow_html=True)


def residence_type_analysis(df: pd.DataFrame):
    # Translating
    df['tipo_residencia'] = df['tipo_residencia'].map({
       'Casa': 'House',
       'Governamental': 'Government housing',
       'Com os pais': 'Living with parents',
       'Aluguel': 'Rented',
       'Comunitário': 'Communal housing',
       'Estúdio': 'Studio apartment'})
    
    # Variable Title
    st.markdown('### Residence Type Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, y='tipo_residencia', element='step', discrete=True)
    
    # Plot config
    plt.title('Residence Type Distribution')
    plt.ylabel('')
    plt.xlabel('Frequency')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    With the majority of the customers living in a house, it can be hard to
    generalize and predict customers' income, as the dataset is not evenly
    distributed across residence types.
    """, unsafe_allow_html=True)
    
    st.markdown('#### Bivariate Analysis')
    
    # Creating barplot
    sns.barplot(data=df, x='renda', y='tipo_residencia')
    
    # Plot config
    plt.title('Mean Income by Residence Type')
    plt.ylabel('')
    plt.xlabel('Income')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    Due to low freqeuncy, most of the variables have a wide confidence
    interval, which makes modeling really challenging.
    """, unsafe_allow_html=True)


def age_analysis(df: pd.DataFrame):
    # Variable Title
    st.markdown('### Age Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='idade', element='step', discrete=True)
    
    # Plot config
    plt.title('Age Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('Age')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    The dataset has a high concentration of customers aged **30** to **50**.
    After that, the frequency decreases.
    """, unsafe_allow_html=True)
    
    # Creating scatterplot
    sns.scatterplot(data=df, x='idade', y='renda')
    
    # Plot config
    plt.title('Relationship Between Age and Income')
    plt.ylabel('Income')
    plt.xlabel('Age')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    It suggests that most customers' **income** stays stays relatively low and
    uniform. So, age is not useful for predicting a customer's **income**.
    """, unsafe_allow_html=True)


def job_tenure_analysis(df: pd.DataFrame):
    # Variable Title
    st.markdown('### Job Tenure Analysis')
    
    st.markdown('#### Univariate Analysis')
    
    # Creating histogram
    sns.histplot(data=df, x='tempo_emprego', element='step', discrete=True)
    
    # Plot config
    plt.title('Job Tenure Distribution')
    plt.ylabel('Frequency')
    plt.xlabel('Job Tenure (years)')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    # Distribution analysis
    st.markdown("""
    No surprises here. The distribution is mostly concentrated between 0 and
    10 years of job tenure, as people generally stay only a few years in a
    company to gain experience (which is also better for their résumé).
    However, most employees leave before reaching 15 years, looking for career
    growth.
    """, unsafe_allow_html=True)
    
    # Creating scatterplot
    sns.scatterplot(data=df, x='tempo_emprego', y='renda')
    
    # Plot config
    plt.title('Relationship Between Job Tenure and Income')
    plt.ylabel('Income')
    plt.xlabel('Job Tenure (years)')
    
    # Showing plot on Streamlit
    st.pyplot(plt)
    plt.close()
    
    st.markdown("""
    Something interesting! It is possible to see that customers with higher
    **job tenure** tend to have a higher **income**.
    """, unsafe_allow_html=True)