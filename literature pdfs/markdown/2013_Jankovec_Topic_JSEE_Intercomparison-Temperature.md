# Intercomparison of Temperature

Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/135/3/031012/6323733/sol_135_3_031012.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/135/3/031012/6323733/sol_135_3_031012.pdf) by University of Oxford user on 04 August 2026

# Sensors for Outdoor Monitoring of Photovoltaic Modules

Solar cells’ temperature is a very important parameter that affects performance of photo- voltaic (PV) modules since main electrical parameters of PV cells and modules are tem- perature dependent regardless the technology. The present study evaluates and compares different sensor types and mountings for long term outdoor temperature monitoring of PV modules along with a standardized method for determination of cell’s temperature

## Marko Jankovec

from open-circuit voltage. For that purpose, a special multicrystalline silicon PV module e-mail: marko.jankovec@fe.uni-lj.si with miniature in situ Pt1000 temperature sensors was used for reference temperature measurement. On the back side of the PV module different temperature sensors were

## Marko Topicˇattached, including thermocouple (TC), platinum Pt1000 (PT) and digital temperature

sensors DS18B20 (DS). All sensors except one were covered by a 1 cm thick insulation University of Ljubljana, block. The whole setup was mounted on the outdoor PV testing site and all temperatures Faculty of Electrical Engineering, were monitored for several days with selection of different environmental conditions. On Trzˇasˇka cesta 25, the basis of measurement results, deviations of different temperature sensors are investi- SI-1000 Ljubljana, Slovenia gated and compared to temperature calculated from open-circuit voltage measurement according to standard EN 60904-5. Among sensors attached at the back side, covered PT and TC sensors deliver the best results in range of 1–2 C of lower temperature in aver- age; while the covered DS sensor gives additional 1–2 C underestimated temperature values. The worst measurement results demonstrate the PT sensor without insulation. All temperature sensors exhibit similar and adequate time response regarding the thermal capacitance of the PV module. DS sensors, although showing somewhat worse results, offer great advantages if several temperatures have to be acquired simultaneously and require very simple data acquisition equipment. They feature comparable measurement accuracy than commonly used Pt1000 temperature sensors if they are covered by insula- tion with 10 mm thick walls in lateral direction to avoid micro-environmental changes. [DOI: 10.1115/1.4023518]

### Keywords: photovoltaics, measurement

1 Introduction Huang et al. [7]. However, a procedure of putting a PV module in

Output power of a PV module significantly depends on the a temperature controlled chamber, and waiting to be stabilized at

junction temperature of solar cells, which has to be measured each preselected before being measured under flash illumination

accurately for proper electrical characterization of PV modules for each type of PV module under investigation is rather incon-

and their inter comparison [1,2]. The acceptable level of accuracy venient and time consuming.

can be easily achieved in indoor measurement environments Since the solar cells’ junctions are not physically accessible for

equipped with adequate temperature conditioning facilities/com- nondestructive sensor attachment, temperature of PV module is

partments and flash light sources for illumination [3]. On the con- most commonly measured indirectly by measuring the average

trary, performance measurement of PV modules in open space temperature of the module’s back side surface. The procedure and

mountings under outdoor conditions (e.g., long term PV monitor- preferred measurement locations are defined in the standard IEC

ing) requires much more attention to be paid due to irradiance, 60891; however, it does not specify any detailed requirements for

wind, and different PV module structures and mountings that the sensor type and the way of attachment to the back side of the

influence the temperature conditions and microclimate in the vi- PV module [8]. This calls for a survey in particular for different

cinity of the applied adjacent external temperature sensors [4,5]. type of methods in order to obtain precise results since the correla-

Temperature of the PV module can be calculated from meas- tion between the temperature of the cell and the back sheet of the

ured open-circuit voltage (Voc) according to standard IEC 60904-5 PV module depends on several factors and is not a straightforward

which delivers inherent junction temperature of the laminated relationship that could be applied to any kind of PV module in

cells [6]. This method gives accurate results in any operating con- any mounting and environmental condition to correct the mea-

