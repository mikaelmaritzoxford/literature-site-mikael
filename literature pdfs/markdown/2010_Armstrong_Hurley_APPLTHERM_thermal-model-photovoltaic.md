Applied Thermal Engineering 30 (2010) 1488e1495

Contents lists available at ScienceDirect

# Applied Thermal Engineering

journal homepage: www.elsevier.com/locate/apthermeng

## A thermal model for photovoltaic panels under varying atmospheric conditions

#### S. Armstrong*, W.G. Hurley

Power Electronics Research Centre, Electrical and Electronic Engineering, National University of Ireland, Galway, Ireland

##### article info abstract

Article history: The response of the photovoltaic (PV) panel temperature is dynamic with respect to the changes in the Received 1 June 2009 incoming solar radiation. During periods of rapidly changing conditions, a steady state model of the Accepted 5 March 2010 operating temperature cannot be justified because the response time of the PV panel temperature Available online 12 March 2010 becomes significant due to its large thermal mass. Therefore, it is of interest to determine the thermal response time of the PV panel. Previous attempts to determine the thermal response time have used Keywords: indoor measurements, controlling the wind flow over the surface of the panel with fans or conducting Photovoltaic the experiments in darkness to avoid radiative heat loss effects. In real operating conditions, the effective External convective losses PV panel temperature is subjected to randomly varying ambient temperature and fluctuating wind Temperature evolution speeds and directions; parameters that are not replicated in controlled, indoor experiments. A new thermal model is proposed that incorporates atmospheric conditions; effects of PV panel material composition and mounting structure. Experimental results are presented which verify the thermal behaviour of a photovoltaic panel for low to strong winds. 2010 Elsevier Ltd. All rights reserved.

1. Introduction The PV panel operating temperature is dependent upon many factors; solar radiation, ambient temperature, wind speed and direction, panel material composition, and mounting structure. For a typical commercial PV panel, a proportion of the solar radiation is converted into electricity, typically 13e20%, and the remainder is converted into heat [1]. In addition, the PV panel also generates its own heat due to the photovoltaic action and further heating occurs due to the energy radiated at the infrared wavelength of the solar spectrum. The effects of the PV panel operating temperature on the output efficiency have been well documented [2,3], with increasing temperature decreasing the amount of power available. When evaluating the efficiency of a PV system, the temperature variations are often regarded as instantaneous or use hourly steady state models. However, the changes in temperature due to varying solar radiation levels do not occur immediately. The PV panel heats up and cools down gradually from step changes in solar radiation and the temperature lags the solar radiation changes, following an exponential response. If the power output from the PV panel is modelled in short time periods, for example, on a minute by minute basis, the temperature response becomes considerably more important compared to the time period of interest. The proposed
thermal model may be used to determine the speed of response of the PV panel to changing input conditions. The behaviour of the PV panel as a thermal mass has been described in the literature [4e7].In[4,5], the panel is modelled as a lumped thermal heat capacity model to predict the operating temperature using a thermal energy balance equation. The time constant, s, of the PV panel, by analogy with RC circuits, is defined as the time taken for the panel temperature to reach 63% of the total change in temperature in response to a step change in the solar radiation In [5], the authors predicted a time constant of approxi- mately 7 min for the BP Solar BP585 85 W panel by observing the temperature changes. The panel took 15 min to reach equilibrium. The temperature response for the BP585 panel was observed to be approximately 15 min in Ref. [6]. Similar observations were reported for panels of a similar wattage in Ref. [7], noting also that larger PV panels or panels with increased back insulation took almost twice as much time to reach a quasi-steady temperature. These observations highlight the importance of careful consider- ation of the PV composition and mounting arrangements. No attempts were made in these works to theoretically quantify the response time. Some experimental work to determine the thermal response time was described in the literature. In Ref. [8], a Kyocera 125 W PV panel was subjected to a step change of solar radiation of 800 W/m². A barrier was placed around the panel to avoid wind effects. This is not indicative of real operating conditions because wind flow is one of the most pertinent parameters in determining

* Corresponding author. E-mail address: sara.n.armstrong@gmail.com (S. Armstrong).
1359-4311/$ e see front matter 2010 Elsevier Ltd. All rights reserved. doi:10.1016/j.applthermaleng.2010.03.012

