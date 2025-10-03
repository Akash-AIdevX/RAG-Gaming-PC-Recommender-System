# RAG-Gaming-PC-Recommender-System

## Goals of the Project
- Help users find the best Gaming PC within their budget.  
- Allow users to search using natural language queries, e.g., "Recommend me RTX 3060 gaming PC under 1.3 lakhs".  
- Build an AI-powered recommender system that provides personalized results quickly.  

## Process
1. Collected and cleaned dataset of gaming PCs and their specifications (CPU, GPU, RAM, Storage, Price, etc.).  
2. Implemented a Retrieval-Augmented Generation (RAG) pipeline in Python to handle natural language queries.  
3. Integrated with Django backend for handling user requests.  
4. Designed a frontend UI with HTML, CSS, and JavaScript for an interactive and user-friendly interface.  
5. Connected backend and frontend using REST API so results update dynamically.  

## Features
- Users can type free-text queries like "gaming PC with RTX 3080 under 1 lakh".  
- Budget filtering in INR.  
- Displays multiple PC recommendations with name, specs, and price.  
- Simple and clean search interface for a professional look.  
- Scalable system – new PCs/specs can be added easily to the database.  

## Demo
[Demo Link](https://drive.google.com/file/d/1k_9dsH-bV7r9P4KN4R119GEI8TFvnfh3/view?usp=sharing)

## Skills Used
- Python  
- Django  
- RAG (Retrieval-Augmented Generation)  
- Natural Language Processing (NLP)  
- HTML  
- CSS  
- JavaScript  
- REST API  
- Machine Learning (Recommender Systems)  
- Data Processing  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Akash-AIdevX/RAG-Gaming-PC-Recommender-System.git
cd RAG-Gaming-PC-Recommender-System
```
2.Requirements.txt
```txt
Django>=4.2
djangorestframework>=3.20
numpy>=1.25
pandas>=2.1
faiss-cpu>=1.7.4
sentence-transformers>=2.2.2
scikit-learn>=1.3
torch>=2.1
transformers>=5.3
python-dotenv>=1.1
```