ditions as long as irradiance is kept above a certain level (the surement error [9–12]. Furthermore, the IEC 60891 standard

standard requires at least 200 W/m²) and if open-circuit voltage at requires at least four sensors to be attached to a single PV module,

standard test conditions (STC) and it’s temperature coefficient b which requires data acquisition equipment with many input chan-

of the cells in the particular PV module under test are known. nels, particularly where several PV modules are monitored

This method can be further improved by obtaining empirical tem- simultaneously.

perature and irradiation dependence of Vocas demonstrated by Krauter and Preiss carried out a detailed study of temperature measurement accuracy by using Pt100 temperature sensors in dif- ferent attachment configurations, among which one Pt100 was

|Contributed|by the SolarTEnergy|Division|of ASME for|publication|in the|
|---|---|---|---|---|---|
|J|P V|. Manuscript received July 16, 2012; final||||
|manuscript Editor: Santiago Silvestre.|received January|7, 2013; published|online April|29, 2013.|Assoc.|

OURNAL OF RESSURE ESSEL ECHNOLOGY laminated directly in the PV module behind the cell [13]. It is shown that even by using PT100 attached at the back surface and covered by ten layers of tape to prevent sensor cooling, they still

Journal of Solar Energy Engineering Copyright VC2013 by ASME AUGUST 2013, Vol. 135 / 031012-1

Fig. 2 Locations and attachment of sensors in the center of

the cell A

underestimated nominal operating cell temperature (NOCT) for

C. A development of a low-cost multichannel measuring system
was recently reported, where negative temperature coefficient sen- sors were used, which proved to be very accurate, if sensors are previously calibrated [14]. However, a current excitation source and an analog voltage input are needed for each sensor for simul- taneous temperature data acquisition. One possibility that is available lately is to use digital CMOS temperature sensors, based on a band-gap principle [15]. One of the most versatile sensors from this group is DS18B20 by Maxim, which provides temperature measurements with resolution of

0.0625 C and expanded measurement uncertainty of 60.5 C (coverage factor k ¼ 3) in the temperature range from 10 Cto þ85 C[16]. The DS18B20 communicates over a 1-Wire bus that requires only one data line and ground for communication. The DS18B20 can derive power directly from the data line, eliminat- ing the need for an additional power supply connection. Each sen- sor has unique serial code, which allows connection of multiple sensors to the same one-wire bus. Thus, it is straightforward to apply one microprocessor based data acquisition unit with general purpose digital inputs to control many DS18B20s distributed over several PV modules even at different PV arrays. Many researchers have already taken advantage of DS18B20 in their applications including PV monitoring applications [17–19]. In the presented study, we explore the accuracy of using DS18B20 for simultaneous temperature measurement of several PV modules for long term monitoring at outdoor conditions with comparison to other most common sensor types. As a reference, junction temperature is calculated from Vocmeasurement accord- ing to IEC 60904-5.
### 2 Experiment

A special 36 cell multicrystalline silicon PV module was lami- nated together with three PT1000 temperature sensors (PT) for a reference temperature measurement. Sensors were attached by thermally conductive paste to the back side of two cells in the middle of the PV module, named A and B, as shown in Fig. 1. Prior the PV module lamination the open-circuit voltage tem- perature coefficient (b) of cell A was measured under class AAA solar simulator Oriel 92194 A on a temperature stabilized platform for reference temperature measurement [20]. For each acquired point, we stabilized the temperature of the cell and measured open-circuit voltage during a short light pulse to prevent heating of the cell. The PV module was laminated in a standard way, starting with glass, electronic velocity analyzer (EVA) foil, 156 156 mm² multicrystalline Si solar cells, EVA foil and white Tedlar back

Fig. 3 A photo of sensors attached at the white back sheet at

the center of the cell A. Location of the laminated PT sensor is marked by a dot on the back sheet.

