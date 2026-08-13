|European Association for the|International Conference on Renewable Energies and Power Quality|
|---|---|
|Development of Renewable Energies, Environment||
|and Power Quality (EA4EPQ)|Santiago de Compostela (Spain), 28th to 30th March, 2012|

(ICREPQ’12)

# Comparison of PV Cell Temperature Estimation by Different Thermal Power Exchange Calculation Methods

1 1 2

M. Bardhi, G. Grandi and G.M. Tina 1 Department of Electrical Engineering
D.I.E., University of Bologna, Italy
Phone number: +39 3334505488, e-mail: <u>marinel.bardhi@studio.unibo.it</u>, <u>gabriele.grandi@unibo.it</u>

2 Department of Electric, Electronic and Informatics Engineering

D.I.E.E.I., University of Catania, Italy
Phone number: + 39 095 7382337, e-mail: <u>giuseppe.tina@dieei.unict.it</u>

**Abstract** A steady-state thermal model for calculate the tem-lot of parameters are needed [2 - 4]. Other method are perature of a photovoltaic (PV) module has been developed for based on a single layer model, so one equation to describe outdoor installation such as ground-mounted systems. The PV it is used and the PV panel is divided in front and rear temperature is influenced by environmental variables such as: sections [5 - 11]; In more of the models, in particular, the irradiance ambient temperature, intensity and direction of the forced convection is considered and the long-wave wind, module design, orientation and mounting structure. As radiation is neglected. Few studies are made with natural well as it is influenced by electrical parameters. In literature convection or with limited ventilation. It is found in this some single layer thermal balance consider only an overall heat transfer coefficient as a function of wind speed, neglecting the case that the radiative contribution is the greater form of

radiative thermal flux. In this paper, five thermal balance are heat exchange between the module and the surrounding compared and it is shown that the radiative term cannot be environment. neglected, otherwise the PV temperature could be overestimated The model considered in this paper [1] aims to obtain a for low solar radiation intensity and it could be underestimated mono-dimensional module’s operating temperature and for high solar radiation intensity. For this reason, the percentage the percentage contribution of the thermal exchanges contribution of the heat exchanges, normalized as function of normalized as function of normal incoming solar normal incoming solar radiation, are evaluated for wind speed radiation. Moreover, the parameters found in literature in within 1 m/s (natural convection). different models are compared. The proposed model distinguishes the thermal balance

## KeyWords terms into front and rear, as shown in Fig. 1; where swin is

the incident solar radiation, *Q* are the heat exchanges, *T*

Single layer photovoltaic module, energy balance, tem- perature estimation, natural convection.

**1. Introduction** There are a lot of parameters related to the photovoltaic module temperature (*Tpv*); they can be classified as follow: meteorological and PV module installation site data, thermal characteristic of module materials, its geometrical and electrical characteristics [1]. They are summarized into the well-known thermal model transfer contributions: conduction, convection, radiation (solar and long-wave) and electrical power generated. There are many methods to calculate the operating tem- perature, same consider a multi-layer thermal model, but a
Fig.1. Scheme of energy flux

