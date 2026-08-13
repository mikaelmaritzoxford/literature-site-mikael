Renewable Energy 68 (2014) 378e396

Contents lists available at ScienceDirect

# Renewable Energy

journal homepage: www.elsevier.com/locate/renene

## Experimental operating cell temperature assessment of BIPV with different installation configurations on roofs under

## Mediterranean climate

a, * b a

### M. D’Orazio, C. Di Perna, E. Di Giuseppe

aConstruction, Civil Engineering and Architecture Department, Università Politecnica delle Marche, Via Brecce Bianche, 60131 Ancona, Italy bIndustrial Engineering and Mathematics Sciences Department, Università Politecnica delle Marche, Via Brecce Bianche, 60131 Ancona, Italy

#### article info abstract

Article history: The presence of an air gap between a photovoltaic (PV) module and roof facilitates ventilation cooling Received 30 July 2013 under the device and consequently reduces cell temperature and improves its performance. In case of Accepted 6 February 2014 rack-mounted PV installation, the Nominal Operating Cell Temperature (NOCT) method could be effec- Available online 6 March 2014 tively used to predict the temperature of the module for various environmental conditions. Many countries, for esthetic purposes, offer economic advantages (tax deductions, incentives, etc.) Keywords: for the installation of building integrated photovoltaic modules (BIPV), with water-tightness capability Photovoltaic and adequate mechanical resistance in order to substitute tile covering or part of it. Nevertheless, poor or BIPV absent ventilation under BIPV panels could cause them to overheat and reduce their efficiency. Lack of Cell temperature NOCT validated predictive tools for the evaluation of BIVP energy performance could be another barrier to their Sandia National Laboratory model widespread application. In this study, we investigated the thermal performance of PV modules installed in a real scale experimental building over a traditional clay tile pitched roof in Italy for almost one year (from August 2009 to June 2010). One PV module was rack-mounted over the roof covering with a 0.2 m air gap; the others were fully integrated and installed at the same level of the roof covering (one with an air gap of

0.04 m, the other mounted directly in contact with the insulation). Temperature and heat flux measurements for each panel, and environmental parameters were recorded. Two temperature prediction models, NOCT model and SNL (Sandia National Laboratory) model were used to predict BIPV temperature and energy efficiency so that their suitability for BIPV could be eval- uated. SNL model takes into account also the wind speed. Experimental results demonstrate that even though the rack-mounted PV module constantly main- tains cell temperature below that of the other full-building integrated modules, due to the presence of a higher air gap, the difference in the energy produced by the BIPV modules estimated for the entire monitoring period is less than 4%. The two predictive models, NOCT and SNL, cause the differences in predicted and calculated tem- perature up to 10 C. However, subsequent percentage variations on the energy predicted compared to that arising from the temperature measured generally turn out to be lower than 5%. An optimization of empirical coefficients used for calculations based on the SNL method allows for the reduction of this value below 2.5%.
2014 Elsevier Ltd. All rights reserved.

