#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        Income = float(request.form.get("Income"))
        Age = float(request.form.get("Age"))
        Loan = float(request.form.get("Loan"))
        print(Income, Age, Loan)
        model = joblib.load("XGBoost")
        pred = model.predict([[Income, Age, Loan]])
        s = "The credit card default is " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Try Again"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