S. Armstrong, W.G. Hurley / Applied Thermal Engineering 30 (2010) 1488e1495
Nomenclature

|w|wind speed (m/s)|
|---|---|
|Greek symbols:||
|b|volumetric thermal expansion coefficient|
|r|density of the material (kg/m³)|
|3|emissivity (dimensionless)|
|s|boltzmann constant (W/m K)|
|n|kinematic viscosity (m²/s)|
|q|angle of inclination from the vertical ( )|
|m Subscripts:|dynamic viscosity (kg/m s)|
|air|air|
|amb|ambient temperature|
|cell|photovoltaic cells|
|conv|convective|
|cr|critical|
|film|film|
|rad|radiative|
|s|surface|

DT temperature difference ( K) A surface area (m²) c specific heat capacity (J/ K) F view factor (dimensionless) g acceleration due to earth’s gravity (m/s) h heat transfer coefficient (W/m² K) Gr Grashof number (dimensionless) k thermal conductivity (W/m K) L length (m) Nu Nusselt number (dimensionless) Pr Prandtl number (dimensionless) q heat loss (W) Ra Rayleigh number (dimensionless) Re Reynolds number (dimensionless) S measured solar radiation falling on the tilted PV panel (W/m²) T temperature ( C) t thickness of material (m)

the operating temperature. A time constant of approximately

10.5 min was estimated from their measurements. Indoor measurements were carried out in Ref. [9]. The PV panel was heated to a stable temperature and airflow from a blower fan with four speed levels to represent different wind speeds was allowed to flow over the front and back surfaces of the panel. These indoor measurements showed various time constants of approximately

|(W/m K); A|PV panel surface area (m²)|
|---|---|
|Thermal capacitance refers to the ability of a material to absorb||
|and store heat. C|,isdefined as:|
|C ¼ rcA|t|
 5e10 min for an unspecified PV panel size. There are several shortcomings with this test procedure. The temperature response of the panel was observed under darkness to avoid radiative heat loss and steps were taken to omit free (or natural) convective heat loss. However, on days with little or no wind, these heat transfer processes become significant. Additionally, using a fan produces a parallel flow of wind over the surface of the panel. True winds vary frequently and even seemingly steady wind flows can oscillate 15% around its mean wind speed [10]. The proposed thermal model provides a means of predicting the thermal time constant of a PV panel under varying atmospheric conditions. This is achieved by considering the thermal properties of PV panels in terms of their electrical equivalents by means of an RC circuit and investigating the heat transfer from the surface of a PV panel under varying wind conditions. This model incorporates factors previously overlooked in the literature, such as free and radiative heat loss, varying atmospheric conditions, and the effect of the PV panel tilt angle and mounting structure on the heat loss mechanisms. The description of the thermal model is divided into the following sections; firstly, modelling the temperature response of the PV panel as an RC circuit is introduced, which involves inves- tigating the material composition of the PV panel. Secondly, the convective heat transfer losses (wind induced and free) and radi- ative heat losses are analysed. Finally, the observed time constant of the PV panel is compared with the predicted values under varying wind conditions.
2. RC circuit model The thermal mechanisms of a PV panel can be considered in terms of their electrical equivalents by correlating the electrical resistance and capacitance to the thermal resistance, RTH, and thermal capacitance, CTH. These parameters are used to define the conductive heat transfer in the PV layers. Thermal resistance is
defined as the index of a material’s resistance to heat flow and is given as:

<u>t</u> RTH¼ (1) kAs

t Thickness of material (m); k Thermal conductivity of the material s

TH

TH s(2)

r Density of the material (kg/m³); c Specific heat capacity (J/ K) The thermal resistance network is shown in Fig. 1, where the convective and radiative heat loss processes act in parallel to the conductive heat transfer in the PV layers [4]. In order to determine the thermal resistance and thermal capacitance of the PV panel, each individual layer of the panel has to be examined in turn; these layers are described in the next section.

