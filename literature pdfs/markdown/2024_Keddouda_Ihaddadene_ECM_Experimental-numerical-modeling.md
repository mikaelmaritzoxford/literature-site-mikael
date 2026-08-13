Energy Conversion and Management 312 (2024) 118563

Contents lists available at ScienceDirect

# Energy Conversion and Management

journal homepage: www.elsevier.com/locate/enconman

# Experimental and numerical modeling of photovoltaic modules temperature under varying ambient conditions

Abdelhak Keddouda a, b, *, Razika Ihaddadene a, c, Ali Boukhari d, e, Abdelmalek Atia d, f, Müslüm Arıcı g, h, Nacer Lebbihiat f, i, Nabila Ihaddadene a, c

a *University of M’Sila, Faculty of Technology, Department of Mechanical Engineering, PO Box 166 Ichebilia 28000, M’Sila, Algeria* b *Laboratory of Materials and Mechanics of Structures (L.M.M.S), University of M’Sila, Algeria* c *Water, Environment and Renewable Energies Laboratory, University of M’Sila, M’Sila, Algeria* d *UDERZA Unit, Faculty of Technology, University of El Oued, 39000, El Oued, Algeria* e *LEAP Laboratory, Fr*´*eres Mentouri’s University, 25000, Constantine, Algeria* f *LEVRES Laboratory, Faculty of Technology, University of El Oued, 39000, El Oued, Algeria* g *Kocaeli University, Faculty of Engineering, Department of Mechanical Engineering, 41001, Kocaeli, Turkey* h *International Joint Laboratory on Low-Carbon and New-Energy Nexus Research and Development, Kocaeli University, 41001, Kocaeli, Turkey* i *University of El Oued, Faculty of Technology, Department of Mechanical Engineering, 39000, El Oued, Algeria*

ARTICLE INFO ABSTRACT

*Keywords:* In this work, comprehensive three-dimensional computational fluid dynamics simulation, of fluid flow and heat Module temperature transfer phenomena around a free-standing polycrystalline silicon photovoltaic module is carried out. The Photovoltaic objective is to provide accurate calculation of module’s temperature as a key parameter to estimate its power CFD simulations output. Therefore, experiments were conducted at the university of El Oued, south-east Algeria, to collect the Parametric study necessary dataset for simulations. Considering different heat transfer mechanisms, modeling absorbed solar Regression energy within the cells, and after mesh refinement study and model validation, simulations were performed and different parameters have been investigated. Results show that more accurate module temperature (*Tback*) esti mation can be achieved based on numerical simulations. It was also found that numerical simulation overcome other models from literature and provides better results, achieving an *R*2of 0.995 and a mean absolute error (MAE) of 0.822. Results also indicate that, solar radiation (*G*), ambient temperature (*Ta*) and wind speed (*Ws*) tend to have the major impact on *Tback*, an increase of 100*W/m*2in *G* can produce an increase of 4 ◦ *C* in *Tback*at low wind speeds, and about 2*.*4 ◦ *C* for relatively higher *Ws*. *Ta*also tends to yield linear increase in *Tback*, expecting 5*.*8 ◦ *C* rise, for 6 ◦ *C* increase in *Ta*at 700*W/m*2and 1*m/s* of solar radiation and wind speed, respectively. Additionally, a regression-based model was proposed for engineering applications, providing accurate results with an *R*2of 0.989, a MAE of 1.009, which is 10% more accurate than the best model from literature.

transfer mechanisms must be taken in consideration when performing

**1. Introduction**
an energy balance on the module in order to estimate and predict its temperature. Those mechanisms, in most cases, take place on both sides The operating temperature of photovoltaic (PV) modules is an of the PV module. Several approaches were considered in literature to important parameter, which the performance and efficiency of the predict the PV module temperature, involving data-driven and machine conversion of solar to electrical energy essentially depend on [1–3]. Due learning modeling [8–13], dynamic energy balance method [14–16], to the fact that significant part of the energy reaching the panel in the thermal modeling [17–20], and different numerical methods as well form of incident solar radiation is released to the environment in the [21–23]. The following is a review of some of those approaches taken form of heat, the module temperature is related to the environmental recently. conditions in which the panel itself is placed. It is well established that it One of the earliest models for predicting photovoltaic modules can be significantly affected by different parameters such as ambient temperature is the one proposed by Ross [24]. It is simply, a linear and temperature, wind speed, and solar radiation [4–7], thus, standard heat straightforward expression for the cells temperature, stating that the

