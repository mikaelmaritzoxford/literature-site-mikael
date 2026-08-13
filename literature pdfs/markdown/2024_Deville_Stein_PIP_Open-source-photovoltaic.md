Received: 23 May 2023 Revised: 27 October 2023 Accepted: 5 December 2023 DOI: 10.1002/pip.3763

<u>RESEARCH ARTICLE</u>

# Open-source photovoltaic model pipeline validation against well-characterized system data

1,2 1 1 2 Lelia Deville | Marios Theristis | Bruce H. King | Terrence L. Chambers | 1 Joshua S. Stein

1 Department of Photovoltaics and Materials Technology, Sandia National Laboratories, Abstract Albuquerque, New Mexico, 87185, USA All freely available plane-of-array (POA) transposition models and photovoltaic 2 Department of Mechanical Engineering, University of Louisiana at Lafayette, Lafayette, (PV) temperature and performance models in pvlib-python and pvpltools-python were Louisiana, 70504, USA examined against multiyear field data from Albuquerque, New Mexico. The data

Correspondence include different PV systems composed of crystalline silicon modules that vary in cell Lelia Deville, Sandia National Laboratories, type, module construction, and materials. These systems have been characterized via Albuquerque, NM 87185, USA. Email: lmdevil@sandia.gov IEC 61853-1 and 61853-2 testing, and the input data for each model were sourced from these system-specific test results, rather than considering any generic input Funding information Office of Energy Efficiency and Renewable data (e.g., manufacturer's specification [spec] sheets or generic Panneau Solaire [PAN] Energy, Grant/Award Numbers: 38267, 38268;files). Six POA transposition models, 7 temperature models, and 12 performance US Department of Energy (Office of Science, Office of Basic Energy Sciences and Energy models are included in this comparative analysis. These freely available models were Efficiency and Renewable Energy, Solar Energyproven effective across many different types of technologies. The POA transposition Technology Program); Solar Energy Technologies Office models exhibited average normalized mean bias errors (NMBEs) within ±3%. Most PV temperature models underestimated temperature exhibiting mean and median residuals ranging from 6.5 C to 2.7 C; all temperature models saw a reduction in root mean square error when using transient assumptions over steady state. The per- formance models demonstrated similar behavior with a first and third interquartile NMBEs within ±4.2% and an overall average NMBE within ±2.3%. Although differ- ences among models were observed at different times of the day/year, this study shows that the availability of system-specific input data is more important than model selection. For example, using spec sheet or generic PAN file data with a com- plex PV performance model does not guarantee a better accuracy than a simpler PV performance model that uses system-specific data.

KEYWORDS modeling comparison, performance modeling, photovoltaics

1 | INTRODUCTION Performance models take as inputs irradiance and weather time series data and parameters that describe the performance characteristics of One of the most powerful tools for the planning and performance the PV plant components as well as system design specifications analysis of a photovoltaic (PV) system is a performance model. and produce as output time series of simulated power or efficiency of

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. © 2023 The Authors. Progress in Photovoltaics: Research and Applications published by John Wiley & Sons Ltd.

Prog Photovolt Res Appl. 2024;32:291–303. wileyonlinelibrary.com/journal/pip

1099159x, 2024, 5, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.3763](https://onlinelibrary.wiley.com/doi/10.1002/pip.3763) by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [01/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License DEVILLE ET AL.

have been characterized by both Sandia National Laboratories and an external laboratory using various methods to obtain PAN files, IEC 61853-1, 61853-2, and Sandia Array Performance Model (SAPM) data. Using these test data, the systems' power and efficiency will be analyzed against PV performance model predictions. An overview of the POA transposition, temperature models, and performance models is given, and the PV systems are described. The results and error cal- culations of each irradiance, temperature, and performance model are presented and discussed.

## 2 | OVERVIEW OF MODELS

For all models considered in this study, a more in-depth description and all defining equations can be found in the original paper establish- ing the model; citations to the original paper are given in the respec- tive subsections.

2.1 | POA transposition models
Table 1 shows the irradiance transposition models compared in this
 study, which were run using pvlib-python v0.9.3 [11, 12]. Overall, six models were included: Isotropic [13], Haydavies [14], Klucher [15], Reindl [16], King [17], and Perez [18] models. The Perez model has multiple sets of coefficients based on data from specific geographical locations, but all share the same solar geometry inputs. To determine which one is more appropriate for the irradiance transposition com- parison, all 11 Perez models (available in pvlib-python) were tested: all- sitescomposite1990, allsitescomposite1988, sandiacomposite1988, usacomposite1988, france1988, phoenix1988, elmonte1988, osage1988, albuquerque1988, capecanaveral1988, and albany1988.
the system. Modeling can serve as both a simulation and optimization tool and can be used at various stages of development in a PV system, for example, site assessment, design evaluation, technology compari- sons, and in proving bankability of a project. Models vary according to the performance factors they consider, number of inputs, complexity of calculations, financial considerations, and scale of application [1]. The simplest models relate maximum power output to incident irradi- ance and operating temperature using a multilinear function. Other models rely on treating the PV system as an equivalent circuit with one or more diodes and resistors in series and in parallel [2]. Others are semiempirical and require extensive module measurements be made in outdoor conditions. The simplest models require inputs that are readily available from commercial specification or specification (spec) sheets, while others require testing to be conducted on mod- ules under controlled conditions. Many comparisons of simple, freely available models exist (e.g., Marion et al. [3]), but these comparisons usually only consider two to three models at a time or models that require the exact same inputs [4] and/or are benchmarked on a limited number of systems [5]. These comparisons rarely use module-specific measured data: mean- ing that instead of fully characterizing the modules prior to modeling, manufacturer supplied spec sheet or Panneau Solaire (PAN) data are used. The latter approach assumes that all PV modules with the same model number perform identically according to the spec sheets. This is not true because they can vary in nameplate and operating perfor- mance and even the rate they degrade over time (see, e.g., in Theristis et al. [6]). In such cases, a PV performance modeling comparison would be biased by uncertainties in the environmental and module specific characterization data rather than focusing on the ability of the models to predict a system's behavior. An international blind PV performance modeling comparison was recently published by the Sandia-led PV Performance Modeling Collaborative (PVPMC), involv- ing participants from 32 institutions [7]. The results demonstrated improved precision among models, but accuracy still depends on the modeler's skill and derate assumptions. These create the need for a comprehensive comparison of PV performance models against multi- year field data from well-characterized systems consisting of different types of PV modules. This study compares all freely available photovoltaic performance models from pvlib-python and pvpltools-python. The models were tested against well-characterized crystalline silicon (c-Si) systems in Albuquerque, New Mexico (NM). These c-Si systems include technol- ogies that were more recently established, that is, not solely aluminum back surface field (Al-BSF) modules, which was the major technology used when these models were originally defined. The models used in this study vary in their methods of calculation but do not use data- driven approaches, such as machine learning [8, 9]. The systems that are included in this study are limited to fixed tilt, monofacial, c-Si [10]. Furthermore, six plane-of-array (POA) transposition models and seven temperature models are compared against data measured on-site. Seven PV systems located at Sandia's Photovoltaic Systems Eval- uation Laboratory are being considered. All available data for each system, which range from 2 to 4 years, are being used. These systems

2.2 | PV module temperature models All temperature models examined in this study were run and com- pared using pvlib-python v0.9.3 under steady-and transient-state assumptions. The steady-state analysis includes two module tempera- ture models (SAPM [19] and Faiman [20]) and four cell temperature models (Ross [21], PVSyst [22], SAM NOCT [23], and SAPM Cell [19]). These models' inputs and outputs are described in Table 2. To exam- ine the influence of transient-state assumptions on the temperature predictions, the same models were rerun by incorporating the Fuen- tes [24] and additive Prilliman [25] transient temperature models. Many of these models use empirical coefficients to describe mod- ule temperature. SAPM uses a, a coefficient to establish the upper limit of module temperature during periods of low wind speed and high solar irradiance, and b, a coefficient to establish the rate at which module temperature decreases as wind speed increases. SAPM also considers a parameter known as ΔT, which is the temperature differ- ence between the cell and back of module surface at an irradiance of 1000 W/m². Faiman uses two heat loss coefficients, U0 and U1; U1

TABLE 1 Necessary inputs into the

Isotropic Perez (All) Haydavies Klucher Reindl King POA transposition models considered in this study. Module tilt ✔✔ ✔ ✔✔✔ System azimuth ✔✔ ✔✔ Solar azimuth ✔✔ ✔✔ Solar zenith ✔✔ ✔✔✔ GHI ✔✔✔ DHI ✔✔ ✔ ✔✔✔ DNI ✔✔ ✔ Extraterrestrial DNI ✔✔ ✔ Airmass ✔

Abbreviations: DHI, direct horizontal irradiance; DNI, direct normal irradiance; GHI, global horizontal irradiance.

TABLE 2 Necessary inputs for the cell and module temperature models considered in this study.

Module temperature models Cell temperature models Transient models

SAPM Faiman Ross PVSyst SAM NOCT SAPM Fuentes a Prilliman Global POA ✔✔ ✔✔✔✔✔ Ambient temp ✔✔ ✔✔✔✔✔ Wind speed ✔✔ ✔✔✔✔✔ NOCT ✔✔ ✔ a

Module height ✔✔ Model specific coefficients ✔ ✔ ✔ ✔ ✔ a, b U0, U1 Uc, Uv a, b, ΔT a0–a3 Module efficiency ✔✔ Absorption ✔✔ ✔ Emissivity ✔ Module unit mass ✔ Steady-state modeled temp ✔ a Fuentes model uses an installed NOCT which is determined following methods defined by Fuentes [24].

considers the influence of wind, while U0 does not. PVSyst similarly appropriate format. This standard measures power at 27 different var- considers two heat loss coefficients, Uc and Uv, where Uc does not iations of temperature and irradiance. SAPM typically uses a set of consider wind and Uv does. The Prilliman model uses four coeffi-module coefficients acquired through extensive outdoor testing, cients, a0 through a3. These come from a bilinear interpolation matrix which is only available in a handful of test labs around the world. using minimum and maximum wind speed values. However, in this study, the same IEC 61853-1 data were translated into SAPM coefficients in order to ensure the same source of inputs. PVWatts is the most straightforward of all models used, requiring only

2.3 | PV performance models
the temperature coefficients and power at standard test conditions (STC): 1000 W/m² and 25 C. CEC and Desoto use module parame- The performance models compared in this study were taken from two ters, like current and voltage at STC, found in the IEC 61853-1 matrix different python packages. SAPM [19], PVWatts v5 (PVW)[26], to determine their specific model coefficients. PVSyst uses a file of CEC [27], Desoto (DES)[28], and PVSyst v6 (PVS) were run using specific module coefficients called a PAN file. The remaining models pvlib-python v0.9.3, and ADR [4], Heydenreich (HEY)[29], MotherPV are referred to as “Matrix Models” since they use the IEC 61853-1 (MOT)[30], PVGIS (PVG)[31], MPM5 [32], MPM6 [32], and Bilinear matrix data. Interpolation (BIL) were run using pvpltools-python [33]. Table 3 shows the inputs and outputs of each model and groups them by similarity. Although all data from this study came from one source (i.e., flash | FIELD DATA test measurements under varying irradiance levels and temperatures), the models consider inputs in different forms. To obtain these differ-Data for this study consist of measured irradiance, weather, and sys- ent forms, IEC 61853-1 [34] test data were translated into the tem output data along with module characterization data.

TABLE 3 Necessary inputs and outputs for the PV performance models considered in this study.

Matrix models Sandia Array Performance PVWatts PVSyst CEC and Desoto (ADR, HEY, MOT, PVG, MPM5, Model (SAPM) (PVW) (PVS) (DES) MPM6, and BIL) Input parameters Effective irradiance ✔✔✔✔✔ Measured module ✔ a ✔ a ✔ a ✔ a ✔ temp SAPM coefficients ✔ Temperature ✔✔ coefficients PAN file ✔ IEC 61853-1 data ✔✔✔ Output values Short-circuit current ✔✔✔ (Isc) Current at max. ✔✔✔ power (Imp) Voltage at max. ✔✔✔ power (Vmp) Open-circuit voltage ✔✔✔ (Voc) Max. power (Pmp) ✔✔✔✔ Normalized ✔ efficiency a These models use cell temperature, which is calculated from module temperature using Equation (2).

TABLE 4 System information of the seven SLTE systems used in study.

a

|Manufacturer and model|Cell technology|# of modules|Installation date|Start date|Abbreviation used|
|---|---|---|---|---|---|
|LG 320N1K-A5|N-PERT Si|4 strings of 12 (48)|January 2018|May 2018|LG320|
|Panasonic VBHN325SA16|HIT Mono Si|4 strings of 12 (48)|January 2018|May 2018|Panasonic325|
|Canadian Solar CS6K-270P|Poly-Si|4 strings of 12 (48)|October 2017|January 2018|CSpoly270|
|Canadian Solar CS6K-275 M|Mono-Si|4 strings of 12 (48)|October 2017|January 2018|CSmono275|
|Hanwha Q Cells Plus Q.Plus BFR-G4.1 280|Poly-Si PERC|4 strings of 12 (48)|October 2017|January 2018|Qpoly280|
|Hanwha Q Cells Peak Q.Peak BFR-G4.1 300|Mono-Si PERC|4 strings of 12 (48)|October 2017|January 2018|Qmono300|
|Mission Solar MSE300SQ5T The start date indicates the beginning of the reporting period which ends on the same date for all systems (December 31, 2021).|Mono-Si PERC|4 strings of 12 (48)|May 2019|May 2019|Mission300|

a

3.1 | System and instrument data
respectively. The systems consist of varying types of c-Si technologies only; no thin film modules were included in the study. Furthermore, Seven PV systems from the Systems Long-Term Exposure (SLTE) pro-these systems are small-scale laboratory systems that are monitored ject (previously known as the PV Lifetime Project [6]) were used in closely and use periodically calibrated sensors, which means more this study for benchmarking the models. The PV systems were accurate data, fewer data outages, and lower losses than typical com- installed from 2017 to 2019 and their details are given in Table 4. All mercial scale systems may exhibit. The reporting period for all systems systems have the same tilt and orientation of and 180, begins at their start date and ends on December 31, 2021. Voltage

specific yield of 1500 kWh/kWp/year and an electricity price of $0.05/kWh, this 4.5% overprediction could introduce a bias of $1.68 M/year in estimated revenues. Therefore, this simplified com- parison can show that given accurate module data, the models are able to perform similarly and accurately with a potentially reduced financial risk.

and current were measured at the string level for all systems using shunts and voltage dividers, with a combined system measurement accuracy of 99.83%. The inverter used varied throughout the systems, being either the SMA Sunny TriPower 15000TL-US or 20000TL-US models. Only DC current and voltage measurements were used in this study. Meteorological data were collected on site at 1 min average intervals. GHI was measured using a Kipp and Zonen CMP-21 pyran- ometer. Kipp and Zonen CH1 and Eppley normal incidence pyrheliom- eters (NIP) were used to measure DNI. To measure the DHI, two Eppley Precision Spectral Pyranometers (PSP) were used, one having a shade disk and the other having a shade band. The POA irradiance was measured using a Kipp & Zonen CMP-11 pyranometer. Wind speed was measured at 10 m above ground level using a Climatronics Wind Mark III Wind Sensor. Pressure was measured using a MetOne BX-597A sensor. Air temperature was measured using two Climatro- nics Aspirated Shield Temperature Sensors. Module temperature was measured using back of module resistance temperature detectors (RTDs) on one module of each string.

3.3 | Module data collection To ensure an apples-to-apples comparison between all models, all module-specific input data were sourced from the same testing proce- dure (i.e., IEC 61853). No spec sheet data were used to allow a fair comparison among the models without any external biases caused by possible inaccurate input data. Matrix data were obtained from IEC 61853-1 testing performed at CFV Labs [35]. This testing took place between November 4, 2019, and December 13, 2019, on a single control module of each type. The control modules were placed out- side for light soaking prior to being sent for testing and are not part of the system being used to evaluate the models. These test data were then used to produce SAPM coefficients, generate the PAN files, and provide the inputs necessary for the PVWatts, CEC, and Desoto models. The original calibration method for the SAPM relies on a piece- wise solution of each primary equation, using data sets tightly con- strained to specific outdoor environmental conditions. Separate thermal tests were required when using outdoor data to determine temperature coefficients prior to calibrating the primary equations. In this study, however, the primary equations were solved simulta- neously via multivariate regression analysis and did not require a sepa- rate thermal test [36]. In this method, all coefficients of each primary equation were solved without constraint, allowing for the translation of the IEC 61853-1 matrix into SAPM coefficients with no additional inputs. To generate the PAN files, PanOPT
®, a proprietary software developed by CFV Labs was used. This process involved taking mea- sured cardinal point values (Isc, Voc, Vmp, and Imp) over a tempera- ture and irradiance matrix as described in IEC 61853-1 and optimizing the PVSyst single-diode model parameters to fit that data. The

3.2 | Using generic specification sheet versus module-specific characterization data When module-specific data (e.g., IEC 61853 and 61215 data from selected modules retrieved from the system under evaluation) are not available, using the spec sheet can introduce a bias due to overrating or underrating. The power measurements taken from the modules used in this study varied by up to ~5% from the spec sheet [6]. Such differences in power will bias the model predictions and this should be attributed to the input accuracy, and not the modeling accuracy. To quantify this, Figure 1 compares three models using spec sheet (nameplate) and measured (IEC 61853-1) data of the most overrated system in the SLTE project. This system (Mission300) was selected because the modules' power was up to ~5% (or ~15 W; see Theristis et al. [6] for more information) lower than the spec sheet rating. As it can be seen, this overrating is directly reflected in the error of the models, with the nameplate Misson300 NMBE consistently overesti- mating power by 4–4.5% higher than its measured data counterpart. To put this into perspective, assuming a 500 MW power plant with a
FIGURE 1 NMBE of three models for the
 Mission300 system with input data coming from the module specific measured data and the manufacturer supplied nameplate data. The mean values, represented by the green triangle, are shown in each box. The amount of error in the nameplate values correlates directly to the increase seen in NMBE of the Mission300 system between data sources.

TABLE 5 Filtering criteria applied to all system and weather data
 parameter fit was bootstrapped using a proprietary CFV process simi-
to remove nighttime, unphysical values, and outliers. lar to others described in the literature which consider the single- diode model in various conditions (Open Circuit, Short Circuit, and Filter parameter Lower bound Upper bound Maximum Power Point). Solar elevation 15 90 Effective 50 W/m² 1200 W/m² irradiance 4 | METHODOLOGY Module 40 C85 C temperature Preliminary calculations were necessary since performance models Ambient 10 C40 C temperature require effective irradiance and cell temperature, while field measure- Current v 70% of slope of Imp/ 130% of slope of Imp/ ments only provided POA irradiance (i.e., by means of pyranometer irradiance GeffGeff measurements) and module temperature.

FIGURE 2 Pie chart displaying the average amount of data

removed by each filtering criterion and remaining available data.

4.1 | Effective irradiance calculation and module temperature conversion Effective irradiance was calculated using the SAPM model [19]by translating the direct and diffuse POA to the irradiance “seen” by solar cells and by also considering angle of incidence (AOI) losses; no spectral losses were considered since no spectral loss coefficients for the modules were available from the measured data. POA ground diffuse irradiance was calculated with a constant albedo of 0.189, which was the mean and median of the measured albedo data for the reporting period. The albedo is assumed to be the same for all systems, since all systems share a ground covering material of crushed gravel. The AOI losses were calculated using reference data for each module from IEC 61853-2 testing con- ducted at CFV Labs [37]. All IEC 61853-1 [34] and 61853-2 [38] power rating and AOI data are publicly available at the PVPMC website [39]. Equation (1) describes the method of calculating effec- tive irradiance, where IAM is the incidence angle modifier interpo- lated linearly from the IEC 61853-2 data and fdis the fraction of diffuse irradiance on the plane of array that is not reflected away, which is set to 1.
Geff¼ POAdirectIAM þfdPOAdiffuse: ð1Þ

The measured module temperature data come from RTDs on a sample module in each string. When using the models described pre- viously, some of these needed to be translated from cell temperature to module temperature. To fairly compare the cell temperature models to measured module temperature, they were converted to module temperature using the equation defined in King et al. [19]:

<u>POA</u> T mod¼ TcellΔT, ð2Þ POA₀

where Tmodis module temperature, Tcellis cell temperature, POA is the plane-of-array irradiance, POA₀ is irradiance at STC, and ΔT is a parameter which depends on module mounting and front/rear mate- rial (i.e., glass/glass or glass/polymer) and is set to 3 C in this case.

These modeled module temperature values were then compared with the average RTD measurement for a given system.

4.2 | Data filtering Weather, irradiance, and operational data were filtered based on the criteria listed in Table 5. As an example, Figure 2 shows the average amount of filtered data after each filter is applied. All systems have some initial data unavailability from periods of testing or system out- ages; on average, 2% of the total data were initially missing or unavail- able. Snow fall and snow depth data were taken from National Oceanic and Atmospheric Administration's (NOAA) online climate data from the Albuquerque International Airport weather station. Of the 4 years of data taken, 35 of the days have recorded snow fall and/or depth. Removing these days accounts for about 2% of data being removed. As expected, the solar elevation filter removes the largest amount of data due to nighttime. It also includes early morn- ings and late afternoons when the sun is low in the sky and concealed by mountains. After this filter is applied, only 4% more data are removed by the other filters described in Table 5. The average amount of remaining data was 32%. The system with the highest data

FIGURE 3 Describing the

different pipelines (module specific, weather, and irradiance data) for the PV performance modeling comparison. The dashed lines and boxes show at what step in the pipeline the comparisons described in this study are conducted.

N P ðÞ PMPOðÞi availability is the Mission300 system with 34% of the data remaining. i¼1 NMBE ¼ 100, ð3Þ The system with the least data availability is the CSpoly270 system N P P ðÞi O with 31% of the data remaining. This difference could be due to the i¼1 differences in length of data collection for these systems. The Mis- sion300 system was deployed in 2019, while the CSpoly270 system was deployed two years earlier in 2017. The filtered effective irradiance and module temperature data were used as inputs into the performance models. A flowchart is shown in Figure 3 describing the process for finding and calculating all parameters necessary for each model. All models are used to calculate string power and use the same weather and irradiance inputs.

where PMis the modeled parameter and POis the observed parame-

4.3 | Performance model evaluation metrics The results of each model were compared against the measured data. All analysis was completed at the same 1 min timestep as the measured data; any resampling shown in analysis was done after the results were generated. The normalized mean bias error (NMBE) and mean bias error (MBE) were calculated using (3) and (4)to reflect the model's prediction bias. Root mean square error (RMSE) was also used and calculated using (5). RMSE is the standard devia- tion of the residuals and shows how far the model's predictions are spread from the measured values. To obtain normalized RMSE (NRMSE), the RMSE is divided by the mean of the measured values.
P N ðÞ PMPOðÞi i¼1 MBE ¼, ð4Þ N

vffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi u uN uP ðÞ P ðÞ i P ðÞi2 O M RMSE ¼ t <u>i¼1</u>, ð5Þ N

ter; i represents the string number; and N is the number of observa- tions. The errors are calculated at each string and the average is taken. These calculations are applied to modeled temperature and power. For POA irradiance, since there is only one measured value, it is compared directly to the modeled value.

5 | PLANE OF ARRAY IRRADIANCE TRANSPOSITION MODEL COMPARISON

The Perez model has different submodels, and the first investigation was to run all submodels to determine the best performing one to compare to all other transposition models tested in the study.

FIGURE 4 RMSE versus MBE of 11 Perez

POA models shows the similarity in performance between the albuquerque1988 and phoenix1988 models.

FIGURE 5 RMSE versus MBE of the six POA

transposition models showing that Perez– abq1988 had the lowest MBE and Klucher had the lowest RMSE.

5.1 | Choosing a Perez model
consistent performance at all irradiance levels. For these reasons, it was the transposition model chosen to be used in the remainder of All eleven Perez models were tested to determine the best one to use the study. in the overall transposition model comparison. The models differ in the geographical location at which their coefficients were determined. The models with the best performance were the phoenix1988 and 6 | CELL AND MODULE TEMPERATURE albuquerque1988, which had the lowest RMSE and MBE, respectively. MODEL COMPARISON The MBE and RMSE for these models are plotted in Figure 4. Since these locations (i.e., Phoenix and Albuquerque) are close to the sys- When comparing the steady-state temperature models, all cell tem- tems being investigated, this result was expected. Therefore, the

|tems being|investigated,|this result|was expected.|perature models were converted to module temperature. The models'||||
|---|---|---|---|---|---|---|---|
|model selected for use in the main comparison was albuquerque1988.||||performance compared.|in both|steady-state|and transient|

perature models were converted to module temperature. The models' conditions were

5.2 | Transposition model comparison The MBE and RMSE values for all models are shown in Figure 5. Overall, most of the transposition models performed similarly with an MBE of ±10 W/m², with King being the only exception. The Isotropic model underestimated irradiance, whereas the King model overesti- mated. The RMSE values of Perez and Klucher were lower (<40 W/ m²) than all other models. The transposition models' performance varied at different irradi- ance levels, as shown in Figure 6. Isotropic, Klucher, Reindl, and Hay- davies were the best performing models at very low irradiance (<150 W/m²). The King model performed much worse than other models at low irradiance and it consistently overestimated irradiance until it reached similar levels of NMBE at around >650 W/m². The Perez–abq1998 model exhibited better performance at irradiance levels with the highest proportion of the data in them and the most
6.1 | Steady-state modeling For all cell and module temperature models, the mean and median residuals ranged from approximately 6.5 C to 2.7 C when all sys- tems were considered. Not all models performed similarly on a given system; this shows that model performance was more dependent on the model parameters and not the specific PV technology. Figure 7 shows the model performance per system, in which most of them underestimate temperature, except Ross. In the boxplots, the triangles represent the mean, the lines within the boxes show the median, the boxes extend to the 25th and 75th percentiles, and the whiskers show the furthest outliers that are still within the 1.5 interquartile range. The most accurate model was the PVSyst (cell temperature converted to module temperature) model, which had the lowest mean residual of 1.4 C when all systems were considered. Figure 8 shows

FIGURE 6 NMBE of six irradiance

transposition models plotted at various irradiance intervals. Overall, the NMBE values at all irradiance levels for most models were within ±3% of the measurements when irradiance is greater than 350 W/m².

FIGURE 7 Residuals of modeled module

temperature and average measured module temperature. All models but Ross had the tendency to underpredict.

FIGURE 8 Residuals of six cell/module

temperature models plotted at various irradiance intervals. All models overpredicted at low irradiances, and all models, except Ross, had opposite behavior at high irradiance.

the models' average residuals at different irradiance intervals. Similar comparison. In the PVSyst cell temperature model, efficiency is a to the performance shown in Figure 7, Ross was the only model to required input. The default efficiency value assumed in pvlib-python have consistent, positive bias. All other models continually had v0.9.3 is 0.1, but the model yielded higher accuracy when using the increasingly negative bias at higher irradiance intervals. This indicates manufacturer's efficiency at STC. The highest accuracy was observed that the models had the tendency to overpredict at lower irradiance when the efficiency was calculated based on measured system perfor- levels and underpredict at higher irradiance levels. mance and weather conditions. For models requiring nominal operating cell temperature (NOCT), this value was tested against nominal module operating temperature (NMOT). Two cases were tested: (a) cell temperature models using 6.2 | Moving beyond steady-state modeling NMOT and (b) cell temperature models using NOCT and then con- verting these values to module temperature using Equation (2). Case The temperature models were all then considered with transient

(b) resulted in lower errors and was the method used for this assumptions. Figure 9 shows the Faiman model with both steady-

FIGURE 9 Diurnal variation of module temperature during August clear-sky (a) and cloudy (b) days as well as January clear-sky (c) and cloudy

(d) days. The mean measured module temperature of the Qpoly280 system is shown in black; the Faiman model with steady-state assumptions in blue; the Faiman model with the additive Prilliman transient model in red; and the Fuentes model in green. As expected, the importance of incorporating transient temperature modeling is more significant during dynamic weather conditions.
FIGURE 10 RMSE of steady-state and

transient temperature models in which the transient assumptions improved for all models; the best being Faiman. The Prilliman model was not applied to Fuentes due to it already having transient assumptions in the default version of the model. Fuentes exhibited the lowest overall RMSE of 3.6 C.

state and transient assumptions (i.e., by applying the additive Prilli-conditions would show larger improvements when applying the tran- man) for the Qpoly280 system during clear and cloudy days in January sient temperature model. In this case, the model with the greatest and August 2018. The steady-state model, shown in blue, is more sus-reduction in RMSE was the Faiman model. Of all models, Fuentes had ceptible to instantaneous irradiance changes, for example, caused by the lowest RMSE of 3.6 C. passing clouds. The transient models, Faiman with additive Prilliman model in red and Fuentes in green, more closely follow the shape and consistency of the measured mean RTD values in black. Figure 10 7 | PV PERFORMANCE MODEL shows the changes in RMSE before (i.e., steady-state assumptions) COMPARISON and after applying the transient temperature model. These results indicate that considering transient behavior reduces the spread, even Although the 12 PV performance models varied widely in their inputs in Albuquerque, NM, where the sky conditions are relatively consis-and calculations, the performance of models for a given system was tent all year round. It is speculated that locations with more dynamic very similar. Figure 11 shows the NMBE for all models and systems

FIGURE 11 NMBE of all models, systems,

and years of data showing clustering based on model type and an overall low variability in overall model performance. Average NMBE for all models was within ±2.3% of measured values.

FIGURE 12 NRMSE versus NMBE for all

performance models and systems. The range of values of both metrics is relatively low but allows for observation of the clustering among modeling families (e.g., IEC61853-1 vs. single-diode models).

FIGURE 13 NMBE of each model at various

irradiance intervals for the Panasonic325 system and all years of data. The models are grouped in color according to their inputs and calculation type.

after a flat 2% derate was applied to account for degradation, soiling, sheet or PAN file) may be more important than the model itself. If a wiring losses, and so forth. All models exhibited a first and third quar-module's performance closely matches the specification sheet, this tile NMBEs within ±4.2%. The average NMBE for all models was may not be the case. Figure 12 shows the model's average NRMSE within ±2.3% of the measured values. The simplest model, PVWatts, versus NMBE. The NRMSE spread is also tight, varying from 4.4% to considered only two module specific inputs: the STC power and the 4.6%. While this NRMSE range was low, it is still clear that models of temperature coefficient of power. Even so, this model performed on similar type had the tendency to cluster together, like the matrix par with and sometimes exceeded the performance of more detailed models or CEC and Desoto. models, like PVSyst. This is another indication that the module input Figure 13 shows the NMBE for all models at various irradiance data being sourced from the specific system (and not a generic spec levels for the Panasonic325 system. The amount of data

represented by a given interval is shown on the right axis as a per- centage of total data. PVWatts, shown in blue, consistently overpre- dicts at lower irradiance levels. A low-light correction was included in v1 of PVWatts but was later removed in v5, which is the version implemented in pvlib-python v0.9.3. If this model is being used in a location that frequently experiences low irradiance, it may be bene- ficial to include the low-light portion of the model. In general, the single-diode models, like CEC and Desoto, exhibit the trend of over- prediction at lower irradiances while the Matrix models had the ten- dency to underpredict, but this trend is the opposite at higher irradiances.

## 8 | CONCLUSIONS AND LIMITATIONS

This study compared 6 POA transposition models, 7 PV temperature models, and 12 PV performance models against multiyear field data from well-characterized systems in Albuquerque, NM. Overall, the models performed similarly, but differences can be seen at various times of day and irradiance conditions. As expected, using a location-specific Perez submodel improved the model's performance. The temperature modeling comparison indicated that using a transient temperature model improves accuracy even in Albuquerque where conditions are relatively steady state. It is hypothesized that further accuracy improvements would be observed when using these models in locations with more dynamic conditions, for example, pass- ing clouds. The PV performance modeling comparison demonstrated that using a more complex model does not guarantee any greater accuracy. Using module-specific inputs (i.e., data that correspond to the modules under investigation and PAN files that have been gener- ated for the specific installation) was more critical in getting accurate results rather than using a more complex model and generic spec sheet or PAN file data. When comparing the models using systems with an observable difference in measured and nameplate values, the models' error was directly correlated to the difference in module per- formance. This indicates that when modeling a system, a large effort should be placed on characterizing the system under investigation (e.g., via IEC 61853 and/or 61215 testing) rather than focusing only on the model selection. All temperature and performance models in this study were com- pared with seven c-Si systems; no thin-film modules were available. It should also be noted that the SLTE systems that were considered are small-scale laboratory systems that are monitored closely, and there- fore, common derate assumptions do not apply. For example, the shorter strings and wiring runs of typical laboratory systems differ from those seen in large-scale systems. Due to the size of large-scale systems, the potential for nonuniformities across strings and arrays would influence the modeling accuracy of both temperature and per- formance modeling. Furthermore, laboratory systems are continuously monitored and equipped with state-of-the-art sensors for research purposes and are cleaned and calibrated periodically. Although some of these aspects hold true in commercial installations also, others can be cost-prohibitive.

AUTHOR CONTRIBUTIONS Lelia Deville: Methodology; software; validation; formal analysis; investigation; data curation; writing—original draft; review and editing; visualization. Marios Theristis: Conceptualization; methodology; vali- dation; writing—original draft; review and editing; supervision; project administration. Bruce H. King: methodology; data curation. Terrence

L. Chambers: writing—review and editing; supervision. Joshua
S. Stein: Conceptualization; methodology; validation; supervision; funding acquisition, writing—review and editing. All authors reviewed and approved the manuscript. ACKNOWLEDGMENTS The authors would like to thank Dr. Clifford W. Hansen, Kevin Ander- son, and Jim Crimmins for their valuable inputs. This work was sup- ported by the US Department of Energy's Office of Energy Efficiency and Renewable Energy (EERE) under the Solar Energy Technologies Office Award Numbers 38267 and 38268. Sandia National Laborato- ries is a multimission laboratory managed and operated by National Technology & Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honeywell International Inc., for the US Department of Energy's National Nuclear Security Administration under contract DE- NA0003525. This paper describes objective technical results and anal- ysis. Any subjective views or opinions that might be expressed in the paper do not necessarily represent the views of the US Department of Energy or the US Government. DATA AVAILABILITY STATEMENT Research data are not shared. ORCID Lelia Deville [https://orcid.org/0000-0002-5021-9743](https://orcid.org/0000-0002-5021-9743) Marios Theristis [https://orcid.org/0000-0002-7265-4922](https://orcid.org/0000-0002-7265-4922) REFERENCES
1. Tozzi P Jr, Jo JH. A comparative analysis of renewable energy simula- tion tools: performance simulation model vs. system optimization. Renew Sustain Energy Rev. 2017;80:390-398. doi:10.1016/j.rser.2017.
05.153
2. Shongwe S, Hanif M. Comparative analysis of different single-diode PV modeling methods. IEEE J Photovoltaics. 2015;5(3):938-946. doi:
10.1109/jphotov.2015.2395137
3. Marion B.. Comparison of Predictive Models for Photovoltaic Module Performance.
4. Driesse A, Theristis M, Stein JS. A new photovoltaic module efficiency model for energy prediction and rating. IEEE J Photovoltaics. 2021; 11(2):527-534. doi:10.1109/JPHOTOV.2020.3045677
5. Kichou S, Silvestre S, Guglielminotti L, Mora-Lopez ~ L, Muñoz- Ceron E. Comparison of two PV array models for the simulation of PV ~ systems using five different algorithms for the parameters identifica- tion. Renew Energy. 2016;99:270-279. doi:10.1016/j.renene.2016.
07.002
6. Theristis M, Stein JS, Deline C, et al. Onymous early-life performance degradation analysis of recent photovoltaic module technologies. Progr Photovoltaics: Res Applic. 2023;31(2):149-160. doi:10.1002/pip.
7. Theristis M, Riedel-Lyngskær N, Stein JS, et al. Blind photovoltaic modeling intercomparison: a multidimensional data analysis and

lessons learned. Progr Photovoltaics: Res Applic. 2023;1-14. doi:10. 1002/pip.3729)

8. Livera A, Theristis M, Makrides G, Ransome S, Sutterlueti J, Georghiou GE. Optimal development of location and technology inde- pendent machine learning photovoltaic performance predictive models. In: 46th IEEE Photovoltaic Specialists Conference (PVSC), 16–21 June 2019; 2019:1270-1275. doi:10.1109/pvsc40753.2019.8980474
9. Livera A, Theristis M, Makrides G, Sutterlueti J, Ransome S, Georghiou GE. Performance analysis of mechanistic and machine learning models for photovoltaic energy yield prediction. In: Proceed- ings of the 36th European Photovoltaic Solar Energy Conference and Exhibition; 2019:9-13.
10. Riedel-Lyngskær N, Berrian D, Alvarez Mira D, et al. Validation of bifacial photovoltaic simulation software against monitoring data from large-scale single-axis trackers and fixed tilt systems in Denmark. Appl Sci. 2020;10(23):8487. doi:10.3390/app10238487
11. Stein JS, Holmgren WF, Forbess J, Hansen CW. PVLIB: open source photovoltaic performance modeling functions for Matlab and Python. In: 2016 43rd IEEE Photovoltaic Specialists Conference (PVSC). IEEE; 2016:3425-3430.
12. Holmgren WF, Hansen CW, Mikofski MA. pvlib python: a python package for modeling solar energy systems. J Open Source Softw. 2018;3(29):884. doi:10.21105/joss.00884
13. Hottel H, Whillier A. Evaluation of flat-plate solar collector perfor- mance. In: Trans. Conf. Use of Solar Energy. Vol.3; 1955.
14. Hay JE. Calculating solar radiation for inclined surfaces: practical approaches. Renew Energy. 1993;3(4–5):373-380. doi:10.1016/0960- 1481(93)90104-O
15. Klucher TM. Evaluation of models to predict insolation on tilted sur- faces. Solar Energy. 1979;23(2):111-114. doi:10.1016/0038-092X(79) 90110-5
16. Reindl D, Beckman W, Duffie J. Evaluation of hourly tilted surface radiation models. In: Solar Energy. Vol.45, no. 1; 1990:9-17.
17. King D.. "Simple Sandia Sky Diffuse Model." [https://pvpmc.sandia.gov/](https://pvpmc.sandia.gov/) modeling-steps/1-weather-design-inputs/plane-of-array-poa- irradiance/calculating-poa-irradiance/poa-sky-diffuse/simple-sandia- sky-diffuse-model/
18. Perez R, Stewart R, Seals R, Guertin T. The Development and Verifica- tion of the Perez Diffuse Radiation Model. Sandia National Laboratories;
1988.
19. King D. L., Boyson W. E., and Kratochvil J. A., "Photovoltaic Array Per- formance Model," Sandia Report No SAND 2004-3535, 2004. Accessed: [http://www.osti.gov/scitech//servlets/purl/919131-](http://www.osti.gov/scitech//servlets/purl/919131-) sca5ep/
20. Faiman D. Assessing the outdoor operating temperature of photovol- taic modules. Progr Photovoltaics: Res Applic. 2008;16(4):307-315. doi:
10.1002/pip.813
21. Ross R. Design techniques for flat-plate photovoltaic arrays. In: Pro- ceedings of the 15th Photovoltaic Specialists Conference; 1981:12-15.
22. Mermoud A, Wittmer B. PVSYST User's Manual. Switzerland; 2014.
23. Gilman P, Dobos A, DiOrio N, Freeman J, Janzou S, Ryberg D. SAM Photovoltaic Model Technical Reference Update. NREL; 2018.
24. Fuentes MK. A Simplified Thermal Model for Flat-Plate Photovoltaic Arrays. Sandia National Laboratories; 1987.
25. Prilliman M, Stein JS, Riley D, Tamizhmani G. Transient weighted moving-average model of photovoltaic module back-surface tempera- ture. IEEE J Photovoltaics. 2020;10(4):1053-1060. doi:10.1109/ jphotov.2020.2992351
26. Dobos AP. PVWatts Version 5 Manual. National Renewable Energy Lab.(NREL); 2014.
27. Dobos AP. An improved coefficient calculator for the California energy commission 6 parameter photovoltaic module model. J Solar Energy Eng. 2012;134(2):1-6. doi:10.1115/1.4005759
28. De Soto W, Klein SA, Beckman WA. Improvement and validation of a model for photovoltaic array performance. Solar Energy. 2006;80(1): 78-88. doi:10.1016/j.solener.2005.06.010
29. Heydenreich W, Müller B, Reise C. Describing the world with three parameters: a new approach to PV module power modelling. In: 23rd European PV Solar Energy Conference and Exhibition (EU PVSEC); 2008: 2786-2789.
30. de Montgareuil AG, Sicot L, Martin J, Mezzasalma F, Merten J. A new tool for the MotherPV method: modeling of the irradiance coefficient of photovoltaic modules. In: 24th European Photovoltaic Solar Energy Conference (EU PVSEC); 2009:21-25.
31. Huld T, Friesen G, Skoczek A, et al. A power-rating model for crystal- line silicon PV modules. Sol Energ Mat Sol C. 2011;95(12):3359-3369. doi:10.1016/j.solmat.2011.07.026
32. Ransome S, Sutterlueti J. How to choose the best empirical model for optimum energy yield predictions. In: 44th IEEE Photovoltaic Specialist Conference (PVSC). IEEE; 2017:652-657.
33. Driesse A. "PV Performance Labs Tools for Python," GitHub repository at [https://github.com/adriesse/pvpltools-python](https://github.com/adriesse/pvpltools-python), 2020.
34. Standard IEC 61853-1, "Photovoltaic (PV) Module Performance Testing and Energy Rating—Part 1: Irradiance and Temperature Performance Measurements and Power Rating," 2011.
35. Sillerud C. "19074 PAN File Report," 2019. pvpmc.sandia.gov/pv- research/pv-lifetime-project/pv-lifetime-modules/.
36. Zirzow D. “20125 Test Report,” 2020. pvpmc.sandia.gov/pv- research/pv-lifetime-project/pv-lifetime-modules.
37. King BH, Robinson CD. Simplifying Methods to Calibrate the Sandia Array Performance Model: Elimination of the Traditional Thermal Test. Sandia National Laboratories; 2016.
38. Standard IEC 61853-2, "Photovoltaic (PV) Module Performance Testing and Energy Rating—Part 2: Spectral Responsivity, Incidence Angle and Module Operating Temperature Measurements," 2016.
39. PV Performance Modeling Collaborative. Sandia National Laboratories;
2019. [Online]. Available: [https://pvpmc.sandia.gov/](https://pvpmc.sandia.gov/) How to cite this article: Deville L, Theristis M, King BH, Chambers TL, Stein JS. Open-source photovoltaic model pipeline validation against well-characterized system data. Prog Photovolt Res Appl. 2024;32(5):291‐303. doi:10.1002/pip. 3763