3. PV panel composition The PV panel is composed of a variety of different layers depending on the photovoltaic technology used. The PV panel under investigation in this work is the polycrystalline BP Solar BP350U. There are six main layers in this PV panel; the glass covering, an anti-reflective coating (ARC), PV cells, ethylene vinyl acetate (EVA) layer, metal back sheet and a tedlar PVF layer. These layers are embedded in a metal frame, the effects of which are not included, since its low surface area with respect to the panel area has a negligible effect on the temperature response [5]. The various layers are briefly reviewed below. Glass Covering: The glass cover of the PV panel is made of tempered glass, which had been through a process of rapid heating and cooling to enhance its strength. PV glass differs from conventional glass. Glass used for buildings, for example, has low transmittance to keep heat and glare out of the building. However, the glass used in PV panels is ultra-clear, with a high transmittance rate and low iron content to extract as much solar energy as possible. Anti-Reflective Coating (ARC): Silicon can reflect up to 35% of the incoming radiation. To counteract this, an ARC is applied

Photovoltaic panel layers

RthEVARthbacksheet RthTedlar RthglassRthARCRthcell Back surface Front surface

tnorf kcab ht ht Cthglass PDCthARC Cthcell CthEVACthbacksheet CthTedlar R R

Photovoltaic thermal resistance network.

T amb

Fig. 1.

(silicon nitride), typically only nanometers thick, which chan- nels the incoming photons into the lower layers of the cells. Photovoltaic (PV) cells: Polycrystalline silicon wafers are used in the BP350U panel. A wafer thickness of 225 mm is used in this PV panel [11]. EVA Layer: The PV cells are encapsulated in a layer of ethylene vinyl acetate (EVA) to affix the PV cells to the cover glass and the back encapsulating material and to provide moisture resistance and electrical isolation. Rear Metal Contact: Full metal contact is made on the reverse side of the PV cells by screen-printing a metal paste, typically aluminium, onto the back surface. Tedlar Polymer Layer: The polymer layer in the BP350U is made of polyvinyl fluoride (PVF). This layer is photostable and provides additional insulation and moisture protection for the PV layers.

The thickness (t), thermal conductivity (k), density (r), and heat capacity (c) of each PV layer is shown in Table 1. Using equations (1) and (2), and the parameters given in Table 1, the thermal resistance and thermal capacitance of each layer may be found. The properties of the PV panel materials are assumed to be independent of temperature. The prevailing wind conditions and varying ambient temperatures also have a significant effect on the PV panel thermal response time; therefore, the methods to determine these heat transfer processes are reviewed next.

4. Convective heat transfer from the PV panel surface Once the conductive thermal resistance and thermal capaci- tance of each layer of the PV panel has been derived the convective heat transfer at the surface of the PV panel, Rconvmust also be considered in order to determine the overall thermal response time of the PV panel. The convective heat loss is calculated as: <u>1</u> Rconv¼ (3) hAs h Overall convective heat transfer coefficient (W/m² K) Two heat transfer coefficients need to be established; a forced convection heat transfer coefficient due to the wind flow flowing over the surface of the PV panel, hforced, and a free convective heat
Table 1
 Photovoltaic layer properties.
transfer coefficient, hfree. These coefficients are described in the following sections.

4.1. Forced convection heat transfer coefficient Forced convection plays a major role in determining the thermal response of the PV panel and a diverse range of values for the hforced coefficient is available [18]. These equations were developed from fundamental heat transfer theory [19], wind tunnel measurements [20e23], and field measurements [24e26]. Table 2 shows a summary of these different approaches. Equations (4)e(10) are based on measurements in wind tunnels and (11e15) were derived from field measurements. In these tests, a heated plate was placed outdoors and the forced convective heat transfer coefficient, hforced, was correlated against the prevailing wind speed. The effect of wind direction was included in Refs. [25,26]. The resultant hforcedcoefficients from indoor wind tunnel tests and outdoor field measurements for a range of wind speeds are shown in Fig. 2(a) and (b) respectively. From Fig. 2(a), it can be seen that the well known Nusselt relations predict the smallest value of h forcedcoefficient. It has been argued that under real operating conditions, the fundamental heat transfer formulae have little application to PV panels for many reasons. Firstly, the upper surface temperature of the PV panel will vary with time and may not be isothermal due to the small scale wind fluctuations over the surface. Secondly, naturally occurring wind contains free stream turbulence resulting from the edges of fences, trees and roofs which increases the rate of heat transfer from the PV surface; these factors are not indicated in the general heat transfer formulae. The results of the field measurements highlight several weak- nesses in the early wind tunnel experiments. Field measurements indicated that the measured heat transfer coefficient could be as much as 30% greater than that predicted using the general wind tunnel formulae [25]. Also, the PV panel is generally not placed vertically; it is tilted at an angle to optimize the output power. This causes the edge of the PV panel to act as an obstacle to the incoming wind, which gives rise to flow phenomena such as separation and reattachment. This causes the speed of the wind to drop almost to zero after coming into contact with the edge of the panel. The flow became turbulent after reattachment [26,27]. This results in a higher heat transfer than is generally reported in the literature.