|1. Introduction||||||established|and documented|[1e3]. Consequently,|a very|large|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||number of correlations expressing the temperature dependence of|||||
|The|importance|of operating|temperature|in relation|to the|the PV electrical efficiency can be retrieved. The module efficiency|||||
|electrical|efficiency|of a Photovoltaic|(PV)|device is|very well|at Standard Test Conditions (STC) is defined at 25 the wind speed and the type of mounting of the PV modules (free-|||C. Depending on||
|* Corresponding author. Tel.: þ39 (0) 712204587; fax: þ39 (0) 712204582.||||||standing|or roof integrated)|there is a temperature|rise|of₂the|
|E-mail address: m.dorazio@univpm.it (M. D’Orazio). [http://dx.doi.org/10.1016/j.renene.2014.02.009](http://dx.doi.org/10.1016/j.renene.2014.02.009) 0960-1481/|2014 Elsevier Ltd. All rights reserved.|||||modules with respect to the ambient of 20e40|||C at 1000 W/m .So||

M. D’Orazio et al. / Renewable Energy 68 (2014) 378e396

|Nomenclature|||EP|average daily energy production related to P [kWh/|
|---|---|---|---|---|
|||||kWp]|
|Tc|cell/module temperature [ C]||(a-b)|variation in energy production of module type A in|
|Tb|back-side cell temperature [ C]|||respect to type B [%]|
|Ta|ambient temperature [ C]||(c-b)|variation in energy production of module type C in|
|Tr|reference temperature [ C]|||respect to type B [%]|
|Tairback|temperature of the air gap behind the module [ C]||P|peak power [kW]|
|Tfront|cell external surface temperature [ C]||A|BIPV module surface [m²]|
|K|Ross coefficient [K m²/W]||K|shading coefficient [e]|
|Gt|total incoming solar irradiance [W/m²]||bos|balance of system efficiency [e]|
|It|solar irradiance incident on module’s surface [W/m²]||a|empirically-determined coefficient establishing the|
|Gref|reference solar irradiance [1000 W/m²]|||upper limit for module temperature at low wind|
|Vw|wind speed [m/s] cell/module electrical efficiency [e]|||speeds and high solar irradiance (Sandia National Laboratory Model)|
|r E|cell/module electrical efficiency at temperature T efficiency correction coefficient for temperature [ C efficiency correction coefficient for solar irradiance [e] average daily energy production [kWh]|r[e] 1]|b|empirically-determined coefficient establishing the rate at which module temperature drops as wind speed increases (Sandia National Laboratory Model)|

DEP

DEP

h

h h b g

the losses in PV energy production caused by the rise of module temperature (“temperature effect”) will be positive when the effective module temperature exceeds 25 C, otherwise the losses are negative. To overcome this issue, some authors recommend high air gaps behind PV modules in order to minimize over-heating and energy loss of the modules, even if there is no clear agreement on optimum gap size for good PV performance, and values could vary over a wide range. Many studies have investigated the nature of the flow and temperature distribution in air gaps behind PV panels [4e7]. Gan [8,9], with the computational fluid dynamics method, determined the effects of air gap size on the thermal performance of PV modules for a range of roof pitches and panel lengths at different solar heat gain levels. He found that a minimum air gap of

0.12e0.15 m is required for multiple module installation and of
0.14e0.16 m for single module installation, depending on roof pitches. Guiavarch and Peuportier [10] implemented a model for build- ing integrated photovoltaic (BIPV) in a dynamic simulation tool and evaluated the influence of the type of integration of PV collector in buildings on their efficiency. They found out that an air gap of 0.1 m improved the efficiency of PV compared with the integration without an air gap. However, they defined this difference of effi- ciency “not dramatic” and underlined that results are to be com- plemented with architectural and economical aspects. An interesting study of Fanney et al. [11] was carried out on a building integrated photovoltaic test bed to provide some perfor- mance data needed for model validation. The facility incorporates four identical pairs of building integrated photovoltaic panels constructed using single-crystalline, polycrystalline, silicon film, and amorphous silicon photovoltaic cells. One panel of each iden- tical pair was installed with thermal insulation attached to its rear surface. The second paired panel was installed without thermal insulation, in order to quantify the effect of elevated cell temper- ature on the panels’ performance for different cell technologies. Results showed that the addition of insulation to the rear of crys- talline, polycrystalline, and silicon film panels resulted in declines in energy production of 3.3, 2.5, and 3.4%, respectively. Unlike the other BIPV panels, the insulated amorphous silicon panel out- performed the non-insulated panel by 1.5%. By the analysis of real PV modules and the use of an economic assessment method, Reinders et al. [12] demonstrated that a well- ventilated PV array results in an improved performance, but
increases electricity generating costs, based on investment costs, operation costs, economic lifetime, interest rate and depreciation. Recently, many countries, for esthetic purposes, have started offering economic advantages (tax deductions, incentives, etc.) for the installation of building integrated photovoltaic modules (BIPV). For domestic applications, these kinds of modules often substitute part of the roof covering and are installed totally coplanar to it. The market for these systems is now spreading because they combine electrical production ability with water- tightness, mechanical resistance and poor maintenance. In southern European countries like Italy, where clay tile roofs are quite diffused, it is normal to have an air gap between 0.03 and

0.06 m directly below the tiles, but at the same time the air gap should not be more than 0.09 m in order to guarantee water- tightness of the roof covering. In these roof mounting configura- tions, the photovoltaic panels can be installed on the wooden frame of the tiles so as to create small air gaps which are able to cool the modules. Alternatively, the panels can be mounted directly in contact with the insulation. Nevertheless, poor or absent ventila- tion under the cells could cause an overheating of BIPV, and this especially happens in presence of the current high insulation levels in the building envelope. The consequence could be a reduction in their efficiency. In addition to concerns over first costs, a barrier to the wide- spread proliferation of BIPV is the lack of performance data. Another obstacle is lack of effective predictive performance tools which could accurately inform the designers and building owners about their performance and justify their application. Concerning PV rack-mounted installation, the nominal oper- ating cell temperature (NOCT), can be effectively used to predict the temperature of the module under various environmental conditions. However, the heat transfer phenomena of a rack-mounted PV module and a BIPV module are quite different. Unlike rack-mounted modules, the two sides of the BIPV modules are subjected to significantly different environmental conditions, depending also on the heat transfer in the air gap which can be created under the module. During the past 15 years many studies focused on the in situ BIPV performance, showing that for a more precise determination of the cell temperature, predictive models that include wind speed as a variable should be used [3]. The US Sandia National Laboratories (SNL) method relies on a properly designed and well controlled

|380|M. D’Orazio et al. / Renewable Energy 68 (2014) 378e396|
|---|---|
|Table 1||
|Principal values of the Ross coefficient k adapted by Skoplaki||
|et al. [16] from data in Ref. [21].||
|PV array type|k (K m /W)|
|Well cooled|0.02|
|Free standing|0.0208|
|Flat on roof|0.026|
|Not so well cooled|0.0342|
|Transparent PV|0.0455|
|Façade integrated|0.0538|
|On sloped roof|0.0563|

Table 2

The empirical coefficients a and b, used in the SNL model whose set of values are determined for various cell types and PV module installation.

|Module type|Mount|ab|DT ( C)|
|---|---|---|---|
|Glass/cell/glass|Open rack|3.47|0.0594 3|
|Glass/cell/glass|Close roof mount|2.98|0.0471 1|
|Glass/cell/polymer sheet|Open rack|3.56|0.0750 3|
|Glass/cell/polymer sheet|Insulated back|2.81|0.0455 0|
|Polymer/thin-film/steel|Open rack|3.58|0.113 3|

outdoor test bed for BIPV [11,13,14]. Thanks to the high quality experimental data provided, a new technique to compute the operating temperature of cells within building integrated photo- voltaic modules using a one-dimensional transient heat transfer model was developed, which also takes into account the wind speed. A simpler empirically-based thermal model was then developed at Sandia for system engineering and performance modeling purposes [14,15] The aim of this study is to assess the performance of BIPV mounted on a clay tile roof in three different configurations: rack- mounted over the roof covering, with a minimum air gap between the modules and building envelope and in contact with roof insulation. The research intended to determine whether in a temperate climate, like the one in Italy, it would be necessary to provide higher air gaps on the rear of the panel, as suggested by some researches, in order to minimize overheating and to improve PV performance, or whether the gaps normally provided in traditional configurations of tile roof may be sufficient to ensure good performance. Starting from the experimental data provided by our test roofs, we then evaluated the suitability of NOCT and SNL models for BIPV

temperature prediction and consequent errors of expected elec- trical power output generated during a long term performance (almost one year).

2. Cell temperature calculation models Several models have been developed to estimate the operating cell temperature related to PV mounting configuration, and many studies claim its importance in relation to the electrical efficiency of a photovoltaic device [1,14,15,17e19]. It is actually well established that the temperature of the module strongly affects its energy performance. Skoplaki and Palyvos [3,16] retrieve many correlations which express the adverse effect of an operating temperature increase on the electrical efficiency of the PV module. As the PV cells are encapsulated for moisture protection, prac- tically cell temperature is very difficult to measure. For major convenience, the temperature at the back of the cell (Tb)is commonly measured instead. The Tbcan be obtained from the temperature of the cells (Tc) by the simple expression in (1) [14]: <u>Gt</u> T c¼ Tbþ DT (1) Gref In which Grefis the reference solar irradiance (1000 W/m²), Gtis the total incoming solar irradiance (W/m²), DT is the temperature dif- ference between the cell and the back surface of the module at the reference solar irradiance level. This temperature difference is typically 2e3 C for flat-plate modules in an open-rack mount. For flat-plate modules, with a thermally-insulated back surface, this temperature difference can be assumed to be zero. The simplest explicit equation for the operating temperature of a PV module links Tcwith the ambient temperature and the solar irradiance flux in a linear expression (2): T c¼ Taþ kGt(2) where k is a dimensional parameter, known as Ross coefficient [20], ranging between 0.02 and 0.04 K m²/W. Its value depends on the level of integration of the module and the size of air gap behind the modules. Skoplaki and Palyvos [16] adapted the principal k values from data in Ref. [21]. Results are listed in Table 1. An established procedure to calculate the PV module operating temperature involves use of the nominal operating cell temperature
Fig. 1. View of the real-scale experimental building with photovoltaic modules, south pitch (Ancona, Italy).

Fig. 2. PV modules electrical and physical main characteristics.

Fig. 3. Position of the probes in the roofs and PV modules. Stratigraphies of the roofs: on the left the ventilated roofs (A, B) and on the right the non-ventilated roof (C).

(NOCT) [22] over a range of environmental conditions [23]. This The method used for determining cell temperature must then method is very widespread because manufacturers usually include cover a wide range of environmental conditions and mounting this parameter in the data sheets of PV modules, but it is defined in systems. Many studies have investigated the suitability of the NOCT specific mounting and Nominal Terrestrial Environment (NTE) model for BIPV under various conditions [13,24e27], with discor- conditions [22]. dant results on the effectiveness of the model. Nevertheless, an increasing interest in BIPV applications However, even in case of high uncertainties in the predicted brought forward the need for a proper estimation of NOCT which temperatures by the NOCT model, the effect on the predicted power would take into account the deviation from NTE and mounting output of the PV module over a long term is not very significant. In conditions. the study of Trinuruk et al. [27], the total percentage error of the When a PV module is integrated into the exterior envelope of expected power outputs would be less than 6% for the maximum a building, the two sides of the module will be subjected to error of 10 C in temperature prediction. significantly different environmental conditions. Insulating mate-Alonso García and Balenzategui [25] found that a 3 C inac- rials or roof ventilated air gap may further affect the operating curacy in NOCT estimation introduces only a 1.5% error in yearly temperature. performance assessment.

Table 3

Summary of the main weather conditions of the summer days taken into consideration for the first analysis: a sunny day without wind, a sunny and windy day and a cloudy day.

Mean external air Maximum external Mean wind speed (m/s) Maximum wind Mean solar Maximum solar <u>temperature ( C) air temperature ( C) speed (m/s) irradiance (W/m) irradiance (W/m)</u> Sunny not windy day (21/08/2009) 26.3 35.2 0.6 2.0 308.0 953.0 Sunny windy day (05/08/2009) 22.7 35.2 1.5 4.2 309.0 1034.4 Cloudy day (30/08/2009) 23.3 26.5 0.9 3.1 132.9 640.5

|100.0 90.0 80.0 70.0 60.0 C]||||||||Module A-Sunny Day|||||T front Tb|External Air Temperature Internal Air Temperature T air back T NOCT predicted T SNL predicted|||1000 800 600||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|50.0 Temperature [40.0 30.0 20.0 10.0 0.0|||||||||||||Flux|Global Irradiance|||400 200 0|Heat Flux [W/m2] Global irradiance [W/m2]|
|100.0 90.0 80.0 70.0 60.0 C] 50.0|12:00 12:50 1:40 AM AM|2:30 AM AM|3:20 4:10 AM AM|5:00 5:50 AM AM|6:40 7:30 AM AM|8:20 AM AM|AM AM|9:10 10:00 10:50 11:40 12:30 1:20 AM PM Time Module B-Sunny Day|2:10 PM PM|3:00 3:50 PM PM|4:40 5:30 PM PM|6:20 PM PM|7:10 8:00 PM T front Tb|8:50 PM PM External Air Temperature Internal Air Temperature T air back Tb NOCT predicted Tb SNL predicted Global Irradiance|9:40 10:30 11:20 PM|PM|1000 800 600||
|Temperature [40.0 30.0 20.0 10.0 0.0|12:00 12:50 1:40 AM AM|2:30 AM AM|3:20 4:10 AM AM|5:00 5:50 AM AM|6:40 7:30 AM AM|8:20 AM AM|AM AM|9:10 10:00 10:50 11:40 12:30 1:20 AM PM|2:10 PM PM|3:00 3:50 PM PM|4:40 5:30 PM PM|6:20 PM PM|Flux 7:10 8:00 PM|8:50 PM PM|9:40 10:30 11:20 PM|PM|400 200 0|Heat Flux [W/m2] Global Irradiance [W/m2]|
|||||||||Time|||||||||||

Fig. 4. (a,b,c) Sunny and non-windy day (21/08/2009): measured Tb, Tfront, Tairbackand heat flux on the PV modules (A, B, C), weather conditions (air temperature, global irradiance)

and building indoor temperature. Comparison with Tbtrend predicted by NOCT and SNL models.

**Module C-Sunny Day**

100.0
External Air Temperature

90.0Internal Air Temperature 1000
T front

80.0
T air back

Tb800

70.0
Tb NOCT predicted

60.0 Tb SNL predicted
**C]** Global Irradiance600

