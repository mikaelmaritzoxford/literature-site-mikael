Available online at www.sciencedirect.com

Solar Energy 93 (2013) 183–194 www.elsevier.com/locate/solener

# Dynamic thermal model of solar PV systems under varying climatic conditions

⇑

## Diego Torres Lobera, Seppo Valkealahti

Department of Electrical Energy Engineering, P.O. Box 692, FI-33101 Tampere, Finland

Received 18 December 2012; received in revised form 13 February 2013; accepted 7 March 2013 Available online 13 May 2013

Communicated by: Associate Editor Jan Kleissl

Abstract

The operating temperature of photovoltaic (PV) modules plays a central role in the photovoltaic energy conversion process, because the output voltage and, thereby, the produced output power decreases with increasing module temperature. The thermal response of PV modules is dynamic to changes in the climatic conditions affecting to the module. Therefore, a steady state model of module temperature cannot be justified. This paper presents a dynamic thermal model based on the total energy balance in the PV module. Main heat transfer mechanisms between the module and its environment have been modelled theoretical. The model is verified by the measurements data of the TUT solar photovoltaic power station research plant, which contains an accurate weather station, solar radiation measurements and a mesh of irradiance and module temperature measurements. A systematic sensitivity analysis of site-specific parameters was carried out to fine- tune the dynamic thermal model. The model was validated using time series of 1-s measurements data of three summer months and was found to differ less than 2 C from the measured module temperatures 80% of the time. 2013 Elsevier Ltd. All rights reserved.

Keywords: Photovoltaic; Thermal model; PV module; Module temperature; Solar power generation; Site-specific parameters

# 1. Introduction

the module materials, the surrounding environment, and the present and recent climatic conditions. The electrical performance of photovoltaic (PV) cells Previous work in modelling the temperature of PV mod- and modules is affected by climatic conditions directly via ules has focused on obtaining correlations that predict the incident solar radiation and indirectly via operating tem-module temperature based on the incoming solar irradi- perature, which depends upon many factors such us ambi-ance, ambient temperature and wind speed (Schott, 1985; ent temperature, wind speed, and direction. (Nagae et al., Servant, 1985; Malik and Damit, 2003; Nordmann and

2006). The PV cell operating temperature plays, in fact, a Clavadetscher, 2003; Krauter, 2004; Franghiadakis and central role in the photovoltaic conversion process, because Tzanetakis, 2006; Mattiei et al., 2006; Chenni et al., 2007; the output voltage and, thereby, the power produced by Durisch et al., 2007, and Topic et al., 2007). These cells and modules decreases considerably with increasing approaches generally do not consider the thermal mass of temperature (Skoplaki et al., 2008). The operating temper-the modules, but assume that the module temperature fol- ature of PV modules depends on the physical properties of lows immediately the changes in the climatic conditions,
i.e., a steady-state approach is assumed to be valid. Similar result is obtained by methods, which simply predict the
⇑ Corresponding author. Tel.: +358 40 1981 510. module temperature by extrapolating a known reference E-mail address: diego.torres@tut.fi (D. Torres Lobera). state, such as the normal operating cell temperature TNOCT