sheet. Cells were approximately 3 mm apart from each other. Each of PT sensors was connected by two thin copper wires iso- lated with lacquer that were lead out to an opening of junction box. After lamination, the PV module was framed into aluminum frame. On the back side of the PV module in close vicinity of the cen- ter of the cell A different temperature sensors were attached to the back sheet as shown in Figs. 2 and 3 and their main characteristics are summarized in Table 1. Our aim was to evaluate temperature sensors including their specified uncertainties; hence, no prior calibration or sensor matching was performed. All sensors except one PT sensor were covered by blocks of extruded polystyrene (XPS) insulation, which were approximately 30 mm high and 10 mm thick in order to minimize the sensor cooling due to air flow in their vicinity. An uncovered PT sensor was fixed to its position by thin wooden pin. Between each sensor and back sheet, we applied thermally con- ductive paste for better thermal contact. Cold junction of the TC sensor was measured by another DS sensor thus expanded uncer- tainty stated in Table 1 is calculated assuming both sensors are uncorrelated, as recommended in Ref. [21]. Both terminals of the cell A were accessible outside the module for Vocmeasurement. The PV module was mounted on our PV monitoring site on the roof top of the faculty building facing south with 30 deg of incli- nation [22]. In-plane irradiance, air temperature, and wind speed

|Table 1|Types and uncertainty data of temperature sensors||||
|---|---|---|---|---|
|used in the experiment|||||
|Sensor|Type|Class|Expanded uncertainty T ¼ (0, 85||
|PT|Pt1000|1/3 Bþ||60.25 C(k ¼ 2)|
|TC|K-thermocouple|2||63.2 C(k ¼ 2)|
|DS|DS18B20|—||60.5 C(k ¼ 3)|

Fig. 1 Locations of laminated PT sensors in the PV module

### 031012-2 / Vol. 135, AUGUST 2013

C)
### Transactions of the ASME

Fig. 4 Temperature difference of temperature under the center

of cell A according to two other locations versus temperature difference of the temperature at the center of cell A and air tem- perature (regression lines added)

were simultaneously acquired along with all temperatures from all sensors by a data logger every 10 s. Analogue inputs and excita- tion sources of data logger were previously calibrated; hence, their effect to the measurement accuracy was negligible. Temperature monitoring was performed continuously for 18 days of different weather conditions ranging from almost clear sky to cloudy days.

### 3 Results

3.1 A Comparison of Laminated PT Sensors. Initially we
have compared temperature results of laminated PT sensors to find possible differences in temperatures at the given locations. Results of temperature differences for the whole monitoring time period are shown in Fig. 4. The center of cell A has mostly higher temperature than the cor- ner (triangles in Fig. 4) and it increases with overtemperature of the cell according to air temperature. Similar but much less pro- nounced trend can be observed by comparing temperatures of cen- ters of cells A and B (circles in Fig. 4). Both cells lie in the middle part of the PV module equally away from the frame thus slight overheating of the center of cell A according to cell B can be attributed to additional adjacent external temperature sensors covered with XPS insulation in the central area of cell A at the back side of the PV module. As shown in Figs. 2 and 3, we have applied three temperature sensors with XPS insulation with total area of approximately 3 cm² in close vicinity to the laminated PT sensor. From the response line in Fig. 4, we can conclude, that the effect of the back side insulated sensor attachments affect the cells temperature difference remains below 2 C in the overtemperature range of 40 C.

3.2 Evaluation of Temperature Measurement From
Voc. Initially, we have compared the open-circuit voltage mea- surement of the cell A and calculated its temperature according to standard EN 60904-5. The standard requires knowledge of open- circuit voltage at STC, temperature coefficient b and diode quality factor A. The latter is used to calculate thermal voltage D ¼ AkT/q which implicitly includes the resulting temperature of PV module. The temperature can be explicitly calculated if the factor A is known. If not, the standard offers another possibility where ther- mal voltage D can be determined from two Vocmeasurements at different steady-state irradiances in the range of interest while keeping constant temperature. We have compared both methods on a set of acquired Vocdata and compared results with tempera- ture of laminated PT sensor in the middle of the cell A. As for open-circuit voltage temperature coefficient we compared results

### Journal of Solar Energy Engineering

Fig. 5 Junction temperature difference between Vocmethods

and the temperature of at the back side at the center of cell A in three cases, where different parameters were used in the Voc method. Pairs of lines show the 95 percentile range of each data sets.

