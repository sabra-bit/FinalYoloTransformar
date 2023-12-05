import streamlit as st
from io import StringIO
from ultralytics import YOLO
from PIL import Image
import requests
import os , time
import platform
print(platform.system())
st.header('car accident detection system', divider='rainbow')
st.header(':blue[import car image] ')
costrear=costfront=costleft=costright=0
tab1, tab2, tab3 , tab4 = st.tabs(["left", "right", "front","rear"])
with tab1:
    uploaded_file = st.file_uploader("Choose a file to upload left side")

    if uploaded_file:
        st.image(uploaded_file)
        img = Image.open(uploaded_file)
        model = YOLO("best.pt")
        results = model(img)
        names = model.names

        
        clas = []
        for r in results:
            for c in r.boxes.cls:
                clas.append(names[int(c)])
                print(names[int(c)])
        res = [clas[i] for i in range(len(clas)) if i == clas.index(clas[i]) ]
        
        print(res)
        
        
        API_TOKEN="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"
        API_URL = "https://api-inference.huggingface.co/models/opiljain/autotrain-cardamage-3762299975"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        def query():
            
            data = uploaded_file.getbuffer()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query()
        
        print(output)
        
        if res and output:
            st.info('calculate fixing Cost estimation', icon="ℹ️")
            if output[0]["label"] == "Door" or output[0]["label"] == "hood" :
                st.write(output[0]["label"] + " has "+ res[0])
                col1, col2, col3 ,col4 ,col5 = st.columns(5)
                costleft = 0
                with col1:
                    xleft=number = st.number_input('hour ')

                with col2:
                    yleft=number = st.number_input('cost of hour ')

                with col3:
                    zleft=number = st.number_input('cost of new  '+output[0]["label"])
                with col4:
                    if st.button('calculate '):
                        costleft = xleft*yleft+zleft
                with col5:
                    if costleft:
                        st.success(str(costleft))
                    
                        
            else:
                st.warning("cann't detect problem", icon="⚠️")
                
        else:
            st.warning("cann't detect car problem", icon="⚠️")
            if st.button('add to dataset ', type="primary"):
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                st.success('Done!')
with tab2:
    uploaded_file = st.file_uploader("Choose a file to upload right side")

    if uploaded_file:
        st.image(uploaded_file)
        img = Image.open(uploaded_file)
        model = YOLO("best.pt")
        results = model(img)
        names = model.names

        
        clas = []
        for r in results:
            for c in r.boxes.cls:
                clas.append(names[int(c)])
                print(names[int(c)])
        res = [clas[i] for i in range(len(clas)) if i == clas.index(clas[i]) ]
        
        print(res)
        
        
        API_TOKEN="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"
        API_URL = "https://api-inference.huggingface.co/models/opiljain/autotrain-cardamage-3762299975"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        def query():
            
            data = uploaded_file.getbuffer()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query()
        
        print(output)
        
        if res and output:
            st.info('calculate fixing Cost estimation', icon="ℹ️")
            if output[0]["label"] == "Door" or output[0]["label"] == "hood" :
                st.write(output[0]["label"] + " has "+ res[0])
                col1, col2, col3 ,col4 ,col5 = st.columns(5)
                costright = 0
                with col1:
                    xright=number = st.number_input('hour  ')

                with col2:
                    yright=number = st.number_input('cost of hour  ')

                with col3:
                    zright=number = st.number_input('cost of new   '+output[0]["label"])
                with col4:
                    if st.button('calculate  '):
                        costright = xright*yright+zright
                with col5:
                    if costright:
                        st.success(str(costright))
                    
                        
            else:
                st.warning("cann't detect problem", icon="⚠️")
                
        else:
            st.warning("cann't detect car problem", icon="⚠️")
            if st.button('add to dataset', type="primary"):
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                st.success('Done!')
with tab3:
    uploaded_file = st.file_uploader("Choose a file to upload front side")

    if uploaded_file:
        st.image(uploaded_file)
        img = Image.open(uploaded_file)
        model = YOLO("best.pt")
        results = model(img)
        names = model.names

        
        clas = []
        for r in results:
            for c in r.boxes.cls:
                clas.append(names[int(c)])
                print(names[int(c)])
        res = [clas[i] for i in range(len(clas)) if i == clas.index(clas[i]) ]
        
        print(res)
        
        
        API_TOKEN="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"
        API_URL = "https://api-inference.huggingface.co/models/opiljain/autotrain-cardamage-3762299975"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        def query():
            
            data = uploaded_file.getbuffer()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query()
        
        print(output)
        
        if res and output:
            st.info('calculate fixing Cost estimation', icon="ℹ️")
            if output[0]["label"] == "Door" or output[0]["label"] == "hood" :
                st.write(output[0]["label"] + " has "+ res[0])
                col1, col2, col3 ,col4 ,col5 = st.columns(5)
                costfront = 0
                with col1:
                    xfront=number = st.number_input('hour   ')

                with col2:
                    yfront=number = st.number_input('cost of hour   ')

                with col3:
                    zfront=number = st.number_input('cost of new    '+output[0]["label"])
                with col4:
                    if st.button('calculate   '):
                        costfront = xfront*yfront+zfront
                with col5:
                    if costfront:
                        st.success(str(costfront))
                    
                        
            else:
                st.warning("cann't detect problem", icon="⚠️")
                
        else:
            st.warning("cann't detect car problem", icon="⚠️")
            if st.button('add to dataset', type="primary"):
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                st.success('Done!')
with tab4:
    uploaded_file = st.file_uploader("Choose a file to upload rear side")

    if uploaded_file:
        st.image(uploaded_file)
        img = Image.open(uploaded_file)
        model = YOLO("best.pt")
        results = model(img)
        names = model.names

        
        clas = []
        for r in results:
            for c in r.boxes.cls:
                clas.append(names[int(c)])
                print(names[int(c)])
        res = [clas[i] for i in range(len(clas)) if i == clas.index(clas[i]) ]
        
        print(res)
        
        
        API_TOKEN="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"
        API_URL = "https://api-inference.huggingface.co/models/opiljain/autotrain-cardamage-3762299975"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        def query():
            
            data = uploaded_file.getbuffer()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query()
        
        print(output)
        
        if res and output:
            st.info('calculate fixing Cost estimation', icon="ℹ️")
            if output[0]["label"] == "Door" or output[0]["label"] == "hood" :
                st.write(output[0]["label"] + " has "+ res[0])
                col1, col2, col3 ,col4 ,col5 = st.columns(5)
                costrear = 0
                with col1:
                    xrear=number = st.number_input('hour    ')

                with col2:
                    yrear=number = st.number_input('cost of hour    ')

                with col3:
                    zrear=number = st.number_input('cost of new     '+output[0]["label"])
                with col4:
                    if st.button('calculate    '):
                        costrear = xrear*yrear+zrear
                with col5:
                    if costrear:
                        st.success(str(costrear))
                    
                        
            else:
                st.warning("cann't detect problem", icon="⚠️")
                
        else:
            st.warning("cann't detect car problem", icon="⚠️")
            if st.button('add to dataset', type="primary"):
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                st.success('Done!')
                

if st.button('Get total cost', type="primary"):
    try:
        costfront = xfront*yfront+zfront
    except:
        costfront = 0
        
    try:
        costleft = xleft*yleft+zleft
    except:
        costleft = 0
    try:
        costright = xright*yright+zright
    except:
        costright = 0
    try:
        costrear = xrear*yrear+zrear
    except:
        costrear = 0
    
    
    st.success("Total cost: "+str(int(costrear+costfront+costleft+costright))+"$")
    print()

    
    
# from ultralytics import YOLO
# model = YOLO("best.pt")
# results = model("12.jpeg")

# names = model.names

# for r in results:
#     for c in r.boxes.cls:
#         print(names[int(c)])

