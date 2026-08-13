Available online at www.sciencedirect.com

# ScienceDirect

Solar Energy 110 (2014) 656–666 www.elsevier.com/locate/solener

# Measuring and estimating the temperature of photovoltaic modules

### a,⇑ a b a

## F. Mavromatakis, E. Kavoussanaki, F. Vignola, Y. Franghiadakis

a Technological Educational Institute of Crete, Department of Electrical Engineering, Estavromenos, GR-71004 Heraklion, Crete, Greece b Solar Radiation Monitoring Laboratory, Department of Physics, 1274 University of Oregon, Eugene, OR, USA

Received 30 April 2014; received in revised form 25 July 2014; accepted 6 October 2014 Available online 28 October 2014

Communicated by: Associate Editor Igor Tyukhov

Abstract

The temperature of a photovoltaic module is a key parameter for the accurate assessment of its performance. In cases where actual measurements are not available, a number of different models can be used to estimate the temperature of the module. Seven such rela- tions are applied and evaluated against experimental data. Comparisons show that the residuals can be described by a Gaussian distri- bution with the minimum half width at half maximum of ~2.2 C. Implementation of a simple heat transfer model also results in similar uncertainties (~2.1–2.2 C). Considering the simplicity of the relations, the complexity of the physics involved (uncertainties in the heat transfer coefficients, transient phenomena) this accuracy is usually considered to be satisfactory. A more reliable way to determine module temperature is to use the open circuit voltage method where this single value ideally pro- vides knowledge of the average temperature of all cells. It is shown that this method that utilizes the EN 60904-5 standard is not easy to apply and the accuracy is limited by the uncertainties of the various parameters. In particular, the experimental uncertainty in the deter- mination of the thermal voltage becomes a significant source of uncertainty in determining the parameters that characterize module per- formance if the diode quality factor is not precisely known. An analysis of the accuracy of the required parameters such as the open circuit voltage at reference conditions, its rate of change with temperature, and the diode quality factor indicate that a series of measure- ments in a temperature controlled environment could be used to reach the goal of determining the cell temperature with an uncertainty of 1 C or less. 2014 Elsevier Ltd. All rights reserved.

Keywords: Photovoltaics; Power modeling; Cell temperature; Open circuit voltage; Measurements

# 1. Introduction

temperatures above 45–50 C are usual during summer it is evident that module efficiency decreases significantly from Module temperature is an important factor that influ-efficiency ratings obtained at standard operating conditions ences the power produced by a photovoltaic system based on measurements at 25 C. While temperature effects (Ye et al., 2013; Lobera and Valkealahti, 2013). Typically, are secondary to the influence of incident radiation, accurate a crystalline silicon module loses about 4% of its power output measurements and estimates of the cell/module temperature for every 10 C raise in module temperature. Since module are needed to accurately estimate photovoltaic (PV) system performance and to appropriately manage PV system out- put. In addition, validation of PV system performance ⇑ Corresponding author. requires translation of their output determined under STC E-mail addresses: fotis@staff.teicrete.gr (F. Mavromatakis), ekav@