* Corresponding author. *E-mail address:* abdelhak.keddouda@univ-msila.dz (A. Keddouda).
[https://doi.org/10.1016/j.enconman.2024.118563](https://doi.org/10.1016/j.enconman.2024.118563) Received 29 February 2024; Received in revised form 26 April 2024; Accepted 14 May 2024 Available online 18 May 2024 0196-8904/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

*A. Keddouda et al. Energy &RQYHUVLRQ DQG 0DQDJHPHQW 312 (2024) 118563*

|Nomenclature||||η|Module efficiency (||)|
|---|---|---|---|---|---|---|---|
|||||τα|Absorbance-transmittance coefficient (|||
|A|Module area (m²)|||Y|Variable (|)||
|C|Specific heat capacity (J.kg||.K)|F|View factor (|)||
|g|Acceleration of gravity (m.s||)|Subscripts||||
|G|Solar radiation (W.m|)||a|Ambient|||
|K|Turbulence kinetic energy (m².s||)|s|Speed|||
|∊|Surface emissivity/Turbulence dissipation rate (m².s|||sky|Sky|||
|k|Thermal conductivity (W.m||.K)|gr|Ground|||
|S|Volumetric heat source (W.m||)|ref|Reference state|||
|V|Volume (m³)|||pred|Predicted|||
|T|Ambient temperature (|C)||measu|Measured|||
|W|Wind speed (m.s|)||i, j, k|Index|||
|T|Module temperature (|C)||Abbreviations||||
|P|Module power output (W)|||ANN|Artificial Neural Network|||
|n|Number of attributes (|)||STC|Standard Test Conditions|||
|T|Temperature (|C)||MAE|Mean Absolute Error|||
|ΔT|Temperature difference (T||T)(C)|MAPE|Mean Absolute Percentage Error|||
|t|Thickness (mm)|||PV|Photovoltaic|||
|ρ|Density (kg.m|)||RANS|Reynolds Averaged Navier-Stokes|||
|μ|Temperature coefficient/Viscosity (Pa.s)|||RMSE|Root Mean Squared Error|||
|σ α|Stefan-Boltzmann constant (W.m Module inclination angle (||.K) )|MSE|Mean Squared Error|||

)

1 1 p 2 2 2 3 ) 1 1 3 e

◦ a 1 s ◦ pv pv

◦ ◦ pv a

2 4 ◦

difference (*TcTa*) linearly depends on solar radiation *G* through a constant of proportionality *k* in the range of 0*.*02 to 0*.*04, while more recent studies indicated that the range for *k* can be extended upwards [25]. Based on Ross model, several similar model equations have been proposed in literature [26–30], where the temperature difference be tween the cell and ambient temperature is a function of solar radiation. Similarly, a model was established by Lasnier [31], where a regression analysis was performed to estimate the module temperature, relating it to solar radiation and ambient temperature. Servant [32] proposed a regression-based model including wind speed effects, the model assumes linear relation with ambient parameters, and was found to well repre sent experimental data. King [33] also developed an empirical model for module temperature estimation, stating that it is a function of solar ra diation, ambient temperature, and wind speed. Furthermore, in another investigation, King et al. [34] proposed a similar model that includes material properties and assumes that cell temperature is related to back- side temperature, where they determined empirical coefficients to esti mate it. Additionally, TamizhMani et al. [35] proposed models for module temperature, one of which accounts for ambient temperature, solar radiation, and wind speed, while the other adds relative humidity as an input. Their results indicated that ambient temperature sets the module temperature, and solar radiation explains its raise, while wind speed helps reducing it. Moreover, King et al. [36] presented an addi tional model for module cell temperature, similar to their previous model, the model accounted for same parameters, and taking in consideration mounting configuration and module type. Mondol et al. [28] presented a model for module temperature, relating it to ambient temperature and solar radiation, where they indicated that their pro posed model produced a predictive error less than the one by nominal operating cell temperature (NOCT) approach. Skoplaki et al. [37] introduced a semi-empirical correlation for module temperature, which related PV module temperature to basic environmental variables. Ac cording to their results, and neglecting the effect of free convection, the correlation error was within 3%, and can be reduced to 1*.*6% for solar radiation between 600 *W/m* and wind speeds within 1*.*2 to 4*m/s*. Almaktar et al. [38] showed that module temperature can be related to ambient temperature, and introduced regression models to estimate

module temperature based on solar radiation, ambient temperature, wind speed and relative humidity. Their finding indicated that module temperature correlations was showing good agreement with experi mental data and predicted the module temperature of polycrystalline and monocrystalline modules with low error values. Muzathik [10] proposed a simple correlation for module temperature prediction, with solar radiation, ambient temperature and wind speed as inputs. Their results showed that the model was producing a predictive root mean squared error (RMSE) of about 2*.*85%. Bailek et al. [8] developed a regression-based model equation for PV module back-side temperature. Taking solar radiation and ambient temperature as inputs, their model was predicting module temperature with an error of 10% and a corre lation coefficient of *R²* = 0*.*955. Kaplanis et al. [39] investigated the prediction of PV module temperature and performance. Considering significant number of parameters and performing a theoretical analysis, they developed a compact model for different mounting conditions, with validation against experimental data and comparison with other similar models. Their results indicated that the proposed model had superior performance and lower relative error. Hove [40] showed that module temperature can be approximated by applying an energy balance equation, where the heat loss from the module can be evaluated using experimental data. Also, Mattei et al. [41] proposed an energy balance based method to estimate the tem perature of photovoltaic modules. The approach considered a value of

0*.*81 for the absorbance-transmittance coefficient (*τα*) and heat loss coefficient determined via experimental data. their results showed that the mean squared error (MSE) of their model was at 2*.*24
◦

C. Tiwari and
Sodha [42,43] implemented an energy balance based equation to esti mate the module (cell) temperature in an integrated photovoltaic and thermal solar system, indicating that the system’s results remained in a good agreement with experimental data. Additionally, Migliorini et al. [44] proposed a thermal-electrical model that accounts for the dynamics of photovoltaic modules. The module temperature was calculated in the thermal model and used to predict the power output, and similarly, Gu et al. [45], proposed a coupled thermo-electrical model to investigate and estimate module temperature and power output. Their findings indicated a significant reduction in the predictive error because of the

**Fig. 1.** Photovoltaic modules considered in this study.

**Table 1**

Electrical characteristics of the photovoltaic module. Characteristic Value Open-circuit voltage (*Voc*) 22.70 V Optimum operating voltage (*Vmp*) 18.60 V Short-circuit current current (*Isc*) 9.08 A A Optimum operating (*Imp*) 8.61 Maximum power at STC (*Pmax*) 160 W Cell efficiency 18.3 % Module efficiency 16.2 % Maximum system voltage 1000 V DC Operating temperature-40C◦ ◦ Power tolerance 0/ +3 to % + 85C

important dynamics of the module. Akhsassi et al. [46] presented an experimental study with thermal modeling of PV modules, and proposed two different models distinguished by whether they account for wind effect or not. According to their findings, proposed models introduced an improved performance in comparison to similar models from literature. Bevilacqua et al. [47] performed an investigation based on an energy balance approach and finite difference approach to investigate the module temperature under spray cooling. The model was aiming to provide thermal field within the module and it was found that the cooling can provide up to 7*.*8% increase in electric power and 28*.*2% decrease in module temperature. Ceylan et al. [48] implemented artificial neural network (ANN), where experimentally controlled solar radiation and ambient tempera ture were used to train the ANN model, and predict module temperature, then its efficiency and power output. Cos¸ kun et al. [49] used ANNs to estimate the module surface temperature based on solar radiation, ambient temperature and wind speed. After assessing several training algorithms, they concluded that ANNs can predict module temperature accurately. Furthermore, Sohani and Sayyaadi [50] determined that best function form for module temperature prediction using genetic pro gramming. Accounting for relative humidity as an effective parameter, they found that proposed function provided significant superior per formance when compared to literature models such NOCT approach. Additionally, Gong et al. [51] implemented an optimization algorithm to investigate the of temperature and radiation on the performance of PV module performance, where they found that the increase in temperature can cause linear decrease in module’s performance. Dong et al. [9] suggested a radial basis function neural network assisted hybrid

modeling in estimation of photovoltaic module’s temperature. Based on the network output, they proposed a correction factor to introduce more generalizability. According to their findings, significant improvement in prediction of cell temperature have been achieved using their approach. Dong et al. [52], proposed radial basis function neural network-based hybrid model to predict PV module cell temperature. Using an optimi zation model with *l*1norm penalty, their model demonstrated accurate predictions and promising results. Shiravi et al. [53] carried out an experimental investigation on the effect of wind velocity and solar ra diation intensity on the performance of solar PV modules. Deriving correlations for module temperature, efficiency, and power output, they showed that the considered parameters have a significant effect on the module performance. Computational fluid dynamics (CFD) simulation was also considered by a number of authors [54–56], for PV module temperature, efficiency, power output and mounting conditions in vestigations, and also for PV/thermal systems [57,58]. Lu and Zhao [59] considered CFD simulation for the study of dust effect on PV modules performance. According to their study, dust deposition reduced the module’s efficiency, with different effect for different dust particles sizes. Wind effect on photovoltaic modules have been considered [60,61], where it was found that wind speed affect the module cooling process and also the pressure distribution on the module’s surfaces. Based on the extended literature review above, the major part of module temperature prediction, was performed using data-driven models and thermal analysis, and only a limited number of studies have considered implementing CFD simulations to predict photovoltaic module temperature and perform parametric studies investigating essential and key factors affecting the temperature of photovoltaic modules and their performance, such as solar radiation, ambient tem perature, or the combination of those parameters with wind speed and mounting conditions. Moreover, many of those studies were focusing only on a specific parameter, such as wind speed, wind direction [62–64], and considering building integrated photovoltaic modules [65–67]. It was also found that in literature, free convection and radi ation heat transfer were often neglected in many cases, which can be important at low wind speeds or high temperature differences. There fore, this work was proposed, aiming to cover those shortcomings and contributes by performing numerical simulations, based on a finite volume method code as a better alternative to other approaches in literature, for the prediction of a free-standing photovoltaic module temperature, under varying ambient conditions. Additionally, this work seeks to provide a comprehensive parametric study on different pa rameters affecting the temperature and performance of photovoltaic modules. This work also intends to provide a novel exportable temper ature model for engineering applications, the work also can be consid ered the first of its kind in the arid climatic condition of south Algeria. Furthermore, the study location typically experiences high levels of solar irradiance, providing an ample sunlight available, which is essential for solar PV systems in similar locations. Besides, the arid climatic of south Algeria also known to have minimal cloud cover, providing consistent and predictable sunlight for solar panels, however, this also may cause significant increase in photovoltaic modules temperature and reducing their efficiency.

**2. Materials and methods**
*2.1. Experimental setup* In order to perform the necessary simulations to predict the module temperature and power output, experimental and in-situ weather data are needed, therefore, a data acquisition system and two identical JONSOL JSP-36 type polycrystalline silicon PV modules were used. Ambient temperature (Ta), solar radiation (G), wind speed (Ws) wind direction (Wd), and module temperature (Tpv) were recorded during December 25, 2022 (sunrise at 07:32 and sunset at 17:30) and January 02, 2023 (sunrise at 07:34 and sunset at 17:35). Moreover, the power

*Energy &RQYHUVLRQ DQG 0DQDJHPHQW 312 (2024) 118563*

other electrical characteristics of the

output of both modules (Ppv) was simultaneously recorded along with other parameters, where data logging interval was set to three (03) seconds, while the average of 30-min will be used during simulations. The experimental setup and PV modules are presented in Fig. 1. The maximum power of one module at Standard Test Conditions (STC) and

**Table 5**

Mesh independency test results and details. ◦ Mesh # Number of elements Tback(

C) Abs. Change
01 714,558 47.840 02 828,688 47.860 0.020 03 993,695 47.877 0.017 04 1,188,376 47.900 0.023 05 1,499,054 47.905 0.005

