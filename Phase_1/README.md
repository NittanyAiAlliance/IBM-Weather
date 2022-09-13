
Headline: AI helps in better predicting hurricanes, says Penn State’s Nittany AI team in collaboration with IBM  

 

INTRODUCTION 

In a new effort to improve the seasonal forecasting of tropical cyclone activity in the Atlantic Ocean, a team with Penn State’s Nittany AI Alliance is proud to announce that it is collaborating with IBM to develop a new prediction model.  

Tropical cyclones, especially hurricanes, are among nature's most powerful and destructive storms. They are responsible for extensive economic and humanitarian impacts, causing nearly $1 trillion in damages, about half of all weather-related disaster damages, and nearly 7,000 deaths in the United States alone since 1980.  

Considering these impacts, much effort has been focused on producing and improving seasonal outlooks of tropical-cyclone activity for the Atlantic Ocean basin.  These outlooks have had varying levels of skill, with some successes, but a major shortcoming across nearly all seasonal forecast models is under-predicting activity in the most active hurricane seasons, such as the 2005, 2020, and 2021 seasons.  This shortcoming can have major consequences when expectations by local/state governments and the public are too low with respect to the actual severity of the season, resulting in under-preparedness for catastrophic storm events.  

Unlike prior models, the current model leverages deep learning, a form of artificial intelligence, to understand at a deeper level the relationships among various climate state variables that are thought to have skill in predicting the amount of seasonal tropical cyclone activity. After exploring RNN, CNN and other neural network structures, the Penn State team determined that a CNN (convolutional neural network) provided the best results in terms of accurate prediction.  

In addition to the existing variables that are known to provide skill to the forecast (such as El Nino, North Atlantic Oscillation, and sea surface temperatures in the main development region), we examined sea surface height (SSH), zonal and meridional ocean surface stress (TAUX and TAUY), and salinity. Special attention was given to making sure that the model could accurately predict above active seasons such as the 2005, 2020, and 2021 seasons. This is further discussed in the Convolutional Neural Network section. 

OBTAINING DATA 

Original Dataset 

The Columbia IRI DODS/OpenDat URL for the sea surface height data was downloadable. However, this was not the case with the temperature and salinity data. We could not read the data with the OpenDat URLs or do a bulk download at the beginning. 

The IRI faculty at Columbia have stated that we should not use the DODS/OpenDat until further notice but, rather, download the  files, which were in NetCDF format, then open them locally. Unfortunately, there is a size limit, so we were unable to download the entire dataset all at once. The maximum amount of data obtainable in one call was 1 years' worth. 

 Simple Ocean Data Assimilation (SODA) Dataset 

We were seeking more recent data so that we could make a prediction for 2022 by the end of the semester. Once IBM provided us with information about temperature and salinity data sourced from NOAA’s Physical Science Laboratory, we noticed that the data were more recent but not in DODS/OpenDat format. There was a total of 42 data files (years 1980-2022) for both salinity and temperature. In that case, downloading each file was not the ideal thing to do, so IBM recommended that we use FTP (File Transfer Protocol) to obtain the files instead of downloading each file and opening them locally. As soon as they recommended FTP, we produced the idea of researching ways to download files by FTP in Python and then merge all the files into one file afterwards. In Python, we used the ftplib (FTP Library) module to FTP all the files. The purpose of FTP is to transfer between computers in a network, and ftplib implements the client side of FTP protocol. The process for FTP protocol we used included importing the necessary modules, specifying the URL and directory, creating a folder for the salinity and temperature data, and writing all the files from NOAA’s Physical Science Laboratory to the salinity and temperature folders we created. After following FTP protocol, we merged both files, wrote them into single NetCDF files, then created a pandas data frame for them and saved them to csv files.  

Pros of using a larger dataset 

The more data that is available, the more accurate predictions that can be made. In our case, we needed both recent data as well as past data to make an accurate prediction for the current year of 2022.  

Difficulties in Obtaining Datasets 

Few websites offer data URLS in DODS/OpenDat format. The advantages of the DODS/OpenDat format are that it  contains all the data needed for data manipulation purposes and we would not need to download each file and open them locally. If there were databases that offered recent salinity and temperature data in DODS/OpenDat format, we would not be required to use FTP then merge all data files into one file.  

XGBOOST MODEL 

In the beginning, the team focused on creating small Neural Networks (3-4 Neuron) and XGBoost Trees. Using these approaches, results similar to the current industry standard were obtained. The problem with this approach was the inability to predict accurately the number of named storms in the outlier years (e.g., 2005, 2020, 2021). 

