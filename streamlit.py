import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("INDIAN CUISINE ANALYSIS")
data = pd.read_csv("cleaned_df (1).csv")


#st.dataframe(data,width=800,height=500)
#type(data)

#num=st.text_input("Enter No. of recipes")
#st.write(num)

#select=st.selectbox("Allergens",["milk","almonds","meat"],index=0)
#st.write(select)

#slide = st.slider("Rate me",max_value=10)

#num2 = st.number_input("numbers",min_value=0.0,max_value=10.0,step=1.0)

#img = st.file_uploader("upload a file")
#st.image(img)

data = data.head(20)
#st.line_chart(data)
#st.set_option('deprecation.showPyplotGlobalUse', True)
#fig, ax = plt.subplots()
#ax.scatter(data['CookTimeInMins'],data['PrepTimeInMins'])
#st.pyplot(fig)

#with depcration
#st.set_option('deprecation.showPyplotGlobalUse', False)
#plt.scatter(data['CookTimeInMins'],data['PrepTimeInMins'])
#st.pyplot()

#streamlit charts
#st.line_chart(data)
#st.area_chart(data)
#st.bar_chart(data)

#image
#st.image("WIN_20230405_18_24_35_Pro.jpg")

#sidebar
plt.style.use("ggplot")

rad=st.sidebar.radio("Navigation",["Home","Visualization","Recommendation System","Error Handling"])
if rad == "Home":
    st.dataframe(data,width=800,height=500)
    type(data)
    num=st.text_input("Enter No. of recipes")
    st.write(num)

    select=st.selectbox("Allergens",["milk","almonds","meat"],index=0)
    st.write(select)

    slide = st.slider("Rate me",max_value=10)

    num2 = st.number_input("numbers",min_value=0.0,max_value=10.0,step=1.0)

    img = st.file_uploader("upload a file")
    #st.image(img)

    #image
    st.image("us.jpg") 

elif rad == "Visualization":  

    viz = ["scatter","line","bar"]
    final=st.sidebar.selectbox("select the viz",viz)
    st.write(final)

    if final == viz[0]:
        #with depcration
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.scatter(data['CookTimeInMins'],data['PrepTimeInMins'])
        st.pyplot()

elif rad == "Recommendation System":
    st.title("Recipe")

else:
    st.error("Error: Error guys")
    st.success("Success: Jeet gaye")
    st.info("Information: Important khabar")
    st.exception(RuntimeError("Danger"))
    st.warning("Warning: Just a warning")

    st.balloons()
    