**Fig. 3.** 3-D view of selected mesh after mesh refinement study.

**Fig. 4.** Validation of the CFD code from present study with study performed by

Aly et al. [21].

temperature (*Ta*) sensor, an anemometer and a wind direction sensor to measure wind speeds (*Ws*) and wind direction (*Wd*), respectively. A relative humidity (RH) sensor, current sensor and voltage divider for each module to measure current and voltage, respectively, which eventually lead to determine the generated power by the photovoltaic modules (*Ppv*). For the temperature of the PV modules (*Tpv*), five K-type thermocouples are mounted in five different locations (one at each corner, and one centered at the middle), on the rear side of each module. Finally, output values from all sensors are transmitted to a microcon troller for storage and treatment purposes and collecting the datasets needed for this work.

*2.2. Error assessment* To analyze and assess the error in predictions of different models in this work, several statistical metrics are implemented. First, the coeffi
cient of determination (*R²*) is used to evaluate the variations in the predicted variable being accounted for by the model, the adjusted and predicted *R*2are also used to assess the quality of the fit with respect to included explanatory variables in the model, and new unseen dataset, respectively. Furthermore, the mean absolute error (MAE) is used to evaluate the average deviation of predicted values from the actually measured ones. In addition, the mean squared error (MSE) and root mean squared error (RMSE) are used to evaluate the error in predictions, giving more weight to large errors and less weight to low errors. Moreover, to estimate the percentage of difference between actual and predicted values, the mean absolute percentage error (MAPE) is used. Mathematical expression of each of those metrics is given as follows: ∑*n*) 2 *in*=1*Yi,measYi,pred* *R* = 1 ∑) (1) *i*=1*Yi,measYi,pred*

1 ∑ *n*⃒ ⃒ ⃒ ⃒ *MAE* = *Yi,measYi,pred*(2) *n* *i*=1

1 ∑

*n*)
2 *MSE* = *Yi,measYi,pred*(3) *n* *i*=1 √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ 1 ∑ *n* ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ) *RMSE* = *Yi,measYi,pred* 2

(4)
*n* *i*=1

*n*⃒⃒ ⃒⃒ 1 ∑ ⃒⃒ *Yi,measYi,pred* ⃒⃒ *MAPE* = (5) *n* *i*=1 *Yi,meas*

where *Yi,meas*and *Yi,pred*are the measured and predicted target variables, respectively. Whereas, *n* is the number of samples, and *Yi,pred*is the mean value of predicted target.

*2.3. Uncertainty analysis* In experimentations, some degree of uncertainty is often present, no matter how accurate an instrument is. The causes can range from in strument sensibility, calibration to ambient conditions effects [68]. One way to estimate that uncertainty is averaging the values of one partic ular variable as best estimate of such variable, by replicating experi ments as much as possible. This procedure was not possible due to the nature of the problem in hand in this study, but the average over a specific time interval of all variables is taken in consideration to reduce potential errors which may occur at some points in during experimen tations. Furthermore, before conducting any measurements, instruments were well calibrated. The calibration process indicated great level of precision for all instruments, where for example, the errors in the solar radiation measurement were only in the range of ∓3% when the process of calibration was performed against the SolData Instruments hand pyranometer (type 105hp). For ambient temperature and relative hu
◦ midity, as indicated by the supplier, the resolution is 0*.*1% and 0 ◦

*.*1 *C*,
and uncertainties of sensors’ measurements are only 5% and 0*.*5 *C*, at maximum, respectively. For the wind direction and wind speed, it was claimed by the supplier, that the devices’ accuracy of measurements is within ∓3%, with the response time not exceeding 1*s*, for an accepted wind speed measurement range of of 0 30*m/s*. Whereas in PV module temperature (*Tpv*), the utilized K-type thermocouples are offering a measuring range of measurement 40 to 400 ◦ *C* with an accuracy of ±

0.75 % and having thermal response time under 0*.*5*s*.
*2.4. Physical model* In this work, 3-Dimensional fluid flow and heat transfer around a free-standing photovoltaic module is investigated. The objective is to model heat conduction within the PV module’s different layers, as well

**Fig. 5.** Weather data collected during 25 December 2022, (a) ambient temperature and solar radiation, and (b) wind speed.

as convective and radiative heat exchanges between the module’s outer surfaces and its surrounding, which will eventually lead to predicting its average temperature, efficiency and power output. For that purpose, a physical model similar to that schemed in Fig. 2 is considered for sim ulations, the fluid (air) domain is of length *L*, width *W* and a height *H*, the PV module is located at one third of the length *L*, and the sur rounding air domain is considered to be large enough so that its boundaries does not affect the solution. The photovoltaic module (Fig. 2) considered for simulations and study purposes, consists of five different layers, from top to bottom, Glass, EVA, PV Cells, EVA, and a back-sheet of Tedlar Polyester Tedlar (TPT), material and thermophys ical properties of different module layers as well as the surrounding air are presented in Table 2.

*2.5. Mathematical formulation* Fluid flows and heat transfer simulations typically involve the nu merical solution of the Navier-Stokes equations, energy equation, and if applicable, some modeling equations to account for turbulence are solved as well. In such case, several approaches for modeling turbulence can be taken, such as the Large Eddy Simulations (LES), an eddy (tur bulent) viscosity modeling approach, or some hybrid combination of both. While the first is computationally expensive, the eddy viscosity approach, which deals with the solution of what is known as the Rey nolds Averaged Navier-Stokes (RANS) equations, is less expensive and provides reasonable results. Therefore, in this work, the two equations *k* ∊ model, which is a widely used turbulence model for such applica tions [55,61,67], is implemented to solve the governing equations in order to obtain the temperature and flow fields and predict the module’s temperature.
*2.5.1. Governing equations* For the free-standing photovoltaic module under investigation, the surrounding air is considered to be an incompressible, with constant thermophysical properties, and the flow was considered to be turbulent. Under those assumptions, the continuity, RANS equations and the en ergy equation can be written as follows: *∂*(*ρui*) = 0 (6) *∂xi* *∂*(*ρu*) *∂*(*ρuiuj*) *∂p ∂*
[ ( *∂u ∂uj*3 *∂uj* )] *∂* () *i* + = + *μ* *i* + *δ* + *ρu*ʹ*u*ʹ *∂t ∂x ∂x ∂x ∂x ∂x* 2 *ij* *∂x ∂x* *i j* *j i i j i j j*

(7)
*∂*(*ρcpT*)) *∂t* + ∇*. ρuicpT* = ∇*.q*+ *Se*(8)

where *ρu*ʹ*iu*ʹ is known as the Reynolds stresses, which must be modeled in*j* order to close the system of governing equations. One of the widely used approaches to model it, is the Boussinesq hypothesis, which is employed in several eddy viscosity turbulence models. In this work, the *k* ∊ tur bulence model is used and it is presented in the numerical procedure section. The source term (*Se*) in Eq. (8) represents the volumetric heat source in the solid PV module, it mainly consists of two terms, one is the absorbed solar radiation, as a positive part of the source term, and the second is delivered electrical power output of the module as the negative part. Its modeling is as follows: *AG Ppv* *S* *e* = *V*

(9)

**Fig. 6.** Temperature contours at different time steps during December 25, 2022 (sunny day), (a) module’s back side, and (b) top side.

