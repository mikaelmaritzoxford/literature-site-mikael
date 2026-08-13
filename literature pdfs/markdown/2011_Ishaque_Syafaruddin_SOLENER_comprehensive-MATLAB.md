Available online at www.sciencedirect.com

Solar Energy 85 (2011) 2217–2227 www.elsevier.com/locate/solener

# A comprehensive MATLAB Simulink PV system simulator with partial shading capability based on two-diode model

a a,⇑ b

##, Zainal Salam

## Kashif Ishaque

##, Syafaruddin

a Faculty of Electrical Engineering, Universiti Teknologi Malaysia, UTM 81310, Skudai, Johor Bahru, Malaysia b Kumamoto University, 2-39-1 Kurokami, Kumamoto 860-8555, Japan

Received 4 January 2011; received in revised form 24 May 2011; accepted 6 June 2011 Available online 5 July 2011

Communicated by: Associate Editor Igor Tyukhov

Abstract

This paper proposes a comprehensive MATLAB Simulink simulator for photovoltaic (PV) system. The simulator utilizes a new two- diode model to represent the PV cell. This model is known to have better accuracy at low irradiance level that allows for a more accurate prediction of PV system performance during partial shading condition. To reduce computational time, only four parameters are extracted for the model. The values of Rpand Rsare computed by an efficient iteration method. Furthermore, all the inputs to the sim- ulators are information available on standard PV module datasheet. The simulator supports a large array combination that can be inter- faced to MPPT algorithms and power electronic converters. The accurateness of the simulator is verified by applying the model to five PV modules of different types (multi-crystalline, mono-crystalline, and thin-film) from various manufacturers. It is envisaged that the pro- posed work can be very useful for PV professionals who require simple, fast, and accurate PV simulator to design their systems. The developed simulator is freely available for download. 2011 Elsevier Ltd. All rights reserved.

Keywords: PV module; Partial shading; Bypass diode; Blocking diode; Simulator; MATLAB Simulink

1. Introduction Large and small scale PV power systems have been com- mercialized due to its potential long term benefits. Their growth rates have been accelerated by the generous fed-in tariff schemes and other initiatives provided by various governments to promote sustainable green energy. In large PV power generation, systems are dominated by grid- connected; examples can be seen in (Albuquerque et al., 2010; Beser et al., 2010; Chen et al., 2010; Mellit and Pavan, 2010; Yoon et al., 2011). To ensure optimal use of the available solar energy, maximum power point track- ing (MPPT) scheme is applied to the power converters ⇑ Corresponding author. Tel.: +60 7 5536187; fax: +60 7 5566272. E-mail addresses: kashif@fkegraduate.utm.my (K. Ishaque), zainals@fke.utm.my (Z. Salam). 0038-092X/$ - see front matter 2011 Elsevier Ltd. All rights reserved. doi:10.1016/j.solener.2011.06.008
(Chaouachi et al., 2010; Enrique et al., 2010; Messai et al., 2011). However, for a proper design of MPPT con- troller, an accurate simulation model of the module is required. This is especially the case when the peak power point changes continuously due to environmental varia- tions. In particular, one important situation to be consid- ered is the substantial drop of power yield during partial shading condition. The most important component that affects the accuracy of simulation is the PV cell modeling. For improved accuracy, the two-diode model (with Rpand Rs) has been proposed by several researchers (Hovinen, 1994; Gow and Manning, 1999; Hyvarinen and Karila, 2003; Nishioka et al., 2003, 2007; Kurobe and Matsunami, 2005; Chowdhury et al., 2007). Although more to that of single diode model, the inclusion of an additional diode increases the number of computed parameters. Several

