This full text paper was peer-reviewed at the direction of IEEE Instrumentation and Measurement Society prior to the acceptance and publication.

# Photovoltaic Module Cell Temperature Measurements using Linear Interpolation Technique

a a a a a b Gavin Mangeni, Rodney H. G. Tan, T. H. Tan, S. K. Cheo, V. H. Mok and J. Y. Pang *a* *Faculty of Engineering, Technology & Built Environment, UCSI University, Kuala Lumpur, Malaysia.* *b* *School of Engineering and Physical Sciences, Heriot Watt University, Putrajaya, Malaysia.*

***Abstract*—This paper presents a photovoltaic module cell temperature measurement and 81 points heat distribution**

**mapping technique using only 9 temperature sensors. The operating principle, mapping technique, experiment setup and**

**performance analysis of the proposed measurement system is discussed. The proposed measurement system consists of 9**

**negative temperature coefficient thermistor based temperature sensors attached at the back of photovoltaic panel equally spaced**

**in 3 by 3 manner, a microcontroller, a data acquisition and visualization software with interpolation technique developed in**

**MATLAB. The proposed temperature measurement system is verified using FLUKE infrared thermometer at every single point**

**of measurement. The results show an average error of 1 °C and** **the error tend to decrease as the solar irradiance received from the panel increases. The proposed measurement system contributes to**

**the visualization of 9 by 9 heat distribution across a given panel** **for thermal flow analysis in PV/T cooling design studies.**

***Keywords—Temperature measurement, Heat distribution, NTC thermistor, Photovoltaic module, Infrared thermometer, PV/T***

I. INTRODUCTION
Most of the applications relating to the field of solar energy and more specifically photovoltaic applications, require one to know the temperature on the surface of photovoltaic modules as well as the solar radiation incident on them with adequate precision and reliability [1 – 4]. This is because the I-V curve of the photovoltaic module depends on the temperature and incident solar irradiation [5]. As a result, the maximum power point that determines the optimal operation point for efficient use of the photovoltaic module changes continuously [6, 7]. The climatic conditions in Malaysia are highly favorable for development of solar energy systems since Malaysia lies entirely in the equatorial zone [8]. The design and testing of a new and inexpensive digital sensor based temperature-measuring system with remote operation is presented. A precision Pt100 sensor was used as the standard sensor for calibration and comparison [9]. An aerial solar thermography and monitoring system is developed to determine the operational status on large-scale solar PV installations. Infrared thermography has the ability to see the heat differential of the PV cells and can thus be used to show when any of those cells are defective [10]. An efficient and low- cost NTC thermistor based temperature logging system for measurements of photovoltaic module temperature is developed [11]. A study of the NTC thermistor characteristic curve-fitting methods is discussed [12]. This is because the thermistor characteristic equation directly determines the

temperature measurement accuracy of the sensor. However, previous research works are mainly focusing on measuring the temperature of solar PV using only one temperature sensor. In this work, we propose an inexpensive and accurate temperature measurement system to study the effects of heat dissipation on a single PV module. The system configuration is NTC sensor based and interpolation technique is applied to estimate 81 multiple temperature measurements using only 9 sensors. The proposed system helps in thermal flow analysis studies of photovoltaic/thermal (PV/T) systems, for instance, evaluation of the daily thermal characteristic of a BIPVT collector [13] and solar collector cooling systems design since PV cooling not only lowers the PV cell temperature, but also enhances its thermal efficiency [14, 15]. Smart monitoring of PV plants can be used to study the ageing effects of third generation solar cells under different stress conditions [16], and early detection of system failures like hotspots, cells cracking, encapsulation and corrosion failures [17].

## II. METHODOLOGY

*A. Overview* The block diagram of the proposed temperature measurement system is given in Fig. 1. The system consists of 9 NTC thermistor sensors that measure temperature of the photovoltaic module. The temperature acquisition unit is a device used for collect the temperature reading from NTC thermistor as demonstrated in Fig. 2. The temperature acquisition unit consists of a microcontroller and a temperature measurement circuit board. The microcontroller receives these temperature readings, digitizes them and sends them serially via its USB protocol to the end user computer in real time. Matlab software is used to develop an interactive graphical interface to display the heat distribution of the solar module under test.
978-1-5090-3596-0/17/$31.00 ©2017 IEEE

Solar PV

Temperature Acquisition Unit

Fig. 1. Block diagram of the developed measurement system

Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on August 04,2026 at 10:51:35 UTC from IEEE Xplore. Restrictions apply.

NTC sensor The Negative Temperature Coefficient (NTC) thermistor is a ceramic oxide semiconductor, which can meet the requirement of high-precision temperature measurement, and thus chosen for use in this project over the traditional Positive Temperature Coefficient thermistors like the Pt100. The functional relationship between NTC thermistor resistance and temperature obeys a negative exponential function of R-T (resistance-temperature) equation. As a result, the NTC thermistor is primarily used as both a resistive temperature sensor and a current limiting device. The thermistor operates in such a way that when the temperature is increased, the value of its resistance drops, and has an operating temperature range from -55 °C to 125 °C. The specification used in this project is the BS25 3950 NTC thermistor, with 10 Kȍ resistance value and 1% precision. Theoretically, the NTC thermistor characteristics show a negative exponential curve equation, but in practice the use of the theoretical equation would lead to a significant nonlinear error [12]. Therefore, equation (1) with an alternative characteristic of the resistance curve fitting is chosen.

## 111 <u>R</u>

(1) =+*In*()
## TT B₀₀R0

where *T₀* is nominal temperature, *B₀* is nominal Beta constant, *R* is resistance (ȍ) and *T* is temperature (K). Reformulating equation (1) for the NTC thermistor gives the temperature value according to equation (2).

<u>1</u> *T* =− 273.15 11 *R*

(()(log)) + () *BRT*000
(2)
where *BO = 3950*, nominal beta constant at 25 °C, *RO* = 10 Kȍ, nominal resistance at 25 °C, *TO* = 298.15 K, nominal temperature at 25 °C. The resistance value, R is determined using a voltage divider circuit. The circuit consists a 10Kȍ resistor connected in series with the NTC thermistor. 5V DC from the microcontroller board is applied to power the resistive circuit. The microcontroller then reads the value of the potential across the NTC thermistor via its analog pin, and then outputs the specified string to a serial port with 10 bit ADC resolution

i.e. 0-1023 in decimal. The value sent serially is an integer value and thus needs to be converted to voltage according to equation
(3).
<u>1024</u> *ADC* = *Vout**() (3) *Vref*

Consequently, the measured resistance across the thermistor is determined by equation (4).

*R* = <u>0</u>

(4)
<u>R</u> 1024 ()1 − *ADC*

Microcontroller

Fig. 2. Temperature acquisition unit hardware assembly

*B. Heat Distribution Mapping Technique* The heat distribution mapping technique is a technique that is used to develop a thermograph that records and displays the temperature measurements at the back surface of the PV module under test. The application of this technique consists of calibration, linear interpolation and a display interface of the PV module cell temperature by color mapping. A flowchart of the developed software program is given in
Fig. 3. The program begins with initialization of the serial
 communication port of the microcontroller. Thereafter, the program reads the temperature from the 9 NTC sensors. A 3 by 3 matrix array is created and consequently linearly interpolated to a 9 by 9 matrix array and the results are printed onto a color map. If the stop button not active, the program will continuously read the temperature values. If the user presses the calibration button, the calibration mode will activate.
Fig. 3. Flow chart of the developed software program
 The calibration method is demonstrated in Fig. 4. The first role is to identify the calibration mask that is obtained by

subtracting the set calibration value from the temperature readings from the NTC thermistor. A 3 by 3 matrix is used as an example to illustrate this principle. The temperature measurement data is then be added to calibration mask value to get the actual calibrated temperature readings that are recorded for further analysis. It is observed that the first set of data immediately after calibration will all be equal, thereby offsetting any errors that might arise due to mismatch among the NTC thermistors sensors.

