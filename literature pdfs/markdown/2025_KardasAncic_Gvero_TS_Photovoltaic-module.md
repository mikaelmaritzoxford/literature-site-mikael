Kardaš Ančić, D., *et al.*: Photovoltaic Module Temperature Estimation ... <u>THERMAL SCIENCE: Year 2025, Vol. 29, No. 5A, pp. 3367-3376 3367</u>

# PHOTOVOLTAIC MODULE TEMPERATURE ESTIMATION UNDER VARIOUS ENVIRONMENTAL CONDITIONS

# Preliminary Experimental and Theoretic Study

by

## Danijela KARDAŠ ANČIĆ

***a**** ***, Mirko S. KOMATINA*** ***b*** ***, and Petar M. GVERO*** ***a***

a Faculty of Mechanical Engineering, University of Banja Luka, Banja Luka, Bosnia and Herzegovina b Faculty of Mechanical Engineering, University of Belgrade, Belgrade, Serbia Original scientific paper [https://doi.org/10.2298/TSCI241224049K](https://doi.org/10.2298/TSCI241224049K)

*The most of the solar radiation that reaches PV (module is transformed into the* *heat and partly is transformed into electricity. This causes an increment in the* *PV module temperature which leads to a decrease in its electrical efficiency. PV* *module temperature significantly depends on environmental factors such as solar* *radiation, air temperature and wind velocity. An overview of different empirical* *models for the estimation of PV module temperature using measured weather data* *is presented. The obtained results were compared with the measured data of the* *PV module temperature at the experimental set-up with the aim of preliminary* *analyzes which empirical model is optimal for analyzed geographical and climate* *location. Empirical models were evaluated into two categories: models that take* *into account wind velocity and those that do not. Analyses show that average tem-* *perature difference between measured values of the PV module temperature and* *the values predicted by the empirical models that do not consider wind velocity is*

*13.37 °C and for models that do is 7.40 °C. This proves that is very important to* *consider the effect of wind on PV module temperature. Analyzing obtained data,* *it can be concluded that temperature of the PV module is above 25 °C for whole* *measured period with significant impact of meteorological parameters.* Key words*: PV module temperature, theoretical models,* *experimental study, meteorological data*
## Introduction

Worldwide yearly renewable capacity increases expanded by nearly 50% in 2023, the quickest development rate in the past two decades [1]. The EU is proposing to increment the target in the renewable energy directive to 45% by 2030 [2]. Over the coming five years, a few renewable energy breakthroughs are anticipated to be accomplished [1]: in 2025, RES will become the largest source of electrical energy generation; solar PV will surpass nuclear elec- tricity generation in 2025 and 2026 and in 2028, RES will account for more than 42% of global electricity generation, with the share of wind and solar PV raising to 25%. Despite the challenges associated with the development and implementation of re- newable energy systems, solar energy is one of the most favorable renewable energy resources all around the world [1-4]. Solar energy gives numerous advantages like extraordinary poten- tial, low prices per individual system, near zero or decreased GHG emissions, no noise emis-

* Corresponding author, e-mail: danijela.kardas@mf.unibl.org

<u>3368 THERMAL SCIENCE: Year 2025, Vol. 29, No. 5A, pp. 3367-3376</u>

sion and no require for fossil fuels [5]. The PV technology stands out in solar energy utilization because of its better potential for performance enhancement, cost decline and development of subsystems [6]. With the REPowerEU plan, EU Solar Energy Strategy want to bring nearly 600 GW of solar photovoltaic by 2030 [7]. Solar PV technology will dominate solar power generation between now and 2050 [8]. Solar PV technology is a quickly developing area that can be applied to both building integration and inaccessible areas [9]. However, at this time, PV technology still has higher costs in comparison traditional power production technologies [10]. In order to achieve this, development of PV technology is being done continuously to make it competitive in the market with traditional energy production from fossil fuels. In order to com- pare the characteristics of PV modules from different manufacturers and different material of cells under equal conditions, standard test conditions (STC) were defined. The STC define that the PV module is performed and testing at a irradiance of 1000 W/m², air mass AM 1.5 (defined by standards ISO 9845-1:2022 and ASTM G173-03) and that the temperature of the PV cells is 25 °C. Under these conditions, all the operating parameters of the PV panel are defined. In real operating conditions, the irradiance is generally lower and the temperature of the PV cells is higher than the values defined for STC. Irradiance varies due to the meteorological parameters such as weather, geographical location, seasonal changes, and period of the day and position of the sun in the sky. As the irradiance drops below the standard 1000 W/m², the *I-V* charac- teristic of the module changes. Temperature have a significant impact on the performance of PV modules. The PV cell temperature greater than 25 °C negatively affect the PV electrical efficiency [11, 12]. This is a major disadvantage of solar PV technology. When the tempera- ture of the PV cells exceeds 25 °C, the electrical efficiency decrease at a rate of 0.4-0.65%/°C [13, 14]. Typical PV module transform 6%-20% of the solar energy into electricity while the rest is transformed into heat, depending on the type of PV cell technology and the meteorological conditions [15-17]. Environmental factors have the significant impact on the operation of PV systems. The most important environmental factors are: solar irradiance, air temperature, wind, dust accumulation, soiling, and effect of shading [18-23]. The types of solar cell technology used has also influence the electrical performance of the PV module. It was performed a study to analyze the performance of monocrystalline, polycrystalline, and thin film PV module over a year in Amman, Jordan [17]. The results showed that the annual energy yield for the monocrys- talline, polycrystalline and thin film PV modules, had the deviation of 15.4%, 17%, and

19.5%, respectively. Different mounting systems can significantly affect PV module tempera- ture and system efficiency. This is due to air-flow and ventilation around the PV module, which can influence the heat dissipation of the panel and the module temperature [18].
## Theoretical models for photovoltaic module temperature

In the literature, different models have been suggested for predicting PV cell tempera- ture [24]. The complexity of the models increases according to a number of parameters which are taking into account (ambient temperature, solar radiation, wind velocity, empirical coeffi- cients, and heat transfer parameters). To improve the research in this field, artificial intelligence methods were used such as artificial neural networks [25, 26], genetic programming [27], and machine learning [28]. Several correlations from the literature that describe the temperature distribution of PV module/cells will be analyzed in this paper, tab. 1. The analyzed correlations are the most frequently used in the literature and include those that were first developed in the field to some of the most recent ones. These correlations include the most relevant meteorolog- ical parameters for analyzing PV module temperature.

These correlations are empirical equations and they are based mostly on meteorological data. The temperature of the back surface of the photovoltaic module, *T*m, and the temperature of the photovoltaic cell, *T*c, can differ for high intensities of solar radiation [29]. At solar radiation of 1000 W/m², this temperature difference is typically 2-3 °C for flat-plate modules in an open- rack mount. For flat-plate modules with a thermally insulated back surface, this temperature difference can be neglected [30]. Given that for the analyzed location, the average daily solar radiation is less than 700 W/m², these differences were ignored and *T*c= *T*m= *T*PV was adopted. For all analyzed empirical models listed in tab. 1, thermal accumulation of the PV module is neglected. This means that in the change in the environmental factors (solar irradiation, air temperature and wind velocity), there is a sudden change of the temperature of the PV module calculated by the models. In order to investigate the influence of wind speed, empirical models were analyzed in two categories: models that take into account wind velocity and those that do not. Since any of the analyzed empirical models can not be used as general model for all geo- graphical areas and climate, because an own experimental installation was designed, construct- ed and built in order to determine empirical model that can be adopted for own geographical location and climate for PV module temperature estimation.

**Table 1. Analyzed empirical models for PV module temperature estimation from the literature**

|References|Empirical model||
|---|---|---|
|[31]|TT = 0.03 + G PV a T|Models that do not take into account the effect of wind velocity on the temperature|
|[32]|TT =+− 0.028 G 1 PV a T||
|[33]|TG = 0.0175( 300) − + 1.14( T 25) 30.006 −+of the photovoltaic module PV T a||
|[34]|TT = 0.031 + G PV a T||
|[30]|−− 3.47 0.0594 v T = TG + e PV a T|Models that do take into account the effect of wind velocity on the temperature of the photovoltaic module|
|[30]|() a + bv T = TG + e T PV a||
|[35]|0.32 TT = + PV a T + 2 v G 8.91||
|[36]|T = + 0.9458 TGv 0.0215 −+ 1.2376 2.0458 PV a T||

## Experimental set-up

An experimental installation was designed, constructed and built in order to be able to measure the temperature of PV module in real time taking into account relevant meteorological parameters such as air temperature, solar radiation and wind velocity, fig. 1. Experimental installation used for this study is located outside of the building of the Faculty of Mechanical Engineering in Banja Luka (44.46282 N, 17.11502 E) and the meteorological station is installed on the rooftop of the building. All meteorological data can be found on the website [https://www.wunderground.com/dashboard/pws/IBAN-](https://www.wunderground.com/dashboard/pws/IBAN-) JA1. The PV module chosen for the study is a monocrystalline type (SZ-100-36M) with a glass/cells/tedlar configuration. Technical specification of the PV module are given in tab. 2. The module temperature was measured by two PT100 thermocouple placed on the rear

**Figure 1. The different outdoor experimental facilities; (a) EASY – E4 –UC – 12 RC1 data**

**acqusition, (b) positions of thermocouples for measuring the PV module temeprature, and**

**(c) experimental set-up**
of the PV module in two points. These locations were chosen to determine a difference in the temperature distribution across the panel. Two diametrically different points were cho- sen for positioning the thermocouples, left corner down and upper right, fig. 1(c). The av- erage value of these two temperatures was used for further analysis. Accuracy of PT100 is ±(0.15 + 0.002 × |*T*|) °C for the range from – 50-300 °C. The panels were placed on a metal pillar. The reason for this is to ensure an undisturbed flow of wind around the panel and thus to obtain the most relevant data on its influence on the temperature of the panel.

**Table 2. Technical specification of the PV module**

|Standard test conditions AM = 1.5, E = 1000 W/m², T = 25 ℃ C||
|---|---|
|Nominal power|100 W|
|Cell type/efficiency|Monocrystalline 17.66%|
|Maximum power current, I mpp|5.41 A|
|Maximum power voltage, V mpp|18.50 V|
|Open-circuit voltage, V oc|22.50 V|
|Short-circuit current, I sc|5.92 A|
|Working temperature|– 40 ℃ to + 80 ℃|
|Module dimensions|1020 mm × 670 mm × 35 mm|

The datasets were collected in period of three days (July 15-17, 2023) from 9:45 a. m. to 3:55 p. m. with a 10 minutes recording interval and stored via EASY-E4-UC-12RC1 data ac- quisition. Month July was selected for these analysis as a warmest month in the year for analyzed geographical area. Measurements were performed three days in a row in order to obtain the most relevant data depending on changes in meteorological parameters. Meteorological data including solar radiation, ambient temperature and wind velocity were measured by the meteorological sta- tion Luft WS10. Technical data for meteorological station are given in tab. 3.

**Table 3. Technical specification of the meteorological station Luft WS10**

Air temperature PTC, – 40 to + 60 °C ( ±1.0 °C )

Irradiance Silicium – Pyranometer, 0 -1500 W/m² (±10 % or ±120 W/m²)

Wind velocity 0-40 m/s (±1 m/s or 5%)

## Results and discussion

Meteorological data including solar radiation, ambient temperature and wind velocity were used as input parameters for the analyzed theoretical models. Table 4 shows the maximum and minimum values of weather data recorded at the site under experimental investigations. The measurements showed that solar radiation, *G*, ambient temperature, *T*a, and wind velocity, *v*, ranged from 457-822.3 W/m², 34.8-40.8 °C, and 1.3-13.5 km/h, respectively. In general, fluctuations in environmental factors in the same day affect the accuracy of the PV module temperature results [11].

**Table 4. The maximum and minimum values of weather data recorded at the site under experimental study**

–2 –1

|Day||G [Wm]|T [°C]|v [kmh]|
|---|---|---|---|---|
|July 15, 2023|Maximum|822.3|37.9|10.3|
||Minimum|457|30.7|1.3|
|July 16, 2023|Maximum|810.4|39|13.5|
||Minimum|453.3|32.7|1.6|
|July 17, 2023|Maximum|806.7|40.8|9.3|
||Minimum|461|34.8|1.6|

*T* a

Daily average measured PV module temperature, average predicted PV module tem- perature by empirical models and average difference between them are given by tab. 5.

**Table 5. Daily average measured PV module temperature, average predicted**

**PV module temperature by theoretical models and average difference**

||July 15, 2023|July 16, 2023|July 17, 2023|Range||||
|---|---|---|---|---|---|---|---|
|Daily average measured PV module temperature [°C]|40.86 Daily average PV module temperature by theoretical models [°C]|42.43 Average difference [°C]|42.59 Daily average PV module temperature by theoretical models [°C]|Average difference [°C]|Daily average PV module temperature by theoretical models [°C]|Average difference [°C]||
|[31]|55.81|14.95|57.93|15.31|59.31|16.72|7|
|[32]|53.41|12.54|55.54|12.74|56.94|14.35|6|
|[33]|48.13|7.27|50.64|7.84|52.41|9.81|4|
|[34]|56.52|15.65|58.63|15.83|60.00|17.41|8|
|[30]|50.95|10.08|52.86|10.06|54.98|12.39|5|
|[30]|48.47|7.60|50.39|7.59|52.58|9.69|3|
|[35]|47.05|6.19|48.92|6.11|51.19|8.59|2|
|[36]|43.69|2.82|45.43|2.62|47.65|5.06|1|

As it can be seen in tab. 5. all empirical models give the temperature of the PV module above 25 °C for the whole measured period as well as the experimental data. It can be seen that all

models overestimated the operating temperature of the PV module. The maximum value of the average daily temperature difference between estimated and measured PV module temperature is

17.41 °C for Mondol model (day 17.7.2023.) and the minimum value is 2.62 °C for the model Kamuyu (day 16.7.2023.). Comparing measured and predicted values of the PV module tem- perature by the empirical models, it can be concluded that the Kamuyu model best predicts the PV module temperature for this experimental research and obtained meteorological data, tab. 5. Table 6 gives average values of meteorological data (air temperature, wind velocity and irradiance) for the whole period of measurement as well as daily average measured PV module temperature.
**Table 6. Average values of meteorological data for the whole period of**
 **measurement as well as daily average measured PV module temperature**
July 15, 2023 July 16, 2023 July 17, 2023 Daily average irradiance [Wm–2] 703.62 698.15 686.63

|Daily average measured air temperature [°C]|34.71|36.99|38.72|
|---|---|---|---|
|Daily average measured wind velocity [kmh|5.10|5.34|4.67|
|Daily average measured PV|40.86|42.43|42.59|

–1]

module temperature [°C]

As it can be seen in tab. 6, the highest measured PV module temperature correspond with the day with highest air temperature and the lowest wind velocity (day 17.7.2023.). The lowest measured PV module temperature correspond with the day with lowest air temperature and higher wind velocity (day 15.7.2023.). The solar irradiation values were relatively close through whole measured period. Figures 2-4 represent graphical presentation of analyzed mod- els for the estimation PV module temperature for the whole period of measurements as well as measured PV module temperature and measured meteorological data.

**Figure 2. Analyzed theoretical models for estimation of the**

**PV module temperature July 15, 2023** (*for color image see journal web site*)

From all analyzed theoretical models that do not take into account wind velocity, Mondol model predicts the highest PV module temperatures for the whole measured period and the lowest are by Laisner and Ang model. Analyzing these models, it can be concluded that they directly depend on the amount of solar radiation and air temperature. The diagrams of the

**Figure 3. Analyzed theoretical models for estimation of the PV module**

**temperature July 16, 2023** (*for color image see journal web site*)

**Figure 4. Analyzed theoretical models for estimation of the PV module**

**temperature July 17, 2023** (*for color image see journal web site*)

analyzed theoretical models follow the solar radiation distribution curve. Analyzing the models that take into account the influence of the wind, it is shown that these models give lower PV module temperature compared to the models that do not analyze it. The reason for this is that these models also consider heat losses by convection and radiation the environment due to the influence of the wind with different velocities. These models correspond with real conditions. Analyzing these models, King *et al*. [30] model predicts the highest temperatures of the pho- tovoltaic module for the whole measured period and the lowest are by Kamuyu *et al*. [36]. It can be seen that the maximum measured wind velocity correspond to a drop in the temperature of the PV module for all theoretical models but also for measured values for PV temperature, figs. 2-4. Daily distribution of solar radiation, air temperature, wind velocity and measured PV module temperature compared with results of Kamuyu model are given by fig. 5. As it can be seen in fig. 5., maximum value of measured PV module temperature correspond to the maximum daily solar irradiance and drop of wind velocity (around 1 p. m., fig. 5). As wind velocity rises PV module temperature decrease. This all confirms the influence of the wind on the convective cooling of the PV module. At the first part of the day, solar ra- diation, air temperature and PV module temperature rise. The PV module temperature curve is

following the solar radiation distribution curve with maximum and minimum values depending on wind velocity. It can be concluded that in the first part of the day, PV module temperature is influenced most by solar radiation and wind velocity. At the second part of the day (after 2 p.

m.) air temperature and wind velocity have bigger influence on PV module temperature then the solar radiation. It can been seen that measured PV model temperature and Kamuyu model have same minimum and maximum values in the same time of the day, fig. 5. This correspond with the previous conclusion that Kamuyu model best predicts PV module temperature for this experimental research, tab. 5.
**Figure 5. Measured PV module temperature on July 17, 2023 and**
 **results of Kamuyu model** (*for color image see journal web site*)
## Conclusion

Experimental research was performed to define empirical model for predicting PV module temperature for analyzed geographical and climate area. Performed analysis aimed to compare empirical models for prediction of the PV module temperature from literature with an own performed experimental results. Two groups of empirical models were considered: models that do not take into account wind velocity and models that do take. All analyzed models give their maximum values for PV module temperature for the same day and same time, 17.7.2023. around 2 p. m.. Measured PV module temperature for this day and time is 45.25 °C. On this day and time is measured highest average daily air temperature 38.72 °C and lowest average daily wind velocity 4.67 km/h comparing to the whole period of measurements. Results show that models that do not consider wind velocity have higher temperature difference between estimat- ed and measured PV module temperature. This is because real conditions and convective cool- ing are not taken into account. Comparing the measured values of the PV module temperature and the values predicted by the theoretical models, it can be concluded that the Kamuyu model best predicts the PV module temperature for this experimental research and obtained data. Dif- ferences in values of PV module temperature estimation are from the neglect of the thermal ac- cumulation of the PV module in empirical models. Also, all empirical models were developed in different geographical locations using specific meteorological parameters for these locations which in the end shape and form these empirical models. Analyzing experimental data, it can be concluded that temperature of the PV module is above 25 °C for whole measured period with significant impact of meteorological parameters. Considering the climate changes, increasingly hot summers with extremely high air temperatures and solar radiation, it can be expected that the temperature of the PV module will be above 25 °C for almost half of the year. In order to obtain more relevant data of using empirical models for PV module temperature for analyzed

geographical and climate area, it is necessary to carry out the experimental research that will cover a longer period of time. Considering the measured high PV module temperatures, for some future research will analyze cooling possibilities and its effect both on the temperature of the PV panel and its performance. These analyzes will include heat exchanger analyzes for this purpose, working fluids and their different mass-flows in order to analyze the cooling effects on PV module’s output in different scenarios. All these parameters will be tested experimentally depending on the climatological parameters.

## Nomenclature

–2]

|G – global solar radiation, [Wm|Subscripts|
|---|---|
|T – temperature, [°C]|a – air|
|v – wind velocity, [ms|c – cell|
|Acronyms|m – module|
|STC – standard test conditions|PV – photovoltaic T – time, [second]|

–1].

## Acknowledgment

The authors acknowledge the support of the European Research Executive Agency (REA) for funding this research under the project *ENPOWER – Enhancing Scientific Capacity* *for Energy Poverty* (*101160253 – ENPOWER – HORIZON-WIDERA-2023-ACCESS-02*). The authors acknowledge the support of the Science Fund of the Republic of Ser- bia, Grant No. 4344, *ForwardLooking Framework for Accelerating Households* Green Energy Transition – FF GreEN and by the Ministry of Science, Technological Development and Inno- vation of the Republic of Serbia; Grant No. 451-03-137/2025-03/200105.

## Disclaimer

Funded by the EU. Views and opinions expressed are however those of the authors only and do not necessarily reflect those of the EU or European Research Executive Agency (REA). Neither the EU nor the granting authority can be held responsible for them.

## References

[1] ***, Renewables 2023 – Analysis and forecast to 2028, International Energy Agency Report, 2024 [2] ***, REPowerEU Plan, European Commission, 2022 [3] Akrami, E., *et al.*, Integrated an Innovative Energy System Assessment by Assisting Solar Energy for Day and Night Time Power Generation: Exergetic and Exergo-Economic Investigation, *Energy Conversion* *and Management*, *175* (2018), Sept., pp. 21-32 [4] Aslan, G., *et al*., Impact of Harsh Weather Conditions on Solar Photovoltaic Cell Temperature: Experi- mental Analysis and Thermal-Optical Modelling, *Solar Energy*, *252* (2023), Mar., pp. 176-194 [5] Ahmed, H., *et al.*, Experimental and numerical investigation for PV Cooling by Forced Convection, *Alex-* *andria Engineering Journal*, *64* (2023), Feb., pp. 427-440 [6] Adefarati T., Bansal R., Reliability and Economic Assessment of a Microgrid Power System with the Integration of Renewable Energy Resources, *Applied Energy*, *206* (2017), Nov., pp. 911-933 [7] ***, EU Solar Energy Strategy, European Commission, Brussels, 2022 [8] ***, The future of Solar energy, MIT, 2015 [9] Valencia-Caballero, D., *et al.*, Performance Analysis of a Novel Building Integrated Low Concentration Photovoltaic Skylight with Seasonal Solar Control, *Journal of Building Engineering*, *4* (2022), 104687 [10] Strielkowski, W., Renewable Energy Sources, Power Markets, and Smart Grids, in: *Social Impacts of Smart* *Grids*, Elsevier, Amsterdam, The Netherlands, 2020, pp. 97-151 [11] Nouar, A., Methodology for Predicting the PV Module Temperature Based on Actual and Estimated Weather Data, *Energy Conversion and Management*, *14* (2022), 100182 [12] Santiago, I., *et al*., Modelling of Photovoltaic Cell Temperature Losses: A Review and A Practice Case in South Spain, *Renewable and Sustainable Energy Reviews*, *90* (2018), July, pp. 70-89

[13] Sharaf, M., *et al*., Performance Enhancement of Photovoltaic Cells Using Phase Change Material (PCM) in Winter, *Alexandria Engineering Journal*, *61* (2022), 6, pp. 4229-4239 [14] Gurbuz, H., *et al*., Experimental Investigation on Electrical Power and Thermal Energy Storage Perfor- mance of a Solar Hybrid PV/T-PCM Energy Conversion System, *Journal of Building Engineering*, *69* (2023), 106271 [15] Yoong, C. B., Optimal Orientation and Tilting Angle of PV Panels Considering Shading and Temeprature effects, Ph. D. thesis, Lee Kong Chian Faculty of Engineering and Science Universiti Tunku Abdul Rah- man, Sungai Long, Malaysia, 2023 [16] Rahman, M. M., *et al.*, Effects of Operational Conditions on the Energy Efficiency of Photovoltaic Mod- ules Operating in Malaysia, *Journal of Clean Production*, *164* (2017), Feb., pp. 1474-1485 [17] Fouad, M., *et al*., An Integrated Review of Factors Influencing the Perfomance of Photovoltaic Panels, *Renewable and Sustainable Energy Reviews*, *80* (2017), Dec., pp. 1499-1511 [18] Nezamisavojbolaghi, M., *et al*., The Impact of Dust Deposition on PV Panels’ Efficiency and Mitigation Solutions: Review Article, *Energie*s, *16* (2023), 16, pp. 2-19 [19] Gallardo-Saavedra, S., Karlson B., Simulation, Validation and Analysis of Shading Effects on a PV Sys- tem, *Solar Energy*, *170* (2018), Aug., pp. 828-839 [20] Conceicao, R., *et al*., Soiling Effect in Solar Energy Conversion Systems: A Review, *Renewable and Sus-* *tainable Energy Reviews*, *162* (2022), 112434 [21] Korab, R., *et al.*, A dynamic Thermal Model for a Photovoltaic Module under Varying Atmospheric Con- ditions, *Energy Conversion and Management*, *280* (2023), 116773 [22] Shadid, R., *et al*., Investigation of Weather Conditions on the Output Power of Various Photovoltaic Sys- tems, *Renewable Energy*, *217* (2023), 119202 [23] Browne, M. C., *et al*., Heat Retention of a Photovoltaic/Thermal Collector with PCM, *Solar Energy*, *133* (2016), Aug., pp. 533-548 [24] Sohani, A., *et al*., Comparative Study of Temperature Distribution Impact on Prediction Accuracy of Sim- ulation Approaches for Poly and Mono Crystalline Solar Modules, *Energy Conversion and Management*, *239* (2021), 114221 [25] Jaber, M., *et al.*, Prediction Model for the Performance of Different PV Modules Using Artifi cial Neural Networks, *Applied Sciences*, *12* (2022), 12, 7 [26] Sulaiman, S. I., *et al*., M*odelling of Operating Photovoltaic Module Temperature Using Hybrid Cuckoo* *and Artificial Neural Network*, (Eds. Kim, Y. S., Kang, B. H., Richards, D.), Knowledge Management and Acquisition for Smart Systems and Services, PKAW 2014, Lecture Notes in Computer Science, Springer, Heidelberg, Germany, 2014 [27] Sohani, A., Sayyaadi, H., Employing Genetic Programming to Find the Best Correlation Predict Tempera- ture of Solar Photovoltaic Panels, *Energy Conversion and Management*, *224* (2020), 113291 [28] Keddouda, A., *et al*., Photovoltaic Module Temperature Prediction Using Various Machine Learning Al- gorithms: Performance evaluation, *Applied Energy*, *363* (2024), 123064 [29] Zouine, M., *et al*., Mathematical Models Calculating PV Module Temperature Using Weather Data: Ex- perimental Study, *Proceedings*, 1st International Conference on Electronic Engineering and Renewable Energy, ICEERE 2018, Lecture Notes in Electrical Engineering, Singapore, Singapore, 2019 [30] King, D. L., *et al*., *Photovoltaic Array Performance Model*, Sandia National Laboratories, Albuquerque,

N. Mexico, USA, 2004
[31] Ross, R. G., Interface Design Considerations for Terrestrial Solar Cells Modules, *Proceedings*, 12th IEEE Photovoltaic Specialists Conference, Baton Rouge, La., USA, 1976 [32] Schott, T., Operation Temperatures of PV Modules: A Theoretical and Experimental, *Proceedings*, 6th EC Photovoltaic Solar Energy Conference, London, UK, 1985 [33] Lasnier, F., Ang, T. G., *Photovoltaic Engineering Handbook*, Taylor and Francis, New York, USA, 1990 [34] Mondol, J. D., *et al*.,Comparison of Measured and Predicted Long Term Performance of Grid a Connected Photovoltaic System, *Energy Conversion and Management*, *48* (2007), 4, pp. 1065-1080 [35] Skoplaki, E., *et al*., A Simple Correlation for the Operating Temperature of Photovoltaic Modules of Arbi- trary Mounting, *Solar Energy Materials and Solar Cells*, *92* (2008), 11, pp. 1393-1402 [36] Kamuyu, C. L. W., *et al*., Prediction Model of Photovoltaic Module Temperature for Power Performance of Floating PV, *Energies*, *11* (2018), 2, 447

Paper submitted: December 24, 2024 Paper revised: February 25, 2025 2025 Published by the Vinča Institute of Nuclear Sciences, Belgrade, Serbia. Paper accepted: March 1, 2025 This is an open access article distributed under the CC BY-NC-ND 4.0 terms and conditions.