K. Ishaque et al. / Solar Energy 85 (2011) 2217–2227
computational methods are proposed (Hovinen, 1994; Gow and Manning, 1999; Chowdhury et al., 2007), but in all of these techniques, new coefficients are introduced into the equations, increasing the computing burdens. An alternative approach to describe the two-diode model is by investigating its physical characteristics such as the elec- tron diffusion coefficient, minority carrier’s lifetime, intrin- sic carrier density, and other semiconductor parameters (Hyvarinen and Karila, 2003; Nishioka et al., 2003, 2007; Kurobe and Matsunami, 2005). While these models are useful to understand the behavior of the cell, information about these parameters is not always available in commer- cial PV datasheets. A comprehensive PV system simulator should fulfill the following criteria: (1) it should be fast, yet can accurately predict the I–V and P–V characteristic curves, including partial shading condition. (2) It should be a flexible tool to develop and validate the PV system design, inclusive of the power converter and MPPT control. Although exist- ing software packages like P-Spice, PV-DesignPro, Solar- Pro, PVcad, and PVsyst are available in the market, they are relatively expensive, unnecessarily complex and rarely support the interfacing of the PV arrays with power con- verters (Ishaque et al., 2011b). Over the years, several researchers have studied the characteristics of PV modules under partial shading condi- tions. In (Alonso-Garcı´a et al., 2006), an experimental study was carried out but was limited to module-level shad- ing. The effect of shading on the output of the PV modules and the changes in their I–V characteristics was investi- gated by (Kawamura et al., 2003). A numerical algorithm was proposed by (Quaschning and Hanitsch, 1996) to sim- ulate the complex shading characteristics of the arrays whereby every element (each cell of the module, bypass diode, blocking diode, etc.) was represented by a mathe- matical expression. The results were attractive but the sim- ulation was considerably complex, thus limiting its ability to predict the performance of larger systems. A MATLAB based modeling to study the effects of partial shading based on the single diode model was proposed in (Patel and Agarwal, 2008). Although the model is relatively simple, it exhibits serious deficiencies when subjected to high tem- perature variations. Moreover, it does not account for the open circuit voltage coefficient, KV(Ishaque et al., 2011a). Considering the importance of this issue, this paper pro- poses a fast, accurate, and comprehensive PV system simu- lator using the MATLAB Simulink environment. The availability of the simulator in the MATLAB platform is seen as an advantage from the perspective of researchers and practitioners alike as this software has almost become a de-facto standard in various engineering discipline. An important contribution of this work is the application of the two-diode model that is known to have better accuracy, especially at low irradiance level. It allows for a more accu- rate prediction of PV system performance during partial shading conditions. To reduce computational time, the model parameters extraction is reduced to four while the

values of Rpand Rsare estimated by an efficient iteration method. The accurateness of the model is compared with two other modeling methods namely the Rs-andRp-model. In addition, the proposed work supports large array simu- lation that can be interfaced with MPPT algorithms and actual power electronic converters. This allows for the designer to evaluate the overall system performance when interacting with other components within the systems. It is envisaged that the proposed work can be very useful for PV professionals who require fast and accurate PV sim- ulator to design their system.

2. PV module modeling
2.1. Modeling using the two-diode model The two diode model is depicted in Fig. 1. The output current of the module can be described as (Chih-Tang et al., 1957)
≥ ~ I¼I I exp <u>V þ IRS</u> 1 PV o1 a₁VT 1 ≥ ~ ~ <u>V þ IRsV þ IRs</u> I o2exp a V 1 R ð1Þ 2 T 2 p

where IPVis the current generated by the incidence of light. I o1and Io2are the reverse saturation currents of diode 1 and diode 2, respectively. The Io2term is introduced to compensate for the recombination loss in the depletion re- gion as described in (Chih-Tang et al., 1957). Other vari- ables are defined as follows: VT 1,2(= NskT/q) is the thermal voltage of the PV module having Nscells con- nected in series, q is the electron charge (1.60217646 10 19

C), k is the Boltzmann constant
(1.3806503 10 23 J/K), and T is the temperature of the p–n junction in K. Variables a₁ and a₂ represent the diode ideality constants; a₁ and a₂ represent the diffusion and recombination current component, respectively. Typically, three points at Standard Test Conditions (STC) (Isc, 0), (Vmp, Imp) and (Voc, 0) are provided by the manufacturer’s datasheet. An accurate estimation of these points for other conditions is the main goal of every modeling technique. Although greater accuracy can be achieved using this model (compared to the single diode model), it requires the computation of seven parameters, namely IPV, Io1, I o2, Rp, Rs, a1,and a₂. To simplify, several researchers assumed a₁ = 1 and a₂ = 2. The values are chosen based on the approximations of the Schokley–Read–Hall

<u>I</u>

*I* *D1ID2* *+* *Rs*

*I Rp* *V* *PV*

<u>-</u>

Fig. 1. Two diode model of PV cell.

recombination in the space charge layer in the photodiode

|||and R|values||
|---|---|---|---|---|
|||p|s||
||||p||
||PP|mp|mp s||
|p||V þI R|V þI R|P|
|PV|o|V|ðp 1ÞV|V|

(Chih-Tang et al., 1957). Although this assumption is widely used but not always true (Keith et al., 2000).

2.2. Extraction of model parameters
2.2.1. Determination of IPVcurrent The equation for PV current as a function of tempera- ture and irradiance can be written as:
<u>G</u> I PV¼ðIPV STCþ KiDT Þ ð2Þ GSTC

where IPV STC(in Ampere) is the light generated current at STC, DT ¼ T TSTC(in Kelvin, TSTC=25 C), G is the surface irradiance of the cell, and GSTC(1000 W/m²) is the irradiance at STC. The constant Kiis the short circuit cur- rent coefficient, normally provided by the manufacturer.

2.2.2. Determination of saturation current and diode ideality factors For a single diode model, the equation to describe the reverse saturation current that considers the temperature variation is given by (Villalva et al., 2009), i.e.,
<u>ðIPV STCþ KiDT Þ</u> I o¼ ð3Þ exp ½ ðVoc;STCþ KvDT Þ=aVT1