50.0
Flux

**Temperature [**

40.0**Heat Flux [W/m2]**
400 **Global Irradiance [W/m2]**

30.0
20.0
200

10.0
0.0 0 12:00 12:50 1:40 2:30 3:20 4:10 5:00 5:50 6:40 7:30 8:20 9:10 10:00 10:50 11:40 12:30 1:20 2:10 3:00 3:50 4:40 5:30 6:20 7:10 8:00 8:50 9:40 10:30 11:20 AM AM AM AM AM AM AM AM AM AM AM AM AM AM AM PM PM PM PM PM PM PM PM PM PM PM PM PM PM
**Time**

Fig. 4. (continued).

The US Sandia National Laboratory PV thermal model is based on roof systems were all made up of two crossed layers of pine wood the operating temperature [14] of the module, which can be panels with a total thickness of 5 cm and EPS insulation of 4 cm. The estimated on the basis of ambient temperature, solar irradiance, roofs were different from each other due to the presence of a wind speed and a set of empirically determined coefficients ventilation duct between the insulation and the traditional clay tile depending on the mounting configuration of the module. With covering (4 cm). The roofs, named A and B, were ventilated, while symbols (3): roof C was not ventilated. PV modules were installed on the south roof pitch, two panels T b¼ Taþ Itexp ðaþbVw Þ

(3) over each one of the three different roof systems. The modules were made up of mono-crystalline silicon cells (156 156 mm) and
where a and b are the empirical coefficients, whose set of values are differed from each other by their level of integration, according to summarized in Table 2 for various cell types and PV module Italian law DM 19.02. 2007 [28] in the following way: installation. The model has proven to be very adaptable for design purposes- Type A (on roof A): Fully integrated PV module installed at the by providing the expected module operating temperature with an same level of the roof covering with an air gap of 0.04 m (be- accuracy of about 5 C. Temperature uncertainties of this tween the panel and the insulation); magnitude have resulted in less than a 3% effect on the power- Type B (on roof B): Partly integrated PV module installed over output of the module. the roof with an air gap of 0.2 m (between the panel and the tile covering);

3. Materials and methods- Type C (on roof C): Fully integrated PV module mounted directly
in contact with roof insulation.

3.1. Experimental devices
The modules had a metal frame supporting the cells, which The research was carried out by analyzing the thermal perfor-further distanced them from the roof supports (wooden structure mance and energy efficiency of three PV modules installed on a for system A, insulation for system C), creating an additional air gap real-scale experimental building (Fig. 1) in the vicinity of the of 0.02 m behind the panels. Marche Polytechnic University of Ancona (Italy, 2064 DD). The NOCT value of the tested PV modules declared by the The roof of the building had a north pitch of 1.5 m and a main manufacturer’s specifications was 46 C. south pitch of 6 m and a 17 slope. The latter was divided into 3 roof Fig. 2 summarizes the electrical and physical main characteris- modules of the same width (1.60 m) and same length of 5.6 m. The tics of the PV modules.

|100.0 90.0 80.0 70.0 60.0 C]||||||||Module A-Windy Day||||T front Tb|External Air Temperature Internal Air Temperature T air back T NOCT predicted T SNL predicted||1000 800 600||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|50.0|||||||||||||Global Irradiance||||
|Temperature [40.0 30.0 20.0 10.0 0.0||||||||||||Flux|||400 200 0|Heat Flux [W/m2] Global Irradiance [W/m2]|
|AM|12:00 12:50 1:40 AM AM|2:30 3:20 AM AM|4:10 5:00 AM AM|5:50 6:40 AM AM|7:30 8:20 AM AM|AM AM|9:10 10:00 10:50 11:40 12:30 1:20 AM AM|PM PM|2:10 3:00 PM PM|3:50 4:40 PM PM|5:30 6:20 PM PM|7:10 8:00 PM PM|8:50 PM PM|9:40 10:30 11:20 PM PM|||
|100.0 90.0 80.0 70.0 60.0 C] 50.0 Temperature [40.0 30.0 20.0 10.0 0.0 AM|12:00 12:50 1:40 AM AM|2:30 3:20 AM AM|4:10 5:00 AM AM|5:50 6:40 AM AM|7:30 8:20 AM AM|AM AM|Time 9:10 10:00 10:50 11:40 12:30 1:20 AM AM Time|Module B -Windy Day PM PM|2:10 3:00 PM PM|3:50 4:40 PM PM|5:30 6:20 PM PM|T front Tb Flux 7:10 8:00 PM PM|External Air Temperature Internal Air Temperature T air back Tb NOCT predicted Tb SNL predicted Global Irradiance 8:50 PM PM|9:40 10:30 11:20 PM PM|1000 800 600 400 200 0|Heat Flux [W/m2] Global Irradiance [W/m2]|

Fig. 5. (a,b,c) Sunny and windy day (05/08/2009): measured Tb, Tfront, Tairbackand heat flux on the PV modules (A, B, C), weather conditions (air temperature, global irradiance) and

building indoor temperature. Comparison with Tbtrend predicted by NOCT and SNL models.

**Module C-Windy Day**

External Air Temperature

Internal Air Temperature1000

T front

T air back

Tb800

Tb NOCT predicted

Tb SNL predicted

600 Global Irradiance

Flux

**Heat Flux [W/m2]** 400 **Global Irradiance [W/m2]**

100.0
90.0
80.0
70.0
60.0
**C]**

