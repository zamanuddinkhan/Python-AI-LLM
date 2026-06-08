# Verify Python Version
py --version

# Verify pip Version
py -m pip --version

# Upgrade pip
py -m pip install --upgrade pip

# Create Virtual Environment for Libraries Like: [OpenAI, LangChain, LangGraph, CrewAI, FastAPI, Uvicorn]
py -m venv venv

# Activate Virtual Environment (CMD)
venv\Scripts\activate

# Deactivate Virtual Environment After Use
deactivate

# To Install It
py -m pip install numpy
py -m pip install pandas
py -m pip install matplotlib
py -m pip install seaborn
py -m pip install scikit-learn 
py -m pip install jupyter
py -m pip install openai
py -m pip install langchain
py -m pip install langgraph
py -m pip install crewai
py -m pip install fastapi
py -m pip install uvicorn
py -m pip install python-dotenv

# To Verify It
py -m pip show numpy
py -m pip show pandas
py -m pip show matplotlib
py -m pip show seaborn
py -m pip show scikit-learn 
py -m pip show jupyter
py -m pip show openai
py -m pip show langchain
py -m pip show langgraph
py -m pip show crewai
py -m pip show fastapi
py -m pip show uvicorn
py -m pip show python-dotenv

# To See All Installed Packages
py -m pip list

# To Check for Outdated Packages
py -m pip list --outdated

# To Upgrade a Package
py -m pip install --upgrade numpy

# To Save Project Dependencies
py -m pip freeze > requirements.txt

# To Install Dependencies from requirements.txt
py -m pip install -r requirements.txt

# Uninstall a Package
py -m pip uninstall numpy

# Install Specific Version
py -m pip install numpy==2.3.0

# Upgrade All Packages (manual process)
py -m pip list --outdated