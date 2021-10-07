import pandas as pd
import numpy as np

json = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}, {"Gender": "Male", "HeightCm": 161, "WeightKg":85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77}, {"Gender": "Female", "HeightCm": 166,"WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
data = pd.DataFrame(json)
d = {}


def table(x):
    if x < 18.4:
        d['category'] = 'Underweight'
        d['health_risk'] = 'Malnutrition'
    elif 18.5 < x < 24.9:
        d['category'] = 'Normal weight'
        d['health_risk'] = 'Low risk'
    elif 25 < x < 29.9:
        d['category'] = 'Overweight'
        d['health_risk'] = 'Enhanced risk'
    elif 30 < x < 34.9:
        d['category'] = 'Moderately obese '
        d['health_risk'] = 'Medium risk'
    elif 35 < x < 39.9:
        d['category'] = 'Severely obese'
        d['health_risk'] = 'High risk'
    else:
        d['category'] = 'Very severely obese'
        d['health_risk'] = 'Very high risk'
    return d
try:
    """Calculating BMI"""
    data['BMI'] = np.where(data['HeightCm'], (data['WeightKg'] * 10000 / data['HeightCm'] ** 2), 0)

    """Using Iterative method"""
    # for i in range(len(data)):
    #      data.loc[i, "BMI"] = data.loc[i,'WeightKg'] * 10000 / data.loc[i,'HeightCm'] ** 2

    """Finding Category and Health risk based on table"""
    for i in range(len(data)):
        data.loc[i, "category"] = table(data.loc[i, "BMI"])['category']
        data.loc[i, "Health Risk"] = table(data.loc[i, "BMI"])['health_risk']

    oweight = np.where(data['category'] == "Overweight", 1, 0) #calculation of overweight people

    data.to_json("new_json.json")  # Creates a new JSON with added column names
    data.to_csv("updated.csv")
    print(data.to_string())
    print("Total number of overweight people:", sum(oweight))
except:
    print("Error While Performing Operation")