The constant Kvis the open circuit voltage coefficient; this value is available from the datasheet. For the two diode model, several researchers have calculated the values of I o1and Io2using iteration. The iteration approach greatly increases the computation time, primarily due to the non- suitable values of the initial conditions (Jinhui et al.,

2009). In (Ishaque et al., 2011a), a new analytical equation of both saturation currents was derived. Both saturation currents can be calculated as:
#### I ¼ I ¼ I

|o1 o2 o||p|
|---|---|---|
||PV STC i|p|
|oc;STC|v||

<u>ðI þ K DT Þ</u> ¼ ð4Þ exp½ðV þ K DT Þ=fða₁ þ a₂Þ=pgVT1

The equalization simplifies the computation because no iteration is required; the solution can be obtained analyti- cally. In accordance to Shockley’s diffusion theory, the dif- fusion current, a₁ must be unity (Chih-Tang et al., 1957). The value of a₂, however, is flexible. Based on extensive simulation carried out, it is found that if a₂ P 1.2, the best match between the proposed model and practical I–V curve is observed. Since (a₁ + a₂)/p = 1 and a₁ = 1, it follows that variable p can be chosen to be P2.2. This generalization can eliminate the ambiguity in selecting the values of a₁ and a₂. Eq. (1) can be simplified in terms of p as. ~~ <u>V þ IRsV þ IRs</u> I¼IPV o

|I exp|þ exp|2|are obtained analytically. Variable p can||
|---|---|---|---|---|
|PV o s p|T|T|o||

VTðp 1ÞVT ~ <u>V þ IR</u> ð5Þ R

2.2.3. Determination of R From Eq. (5), the expression for R at maximum power point (M) can be rearranged and rewritten as:
<u>V þ I R</u> R ¼ no hi mp mp s <u>mp mp s</u> max;E I I exp T þexp T 2 mp ð6Þ

It can be seen that Eq. (6) is an algebraic equation for any finite value of Rs, the value of Rpcan be calculated eas- ily. Therefore, by taking the advantage of this algebraic expression, a simple and linear iterative method can be adopted. The remaining two parameters of Eq. (5), i.e., Rpand Rs,are obtained through matching technique (Ishaque et al., 2011a). Although this approach has been used in the single diode model, it has not been applied for two-diode model. The idea behind this method is to match the calculated peak power (Pmp,C) and the experi- mental (from manufacturer’s datasheet) peak power

(P) by iteratively increasing the value of R while simul- mp,E s taneously calculating the Rpvalue. To start the iteration process, the suitable initial values (typically a low value – to ensure better results) for Rp and R are assigned. Hence, R is chosen to be zero and s s Rpis calculated by following equation: ~ ~ <u>VmpVocnVmp</u> Rpo¼ ð7Þ I scnImpImp where the first term in bracket in Eq. (7) is the slope of the line segment between the short circuit and the MPPpoint, while the second is the slope of line segment between the open circuit voltage and MPPpoint. For a typical PV mod- ule, the difference between the nominal values of Vocnand Vmpis not large; consequently, the second term in Eq. (7) will always be very low. Furthermore, the first term will also result in a very low value compared to the actual value of R. This ensures that Eq. (7) will always return a low va- lue of R, which is a good initial guess for the iteration. For each iteration, the value of Rpis calculated simulta- neously using Eq. (6). With the availability of all the seven parameters, the output current of the cell can now be deter- mined using well known numerical techniques. In our work, we have utilized standard Newton–Raphson method. This algorithm has the advantage of a very quick, quadratic convergence for initial values near the root, so that a good solution can be calculated within a few itera- tion steps (Quaschning and Hanitsch, 1996). The flowchart that describes the Pmpmatching algorithm is given in
Fig. 2.
 Using Eqs. (2) and (4), all the four parameters of this model can be readily extracted, i.e., IPV, Io, Rp,and Rs. From these, only R and R need to be determined by iter-
p s ation. IPVand Io be chosen to be any number value greater than 2.2. These simplifications have greatly improved the computational speed of the simulator.

≥

3.1. Verification of the two-diode model for different irradiation levels
Fig. 3 shows the I–V curves for a single KC200GT mod-
 ule for different levels of irradiation (per unit quantity: Sun = 1 equivalent to 1000 W/m²). The calculated values from the proposed two-diode and Rp-models are evaluated against measured data from the manufacturer’s datasheet. Comparison to the Rs-model is not included to avoid over- crowding of plot. However, the results for the Rs-model will be analyzed later in the performance evaluation between the three models. The proposed two-diode model and the Rp-model exhibit similar results at STC. This is to be expected because both models use the similar maxi- mum power matching algorithm at STC. However, as the irradiance goes lower, more accurate results are obtained from the two-diode model, especially in the vicinity of the open circuit voltage. At Voc, the Rp-model shows depar- ture from the experimental data, suggesting that Rp-model is inadequate when dealing with low irradiance level. This variation is envisaged to have significant impact during partial shading.
