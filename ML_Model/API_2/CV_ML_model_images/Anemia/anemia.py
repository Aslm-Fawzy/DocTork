#!/usr/bin/env python
# coding: utf-8

# In[63]:


import cv2
import pytesseract
import re
import numpy as np
import pandas as pd
import joblib
import easyocr

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


def predict_image(path):
    keywords = ['HB', 'MCV', 'MCH', 'Gender']
    try:

        try:

            img = cv2.imread(path)
            # Convert the image to gray scale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ocr_output = pytesseract.image_to_string(img_gray)
            dictionary = {}
            for line in ocr_output.split('\n'):
                if 'MCHC' in line:
                    continue

                for keyword in keywords:
                    try:
                        try:
                            if re.search(keyword, line, re.IGNORECASE):
                                if '=' in line:
                                    list_ = line.split('=')
                                    list_ = str(list_)
                                    result = re.search(
                                        '\d+\.{0,1}\d*', list_).group()
                                    dictionary[keyword] = float(result)
                                    break
                                elif ':' in line:
                                    list_ = line.split(':')
                                    list_ = str(list_)
                                    result = re.search(
                                        '\d+\.{0,1}\d*', list_).group()
                                    dictionary[keyword] = float(result)
                                    break

                            elif re.search('Male', line):
                                dictionary['Gender'] = 'Male'
                                break

                            elif re.search('Female', line):
                                dictionary['Gender'] = 'Female'
                                break
                        except:
                            if re.search(keyword, line, re.IGNORECASE):
                                list_ = str(line.split())
                                result = re.search(
                                    '\d+\.{0,1}\d*', list_).group()
                                dictionary[keyword] = float(result)
                                break
                    except:
                        continue

            # return dictionary["HB"]
            model = joblib.load(
                'DocTork-master/ML_Model/API_2/CV_ML_model_images/Anemia/Model/GradientBoostingModel(anemia-m,f-3features)_2.h5')
            features = list(model.feature_names_in_)

            data_dic = {}
            data_dic[features[0]] = dictionary["HB"]
            data_dic[features[1]] = dictionary["MCH"]
            data_dic[features[2]] = dictionary["MCV"]
            if dictionary['Gender'].startswith('F'):
                data_dic[features[3]] = 0
            elif dictionary['Gender'].startswith('M'):
                data_dic[features[3]] = 1
            custom_data = pd.DataFrame(data=[data_dic])
            output = model.predict(custom_data)[0]
            correct_predication_name = {
                'Anemia': 'Normal Anemia',
                'Good': 'Normal ',
                'Micro': 'Microcytic Anemia',
                          'Macro': 'Macrocytic Anemia',
                          'CML': 'Chronic Myelogenous Leukemia',
                          'Acute L': 'Acute Lymphoblastic Leukemia',
                          'HyperTyroid':  'Hyperthyroidism',
                          'Hypothyroid': 'Hypothyroidism',
                          'Other Thyroid Abnormalities':  'Other Thyroid Abnormalities',
                          'Normal':  'Normal ',
                          'Hyperuricosuria (Gout)': 'Hyperuricemia (Gout)',
                          'Hypouricosuria ':  'Hypouricemia',
                          'Jaundice':  'Jaundice',
                          'Diabetic': 'Diabetes',
                          'Pre Diabetic': 'Prediabetes',
                          'Hypoglycemia': 'Hypoglycemia',
                          'Prostatic_Cancer':  'Prostatic Cancer',
                          'Rheumatiod_Arthities': 'Rheumatoid Arthritis',
                          'Hypoparathyroid': 'Hypoparathyroidism',
                          'Another Disease':  'Another Disease',
                          'Hyperparathyroid': 'Hyperparathyroidism',
                          'Acute  L or CML':  'Acute Lymphoblastic Lekumia and Chronic Myelogenous Lekumia',
                          'Good':  'Normal',
                          'Normal': 'Normal'}

            patient_output_disease = correct_predication_name[output]
            return patient_output_disease

        except:
            # this needs to run only once to load the model into memory
            reader = easyocr.Reader(['en'], gpu=False)
            img = path
            output = reader.readtext(img, detail=1)
            dictionary = {}
            for i in output:
                probability = i[-1]

                if probability >= 0.6:
                    text = i[1]

                if 'MCHC' in text:
                    continue

                for keyword in keywords:
                    try:
                        try:
                            if re.search(keyword, text, re.IGNORECASE):
                                if '=' in text:
                                    list_ = text.split('=')
                                    list_ = str(list_)
                                    result = re.search(
                                        '\d+\.{0,1}\d*', list_).group()
                                    dictionary[keyword] = float(result)
                                    break
                                elif ':' in text:
                                    list_ = text.split(':')
                                    list_ = str(list_)
                                    result = re.search(
                                        '\d+\.{0,1}\d*', list_).group()
                                    dictionary[keyword] = float(result)
                                    break

                            elif re.search('Male', text):
                                dictionary['Gender'] = 'Male'
                                break

                            elif re.search('Female', text):
                                dictionary['Gender'] = 'Female'
                                break
                        except:
                            if re.search(keyword, text, re.IGNORECASE):
                                list_ = str(text.split())
                                result = re.search(
                                    '\d+\.{0,1}\d*', list_).group()
                                dictionary[keyword] = float(result)
                                break
                    except:
                        continue
                model = joblib.load(
                    'DocTork-master/ML_Model/API_2/CV_ML_model_images/Anemia/Model/GradientBoostingModel(anemia-m,f-3features)_2.h5')
                features = list(model.feature_names_in_)

                data_dic = {}
                data_dic[features[0]] = dictionary["HB"]
                data_dic[features[1]] = dictionary["MCH"]
                data_dic[features[2]] = dictionary["MCV"]
                if dictionary['Gender'].startswith('F'):
                    data_dic[features[3]] = 0
                elif dictionary['Gender'].startswith('M'):
                    data_dic[features[3]] = 1
                custom_data = pd.DataFrame(data=[data_dic])
                output = model.predict(custom_data)[0]
                correct_predication_name = {
                    'Anemia': 'Normal Anemia',
                    'Good': 'Normal ',
                    'Micro': 'Microcytic Anemia',
                    'Macro': 'Macrocytic Anemia',
                    'CML': 'Chronic Myelogenous Leukemia',
                    'Acute L': 'Acute Lymphoblastic Leukemia',
                    'HyperTyroid':  'Hyperthyroidism',
                    'Hypothyroid': 'Hypothyroidism',
                    'Other Thyroid Abnormalities':  'Other Thyroid Abnormalities',
                    'Normal':  'Normal ',
                    'Hyperuricosuria (Gout)': 'Hyperuricemia (Gout)',
                    'Hypouricosuria ':  'Hypouricemia',
                    'Jaundice':  'Jaundice',
                    'Diabetic': 'Diabetes',
                    'Pre Diabetic': 'Prediabetes',
                    'Hypoglycemia': 'Hypoglycemia',
                    'Prostatic_Cancer':  'Prostatic Cancer',
                    'Rheumatiod_Arthities': 'Rheumatoid Arthritis',
                    'Hypoparathyroid': 'Hypoparathyroidism',
                    'Another Disease':  'Another Disease',
                    'Hyperparathyroid': 'Hyperparathyroidism',
                    'Acute  L or CML':  'Acute Lymphoblastic Lekumia and Chronic Myelogenous Lekumia',
                    'Good':  'Normal',
                    'Normal': 'Normal'}

                patient_output_disease = correct_predication_name[output]
                return patient_output_disease
    except:
        print('Your uploaded image can\'t be detected')
        print('-----'*10)
        model = joblib.load(
            'DocTork-master/ML_Model/API_2/CV_ML_model_images/Anemia/Model/GradientBoostingModel(anemia-m,f-3features)_2.h5')
        features = list(model.feature_names_in_)
        return 'Your uploaded image can\'t be detected\n \t Enter Manually the Following Please : ', features[:-1]

# In[ ]:
