# chetak - A Natural Disaster Prediction model
## Contents
1. Problem Statement<br>
2. Solution Strategy<br>
3. Dependencies<br>
4. Commands to run chetak<br>
## Problem Statement
Natural disasters pose a significant threat to human lives, infrastructure, and the environment. Timely prediction and identification of these disasters are crucial for effective disaster management and mitigation. However, existing prediction systems often lack accuracy, leading to inadequate preparedness and response efforts. Therefore, there is a pressing need to develop an advanced natural disaster prediction system that leverages AI algorithms and utilizes environmental data to provide accurate and timely warnings for disasters such as hurricanes, floods, wildfires, and earthquakes. This system aims to benefit various stakeholders, including government agencies, emergency management organizations, first responders, and affected communities, by enhancing their ability to prepare for and respond to natural disasters. By improving prediction accuracy and enabling proactive measures, the system aims to minimize the loss of life, damage to infrastructure, and environmental impact caused by natural disasters.
<br>
## Solution Strategy
The idea is to create a cloud-based AI platform that integrates data from various sources, applies machine learning algorithms for natural disaster prediction, and provides real-time alerts and visualizations. The platform would include components for data ingestion, preprocessing, and feature engineering. It would also have a repository of machine learning models specific to each type of natural disaster. The platform would allow for model training and optimization, real-time prediction and alerting, and a user-friendly interface with interactive visualizations. The scalable infrastructure and security measures would ensure the platform's efficiency, reliability, and protection of sensitive data.
<br>
## Dependencies
python3<br>
numpy<br>
pandas<br>
matplotlib<br>
scikit-learn<br>
seaborn<br>
tensorflow<br>
os<br>
opencv<br>
albumentations<br>
## Commands to run chetak
~~~~
Creating the environment:

$bash Anaconda-latest-Linux-x86_64.sh
$conda create -name env1
$conda activate env1
$conda install jupyter

Installing Dependencies:

$sudo apt install python3
$sudo apt install python3-pip
$pip install numpy
$pip install pandas
$pip install matplotlib
$pip install scikit-learn
$pip install seaborn
$pip install tensorflow
$pip install albumentations
$pip install opencv-python
$git clone https://github.com/vatika17/chetak.git
$cd chetak
$jupyter notebook
Access each notebook and run each cells.
~~~~