Fig. 4. Example to illustrate the calibration method used

Linear interpolation technique is used to estimate new temperature data points within the range of the readings obtained from the temperature sensors. This technique enables us to estimate and calculate multiple temperature measurements from the photovoltaic module. Linear interpolation algorithm in two dimensions is computed using equations (5) and (6). It requires only four known data values that are nearest to each other and are located in diagonal directions from a given value in order to estimate a value that is assumed to lie on a straight line joining the two nearest points in each dimension [18]. ªº *aa* 11 12

(5) «»
¬¼ *aa*21 22

() <u>aa +</u> 11 <u>11 12</u> 12 2 ()( <u>aa11</u>+++++<u>21</u>*aaaa*11 12 21 22)() <u>aa12 22</u> 242

(6)
() <u>aa21+22</u> 21 2 22

The algorithm illustrates a method used to expand the measurement area without increasing the number of NTC thermistors. The advantage of using linear interpolation technique is that one can enjoy cost savings, as they do not need to purchase the extra temperatures sensors.

A color map is used to visualize the heat distribution thermograph at the back of the PV module. The aim is to be able to observe the temperature changes of the PV module under direct sun, so as to assess it performance. A 9 by 9 matrix array size is chosen to implement the heat distribution mapping. The color bar is used to display the color scale as well as indicate the mapping of the temperature readings on the color map.

## III. RESULTS AND DISCUSSION

*A. Experimental Setup* The experimental setup of the proposed temperature measurement system illustrated in Fig. 5. The apparatus used to measure the temperature of the photovoltaic module include; thermal compound, infrared thermometer, solar power meter, Blu-tack adhesive, USB cable, notebook computer and the temperature acquisition unit. The photovoltaic module is placed onto a metal trolley and the entire set up tested outdoors under direct sunlight. The Blu-tack adhesive is used to attach the thermistor to the PV module, whereas the thermal compound helps to maximize the contact surface area between the PV module and the NTC sensor. The Fluke 572-2 temperature infrared thermometer helps in calibration of the NTC temperature sensor and it is also used to verify the accuracy of the measured temperature data recorded using the developed software program. The PCE-SPM 1 cosine corrected solar power meter is used to measure the horizontal irradiation in units of Watt per meters squared (W/m²). The irradiance readings are useful in understanding how the sunlight striking the photovoltaic module affects the heat dissipated at the back of the PV module, and thus evaluate its performance.
Solar PV

Solar Power Meter Temperature Acquisition

Fig. 5. Overall experimental setup

Table 1 shows the characteristics of the photovoltaic

module used in this experiment. The data in table 1 is obtained separately using standard test results of the I-V curve characteristics of the PV module.

ªº *aa* «» «»Unit «» «» «» «» *aa* «» ¬¼

|TABLE I.|MONO-CRYSTALLINE PV MODULE CHARACTERISTICS||
|---|---|---|
|Maximum power output (W)||80|
|Maximum power current (A)||4.142|
|Maximum power voltage (V)||19.485|
|Short circuit current I|(A)|4.293|
|Open circuit voltage V|(V)|23.176|
|Series resistance R|(Ohm)|0.5|
|Shunt resistance R|(Ohm)|294.72|

*sc*

*oc*

*s*

*sh*

The procedures followed when conducting the experiment are given.

- Clean the front surface of the PV module to remove any dust particles.
- Apply thermal compound to each of the NTC sensors and then place them to the back surface of the PV module using Blu-tack adhesive.
- Ensure there is minimal shading or sun blocking at the area where the PV module is placed.
- Place the PV module at desired tilt angle in degrees and allow it expose to sunlight for 10 minutes.
- Place the solar power meter beside the PV module as shown in fig. 5 so as to measure the radiation.