[https://doi.org/10.24084/repqj10.417](https://doi.org/10.24084/repqj10.417) RE&PQJ, Vol.1, No.10, April

are the temperatures, *Ppv* is the generated electric power, *θ* is the solar angle of incidence and *β* is the module tilt angle. Moreover, the subscripts *f* and *b* stay for front and back/rear surfaces, respectively. *Pv* is photovoltaic module, *conv* is the convection, *rad* is the long-wave radiation, *a* is the ambient, *s* is the sky and *g* is the ground. The following assumption are made [1]: -The transition time is not considered therefore the model’s variables are constant over time. -The thermal conduction within the device and be- tween it and the support structure are negligible. -Material properties are assumed to be independent of temperature and equal on both sides. -The optical properties (emissivity, reflection, absorp- tion and transmission coefficients) are supposed con- stant, i.e. independent of wavelength, temperature and angle of incidence. -Surfaces are isothermal. -Clear sky conditions are considered. -Natural convection is the only form of heat transfer considered, where fluid flow up to *v* = 1 m/s speed. -Ground-mounted system is considered; in this case the rear convective fluid flow does not interact with ground. -Ground temperature is assumed equal to ambient temperature and this one is assumed equal in all sides of the photovoltaic module. -Mean temperature *Tpv* is assumed for the PV module. Note that temperatures of front and back (rear) surfaces of the PV module, *Tpv,f*and *Tpv,b*, are not the same. The cells temperature is usually obtained by standard indoor tests, where a thermal sensor in placed on the back surface. However, the difference between the cells and the back cover is about 3-4 °C, but it is neglected and an average temperature is assumed.

**2. Thermal model** With the above assumptions the energy balance on a PV module [1] is expressed as follow:
### SWn pv rad+=-convQQP(1)

Where *SWn* is the net solar radiation, furthermore it is assumed *QSWn pvP*.-=

There are many studies in literature that aim to modelize the thermal behaviour of a PV module and so to determine the PV cell temperature depending on some variables (en- vironmental and electrical variables) and some parameters (module and installation parameters). The one layer model is the most used because it allows to reach a good precision with a low computational effort and by a limited number of variables and parameters. A thermal equivalent electrical circuit can be used effec- tively to find the thermal fluxes and the unknown tem- peratures in a PV module (whose complexity is fixed by the number of considered layers) that affect a ground mounted PV module. For example, Fig. 2 shows two equivalent circuits related to a single layer model. It is worth noticing that the voltage source Tskyis a voltage controlled voltage source as itepends d on the ambient temperature Ta, as hereinafter explained. Specifically, the circuit shown in Fig. 2.b has been ob- tained by the circuit of Fig. 2.a under the hypotheses that both ambient (*Ta*) and ground (*Tg*) temperatures are the same up and down of the PV module. In this case the thermal conductances of the front surface are in parallel to the corresponding ones of the back surface. Another difference is about conductances, related to ra- diative thermal exchange, grad that are non-linear in (a) and linear in (b), see Section 2.C.

*A. Net Solar radiation and Electric Power* *generated* The net shortwave radiation SWn (W) is a function of incident solar radiation *swin* (W/m²) reaching the PV module surface, its reflected fraction *ρpv·swin* by the front face and the angle of incidence θ [12] between the normal of the surface and the sunlight direction:
*SW swn*)1()cos(*in*rq*Apv*×-××= (2)

The reflectivity *ρpv*is a function of module configuration, characteristics of materials, orientation, sun position and wavelength. Some value are evaluated experimentally by [10], as about 8.88% for single-crystalline silicon, 10.8% for multicrystalline silicon, and 10.5% for amourfous sili- con. In this paper a mean value of 10% has been con- sidered. The electric power generated *Ppv* by typical silicon solar cell is about 12% of the normal incident solar radiation according to Standard Test Conditions (STC) efficiency

[https://doi.org/10.24084/repqj10.417](https://doi.org/10.24084/repqj10.417) RE&PQJ, Vol.1, No.10, April

(a) (b)
Fig. 2. Equivalent circuit for one-layer thermal model of a PV module: a) complete circuit and b) simplified.

