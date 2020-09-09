# IoTData-Realtime-Ingestion-Inference  
Developing a ML model to achieve value-driven business outcomes is challenging.  
This is especially true for IoT applications.  
Due to the high temporal data resolution and continuously changing IoT Thing status, the fine-tuned ML model needs to be retrained regularly to adapt to such changes.  
In the first two repositories (https://github.com/Julia-Bobo-Hu/Automated-Historian-IoT-Data-Exploration) and (https://github.com/Julia-Bobo-Hu/Automated_ML_training_IoTNotebook),  
I demoed how to leverage IoT Analytics platform to automate the first stage of the IoT analytics virtuous cycle:  (1) Automate Data Exploration and AI Model Building.  
For the second stage, in this repository, I will demonstrate the solution for second part of the virtuous cycle of IoT ML:  
(2) IoT Data Real-time Ingestion and ML Model Inference.  
With efficient AWS managed IoT Analytics platform, these two parts are mutually complementary and can produce natural synergy.  

## Step 1: A walk through of the high-level solution architect for Real-time IoT data ingestion and inference:

![alt text](https://github.com/Julia-Bobo-Hu/Automated-Historian-IoT-Data-Exploration/blob/master/images/Step1_architecture_revised_batch_method.png?raw=true)