using a value from datasheet of the cell type (b ¼0.36%/ C) and the actual value of the cell A we have previously measured (b ¼0.32%/ C). Thus, we have evaluated three different cases as follows:

(1) b ¼0.36%/ C from datasheet and D ¼ 28 mV from measurement
(2) b ¼0.32%/ C from measurement and D ¼ 28 mV from measurement
(3) b ¼0.32%/ C from measurement and A ¼ 1.18 from measurement Results of all three different cases are shown in Fig. 5. For the
reference temperature we took laminated PT sensor in the center of cell A. Ideally we would expect in Fig. 5 a horizontal line at T –T that equals 0 C. Although there is a pronounced temperature dif- Voc A center

ference between center and corner temperature of cell A (Fig. 4) and T presumably averages this temperature inhomogeneity across the cell, results show a much better agreement when actual V oc

temperature coefficient b and diode quality factor A are used. The 95 percentile range in the latter case exhibits temperature span of 61 C across the whole range of cell temperatures (10–55 C). Thus, we will use these results as a reference temperature measure- ment latter on for comparison, which will be assumed as the true value of the cell temperature for further comparison and uncer- tainty estimates.

3.3 Comparison of Sensors Attached at the Back Side of
PV Module. In Fig. 6, results of temperature, irradiance, and air flow monitoring are shown for a day with mostly clear sky and occasional wind. A detailed measurement data for four different time sections across the day are shown in Fig. 7. It is clearly evident from 10:00 till 14:00 that temperature of the PV module measured by several sensors (see legend in Fig. 6) is in negative correlation to the air flow. Furthermore, pronounced short-time fluctuations of the temperature of the uncovered PT sensor in Figs. 6 and 7, can be also contributed to the effect of air flow across the PV module which effectively cools the sensor to the lowest temperature of all sensors used here. The effect of wind can be also shown in the air temperature as noise and slightly lower temperature trend at the time period with presence of wind. At irradiances below 500 W/m² (morning and evening time) all sensors give very close results except Vocmethod, which renders pronounced deviation of temperature at irradiances below 200 W/m²

### AUGUST 2013, Vol. 135 / 031012-3

Covered PT and TC deliver almost identical results, but up to

1.5 C lower than the laminated PT sensor. TC sensor also exhib- its slightly higher variations which can be attributed to effect of temperature fluctuations of cold junction. Covered digital sensor DS has the lowest values among all covered sensors.
irradiance,

|Fig. 6 Temperature,|and air flow|data acquired|
|---|---|---|
|during a clear sky day|||
|oc|||

(early morning and late afternoon in Fig. 6). Above 200 W/m² the V method matches very closely to laminated PT sensor behind cell A although it is also affected by wind as it is clearly seen in lower left graph in Fig. 7, where the temperature difference increases during the wind induced temperature drop. It is interest- ing that an uncovered PT sensor gives the highest values at low irradiances (upper left graph in Fig. 7) in contrast to other part of the day, where it delivers the lowest values. This is most likely since the temperature gradient through the PV module does not build up at low irradiances. Hence, in that condition PV modules are usually colder on the top side facing sky due to radiation emissivity.

3.4 Time Response Test. To test the response time of the
temperature sensors under test we have repeatedly covered and uncovered the PV module with wooden cover in the time of direct sunlight. This resulted in rapid cooling and heating of the PV module due the relatively low air temperature of the particular day. From Fig. 8, we can conclude that all temperature sensors exhibit similar and adequate time response regarding the thermal capacitance of the PV module. Temperature deviations between all sensors during the shading of the PV module were in a range of 1 C. All readings were in close correlation with the air temper- ature, as shown in Fig. 9.

3.5 Summary. Figure 10 presents the summary of the tem-
perature differences for each sensor according to the calculated temperature from Vocof the cell A, which is taken as a reference cell temperature. Temperatures differences are shown as average values, one sigma deviation ranges and total deviation ranges and are grouped according to weather condition (cloudy, sunny days) and time in a chosen sunny day. Summary was performed on data at irradiances above 200 W/m² to assure valid reference tempera- ture determined from Voc. First thing to be noticed is that there are temperature deviations even between laminated sensors out of the expected uncertainty range. This is a little bit unexpected since these sensors were thor- oughly attached directly to the back side of the cells inside the PV