|31.60|31.81 32.02|32.23|32.43 32.54|32.64 32.74|32.84|
|---|---|---|---|---|---|
|31.63|31.85 32.07|32.29|32.50 32.54|32.57 32.6|32.63|
|31.65|31.88 32.11|32.34|32.56 32.53|32.49 32.46|32.42|
|31.68|31.92 32.15|32.40|32.63 32.53|32.42 32.32|32.21|
|31.70|31.95 32.20|32.45|32.69 32.52|32.34 32.17|31.99|
|32.09|32.24 32.40|32.56|32.71 32.58|32.45 32.32|32.18|
|32.47|32.54 32.60|32.67|32.73 32.64|32.55 32.46|32.37|
|32.85|32.83 32.80|32.78|32.75 32.71|32.66 32.61|32.56|
|33.23|33.12 33.00|32.89|32.77 32.77|32.76 32.76|32.75|

- Open Matlab software and run the PV temperature measurement program.
- Record and verify the temperature readings using the infrared thermometer.
Fig. 6 illustrates how the 9 NTC temperature sensors are

positioned at the back surface of the mono crystalline PV module. The temperature sensors are placed in such a way that they are evenly spaced from one another and are labeled T1 to T9 respectively.

conducted outdoors at UCSI University that is located at latitude: 3°5’5. 531” N, and longitude: 101°44’12. 64” E from January to August 2016.

Table 2 shows the 81 linearly interpolated temperature data

points using only 9 readings from the NTC sensors. The highlighted points in gray represent the positions where the sensors are placed. It is observed that the interpolated values are got by repeatedly halving intervals in each dimension using equation (6). For instance, 32.11 °C in row 3, column 3 of interpolated data is calculated by first linearly interpolating between known sensor readings at locations [1 5; 1 5] represented in matrix form, giving four new estimated values in each dimension (blue highlight). The average of these values

i.e. 32.02 °C, 31.65 °C, 32.56 °C, 32.20 °C, gives the desired temperature by further interpolation. A polynomial straight-line is generated during interpolation and each links two consecutive points of the sequence in both the *x* and *y* directions [19,20]. TABLE II. INTERPOLATED TEMPERATURE DATA POINTS
Temperature data points from thermistor

<u>31.60 32.43 32.84</u>
<u>31.70 32.69 31.99</u>
33.23 32.77 32.75
Interpolated Temperature data points

<u>31.60 31.81 32.02 32.23 32.43 32.54 32.64 32.74 32.84</u>

|T1|T2|T3|
|---|---|---|
|T4|T5|T6|
|T7|T8|T9|

Fig. 6. Temperature sensor placement onto the solar module

*B. Results and Discussion* The results of the photovoltaic cell temperature measurement system are presented. The experiments were
Fig. 7 represents a 3 by 3 heat distribution color map that

displays the temperature from PV module at solar irradiances of 642 W/m², 581 W/m² and 456 W/m². These results were recorded on a sunny day, 3 rd August 2016. Each of the color maps accurately displays the different thermal levels from the PV cells. As the solar irradiance increases, the PV module dissipates more heat and the temperature measurements consequently change color to the hotter regions according the color bar scale. It is also observed that the heat distribution is non-uniform across the PV module.

Fig. 7. 3 by 3 heat distribution color map at different irradiance

Fig. 8 represents a 9 by 9 heat distribution color map that

has been interpolated using temperature data from Fig. 9. An infrared thermometer is used to verify the reliability and accuracy of the obtained interpolated temperature measurements. It is also observed that the heat distribution before and after interpolation on the color map is similar, and therefore the interpolation program was successfully executed with zero errors present.

Fig. 10. Measurement comparison at irradiance of 581 W/m²

The bar graph in Fig. 11 represents temperature measurement comparisons a low irradiation of 456 W/m². It is observed that the average temperatures are 56 °C and 55 °C for proposed method and the infrared thermometer readings respectively. The maximum temperature using the proposed

Fig. 8. 9 by 9 interpolated heat distribution color map at different irradiance