()) Initially, the temperature, velocity, and pressure fields of the
*P* *pv*= *ηref*1 *μrefT TrefAG* (10) computational domain were initialized with a constant value (domain averaged) by solving an appropriate Laplace equation for each variable. where *A* and *V* are respectively, the area and volume of the module, *Ppv* is the module’s power output, *ηref*is the module efficiency at STC, *Tref*is the module temperature at reference mode, *μref*is temperature coeffi cient, which is considered to be constant for simplicity, and *T* is the

Additionally, Table 3 summarizes the different boundary conditions applied at the boundaries of the computational domain, which corre sponds to the adequate experimentally collected data, that are used to obtain the numerical solution. module temperature.

*2.5.2. Boundary and initial conditions*
*2.6. Numerical procedure*
In this work, at the inlet of the computational domain, a set of different inlet velocities that corresponds with collected experimental The numerical modeling of fluid flow and heat transfer around a PV data of wind speed are used, in addition to ambient temperature, module, requires the numerical solution of the RANS and energy equa whereas at the outlet, a pressure outlet boundary condition is applied. tions to determine the flow and temperature fields. In order to account The temperature at the boundaries of the domain (left and right sides) for the presence of turbulence in the flow, the *k* ∊ turbulence model is were equal to ambient temperature, while for the top side (sky) the implemented in this work, and thus, two additional transport equations, temperature was calculated using Eq. (11) [63]. The ground tempera for turbulent kinetic energy and its dissipation rate, are solved simul ture (bottom side) was estimated using Eq. (12) [69]: taneously with other governing equations, in the following section the *k* ∊ turbulence model is presented. *T* *sky*= 0*. Ta* *.* (11)

*2.6.1. Modeling turbulence*
*T* *gr*= 17*.*898 + 0*. Ta*(12) ANSYS Fluent CFD code was used to investigate the transient fluid flow and heat transfer phenomena in the considered PV module and the

**Fig. 7.** Temperature contours at different time steps during January 02, 2023 (cloudy day), (a) module’s back side, and (b) top side.

**Fig. 8.** Predicted temperature profiles for the different module layers during December 25, 2022.

air domain surrounding it. Fluent solver, based on the finite volume model was used to model turbulent flow and solve the RANS equations method, was implemented to solve the set of governing equations of numerically, which is an extensively validated turbulence model, and continuity, momentum and energy, for which, standard *k* ∊ turbulence known for its suitability for fully turbulent flows, computational effi

**Fig. 9.** Comparison of simulation results with experimental data and other well-known temperature models, (a) sunny day and (b) cloudy day.

**Table 6** *k²*

*μt*= *ρCμ* Evaluation of the performance different models versus experimental data using ∊ statistical indicators.

|statistical indicators.||||||Here, C|is constant, and the model constants are: C|
|---|---|---|---|---|---|---|---|
|Model|R Sunny day|adj R pre R|RMSE|MAE MSE|MAPE (%)|1.92, δ equations can be found in reference [70]. Those model constants, are among possible reasons that can cause uncertainties in simulations,|= 1.0, δ|
|Present|0.995|0.991 0.991|0.983|0.822 0.966|3.243|since they are determined empirically. Additionally, like any modeling||
|Ross (CFD)|0.996|0.925 0.942|2.912|2.715 8.481|10.386|process, uncertainties associated with turbulence modeling could be||
|King|0.996|0.960 0.963|2.128|2.016 4.530|8.669|caused by other reasons such as turbulence closure and simplifying as||
|Skoplaki|0.993 Cloudy day|0.963 0.964|2.048|1.861 4.196|8.205|sumptions, near-wall region effect modeling, and free stream turbulence and inlet conditions.||
|Present (CFD)|0.988|0.974 0.970|1.702|1.174 2.896|5.199|||
|Ross|0.988|0.935 0.939|2.696|2.535 7.271|16.124|2.6.2.|Modeling radiation|
|King|0.988|0.947 0.939|2.439|2.171 5.947|15.149|In order to account for radiative heat transfer during simulations, the||
|Skoplaki ciency, and robustness. Transport equations for the turbulent kinetic energy k and the dissipation rate ∊ of the turbulence model are given as follows [70]:|0.990 ) [(|0.944 0.931 )]|2.518|2.198 6.339|15.420|surface-to-surface (S2S) radiation model is implemented, a radiation model available in Ansys Fluent, which has been extensively used and validated in literature, known for its computational efficiency, and supports for both transient and steady state simulations. The model as sumes that surfaces are gray and diffuse, emissivity and absorptivity of surfaces are independent of wavelength. Also, the emissivity equals the||
|∂(ρk) + ∂ ρku|= ∂|μ μ ∂k|+ G + G|ρ∊ Y + S|(13)|absorptivity. The model also considers that the surfaces are opaque,||
|∂t|∂x ∂x ) [(|δ ∂x )]||||which lead to neglecting the transmissivity. Additionally, for a diffuse surface, the reflectivity is independent of the outgoing (or incoming)||
|∂(ρ∊) + ∂ ρ∊u|= ∂|μ μ ∂∊ + ρC S|∊ ρC₂|∊ √̅̅̅̅̅ + C|∊ C G + S|directions. [70]. Therefore, the radiative energy leaving a given surface||
|∂t|∂x ∂x|δ ∂x||k + ν∊|k (14)|k is given by Eq. (15): q = ∊|σT⁴ + ρ q|
|where the eddy viscosity μ||is calculated using the following expression:||||where ∊|is the emissivity, σ is the Stefan-Boltzmann constant, and ρ is|
|||||||9||

Here, *Cμ*is constant, and the model constants are: *C*1∊= 1*.*44, *C*2∊= 2 2 2 *k k*= 1*.*0 and *δ*∊= 1*.*3. Further details about the model’s

*j t* *k b M k* *j j k j*

2 *j t* 1∊ 3∊ *b* ∊ *j j* ∊ *j*

*out,k k k k in,k*(15)

*t* *k*

◦ *back*

1 ∊*k*, while *qin,k*is the energy flux incident on the same surface. The amount of that energy is a function of what is known as the “view factor *F* *jk* ”. *qin,k*can be calculated using the following equation: ∑ *n* *Akqin,k*= *Ajqout,jFjk*(16) *j*

Here, *Ak*is the area of the surface *k* and *Fjk*is the view factor between the area *j* and *k*. *n* is the number of contributing surfaces. The emissivity coefficients for the different surfaces in the model are shown in Table 4.

*2.6.3. Mesh sensitivity test* A mesh independency test was performed to ensure the accuracy of the solution, and eliminate any possible uncertainties associated with insufficient grid resolution near walls and boundaries. Thus, for all simulations, numerical results were obtained using the standard *k* ∊ turbulence model, in combination with the Enhanced Wall Treatment’s wall functions, where values of *Y*+= 1 were desired for the numerical resolution of the near wall region to ensure accurate prediction of the wall shear stress and wall heat transfer. Additionally, first and second order accurate discretization schemes were preferred for the temporal and spatial discretization of the different terms of the governing equa tions, respectively. Furthermore, the Coupled algorithm was used to solve the pressure–velocity coupling for all simulations, which, despite being computationally heavy, it has some advantages over other algo rithms as a fully implicit algorithm. Results and details of the mesh refinement study are shown in Table 5. Considering mesh elements number, simulation time and the rate of change in the module’s back temperature (*Tback*). It can be noted that mesh 04, which is shown in
Fig. 3, can be taken as an optimum mesh for the subsequence simula
 tions, as it provides accurate results for predicted temperature, and further refinement in the mesh beyond that is just more computational cost.
*2.6.4. Validation* In order to validate the accuracy of the numerical model in this study, the experiments of Aly et al. [21] were simulated using their experimental data, under the same condition of solar radiation, ambient temperature, and wind speed for the day of June 25, 2014, and the same material properties and dimensions from their study, by implementing the CFD code from this study. In comparison with experimental data from their study, it was found that the results from present CFD code predicted the PV module temperature during the day of June 25, 2014 with a high level of accuracy during day period, as it is shown in Fig. 4,
*s a*

which makes the model in present work suitable and reliable for current investigation.