Fig. 7

Temperature and irradiance data at different times of the day in Fig. 6

module stack, and were exposed to the same temperature condi- tions. The closest mean measurement values exhibits laminated PT sensor in the center of cell A which also has the lowest devia- tions in all conditions. The laminated PT sensor in the corner of the cell A delivers in average 1 C lower temperature results with larger deviations since the cell is cooled at the edges by the white backsheet, which reflects irradiance. Even more discrepancies are noticed in results of PT sensor, laminated in the center of cell B, especially in time periods with higher average irradiance (clear day from 10:00 to 14:00), when the average measured tempera- tures are even lower than at the corner of cell A. Since both cells A and B lie in the same area of the PV module, the only reason to this effect is additional heating of cell A due to several XPS insu- lators at the back side which also influence the air flow behind the cell A. Further, we compare sensors attached at the back side in terms of average temperature difference in the whole dataset (DT ¼ T – TVoc), measured standard deviation (r) and expanded uncertainty

(U) including uncertainty of the sensor itself using coverage factor
Fig. 8 Response of temperature sensors and temperature cal-

||||||k ¼ 2 following|recommendations|
|---|---|---|---|---|---|---|
|culated|from V|during|and uncovering|of the PV|||
|module||||||m|
|||||||m|
||||||m||

culated from Vocduring covering and uncovering of the PV in Ref. [21]. Covered PT (DT ¼1.05 C, r ¼ 0.96 C, U ¼ 1.94 C) and TC (DT ¼1.42 C, r ¼ 0.96 C, U ¼ 3.73 C) sensors deliver somewhat better results than covered DS (DT ¼2.44 C, rm¼ 1.39 C, U ¼ 2.81 C). The worst measurement results demonstrates the PT sensor without insulation as expected (DT ¼3.04 C, r ¼ 2.08 C, U ¼ 4.16 C).

### 4 Discussion

Results show that the Vocmethod is the most accurate way to measure temperature of the PV modules, since it is not affected by sensors displacement or way of attachment. However, it is not ap- plicable at low irradiances. Nonetheless, in order to achieve desired measurement accuracy this method requires detailed knowledge of Voc, temperature coefficient b and diode quality factor A for a particular cell type used in the PV module. Those parameters are rarely well known for a module under test or they are to be even determined from the previous measurements at STC. This makes the use of this method rather limited. Among sensors attached at the back side, PT and TC sensors deliver most accurate results. We prefer PT sensors over TC since the latter have usually higher tolerances and require cold junction temperature compensation. Regarding DS sensors, although show- ing somewhat worse results, they offer some great advantages.

Fig. 9 Air and sensors temperatures during the shading of the

The main advantage is that DS sensors are more versatile particu- PV module larly if several temperatures have to be acquired simultaneously, since they can be connected in parallel to a digital bus with a capacity of more than 30 sensors and require very simple and inexpensive data acquisition equipment. Their main drawback is their sizes (standard JEDEC TO-92 housing) that make them harder to attach to the desired place and are more sensitive to micro-environmental changes. Thus, we explored the possibilities of using DS sensors for PV module monitoring applications and their sensitivity to micro cli- mate at the back side of the PV module. We varied the dimensions of XPS insulation on DS sensors in the way that we varied the lat- eral wall thickness between sensor body and air in three steps,

e.g., approximately 3 mm, 5 mm, and 10 mm as shown in Fig. 11. The height of XPS insulation blocks was kept approximately 30 mm. To minimize the heat flow from sensor across the leads, very thin wires were used that were attached to the back sheet of the PV module by a tape. Hence, the temperature of the wires was kept close to the temperature of the PV module. For each of three insulation configurations, we mounted DS sensor near the center of cell A and performed a few day monitoring. DS sensor readings were compared to the covered PT sensor attached at the center of the cell A.
Fig. 10 Temperature deviations of each sensor measurement Results are summarized in Fig. 12 for two cases with different