50.0
**Temperature [**

40.0
30.0
20.0
10.0
0.0 AM AM AM AM AM AM AM AM AM AM AM AM AM AM AM
**Time**

Fig. 5.

3.2. Monitoring system External weather conditions were recorded throughout almost one year by means of a 12-bit datalogger to which instruments were connected in order to measure global irradiance, tempera- ture and relative humidity of the air outside, wind speed and direction. All radiometer probes were arranged on a plane parallel to the pitch plane in order to measure the irradiance directly incident on the PV modules. Internal air temperature and RH% were also measured by a thermal hygrometric probe. Thermal data on different roofs and modules (Fig. 3) were recorded in the same period by means of 3 12-bit dataloggers connected to:
- thermal resistances for measuring modules front and rear sur- face temperatures;
- thermal resistances for measuring temperatures within the different layers of the roof (surface of the insulation, air gap, surface of the wood slab);
- heat flow meters for measuring heat flux behind the modules. The accuracy of the probes was þ/ 0.15 C for PT100 thermal resistances, þ/ 5% for heat flow meters, 0.5% of mv for the ane- mometers, 5% for radiometric probes, þ/ 0.1 C for internal air temperature probe and þ/ 1.5% for internal RH probe; þ/ 0.2 C for external air temperature probe and þ/ 1.5% for external RH probe. All the probes and measurement connections were cali- brated beforehand, and the calibration results were noted in order
0 PM PM PM PM PM PM PM PM PM PM PM PM PM PM

(continued).

to correct the values that were measured. The acquisition rate was set to 10 s, while the post processing rate was set to 10 min.

3.3. Comparison of the temperature predictive model results In this research, we used NOCT and SNL models to predict the yearly temperature of the modules and their consequent perfor- mance (see Appendix for calculation details). The prediction results were then compared to recorded data in order to evaluate the suitability of the models in BIPV applications. NOCT values of the tested modules were taken according to the manufacturer’s specifications. Calculation of module temperature was carried out based on the recorded solar irradiance and ambient temperature, following the known equation (4): ðNOCT 20ÞGt T c¼ Taþ (4)
800

Concerning the SNL model, we used eq. (3), by considering the external climatic conditions (temperature, solar irradiance, wind speed) and the database of the empirical coefficient in Table 2, developed by SNL researchers for various cell types and module installation. Among the empirical coefficients, we adopted the following ones, based on the most similar installation condition:

a ¼2.98, b ¼0.0471; for modules A and C, with a close-roof mount; a ¼3.47, b ¼0.0594; for module B, with an open-rack mount.

In our analysis, we assumed that Tc¼ Tb, considering that the back plate of the module is thin and has low thermal resistance.

12:00 12:50 1:40 2:30 3:20 4:10 5:00 5:50 6:40 7:30 8:20 9:10 10:00 10:50 11:40 12:30 1:20 2:10 3:00 3:50 4:40 5:30 6:20 7:10 8:00 8:50 9:40 10:30 11:20

|100.0 90.0 80.0 70.0 60.0 C]||||||||Module A-Cloudy Day|||||T front T air back Tb|External Air Temperature Internal Air Temperature T NOCT predicted T SNL predicted||1000 800 600||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|50.0 Temperature [40.0 30.0 20.0 10.0 0.0|||||||||||||Flux|Global Irradiance||400 200 0|Heat Flux [W/m2] Global Irradiance [W/m2]|
|AM 100.0 90.0 80.0 70.0 60.0 C] 50.0 Temperature [40.0 30.0 20.0 10.0 0.0 AM|12:00 12:50 1:40 AM AM 12:00 12:50 1:40 AM AM|2:30 3:20 AM AM 2:30 3:20 AM AM|4:10 5:00 AM AM 4:10 5:00 AM AM|5:50 6:40 AM AM 5:50 6:40 AM AM|7:30 8:20 AM AM 7:30 8:20 AM AM|AM AM|AM AM AM AM|9:10 10:00 10:50 11:40 12:30 1:20 AM PM Time Module B-Cloudy Day 9:10 10:00 10:50 11:40 12:30 1:20 AM PM Time|2:10 PM PM 2:10 PM PM|3:00 3:50 PM PM 3:00 3:50 PM PM|4:40 5:30 PM PM 4:40 5:30 PM PM|6:20 PM 6:20 PM|7:10 8:00 PM PM T front T air back Tb Flux 7:10 8:00 PM PM|8:50 PM PM External Air Temperature Internal Air Temperature Tb NOCT predicted Tb SNL predicted Global Irradiance 8:50 PM PM|9:40 10:30 11:20 PM PM 9:40 10:30 11:20 PM PM|1000 800 600 400 200 0|Heat Flux [W/m2] Global Irradiance [W/m2]|

|Fig. 6. (a,b,c) Cloudy day (30/08/2009): measured T|, T|, T and heat flux on the PV modules (A, B, C), weather conditions (air temperature, global irradiance) and building|
|---|---|---|
|indoor temperature. Comparison with T|trend predicted by NOCT and SNL models.||

b front airback b

**Module C-Cloudy Day**

100.0
External Air Temperature

90.0 Internal Air Temperature1000
T front

80.0
T air back

70.0
Tb800

Tb NOCT predicted

60.0Tb SNL predicted
**C]** Global Irradiance 600

50.0
Flux