|Table I. - Module efficiency formulas||
|---|---|
|Correlation|Ref.|
|TT ×+-×-×= Logsw)] bhh g pv STC 10 in|[3,4,5,10,13] ()(1[|
|4/14/1 hh 22 -×-= (4, 273) 0|[14]|
|××× sw atb 0 in bhh --×-×= TT)(1[] 0 STCa h|[15]|

*STC*

*T* *pv*

*STC*

*conv*-××+=-×=*aconvpv* ηSTC:

*P* h*pvswSTC*)cos(*in*q *A* ×××= (3)

However, in the calculation of the *Ppv*, the dependency of the efficiency in operating temperature and irradiance should be considered. There are many correlations in literature summarized in [7]. Table I shows three correlations:

-the first one is probably the most used expression for h where *TPV* and *swin* are the variables; it is compared with *ηSTC* assumed in (3) and a difference of temperature is discovered of about 0.32 °C (*Tpv*=

44.98 °C considering *ηSTC* and *Tpv*=45.3 °C considering h). The comparison is made assuming:
2 *β*=30 degree, *swin*=700 W/m, *Ta*=20 °C, module parameter *β₀* =0,4 %/°C, and *γ* =0, *TSTC*=25 °C [3,5,7,10]; -the second one shows that in some cases the correlation between *Tpv* and h is not linear; -the third one uses directly the ambient variables (*swin*, *Ta* and *v*) to determine the convective coefficient *h*.

The different formulations of the value *Q* are motivated by the different definition of the efficiency *η* (Table II), in particular the considered irradiance. In this way (assuming θ = 0 degree) for the incident solar radiation, the part crossing the glass is *τ·swin*, where *τ* is the transmittance of the cover system for beam and diffuse radiation, and the part absorbed by the PV cells is *α·τ·swin,* with *α* the absorption coefficient of the cells. The data *α·τ* = 0.855 is very close to data found in the lit- erature [3,5]. As stated above, we consider a constant optical parameters (a good approximation only for the central day time period). Its value is sun position- dependent with a 20-30% reduction [11].

*B. Convection Exchange* The rate of heat transfer by natural convection from a solid surface at a uniform temperature *Tpv* to the surroundings fluid, at ambient temperature *Ta*, is expressed by Newton’s law of cooling as:
### TTAhhTTgQabf pv)()()( (4)

where *gconv* is the convective conductance, *hf*and *hb* are the front and back convective coefficients, respectively, *A* is the surface area. The heat transfer from inclined plate could be predicted by vertical plate formulas, if the component of the gravity vector along a surface of the plate was used in the calcu- lation of the Rayleigh number *Ra*. This is substantially correct for the lower surface. For the upper surface the boundary layer becomes unstable [17]. The experiments confirm what we suspect for the lower surface of a hot plate, but the opposite is observed on the upper surface. When the boundary layer remains intact, the Nusselt number *Nu* *Lh*× *Nu* = (5) *k* can be determined from the vertical plate relations provided that *g* in Ra relation is replaced by *g·sin(β)*, for β<30° [2,18,19,20]. *Nu* relation for the upper surface are available in literature [1]. Some authors suggest the following Churchill and Chu formula:

2 é ù ê ú

## () 387.0

ê6/1 ú *Ra* ×

825.0 27 ê /8
*Nu* (6) += ú 16/9ê ú

492.0 ê
ç úæ ÷ ö 1 + Pr ê ç úè ÷ ø ë û

for the inclined hot plate in all range of Ra, but most accurate in the range 10 -1 ≤ Ra ≤ 10 9. For the hypothesis take in this work the Ra value stands in the range 10 7 -10 9. Furthermore the laminar fluid flow transition is assumed negligible applying the Vliet’s formula [18] The convective coefficient *h* is a function of the fluid properties: density (*k*), kinematic viscosity (*νk*), dynamic viscosity (*αd*) and volume expansion coefficient (*β’*); they

||||Table II: - PV module temperatures comparison as a function of net solar radiation less electric power generated (formulas found in literature)||||
|---|---|---|---|---|---|---|
||Correlation Q)1(A sw hr in Eq. 4 Q)(sw A hta in Q A sw)(tha in|Ref. ××--= [10] ××-×= [5] ×××-= [16]|Optical Parameters ρ = 0.1 ρ = 0.0888 η = 0.12 STC α · τ = 0.9 α · τ = 0.855 α · τ = 0.875 α · τ = 0.9*0,9=0.81 η = 0.12 STC α · τ = 0.9; τ = 0.9 α · τ = 0.94*0.93=0.8742 α · τ = 0.9*0.9=0.81 α · τ = 0.9*0.95=0.855 η = 0.12 STC|Ref. [10] [3,5] [3,5]|T [°C] pv 44.98 45.32 44.98 43.56 44.19 42.12 45.35 44.43 42.51 43.75||

|||||Table. III. - PV module temperatures evaluated with different Long-wave radiation formulas: Eq. (7) and Eq. (11)||||||
|---|---|---|---|---|---|---|---|---|---|
||SW n [%]|Q rad,f,s [%]|Q rad,f,g [%]|Q rad,b,s [%]|Q rad,b,g [%]|Q conv,f [%]|Q conv,b [%]|P pv [%]|T pv [°C]|
|Eq. (9)|90|-29.9|-1.4|-2|-18.4|-14.6|-11.7|-12|44.98|
|Eq. (12)|90|-29.5|-1.5|-1.8|-16.8|-15.7|-12.7|-12|46.48|

The measurement of sky temperature is complex and rarely available; several expressions allow the calculation of this temperature, a simple ones [3] is given by Swinbank [20] and is used in this study:

5.1
0552

*T*.0 *T* ×= (10) *s* *a*
In literature there is a different formulation of the thermal radiation exchange (10), where the surrounding emissivity coefficients (ground and sky) are implemented in Eq. (6) [10,11]:

follow:

||||4|4|
|---|---|---|---|---|
|||sfconv,|f pv|ss|
|,, sfrad pv|s|, gf|4 f pv|4 gg|
|,, gfrad pv|g|, sb|4 b pv|4 ss|
|sbrad ,, pv|s|, gb|4 4 b pv|gg|
|gbrad,, pv|g||||

*TTAFQ* ees ()

are evaluated at the film temperature *(Ta+Tpv)/2*, except *β’*, which should be evaluated at *Ta* On the other hand, the convective coefficients that we can find in literature [5 - 9] are only wind-speed-dependent and they are not reliable for low -or without- wind speed.

*C. Long-Wave Radiation Exchange* The long-wave radiation leaving one surface that reaches the surrounding environment (sky and ground) as a function of view factor is given by the electric analogy as
)(

)( +×-××××+ (7) *TTg*)( ×-××××+ *TTg*)(

The radiative conductance between a surface i and the sky or ground (*grad,s* or *grad,g*) is expressed by [2,3,4,19]:

*TTTTAFsiisirad pv*,,, *s pv*se*s*( 22 )()

(8)
*giigirad pvTTTTAFg pv*,,, *g*se()() 22

The view factors are assumed as [1,2,3,11]:

cos1 + cos1b-b

||; F =|F =|||
|---|---|---|---|---|
|,|sf,|gf|||
|,|sb,|gb|STC|pv|
|||||f f|
||||b||

2 2

(9)
-+)cos(1 bp--bp)cos(1 =*F*; *F* = 2 2

Where the subscripts *f* and *b* stand for the front and rear surfaces of the PV module. If sky is assumed as a black-body its temperature can be thought as a weighted average of the temperature between the ground and the upper troposphere where water vapor is much less abundant; the weight being a function of at- mospherically composition that change in height. For this reason the “sky temperature” is not the actual temperature of the sky and is called equivalent temperature. The actual sky temperature is not constant in height [1].

*TTAF* ees () (11) *TTAF* ees ()

( ees) *TTAF*

In Table III is compared the two formulas with emissivity coefficients equal to *0.95* [10,11] and *0.9* for the sky and ground respectively.

**3. Impact of models on Tpv** The aim of the thermal balance is to calculate the operating temperature and to understand how the single heat exchanges (normalized to the normal incident solar radiation) contributes to the global balance. A monocrystaline silicon solar cell is considered, with th₂e following parameters: surface area *A* = 0.769 × 1.586 m, efficiency *η* = 0.12, front albedo coefficient *ρ = 0.1* [10], front and rear emissivity coefficients, *ε* = 0.91 and *ε* and *ε* =0.85, respectively [2,10,11]. Furthermore the characteristic length is assumed equal to the height of the PV module: *L* = 1.586 m. The case examined in this work has been evaluated under some common conditions:
1) south orientation: to maximize the incident solar radiation;
2) mid-latitude installation site (45° north);