method according to the reference temperature, which was cal-weather conditions, i.e., sunny, cloudy day, and all weather condi- culated from Voctions. Since measurements for each case were performed at

Journal of Solar Energy Engineering AUGUST 2013, Vol. 135 / 031012-5

DS sensor (DS18B20) covered by a XPS block with lateral insulation thick-

Fig. 11

ness of 3 mm (left hand side) and 10 mm (right hand side)

In order to render similar measurement precision than PT sensors, the DS18B20 sensors should be mounted by thermally conductive paste and covered by insulation of at least 10 mm thick walls in lateral direction. By that, a low-cost temperature monitoring solu- tion can be achieved with reasonable additional uncertainty in a range of 60.5 C with regard to most commonly used Pt1000 sen- sors, but with much more versatility where temperature has to be measured at multiple locations and/or larger distances.

Fig. 12 Average temperature deviations between DS and PT

sensor at the center of the cell A using different wall thick- nesses of XPS insulation on DS sensor

different times the result datasets for each case were filtered in a way that only results with similar weather conditions were compared. Results indicate that the average deviation of DS sensor results according to the PT sensor reduces by increasing the thickness of the XPS insulation and at 10 mm thick wall they fall within the range of less than 60.5 C under all weather conditions. It is evident, that due to more pronounced effect of XPS insula- tion the positive trend of temperature deviation is much more expressed in sunny conditions or at high irradiances.

### 5 Conclusion

Temperature measurement method from Vocmay give very accurate results (at irradiances above 200 W/m²) only if parame- ters b, A, and Vocat STC conditions are known for the actual PV module under test. Sensors attached at the back side of the PV module cause a slight temperature raise of the cell area around applied insulation, however, less than 1 C in average. They are strongly affected by the air flow at the back side. Both effects call for appropriate insulation trade-off. Small temperature sensors (PT, TC) render very good results if they are attached at the back by thermally conductive paste and covered by insulation at least 10 mm in lateral diameter. However, their usage becomes incon- venient in cases where large number of temperatures at different locations have to be monitored simultaneously. In such cases digi- tal temperature sensors, such as DS18B20, are more appropriate.

Acknowledgment

The authors would like to thank Jozˇe Stepan and Kristijan Brecl for help in the experimental part. The work has been funded by the Slovenian Research Agency under the P2/0197 program.

References [1] King, D. L., Kratochvil, J. A., and Boyson, W. E., 1997, “Temperature Coeffi- cients for PV Modules and Arrays: Measurement Methods. Difficulties and Results,” Proceedings of 26th IEEE Photovoltaics Specialists Conference, Ana- heim, September 29–October 3, pp. 1183–1186. [2] Skoplaki, E., and Palyvos, J. A., 2009, “On the Temperature Dependence of Photovoltaic Module Electrical Performance: A Review of Efficiency/Power Correlations,” Sol. Energy, 83, pp. 614–624. [3] Bliss, M., Betts, T. R., and Gottschalg, R., 2010, “Indoor Measurement of Pho- tovoltaic Device Characteristics at Varying Irradiance, Temperature and Spec-

[4] Fanney, A. H., Davis, M. W., Dougherty, B. P., King, D. L., Boyson, W. E., trum for Energy Rating,” Meas. Sci. Technol., 21(11), pp. 115701–115712.

and Kratochvil, J. A., 2006, “Comparison of Photovoltaic Module Performance Measurements,” ASME J. Sol. Energy, 128, pp. 152–159. [5] King, D. L., 1996, “Photovoltaic Module and Array Performance Characteriza- tion Review, ATP Press, pp. 347–368. Methods for All System Operating Conditions,” NREL/SNL Program