Fig. 4 analyzes the relative error of Vocand the maxi-
 mum power point Pmpfor KC200GT module at different
Fig. 2. Matching algorithm. irradiance levels. The temperature is set to STC. The rela-
 tive error is defined as the difference between simulated and measured Vocand Pmpvalues. The difference is then divided
3. Validation of the two-diode model
by the measured value. As can be seen at STC irradiance, there is a very small difference in the Vocvalues among The two diode model and its parameters extractions the three models. However, as the irradiance is reduced, described in this paper are validated by measured parame- a significant deviation is observed for the Rsand R -mod-p ters of five PV modules of different brands/models. These els. Similar results can be seen for the Pmp. On the other include the multi-, mono-crystalline, and thin-film types. hand, the proposed two-diode model accurately calculates The specifications of the modules are summarized in Pmpat all irradiance values.

Table 1. The detailed modeling results for the aforemen-

tioned PV modules (except SM55) using this model can be seen in (Ishaque et al., 2011a). The SM55 PV module 3.2. Verification of the two-diode model for temperature will be used later in the validation of partial shading variations results. The computational results are compared with the Rs(Walker, 2001) and Rp(Villalva et al., 2009) models. The performance of the models when subjected to tem-

Table 2 shows the parameters for the proposed two-diode perature variation is considered. All measurements are con-

model. The actual number of parameters computed is only ducted at STC irradiance of 1000 W/m². The proposed four because Io1= Io2= Iowhile a₁ = 1 and p can be cho-model is compared to the Rs-model. The comparison sen arbitrarily, i.e., p P 2.2. specifically is chosen to highlight the problem with the

Table 1

STC specifications for the modules used in the experiments. Parameter <u>Multi-crystalline</u> Mono-crystalline Thin-film

|Parameter|Multi-crystalline|||Mono-crystalline|Thin-film|
|---|---|---|---|---|---|
||Siemens|Kyocera|Shell|Shell|Shell|
||SM55|KG200GT|S36|SP-70|ST40|
|I|3.45 A|8.21 A|2.3 A|4.7 A|2.68 A|
|V|21.7 V|32.9 V|21.4 V|21.4 V|23.3 V|
|I|3.15 A|7.61 A|2.18 A|4.25 A|2.41 A|
|V|17.4 V|26.3 V|16.5 V|16.5 V|16.6 V|
|K|77 mV/ C|123 mV/ C|76 mV/ C|76 mV/ C|100 mV/ C|
|K|1.2 mA/ C|3.18 mA/ C|1 mA/ C|2 mA/ C|0.35 mA/ C|
|N|36|54|36|36|42|

sc oc mp mp v i s

Table 2

Parameters for the proposed two-diode model. Parameter <u>Multi-crystalline</u>

|Parameter|Multi-crystalline||||
|---|---|---|---|---|
||Siemens||Kyocera||
||SM55||KG200GT||
|I|3.45 A||8.21 A||
|V|21.7 V||32.9 V||
|I|3.15 A||7.61 A||
|V|17.4 V||26.3 V||
|I|2.232|10 A|4.218|10 A|
|I|3.45 A||8.21 A||
|R|144.3 X||160.5 X||
|R|0.47 X||0.32 X||

|||Mono-crystalline||Thin-film||
|---|---|---|---|---|---|
|Shell||Shell||Shell||
|S36||SP-70||ST40||
|2.3 A||4.7 A||2.68 A||
|21.4 V||21.4 V||23.3 V||
|2.16 A||4.24 A||2.41 A||
|16.7 V||16.5 V||16.6 V||
|2.059|10 A|4.206|10 A|1.13|10 A|
|2.3 A||4.7 A||2.68 A||
|806.4 X||91 X||263.3 X||
|0.89 X||0.51||1.6 X||

sc oc mp mp 10 10 10 10 9 o PV p s

**Proposed Two-diode Model Rp-Model Experimental Data**Rs-model when subjected to temperature changes. The KC200GT PV module tested here for analysis. As can be **KC200GT Multi-Crystalline PV Module**seen in Fig. 5, the curves I–V computed by the two-diode **8**model fit accurately to the experimental data for all tem- **Sun=1** perature conditions. In contrast, at higher temperature, results from the Rs-model deviate from the measured val- ues quite significantly. **6** **Sun=0.8** Fig. 6 shows the performance of the three models for the Vocand Pmpwhen subjected to variations in module tem- **I (A)Sun=0.6**perature. There is no significant difference between the Rp **4** and the two-diode models. However, the Rsmodel exhibits poor performance for both Vocand Pmpcalculations. **Sun=0.4** **2**

3.3. Verification of model for various PV technologies
**Sun=0.2** **0 0**

|0 0|||
|---|---|---|
||10|V (V) 20|
|Fig. 3. I–V curves of R|-model and proposed two-diode model of the||
|KC200GT PV module for several irradiation levels.|||

