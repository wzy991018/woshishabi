#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request


# In[2]:


app=Flask(__name__)


# In[3]:


import joblib
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates=float(request.form.get("rates"))
        model=joblib.load("regression")
        print(2)
        r1=model.predict([[rates]])
        print(3)
        model=joblib.load("Tree")
        print(4)
        r2=model.predict([[rates]])
        print(5)
        return(render_template("index.html",result1=r1,result2=r2))
        
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