**Temperature [**40.0**Heat Flux [W/m2]** 400 **Global Irradiance [W/m2]**

30.0
20.0
200

10.0
0.0 0 12:00 12:50 1:40 2:30 3:20 4:10 5:00 5:50 6:40 7:30 8:20 9:10 10:00 10:50 11:40 12:30 1:20 2:10 3:00 3:50 4:40 5:30 6:20 7:10 8:00 8:50 9:40 10:30 11:20 AM AM AM AM AM AM AM AM AM AM AM AM AM AM AM PM PM PM PM PM PM PM PM PM PM PM PM PM PM
**Time**

Fig. 6. (continued).

4. Results and discussion It can be observed how the partially integrated photovoltaic
module B, because of the presence of a high air gap, constantly

4.1. Experimental and predicted thermal performance of the PV
maintains cell temperature lower than that of the fully integrated modules solutions A and C. On a sunny and non-windy day, Tbof module B (Fig. 4b) reached The thermal performance of the PV modules under study was a peak temperature of 65.5 C compared to 77.3 C of module A firstly analyzed on three summer days with different weather (Fig. 4a) and 78.8 C of module C (Fig. 4c). conditions: a sunny day without wind, a cloudy day and a sunny BIPV modules operated at temperatures higher than those of day with wind (Table 3). Summer conditions in Italy represent the module B, with temperatures ranging from 10 to 15 C above, in worst operating conditions for BIPV modules because of the high agreement with previous researches [15]. external temperatures reached. Similarly, the Tfrontof module B had a peak temperature of about The graphs in Figs. 4e6 show the Tbtemperature trend that was 15 C lower than that of modules A and C. In module C, where the measured (also compared to the one predicted by the NOCT and structure of the panel remains in contact with roof insulation and SNL methods), the temperature trend on the panel and behind it, the cells are only 0.02 m far from it, the air temperature of this and the heat flux trend behind the panel. In addition, they show the unventilated air gap reaches 75.3 C. In module A, where the air gap weather conditions (air temperature, global irradiance) and inter-is wider and more ventilated, the temperature reaches a peak of nal temperature recorded. 60.4 C. The Tairbackin module B reaches 46.2 C. The overheating of module C is justified by the limited heat flux behind the panel (maximum 62.5 W/m²), which is half of the value

Table 4 compared to the values reached in module A (maximum 114.6 W/

Summary of the Tcvalues measured and predicted by the NOCT and SNL modelsm²) and notably lower compared to those in module B (maximum averaged in the whole month of August for the three PV modules. Root mean square

324.5 W/m²).
error (RMSE) and mean absolute error (MAE) are used to assess the suitability of the models.On a sunny day with wind (Fig. 5), the wind reached a maximum speed of 4.15 m/s (the city of Ancona, where this experimental building <u>Module A Module B Module C</u>

|is located, is not very windy). A general reduction in T||was observed in||
|---|---|---|---|
|all the systems that were analyzed. In particular, the performance of||||
|module A (Fig. 5a) improved bringing T|(peaking at 54.3||C) closer to|
|the maximum values of module B (47.5 C, which is only limitedly affected by convection cooling because of|C) (Fig. 5b). The T||in module|
|the wind, reached a maximum temperature of 64.6||C(Fig. 5c).||

b <u>Real NOCT SNL Real NOCT SNL Real NOCT SNL</u> No. of observation ¼ 4464 b Averaged value of Tc( C) 33.9 33.8 38.2 31.5 33.8 33.4 34.9 33.8 38.2 b MAE ( C) 4.5 4.5 2.8 2.6 5.3 3.7 RMSE ( C) 5.4 5.4 3.4 3.0 6.3 4.3

|100||Module A||
|---|---|---|---|
|95|Module A|||
|90|Module A predicted NOCT||ICT conditions|
|85|Module A predicted SNL|||
|80 75 70 65|Linear (Module A)|||
|60 C) (55 a -T b 50 T 45 40 35 30 25 20 15 10 5 0 0|200 400|600 800 1000 Solar Irradiance (W/m²)|y = 0.040x R² = 0.931 NOCT conditions 1200|

Fig. 7. PV module and external temperature difference (TbTa) plotted against the solar irradiance for the Module A, throughout the month of August. Tbis experimentally

recorded and calculated by NOCT and SNL models. Standardized reference lines are given, which show both NOCT and ICT conditions.

In the photovoltaic modules that were ventilated at the back (A and B), there was a substantial reduction in air temperature in the air gap (less than 40 C in module A and less than 30 C in module

B), while in module C the air maintained a temperature close to the temperature at the back of the panel (60.9 C). In fact, convective heat exchange causes an increase in heat flux at the back of module A even if the air that passes through the air gap between cells and the roof covering is little because of the frictional resistance at the air gap entrance. On a day with poor solar irradiance (Fig. 6), the difference in the performance between the three systems levels out substantially. Low solar irradiance causes a general lowering of temperature of the panel and of the roof covering. When we compare the Tbmeasured on the days with the Tb predicted by the NOCT and SNL models (shown in the graphs), it can be observed that as regards module B, both models come close to its real performance on a sunny day (Fig. 4b) as well as on a cloudy day (Fig. 6b), both of which were not so windy. The two methods however turn out to be less efficacious on a windy day (Fig. 5b). In this case, both of them overestimate cell temperature. In particular, the difference in temperature reaches C with the NOCT model, while it reaches 8 C with the SNL model. In fact, the NOCT model ignores the effects of wind speed
when it evaluates the operating temperature of the photovoltaic cells. As regards the BIPV modules A and C, the SNL method comes closer to real Tbtemperature trend compared to the NOCT model, during the sunny (Fig. 4a,c) and cloudy (Fig. 6a,c) days, which were not so windy. In general, the NOCT method underestimates Tbtemperatures; on a sunny day by up to 13 C. On a windy day (Fig. 5a,c), both methods are less effective in terms of BIPV performance. The Tcvalues measured and predicted by the models averaged in the whole month of August are summarized in Table 4. Root mean square error (RMSE) and mean absolute error (MAE) are used to assess the suitability of the models. The discrepancies of both model predictions for the temperatures of modules A and C are generally caused by the dissimilarity between BIPV installation and the standard installation as defined by the models. The graphs in Figs. 7e9 show the recorded module and external temperature difference (TbTa) plotted against the solar irradiance for the three types of modules, throughout the month of August. Standardized reference lines are given, which show both NOCT and ICT conditions. ICT refers to an Insulated Test Condition (when a module is insulated by 10 cm of expanded polystyrene so that it

|100||Module B||
|---|---|---|---|
|95|Module B|||
|90|Module B predicted NOCT||ICT conditions|
|85|Module B predicted SNL|||
|80 75 70 65|Linear (Module B)|||
|60 C) (a 55 -T b 50 T 45 40 35 30 25 20 15 10 5 0 0|200 400|600 800 1000 Solar Irradiance (W/m²)|y = 0.029x R² = 0.934 NOCT conditions 1200|

Fig. 8. PV module and external temperature difference (TbTa) plotted against the solar irradiance for the Module B, throughout the month of August. Tbis experimentally

recorded and calculated by NOCT and SNL models. Standardized reference lines are given, which show both NOCT and ICT conditions.

does not have convective and radiative flow behind the module [24]). The performance of PV modules does not follow a straight line, but something more like a cloud of measurement points due to convective and radiative energy flows, depending on boundary conditions. In general, the large amount of scatter is due to the thermal storage capacity of the panels, the environmental condi- tions recorded on cloudy days (high external temperatures with low irradiance), and the variations in wind speed. It can be observed that the temperature difference recorded reaches more than 15 C at the same irradiance, particularly for BIPV module A, which is ventilated at the back. The R² index in the graphs shows a good linearity of the recorded data. All the modules analyzed show a Ross Coefficient [20], ranging between 0.029 and 0.043 K m²/W, in agreement with the classifi- cation by Skoplaki and Palyvos [16]. Module B, which has the lowest T b, has a Ross coefficient of 0.029 K m²/W (near the “free standing” mount). The different radiative and convective heat exchanges on the rear side of the BIPV applications A and C cause the NOCT line to move upwards: the coefficients of modules A and C are higher and nearer the “not so well cooled” conditions of Ref. [16]. In the same graphs, temperatures predicted by experimental data in the same period with NOCT and SNL methods are shown.

Module B, which can be considered as rack-mounted over the roof, better fits the NOCT conditions, compared to modules A and C. For Module B, both NOCT and SNL models give good results in tem- perature assessment (Fig. 8): mean measured temperature differ- ence deviates from NOCT prediction by about 5 C and from SNL prediction by less than 5 C. In the case of the BIPV modules A and C, the NOCT model overpredicts the performance of the modules (lower slope of the trend line) (Figs. 7 and 9), up to 10 C; the SNL model could underpredict the performance by less than 10 C.

4.2. Experimental and predicted yearly energy performance of the PV modules
Table 5 summarizes the weather conditions (air temperature,
 solar irradiance, wind speed), the Tbmeasured and the Tcpredicted by NOCT and SNL models, averaged monthly for the three devices (A,B,C) during the whole monitoring period (from August 2009 to June 2010). Monthly averaged Tbactually measured and those predicted with the SNL and NOCT models were then used to calculate the efficiency of the panels (see Appendix for calculation details).

|100||Module C||
|---|---|---|---|
|95|Module C|||
|90|Module C predicted NOCT||ICT conditions|
|85|Module C predicted SNL|||
|80 75 70 65|Linear (Module C)|||
|60 C) (a 55 T-b 50 T 45 40 35 30 25 20 15 10 5 0 0|200 400|600 800 1000 Solar Irradiance (W/m²)|y = 0.043x R² = 0.948 NOCT conditions 1200|

Fig. 9. PV module and external temperature difference (TbTa) plotted against the solar irradiance for the Module C, throughout the month of August. Tbis experimentally

recorded and calculated by NOCT and SNL models. Standardized reference lines are given, which show both NOCT and ICT conditions.

The graphs in Figs. 10e12 show the scatterplot of the efficiency of the analyzed systems, which were calculated starting from the predicted Tbagainst the efficiency calculated starting by the measured Tb,during almost one year (from August 2009 to June

2010). For module B, both SNL and NOCT methods are effective in the real efficiency prediction (Fig. 11). As regards the BIPV modules (Figs. 10 and 12), the SNL method tends to underestimate the efficiency of the panels. On the contrary, the NOCT method tends to overestimate the efficiency especially for values lower than 0.12. Both graphs show a dispersion of dots by efficiencies measured between 0.11 and 0.13. This phenomenon is due to a transient thermal phenomenon caused by sudden variations of solar irradi- ance and by the heat capacity of the modules, as also underlined in Ref. [14]. The Tbcalculated with SNL and NOCT models was then used to predict average energy production almost throughout the year (from August 2009 to June 2010). The values were compared with those calculated starting from monitoring data. In Fig. 13, the average daily energy production given out monthly by the module has been reported. The energy calculated EP was related for each system to the peak power. The graph also
show the percentage variation in energy production of module types A and C in respect to type B (DEP(a-b), DEP(c-b)). Experimental results demonstrate that even though the rack- mounted PV module B constantly has a higher energy production, the difference with modules A and C is less than 4%. Module A, with a ventilated air gap, shows a better performance compared to the not ventilated module C: DEP(a-b)is less than 3%.

Fig. 14 reports the percentage differences of the average daily

energy production calculated starting from the Tbpredicted (NOCT and SNL models) and the one calculated starting from the experi- mentally measured Tb. From the graph, it can be deduced that some variations between predicted and calculated temperature above 10 C somehow cause percentage variations on the calculated energy which is generally lower than 5% in accordance with what has already been observed in Refs. [25,27]. Moreover, Fig. 14 also shows that for the photovoltaic panel type B, the SNL method is more efficacious than the NOCT method: the maximum monthly differences are lower than 2.0% against 2.5%. Both methods underestimate the energy output for this partially integrated module. For the BIPV systems A and C, there are greater differences be- tween experimental and calculated values: differences up to 4.7%

Table 5

Summary of the weather conditions (air temperature, solar irradiance, wind speed), of the Tbmeasured and the Tcpredicted by NOCT and SNL models, averaged monthly for the three devices (A,B,C) during the whole monitoring period (from August 2009 to June 2010). NOCT predicted temperature is the same for the three modules and SNL predicted temperature is the same for modules A and C, with similar close-roof mount.

|Month|Average|Average daily sum|Average wind|Average|Average|Average|Average predicted|Average predicted|Average predicted|
|---|---|---|---|---|---|---|---|---|---|
||external air temperature ( C)|of global irradiance per square meter|speed (m/s)|measured T b (A) ( C)|measured T b (B) ( C)|measured T b (C) ( C)|T b (A,B,C) NOCT model ( C)|T b (A,C) SNL model ( C)|T b (B) SNL model ( C)|
|||2 (kWh/m )||||||||
|August|24.5|6.5|0.9|33.9|31.5|34.9|33.8|38.2|33.4|
|September|20.8|5.2|0.9|27.4|25.5|28.3|28.1|31.5|27.8|
|October|13.9|3.7|0.8|17.3|16.6|18.0|18.9|21.3|18.7|
|November|10.5|2.2|0.6|11.6|11.7|12.5|13.2|14.6|13.2|
|December|6.9|1.6|1.3|6.8|7.2|7.4|8.9|9.9|8.8|
|January|5.0|2.0|0.9|5.6|5.9|6.4|7.4|8.5|7.3|
|February|3.1|2.8|1.1|3.3|3.6|3.9|4.9|5.7|4.8|
|March|10.8|4.1|1.1|15.1|14.4|16.0|16.9|19.9|16.7|
|April|10.9|5.4|1.0|17.9|16.9|18.9|17.3|20.3|17.0|
|May|17.8|5.8|1.0|25.6|23.7|27.1|28.0|32.8|27.5|
|June|22.4|6.7|1.1|30.7|28.2|31.8|32.3|36.8|31.8|

for the SNL method and up to 1.9% for the NOCT method, in module 4.3. Optimizing SNL model for BIPV in the Mediterranean climate A; differences up to 3.6% for the SNL method and up to 2.9% for the NOCT method, in module C. In general, in this case, the NOCT The errors caused by these prediction results are acceptable for method tends to overestimate the energy production of the most engineering applications in PV systems and design purposes. photovoltaic modules which are fully integrated compared to the Nevertheless, in order to optimize the SNL method for the BIPV, SNL method. mounted on the experimental roof covering, empirically new co- The SNL model turned out to be less efficacious in evaluating efficients a and b were determined. energy performance, probably because of the empirical coefficients Fig. 15 shows linear regressions that better fit the relation be- chosen and used in equation (3) for calculating Tc. tween the experimental data recorded throughout the monitoring

#### Module A

0.150
0.140
0.130
0.120 **PV efficiency from predicted temperature**
0.110

|||SNL model|NOCT model|
|---|---|---|---|
|0.100||||
|0.100|0.120 PV efficiency from measured temperature|0.140|0.150|
|Fig. 10. Scatterplot of the efficiency of the Module A calculated starting from the predicted T year (from August 2009 to June 2010).|||during almost one|

0.110 0.130
b plotted against the efficiency calculated starting by the measured Tb,

experimentally measured Fig. 14.

Fig. 13.

Percentage differences of the average daily energy production calculated starting from the **Average Daily energy production EP (kWh/kWp)** -6.000-4.000-2.000 0.000 2.000 4.000 6.000 8.000 -6.0% 4.0% Average daily energy production values given out monthly by the three PV modules analyzed almost throughout the year (from August 2009 to June 2010).

|-5.0% -4.0%|-3.0%|-2.0%|Difference (%) -1.0%|0.0%|1.0%|2.0% 3.0% 1.9%|
|---|---|---|---|---|---|---|
|||-1.0%|||||
|, throughout the year (from August 2009 to June 2010).|-2.5% -2.4%|-1.5% -1.4% -1.0% -1.3% -1.1%|-0.5%||1.0%|1.4% 2.4%|
||-2.2% -1.9% -2.5% -2.5% predicted (NOCT and SNL models) and the one calculated starting from the -2.3% -3.0% -2.0%|-1.2% -1.2% -1.0% -1.2% -0.9% -0.9% -1.0% -1.4% -1.1% -1.5%|-0.9% -0.6% -0.5% -0.4% -0.5% -0.2% -0.8% -0.4% -0.8% -0.9%|0.4% 0.3% 0.3%|0.8% 1.4% 1.0% 1.2% 1.2%|2.0% 1.9%|
|-3.5% -3.6%|-2.5% -2.4% -2.0% -2.4%|-1.2%|-0.1%|0.3%|0.9% 0.9%||
|-4.0% -3.3%|-1.9%||||||

August -2.8% 5.03 August 5.18

2.9%-3.8% 4.98
T b September September-2.8% 4.11

4.23
-3.8% 4.07

October -2.1% 3.05 October 3.12 -3.1% 3.02 **Average daily energy production EP (kWh/kWp)** November -1.1% 1.91 M. D November 1.93 -2.6% 1.88 ’Orazio et al. / Renewable Energy 68 (2014) 378 **Predicted Energy Difference (%)**

Dicember -0.7% 1.42 December 1.43 -2.0% 1.41 **Period (month)**

January -0.8% 1.81

1.82
**Month**January-2.3% 1.78

Fabruary T-0.6% 2.53 b

2.55
February-2.0% 2.50

March-1.7% 3.47 e

3.52
-2.5% 3.44 March Δ Module A EP(a-b) April-1.8% 4.52

4.60
SNL prediction-module C SNL prediction-module B SNL prediction-module A NOCT prediction-module C NOCT prediction-module B NOCT prediction-module A-2.7% 4.48 April Δ Module B EP(c-b) May-2.3% 4.66

4.76
-3.3% 4.61 May -4.7% Module C June-2.6% 5.31

5.45
-3.3% 5.27 June -6.0%-4.0%-2.0% 0.0% 2.0% 4.0% 6.0% 8.0%

**EP (%)**

|-2.00|Wind Speed (m/s)|
|---|---|
|0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 -2.50 -3.00 -3.50 ln[(Tc-Ta)/E] -4.00|y = -0.0098x - 3.13 y = -0.0134x - 3.24 y = -0.0399x - 3.51|
|-4.50 -5.00|Module A Module B Module C Linear (module A) Linear (Module B) Linear (Module C)|

Fig. 15. Experimentally determined relationship for back surface temperature of the three modules analyzed as a function of solar irradiance, ambient temperature and wind speed.

period: panel temperature, external air temperature, and wind speed. It is evident from the graph that thermal transients caused by clouds and the heat capacitance of the modules introduce random influences on the temperature of the modules, but these effects average out on an annual basis [9]. The empirical coefficients obtained with optimization (intercept and slope of the linear fit) are:

a ¼3.24, b ¼0.0134, for the module A, with a ventilated gap; a ¼3.51, b ¼0.0399, for the module B, open rack mounted; a ¼3.13, b ¼0.0098, for the module C, in contact with the insulation.

With the use of these new coefficients, suitable for these roof mounting configuration under these site weather conditions, the maximum variations of energy output calculated with the SNL method compared to the energy determined with actual recorded temperatures were verified under 2.5% for all the modules (Fig. 16).

5. Conclusions The main conclusions from the investigation of the thermal performance of 3 BIPV modules installed in a real scale experimental building over a traditional clay tile pitched roof in Italy is that the difference between the energy produced, calculated based on the recorded Tb, is lower than 4% regardless of installation conditions. The main conclusions from the evaluation of the suitability of the two temperature prediction models (NOCT model and SNL model) for BIPV temperature and energy efficiency are the following:
- On summer days with no wind, both methods for rack-mounted module B come quite close to its real performance. As regards the BIPV modules A and C, the SNL method proves to give better results.
- Both methods are less efficacious in the prediction of the tem- peratures of the panels on a windy summer day: for module B, both methods overestimate cell temperature, up to 12 C with the NOCT method and up to 8 C with the SNL method.
- Differences between the predicted and calculated temperature around 10 C cause percentage variations on the energy pre- dicted compared to the energy from measured temperature which are generally lower than 5% in accordance with preceding results [11,25,27].
- For the partially integrated photovoltaic panel B, the SNL method is more efficacious than the NOCT method: differences between the monthly predicted and experimental values are up to 2.0% against 2.5%. Both the methods underestimate en- ergy output.
- For the BIPV systems A and C, an opposite phenomenon was observed. There were differences of up to 4.7% for the SNL method and up to 1.9% for NOCT method in module A; differences up to 3.6% for the SNL method and up to 2.9% for the NOCT method in module C. In general, in this case, the NOCT model tends to overestimate the energy production of the fully integrated photovoltaic modules compared to those of the SNL method.
- An optimization of the empirical coefficients used for calcu- lating based on the SNL method allows for the reduction of these differences between the predicted and experimental values under 2.5% for the analyzed modules under these installation condition.

NOCT prediction-module A **Predicted Energy Difference (%)** NOCT prediction-module B

NOCT prediction-module C

SNL prediction-module A

SNL prediction-module B

SNL prediction-module C

1.4%
1.2% 1.2%
1.0%
0.9% 0.9%
0.3% 0.3% 0.3%
-0.2%-0.1% -0.3%-0.4% -0.5% -0.5%-0.4% -0.7%-0.7% -0.9%-1.0% -1.1%-1.2%-1.1%-1.2% -1.3% -1.4% -1.4%-1.3% -1.5% -1.5% -1.6%

-2.1% 2.3% -

2.4%-
-2.4%-2.5%

January February March April May June **Month**

Fig. 16. Percentage differences of the average daily energy production calculated starting from the Tbpredicted (NOCT and SNL models) and the one calculated starting from the

experimentally measured Tb, throughout the year (from August 2009 to June 2010). Coefficients a and b of the SNL model are empirically determined and optimized for the BIPV analyzed.

4.0%
3.0% 2.9%
2.4%
2.0% 1.9%
2.0% 1.9%
1.4%
1.0%
1.0% 0.8%
0.4%
0.3%
0.1%
0.0% -0.1%
-0.2% -1.0%-0.4%-0.5%-0.4%-0.4%-0.4%-0.4% -0.6%-0.5% -0.2% -0.6% -0.8% -0.6% -1.0% -1.1% **Difference (%)**-1.2% -2.0%-1.4%-1.4%

-3.0%

-4.0%

-5.0%

-6.0% August September October November December

standard conditions provided by the manufacturers with the tem- perature of the cells [30]:

#### h ¼ hr½1 bðTcTrÞþg Log Gt(A.1)

Most often, the equation is used with g ¼ 0 [31] and then goes down to (A.2), which represents the traditional linear expression for the PV electrical efficiency:

#### h ¼ hr½1 bðTcTrÞ (A.2)

Using (A.2) for each PV module analyzed (A,B,C), we could find the effective efficiency (A.3) and consequently estimate the energy production, as in (A.4):

h i h ¼ h 1 b T Tr(A.3) ðA;B;CÞ r cðA;B;CÞ

E ðA;B;CÞ¼ hðA;B;CÞ$hbos$AðA;B;CÞ$GðA;B;CÞ$k (A.4)

In our case, the module surface areas were 2.43 m² for BIPV A and C;

2.92 m² for BIPV B. K was equal to 1 because the building was set in an open area and the roof pitch was facing exactly south. G(A,B,C) was directly measured. hboswas considered equal to 0.89. The three PV system modules were formed by a different number of PV cells (for type B, 60 cells while for the types A and C, 50 cells). Therefore, the modules are characterized by different peak powers. In order to
In conclusion, for the analyzed installation condition, typical of a traditional clay tile Italian roof at that latitude, experimental results show that a 0.04 m air gap is enough for reducing the overheating of a BIPV. The related energy annual production reaches less than 3% difference with the rack-mounted system. According to Norton et al. [29], considerable enhancement of BIPV system performance would be achievable without improvement in PV cell performance. Given that the latter will continue to improve, the prospects for a greater range of viable BIPV applications will include: incorporating PV materials into products such as roofing materials, windows and awnings. This provides the opportunity for cost reduction by replacing common building materials with PV materials at marginal costs. The use of predictive models as NOCT and SNL for BIPV modules are acceptable for most engineering applications in PV systems and design purposes. The errors caused by the energy prediction results are generally lower than 5%. The optimization of the empirical coefficients of SNL model proposed by this study reduces the error under 2.5% for these type of PV modules and under these site weather conditions.

Appendix. The PV module efficiency calculation

There are many models for the assessment of photovoltaic module efficiency. The most known is given by the following equation (A.1), which adjusts the reference module efficiency in

compare module performance, it was therefore necessary to relate the energy calculated for each system to its peak power (A.5):

#### EPða;b;cÞ¼ Eða;b;cÞ=Pða;b;cÞ(A.5)

In our case, Pa¼ Pc¼ 0.185 kWp and Pb¼ 0.21 kWp. Finally we calculated the variation in energy production of module types A and C in respect to type B by the following relations:

<u>EPðaÞEPðbÞ</u> DEPða bÞ¼ (A.6) EPðbÞ

<u>EPðcÞEPðbÞ</u> DEPðc bÞ¼ (A.7) EPðbÞ

References

[1] Baltus C, Eikelboom J, van Zolingen R. Analytical monitoring of losses in PV systems. In: 14th European photovoltaic solar energy conference, Barcelona, Spain; 1997. pp. 1547e50. [2] Anis W, Nour A. Energy losses in photovoltaic systems. Energy Convers Manag 1995;36:1107e13. [3] Skoplaki E, Palyvos JA. On the temperature dependence of photovoltaic module electrical performance: a review of efficiency/power correlations. Sol Energy 2009;83:614e24. [4] Moshfegh B, Sandberg M, Bloem JJ, Ossenbrink JH. Analysis of fluid flow and heat transfer within the photovoltaic facade on the Elsa building, JRC Ispra. In: Proceedings of the 13th European PV solar energy conference, Nice, France;

1995. pp. 2215e7.
[5] Sandberg M, Moshfegh B. Investigation of fluid flow and heat transfer in a vertical channel heated from one side by PV elementsdpart II, experimental study. In: Proceedings of the world renewable energy conference; 1996. pp. 254e8. [6] Yang H, Marshall RH, Brinkworth BJ. Validated simulation for thermal regu- lation of photovoltaic wall structures. In: Proceedings of the 25th IEEE PV specialists conference, Washington, DC; 1996. [7] Moshfegh B, Sandberg M. Flow and heat transfer in the air gap behind photovoltaic panels. Renew Sustain Energy Rev 1998;2:287e301. [8] Gan G. Numerical determination of adequate air gaps for building-integrated photovoltaics. Sol Energy; 2009:1e21. [9] Gan G. Effect of air gap on the performance of building-integrated photovol- taics. Energy 2009;34:913e21. [10] Guiavarch A, Peuportier B. Photovoltaic collectors efficiency according to their integration in buildings. Sol Energy 2006;80:65e77. [11] Fanney A, Dougherty B, Davis M. Measured performance of building inte- grated photovoltaic panels. J Sol Energy Eng 2001;123:187e92.

[12] Reinders AHME, Dijk VAP, Van Wiemken E, Turkenburg WC. A technical and economic simulation. Prog Photovolt: Res Appl 1999;82:71 analysis of monitored grid connectede82 PV. systems by means of

[13] Davis MW, Fanney A, Dougherty BP. Prediction of building integrated photovoltaic cell temperatures. J Sol Energy Eng 2001;123:200. [14] King D, Kratochvil J, Boyson W. Photovoltaic array performance model; 2004. [15] Fuentes Syst Res; 1987 MK. A. simplified thermal model for flat-plate photovoltaic arrays.

[16] Skoplaki E, Palyvos JA. Operating temperature of photovoltaic modules: a survey of pertinent correlations. Renew Energy 2009;34:23e9. [17] Kiefer K, Korkel T, Reinders A, Rossler E, Wiemken E. 2250 PV-roof in Germany e operating results from intensified monitoring and analysis through nu- merical modelling. In: 13th European photovoltaic solar energy conference, Nice, France; 1995. pp. 575e9. [18] Schaub P, Mermoud A, Guisan O. Evaluation of the different losses involved in two photovoltaic systems. In: 12th European photovoltaic solar energy con- ference, Amsterdam, Netherlands; 1994. pp. 859e62. [19] Jones Energy 2001;70:349e59. AD, Underwood CP. A thermal model for photovoltaic systems. Sol

[20] Ross RG. Interface design consideration for terrestrial solar cell modules. In: Proceedings of the 12th IEEE photovoltaic specialists conference, Baton Rouge, LA; 1976. pp. 801e6. [21] Nordmann T, Clavadetscher L. Understanding temperature effects on PV systems performance. In: Proceedings of the third world conference on photovoltaic energy conversion, Isaka, Japan; 2003. pp. 2243e6. [22] ASTM. E 1036M standard test methods for electrical performance of non- concentrator terrestrial photovoltaic modules and arrays using reference cells, vol. 12.02; 1999. [23] Koehl M, Heck M, Wiesmeier S, Wirth J. Modeling of the nominal operating cell temperature based on outdoor weathering. Sol Energy Mater Sol Cells 2011;95:1638e46. [24] Bloem JJ. Evaluation of a PV-integrated building application in a well- controlled outdoor test environment. Build Environ 2008;43:205e16. [25] Alonso García MC, Balenzategui JL. Estimation of photovoltaic module yearly temperature and performance based on nominal operation cell temperature calculations. Renew Energy 2004;29:1997e2010. [26] Mattei M, Notton G, Cristofari C, Muselli M, Poggi P. Calculation of the poly- crystalline PV module temperature using a simple method of energy balance. Renew Energy 2006;31:553e67. [27] Trinuruk P, Sorapipatana C, Chenvidhya D. Estimating operating cell tem- perature of BIPV modules in Thailand. Renew Energy 2009;34:2515e23. [28] DECRETO MINISTERIALE. Criteri e modalita’ per incentivare la produzione di energia elettrica mediante conversione fotovoltaica della fonte solare, in attuazione dell’articolo 7 del decreto legislativo 29 dicembre 2003, n. 387; 19 febbraio 2007 [in Italian]. [29] Norton B, Eames PC, Mallick TK, Huang MJ, McCormack SJ, Mondol JD, et al. Enhancing the performance of building integrated photovoltaics. Sol Energy 2011;85:1629e64. [30] Evans DL. Simplified method for predicting photovoltaic array output. Sol Energy 1981;27:555e60. [31] Evans DL. Cost studies on terrestrial photovoltaic power system with sunlight concentration. Sol Energy 1977;19:255e66.