**3. Results and discussion** In this work, module temperature of free-standing polycrystalline silicon photovoltaic module is predicted using CFD simulations, which will be used to estimate the photovoltaic power output. In addition, the effects of different parameters influencing the performance of the module are investigated in a separated parametric study. Therefore, experimental data was used to perform numerical simulations, where ambient temperature (*Ta*), solar radiation (*G*) and wind speed (*Ws*) were recorded during December 25, 2022 (sunrise at 07:32 and sunset at 17:30), and January 02, 2023 (sunrise at 07:34 and sunset at 17:35). For illustration, the experimental data during the two days are shown in
Fig. 5. Environmental conditions during that day have a typical trend,
 solar irradiation and ambient temperature show a tendency of rising during morning to noon time, and afterwards decay during the after noon to evening. On the other hand, wind speed values, have some kind of a random behavior.
*3.1. Temperature prediction* The temperature distribution on the module’s top and back surfaces, at different hours of the day during 25 December 2022 (sunny day), are shown in Fig. 6, where the nonuniform temperature distribution can be observed. This distribution is mainly caused by the complex flow phe nomena around the module, which resulted in a nonuniform heat transfer coefficient. Also, the back side of the module has the higher temperature values, which is due to weak heat transfer rate that is caused by the wake formed at the module’s back surface. The lower edges of the module are cooled by the effect of the wind and the lower ambient temperature, while during morning and late afternoon time, the ambient temperature is almost equal or even higher than the module’s temperature. Regardless of the fact that the season was winter, and the temperature are relatively low, module temperature during day times can reach values that are significantly higher than ambient temperature, which indicates the possibility of making use out of that heat in a several ways. For the cloudy day, generally similar temperature distribution was obtained (Fig. 7), however, the back-side temperature was reduced significantly during noon time, the difference from sunny day during the same period was at the limits of 10
◦