|Layer|Thickness t, (m)||Thermal conductivity k,(W/m K)|Density r, (kg/m|Specific heat Capacity c, (J/kg C)|
|---|---|---|---|---|---|
|1. Glass|0.003 [11]||1.8 [4]|3000 [5]|500 [5]|
|2. ARC|100 10|[13]|32 [14]|2400 [14]|691 [14]|
|3. PV Cells|225 10|[11]|148 [12]|2330 [5]|677 [5]|
|4. EVA|500 10|[9,12]|0.35 [12]|960 [17]|2090 [17]|
|5. Rear contact|10 10|[15]|237 [16]|2700 [16]|900 [16]|
|6. Tedlar|0.0001 [12]||0.2 [12]|1200 [5]|1250 [5]|

<u>Layer Thickness t, (m) Thermal conductivity k,(W/m K) Density r, (kg/m</u>3<u>) Specific heat Capacity c, (J/kg C)</u>

Table 2

Forced convection equations.

<u>Author Equation</u> Comment

|Author|Equation||Comment|
|---|---|---|---|
|Indoor wind tunnel tests||||
|1. Nusselt Relation [19]|Nu ¼ 0:664Re|Pr (4)|Laminar wind flow|
||Nu ¼ 0:037Re|Pr (5)|Turbulent wind flow|
|2. MacAdams [20]|h ¼ 3:8w þ 5:7|(6)|May contain free convective a and radiative effects|
|3. Watmuff [21]|h ¼ 3:0w þ 2:8|(7)||
|4. Lunde [22]|h ¼ 2:9w þ 4:5|(8)||
|5. Sparrow [23]|Nu ¼ 0:86Re h ¼ 4:96w|Pr (9) L (10)|Scaled models in wind tunnel|
|Outdoor tests||||
|6. Test [24]|h ¼ 2:56w þ 8:55|(11)|Wind measured at a height of 1 m above the plate|
|7. Sturrock [25]|h ¼ 5:7w h ¼ 5:7w þ 11:4|(12) (13)|Leeward Windward|
|8. Sharples [26]|h ¼ 2:2w þ 8:3 h ¼ 3:3w þ 6:5|(14) (15)|Leeward Windward Flat plate on scaffolding tilted at 35|

1=2 1=3 4=5 1=3

1=2 1=3 0:5 0:5

This phenomenon is documented in Ref. [28] where it was reported The thermal properties of air vary with temperature. These that the presence of a step change in wind flow due to an inclined variations are taken into account because they can have a signifi- plate resulted in a twofold enhancement of the heat transfer from cant effect on the surface coefficients [25]. the inclined plate. Equation (16) was derived for vertical plates but may be easily It was recommended in Ref. [18] that the selection of a suitable adapted for plates inclined at angles up to 60 by replacing g with g hforcedcoefficient involves examining the specific test conditions cosq, where q is the angle of inclination from the vertical [30]. that lead to the available formulae and choosing the test proce- dure that most closely matches the current experimental setup. **a**70 For this reason, the Test approach [24], given by (11) and the Nusselt Relation Sharples method [26], described by (14) and (15) were chosen for McAdams 60 closer investigation in this work. It can be seen in Fig. 2(b), that Watmuff the predicted hforcedcoefficients for the two models are compa-)K Lunde rable. Sharples credits the agreement of his experimentally ° 50 Sparrow 2 derived equation with Test’s work due to the similar dimensions m/W(tneiciffeoc of plates used. The experimental setup for the work described in40 this paper is similar to that used by Test and Sharples. The PV panel is placed on a scaffolding structure at a tilt angle of 35. This 30 is important because a ventilated array shows more pronounced heat transfer. The top layer of Sharples’s experimental setup had decrof a laboratory measured emittance value of 0.9; the emittance of PV20 h glass has a similar value of 0.91. Additionally, the wind measure- ments were taken at 1 m over the roof in Ref. [24] and 1.5 m in 10 Ref. [26], the PV panel under study was placed at approximately 1 m above the structure. Equation (11) derived by Test was chosen 0 for this model, given the lack of short term wind direction1 2 3 4 5 6 7 8 9 10 Wind speed (m/s) measurements. **b**70 Sturrock (WW)

4.2. Free convective heat lossSturrock (LW)
60 Sharples (LW) Sharples (WW) Convective heat loss from the front and rear surfaces of the PV)K Test panel is also taken into account. On days with little or no wind, the °50 2 free convective heat loss becomes more significant. This is espe-m/W( tneiciffeoc cially true in cold climates where the temperature differences40 between the surface and the ambient air may be relatively large [29]. Free convection from the bottom of a heated inclined plate for 30 the entire range of Rayleigh number, is given as a function of the Nusselt number, Nu, [19]:decrof 20 2 32h 1=6 <u>0:387Ra</u> Nu ¼ 40:825 þ h i 5 (16) 10 8=27 9=16 1 þð0:492=PrÞ

Wind speed (m/s) Ra Rayleigh number, (Ra ¼ Gr Pr)(Ra, Gr and Pr are defined in the Appendix); Gr Grashof number; Pr Prandtl number; kairThermalFig. 2. (a) Hforcedcoefficients derived from indoor measurements. (b) Hforcedcoeffi- conductivity of air cients derived from field measurements.

Start

**Input** Ambient and PV surface temperature Thermal properties of air Wind speed Time

Thermal resistance and capacitance of each PV layer

Film temperature, Tfilm and thermal properties of air using Tfilm

Free convection from front and Radiative heat loss Forced convection rear surface of PV panel

Total heat loss co-efficient

PV panel time constant

Fig. 3. Flowchart for the thermal model methodology.

Fig. 4. (a) Outdoor experimental setup. (b) Indoor experimental setup.

**Wind speed: 0.77 m/s Wind speed: 5.76 m/s**

|Solar Radiation Step change in solar radiation Temperature Initial temp: 38.68° Time Constant: 63%: 24.15° Final temp: 15.62°|1000 40 800 35 noitaidaRraloS 600 30 erutare meTp 400 25 200 20 0|Solar Radiation Step change in solar radiation Temperature Initial temp: 29.66° Time Constant: 63%: 23.33° Final temp: 19.61°|
|---|---|---|
|0 00 55 10 10 15 15 20 20 25 25 30 30 35 35 Time (minutes) Fig. 5. Temperature response of the PV panel with wind speed of 0.77 m/s. The magnitude of the convective heat exchange is proportional to the temperature difference between the PV panel surface and the, may be higher surrounding air. The front surface temperature, T cell. The difference the back surface temperature, T back temperature depends on the PV panel composition and the solar radiation levels. An equation given by Ref. [31] is used to predict the front surface temperatures using the measured back temperatures S DT ¼ T þ back 1000 Measured solar radiation falling on the tilted PV panel; Temperature difference between the front surface and the back. This value is given as 3 surface at solar radiation of 1000 W/m² open rack PV panel with a glass/PV cell/polymer composition. Values for alternative PV structures are given in [31]. The free convection from the top of the PV panel is given as: [32] i h 1=4 1=3 1=3 þ 0:56ðGr Nu ¼ 0:14 ðGrPrÞ ðGr PrÞ PrcosqÞ cr cr Wind speed: 2.14 m/s|15 00 5 for 10 Nusselt equal to 15 in 9 2 h ¼ front (17) DT C Gr/Re² sheet Gr/Re² Re² 5. (18) 40|55 10 10 15 15 20 20 25 25 Time (minutes) Fig. 7. Temperature response of the PV panel with wind speed of 5.76 m/s. 11 o o < GrPr cos q < 10 and 15 < q < 75 The critical Grashof number, Gr, is the value at which cr number starts deviating from laminar behaviour. ,30,60 and 70, the Gr number is given as 5 cr 8 6 respectively in Ref. [32]. 10 ,10, and 10 The effective convection heat transfer coefficient from the front surface of the PV panel is derived from the combination of the free and forced convection as given in (19) [33]. qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 3 h³ þ h³ forced free The significance of the free convective component of the heat loss from the PV panel may be determined by the ratio of Gr/Re² where Re is the Reynold’s number (defined in the Appendix). If << 1, the heat loss is dominated by forced convection, >> 1 means free convection is prevailing and a value of Gr/ w1 implies both forced and free convection are significant [19]. Radiative heat transfer from the PV panel surface The radiative heat loss from the front and rear surface of the photovoltaic panel to the sky and the ground is also taken into account when determining the overall thermal response time. The|
|Solar Radiation Temperature Initial temp: 37.72° Step change in solar radiation|q ¼ rad 35 Table 3 30 erutare pmeT|, to the ground is given as [34]: radiative heat loss, q rad 3FsA T⁴ T⁴ s rear =front ground Thermal model experimental results. Thermal model parameters Wind speed (m/s) (a) 0.77 (b) 2.14 (c) 5.76|
|Time Constant: 63%:23.02° Final temp: 15.56° 000|Constants: 25 Variables: h forced 20 h free Rth front Rth back 2 Gr/Re|2 Total PV panel area 0.451 m (front surface) 10.5273 14.0247 23.2924 (front and back surface) 5.8123 4.8730 4.1749 (U) 209.2 m 157.8 m 95.2 m (U) 763.0 m 910.03 m 1062.4 m 0.5536 0.0418 0.0042|
|55 10 10 15 15 20 20 25 25 30 30 35 35 Time (minutes)|40 4015 % Error|RC (measured) (minutes) 6.3800 5.6503 3.9933 RC (predicted) (minutes) 7.4166 6.0833 3.966 13.978% 7.1178%|

1000 40

800 30

noitaidaR raloS600 erutare

20 pmeT

10 200

the For q 9

|than|10,|
|---|---|
|as follows:||
|T|(19)|
|S|,|

cell

for an

(20)

noitaidaRraloS600

0.673%
Fig. 6. Temperature response of the PV panel with wind speed of 2.14 m/s.

that the step change in solar radiation occurs, which is usually a short interval. It can be seen from this table that the proposed thermal model predicts the time constant with a worst case accu- racy of 13.98%, and an average error of 7.26%.

The ground temperature is assumed to be equal to the ambient temperature and it is taken that the ambient temperature is the same on all sides of the PV panel. The radiative heat loss to the sky is given as:

q rad¼ 3FsAsTrear 4 =frontTsky 4 (21)

3 Emissivity (a measure of how well a material radiates heat). The emissivity from the front glass surface is given as 0.91 [4] while the value for the back surface of the PV panel is 0.85 [35]; s Boltzmann constant; F View factor. The heat loss that occurs from the front and rear surface of the PV panel between the ground and the sky is dependent on the view factor. These equations are given in the Appendix. The radiative heat losses may be included in the RC equivalent model of Fig. 1. However, the resulting radiative thermal resistance values are very large when compared to the convective heat resistance values, and therefore were neglected.

6. Validation of the thermal model The total thermal resistance and capacitance of the PV layers (Section 3) and the total heat loss by forced convection, free convection and radiative heat loss effects (Section 4) are combined to give the final value of time constant, s, under the prevailing weather conditions. The methodology for the thermal model is summarised in the flowchart of Fig. 3. The experimental setup for the thermal model is shown in Fig. 4. The setup consists of a BP350U PV panel placed at 35 on a venti- lated scaffolding structure. A moisture resistant thermistor is used to measure the PV back surface temperature. Wind measurements and global radiation values from a BF3 Sunshine sensor are measured and recorded by LabView every minute. The PV panel is connected to a battery, resistive load and maximum power point tracker (MPPT). The PV panel is operated at its maximum power point using MPPT, which ensures that the PV operating tempera- ture is at a minimum [8]. If the panel was left in open circuit, most of the incoming solar radiation would be converted to heat.
7. Results In this section, the thermal model is applied to three cases of varying wind speeds 0.77 m/s, 2.14 m/s, and 5.76 m/s in order to predict the time constant, s, of the PV panel under varying atmo- spheric conditions. Minute by minute measurements of the wind speed, global radiation, PV panel back surface temperature and ambient temperature are used to calculate the convective and radiative heat loss from the panel. The predicted time constant values are compared to the measured time constant under the three different wind speeds. The measured response of the PV panel back temperature to a step change in the solar radiation for each of the three wind speeds are shown in Figs. 5e7. The time constant is estimated for the step change in solar radiation, where the step change must be at least 600 W/m². The values for the forced and free heat transfer coefficients, the equivalent thermal resistances for the front and back surfaces of the PV panel, and measured and predicted time constants are given in Table 3 for each wind speed. The ratio of Gr/Re² is also shown to indicate whether free or forced convection is the dominant heat loss mechanism. The agreement is very good given the unpredictable, intermittent nature of the wind. Errors of 20% in predicting the forced convection coefficient were assumed in Ref. [26] while 12% error were reported in Ref. [30] for indoor tests. In the proposed thermal model, it is expected that these inaccuracies should be minimised because the mean wind speeds, PV cell back surface temperatures and ambient temperatures are averaged over the period of time
8. Conclusions A new thermal model has been presented to predict the temperature response time of a PV panel. The model has been validated by measurements of a PV panel under varying wind speeds. The model incorporates atmospheric conditions, the material composition of the PV panel and the mounting structure. Acknowledgements This work was funded by the Irish Research Council for Science, Engineering & Technology, (IRCSET) and Enterprise Ireland. Appendix A. Definitions of heat transfer parameters Nusselt number is defined as: hL Nu ¼ k air
(A1)

Reynolds number is defined as:

<u>wL</u> Re ¼ (A2) n

Rayleigh number is defined as:

##### Ra ¼ Gr Pr (A3)

Grashof number is defined as:

<u>gbðTcellTambÞL³</u> Gr ¼ 2 (A4) n

The Prandtl number, Pr, is defined as:

##### Pr ¼ cm (A5)

k

The properties Pr, n, and b are evaluated at the film temperature T film, which is defined as:

<u>T</u> <u>cellTamb</u> T film¼ 2 (A6)

View factors for radiative heat loss:

F front sky¼ <u>1</u> ð1 þ cos bÞ (A7) 2

F front ground¼ <u>1</u> ð1 cos bÞ (A8) 2

F rear sky¼ ½1 þ cosðp bÞ (A9)

F rear ground¼ ð1 cosðp bÞÞ (A10)

References

[1] J.K. Tonui, Y. Tripanagnostopoulos, Air-cooled PV/T solar collectors with low cost performance improvements. Solar Energy 81 (4) (2007) 498e511. [2] K.H. Hussein, I. Muta, T. Hoshino, M. Osakada, Maximum photovoltaic power tracking: an algorithm for rapidly changing atmospheric conditions. IEEE Proceedings Generation, Transmission, Distribution 142 (1) (1995) 59e64. [3] P. Midya, P.T. Krein, R.J. Turnbull, R. Peppa, J. Kimball, Dynamic maximum power point tracker for photovoltaic applications, in: 27th IEEE Power Elec- tronics Specialists Conference, 1996, pp. 1710e1716. [4] G. Notton, C. Cristofari, M. Mattei, P. Poggi, Modelling of a double-glass photovoltaic module using finite differences. Applied Thermal Engineering 25 (2005) 2854e2877. [5] A.D. Jones, C.P. Underwood, A thermal model for photovoltaic systems. Solar Energy 70 (4) (2001) 349e359. [6] S.J. Ransome, P. Funtan, Why hourly averaged measurement data is insufficient to model PV system performance accurately, in: 20th European Photovoltaic Solar Energy Conference, 2005, pp. 2752e2755. [7] D.L. King, J.K. Dudley, J.A. Kratochvil, W.E. Boyson, Temperature coefficients for PV modules and arrays: measurements methods, difficulties, and results, in: Proceedings 25th IEEE photovoltaic specialists conference, 1997, pp. 118 3 e1186. [8] G.M. Tina, R. Abate, Experimental verification of thermal behaviour of photovoltaic modules, in: 14th IEEE Mediterranean Electrotechnical Confer- ence, 2008. [9] H. Matsukawa, K. Kurokawa, Temperature fluctuation analysis of photovoltaic modules at short time interval, in: 31st IEEE Photovoltaic Specialists Confer- ence, 2005, pp. 1816e1819. [10] R.E. Lacy, Climate and Building in Britain. Department of the Environment, Building Research Establishment, 1977. [11] BP Solar.www.bpsolar.com (assessed 04.01.10). [12] Z.H. Lu, Q. Yao, Energy analysis of si solar cell modules based on an optical model for arbitrary layers. Solar Energy 81 (2007) 636e647. [13] W. Jooss, Multicrystalline and back contact buried contact silicon solar cells, PhD dissertation, Universitat Konstanz Fachbereich Physik, 2002. [14] J. Lai, T. Perazzo, Z. Shi, A. Majumdar, Optimisation and performance of high resolution micro-optomechanical thermal sensors. Sensors and Actuators 58 (1997) 113e119. [15] G.J.M. Phylipsen, E.A. Alsema, Environmental Life-Cycle Assessment of Multi- crystalline Silicon Solar Cell Modules Report No. 95057. Netherlands Agency for Energy and the Environment, 1995. [16] J.E. Hatch, Aluminum: Properties and Physical Metallurgy, second ed. ASM International, 1984.

[17] STR Photocap Solar Cell Encapsulants.www.strsolar.com (assessed 04.01.10). [18] J.A. Palyvos, A survey of wind convection coefficient correlations for building envelope energy systems 801e808. ’ modelling. Applied Thermal Engineering 28 (2008)

[19] F.P. Incropera, D.P. DeWitt, Fundamentals of Heat and Mass Transfer. John Wiley & Sons, 2002. [20] W.H. McAdams, Heat Transmisson, Third ed. McGraw-Hill, New York, 1954. [21] J.H. Watmuff, W.W.S. Charters, D. Proctor, Solar and Wind Induced External Coefficients Solar Collectors 2nd Quarter. Revue Internationale d’Helio- technique, 1977, p. 56. [22] P.J. Lunde, Solar Thermal Engineering. John Wiley and Sons, 1980. [23] E.M. Sparrow, J.W. Ramsey, E.A. Mass, Effect of finite width on heat transfer and fluid flow about an inclined rectangular plate. Transaction of ASME Journal of Heat Transfer 101 (1979) 199e204. [24] F.L. Test, R.C. Lessmann, A. Johary, Heat transfer during wind flow over rect- angular bodies in the natural environment. Journal of Heat Transfer 103 (2) (1980) 262e267. [25] R.J. Cole, N.S. Sturrock, The convective heat exchange at the external surface of buildings. Building and Environment 12 (1977) 207e214. [26] S. Sharples, P.S. Charlesworth, Full-scale measurements of wind-induced convective heat transfer from a roof-mounted flat plate solar collector. Solar Energy 62 (2) (1998) 69e77. [27] E. Sartori, Convection coefficient equations for forced air flow over flat surfaces. Solar Energy 80 (2006) 1063e1071. [28] S. Shakerin, Wind-related heat transfer coefficient for flat-plate solar collec- tors. Transaction of the ASME 109 (1987) 108e110. [29] O. Turgut, N. Onur, Three dimensional numerical and experimental study of forced convection heat transfer on solar collector surface. International Communications in Heat and Mass Transfer 36 (2009) 274e279. [30] D.R. Pitts, L.E. Sissom, Schaum’s Outline of Theory and Problems of Heat Transfer. McGraw Hill, 1997. [31] D.L. King, W.E. Boyson, J.A. Kratochvil, Photovoltaic Array Performance Model Report: SAND2004e3535. Photovoltaic System R&D Department, Sandia National Laboratories, 2004. [32] A. Bejan, A.D. Kraus, Heat Transfer Handbook. Wiley-IEEE, 2003. [33] S.W. Churchill, A comprehensive correlating equation for laminar, assisting, forced and free convection. Journal of American Institute of Chemical Engi- neers 23 (1) (1976) 10e16. [34] J.A. Duffie, W.A. Beckman, Solar Engineering of Thermal Processes. John Wiley & Sons, New York, 1980. [35] D. Morgan, D. Bazilian, H. Kamalanathan, D.K. Prasad, Thermographic analysis of a building integrated photovoltaic system. Renewable Energy 26 (3) (2002) 449e461.