[6] IEC, International Standard 60904-5:1993, Photovoltaic Devices—Part 5: Determination of the Equivalent Cell Temperature (ECT) of Photovoltaic (PV) Devices by the Open-Circuit Voltage Method, 1st ed., IEC, Geneva. [7] Huang, B. J., Yang, P. E., Lin, Y. P., Lin, B. Y., Chen, J. J., Lai, R. C., and Cheng, J. S., 2011, “Solar Cell Junction Temperature Measurement of PV Mod- ule,” Sol. Energy, 85, pp. 388–392. [8] IEC International Standard 60891:2009, Procedures for Temperature and Irra- diance Corrections to Measured I–V Characteristics of Photovoltaic Devices, 2nd ed., IEC, Geneva. [9] Breteque, E. A., 2009, “Thermal Aspects of c-Si Photovoltaic Module Energy

[10] Mattei, Rating,”M., Sol. Energy Notton,, 83G.,, pp. 1425–1433. Cristofari, C., Musselli, M., and Poggi, P., 2006, “Calculation of the Polycrystalline PV Module Temperature Using a Simple Method of Energy Balance,” Renewable Energy, 31, pp. 553–567. [11] Jones, A. D., and Underwood, C. P., 2001. A Thermal Model for Photovoltaic

[12] Prorok, M., Kolodenny, W., Zdanowicz, T., Gottschalg, R., and Stellbogen, D., Systems, Sol. Energy, 70(4), pp. 349–359.

2008, “Reducing Uncertainty of PV Module Temperature Determination Based on Analysis Using Data Gained During Outdoor Monitoring,” Proc. 23rd Euro- pean Photovoltaic Solar Energy Conference, Valencia, Spain, September 6–10,

[13] Krauter, S., and Preiss, A., 2009, “Comparison of Module Temperature Mea- pp. 2865–2871.

surement Methods,” Proceedings of 34th Photovoltaic Specialists Conference (PVSC), Philadelphia, PA, June 7–12, pp. 333–338.

[14] Eke, R., Kavasoglu, S., and Kavasoglu, N., 2012, “Design and Implementation [19] Jankovec, M., Brecl, K., Kurnik, J., Stepan, J., and Topicˇ, M., 2010, of a Low-Cost Multi-Channel Temperature Measurement System for Photovol-“Evaluation of Different Temperature Measurement Methods of Crystalline Sil- taic Modules,” Measurement, 45(6), pp. 1499–1509. icon PV Modules,” 25th European Photovoltaic Solar Energy Conference/ [15] Meijer, G. C. M., 2001, “Temperature Sensors and Voltage References Imple-5th World Conference on Photovoltaic Energy Conversion, Valencia, Spain, mented in CMOS Technology,” IEEE Sens. J., 1(3), pp. 225–234. September 6–10, pp. 4257–4260. Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/135/3/031012/6323733/sol_135_3_031012.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/135/3/031012/6323733/sol_135_3_031012.pdf) by University of Oxford user on 04 August 2026 [16] Maxim DS18B20 datasheet, [http://datasheets.maxim-ic.com/en/ds/DS18B20](http://datasheets.maxim-ic.com/en/ds/DS18B20). [20] Granek, F., and Zdanowicz, T., 2004, “Advanced System for Calibration and pdf Characterization of Solar Cells,” Optoelectron. Rev., 12(1), pp. 57–67. [17] Belmili, H., Cheikh, S. M. A., Haddadi, M., and Larbes, C., 2010, “Design and [21] ISO/IEC, 2008, Guide 98-3, Uncertainty of Measurement—Part 3: Guide to the Development of a Data Acquisition System for Photovoltaic Modules Charac-Expression of Uncertainty in Measurement (GUM:1995), 1st ed., ISO/IEC, terization,” Renewable Energy, 35, pp. 1484–1492. Geneva. [18] Bohorquez, M. A. M., Gomez, J. M. E., and Marquez, J. M. A., 2009, “A New [22] Kurnik, J., Jankovec, M., Brecl, K., and Topicˇ, M., 2011, “Outdoor Testing of and Inexpensive Temperature-Measuring System: Application to Photovoltaic PV Module Temperature and Performance Under Different Mounting and Solar Facilities,” Sol. Energy, 83, pp. 883–890. Operational Conditions,” Sol. Energy Mater. Sol. Cells, 95(1), pp. 373–376.

Journal of Solar Energy Engineering AUGUST 2013, Vol. 135 / 031012-7