After training and hyper tuning our model, the above feature weights and relative importance were established. This data set was extremely small, which limited the scope of machine learning tactics we could use. These outlier years are the most impactful and often cause the most damage and deaths, so the team viewed it as essential for the model to be able to predict these outlier years. To achieve this, a larger data set was acquired: this being the “Simple Ocean Data Assimilation” dataset from NOAA's Physical Science Laboratory.  

 

 

Transition from XGBoost to CNN 

We tried to build a separate model for extreme years since the Xgboost model works well on normal years. To do that, we first tried to classify the extreme years out of all years via SVR and Xgboost. However, after applying statistical analysis on existing datasets (DBSCAN), we believed that the information in the datasets is exhausted. It is not sufficient to provide enough information to classify the extreme year. On the other hand, XGboost did not produce a satisfying result toward predicting all years together because like previous models, it severely underpredicted the hurricane counts for abnormal years. As a result, new data and a new model was introduced to first classify an upcoming hurricane season into an extremely active year/normal year. 

Convolutional Neural Network Models 

To capture features from multiple data (SSH, temperature, SST) within the same time units, we applied Convolutional Neural Network to our task. CNN is known for its capability in processing image data, but some typical examples also proved its advantage in handling spatial temporal data. The data from the SODA dataset are laid out in spatial and temporal 2D/3D arrays by constructing each year’s April data as an image, with longitude and latitude of the chosen feature at that time as pixels inside the image. Thus, the CNN model can process our data, just like our processing of image data. This allowed the team to take a unique approach to utilize all the information we must make predictions. The structure of the CNN model is obtained from finetuning the initial model structure from Keras. Accuracy is used to be the evaluation metrics with learning epoch set to 15.  

 The CNN model outputs the abnormal years. These outputs are then fed into a  series of XGBoost models like the original models the team worked with to make predictions of the number of hurricanes accordingly. 

 This model design allows for the removal of outliers before training the xgboost model. This is much more efficient because XGBoost is good at making a general model that fits the full dataset, so typically outliers are not captured, but when the data set is divided into two separate datasets and two separate XGBoost models are trained, there is no longer any outliers relative to the individual datasets. 

 Insights into CNN application on SST Data 

The initial performance of the CNN model for temperature SSH data was poor when the threshold for outliers is set to be larger than 15 and the data is highly imbalanced. Additionally, the number of missing values is more than the number of existing values for all years. We used NearestNDInterpolate method to fill missing values and used binary focal cross entropy as our loss function. The new loss function provided an essential weight adjustment option for inputs. We thus avoid imbalanced dataset issue.  

In result, the model captured the key features of the dataset, minimized the validation loss to 0.0683, and the distribution of the result compared to the hurricane count distribution in each year is significantly similar (with P-value less than 0.05 from a chi-square test). We tested our model for both 2020 and 2005 data, and the results outperformed most of the previous predictions from other sources. 

One remaining problem in our model is that the sigmoid layer would squeeze the output probability to a certain range. All variations are compressed to that range, and we have not yet figured out how that range changes. However, this does  not affect our model because we can always rescale it to the range we desired. 


2022 Prediction and Results 

Using comparisons in the distribution of storms vs prediction label from the CNN Model, we were able to generate an estimated range of 16-24 named storms. The mean of this range is 20 named storms for the 2022 season. 

Difficulties obtaining current data prevented us from using the XGboost models for a 2022 prediction. Here are some predictions made in prior years using both the XGboost model and the CNN.  


These two years prove that when combining the XGBoost model and CNN, outlier years can be captured alongside normal years. These two predictions were closer than any other prediction made before these seasons occurred.  

Using the XGboost model alongside the CNN model allows users to understand how the prediction is made given the nature of how gradient boosted trees work. However, when using only the CNN approach, the model is much more of a black box where the relationships between climate state variables (and, by extension, the mechanism behind the predictability) are not well understood. 

CONCLUSION 

With this new model, the team improved the prediction skill for seasonal tropical cyclone activity in the Atlantic, especially in those seasons that might have the greatest number of cyclones. Their prediction for the 2022 season is 20, and they will be providing regular updates on their work throughout the season. 

The future scope of this project includes:  

1. Including multiple features into the CNN rather than purely SST to better increase our accuracy in predicting heavy hurricane seasons 

2. Obtaining current data which can be used to make real time predictions with the XGBoost models 

3. Running categorical validation to see how well model runs on major vs non-major named storms 

 