method was 57.3 °C, and it was obtained at sensor positions T6 that is placed near the middle section of the PV module. A bar graph used to compare the temperature measurements between proposed method and the infrared thermometer at an irradiance of 642 W/m² is given in Fig. 9. All the NTC sensors were calibrated to 60 °C at the start of the experiment. It is observed that the average temperature of the proposed method and infrared thermometer is 59 °C and 58 °C respectively. The highest observed temperature using the two approaches was 61 °C.

Fig. 9. Temperature measurement at irradiance of 642 W/m²

The bar graph in Fig. 10 represents the temperature 2 measurements comparisons at an irradiance of 581 W/m. The average temperature using the proposed method and the infrared thermometer was 56 °C and 55 °C respectively. The average temperature got using the two approaches dropped as 2 2 the irradiation reduced from 642 W/m to 581 W/ m. The highest temperature of 58.5 °C was observed from sensors placed at position T6 using the proposed method.

Fig. 11. Measurement comparison at irradiance of 456 W/m²

The average temperature of each sample of 9 temperature measurements at a given irradiation level from Figures 9,10 and 11, is calculated by adding up all the temperatures and dividing the sum by the sample size equal to 9. Comparison of these average temperatures for both the proposed method and thermometer method gives an average error of േ1 °C. The effect of solar irradiance on the amount of heat dissipated from the solar module using data obtained from the proposed system is illustrated in Fig. 12. It is observed that the module temperature increases as the solar intensity increases for each of the temperature measurements, and thus proof that the heat transfers faster at higher irradiance levels. It is also noticeable that module temperatures rise from the bottom (T9)

towards the upper part (T1), and the highest cell temperatures are concentrated close to the modules middle section (T5).

Fig. 12. The effect of solar irradiance on heat dissipation

However, other factors could also result in the increase of the surface temperature at the back of the module for example local shading of some cell areas of the panel as the sun shines. This leads to the creation of hot spots that could reduce the lifespan of the module. Non-uniform temperature distribution along the solar module is observed despite the fact that all sensors start at the same values after calibration. This is as a result of the differences in the PV cell response to environmental factors like ambient temperature, irradiation and airflow velocity.

## IV. CONCLUSION

This work presents the methodology for estimating the photovoltaic module cell temperature and heat mapping distribution. 81 temperature data measurements were obtained from only 9 NTC sensor readings using linear interpolation technique. This technique helps to save cost, as only a few sensors are required and has more applications in the modeling of I-V curves for PV modules. The highest temperature recorded during the experiments was 61 °C at an irradiance of 642 W/m². An average error of േ1 °C was obtained when the results were compared with those from the Fluke infrared thermometer, which was also used as the standard sensor for calibration. The relationship between solar irradiance and the module cell temperature was also discussed. It was deduced that cell temperature of the PV module increased at higher irradiance levels. This work will be beneficial for PV/T cooling system design studies, evaluation of PV module ageing effects and early detection of PV system failures.

ACKNOWLEDGMENT

The author would like to thank UCSI University CERVIE for providing the financial support (Research Grant Scheme Grant No. Proj-In-FETBE-022) to conduct this research.

REFERENCES [1] Y. Lee and A. Tay, "Finite Element Thermal Analysis of a Solar Photovoltaic Module", *Energy Procedia*, vol. 15, pp. 413-420, 2012. [2] S. Chander, A. Purohit, A. Sharma, Arvind, S. Nehra and M. Dhaka, "A study on photovoltaic parameters of mono-crystalline silicon solar cell with cell temperature", *Energy Reports*, vol. 1, pp. 104-109, 2015. [3] Zaini, N. H., M. Z. Ab Kadir, M. Izadi, N. I. Ahmad, MA M. Radzi, and