**30**To further evaluate the effectiveness of the proposed model for different silicon technologies, comparisons pbetween S36 (mono-crystalline), SP70 (multi-crystalline), and ST40 (thin-film) are carried out. All these modules are manufactured by Shell. For this test, the irradiance is maintained constant at STC. Fig. 7a shows the relative

**3** **Rs-Model** **Rp-Model** **2** **Proposed Two-Diode Model** **1**

|8 6|||KC200GT Multi-Crystallline PV Module|||
|---|---|---|---|---|---|
|I (A)|Rs-Model|Proposed Two-diode Model Experimental Data||||
|4 2 0 0|Fig. 5. I–V curves of R PV module for several temperature levels.|10 s|o C 75 V (V) 20 and proposed two-diode model of the KC200GT|o 50|o C C 25 30|

**0** **Relative Error @ Voc (%)1000 800 600 400 200** **Solar Irradiance (W/m2)**

**(a)**
**6**

**4**

**2**

**0** **Relative Error @ Pmp(%)** **Solar Irradiance (W/m2)**

**(b)**
Fig. 4. Relative error for Vocand Pmp, for Rs, Rpand the proposed two-

diode model for KC200GT PV module.

Rs Model Rp Model Proposed 2-D Model 10

0 50 25 0-25 5

**4** **Rs-Model** **3** **Rp-Model** **2** **Proposed Two-diode Model**

**1**

**Relative Error @ Voc (%)0** **25 50 75** **Temperature (ºC)**

**(a)**
**4**

**3**

**2**

**1**

**Relative Error @ Pmp(%)0** **25 50 75** **Temperature (ºC)**

**(b)**
Fig. 6. Relative error for Vocand Pmp, for Rs, Rpand the proposed two-

diode model for KC200GT PV module.

error for Pmpfor a wide variation of temperature ( 25 C to +50 C). From the data, it can be concluded that more accurate results are obtained from the two-diode model for all silicon technologies. Furthermore, it can be noted that using the Rs-model, considerably errors occur for Vmp and Pmp. This is particularly severe for the thin film tech- nology. Fig. 7b depicts a comparison of all three modeling techniques when the irradiance is varied from 200 to 1000 W/m². A temperature of 25 C is maintained in these analyses. As can be seen, superior results are obtained with the proposed two-diode model. As expected, the Rs-model shows a significant variation with the ST40 PV module. The extensive experimental verification above has pro- ven that the two diode model is superior to that of single diode model with Rsand Rp. This justifies its usage in the proposed simulator.

3.4. Computational time
Table 3 shows the computation time of three modeling
 approaches. Shortest computation time is observed for the Rs-model; this is to be expected as the calculation does not involve any iteration process. For the proposed model, due to the inclusion of an extra diode current in Eq. (5), the

|SM55|8.1|108.1|215.6|
|---|---|---|---|
|KC200GT|21.1|105.3|221.7|
|S36|8.71|256.8|424.6|
|SP-70|7.97|183.8|276.2|
|ST40|1.1|430|646.5|
 computational time, in average, is about 1.6 times longer that of the Rp-model. The increase is much less than one order of magnitude, and hence computational-wise, can be regarded as insignificant. The relatively short computa- tional time is due to the fewer number of parameters to be calculated compared to the previous work on two-diode model. Furthermore, the iteration method to compute the values of Rsand Rpis very efficient. By considering the
0 50 25 0-25 Relative Error @ Pmp (%) 40

0 50 25 0-25 Temperature (ºC)

**(a)**
Rs Model Rp Model Proposed 2-D Model 40

0 1000 800 600 400 200

0 1000 800 600 400 200 Relative Error @ Pmp (%) 40

0 1000 800 600 400 200 Solar Irradiance (W/m 2 )

**(b)**
Fig. 7. Relative error for Pmpof Rs,Rpand the proposed two-diode model

for S36 (multi-crystalline), SP70 (mono-crystalline) and ST40 (thin film)

(a) for irradiance variation and (b) temperature variation.
Table 3
 Computation time (ms). PV module R R Proposed two-diode
s p Type Model Model Model SM55 8.1 108.1 215.6

improved accuracy achieved using the proposed model, the slight increased in computational time is justified.

4. PV simulator development

|I|4exp @ I|A||
|---|---|---|---|
|pp PV|o|||
||N s N T ss|T ss|N s N p N N|
|PV|p s ss|pp||

4.1. Large array configuration In a PV power generation, a centralized inverter topol- ogy is utilized due to economic reasons. A single (central- ized) inverter is connected to a large number of PV modules, typically, in a series parallel configuration. This topology is known as the series–parallel (SP) topology as shown in Fig. 8. Based on Fig. 8, a modified equation for the current for the SP configuration can be written as:
Fig. 8. Series parallel combination in PV array.

Current Group A Volt Sun_A Irradiance Shading Pattern A Group B Current Volt Sun_B Irradiance Shading 1s i Pattern B Current Group C In1 - + + - Volt Sun_C Irradiance Shading Pattern C Group D Current Volt Add Sun_D Irradiance Shading Pattern D

< V þ IRs <u>Nss</u> <u>N</u> <u>pp</u> I¼Npp PV o : V N 0 1 39 0 1 <u>ss ss</u> @ V þ IR <u>pp</u> A 5= @V þ IR <u>pp</u> A þ exp 2 ð8Þ ðP 1ÞV N; R <u>ss</u> pp

where I; I₀; R; R; p are the parameters of an individual PV module. Note that N and N are series and parallel PV modules, respectively in a given SP array. Using the large array configuration described above, a generalized simulation tool is developed in MATLAB Simulink. The structure of the simulator is shown in Fig. 9. The simulator is able to cater for any number NssNpparray, where Nss and Npprepresent the number of series and parallel mod- ules for each group, respectively. The simulator has the capability of showing the effects of shading, temperature, and diodes (bypass and blocking). For illustration, an example of large array simulation with partial shading condition is shown here. Fig. 10 shows a PV array composed of four groups namely, groups A, B, C, and D. Each group can be configured for a different shading and temperature conditions.

Fig. 11 depicts the mask implementation of group A. It

has been developed by based on Eq. (8). To simulate the shading effects of PV array, role of bypass diode is very

Shading Pattern A Shading Pattern B

Blocking Diode Group A Group BGrou

Fig. 10.

BL_di 1 s Out1 + + vSwitch --PV_Data Blocking To Workspace Diode

I-V Curve of PV Simulator

P-V Curve of PV Simulator

Shading Pattern C Shading Pattern D

p CGrou p D

3 PV array.

Fig. 9. Simulink implementation of the PV simulator.

SP connection for 20

Fig. 11. A mask implementation of PV simulator for group A.

vital. Its effect is added by the voltage equation of bypass diode that is given as: ~ <u>IPV</u> VBD¼ AVTln þ 1 ð9Þ Io

where A is the diode ideality factor (for group A) and IPVis the diode current of the bypass diode. Once the shading condition will occur, current will flow from the bypass diode instead of PV module and hence multiple peaks will be observed at the output of PV array.

Fig. 12 shows the input parameter template of the pro-

posed simulator. The module used in this experiment is SM55. All parameters for the inputs are available from manufacture’s datasheet. The other inputs are the shading pattern, temperature, number of series modules (Nss), and number of parallel modules (Npp). Bypass diode of any group can be removed by selecting in the popup menu in the parameter template of the PV simulator.

5. Results and discussion
5.1. Effects of bypass diode Under shaded conditions, the shaded modules behave as a load instead of generator, which produce the hot spot problem. This problem can be avoided by driving the cur- rent of non-shaded PV modules through the bypass diode.
Fig. 12. PV simulator Block parameters window in simulink.
 The proposed simulator must be capable to replicate the effects of this diode. For the given parameters of the simu- lator as shown in Fig. 12, the I–V and P–V curves for three diode, and (3) with the same shading conditions of (2) but different cases are shown in Fig. 13a and b. (1) With no without bypass diode. It can be observed that number of shading (G = 1 kW/m²), (2) with partially shaded peaks equal to the irradiance imposed for each shading pat- (Group A = 1 kW/m², Group B = 0.75 kW/m², Group tern. However, more precisely, it depends on the tempera- C = 0.5 kW/m², Group D = 0.25 kW/m²) and with bypass ture of the modules, the irradiation level, the shading

Fig. 13. (a) I–V curves, (b) P–V curves for SM55 from PV simulator for parameters in Fig. 11.

Fig. 14. (a) I–V curves, (b) P–V curves for SM55 of PV simulator with and without blocking diode.
 pattern, and the array configuration (Patel and Agarwal, circuit current, it becomes reversed biased and a small leak-
2008). age current flows through the diode. Besides removing the
current imbalance condition, blocking diode prevents the module from loading the battery at night by avoiding cur-

5.2. Effect of blocking diode
rent flow from the battery through the PV array.

Bypass diodes, which limit the hot spot effect, offer no protection to the current imbalance. In normal conditions 5.3. Validation of partial shading (i.e., no shading), bypass diodes are reverse biased and remain in this position. In order to protect against current In order to verify the accurateness of the proposed imbalance, a blocking diode is used in series with the PV model for partial shading conditions, the result is com- array such as shown in Fig. 8. Blocking diode modify the pared with the work carried out by (Syafaruddin et al., forward characteristics of a PV array. During normal oper-2010), which is based on Artificial Neural Network. In ation, it is forward biased and conducts the PV array cur-(Syafaruddin et al., 2010), a real-time PV emulator was rent hence produce a small voltage drop that is shown in designed to emulate P–V characteristics curves with a

Fig. 14. When the PV array current goes beyond the short special focus on partial shading conditions. For the PV