||Table IV. - Simple photovoltaic thermal models to predict the operating temperature||||
|---|---|---|---|---|
|=|(bhhta) Th sw a in STC STC STC 0 T pv bh h sw 0 STC in sw in += TT pv a ×+ vhh 1 32.0 w TT × sw pv a in 91.0 ×+= 2 + v NOCT 20 - += TT sw pv a in 800|[5] ××- [6] [7] [8]|××--××+× T 2 h = 25.3 [W/m K] η = 0.12 STC -1 β₀ = 0.0045 [°C] α·τ = 0.9 h₁ =6 [W/m² K] v = 1 [m/s] ω = 1 NOCT = 47 [°C]||
|T|T sw 943 v .0 028.0 528.1 3.4 pv a in|[9]|+×-×+×=||

Table V. - PV temperature and normalized thermal exchanges as function of Solar Radiation intensity <u>Ta = 20 °C, b = 30°, θ = 0°</u> ( )

|T [°C] pv|sw in2 [W/m]|SW N [%]|Q rad,f,s [%]|Q rad,f,g [%]|Q rad,b,s [%]|Q rad,b,g [%]|Q conv,f [%]|Q conv,b [%]|P pv [%]|
|---|---|---|---|---|---|---|---|---|---|
|20.12|100|90|-72.41|-0.04|-4.86|-0.53|-0.09|-0.08|-12|
|25.31|200||-49.17|-0.95|-3.3|-12.37|-6.76|-5.45||
|29.77|300||-40.55|-1.19|-2.72|-15.51|-9.99|-8.04||
|33.87|400||-36.02|-1.3|-2.42|-16.87|-11.85|-9.54||
|37.75|500||-33.22|-1.35|-2.23|-17.6|-13.08|-10.52||
|41.44|600||-31.30|-1.38|-2.1|-18.05|-13.94|-11.21||
|44.98|700||-29.92|-1.41|-2.01|-18.36|-14.59|-11.73||
|48.39|800||-28.87|-1.43|-1.94|-18.57|-15.08|-12.12||
|51.69|900||-28.04|-1.44|-1.88|-18.74|-15.47|-12.43||
|54.9|1000||-27.39|-1.45|-1.84|-18.87|-15.78|-12.68||

