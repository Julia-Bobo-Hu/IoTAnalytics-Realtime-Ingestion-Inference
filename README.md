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

![alt text](https://github.com/Julia-Bobo-Hu/IoTAnalytics-Realtime-Ingestion-Inference/blob/master/images/highlevel_architect.png?raw=true)

This Real-time IoT Analytics solution still use three AWS managed services as backbones. These three services are: IoT Analytics, Containerized IoT Notebook and QuickSight.
The biggest difference between this architect compared with the phase I historian data exploration architect, is that it used IoT Topic to subscribe to the messages sending from IoT Things.
Then IoT Topic rule is used to select data. IoT core is used to stream real-time data to IoT Analytics platform.

The IoT Thing, IoT rule and IoT topics are all provisioned by using the CloudFormation template. There are two cloudformation yaml files in "Cloudformation" folder of this repository.
The first yaml file: "jh-check-ride-iot-analytic-inference" will provision AWS data ingestion resources for 4 types of smart meters (electricity, stream, cold water and hot water).
These 4 smart meters are distributed in 1449 buildings across 16 cities. The timestamp resolution is one reading/ minute. For BI dashboard purpose, two weeks of meter readings are used as input data.
In this yaml file, 4 IoT Things, IoT topic rules, IoT analytic channel, pipeline, datastore and dataset resources will be provisioned with this Cloudformation.
This cloudformation file will also provision necessary roles for different AWS services having correct access. E.g. IoT topic rules needs to access IoT channel, IoT dataset needs S3 write access to output IoT dataset. 

  