0038-092X/$ - see front matter 2013 Elsevier Ltd. All rights reserved. [http://dx.doi.org/10.1016/j.solener.2013.03.028](http://dx.doi.org/10.1016/j.solener.2013.03.028)

D. Torres Lobera, S. Valkealahti / Solar Energy 93 (2013) 183–194
(Skoplaki et al., 2008,andSkoplaki and Palyvos, 2009). However, a steady-state model of PV module temperature cannot be justified during periods of rapid fluctuation of irradiance when the thermal inertia of the module becomes significant (Jones and Underwood, 2001). Field measure- ments at higher sampling rates than 1-min indicate that major changes in irradiance can take place within seconds (Ransome and Funtan, 2005). The slow thermal response of the PV module to sudden changes in irradiance has been pointed out by (Jones and Underwood, 2001), clearly indi- cating the effect of the thermal mass on the thermal response. During rapid irradiance changes the measured module temperature varied within 3 C, but a conventional steady state thermal model predicted temperature fluctua- tion of over 20 C. An error of this magnitude in the ther- mal model will lead to major errors in the predicted output power. In this paper a dynamic thermal model considering the effect of the thermal mass of the PV module in the heat transfer model is developed. The present work extends the previous work based on first-principles energy balance of the PV module (Jones and Underwood, 2001; Notton et al., 2005; Mattiei et al., 2006; Balog et al., 2009; Arm- strong and Hurley, 2010; Caluianu and Ba˘ lta˘ re u, 2012, and Tsai and Tsai, 2012). Previous authors either simplified the thermal model by neglecting some of the heat transfer mechanisms, attempted to implement site-specific correla- tions for obtaining the heat transfer coefficients in cases which are non-site-specific or simplified the model by ignoring some other effects. The present work presents a state of the art generic dynamic thermal model modelling the heat transfer mechanisms of the PV modules without major simplifications. This paper additionally includes a sensitivity analysis and fine-tune of several site-specific parameters required to improve the accuracy of the model. The simulated results are validated using experimental data, collected at the TUT Solar PV Power Research Test Plant in Tampere, Finland (Torres Lobera and Val- kealahti, 2012).

# 2. Thermodynamics of a PV module

The module temperature is calculated considering the thermal energy exchange of the module with its environ- ment through the main heat transfer mechanisms. Estab- lishing the total energy balance on the PV module leads to the following expression:

<u>dTmod</u> q inPoutqlossCmod¼ 0 ð1Þ dt where qinis the incoming shortwave solar radiation reaching the front surface of the PV module, Poutis the electric power produced by the module, qlossincludes the heat transfer losses from the PV module to the envi- ronment and vice versa, Cmodis the heat capacity of the PV module, Tmodis the module temperature, and t is time.

The effective incoming solar radiation reaching the front surface of the PV module can be calculated as:

q ¼ aGA; ð2Þ in where G is the incoming solar irradiance on the tilted PV module, a is the absorptivity and A the area of the PV module. The output power can be extracted directly from the electrical current–voltage characteristic of the PV module as:

### Pout¼ IU; ð3Þ

where I is the produced current and U the voltage. The main mechanisms of heat losses from the PV mod- ule to the environment are conduction, convection and radiation. However, the contact area between the PV mod- ule and its mounting rack is small and the conduction losses can be neglected leading to:

q loss¼ qconvþ qlw; ð4Þ where qconvis the heat loss due to convection, and qlwdue to long-wave radiation. Heat capacity refers to the energy transfer required to change the temperature of an object. In the case of the PV panel, which is a multi-layer laminate, the module heat capacity has traditionally been calculated as a composite of the heat capacities of layers in the laminate:

X N Cmod¼ AdnqnCp;n; ð5Þ n¼1

where dnis the thickness, qnthe density and Cp,nthe specific heat of layer n. N is the number of layers in the module. Because exact heat capacity of the studied PV modules or material parameters of module layers were not available, the values in Table 1 have been used to obtain a first approximation of the heat capacity. In following sections of this paper the value of heat capacity is adjusted based on experimental measurements to its optimal value by a sensitivity analysis. If actual material parameters of the PV module were known, the final heat capacity could be calculated directly in line with the first approximation.

## 2.1. Convection losses

Convective heat transfer occurs between the PV module surface and the surrounding layer of air. The convective mechanisms for PV modules are free convection and forced convection due to the wind. In practice, it is problematic to model convective mechanisms and, therefore, empirical functions have usually been used for approximating the convection losses (Notton et al., 2005). Therefore, only the forced convection component has traditionally been considered when modelling the PV module operating tem- perature. However, in this model, both free and forced con- vection mechanisms are considered to reproduce more accurately the heat exchange between the PV module and the surrounding air in line with (Incropera, 2007, p. 423).

Table 1

Parameter values used to calculate the heat capacity of the studied PV module NP1900Gkg (Jones and Underwood, 2001, and Armstrong and Hurley, 2010). The surface area of the module is A = 1.32 m².

|||||||!|~|||
|---|---|---|---|---|---|---|---|---|---|
|Layer|d (m)|C (J/kg K)|q (kg/m³)|Ad C|q (J/K)|||||
|Glass|0.00400|500|3000|7920||||||
|EVA|0.00100|2090|960|2648||||||
|PV cells|0.00020|677|2330|416||||||
|Rear contact|0.00001|900|2700|32||||L||
|Rear cover|0.00400|1250|1200|7920||||||
|Total||||18,936||L L||mod film 2|air|
|||||||L||||

Layer dn(m) Cp,n(J/kg K) qn(kg/m³) Ad Cn p,nqn(J/K)

According to Newton’s law of cooling, the convective losses are proportional to the overall temperature differ- ence between the surface and the fluid. For the PV module they are defined as:

q conv¼ AhconvðTmodTairÞ; ð6Þ

where hconvis the convection heat transfer coefficient and Tairis the ambient air temperature. The convection heat transfer depends on the physical situation like mounting of the module and the wind conditions. For obtaining hconvboth the free and forced convection heat transfers must be calculated. This is conventionally done by applying air properties in the vicinity of the sur- face. Because the temperature differences in the vicinity of the PV module surface are reasonable, the average of the PV module surface temperature Tmodand the ambient air temperature Tair:

<u>Tmodþ Tair</u> Tfilm¼ ð7Þ 2

is adequate to calculate air properties. The air properties needed are the specific heat Cp, density q, kinematic viscos- ity m, thermal conductivity j, and Prandtl number Pr. These values are obtained by interpolating the values found in the tables of air properties (Weast, 1984), or by finding

|3|3|3|
|---|---|---|
|conv|free|forced|

the best curve fit of the values in the tables and using the obtained equations to evaluate the air properties at the film temperature. Characteristic length L of the object, needed to calculate free and forced convective heat transfer coefficients, is obtained as follows:

<u>A</u> L ¼; ð8Þ 2ðH þ W Þ

where H is the height and W the width of the PV module. The free convection heat transfer coefficient is defined as:

<u>Nufreek</u> h free¼; ð9Þ L

where Nufreeis the Nusselt number for free convection. The most commonly used empirical correlation for external free convection flows in a plate inclined less than 60 is (Incrop- era, 2007):

### Nufree¼ 0:68 þ 0:67ðRaLWÞ; ð10Þ

when the Rayleigh number RaLis in the range 0<RaL<10 9. W is a function dependent on the Prandtl number and is defined as (Incropera, 2007).

16 <u>9</u> 9 <u>16</u> <u>0:492</u> W ¼ 1 þ ð11Þ Pr

Rayleigh number Ra is defined as (Incropera, 2007)

<u>9:81 cosðwÞjT T jL³</u> Ra ¼ Gr Pr ¼ Pr; ð12Þ T m

where Gr is the Grashof number and w is the angle of the PV module to the vertical direction. (Sparrow and Tien, 1977) proposed an empirical method of calculating the forced heat transfer coefficient and showed how it can be calculated regardless of the mod- ule orientation. This method has already been utilised in (Balog et al., 2009) and it defines the forced heat transfer coefficient as

<u>1</u> 2 <u>0:931qmC Rep</u> h forced¼<u>2</u>; ð13Þ LPr³

where Re is the Reynolds number. It is defined as:

Re ¼ <u>L</u> v w; ð14Þ qm

where vwis the local wind speed. The Nusselt number for forced convection can be calculated as:

h forcedL Nuforced¼ : ð15Þ k

Free and forced convection mechanisms are combined into one convective mechanism by the approximation (Incropera, 2007):

### Nu ≈ Nu þ Nu; ð16Þ

such that

Nuconvk h conv¼ L : ð17Þ

## 2.2. Black-body radiation losses

The rate of long wave electromagnetic energy radiation (black body radiation) per unit of area of a body at a sur- face temperature T (in K) is given by the Stefan–Boltzmann law:

q lw¼ reT⁴; ð18Þ

where r is the Stefan–Boltzmann constant and e is the emissivity of the surface. Thus the heat flux from the front and back sides of a PV module standing freely on the roof of a building are, respectively:

|q|F|T|T þre|F|T|T⁴;|
|---|---|---|---|---|---|---|
|lw;front|front fs|4mod|4sky|front fr|4mod|roof|
|lw;back|back bs|||back br||roof|

lw;front¼ A½refront fs 4mod 4sky front fr 4mod roof

q ¼ A½re F T T þre F T T⁴;

ð19Þ

where efrontand ebackare the emissivities of the front and back surfaces, respectively, and Ffs fr bs br

||, F, F|and F|are|
|---|---|---|---|
||fs fr|bs|br|
|||mod||
|sky|||roof|

the view factors from the front-to-sky, front-to-roof, back-to-sky and back-to-roof, respectively. T is the module temperature, T the sky temperature, and T the temperature of the roof. The emissivity of the front and back surfaces of the PV module are typically considered to be between 0.9 and 1 (Balog et al., 2009). The view factor is the fraction of radi- ation which leaves a surface and reaches another surface (Holman, 1992). For a PV module mounted with a tilted angle b (0 6 b 6 p) the view factors are calculated as:

Ffs¼ <u>1</u> 2 ð1 þ cos bÞ; Fbs¼ <u>1</u> 2 ð1 þ cosðp bÞÞ; <u>1 1</u> ð20Þ Ffr¼ 2 ð1 cos bÞ; Fbr¼ 2 ð1 cosðp bÞÞ:

For the case of a PV module mounted with a mounting rack covering the back-plate as illustrated in Fig. 1, the heat flux of long wave radiation on the back of the module takes place mostly between the module and the mounting rack with a view factor of 1. Accordingly, the radiation heat fluxes on the front and on the back are

||4mod 4sky||4mod|
|---|---|---|---|
|front fs||front 4mod 4rack|fr|
|lw;back|back|||

q lw;front¼ A re F T T þre F T T⁴roof;

q ¼ Are T T;

ð21Þ

where Trackis the temperature of the mounting rack. It can be approximated to be equal to the ambient air tempera- ture since the mounting rack is normally under the shadow of the PV module for most of the time and perpendicular to the roof. The roof temperature Troofis more complicated to approximate since it depends on the roof material and the warming up of the construction material itself. According to measurements, a black surfaced roof can reach over

Incoming Long-wave radiation irradiance exchange

50 C higher temperatures than the ambient air temperature. The measurement of the sky temperature is complex and rarely available, which has motivated some authors to either utilise the ambient temperature as the sky tempera- ture (Tsai and Tsai, 2012) or to neglect the contribution of the black-body radiation losses from the PV module to the environment in the overall losses (Armstrong and Hur- ley, 2010). There is extensive literature about the topic and some authors (Hegazy, 2000; Kudish et al., 2002,andNot- ton et al., 2005) have utilised the formula given by (Swin- bank, 1963):

Tsky¼ 0:0552Tair 1:5 : ð22Þ

However, the formula given by (Schott, 1985)

20 Kðclear skyÞ Tsky¼ TairdT; dT ¼ ð23Þ 0 KðovercastÞ

and used in (Jones and Underwood, 2001) provided a more accurate prediction for the module temperature. This ap- proach considers two possible sky conditions, clear sky and overcast, which implies the need of knowing the sky condition. The cloud amount is defined as the amount of sky estimated to be covered by clouds and it can be mea- sured using ceilometers (WMO, 2008). However, such de- gree of accuracy is not required in this study. Just an index of overcast vs. clear sky is needed. This can be

global solar radiation with the theoretical clear-sky radia- tion (clearness index (Wong and Chow, 2001)), with a cam- era recording the sky and analysing the image or by the fraction of diffuse radiation from the incoming solar radia- tion (Wong and Chow, 2001):

k d¼ <u>Gd</u>; ð24Þ Gt

where Gdis the diffuse and Gtthe global incoming solar radiation. This parameter represents the amount of diffuse radiation of the total amount of solar radiation being close to 1 under overcast conditions, and close to 0 under clear sky conditions. Fig. 2 illustrates the kddistribution mea- sured in Tampere, Finland, over a year during daytime with solar radiation data measured with a sampling rate of 1 Hz at the TUT Research Plant (Torres Lobera and Valkealahti, 2012). The peak near 0.95 corresponds to overcast conditions and around 0.18 to clear sky condi- tions. The range from 0.3 to 0.7 corresponds to periods of sky partially covered by clouds, sunrise and sunset. Therefore, it is possible to set limit value for kdto discrim- inate between overcast and clear sky conditions.

# 3. Dynamic thermal model of a PV module

## 3.1. Calculation method

According to Chapter 2 the module temperature Tmodis a nonlinear, time-varying equation without analytical

Convection exchange Mounting rack

Fig. 1. Diagram of the mounting configuration of the PV module with its

mounting rack. The heat transfer processes are indicated with arrows.

hi achieved in several ways such as comparing the incoming

Fig. 2. Distribution of diffuse radiation fraction kdover a year in

Tampere, Finland, during daytime calculated with solar radiation data measured with a sampling rate of 1 Hz.

solution. Therefore, it must be solved numerically. Substi- tuting Eqs. (2), (3), (6), and (21) in Eq. (1) yields: <u>dTmodAaG PoutAhconv</u>ðÞ <u>TmodTair</u> ¼ dt Cmod e frontFfsT 4mod T 4sky þ efrontFfrT 4mod T 4roof þ ebackT 4 modT 4 rack Ar Cmod ð25Þ

Then, the module temperature Tmodat time t + s can be solved based on the value at time t using Eq. (25) by the Euler method as:

<u>dTmod</u> Tmodðt þ sÞ¼TmodðtÞþs; ð26Þ dt

where s is the time step. s must be small to ensure stability of the solving method, which will increase the computa- tional costs in long-term simulations. However, extrapola- tion of the time used for the simulations included in this article indicates that annual simulations would require a couple of minutes to be completed. Therefore the computa- tional costs related to the operation of this thermal model

|DT ¼|ðT|T Þ|;|
|---|---|---|---|
|RMSE|m;i|s;i||
||i¼1|||
|m,i|||s,i|

should not be a concern. Measured module temperatures exhibit changes of over 10 C within a minute. To properly model such fast phe- nomena, the data required for simulations must be time series of, at least, 1-s measurements. The parameters needed to develop and test the simulation method based on Eqs. (25) and (26) are the incident irradiance in the plane of the PV module, ambient temperature, module temperature, horizontal global solar radiation, horizontal diffuse solar radiation, wind speed, and module output power. In this study, all parameters are selected in accor- dance to the characteristics of the PV modules installed at the TUT Solar PV Power Station Research Plant. The dynamic thermal simulation model of a PV module has been developed and tested using measurements collected with the climate and electrical measuring systems of the TUT Research Plant (Torres Lobera and Valkealahti,

2012). The response time constants of the measuring instru- ments have been evaluated and considered to be fast enough to accurately measure the real operating conditions.
## 3.2. Sensitivity analysis of the simulation model

## 3.2.1. Overall capability of the model

Most of the parameters used in the dynamic thermal model are measured climatic variables or parameters that can be extracted from the manufacturer datasheet. Those have been used as such for the model. However, some parameters and factors affecting to the performance of the thermal model either cannot be measured or depend on the site-specific characteristics of the environment where the PV modules are located. Those parameters were the absorptivity a, heat capacity C of the PV module, frac- mod tion of diffuse radiation defining clear sky condition kd, wind speed adjustment coefficient waand roof absorptivity coefficient ar. The effect of parameters, which are not precisely known, to the PV module temperature have been analysed by using two sets of measured data corresponding to three winter days (from March 13th to 16th 2012) and three summer days (from June 13th to 16th 2012). The winter and sum- mer dates have been chosen in such way that the datasets contain data with clear sky, partially cloudy, and overcast conditions to ensure the accuracy of the thermal model for most of the climatic conditions. Preliminary studies indi- cated that the approach of analysing three days is sufficient to evaluate the accuracy of the thermal model under, at least, two different environmental conditions (i.e. clear sky, overcast or partially cloudy sky). The root mean square error (RMSE) between the measured and simulated temperatures DT is used as an indicator of the preci- RMSE sion of the model in this sensitivity analysis. It is calculated as:

"# <u>1</u> 2 <u>1</u> X N 2 RMSE m;i s;ið27Þ N

where T is the measured and T the simulated module temperature at time step i. It must be noted that during the winter test period the roof and ground were covered by snow but the PV module was clean of snow. It is also important to mention that the PV module was in open cir- cuit conditions during the simulation periods in order to ensure that no power is generated and all the energy ab- sorbed by the module is either transmitted to the environ- ment through the energy exchange mechanisms described previously, or kept in the module causing a temperature change according to Eq. (1). The starting point of the sensitivity analysis is the state of the art parameter values in the literature. Therefore, the initial values of the studied parameters are either based on previous work of other authors (a), calculated theoretically

Table 2

Initial and optimal parameter values for the thermal simulation model of TUT solar PV power station research plant.

|TUT solar PV power station research plant.|||
|---|---|---|
|Parameter|Reference value|Optimal value|
|a|0.95|0.95|
|C|18,936 J/K|21,000 J/K|
|k|0.7|0.85|
|w|1.00|0.50|
|a|0.00 m² K/W|0.08 m² K/W|

mod d a r

based on the material properties of the PV modules (Cmod) or considered to have minimum initial effect to the perfor- mance of the model (waand ar). The fraction of diffuse radiation kdis a particular case since it has not been used earlier for discerning between clear sky and overcast condi- tions. Yet, its contribution to the performance of the model cannot be omitted. The initial values of the studied param- eters are shown in Table 2. Fig. 3 illustrates the perfor- mance of the thermal model with these reference values for winter and summer test periods with DTRMSEvalues of 1.18 and 3.77 C, respectively.

Fig. 3 clearly shows a better performance of the model

for the winter period than for the summer period, in which the simulated daytime module temperature is lower than the measured temperature. The main contributions to such large error (DTRMSE= 3.77 C) are that the roof tempera- ture is considered to be the ambient temperature, and the direction of the wind has not been taking into account in the convective losses. The effect of these factors and also the impact of the other three parameters a, Cmodand kd on the dynamic thermal model performance are analysed in Sections 3.2.2–3.2.6. The set of best parameter values can be obtained by means of a sensitivity analysis by studying independently the effect of each parameter on the accuracy of the simula- tion model (DTRMSE). The analysis also provides informa- tion about the importance of each parameter to the accuracy of the simulation model. The obtained optimal set of parameter values jointly with the initial set of refer- ence values are presented in Table 2.

Fig. 4 illustrates the performance of the thermal model

using the optimal parameter values of Table 2 for the win- ter and summer periods. The new DTRMSEvalues of the simulation model temperatures are 1.12 C and 1.78 C for the winter and summer periods, respectively. A major improvement has taken place compared to the DTRMSE values of 1.18 C and 3.77 C obtained by the initial parameter values of Table 2. As can be seen in Fig. 4 the agreement between the sim- ulated and measured PV module temperatures is very good during the winter period. Only small deviations take place between the simulated and measured temperatures for short periods of time. Most of the time, the two lines are on top of each other. During summer time the temperature deviations are larger partly to the more volatile environ- ment (climate). However, during the night- and daytime the model seems to be in good agreement with measured

Fig. 3. (a) Measured module temperatures during the three day winter

period and the simulated temperatures using the initial parameter values in

Table 2. (b) Corresponding values for the summer period.

temperatures. The only major deviations take place on eve- nings, when the measured PV module temperatures are sys- tematically higher than the simulated temperatures. Reason for this is that after 18 O’clock the Sun starts to shine to the backside of the PV module heating it up. How- ever, the sensor measuring the incoming solar radiation mounted with the same orientation and tilt as the PV mod- ule does not measure the incoming direct part of solar radi- ation to the backside. This incident radiation is a key input parameter for the simulation model and, therefore, leads to a systematic error in the predicted module temperature during the evenings. The instantaneous error of the predicted module tem- perature during the summer period is shown in the top graph of Fig. 5. The error is stable and small during night-time and more volatile and slightly larger on day- time. During evenings the error is considerably larger all the time in accord with Fig. 4. Actually the bottom graph in Fig. 5 demonstrates this matter even more explicitly. Just around 18 O’clock the solar radiation received by the tilted PV module drops sharply but the solar radiation on a hor- izontal surface decreases more gradually until the sunset after 22 O’clock. This means that the Sun shines to the back of the PV modules during evening time heating them for several hours until sunset. This incidence occurs during

|Fig. 4. (a) Measured module temperatures during the three day winter period and the simulated temperatures using the optimal parameter values|Fig. 5. (a)|Absolute|differences|between|the predicted|and measured||
|---|---|---|---|---|---|---|---|
|in Table 2. (b) Corresponding values for the summer period.|module temperatures during the summer period. (b) Measured incoming solar radiation on the horizontal plane (blue line) and on the tilted PV module interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)|plane (green|dashed|line) during|the summer|period.|(For|

late spring and summer in Finland. It is also important to remark that no self-shading issues are related to the PV module utilised in the simulations included in this article. Thus far the DTRMSEvalues calculated over 24 h of a day have been presented as an indicator of the precision of the model for the winter and summer periods. However, only the daytime from 6 O’clock to 18 O’clock is relevant for the power production point of view for fixed PV gener- ator installations, such as in TUT. Furthermore, comput- ing the evening hours in late spring and summer time does not seem to be a proper solution due to the systematic error in module temperature prediction as previously explained. Completing the thermal model by taking into account this systematic error would be possible, although only the daytime is relevant for power production as previ- ously stated. Therefore, the input parameters have been optimised based on the daytime measurements to give the best PV module temperature prediction. Table 2 includes the DTRMSEvalues calculated for different daily computing hours for the winter and summer periods to demonstrate the effect on model accuracy. Based on Table 2 it is evident that the optimised param- eter values give more accurate PV module temperature pre- dictions than the initial values for the test periods. This is,

of course, a self-evident result for the test period, but the improvements are considerable, especially for the summer period. It is also notable, that the daytime temperature pre- diction for summer period using optimised parameter val- ues is almost as accurate as the prediction for the winter period. Following sections include the sensitivity analysis of the simulation model to provide a more complete understand- ing on different factors affecting to the PV module temper- ature. The sensitivity analysis is carried out by studying the effect of each parameter at a time to the model accuracy. The daytime DT values between the simulated and RMSE measured temperatures are calculated for winter and sum- mer periods by varying the value of the parameter under evaluation. The rest of the parameters are kept at their optimum values. In this way a parameter value was obtained corresponding to the minimum DT. RMSE

3.2.2. Absorptivity of the PV module Absorptivity of the PV module in Eq. (2) determines the amount of energy absorbed by the module of the total

incoming solar energy. It is a function of the orientation and configuration of the module, and absorptive and reflec- tive properties of the PV module materials. In practice, the absorptivity depends also on the Sun position and the level of solar radiation but it is normally simplified as a constant value. Fig. 6 illustrates the effect of the absorptivity on DTRMSEduring the winter and summer test periods.

Fig. 6 indicates that the absorptivity would be slightly

smaller during winter time than during summer time with minimum DTRMSEvalues being at 0.90 and 0.95, respec- tively. Adjustment of the PV module absorptivity to its optimum value for the winter period would improve the simulation accuracy by some 0.3 C on winter time but it would also decrease the accuracy on summer time by some

0.6 C. Therefore, the best overall annual accuracy is obtained with the absorptivity 0.95. One possible explana- tion for the slight differences in trends of DTRMSEfor sum- mer and winter could be the fact that the absorptivity is dependent on the Sun position and level of irradiance. The average Sun position during winter is considerably lower than during summer in Finland. Moreover the aver- age irradiance received by the PV module during daytime for the winter and summer periods is 290.1 and 547.6 W/ m², respectively. According to (Schott, 1985) absorptivity reduces with decreasing incident solar radiation (i.e. at dawn and dusk) in line with our findings.
3.2.3. Heat capacity of the PV module Heat capacity of a PV module characterises the amount of energy needed for increasing the module temperature. A module with low heat capacity will experience higher tem- perature variations with changing climatic conditions than a module with high heat capacity. This property of PV modules is defined by the material properties compounding the module and has a fixed value. However, it was prob- lematic to define heat capacity for the TUT Research Plant PV modules due to lack of precise material properties since
manufacturers do not typically provide this information for commercial reasons. Therefore, it seemed to be in place to check the sensitivity of the module temperature also on this parameter. Fig. 7 shows the effect of heat capacity of the PV module on the accuracy of the predicted module temperature for the winter and summer test periods. PV module temperature does not seem to be very sensi- tive on the heat capacity (Fig. 7) as far as it is of the right order of magnitude. On winter time the simulation models actually seem to be quite insensitive on the correct value of heat capacity, but on summer time substantial underesti- mation of the heat capacity will lead to major errors in cal- culated module temperatures. Reason for this is the higher temperature difference Tmod–Tairdue to higher level of solar radiation in summer than in winter. Fig. 7 indicates that the initial heat capacity was slightly too small. The minimum DTRMSEvalues for the whole year are found between heat capacities of 20 and 22 kJ/K.

3.2.4. Fraction of diffuse radiation Fraction of diffuse radiation kdis an index that measures the amount of diffuse solar radiation from the total incom- ing solar radiation. As explained in Chapter 2, it can be used as a tool to discern between clear sky and overcast conditions to estimate the temperature of the sky. Low val- ues of kdindicate clear sky conditions (Tsky= Tair–20 K), and high values indicate overcast conditions (Tsky= Tair). Somewhere in between there is a value of kd, which can be used to separate between clear sky and overcast condi- tions. Fig. 8 depicts the effect of varying the limit value of kdon the DTRMSEfor the winter and summer periods. In Fig. 8 DTRMSEincreases when kdlimit decreases below 0.4 or increases above 0.9. This is plausible, because at low kdvalues only clear sky conditions occur and, there- fore, the limit should be larger than 0.4. Accordingly, high kdvalues correspond to overcast conditions and the limit
Fig. 6. DTRMSEof the simulated and measured PV module temperatures

as a function of absorptivity of the PV module for the winter and summer periods. The minimum values of DTRMSEare marked with red markers. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Fig. 7. DTRMSEof the simulated and measured PV module temperatures

as a function of heat capacity of the PV module for the winter and summer test periods. The minimum values of DTRMSEare marked with red markers. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

should be below 0.9. The best fit between the simulated and measured temperatures takes place when kdlimit is 0.85. One should also note, that the model accuracy improves considerably (error decreases from 2.7 to 1.3 C on summer time), when the sky temperature is taken into account correctly.

3.2.5. Wind speed adjustment coefficient Wind sensors are typically located to measure the local overall wind speed in the PV facility areas. The impact of the wind speed and direction on the forced convective losses depend on the mounting system of the PV modules (free standing on a rooftop, integrated in the facade of a building, etc.) and the environment, and the use of a wind speed adjustment coefficient washall be considered in Eq. (14). The wind speed and direction are measured by an ultra- sonic wind sensor at the highest point of the TUT solar PV power station research plant (Torres Lobera and Val- kealahti, 2012). The PV modules are mounted with tilted angle of 45 on mounting racks that cover the back plates of the modules, shielding them from winds blowing from north. Therefore, the wind speed adjustment coefficient is used to approximate the wind speed reduction caused by the mounting racks and Eq. (14) turns into: <u>L</u> Re ¼ vwwa: ð28Þ qm In this study we apply only a simple basic adjustment for the wind speed. The wind speed adjustment coefficient wais set to be 1 for winds blowing towards north, north-east, north-west, east and west directions and a value between 0 and 1 has been seek for winds blowing towards south, south-east and south-west directions providing the smallest DTRMSEfor the simulated temperature. The effect of the
wind speed adjustment coefficient on the error between the predicted and measured module temperatures for the winter and summer periods is illustrated Fig. 9. During the winter period temperature of the PV module does not depend strongly on the speed of wind from north and values of wafrom 0.4 to 1 provide almost the same DTRMSEvalues. This is plausible, because temperature rise of the PV module due to incident solar radiation is small on winter time with respect to ambient air temperature. How- ever, the PV module temperature is quite sensitive on the adjustment coefficient value during summer time and best simulation accuracy is obtained with wa= 0.5. This indi- cates that the installation on the roof and the used mount- ing racks that cover the back plates of the PV modules reduce forced convective losses on the backside considerably.

3.2.6. Roof absorptivity coefficient The roof temperature Troofplays an important role in the long-wave radiative losses of the PV module in the same way as the sky temperature. During cloudy days the increase of the roof temperature with respect to the ambient temperature is not that great due to the low levels of solar radiation and Troofcan be approximated to be equal to Tairwith good accuracy. This approximation would be also acceptable for buildings designed with green roofs, which do not absorb as much solar energy as black- surfaced rooftops. Therefore, for open field PV power plant installations ambient air temperature T can serve
air as a reasonable approximation for ground temperature. Generally speaking, the roof temperature is complicated to approximate accurately since it would require the same type of energy balance analysis as the temperature of the PV modules. However, such accuracy is not required for the present work and a simpler approach has been taken.

|Fig. 8. DT|of the simulated and measured PV module temperatures|as a function of w|for the winter and summer periods for winds blowing||||
|---|---|---|---|---|---|---|
|as a function of k|limit for clear sky and overcast conditions for the|towards|south, south-east|and south-west.|The minimum|values of|
|winter and summer test periods. The minimum DT with red markers. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)||DT references to colour in this figure legend, the reader is referred to the web version of this article.)|are marked|with red markers.|(For interpretation|of the|

Fig. 8. DTRMSEof the simulated and measured PV module temperatures

d RMSEvalues are marked

Fig. 9. DTRMSEof the simulated and measured PV module temperatures

as a function of wafor the winter and summer periods for winds blowing

RMSE

Fig. 10. DTRMSEof the simulated and measured PV module temperatures

as a function of roof absorptivity coefficient for the summer period. The minimum DTRMSEvalue is marked with a red marker. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The temperature of the roof in steady-state can be approx- imated by the expression:

### Troof¼ Tairþ arGh; ð29Þ

where aris the roof absorptivity coefficient and Ghis the horizontal incoming total solar radiation. The effect of ar on the error of the predicted module temperature is de- picted in Fig. 10. During winter time and part of spring, the ground andFig. 11. (a) Measured and simulated module temperatures for the spring

|period|using the|optimal|of Table|2. (b) Absolute|
|---|---|---|---|---|
|differences between the predicted and measured module temperatures.|||||

roofs of buildings in the Nordic countries are covered by period using the optimal parameter values of Table 2. (b) Absolute snow. The existence of snowpack keeps the snow tempera- ture lower than the roof temperature would be otherwise concerning the solar radiation level. The snow reflects most values. Therefore, it is essential to test the performance of the sunlight and all absorbed energy serves to melt the of the model with different measurement data. For that snow instead of increasing its temperature over 0 C. reason, simulations have been performed for a new three Therefore, the roof temperature is considered to be 0 C day period from May 20th to 23rd 2012 (spring period) in the simulations during the existence of snow and the roof and for a case of 91 consecutive days during summer absorptivity coefficient has no effect on the predicted Tmod. 2012 to confirm the accuracy of the optimised thermal During the summer period the roof absorptivity affects model (Table 2). The selected three day period includes the long wavelength heat transfer between the PV module datasets corresponding to non-homogenous climatic con- and the roof surface as shown in Fig. 10. However, the ditions in terms of sky conditions, irradiance, wind speed module temperature does not depend strongly on the roof and direction, etc. It also serves as an easy way for com- absorptivity, i.e., the shape of the curve around the mini- paring with earlier simulations (Figs. 3 and 4). On top of mum in Fig. 10 is quite flat. The best simulation accuracy 2that, the analysis of the whole measurement data of sum- was obtained with ar= 0.08 m K/W, which corresponds mer 2012 serves as the final proof for the model to a roof temperature rice of the order of 60–70 C for sum- performance. mer day radiation levels (Fig. 5). However, the temperature The top graph in Fig. 11 illustrates the performance of prediction improves only less than 1 C in summer time by the optimised thermal model for the spring period obtain- including the warming up of the roof (by increasing arfrom 2ing an all day DTRMSEof the simulated temperature of 0 to 0.08 m K/W).

1.39 C. This error is well in line with the errors of the opti- mised thermal model for the winter and summer periods
# 4. Results presented in Section 3.2 (Table 2). The instantaneous error

between the predicted and measured module temperatures It was actually self-evident that the optimised thermal is depicted at the bottom of Fig. 11. model used for fitting the input parameter provides bet-The major deviations between the simulated and mea- ter results for the test periods than the initial theoretical sured PV module temperatures take place again on

Table 3

The error of simulated all day and daytime module temperatures for the winter and summer test periods using the initial and optimised input

|winter|and summer|periods using|the initial|and optimised|
|---|---|---|---|---|
|parameter values.|||||
|Period|Computing hours (h)|DT ( C)||DT ( C)|
|Winter|0–24|1.18||1.12|
|Winter|6–18|1.63||1.53|
|Summer|0–24|3.77||1.78|
|Summer|6–18|4.76||1.27|

RMSE,Initial RMSE,Optimum

Fig. 12. Daily daytime DTRMSEof the predicted module temperature is

presented for 91 days during summer 2012.

Table 4

DTRMSEand the fraction of time when the error of predicted PV module temperature DT is within certain limits for the spring test period. Computing DTRMSEDT <2 C 2 C<DT <3 C DT >3 C

|Computing|DT|DT <2 C|2 C<DT <3 C|DT >3 C|
|---|---|---|---|---|
|hours (h)|( C)|(%)|(%)|(%)|
|0–24|1.39|87.4|8.4|4.2|
|6–18|1.28|88.8|9.7|1.5|

Table 5

DTRMSEand fraction of time when the error of predicted PV module <u>temperature DT is within certain limits for 91 days during summer 2012.</u>

|RMSE|Computing|DT|DT <2 C|2 C<DT <3 C|DT >3 C|
|---|---|---|---|---|---|
||hours (h)|( C)|(%)|(%)|(%)|
||0–24|1.61|82.0|12.5|5.5|
||6–18|1.63|80.0|14.4|5.6|

Computing DTRMSEDT <2 C 2 C<DT <3 C DT >3 C

evenings. Reason for this is the systematic error in predic- tion of PV module evening temperature as explained already in Section 3.2. This is also a major reason for the bigger all day DTRMSEof the simulated temperatures for summer than for spring and for spring than for winter. The daytime performance of the optimised thermal model for the spring period is better than the all day performance, as expected, yielding a DTRMSEof 1.28 C, which go together with the summer accuracy. It seems to be evident, that the thermal model performs well around the year.

Table 3 includes the calculated DTRMSEfor different

computing times for the spring period as well as the frac- tion of time when the model accuracy (DT) is lower than 2 C, between 2 and 3 C and larger than 3 C. To ensure the accuracy and performance of the dynamic thermal model a set of climatic data corresponding to 91 consecutive days from May 23rd to August 23rd 2012 with a sampling frequency of 1 Hz is used as an input for the thermal model. Fig. 12 shows the daily daytime DTRMSE for the summer 2012. During 77 days out of 91 the daily DTRMSEis below 2 C. This is well in line with the results for the spring period in Table 3. The all day and daytime DTRMSEof the simulated temperatures for the summer per- iod are 1.61 and 1.63 C, respectively, as shown in Table 4. These values are in line with the values for the test period presented in Tables 2 and 3. 80% of the time the simulated PV module temperature differs less than 2 C from the measured temperature and only a small fraction of time the difference is larger than 3 C. The lack of valid winter time data during long periods, when the modules are covered by snow, impedes evaluation of the performance of the model for several consecutive weeks during winter. However, the thermal model is expected to present similar accuracy in winter than in sum- mer or spring. The developed dynamic thermal simulation model of the PV module temperature seems to perform very well. One must also note that the real measurement accuracy in out- door condition is somewhere below 1 C, so that the achieved accuracy is also the practical achievable accuracy. On top of that, this dynamic thermal model will be used to simulate the TUT PV power plant electric power produc- tion capacity. An error of 2 C in module temperature pre- diction will lead to an error of less than 1 W in the available power. This accuracy is clearly enough for the foreseen research purposes see Table 5.

# 5. Conclusions

Temperature of the PV module has a major impact on the voltage and, accordingly, on the produced electric power of the module. In addition, increase in temperature is related to several failure or degradation modes of PV modules. Accurate prediction of PV module temperature is thus important to understand performance, reliability and lifetime of PV modules. The thermal response of PV modules to changes in cli- matic conditions such as irradiance and wind speed can be really fast. Major changes in irradiance take place dur- ing cloudy days and a dynamic model is required to esti- mate the module temperature properly. This is actually crucial to be able to study the operation of PV power sta- tions under varying climatic conditions rigorously, which has not been done until now.

A dynamic state of the art thermal model of PV modules is proposed in this paper, which considers the thermal mass of the module besides of all relevant climatic and site-spe- cific conditions and heat transfer mechanisms. The thermal model is based on the non-steady state equation obtained by considering the total energy balance in the PV module. The main mechanisms of energy exchange between the PV module and its environment are modelled according to their first principle considerations, resulting in a time vary- ing differential equation of the module temperature. The dynamic model has been adapted and further devel- oped from the previous work of other authors. For exam- ple a relatively straightforward and simple way has been developed to estimate the temperature of the sky by using diffuse fraction of solar radiation to discern between clear sky and overcast conditions. Another novelty of this work is the use of 1-s climatic and environmental measurements of the TUT PV power station research plant. In addition, we provide a simple practical approach to further improve the accuracy of the model with respect to site-specific envi- ronmental factors in the form of sensitivity analysis. Three day measurement periods on winter, spring and summer time were used to develop and verify the dynamic thermal model. The simulated daytime PV module temperature accuracies with respect to measured module temperatures were 1.53, 1.28 and 1.27 C, respectively. Finally, the accu- racy of the simulation model was tested with the measured data for 91 consecutive days during summer 2012. The dynamic thermal model predicted the daytime module tem- peratures with an average accuracy of 1.63 C and the dif- ference between simulated and measured temperatures was less than 2 C for 80% of the time. The introduced dynamic thermal model is first of the kind without major compro- mises and, therefore, provides accurate estimates for PV module temperatures on a 1-s time scale.

# References

Armstrong, S., Hurley, W.G., 2010. A thermal model for photovoltaic panels under varying atmospheric conditions. Appl. Therm. Eng. 30, 1488–1495. Balog, R. S., Kuai, Y., Uhrhan, G., 2009. A photovoltaic module thermal model using observed insolation and meteorological data to support a long life, highly reliable module-integrated inverter design by predict- ing expected operating temperature. In: IEEE Energy Conversion Congress and Exposition (ECCE). Caluianu, I.R., Ba˘ lta˘re u, F., 2012. Thermal modelling of a photovoltaic module under variable free convection conditions. Appl. Therm. Eng. 33–34, 86–91. Chenni, R., Makhlouf, M., Kerbache, T., Bouzid, A., 2007. A detailed modelling method for photovoltaic cells. Energy 32, 1724–1730. Durisch, W., Bitnar, B., Mayor, J.-C., Kiess, H., Lam, K.-H., Close, J.,

2007. Efficiency model for photovoltaic modules and demonstration of its application to energy yield estimation. Sol. Energy Mater. Sol. Cells 91, 79–84.
Franghiadakis, Y., Tzanetakis, P., 2006. Explicit empirical relation for the monthly average cell-temperature performance ratio of photovoltaic arrays. Prog. Photovoltaics Res. Appl. 14, 541–551.

Hegazy, A.A., 2000. Comparative study of the performances of four photovoltaic/thermal solar air collectors. Energy Convers. Manage. 41, 861–881. Holman, J.P., 1992. Heat Transfer. McGraw-Hill. Incropera, F.P., 2007. Fundamentals of Heat and Mass Transfer. John Wiley. Jones, A.D., Underwood, C.P., 2001. A thermal model for photovoltaic systems. Sol. Energy 70, 349–359. Krauter, S.C.W., 2004. Development of an integrated solar home system. Sol. Energy Mater. Sol. Cells 82, 119–130. Kudish, A.I., Evseev, E.G., Walter, G., Leukefeld, T., 2002. Simulation study of a solar collector with a selectively coated polymeric double walled absorber plate. Energy Convers. Manage. 43, 651–671. Malik, A.Q., Damit, S.J.B.H., 2003. Outdoor testing of single crystal silicon solar cells. Renew. Energy 28, 1433–1445. Mattiei, M., Notton, G., Cristofari, C., Muselli, M., Poggi, P., 2006. Calculation of the polycrystalline PV module temperature using a simple method of energy balance. Renew. Energy 31, 553–567. Nagae, S., Toda, M., Minemoto, T., Takakura, H., Hamakawa, Y., 2006. Evaluation of the impact of solar spectrum and temperature variations on output power of silicon-based photovoltaic modules. Sol. Energy Mater. Sol. Cells 90, 3568–3575. Nordmann T., Clavadetscher L., 2003. Understanding temperature effects on PV system performance. In: Proceedings of the third world conference on photovoltaic energy conversion. Osaka, Japan, pp. 2243–2246. Notton, G., Cristofari, C., Mattiei, M., Poggi, P., 2005. Modelling of a double-glass photovoltaic module using finite differences. Appl. Therm. Eng. 25, 2854–2877. Ransome, S., Funtan, P., 2005. Why hourly averaged measurement data is insufficient to model PV system performance accurately. In: 20th European Photovoltaic Solar Energy Conference. pp. 2752–2755. Schott, T., 1985. Operation temperatures of PV modules. In: Proceedings of the 6th EC Photovoltaic Solar Energy Conference. London, UK, pp. 392–396. Servant, J.M., 1985. Calculation of the cell temperature for photovoltaic modules from climatic data, In: Proceedings of the 9th Biennial Congress of ISES – Intersol 85. Montreal, Canada, p. 370. Skoplaki, E., Palyvos, J.A., 2009. Operating temperature of photovoltaic modules: a survey of pertinent correlations. Renew. Energy 34, 23–29. Skoplaki, E., Boudouvis, A.G., Palyvos, J.A., 2008. A simple correlation for the operating temperature of photovoltaic modules of arbitrary mounting. Sol. Energy Mater. Sol. Cells 92, 1393–1402. Sparrow, E.M., Tien, K.K., 1977. Forced convection heat transfer at an inclined and yawed square plate-application to solar collectors. Heat Transfer 99, 507–513. Swinbank, W.C., 1963. Long wave radiation from clear skies. Quarterly J. Royal Meteorol. Soc. 89, 339. Topic, M., Brecl, K., Sites, J., 2007. Effective efficiency of PV modules under field conditions. Prog. Photovoltaics Res. Appl. 15, 19–26. Torres Lobera, D., Valkealahti, S., 2012. Operation of TUT solar photovoltaic power station research plant equipped with climatic and electric measuring systems. In: 27th European Photovoltaic Solar Energy Conference. pp. 3905–3910. Tsai, H.-F., Tsai, H.-L., 2012. Implementation and verification of integrated thermal and electrical models for commercial PV modules. Sol. Energy 86, 654–665. Weast, R.C., 1984. CRC Handbook of Chemistry and Physics. In: 64th ed. CRC Press. World Meteorological Organization (WMO). 2008. Guide to Meteoro- logical Instruments and Methods of Observation. WMO-No. 8. Wong, L.T., Chow, W.K., 2001. Solar radiation model. Appl. Energy 69, 191–224.