|E-mail|addresses:|(F. Mavromatakis),|
|---|---|---|
|gmail.com (E. Kavoussanaki), fev@uoregon.edu (F. Vignola), pvjfra@|||
|staff.teicrete.gr (Y. Franghiadakis).|||
|URL: [http://pv.teicrete.gr](http://pv.teicrete.gr) (F. Mavromatakis).|||
|[http://dx.doi.org/10.1016/j.solener.2014.10.009|||](http://dx.doi.org/10.1016/j.solener.2014.10.009|||)
|0038-092X/|2014 Elsevier Ltd. All rights reserved.||

measured during manufacture to the field conditions under which the validation of the system is performed. For field operation of photovoltaic systems, Nominal Operating

F. Mavromatakis et al. / Solar Energy 110 (2014) 656–666
k G tthe relative error of a solar irradiance mea- surement rTthe absolute error in temperature ( C) / the tilt angle of a module Tocell temperature at a reference condition ( C) TSTCthe STC temperature (25 C) b open circuit voltage rate of change with tem- perature (Volts/ C) b⁰ open circuit voltage rate of change with tem- perature (%/ C) Vocopen circuit voltage in (Volts) Voc;oopen circuit voltage at a reference condition (Volts) Voc;STCopen circuit voltage at STC (Volts) D thermal voltage (Volts) Nsnumber of cells in series

Nomenclature

n diode quality factor Gosolar irradiance at a reference condition (W/m²) Gtsolar irradiance at the collector’s plane (W/m²) GSTCsolar irradiance of 1000 W/m² u windwind speed (m/s) Tambambient temperature ( C) U heat exchange coefficient (W/m²/ C) FWHM full width at half maximum of a Gaussian distribution HWHM the half of the FWHM k Bthe Boltzmann constant (J/K) T cell temperature ( C) q the electron charge (Cb) k Vthe relative error of a voltage measurement

Conditions, including Nominal Operation Cell Tempera- ture (NOCT) are often used and NOCT require knowledge of the actual cell temperature (e.g. Muller, 2010). Therefore, to use NOCT it is necessary to either measure the module temperature or to use a model that estimates the module temperature from meteorological data. In general, modules do not provide any direct means to measure cell tempera- ture. While the encapsulation of temperature sensors within a module is possible (e.g. Mattei et al., 2006) it is a process that would add to module cost. The typical method to mea- sure cell temperature consists of attaching a temperature sensor to the back side of the module (e.g. Boho´ rquez et al., 2009; Krauter and Preiss, 2009). There are two ways to estimate cell temperature once the backside temperature of a module is measured. The simplest is to assume that the cell temperature is equal to the temperature on the back of the module. The error introduced by this method is equal to the temperature difference between the temperature inside cell and the backside temperatures. The second method is to add an offset temperature depending on the solar irradiance and the mounting configuration. For example, King et al. (2004) quotes a difference of 3.0 for free standing modules at an irradiance level of 1000 W/m² which is then scaled linearly with irradiance. On the other hand, it is possible to estimate cell temperature by using models based on mete- orological parameters such as incident irradiance, wind speed, ambient temperature, etc. While model estimates cer- tainly have larger uncertainties than measured temperatures, they are useful and certainly produce more accurate PV sys- tem performance predictions than ignoring the temperature effects. Several relations have been developed by various authors over the years. Some of these relations are based on experimental data (e.g. King, 1996), while others utilize both theory and experiment results (e.g. Mattei et al., 2006). The goal of this study is twofold. The first is to highlight the advantages and limitations of the cell temperature

estimation using the EN 60904-5 (1995) standard under field conditions. The second is to compare and contrast seven different relations that estimate the temperature of a photovoltaic module. The model developed by Fuentes (1987) is also applied and is shown to work as well the more phenomenological models. In Section 2 the method prescribed by the EN 60904-5 (1995) standard is discussed along with issues related to its implementation of this pro- cedure in the absence of a solar simulator. In addition, the uncertainties involved in the measurement of cell tempera- tures are also explored. In Section 3 a slightly modified EN 60904-5 (1995) approach is discussed that is also based on the open circuit voltage but better suited for outdoor experiments. The diode quality factor can be determined independently along with the open circuit voltage and its rate of change with temperature. In Section 4 the perfor- mance of seven different module temperature models selected from the literature are examined utilizing experimental data taken at the Technological Educational Institute of Crete (TEIC). Two years of data are used to check the validity of these relationships that provide estimates of photovoltaic module temperature. In addition, the model developed by Fuentes (1987) that uses the installed nominal operating cell temperature and elements of heat transfer theory to determine the module tempera- ture was applied. Finally, in Section 5 the results of this work are discussed.

# 2. Measuring the cell temperature according to the EN 60904-5 standard

The EN 60904-5 standard is a specific approach to esti- mate the solar cell temperature through measurements of the open circuit voltage. The relation used is ≥ ~ T ¼ T þ V V þ D N ln <u>Go</u> ð1Þ o oc oc;o s b Gt

when the diode quality factor, n,is not known. Gtis the solar irradiance incident on the cell/module and T is the cell temperature. The constant Voc;ois the reference open circuit voltage. The Standard Test Conditions are typically chosen for the reference conditions because Voc;STCis given by the manufacturer. The variable b is the rate of change of Voc;STCas a function of temperature and is equal to b⁰ Voc;STCwhere b⁰ is also given by the manufacturer. The accuracy of these values from the manufacturer usu- ally come with a significant uncertainty. The rate of change of Vocas a function of temperature, b, is related to the increase in recombination in the cell as the temperature increases and is given in units of V = C. The thermal voltage D(¼ <u>nk</u> q <u>B</u> <u>T</u> ) is a function of the diode quality factor n and the cell temperature T. The number of cells in series is given by Ns. While any two temperatures and irradiances may be used, the reference temperature and irradiance are chosen to be those of the STC conditions, i.e. TSTCand GSTC. The EN 60904-5 standard determines D through the mea- surement of the open circuit voltage at the same tempera- ture and at two different irradiance levels. Once the diode quality factor is determined, then Eq. (1) can be solved for the unknown cell temperature. It is important to establish the uncertainties of the EN 60904-5 standard approach. The uncertainty for crystalline silicon under typical operating conditions is examined in the following example. To simplify the discussion, it was assumed that there were no uncertainties in the reference temperature of 25 C and irradiance of 1000 W/m². The rate of change with temperature and the open circuit voltage at STC conditions are provided by module manufacturers with two and three significant digits, respectively. Thus, typical relative errors are around 3% and 0.5%, respectively (e.g. 0 2 1 b ¼0:35 0:0110 C, Voc;STC¼ 21:5 0:1 V). The use of error propagation in the formula used to determine D (1) yields an uncertainty of 0.02 V when D is around

0.03 V (The large uncertainty in D is at least an order of magnitude greater than the small uncertainties in Voc;STCof
0.5% and b of 3% that were used to determine the uncer- tainty in D). Using the same approach and Eq. (1) to determine the uncertainty in cell temperature yields the equation
2 2

||||V||V||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2||2|oc||oc;STC||||||||
|T|b|o V||V|||||||t|STC|
|||2||2|||||||||
||D s|STC|G|s||oc;STC|||||||
|||t||||s|||||GG||
|||||||3|||||||
||||||||GG||||||

2 2 <u>oc oc;STC</u> rT¼ðkbðT ToÞÞ þ kV ocþ kVoc;STC b b # ~ ~ r N G ktDN þ ln þ ð2Þ b G b

The variable D is the main factor that affects the uncer- tainty of the cell temperature. If the diode quality factor is not known, the standard methodology for determining D yields

<u>VOC1VOC2</u> D ¼ ð3Þ NslnðGt1=Gt2Þ

for two different irradiance levels Gt1and Gt2. The uncer- tainty in D is affected by the relative difference between the two irradiance levels because of their presence in the natural log in the denominator and this in turn dominates the uncertainty in D. The closer the two different levels of irradiance, the larger the uncertainty on D. This relation- ship is illustrated in Fig. 1 that assumes a 0.5% uncertainty in the open circuit voltages. For typical conditions the uncertainty in temperature is 2–3 C. In order to reduce the cell temperature uncertainty even further, the uncer- tainty in D must be reduced and this would require improved estimates of Voc;STCand b (to less than ~0.3%). To reduce the uncertainties in cell temperature estimates using the EN 60904-5 methodology, it is necessary to improve the determination of D. This requires measure- ments of the open circuit voltage with an accuracy of the order of 40 mV or better for a 36 cell module and irradi- ance levels which differ by e.g. 50%. This last condition runs counter to the EN 60904-5 standard because it pro- poses measurements should be performed ”... in the range of interest and at the same cell temperature”. To fulfill this requirement, the irradiance differences should be in ~10– 20% range. However, small differences in irradiance leads to large uncertainties in D as shown in Fig. 1. To reduce uncertainties in cell temperature estimates, D should be determined with a relative error of less then 10%.

# 3. A similar approach for the measurement of a module’s temperature

Eq. (1) given previously can be rewritten in a form suit- able for linear regression ≥ ~ <u>nk N TB s STCGt</u> Voc¼ Voc;STCþ ln ≥ q ~ GSTC <u>nkBNsGt</u> þ b þ ln ðT TSTCÞð 4Þ q GSTC

which reduces to

Voc¼ Voc;STCþ b ðT TSTCÞð 5Þ 2 for irradiances very close or equal to GSTC¼ 1000 W=m. While keeping the incident irradiance close to GSTCand oc;STC ier to determine. The second term in each of the square brackets in Eq. (4) involving the natural log of G =G can be used to estimate the adjustments that need to be made to V and b to account for small differences in the global irradiance. For example, for n ¼ 1:0 (ideal case)

and N ¼ 36, these terms become 0:925 ln STC <u>t</u> Vand

3:10 10 ln <u>t</u> V/K, respectively. To ensure that the STC temperature measured at the back of the module is the same as the temperature of the solar cells, measurements have to be performed with the module embedded in a tem- perature controlled environment to bring the module into thermal equilibrium with the surroundings.

" ~ ~ varying the solar cell temperature V and b become eas-

<u>nkB T</u>

Fig. 1. The relative uncertainty on D (=

) is shown as a function of the ratio of the two different irradiances that should lie in the range of interest q according to the EN 60904-5 (1995) standard.

Under normal operating conditions outdoors, the tem- perature of the solar cells is different from the temperature on the backside of the module and the changing conditions don’t allow the module to reach thermal equilibrium (e.g. Krauter and Preiss, 2009). Placing the module in a temper- ature controlled box enables the module to reach thermal equilibrium and to have the backside of the module have the same temperature as the solar cells in the module. Any difference between the temperature at the back of the module and the solar cells would shift the estimated Voc;STCof the relationship determined by Eq. (5). This effect is illustrated in Fig. 2 for data from a Shell SM 55 module. Linear regression through Eq. (5) leads to an open circuit voltage of 21.308 ± 0.003 V. Application of a shift of 3 C in all temperatures, to account for the difference between cell temperature and the back of the module, leads to a new value for the open circuit voltage of 21.505 V, while the slope (rate of change of the open circuit voltage) does not change within the uncertainties. However, under real conditions both the intercept and the slope will change. A difference in Voc;STCof ~0.2 V will significantly affect the determination of the cell temperature and its uncertainty (~2.7 C in this example). In order to avoid the unknown temperature difference between the back of the module and the solar cells under outdoor conditions, the module will have to

be covered by an opaque material, be exposed to the sun to record VOC, covered again to avoid unnecessary heating and cool/heat through forced convection to a predeter- mined temperature until Tbackis equal to Tcell(e.g. Huang et al., 2011; Muller et al., 2011).

This procedure will have to be repeated to acquire data over the desired range of temperatures. The change of the module’s open circuit voltage due to the incoming irradi- ance, when exposed for a few seconds, is not significant and much less than the case of concentrated photovoltaic cells (e.g. Moriarty and Emery, 1998). The diode quality factor of crystalline silicon solar cells does not appear to change appreciably (e.g. Breitenstein, 2013; Khan et al.,

2010) under typical operating outdoor conditions. Even if we assume that the diode quality factor is irradiance depen- dent, then we may conduct measurements at M different irradiance levels. The straight line fits will provide us with 2M equations, while the unknowns are M + 2. An alterna- tive solution may involve the determination of the diode quality factor by other means like dark I–V measurements (e.g. King et al., 1997; Bashahu and Nkundabakura, 2006). Of course it is also possible to estimate the diode factor through both ways and compare the results.
# 4. The experimental data

In general, module temperature data are not available and a model is used to estimate it. Temperature models are based on the prevailing meteorological conditions in order to calculate the module’s temperature. There are sev- eral phenomenological models derived from experimental data, while other models are built on a theoretical founda- tion. In this section the available large data set is used to check the statistical significance of seven simple relations. In addition, various thermal (heat transfer) models are available in the literature (e.g. Lobera and Valkealahti, 2013; Armstrong and Hurley, 2010) and the relatively

Fig. 2. Linear regression of the measured open circuit voltage versus DT for a Shell SM 55 photovoltaic module under natural daylight. The intercept is

determined as 21.308 ± 0.003 V.

simple model of Fuentes (1987) was selected for this study as it can be unambiguously implemented since the software code is provided by the author. The module temperature data were acquired over a per- iod of two years from September 2009 to October 2011. Two Phaesun USP 10 modules were placed at tilt angles of 0 and 30 facing South along with two new CMP11 pyr- anometers at the same tilt. The module temperatures were recorded every minute via type T thermocouples (0.5 C uncertainty) along with the solar irradiances (<3% uncer- tainty), while at a short distance away (~10 m), a meteoro- logical station was recording air temperature (0.5 C uncertainty) and wind speed (5% uncertainty) with the same frequency as other meteorological parameters. The wind pattern is well described by a Weibull distribution with a scale parameter of 3.2 and a shape parameter of

1.6 based on 244,052 data points. This implies that the average wind speed in the area is relatively low. The data were selected with an angle of incidence less than 50 to avoid the angular effects introduced by the front glass and a solar irradiance greater than 150 W/m² to avoid large uncertainties associated with low irradiance measurements.
## 4.1. Module temperature relations

There are several models available in the literature that provide estimates of the cell temperature based on the pre- vailing meteorological conditions namely solar irradiance, air temperature, wind speed and sky temperature (e.g. Bardhi et al., 2012). The models used in the present study

are listed below in chronological order along with the spe- cific coefficients given in the corresponding references. Model 1 (Eq. (6)) is taken from King (1996).

Gt 2 T ¼ Tambþ ð0:0712 uwind2:411 uwindþ 32:96Þð 6Þ 1000

Model 2 (Eq. (7)) is taken from King et al. (1998).

Gt 0:223 u T ¼ Tambþ 1000 ð19:6 ewindþ 11:6Þð 7Þ

Model 3 (Eq. (8)) is taken from TamizhMani et al. (2003)

T ¼ 0:943 Tambþ 0:028 Gt1:528 uwindþ 4:3 ð8Þ

Model 4 (Eq. (9)) is taken from King et al. (2004).

T ¼ Tambþ Gte 3:56 0:075 uwind ð9Þ

Model 5 (Eq. (10)) is taken from Duffie and Beckman (2006).

<u>Gt9:5</u> T ¼ Tambþ 800 ðTNOCTTa;NOCTÞ 5:7 þ 3:8 uwind ð10Þ

Model 6 (Eq. (11)) is taken from Mattei et al. (2006).

<u>UPVTambþ GtA</u> T ¼ ð11Þ UPVBGt

where UPVis the heat exchange coefficient and A, B are constants related to the module under consideration. The factor UPVis linear in wind speed along with a fixed term,

i.e. its form is a þ buwind. Model 7 (Eq. (12)) is taken from Skoplaki et al. (2008).

Table 1

Fit results. Parameters abcdthe full width at half maximum is a measure of the accu- Model 1 a

2.23 25.2 –

|/¼0|0.0712|2.23||25.2|–||
|---|---|---|---|---|---|---|
|/ ¼ 30 Model 2|0.0712|2.82||30.9|–||
|/¼0|17.8|0.223||9.76|–||
|/ ¼ 30 Model 3|23.5|0.223||10.5|–||
|/¼0|1.07|0.0186||1.37|3.07||
|/ ¼ 30 Model 4|1.08|0.0226||1.83|4.22||
|/¼0|3.72|0.075||––|||
|/ ¼ 30 Model 5|3.54|0.075||––|||
|/¼0|5.70|1.79||–|–||
|/ ¼ 30 Model 6|5.70|2.04||–|–||
|/¼0|25.5|3.47||–|–||
|/ ¼ 30 Model 7|20.9|3.32||–|–||
|/¼0|8.91|2.78||–|–||
|/ ¼ 30 Parameter held fixed.|8.91|1.81||–|–||
|||||||mod|
|Table 2||||||obs mod|
|Results based on the temperature relations.||||||obs|
|Model /¼0|1 2|3|4567||||
|Gaussian center|0.5|0.8|0.6|0.7|0.5 0.7||
|r / ¼ 30|1.9|2.0|1.8|3.4|2.1 2.9||
|Gaussian center|0.6|0.7|0.6|0.8|0.5 0.4||
|r Gaussian center and r in degrees Celsius.|2.2|2.4|1.9|4.1|2.5 2.3||

/¼0 0.0712 a

a a

a a

a a

a a a

a

0.5
a

2.0
a

0.6
a

2.4
a

<u>0:32</u> T ¼ Tambþ Gtð12Þ 8:91 þ 2:0 uwind

Models 1–7 are examined to determine the extent to which they fit the experimental data. The Gaussfit software (Jefferys et al., 1988) was adopted for this purpose because it can handle large volumes of data. Next, part or all of the model parameters were allowed to vary in order to find the best fit and the resulting parameters are given in Table 1. Subsequently, the frequency histograms were studied and fit with gaussian profiles to determine the offset between

Table 3

Results based on the Fuentes model. Horizontal module Year

|Year|2009|2010|2011|2009|2010|2011|
|---|---|---|---|---|---|---|
|Data|5861|83,359|59,578|28,854|119,526|95,674|
|Gaussian center|0.9|0.4|0.9|0.7|0.8|0.7|
|r Gaussian center and r in degrees Celsius.|1.2|1.8|1.5|1.9|2.0|1.7|

a a a

modeled and experimental temperatures and the width of the distribution (Table 2). As already noted, the half of

### racy of a model.

## 4.2. The Fuentes model

The model presented by Fuentes (1987) is applied with- out modifying any of the equations. This model uses the installed nominal operating cell temperature (INOCT) to estimate the module’s temperature for a given set of ambi- ent temperature, wind speed and solar irradiance. An advantage of this model is that the thermal properties of the module and the mounting configuration are consoli- dated into a single value (INOCT). Fuentes (1987) states an overall uncertainty of less than 4 C and typically, an uncertainty of less than 2.5 C. More details about the physics and the assumptions made can be found in this publication (Fuentes, 1987). The 2009 TEIC data were used by the software to determine the INOC temperatures. Temperatures of 39.8 C and 44.7 C are determined, respectively, for the horizontal and tilted modules. The computed INOCT values were then input to the second part of the code that performs the necessary calculations to estimate the module’s temperature. The modeled tem- peratures (T) were used to calculate the difference DT ¼ T T and build the necessary frequency histo- grams, where T is measured on the back of the module. These were fit with Gaussian profiles to get the most fre- quently occurring offset between the experimental and modeled data and the HWHM of the distribution. The half width of the distribution (HWHM) yields the typical uncer- tainty and is given in Table 3. Table 3 shows that the typ- ical offset is less than one degree Celsius, while the scatter (HWHM) ranges from 1.4 to 2.4. If data from all years are input to the model as a single set (/ ¼ 0 ) then a scatter of 2.1 C is found (Fig. 3), while in the case for the tilted module it is 2.2 C(Fig. 4). Note that the probability to find a value within ±HWHM from the center of the gauss- ian is 76%. Thus, 24% of the temperature differences in the data set will be larger than the HWHM. The offsets of max- imum propability in DT are then 0.3 ± 2.1 C and

0.7 ± 2.2 C, respectively.
# 5. Discussion

The VOCmethodology for temperature measurements (EN 60904-5, 1995; King et al., 2004) is quite promising

Tilted module

Fig. 3. The distribution of DT is shown along with the best Gaussian fit (dash-dotted line). Data from the module at a tilt angle of 0 are used. The center

of the Gaussian is located at 0.3 C, while the HWHM is 2.1 C.

Fig. 4. The distribution of DT is shown along with the best Gaussian fit (dash-dotted line). Data from the module at a tilt angle of 30 are used. The center

of the Gaussian is located at 0.7 C, while the HWHM is 2.2 C.

in the sense that it does provide an estimate of the cell one degree Celsius level, it is necessary to determine the temperature (on average) through a single measurement. module parameters with sufficient accuracy. The uncer- However, the determination of all other parameters tainty analysis presented in Section 2 shows that in order involved is not an easy task, especially when a solar simu-to get down to such an uncertainty, the relative uncertain- lator is not available which is the general case. To ensure ties for the voltage measurements should be ~0.2%, while that the uncertainty in the cell temperature lies within the solar irradiance should be measured with an accuracy

Fig. 5. The predictions of the selected models are shown as a function of wind speed for a solar irradiance of 800 W/m² and an ambient temperature of

20 C. The top plot shows the results using the available correlations from the literature (Models 1–7) while the lower plot shows the results when the best fit parameters, as shown in Table 1, are implemented.

of ~2% or better. The uncertainties on VOC;STCand b will be and the corresponding rate of change with temperature determined through linear regression of a VOCversus DT (b) with sufficient accuracy. However, accurate measure- dataset. Any other factors that affect the measurements will ment of the cell temperature is necessary to achieve the cause a scatter in the data and consequently, will lead to desired accuracy using the VOCmethod. Thus, a solar sim- increased uncertainties of the STC values. Thus, stable ulator should be used with the module at thermal equilib- meteorological conditions are needed to achieve the rium or the module should be enclosed in a temperature required accuracy. Experimental measurements under nat-controlled chamber as discussed in Sections 2and3. Using ural daylight conditions show that it is possible to deter-the VOCmethodology with modules at thermal equilibrium mine the open circuit voltage at STC conditions VOC;STCprovides an excellent opportunity to explore the module

Fig. 6. The distribution of DT is shown for the best fit relation (4) and for the worst two relations (5 & 6) according to Table 2. The rest of the Models

perform better than Model 5 and worse than Model 6. Data from the module at a tilt angle of 30 are used.

performance/temperature correlations to a higher degree of accuracy than currently is being done in the field. In addi- tion these experiments can be conducted over a wide range of temperatures and irradiance levels. It is clearly a difficult task to summarize into a single relation the effects of all mechanisms that contribute to heat loss from a photovoltaic module. A quick survey in the literature reveals several different formulas for the heat loss coefficient under forced convection conditions (e.g. Mattei et al., 2006; Sartori, 2006; Armstrong and Hurley,

2010). The available models provide estimates of the cell temperature are essentially used under all weather condi- tions and any tilt and orientation of the module (Fig. 5). The higher the time resolution of the data, the larger the deviations between actual and calculated module tempera- tures since the thermal mass of a typical module does not
respond to time scale of minutes or less. Nevertheless, some of the models provide a reasonable description of the experimental data (Fig. 6). Model 4 results in the minimum scatter (HWHM) of 2.2 C, followed by Model 1 with a scatter in the range of 2.2–2.6 C. Model 3 is not suitable for wind speeds higher than ~10 m/s since its simple linear dependence leads to unrealistic low module temperatures. Some of the models converge to the ambient temperature under very strong wind conditions. Also Model 5 seems to overestimate the temperature at low wind speeds and slightly underestimate the temperature at higher wind speeds. This behavior may be explained by the specific heat loss coefficient adopted by the authors. Certain models require the wind speed to be measured at a height of 10 meters. Inverter manufacturers may provide the necessary hardware that allows the communication and the recording

of data between the inverter, the solar sensor, the wind speed sensor and the temperature sensors for the module and the ambient air. In general, it is easier for the owner of a PV system to install a meteorological station at a height of e.g. 2 meters rather than at 10 meters. In cases where a model uses heat transfer coefficients that result from correlations of Nusselt numbers, the wind speed is considered at the level of the surface. Also it must be kept in mind that these models describe the temperature of a module under the assumption of ther- mal equilibrium. If this condition does not hold, then large differences can and do result. Especially, under partially cloudy conditions it may be hard to estimate reliably the module temperature. The time response to changes in the temperature depends on the thermal mass of the module and the prevailing conditions (e.g. Armstrong and Hurley, 2010). In addition, if the time resolution of the data is shorter than the typical thermal response times then the models will not perform satisfactorily. If the time resolu- tion of the experimental data are averaged to longer than the thermal time constant, then variations may be smoothed out and better agreement can be expected. The best fit coefficients listed in Table 1 appear similar to the original values in Section 4.1 but some differences are apparent. These new parameters can lead to tempera- ture estimates that differ by several degrees. The model with the least change in parameters is Model 4 for the tilted module. This model displays a global or generic character independent of the module specifics. The rest of the models provide estimates of the module temperature with an over- all uncertainty of less than 3 C. This is a statistical result based on the distribution of conditions experience at our Institute. At very low or high wind velocities the estimates made by certain models deviate significantly as shown in

Fig. 6. In general, one may use a statistically significant

data set to determine the “local” coefficients for such tem- perature relations and then use the updated relation to pre- dict the temperature of the module for any meteorological conditions. The Fuentes (1987) model appears to provide satisfac- tory estimates of the temperatures with an uncertainty of ~2 C despite its simplicity. The author states errors less than 5 C and when temperatures at high insolation levels are considered, then the uncertainties are closer to 2.5 .It is also interesting to note that the model works equally well for the zero tilt module although the code was developed for a 30 C tilted module. Under wind speeds of several m/s and above, forced convection is much stronger than natural convection and in cases of combined free and forced convection, the final heat transfer coefficient may be calculated as either the maximum of the two coefficients or as the third root of the sum (or difference) of the two coefficients to the power of 3 (e.g. Nellis and Klein, 2008, Chapter 6, p.769). The coefficients are added if the two mechanisms act in phase. If the two mechanisms tend to suppress each other then the two coefficients will be sub- tracted. In general, the effect of natural convection to the

final heat transfer coefficient is minor. Under forced con- vection conditions, the two modules are not expected to react differently as the surfaces are flat and the assumption that the heat transfer coefficient does not change signifi- cantly between /¼0 and / ¼ 30 is valid. Under very low or no wind conditions differences are expected in the heat transfer coefficient since natural convection is tilt dependent. The Fuentes (1987) model provides satisfactory estimates of the module temperature with an accuracy of about 2 C. However, it may not be easily integrated as published into a photovoltaic energy model since indepen- dent knowledge of the INOCT parameter is needed and in addition, the software code cannot be summarized into a single relation like those listed in Section 4.1.

# 6. Conclusions

Knowledge of PV module temperature is essential for an accurate assessment of module performance as solar module efficiency decreases by about 0.4% per degree Celsius. The accuracy of the temperature is important because a 2.5% error in the estimated temperature would lead to about a 1% error in the module performance. A comparison is made between seven models that estimates the module tempera- ture using the solar irradiance and other meteorological measurements. The comparison shows that the residuals (TexpTmod) follow a Gaussian distribution with a spread of ~2.2 C (HWHM). A simple heat transfer model also results in similar uncertainties of 2.1–2.2 C. The cell tem- perature may be estimated through measurements of the backside temperature by adding an irradiance dependent offset. In the case of free standing modules, an uncertainty in cell temperature is on the order of ~1–3 C depending on the characteristics of the module itself and the actual meteorological conditions. A more reliable way to determine the cell temperature in a module is to use a measurement of the open circuit volt- age. An examination of the EN 60904-5 standard method- ology demonstrated that considerable effort is needed to minimize the uncertainties in the parameters that are used to make the temperature estimates especially in the case where the diode quality factor has to be measured. To achieve the desired accuracy in cell temperature the evalu- ation in this paper concludes that a series of measurements in a temperature controlled environment are needed to accurately obtain the open circuit voltage, its rate of change with temperature and the diode quality factor under a range of temperatures and solar irradiances. The uncertainty analysis of this method showed the accuracy of the measurements that needed to be achieved in order to produce cell temperature values to the one degree Cel- sius level of uncertainty. This method is not easy to apply given the uncertainties of the various parameters that appear in the calculations according to the EN 60904-5 standard, especially in the case where the diode quality fac- tor is unknown. It is proposed to determine the required parameters through a series of measurements in a temper-

ature controlled environment where the open circuit volt- age, its rate of change with temperature along with the diode quality factor can be estimated for a range of temper- atures and solar irradiances. The error analysis of this method shows that accurate measurements of the various parameters are required in order to get down to the degree Celsius level.

# Acknowledgement

This project is implemented through the Operational Program “Education and Lifelong Learning”, Action Archimedes III and is co-financed by the European Union (European Social Fund) and Greek national funds (National Strategic Reference Framework 2007–2013).

# References

Armstrong, S., Hurley, W.G., 2010. A thermal model for photovoltaic panels under varying atmospheric conditions. Appl. Therm. Eng. 30,

1488.
Bardhi, M., Grandi, G., Tina, G.M., 2012. Comparison of PV cell temperature estimation by different thermal power exchange calculation methods. In: International Conference on Renewable Energies and Power Quality, Santiago de Compostela, Spain, pp. 28–30. Bashahu, M., Nkundabakura, P., 2006. Review and tests of methods for the determination of the solar cell junction ideality factors. Sol. Energy 81, 856. Boho´ rquez, M.A.M., Go´ mez, J.M.E., Ma´rquez, J.M.A., 2009. A new and inexpensive temperature-measuring system: application to photovol- taic solar facilities. Sol. Energy 83, 883. Breitenstein, O., 2013. Understanding the current-voltage characteristics of industrial crystalline silicon solar cells by considering inhomoge- neous current distributions. Opto-Electron. Rev. 21 (3), 259. Duffie, J.A., Beckman, W.A., 2006. Solar Engineering of Thermal Processes. Wiley Interscience, Ch 23. EN 60904-5, 1995. Photovoltaic devices – Part 5: Determination of the equivalent cell temperature (ECT) of photovoltaic (PV) devices by the open-circuit method. Fuentes, M.K., 1987. A simplified thermal model for flat-plate photovol- taic arrays, Sandia report, SAND85-0330. Huang, B.J., Yang, P.E., Lin, Y.P., Lin, B.Y., Chen, H.J., Lai, R.C., Cheng, J.S., 2011. Solar cell junction temperature measurement of PV module. Sol. Energy 85, 388–392.

Jefferys, W.H., Fitzpatrick, M.J., McArthur, B.E., 1988. GaussFit – a system for least squares and robust estimation. Celestial Mech. 41, 39–

49.
Khan, F., Singh, S.N., Husain, M., 2010. Effect o the illumination intensity on cell parameters of a silicon solar cell. Sol. Energy Mater. Sol. Cells 94, 1473. King, D.L., 1996. Photovoltaic module and array performance charac- terization methods for all system operating conditions. Proceeding of NREL/SNL Photovoltaic Program Review Meeting. Sandia National Laboratories. King, D.L., Hansen, B.R., Kratochvil, J.A., Quintanna, M.A., 1997. Dark current-voltage measurements on photovoltaic modules as a diagnostic or manufacturing tool. In: 26th IEEE Photovoltaic Specialists Con- ference, Anaheim, CA. King, D.L., Kratochvil, J.A., Boyson, W.E., Bower, W.I., 1998. Field experience with a new performance characterization procedure for photovoltaic arrays. In: 2nd World Conference and Exhibition on Photovoltaic Solar Energy Conversion, 6–10 July, Austria. King, D.L., Boyson, W.E., Kratochvil, J.A., 2004. Photovoltaic Array Performance Model. Sandia National Laboratories, SAND2004-3535. Krauter, S., Preiss, A., 2009. Comparison of module temperature measurement methods. In: 34th IEEE, Photovoltaic Specialists Conference. Lobera, D.T., Valkealahti, S., 2013. Dynamic thermal model of solar PV systems under varying climatic conditions. Sol. Energy 93, 183. Mattei, M., Notton, G., Cristofari, C., Muselli, M., Poggi, P., 2006. Calculation of the polycrystalline PV Module temperature using a simple method of energy balance. Renew. Energy 31, 553. Moriarty, T., Emery, K., 1998. Thermophotovoltaic cell temperature measurement issues. In: 4th NREL Conference on Thermophotovol- taic Generation of Electricity, Denver, CO. Muller, M., 2010. Measuring and modeling nominal operating cell temperaturei (NOCT). In: PV Performance Modeling Workshop, Albuquerque, NM, September 22–123. Muller, M., Deline, C., Marion, B., Kurtz, S., Bosco, N., 2011. Determining outdoor CPV cell temperature. In: 7th International Conference on Concentrating Photovoltaic Systems, Las Vegas, NV. Nellis, G., Klein, S., 2008. Heat Transfer. Cambridge University Press. Sartori, E., 2006. Convection coefficient equations for forced air flow over flat surfaces. Sol. Energy 80, 1063–1071. Skoplaki, E., Boudouvis, A.G., Palyvos, J.A., 2008. A simple correlation for the operating temperature of photovoltaic modules of arbitrary mounting. Sol. Energy Mater. Sol. Cells 92, 1393. TamizhMani, G., Ji, L., Tang, Y., Petacci, L., Osterwald, C., 2003. Photovoltaic module thermal/wind performance: long-term monitor- ing and model development for energy rating. NCPV and Solar Program Review Meeting. NREL. Ye, Z., Nobre, A., Reindl, T., Luther, J., Reise, C., 2013. On PV module temperatures in tropical regions. Sol. Energy 88, 80.