modules model, the P–V characteristic was generated based on Sandia’s PV module electrical performance model. The main component of the developed emulator consists of two personal computers (PCs) with Analog–Digital (AD) and Digital–Analog (DA) hardware under a real-time dSPACE platform. Several inhomogeneous irradiance distributions were used to investigate the behavior of the proposed system. Here, SM55 PV module is used for the validation. It is expected that once the accuracy of PV module is established (with the two-diode model), the simulator can be extended to any type of PV module. This is a common practice by other researchers too, for example (Patel and Agarwal, 2008; Syafaruddin et al., 2010). It can be observed in

Fig. 15 that, in general, proposed simulator gives the similar

Data (Syafaruddin, Karatepe et al. 2010) Proposed Model 12

Array Current (A) 4

0 0 50 100 150 200 250 300 350 400 Array Voltage (V)

**(a)**
Data (Syafaruddin, Karatepe et al. 2010) Proposed Model

|||Shading occurs here||
|---|---|---|---|
|400 200 Voltage (V) PV Array||(a)||
|0 0|0.2|0.4 0.6 0.8 1||
|10 5 PV Array Current (A)||(b)||
|0 0|0.2|0.4 0.6 0.8 1||
|4000 2000 Power(W)|Local Maxima|(c)||
|0 0 Fig. 17.|0.2|0.4 0.6 0.8 1 Time(s) (a and b) Output voltage and current from the PV array, (c) PV array power (solid line) and dc–dc converter power (dash line).||

Array Power (W) 400

0 Array Voltage (V)

**(b)**
Fig. 15. Simulation and experimental results (a) I–V characteristics and

(b) P–V characteristics.
*I* *PV*LD + PV +

Array *VPV* SW C *Vo* R

### <u>− −</u>

MPPT Controller

Fig. 16. PV system description utilizing designed simulator.

results to the data provided by (Syafaruddin et al. (2010)). In particular, it shows close resemblance especially in the vicin- ity of the global peak. However, there appear some discrep- ancies in the P–V curves at the local peaks. The following reasons could be the sources of disagreement. First, a silicon solar cell was used as an irradiance sensor, which is known to be inferior in accuracy. Secondly, due to the constraint of measurement sampling, the change in irradiation over time during may not be recorded.

5.4. Simulation with converter and MPP controller One of the most important requirements of a PV system simulator is its ability to interface with the power electronic systems with their associated control algorithms. Fig. 16 depicts a simulation example of a PV system together with its boost dc–dc converter and MPPT controller. The SM55 PV modules are used in the simulation for a 20 3 array configuration. The MPPT controller utilizes the conven- tional Perturbation and Observe (P&O) algorithm. The performance of P&O to track the global MPP is evaluated for the partial shading condition shown in Fig. 13b. The simulation results are shown in Fig. 17. Initially, the array receives a uniform irradiation of (G = 1 kW/m²). It is observed that until t = 0.4 s, at which shading occurs, the

PV array’s voltage and current are retained at 309 V and

