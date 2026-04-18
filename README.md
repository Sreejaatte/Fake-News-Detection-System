#Fake-News-Detection-System
Production-ready NLP-based Fake News Detection API using FastAPI, TF-IDF, and ML models with Docker and CI/CD

Fake News Detection ML API

A production-ready machine learning system for detecting fake news using Natural Language Processing (NLP) techniques. The system is designed with a scalable architecture and deployed as a REST API for real-time inference.

Overview

This project implements an end-to-end machine learning pipeline for fake news classification. It covers the complete lifecycle:

- Data preprocessing and feature engineering
- Model training and evaluation
- API development for inference
- Containerization and CI/CD integration

The system is designed to simulate real-world ML deployment scenarios.

Problem Statement

Fake news detection is a critical challenge in modern information systems. This project aims to classify news articles as **FAKE** or **REAL** using machine learning models trained on textual data.

Features

- End-to-end NLP pipeline (preprocessing → training → inference)
- REST API for real-time predictions
- Modular and scalable project structure
- Dockerized deployment
- CI/CD pipeline with automated testing
- Logging and error handling for production readiness

Model Details

- Feature Extraction: TF-IDF Vectorization  
- Algorithms: Logistic Regression / Naive Bayes / Linear Models  
- Evaluation Metrics: Accuracy, Precision, Recall  
- Achieved Accuracy: ~92%  

Tech Stack

- **Language:** Python  
- **ML Libraries:** Scikit-learn, Pandas, NumPy  
- **API Framework:** FastAPI  
- **Deployment:** Docker  
- **CI/CD:** GitHub Actions  
- **Tools:** Git, Linux  