*C*. The temperature difference is
**Fig. 10.** Temperature contours of *T* at different solar radiation values for *W* = 1*m/* s and *T* = 30

*C*.

**Fig. 11.** Variation of *Tback*as function of *G*, (a) for different wind speeds and (b)

for different ambient temperature.

mostly due to lower radiation hitting the module surface, but also because of the lower ambient temperature, where the maximum ambient temperature difference (sunny and cloudy days) was at 8*.*62 ◦ *C*, resulting in the aforementioned temperature drop in module’s back- side. The CFD simulations also allows to predict and capture the heat conduction within the solid PV module itself. As it can be noted in Fig. 8, the average temperature variation at different layers of the module shows that, as it is expected, higher temperature values at cells layer, followed by the back-side temperature, while the top-side layer has the lowest temperature values, this is due to the fact that cells layer absorbs most of the heat energy. The maximum temperature difference (*TcellsTback*) was found to be 0*.*797 ◦ *C*, while the (*TcellsTtop*) difference was 1*.* ◦ *C*, which falls in the intervals indicated within references in the literature. In addition, it can be observed from the graph, that the difference in temperature between different layers gets higher at high solar radiation (*G*) values, which is typically at noon period and drops

down at lower values of *G*. To assess and quantify the errors and un certainties in simulation results and experimental data according to the ASME (American Society of Mechanical Engineers) methodology [71], where, given that *S* denotes the simulation results and *D* denotes the experimental data, the comparison error is given by *E* = *S D*, in this work, the maximum error for results obtained during sunny day was 2*.* 4 ◦ *C* with an average of only 0*.*32 ◦ *C*, whereas during cloudy day, those values were 5*.*3 ◦ *C* and 0*.*53 ◦ *C*, respectively. The numerical results for the prediction of module temperature based on CFD simulations are compared against experimental data, as well as with other well-known photovoltaic modules’ temperature models. The results of comparison are presented in Fig. 9, where it can be seen that CFD simulation results are in very good agreement with experimental data. For different climatic conditions of a sunny day (Fig. 9 (a)) and cloudy day (Fig. 9 (b)), the numerical simulations, relaying on the physics of fluid flow and heat transfer phenomena, are accurately estimating the module temperature and outperforming other models. Additionally, taking into account radiation and free convection heat transfer in this wok improved the prediction accuracy and resulted in well estimated results of photovoltaic module temperature. In com parison to other models, and in particular, during sunny day, other models are overestimating the module temperature, specifically, the average deviation caused by Ross, King, and Skoplaki models was at

2*.*38 ◦ *C*, 1*.*68 ◦ *C*, and 1*.*49
◦ *C*, while it was only at 0*.*32 ◦ *C* for the numerical simulation. The performance of different models considered in this work is also evaluated using several statistical metrics. The results of this evaluation are shown in Table 6, from which, it can be noted that numerical sim ulations performed in this work, presents the best performance when compared to experimental data, attaining a high correlation coefficient of 0*.*995 and high adjusted and predicted *R*2as well. The error in sim ulations results was also lower than all other models, specifically, and for the day of December 25, 2022 (sunny day) the MAE of module temperature resulted in by numerical simulations was only 0.822, while for other models, that error was as large as 2.715, 2.016, and 1.861 for Ross, King and Skoplaki models, respectively. For the cloudy day, the errors were a bit larger, but still, the CFD simulation are more accurate in predicting the module temperature, and showing good agreement with experimental data, as it is indicated by the values of correlation coefficient, as well as the adjusted and predicted *R²*. The error values for the CFD based module temperature were 1.702, 1.174, and 2.896 in terms of RMSE, MAE, and MSE, respectively, which can be considered well better than the results of other statistical models considered in this work. More detail about the statistics of the different models is presented in Table 6.

*3.2. Parametric study* In this section, a parametric study of the influencing parameters on module temperature is carried out, to investigate the effects of different parameters on the module temperature, and hence, its power output. The investigated parameters involve wind speed, inclination angle, solar radiation and ambient temperature, in addition, the combination of those parameters is also examined.
*3.2.1. Effect of solar radiation* Firstly, the effect of solar radiation on module temperature is investigated in this work, a wide range of solar radiation have been considered, varying from 100 to 1000*W/m²*.
◦ The investigation was carried out at an angle of inclination of *α* = 33, for different ambient temperature and wind speed values. Results of simulations in terms of temperature contours are shown ◦ in Fig. 10, which indicates that at an ambient temperature of 30 *C*, a wind speed of 1*m/s*, and a solar radia tion of 100*W/m²*, resulted in a low and fairly uniform temperature distribution on the back-side of the module. On the other hand, a

**Fig. 12.** Temperature contours of *Tback*at different ambient temperature for *Ws*= 1*m/s* and *G* = 700*W/m²*.

**Fig. 13.** Variation of *Tback*as function of *Ta*for different wind speeds.

nonuniform temperature distribution is obtained for higher solar radi ations, such as 550 and 1000*W/m²*. Additionally, *Tback*increases ◦ significantly with the increase in *G*, and Δ*T* can exceed 20 *C* at *G* = 1000*W/m²*. As it is shown in Fig. 11, it was also found that, *Tback*in creases linearly with *G*, this approves the results obtained in literature [23,55]. The slop of the graph Δ*T* versus *G* is significantly different for different wind speed values, indicating that *Ws*has significant impact on the rate of change in module temperature, which can be referred to change in the strength of convective cooling for different wind speed values. However, for constant *Ws*of 1*m/s* and different ambient tem perature, the rate of increase in *Tback*is similar in nature, but also it can be seen that, for a given solar radiation value, an increase in *Ta*of 30 ◦ *C*, results in an increase in module temperature of 5*.*8 ◦ *C* at an average.

*3.2.2. Effect of ambient temperature* Another key parameter in solar photovoltaics, is ambient air tem perature, in this work, its effect on module temperature is investigated at different wind speeds. Results from simulations are shown in terms of
temperature contours of *Tback*for different ambient temperature at a *Ws* of 1*m/s* (Fig. 12), where it reveals that, firstly, a significant temperature rise in *Tback*is caused by the increase in *Ta*at constant *G* and *Ws*. Additionally, lower *Ta*seems to help reducing *Tback*by increasing the heat transfer rate due to larger temperature gradient. The variation of *T* *back*as a function of *Ta*is shown in Fig. 13, which shows that module temperature scales linearly with *Ta*at constant wind speed, this tend to agree with experimental data and results in literature [23], however, as *Ws*gets higher, *Tback*is reduced due to wind-generated cooling via forced convection, and the increase in turbulence and mixing associated with the increase in inertia forces. It is also noted that, the rate of reduction in module temperature gets lower with the increase in wind speed. For example, when the wind speed increase from almost no wind (0*.*01) to 1*m/s*, an average temperature drop of 13*.*97 ◦ *C* is attained, while that drop is found to be only 1*.*47 ◦ *C* as wind speed increases from 3*.*66 to 5*m/s*.

*3.2.3. Effect of wind speed* The effect of wind speed on the module temperature, at different mounting angle of inclination (*α*), was also investigated in this work. Back-side temperature contours are shown in Fig. 14 at different wind speed values for *α* = 33, the figure shows the dominance of free con vection at low wind speed, which leads to higher thermal resistance, and as a result, higher module temperature over the module’s surface, whereas increasing wind speed, introduces more forced convective cooling which helps reducing the module temperature. The variation of *T* at different wind speed values and for different inclination angles is *back* shown in Fig. 15, where it can be observed that, as expected, the cooling effect of the wind on the module temperature gets larger with higher values of wind speed, which agrees with the results in literature [54]. However, that difference in cooling effect is negligible for almost all *α* values at low *Ws*, this is due to the fact that at low wind speed values, the buoyancy driven (natural) convection gets dominant, which lead to lower heat transfer coefficient, resulting in weaker cooling by the con vection mechanism. While, at high wind speed values, the cooling pro cess is more and more dominated by forced convection which leads to higher cooling rate. On the other hand, at wind speeds closer to 1*m/s* and higher, the effect of *α* on the cooling process of the module by the wind starts to be significant, where at high inclination angles such as 60 and 90 degrees, the cooling process of the module is relatively slower and inefficient, whereas, at *α* values of less than 60 degrees, lower module temperature is obtained and more efficient cooling is observed.

◦

**Fig. 14.** Temperature contours of *T* at different wind speed values for *T* = 30

*C*, *G* = 700*W/m*2and *α* = 33. *back*

**Fig. 15.** Module back-side temperature at different values of wind speed and

for different angles on inclination.

*3.2.4. Effect of angle of inclination* One other factors influencing the fluid flow and heat transfer for the photovoltaic module is its mounting angle (*α*). The effect of this parameter at an ambient temperature of 30
◦ *C*, solar radiation of 700*W/m²*, and for different wind speed values is also investigated in this work. Temperature contours from simulation results of *α* = 0 ◦, 33 ◦, and 60 ◦ are shown in Fig. 16, and as it is clearly noted, the temperature distribution on module’s surface is highly affected by the angle of inclination. However, as the plot of variation of *Tback*with *α* values in

Fig. 17 shows, the average temperature of the module is almost inde

pendent of *α* values, which consent with the results in literature [55]. However, with the exception of the case of very low wind speed, where it can be seen that a small continues drop in *Tback*occurs by increasing *α* values from 0 to 90 degrees due to the dominance of buoyancy-driven convection, and since the module is normally hotter than its surround ing, the boundary layer breaks up and forms plumes at the top surface, decreasing the thermal resistance. Thus, the heat transfer rate increases

*a*

relatively with the increase in *α*. Additionally, it can be noted that for all wind speeds, the best wind-generated cooling is obtained at *α* = 33 ◦.

*3.3. Regression-based temperature model* Having carried out a parametric study, along with the experimental and numerical data in hand, a regression-based model equation is developed for the prediction of module temperature based on climatic data. The model takes solar radiation, ambient temperature, and wind speed as inputs where solar radiation (*G*) can have a constant coefficient to scale it down and account for its larger magnitude. On the other hand, as it was found, *Tpv*scales linearly with *Ta*, and to some extent, decreases exponentially with wind speed. Thus, the model would potentially have *T* *a*scaled by a constant factor to account for its linear relation with the target (*Tpv*), while wind speed would be scaled by a constant factor at the exponent of an exponential function taking into account its negative effect on the target. The proposed model can potentially take the form of Eq. (17): *T* *pv*= *aTa*+*bGe*
*cWs* (17)

The constants *a*, *b*, and *c* appearing in the equation above were determined to be 0*.*905, 0*.*0291, and 0*.*031, respectively. To assess the sensitivity of the predicted target (*Tpv*) with respect to each input, a sensitivity analysis on the considered input and their effect on module temperature is performed, which revealed that, at an ambient temper ature of 30 ◦ *C*, a solar radiation of 700*W/m²*, and a wind speed of 1 *m/s*, the predicted module temperature by Eq. (17) is 46*.*9 ◦ *C*, which is very representative and reasonable approximation compared to available experimental data. The analysis also showed that, while holding other inputs constant, an increase in *Ta*from 0 to 47 ◦ *C*, would yield an increase in *Tpv*of about 42 ◦ *C*, while the increase in *G* from 0 to 1000*W/m²*, at *T* *a*= 30 ◦ *C* and *Ws*= 1*m/s*, resulted in a 28 ◦ *C* increase in the module temperature, whereas, increasing wind speed from 0 to 10*m/s*, at *Ta*= 30 ◦ *C* and *G* = 700*W/m²*, yielded a decrease in *Tpv*of about 5*.*6 ◦ *C*, which indicates that the considered input variables are significantly affecting module temperature. The proposed model was validated and tested on new data (03–01-2023) of input values with solar radiation of up to *G* = *W/m²*, maximum ambient temperature of *T* = 26 ◦ *C*, and wind *a* speed of up to *W* = 2 *m/s* and compared to other models and results are *s* presented in Fig. 18. The results show that proposed model well repre sents experimental data and is more accurate in predicting *Tpv*. The statistics of the model in present work, shows a coefficient of

◦

**Fig. 16.** Temperature contours of *T* for different *α* values at *W* = 1 *m/s*, *T* = 30

*C*, and *G* = 700*W/m²*. *back*

**Fig. 17.** Module back-side temperature for different *α* and wind speed values.

determination of 0.989, an adjusted and predicted *R*2of 0.987. The error of prediction using this model was at 1.009 and 1.703 in terms of MAE and MSE, respectively. Furthermore, the standard error of the model was only 1.363, which is 10*.*4% more accurate than the best results obtained by the tested models from literature.

**4. Conclusion** In this study, 3D CFD simulations, have been implemented to esti mate and predict the back-side temperature of a 160 W PV module using experimental data. Experiments were carried out in the south-east of Algeria, during December 25, 2022, January 02 and 03, 2023. Following a mesh refinement study and model validation, the governing equations of fluid flow and heat transfer around a free-standing PV module were solved numerically using ANSYS Fluent CFD code, and module tem perature is determined. Unlike many other studies, a detailed parametric study of the essential parameters and their combination have been considered in this study, where all heat transfer mechanisms have been taken into account, Moreover, this work was a unique investigation and
*s a*

prediction of module temperature under varying ambient conditions in an arid climatic condition. To assess the results, several statistical in dicators were used, and a comparison with models from literature was also carried out. Additionally, a parametric study on the effective pa rameters was performed. Built upon the results yielded in this study, the following concluding points can be drawn:

- The numerical solution, relaying on the physics of fluid flow and heat transfer phenomena around the free-standing PV module, resulted in accurate prediction of module temperature, which will improve power output estimation.
- When compared to models from literature, and experimental data, the numerically estimated *Tback*was in well agreement with experi mental data, more accurate, and produced lower error.
- Statistically, CFD simulations provided an estimated *Tback*with an *R*2 of 0.995, an adjusted and predicted *R*2of 0.991, with a MAE of 0.822. On the other hand, the best model from literature, achieved values of
0.993, 0.963, and 0.964 in terms of *R²*, an adjusted *R²*, and predicted *R*2with MAE of 1.861.
- Different parameters have different impact on the *Tback*where it was found that it scales linearly with solar radiation *G* and ambient temperature *Ta*, while a nonlinear drop was observed due to increasing *Ws*.
- For moderate to high *Ws*values, when forced convection is the dominant mechanism, the effect of *α*, the inclination angle, is almost negligible, while for a free convection dominant flow, a relatively small drop in *Tback*is noted for the increase in *α*.
- The proposed regression-based model, providing very reasonably
2 accurate results, presents a coefficient of 2 determination (*R*) of

0.989, and both adjusted and predicted *R* of 0.987, and a MAE of
1.009. This is 10% more accurate than the best model from literature.
- The proposed models can be used for engineering application such as predicting power plant efficiency and power output calculations, and software involving photovoltaic systems. However, further testing and validation are needed for scenarios that are significantly different form that of present work. Overall, a detailed and comprehensive numerical simulations have been carried out in this work, which resulted in more accurate estima tion of module temperature. Each of the investigated parameters in this work have their own effect on *T*, where based on that, a regression model was developed with better
*back* performance and accurate estimation

**Fig. 18.** Comparison of proposed model results with experimental data and other models from literature.

of module temperature. In future investigations, further aspects of the topic can be considered, such as considering different climatic condi tions, different modeling approaches, and more parameters such as wind direction and sun position (angle).

**CRediT authorship contribution statement**

**Abdelhak Keddouda:** Writing – original draft, Validation, Software, Methodology, Investigation, Formal analysis, Conceptualization. **Razika Ihaddadene:** Writing – review & editing. **Ali Boukhari:** Writing – review & editing, Software, Methodology, Formal analysis, Concep tualization. **Abdelmalek Atia:** Writing – review & editing, Conceptu alization. **Müslüm Arıcı:** Writing – review & editing, Methodology, Formal analysis. **Nacer Lebbihiat:** Writing – original draft, Investiga tion. **Nabila Ihaddadene:** Writing – review & editing.

**Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Data availability**

The data that has been used is confidential.

**Acknowledgements**

The first author thankfully acknowledges the support of Directorate- General for Scientific Research and Technological Development (Min istry of Higher Education and Scientific Research) for PhD scholarship and facilitating this research work.

**References**

[1] Govindasamy D, Daniel F, Kumar A. Performance enhancement of photovoltaic system using composite phase change materials. Energy 2024;288:129871. [2] Keddouda A, Ihaddadene R, Boukhari A, Atia A, Arıcı M, Lebbihiat N, et al. Solar photovoltaic power prediction using artificial neural network and multiple regression considering ambient and operating conditions. Energ Conver Manage 2023;288:117186. [3] Ma X, Li M, Peng Y, Sun L, Chen C. Development of thermo–electrical loss model for photovoltaic module with inhomogeneous temperature. Energy 2022;248: 123542. [4] Hasan K, Yousuf SB, Tushar MSHK, Das BK, Das P, Islam MS. Effects of different environmental and operational factors on the PV performance: A comprehensive review. Energy Sci Eng 2022;10:656–75.

[5] Korab R, Połomski M, Naczynski ´ T, Kandzia T. A dynamic thermal model for a photovoltaic 2023;280:116773 module. under varying atmospheric conditions. Energ Conver Manage

[6] Skoplaki E, Palyvos JA. On the temperature dependence of photovoltaic module electrical performance: A review of efficiency/power correlations. Sol Energy 2009;83:614–24. [7] Vidyanandan K. An overview of factors affecting the performance of solar PV systems. Energy Scan 2017;27:216. [8] Bailek N, Bouchouicha K, Hassan MA, Slimani A, Jamil B. Implicit regression-based correlations to predict the back temperature of PV modules in the arid region of south Algeria. Renew Energy 2020;156:57–67. [9] Dong X-J, Shen J-N, He G-X, Ma Z-F, He Y-J. A general radial basis function neural network assisted hybrid modeling method for photovoltaic cell operating temperature prediction. Energy 2021;234:121212. [10] Muzathik simple correlation.

A. Photovoltaic Int J Energy modules
Eng operating 2014;4:151 temperature. estimation using a

[11] Nguyen DPN, Neyts K, Lauwaert J. Proposed models to improve predicting the operating temperature of different photovoltaic module technologies under various

[12] climatic Ziane A, conditions. Dabou R, Necaibia Appl Sci A, 2021;11:7064 Sahouane N,. Mostefaoui M, Bouraiou A, et al. Tree- based ensemble methods for predicting the module temperature of a grid-tied photovoltaic system in the desert. Int J Green Energy 2021;18:1430–40. [13] Keddouda A, Ihaddadene R, Boukhari A, Atia A, Arıcı M, Lebbihiat N, et al. Photovoltaic module temperature prediction using various machine learning algorithms: Performance evaluation. Appl Energy 2024;363:123064. [14] Kaplanis S, Kaplani E. A new dynamic model to predict transient and steady state PV 12:2temperatures. taking into account the environmental conditions. Energies 2018;

[15] Lobera DT, Valkealahti S. Dynamic thermal model of solar PV systems under varying climatic conditions. Sol Energy 2013;93:183–94. [16] Osma-Pinto G, Ordo´nez-Plata ˜ G. Dynamic thermal modelling for the prediction of the operating temperature of a PV panel with an integrated cooling system. Renew Energy 2020;152:1041–54. [17] Abdolzadeh M, Zarei T. Optical and thermal modeling of a photovoltaic module and experimental evaluation of the modeling performance. Environ Prog Sustain Energy 2017;36:277–93. [18] Gholami A, Ameri M, Zandi M, Ghoachani RG. Electrical, thermal and optical modeling of photovoltaic systems: Step-by-step guide and comparative review study. Sustainable Energy Technol Assess 2022;49:101711. [19] Gu distributions W, Wang X, of Bai a photovoltaic

X. Coupled optical-electrical-thermal module. Energ Conver Manage
loss modelling 2023;276:116476 and energy. [20] Hassan A, Abbas S, Yousuf S, Abbas F, Amin N, Ali S, et al. An experimental and numerical study on the impact of various parameters in improving the heat transfer performance Energy 2023;202:499 characteristics –512. of a water based photovoltaic thermal system. Renew [21] Aly SP, Ahzi S, Barth N, Abdallah A. Using energy balance method to study the thermal behavior of PV panels under time-varying field conditions. Energ Conver Manage 2018;175:246–62. [22] Prilliman M, Stein JS, Riley D, Tamizhmani G. Transient weighted moving-average model of photovoltaic module back-surface temperature. IEEE J Photovoltaics 2020;10:1053–60. [23] Zhou J, Yi Q, Wang Y, Ye Z. Temperature distribution of photovoltaic module based on finite element simulation. Sol Energy 2015;111:97–103. [24] R. Ross Jr. Interface design considerations for terrestrial solar cell modules. 12th Photovoltaic specialists conference1976. pp. 801-6. [25] T. Nordmann, L. Clavadetscher. Understanding temperature effects on PV system performance. 3rd World Conference onPhotovoltaic Energy Conversion, 2003 Proceedings of. IEEE2003. pp. 2243-6. [26] Mondol JD, Yohanis Y, Smyth M, Norton B. Long-term validated simulation of a building integrated photovoltaic system. Sol Energy 2005;78:163–76.

[27] Mondol JD, Yohanis YG, Norton B. The effect of low insolation conditions and inverter oversizing on the long-term performance of a grid-connected photovoltaic system. Prog Photovolt Res Appl 2007;15:353–68. [28] Mondol JD, Yohanis YG, Norton B. Comparison of measured and predicted long term performance of grid a connected photovoltaic system. Energ Conver Manage 2007;48:1065–80. [29] T. Schott. Operation temperatures of pv modules: a theoretical and experimental approach. EC Photovoltaic solar energy conference 61985. pp. 392-6. [30] Durisch W, Bitnar B, Mayor J-C, Kiess H, Lam K-H, Close J. Efficiency model for photovoltaic modules and demonstration of its application to energy yield estimation. Sol Energy Mater Sol Cells 2007;91:79–84. [31] Lasnier F. Photovoltaic engineering handbook. CRC Press; 1990. [32] J.-M. SERVANT. Calculation of the cell temperature for photovoltaic modules from climatic data. Intersol Eighty Five. Elsevier1986. pp. 1640-3. [33] D.L. King. Photovoltaic module and array performance characterization methods for all system operating conditions. AIP conference proceedings. American Institute of Physics1997. pp. 347-68. [34] D.L. King, J.A. Kratochvil, W.E. Boyson. Field experience with a new performance characterization procedure for photovoltaic arrays. Sandia National Lab.(SNL-NM), Albuquerque, NM (United States)1997. [35] G. TamizhMani, L. Ji, Y. Tang, L. Petacci, C. Osterwald. Photovoltaic module thermal/wind performance: long-term monitoring and model development for energy rating. NCPV and Solar Program Review Meeting Proceedings, 24-26 March 2003, Denver, Colorado (CD-ROM). National Renewable Energy Lab., Golden, CO. (US)2003. [36] D.L. King, J.A. Kratochvil, W.E. Boyson. Photovoltaic array performance model. Citeseer2004. [37] Skoplaki E, Boudouvis A, Palyvos J. A simple correlation for the operating temperature of photovoltaic modules of arbitrary mounting. Sol Energy Mater Sol Cells 2008;92:1393–402. [38] Almaktar M, Rahman HA, Hassan MY, Rahman S. Climate-based empirical model for PV module temperature estimation in tropical environment. Appl Solar Energy 2013;49:192–201. [39] Kaplanis S, Kaplani E, Kaldellis J. PV temperature and performance prediction in free-standing, BIPV and BAPV incorporating the effect of temperature and inclination on the heat transfer coefficients and the impact of wind, efficiency and ageing. Renew Energy 2022;181:235–49. [40] Hove T. A method for predicting long-term average performance of photovoltaic systems. Renew Energy 2000;21:207–29. [41] Mattei M, Notton G, Cristofari C, Muselli M, Poggi P. Calculation of the polycrystalline PV module temperature using a simple method of energy balance. Renew Energy 2006;31:553–67. [42] Tiwari A, Sodha M. Performance evaluation of solar PV/T system: An experimental validation. Sol Energy 2006;80:751–9. [43] Tiwari A, Sodha M. Performance evaluation of hybrid PV/thermal water/air heating system: a parametric study. Renew Energy 2006;31:2460–74. [44] Migliorini L, Molinaroli L, Simonetti R, Manzolini G. Development and experimental validation of a comprehensive thermoelectric dynamic model of photovoltaic modules. Sol Energy 2017;144:489–501. [45] Gu W, Ma T, Shen L, Li M, Zhang Y, Zhang W. Coupled electrical-thermal modelling of photovoltaic modules under dynamic conditions. Energy 2019;188: 116043. [46] Akhsassi M, El Fathi A, Erraissi N, Aarich N, Bennouna A, Raoufi M, et al. Experimental investigation and modeling of the thermal behavior of a solar PV module. Sol Energy Mater Sol Cells 2018;180:271–9. [47] Bevilacqua P, Bruno R, Rollo A, Ferraro V. A novel thermal model for PV panels with back surface spray cooling. Energy 2022;255:124401. [48] Ceylan I, ˙ Erkaymaz O, Gedik E, Gürel AE. The prediction of photovoltaic module temperature with artificial neural networks. Case Stud Therm Eng 2014;3:11–20.

[49] C. COSKUN, N. Koçyigit, ˘ Z. OKTAY. Estimation of pv module surface temperature using artificial neural networks. Mugla Journal of Science and Technology. 2 (2016) 15-8. [50] Sohani A, Sayyaadi H. Employing genetic programming to find the best correlation to predict temperature of solar photovoltaic panels. Energ Conver Manage 2020; 224:113291. [51] Gong Y, Wang Z, Lai Z, Jiang M. TVACPSO-assisted analysis of the effects of temperature and irradiance on the PV module performances. Energy 2021;227: 120390. [52] Dong X-J, Shen J-N, Ma Z-F, He Y-J. Simultaneous operating temperature and output power prediction method for photovoltaic modules. Energy 2022;260: 124909. [53] Shiravi AH, Firoozzadeh M, Lotfi M. Experimental study on the effects of air blowing and irradiance intensity on the performance of photovoltaic modules, using central composite design. Energy 2022;238:121633. [54] Dabaghzadeh N, Eslami M. Temperature distribution in a photovoltaic module at various mounting and wind conditions: a complete CFD modeling. J Renewable Sustainable Energy 2019;11. [55] Jaszczur M, Teneta J, Hassan Q, Majewska E, Hanus R. An experimental and numerical investigation of photovoltaic module temperature under varying environmental conditions. Heat Transfer Eng 2021;42:354–67. [56] Kim J, Nam Y. Study on the cooling effect of attached fins on PV using CFD simulation. Energies 2019;12:758. [57] Yildirim MA, Cebula A. A numerical and experimental analysis of a novel highly- efficient water-based PV/T system. Energy 2024;289:129875. [58] Herrando M, Fantoni G, Cubero A, Simon-Allu ´ ´e R, Guedea I, Fueyo N. Numerical analysis of the fluid flow and heat transfer of a hybrid PV-thermal collector and performance assessment. Renew Energy 2023;209:122–32. [59] Lu H, Zhao W. CFD prediction of dust pollution and impact on an isolated ground- mounted solar photovoltaic system. Renew Energy 2019;131:829–40. [60] Abiola-Ogedengbe A, Hangan H, Siddiqui K. Experimental investigation of wind effects on a standalone photovoltaic (PV) module. Renew Energy 2015;78:657–65. [61] Chowdhury MG, Goossens D, Goverde H, Catthoor F. Experimentally validated CFD simulations predicting wind effects on photovoltaic modules mounted on inclined surfaces. Sustainable Energy Technol Assess 2018;30:201–8. [62] Goverde H, Goossens D, Govaerts J, Dubey V, Catthoor F, Baert K, et al. Spatial and temporal analysis of wind effects on PV module temperature and performance. Sustainable Energy Technol Assess 2015;11:36–41. [63] Kaplani E, Kaplanis S. Thermal modelling and experimental assessment of the dependence of PV module temperature on wind velocity and direction, module orientation and inclination. Sol Energy 2014;107:443–60. [64] Schwingshackl C, Petitta M, Wagner JE, Belluardo G, Moser D, Castelli M, et al. Wind effect on PV module temperature: Analysis of different techniques for an accurate estimation. Energy Procedia 2013;40:77–86. [65] Mirzaei PA, Zhang R. Validation of a climatic CFD model to predict the surface temperature of building integrated photovoltaics. Energy Procedia 2015;78: 1865–70. [66] Roeleveld D, Hailu G, Fung A, Naylor D, Yang T, Athienitis A. Validation of computational fluid dynamics (CFD) model of a building integrated photovoltaic/ thermal (BIPV/T) system. Energy Procedia 2015;78:1901–6. [67] Zhang R, Mirzaei PA, Carmeliet J. Prediction of the surface temperature of building-integrated photovoltaics: Development of a high accuracy correlation using computational fluid dynamics. Sol Energy 2017;147:151–63. [68] J.P. Holman. Experimental Methods for Engineers, EIGHTH EDITION, 2011. [69] Ouzzane M, Eslami-Nejad P, Badache M, Aidoun Z. New correlations for the prediction of the undisturbed ground temperature. Geothermics 2015;53:379–84. [70] ANSYS. ANSYS Fluent Theory Guide. ANSYS Inc ed2018. [71] Rakhimov AC, Visser D, Komen E. Uncertainty Quantification method for CFD applied to the turbulent mixing of two water layers. Nucl Eng Des 2018;333:1–15.