3) spring period (May 5
th );

4) solar declination 61°;
*A.* <u>First Step</u>*: net solar radiation formulas* *comparison as a function of generated electric* *power* In the first step, different formulations of Q found in literature are considered, and their impacts on Tpvis evaluated. The corresponding results are shown in Table II. The optical parameters are taken from [3,5] considering the properties of each single layer of module (front glass and TEDLAR). If a direct measurement of the incoming and reflected solar radiations are made, the *ρpv* values are taken from [10]. In [3] it is assumed that *α·τ=*
0.9·0.95=0.855 is very close to the data found in literature, but a difference of about 1.5 °C is observed comparing this value with the data given by [10] assumed for (2).
*B. Second Step: Long-wave Radiation comparing.* In the second step (7) (assumed for this work) and (11) are compared. The difference in PV temperature is about
1.5 °C, but the percentage contributions are very close. The best difference is in the *Qrad,b,g* term: 18.4% with (7) versus 16.8% with (11). The *Qconv* changes even if only the radiative term is modified. In fact, the convective coefficient *h* is *Tpv* dependent as the thermo-physical properties of the fluid are evaluated at film temperature *(Ta+Tpv)/2*. Finally (11) differ from (7) according to the surrounding environment variation through their emissivity coefficients (sky and ground in this case).
*C.* <u>Third Step</u>*: Models Comparison* Five different simplified thermal balances found in literature (see Table IV) have been compared and the temperatures variations as a function of incident solar radiation intensity are shown in Fig. 3. It is observed that models [5,6,7,8,9] have a temperature difference of about 1 °C for low solar irradiance intensity, while a difference
of about 2-3 °C is observed for its high value; anyway the models are in good correlation to the PV temperature value measured in outdoor applications. The five thermal models overestimate the PV temperature values compared with (1) [20] for low Solar irradiance intensity; the opposite happens for its high intensity values.

*D. Temperature variation as a function of solar* *Irradiance intensity* The PV temperature variation as a function of normal in- cident solar radiation, varied from 100 to 1000 W/m, is
2

observed. The hypotheses are 1) solar radiation normal to the PV surface, 2) ambient temperature constant at 20 °C, and 3) tilt angle fixed at 30°. Without incident solar radiation the module temperature should be almost equal to ambient temperature. A small radiative thermal exchange between sky and front/rear surfaces arises, due to the lower temperature of the sky with respect to the surrounding environment, as can be calculated by (10). To balance this effect an incident solar radiation of about

Fig. 3. PV temperature *Tpv*comparison as a function

of Solar Radiation intensity swin

100 W/m2 is necessary, as shown in table V. Increasing *swin* the convective flux increases too, and the radiation flux becomes less important, but it remains the greater term, in particular the radiation exchanged with the sky (28.46% versus 49,55% with 1000 W/m²). The temperature varies linearly, and it is in good correlation with the other cases examined in Fig. 3.

**4. Conclusion** The power balance allows calculating the operating tem- perature of a PV module (or PV system) and evaluating in advance the performance with real working condition. Currently, the performances are determined in indoor tests with standard conditions like STC and NOCT, but the values are never obtainable for outdoor applications. The efficiency of electric conversion depends on the ac- tual temperature of the module, therefore it is so important considers what the contributions that strongly influence the heat dissipation are, to enhance it and to achieve increased electric generation. In the most of the models, in particular, the forced convection is considered, and the long-wave radiation is neglected; less studies are made with natural convection or with limited ventilation. In the present study is observed the long-wave thermal radiation contribution as important part of heat exchange between the module and the surrounding environment, in particular with the sky. Anyway, with incident solar radiation increasing (therefore with temperature increasing) the thermal convection exchange goes up. For example it is observed that:

||2||
|---|---|---|
|in|rad|conv|
|in|rad|conv|
 -*sw* = 300 W/m : *Q* = 59.97 %; *Q* = 18.03 % -*sw* = 1000 W/m²: *Q* = 49,6 %; *Q* = 28,5 % In the first part of the paper is evaluated a temperature variation of about 1.5°C long-wave radiation and Q value. Therefore, an important issue that requires further study is related to the evaluation of *Qrad* and *QSWn pvP* to -= improve the calculation of cell operating temperature. In last part of the paper is observed that with low wind speed and low solar irradiance intensity the considered five thermal models found in literature overestimate the PV temperature compared with the values calculated in this paper. The opposite happens for high solar irradiance intensity: in literature a lot of single layer thermal balance consider only an overall heat transfer coefficient as a function of wind speed, neglecting the radiation exchange. Anyway, the PV temperature values are in good correlation with the field operating temperature measurements.
## References

[1] M. Bardhi, G. Grandi, M. Premuda “Steady State Global Power Balance for Ground-Mounted Photovoltaic Mod- ules”, ID109/©IREC2011-STPE, pp 359-365.

[2] S. Amstrong, W.G. Hurley, “A thermal model for photo- voltaic panels under varying atmospheric condition”, *Ap-* *plied Thermal Engineering*, 2010, vol. 30, pp. 1488-1496. [3] G. Notton, C. Cristofari, M. Mattei, P. Poggi, “Modelling a double-glass photovoltaic module using finite differences”, Applied Thermal Eng., 2005, vol. 25, pp. 2854-2877. [4] G. M. Tina, W. H. Tang, A. J. Mahdi, “Thermal parameters identification of photovoltaic module using genetic algo- rithm”, IET Conference on Renewable Power Generation 2011, vol. 2011. [5] M. Mattei, G. Notton, “Calculation of the polycristalline PV module temperature using a simple method of energy balance”, Renewable Energy 2006, vol.31, pp. 553-567. [6] D. Faiman, “Assessing the outdoor operating temperature of photovoltaic modules”, Progress in Photovoltaics: Research and Applications 2008, vol 16, pp. 307–315. [7] E. Skoplaki, J. Palyvos, “On the temperature dependence of photovoltaic module electrical performance: A review of efficiency/power correlations” Solar Energy 2009, vol. 83, 614-624. [8] INTERNATIONAL STANDARD IEC 61215, Crystalline silicon terrestrial photovoltaic (PV) modules – Design qualification and type approval Second edition 2005-04. [9] G. TamizhMani, L. Ji, Y. Tang, L. Petacci, “Photovoltaic module thermal/wind performance: long-term monitoring and model development for energy rating”, NCPV and so- lar program review meeting 2003, pp. 936-940. [10] J. P. Silva, G. Nofuentes, J. V. Munoz “Spectral reflectance patterns of photovoltaic modules and their thermal effects” Journal of Solar Engineering, 2010, vol. 132. [11] A.D. Jones and C.P. Underwood, “A thermal model for photovoltaic system”, Solar Energy, Vol. 70, pp. 349-359,

2001.
[12] M. Iqbal, An introduction to solar radiation, Academic Press, Orlando FL, 1983. [13] D. L. Evans, “Simplified method for predicting photovoltaic array output”, Solar Energy, 1981, vol. 27, pp. 555–560. [14] M. N. Ravindra, V. K. Srivastava, “Temperature depend- ence of the maximum theoretical efficiency in solar cells. Solar Cells”, Solar Cells, 1979, vol. 1, pp. 107–109. [15] M. D. Siegel, S. A. Klein, W. A. Beckman, “A simplified method for estimating the monthly-average performance of photovoltaic systems”, Solar Energy, 1981, vol 26, pp. 413-

418.
[16] W. Tian, Y. Wang, J. Ren, L. Zhu, “Effect of urban climate on building integrated photovoltaics performance”, Energy conference and Management, 2007, Publisher Elsevier Ltd, Vol. 48, pp. 1-8. [17] J. H. Lienhard IV, J. H. Lienhard V, A Heat Transfer Text- book, 2 nd edition, Phlogiston Press 2003, ISBN-13**:** 9780971383524. [18] Williams S. Janno, *Engineering heat transfer*, Second Edi- tion, C.R.C. Press, ISBN: 0-8493-2126-3. [19] Y. A. Cengel, *Heat Transfer*, Second edition, Mc Graw Hill, 2002, ISBN: 0-07-245893-3. [20] W. C. Swinbank, “Long-wave radiation from clear skies”

C.S.I.R.O. Division of Meteorological Physics, Aspendale, Australia, 1963.