9.44 A, respectively. This corresponds to the MPP of 2917 W, i.e., point A in Fig. 13b. Due to the shading con- ditions (at t = 0.4 s), operating point is shifted to a new MPP at 760 W (point B). This new operating point is clearly a local maxima. This example highlights the inabil- ity of a conventional MPPT scheme (i.e., P&O) to distin- guish between the global and local maxima.
6. Conclusion In this paper, a MATLAB Simulink PV system simula- tor based on an improved two-diode model is proposed. To reduce computational time, the input parameters are reduced to four, and the values of Rpand Rsare estimated by an efficient iteration method. Furthermore, the inputs to the simulator are information available on standard PV module datasheet. The simulator supports large array sim- ulation that can be interfaced with MPPT algorithms and actual power electronic converters. The accurateness of the simulator is verified by five PV modules of different types (multi-crystalline, mono-crystalline, and thin-film) from various manufacturers. It is observed that the two- diode model is superior to the Rpand Rsmodels. Further- more, a PV system, together with the power converters and controllers, is simulated. The results are found to be to be in close agreement with theoretical prediction. The designed simulator is available for free and can be down- loaded from the following Web site: [http://sites.google](http://sites.google). com/site/drkishaque/Downloads. Acknowledgment The authors would like to thank Universiti Teknologi Malaysia for providing the facilities and research grant to conduct this research and the reviewrs for thier valueable comments. References Albuquerque, F.L., Moraes, A.J., et al., 2010. Photovoltaic solar system connected to the electric power grid operating as active power generator and reactive power compensator. Solar Energy 84 (7), 1310–1317. Alonso-Garcı´a, M.C., Ruiz, J.M., et al., 2006. Experimental study of mismatch and shading effects in the I–V characteristic of a photovol- taic module. Solar Energy Materials and Solar Cells 90 (3), 329–340. Beser, E., Arifoglu, B., et al., 2010. A grid-connected photovoltaic power conversion system with single-phase multilevel inverter. Solar Energy 84 (12), 2056–2067. Chaouachi, A., Kamel, R.M., et al., 2010. A novel multi-model neuro- fuzzy-based MPPT for three-phase grid-connected photovoltaic sys- tem. Solar Energy 84 (12), 2219–2229. Chen, Y., Athienitis, A.K., et al., 2010. Modeling, design and thermal performance of a BIPV/T system thermally coupled with a ventilated concrete slab in a low energy solar house: Part 1, BIPV/T system and house energy concept. Solar Energy 84 (11), 1892–1907. Chih-Tang, S., Noyce, R.N., et al., 1957. Carrier generation and recombination in P–N junctions and P–N junction characteristics. Proceedings of the IRE 45 (9), 1228–1243.
Chowdhury, S., Taylor, G.A., et al., 2007. Modelling, simulation and performance analysis of a PV array in an embedded environment. In: Universities Power Engineering Conference, 2007. UPEC 2007. 42nd International. Enrique, J.M., Andu´ jar, J.M., et al., 2010. A reliable, fast and low cost maximum power point tracker for photovoltaic applications. Solar Energy 84 (1), 79–89. Gow, J.A., Manning, C.D., 1999. Development of a photovoltaic array model for use in power-electronics simulation studies. Electric Power Applications – IEE Proceedings 146 (2), 193–200. Hovinen, A., 1994. Fitting of the solar cell IV-curve to the two diode model. Physica Scripta T54, 2. Hyvarinen, J., Karila, J., 2003. New analysis method for crystalline silicon cells. Photovoltaic energy conversion, 2003. In: Proceedings of 3rd World Conference on. Ishaque, K., Salam, Z., et al., 2011a. Simple, fast and accurate two-diode model for photovoltaic modules. Solar Energy Materials and Solar Cells 95 (2), 586–594. Ishaque, K., Salam, Z., et al., 2011b. Modeling and simulation of photovoltaic (PV) system during partial shading based on a two- diode model. Simulation Modelling Practice and Theory 19 (7), 1613–

1626.
Jinhui, X., Zhongdong, Y., et al., 2009. Design of PV array model based on EMTDC/PSCAD. In: Power and Energy Engineering Conference,

2009. APPEEC 2009. Asia-Pacific.
Kawamura, H., Naka, K., et al., 2003. Simulation of I–V characteristics of a PV module with shaded PV cells. Solar Energy Materials and Solar Cells 75 (3–4), 613–621. Keith, M., Peter, A., et al., 2000. Depletion-region recombination in silicon solar cells: when does mDR=2? In: 16th European Photovoltaic Solar Energy Conference and Exhibition, pp. 251–254. Kurobe, K.-i., Matsunami, H.AU, 2005. New two-diode model for detailed analysis of multicrystalline silicon solar cells. Japanese Journal of Applied Physics 44 (12), 8. Mellit, A., Pavan, A.M., 2010. A 24-h forecast of solar irradiance using artificial neural network: application for performance prediction of a grid-connected PV plant at Trieste, Italy. Solar Energy 84 (5), 807–

821.
Messai, A., Mellit, A., et al., 2011. Maximum power point tracking using a GA optimized fuzzy logic controller and its FPGA implementation. Solar Energy 85 (2), 265–277. Nishioka, K., Sakitani, N., et al., 2003. Analysis of the temperature characteristics in polycrystalline Si solar cells using modified equiva- lent circuit model. Japanese Journal of Applied Physics 42 (Part 1, No.

12), 5.
Nishioka, K., Sakitani, N., et al., 2007. Analysis of multicrystalline silicon solar cells by modified 3-diode equivalent circuit model taking leakage current through periphery into consideration. Solar Energy Materials and Solar Cells 91 (13), 1222–1227. Patel, H., Agarwal, V., 2008. MATLAB-based modeling to study the effects of partial shading on PV array characteristics. Energy Conver- sion, IEEE Transactions on 23 (1), 302–310. Quaschning, V., Hanitsch, R., 1996. Numerical simulation of current– voltage characteristics of photovoltaic systems with shaded solar cells. Solar Energy 56 (6), 513–520. Syafaruddin, Karatepe, E., et al., 2010. Development of real-time simulator based on intelligent techniques for maximum power point controller of photovoltaic system. International Journal of Innovative Computing, Information and Control (IJICIC) 6, 20. Villalva, M.G., Gazoli, J.R., et al., 2009. Comprehensive approach to modeling and simulation of photovoltaic arrays. Power Electronics, IEEE Transactions on 24 (5), 1198–1208. Walker, G., 2001. Evaluating MPPT converter topologies using a MATLAB PV model. Journal of Electrical & Electronics Engineering, Australia 21 (1), 8. Yoon, J.-H., Song, J., et al., 2011. Practical application of building integrated photovoltaic (BIPV) system using transparent amorphous silicon thin-film PV module. Solar Energy 85 (5), 723–733.
