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
        model1 = joblib.load("Decision Tree")
        pred1 = model1.predict([[Income, Age, Loan]])
        s = "The credit card default is " + str(pred1) + "based on Decision Tree."
        
        model2 = joblib.load("XGBoost")
        pred2 = model2.predict([[Income, Age, Loan]])
        s1 = "The credit card default is " + str(pred2) + "based on XGBoost."
        
        model3 = joblib.load("Logistic Regression")
        pred3 = model3.predict([[Income, Age, Loan]])
        s2 = "The credit card default is " + str(pred3) + "based on Logistic Regression."        
        
        model4 = joblib.load("Neural Network")
        pred4 = model4.predict([[Income, Age, Loan]])
        s3 = "The credit card default is " + str(pred4) + "based on Neural Network."
        
        model5 = joblib.load("Random Forest")
        pred5 = model5.predict([[Income, Age, Loan]])
        s4 = "The credit card default is " + str(pred5) + "based on Random Forest."        

        return(render_template("index.html",  result = s,
                                              result1 = s1,
                                              result2 = s2,
                                              result3 = s3,
                                              result4 = s4))
    else:
        return(render_template("index.html", result = "Try Again"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




