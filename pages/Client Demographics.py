import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

#loading data

#population 
pop_per_state =pd.read_csv("au.csv")
#Income
couple_family_income = pd.read_excel('Household and families data summary.xlsx',sheet_name='Table 7')
#industries
#employment_industries = pd.read_csv("Industry_AllTimePeriod_DataType_UR_For_10_20.csv")
#employment_industries["2021_"] = pd.to_numeric(employment_industries["2021_"])
#employment_industries["2021%_"] = pd.to_numeric(employment_industries["2021%_"])

st.title("Client Demographics")
st.subheader("Overview")

st.markdown(
    """
    The following dashboard contains:

    - Age distribution of guests: This would include data on the percentage of guests in different age groups, such as children, teenagers, young adults, middle-aged adults, and seniors.
    - Gender distribution of guests: This would include data on the percentage of male and female guests.
    - Occupation: This would include data on the percentage of guests in different occupational groups, such as retiree, students, professionals, blue collar workers etc.
    - Family structure: This would include data on the percentage of guests who are traveling as a family, with children, or alone.
    - Income level: This would include data on the average income level of guests, which could be used to target marketing efforts to different groups of people.
    - Location: This would include data on the percentage of guests from different regions, both within Australia and internationally.
    - repeat customers: This would include data on how many customers have returned to the camp/caravan site.
    - Seasonal variation: This would include data on how the demographics of guests vary by season, such as holiday season, school holidays etc.
    - Feedback: This would include data on feedback received from the customers on their demographics, this can be done by having a section on feedback forms where customers can fill out their demographic information.
    
    """)
#Dataframe editing 
couple_family_income['family type'] = couple_family_income['Unnamed: 0']
source = couple_family_income.sort_values('Total',ascending=True)

source1 = pop_per_state.sort_values('population')

st.subheader('Population density')
st.map(data=pop_per_state)

st.info("We will now see the most populated States and teritories in Australia, you can switch between the population and the actual population present in these states ")

#Population by state
st.subheader("population by State")
interval1 = st.selectbox("Select the population type you want to visualize",["population","population_proper"])
if interval1 == "population":
    bar_chart = alt.Chart(source1).mark_bar().encode(
        y= "population",
        x='admin_name')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval1 == "population_proper":
    bar_chart = alt.Chart(source1).mark_bar().encode(
        y= "population_proper",
        x='admin_name')
    st.altair_chart(bar_chart, use_container_width=True)

st.info("Streamlit has a sorting bug with all versions over 1.11.1, new patch should fix the problem when available")

st.subheader("Key Census data of interest")
interval3 = st.selectbox("Choose the key figure",["Count by generation","Country of birth and ancestry","Growth Comunities"])
if interval3 == "Count by generation":
    st.subheader("Count by generation 2021 census")
    st.image(image="https://www.abs.gov.au/system/files/styles/complex_image/private/099ab8cdfaec09c740dd139109b0158a/RITM0195218%20-%20Census%20DR22%20Infographic%20Population%20%28680x500px%29_GEN%20WEB.jpg?itok=xDQe1wPh",output_format='JPEG')
elif interval3 == "Country of birth and ancestry":
    st.subheader("Country of birth and ancestry")
    st.image(image="https://www.abs.gov.au/system/files/styles/complex_image/private/3a681f68c12cb92c6dffcf5aaa9835f9/RITM0195219%20-%20Census%20DR22%20Infographics%20Cultural%20diversity%20%28680x500px%29_FA%20Third%20Gen%20WEB1.jpg?itok=uy-3ofOS",output_format='JPEG')
elif interval3 == "Growth Comunities":
    st.subheader("Growth Comunities")
    st.image(image="https://www.abs.gov.au/system/files/styles/complex_image/private/5f037271cda61454fb44a6ba574b67a8/RITM0195219%20-%20Census%20DR22%20Infographics%20Cultural%20diversity%20%28680x500px%29_FA%20Map1.jpg?itok=Gil_jONV",output_format='JPEG')

st.subheader("Finances")
st.markdown("The following tables are representative of the financial structure in Australia")


interval3 = st.selectbox("Choose the key figure",["Average superannuation account balance by gender","The top 20 performing balanced options","Employment industries"])
if interval3 == "Average superannuation account balance by gender":
    st.subheader("Average superannuation account balance by gender")
    st.image(image="https://www.apra.gov.au/sites/default/files/styles/embedded_image/public/2019-12/Super%20gender.png?itok=XguB89Di",output_format='JPEG')
elif interval3 == "The top 20 performing balanced options":
    st.subheader("The top 20 performing balanced options")
    st.image(image="https://www.lonsec.com.au/super-fund/wp-content/uploads/sites/3/2022/01/Picture2-1030x402.png",output_format='JPEG')
elif interval3 == "Employment industries":
    st.subheader("Employment industries")
    st.image(image="https://www.aph.gov.au/-/media/05_About_Parliament/54_Parliamentary_Depts/544_Parliamentary_Library/Research_Papers/2020-21/QuickGuides/QG-EmploymentIndustryStatistics-003.PNG?h=481&w=500&la=en&hash=B5931837EE70FF53EE40715EBBE444D425557796",output_format='JPEG')


#Couple and family data visuals
st.subheader('Couple and Family weekly income')
interval = st.selectbox("Select the column you want to visualize",couple_family_income.columns.drop(['family type','Unnamed: 0']))
if interval == couple_family_income.columns[0]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[0],
        x='family type')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval == couple_family_income.columns[1]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[1],
        x='family type')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval == couple_family_income.columns[2]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[2],
        x='family type')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval == couple_family_income.columns[3]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[3],
        x='family type')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval == couple_family_income.columns[4]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[4],
        x='family type')
    st.altair_chart(bar_chart, use_container_width=True)

elif interval == couple_family_income.columns[5]:
    bar_chart = alt.Chart(source).mark_bar().encode(
        y= couple_family_income.columns[5],
        x='family type')
 
    st.altair_chart(bar_chart, use_container_width=True)

st.subheader("Raw view of the family income data")
st.dataframe(couple_family_income)

