import pandas as pd
import streamlit as st
from model import UseCase,assess
st.set_page_config(page_title="AI Opportunity Studio",layout="wide")
st.title("AI Opportunity Studio")
st.caption("Interactive AI use-case prioritization and modeled business case — fictional examples only")
st.warning("Illustrative assumptions. These are not achieved savings or approved governance assessments.")
examples={"Customer email triage":(5000,5,.35,35,28000,6500,5,4,4,2,True),"Invoice processing":(2400,8,.5,33,45000,8500,4,4,4,2,True),"Employee hiring screen":(1200,9,.4,40,32000,10000,4,3,3,5,False),"Inventory forecasting":(900,25,.3,39,55000,12000,5,3,3,2,True),"Knowledge search":(3300,4,.5,38,18000,4900,4,5,4,1,True)}
selected=st.selectbox("Business opportunity",list(examples))
v=examples[selected]
with st.form("scenario"):
    a,b,c=st.columns(3)
    with a:
        volume=st.number_input("Monthly tasks",0,value=v[0]);minutes=st.number_input("Minutes per task",0.0,value=float(v[1]));share=st.slider("Effort reduction (%)",0,100,int(v[2]*100))
    with b:
        rate=st.number_input("Hourly cost (CAD)",0.0,value=float(v[3]));startup=st.number_input("Setup cost (CAD)",0.0,value=float(v[4]));operating=st.number_input("Annual operating cost (CAD)",0.0,value=float(v[5]))
    with c:
        fit=st.slider("Strategic fit",1,5,v[6]);ready=st.slider("Data readiness",1,5,v[7]);feasible=st.slider("Feasibility",1,5,v[8]);privacy=st.slider("Privacy risk",1,5,v[9]);human=st.checkbox("Human review included",v[10])
    st.form_submit_button("Evaluate scenario")
c=UseCase(selected,volume,minutes,share/100,rate,startup,operating,fit,ready,feasible,privacy,human)
r=assess(c)
x,y,z,w=st.columns(4)
x.metric("Hours freed per year",f"{r['hours_saved']:,.0f}")
y.metric("Year-1 net benefit",f"CAD {r['year_one_net_cad']:,.0f}")
z.metric("Three-year net benefit",f"CAD {r['three_year_net_cad']:,.0f}")
w.metric("Weighted priority score",f"{r['score']:.1f}/100")
st.subheader(r["decision"])
st.write("Privacy/governance and data-readiness gates override numeric scoring. Validate assumptions, data controls, accuracy, and change-management costs before any business decision.")
rows=[]
for name,values in examples.items():
    case=UseCase(name,*values)
    rows.append(dict(use_case=name,**assess(case)))
df=pd.DataFrame(rows).sort_values("score",ascending=False)
st.subheader("Portfolio comparison")
st.dataframe(df,hide_index=True,use_container_width=True)
st.bar_chart(df.set_index("use_case")["score"])
st.download_button("Download prioritization CSV",df.to_csv(index=False),"priority_scores.csv","text/csv")
brief=f"ILLUSTRATIVE AI OPPORTUNITY ASSESSMENT\nUse case: {selected}\nDecision: {r['decision']}\nPriority score: {r['score']}\nModeled year-1 benefit: CAD {r['year_one_net_cad']}\nControls: validate privacy, data quality, financial assumptions, and human oversight before a pilot.\n"
st.download_button("Download stakeholder brief",brief,"decision_brief.txt","text/plain")
