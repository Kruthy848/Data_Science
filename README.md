Sales Revenue Prediction API

This project is a Machine Learning powered Flask API that predicts Sales Revenue based on product category, income level, price, discount percent, units sold, and cost.

The model is trained using a dataset with product categories such as Apparel, Beauty, Electronics, and Homegoods.
Features

Predict sales revenue with ML model

REST API built using Python Flask

Supports multiple product categories

Pre-trained model loaded automatically

Easy integration with Web, Mobile, Power BI, etc.
├── Server.py                   # Flask API Server
├── util.py                     # Utility functions to load model and predict
├── artifacts/
│   ├── columns.json            # Feature & category column metadata
│   └── Sales_Optimization.pickel   # Trained ML Model
└── README.md                   # Project documentation