N. Azis. "The effect of temperature on a mono-crystalline solar PV panel", In *2015 IEEE Conference on Energy Conversion (CENCON)*, pp. 249- 253,IEEE, October 2015.
[4] M. Martínez, J. Andújar and J. Enrique, "Temperature Measurement in PV Facilities on a Per-Panel Scale", *Sensors*, vol. 14, no. 8, pp. 13308- 13323, 2014. [5] J. Gow and C. Manning, "Development of a photovoltaic array model for use in power-electronics simulation studies", *IEE Proceedings-Electric* *Power Applications*, vol. 146, no. 2, p. 193, 1999. [6] Enrique, J.M., Andújar, J.M. and Bohórquez, M.A., "A reliable, fast and low cost maximum power point tracker for photovoltaic applications", *Solar Energy*, *84*(1), pp.79-89, 2010. [7] Enrique, J.M., Andújar, J.M., Durán, E. and Martínez, M.A., "Maximum power point tracker based on maximum power point resistance modeling", *Progress in Photovoltaics: Research and* *Applications*, *23*(12), pp.1940-1955, 2015. [8] Mekhilef, S., Safari, A., Mustaffa, W.E.S., Saidur, R., Omar, R. and Younis, M.A.A., “Solar energy in Malaysia: current state and prospects”, Renewable and Sustainable Energy Reviews, 16(1), pp.386-396, 2012. [9] M. Bohórquez, J. Enrique Gómez and J. Andújar Márquez, "A new and inexpensive temperature-measuring system: Application to photovoltaic solar facilities", *Solar Energy*, vol. 83, no. 6, pp. 883-890, 2009. [10] Denio, Harley. "Aerial solar thermography and condition monitoring of photovoltaic systems", In *2012 38th IEEE*, pp. 000613-000618, IEEE, June 2012. *Photovoltaic Specialists Conference (PVSC),*

[11] R. Eke, A. Sertap Kavasoglu and N. Kavasoglu, "Design and implementation of a low-cost multi-channel temperature measurement system for photovoltaic modules", *Measurement*, vol. 45, no. 6, pp. 1499- 1509, 2012. [12] Cong, Yu, Zhou Wang-chao, Sun Bin, and Zhou Hang-xia. "Study on NTC thermistor characteristic curve fitting methods", In *Computer* *Science and Network Technology (ICCSNT), 2011 International* *Conference on*, vol. 4, pp. 2209-2213. IEEE, December 2011. [13] J. Kim, S. Park, J. Kang and J. Kim, "Experimental Performance of Heating System with Building-integrated PVT (BIPVT) Collector", *Energy Procedia*, vol. 48, pp. 1374-1384, 2014. [14] H. Tsai, "Design and Evaluation of a Photovoltaic/Thermal-Assisted Heat Pump Water Heating System", *Energies*, vol. 7, no. 5, pp. 3319-3338,

2014.
[15] X. Xu, R. Niu and G. Feng, "An Experimental and Analytical Study of a Radiative Cooling System with Flat Plate Collectors", *Procedia* *Engineering*, vol. 121, pp. 1574-1581, 2015. [16] L. Ciani, M. Catelani, E. Carnevale, L. Donati and M. Bruzzi, "Evaluation of the Aging Process of Dye-Sensitized Solar Cells Under Different Stress Conditions", *IEEE Transactions on Instrumentation and Measurement*, vol. 64, no. 5, pp. 1179-1187, 2015. [17] L. Cristaldi, M. Faifer, M. Lazzaroni, M. Khalil, M. Catelani and L. Ciani, "Diagnostic architecture: A procedure based on the analysis of the failure causes applied to photovoltaic plants",

2015.
*Measurement*, vol. 67, pp. 99-107,

[18] Zhang and I. Lee, "Interpolation of Sensory Data in the Presence of Obstacles", *Procedia Computer Science*, vol. 29, pp. 2496-2506, 2014. [19] Y. Bai, Z. Zhao, Z. Sun and L. Quan, "A Linear Interpolation Fuzzy Controller for a Boiler Pressure Control System", *IFAC Proceedings* *Volumes*, vol. 46, no. 5, pp. 650-654, 2013. [20] Y. Tsuno, Y. Hishikawa and K. Kurokawa, "Modeling of the I–V curves of the PV modules using linear interpolation/extrapolation", *Solar Energy* *Materials and Solar Cells*, vol. 93, no. 6-7, pp. 1070-1073, 2009.
