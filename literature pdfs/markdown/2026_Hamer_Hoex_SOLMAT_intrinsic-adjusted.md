Solar Energy Materials & Solar Cells 300 (2026) 114218

Contents lists available at ScienceDirect

## Solar Energy Materials and Solar Cells

journal homepage: www.elsevier.com/locate/solmat

# The intrinsic adjusted single-diode model: Solid State Physics meets accurate yield simulation

a,* b a,b a a Phillip Hamer, Chris Huang, Daniel Chen, Alison Lennon, Bram Hoex a *School of Photovoltaic and Renewable Energy Engineering, UNSW Sydney, Sydney, NSW, 2052, Australia* b *SunDrive Solar, Kurnell, NSW, Australia*

## ABSTRACT

The single-diode model (SDM) is the foundation of most photovoltaic yield simulations, but it becomes inaccurate for ultra-high-efficiency silicon devices where intrinsic recombination dominates. Here we present an “intrinsic-adjusted” extension to the single-diode model that explicitly accounts for intrinsic recombination. We compare this intrinsic-adjusted model to standard single-diode models using both simulated and experimental I-V data. We also investigate the use of additional fitting parameters, such as the device width and internal and external series resistances. The intrinsic-adjusted models reduced root-mean-square error by up to an order of magnitude for the simulated data and by a factor of three for the measured data, with improved accuracy near the maximum power point and open-circuit voltage. These results highlight the necessity of incorporating intrinsic recombination into modelling next-generation solar cells and suggest a pathway to more reliable yield simulations as commercial silicon photovoltaic technology approaches its intrinsic efficiency limits.

## 1. Introduction

Photovoltaic cell technology is undergoing rapid evolution, with mass-produced TOPCon and heterojunction (HJT) devices expected to demonstrate cell conversion efficiencies exceeding 26% in the next few years [1]. Champion devices are already well above 27% [2], close to the fundamental limit of 29.4% [3,4]. A key feature of these devices is extremely low carrier recombination, both in the silicon bulk and at the surfaces/contacts. This means that intrinsic recombination, consisting of Auger and radiative components [4,5], has a relatively high share of the total recombination. This, in turn, alters the I-V characteristics of the device, resulting in a significant increase in fill factor [6]. This presents a challenge for simulating these devices in the field. Yield simulation software, such as PVSyst, pvlib and SunSolve [7–9], has almost exclusively used the single-diode model to describe module behavior. This model is relatively straightforward and has, to date, provided sufficient accuracy for these simulations. However, recent studies have identified issues with current practices when simulating high fill factor modules [10]. The authors have previously proposed an intrinsic-adjustment to the single-diode model to overcome these limi tations [11]. More recently PVSyst have presented studies on the use of an intrinsic model in their own fitting process [12]. In the rest of this section, we will provide a very brief discussion of the single diode model and the most common ways of fitting solar cell

data, including the temperature dependence. We then provide a primer on the two sources of intrinsic recombination and their current parameterizations. In section 2, fitting methods and application, we will outline the simulated and measured I-V datasets used in this study. We then describe our method for determining intrinsic recombination and “adjusting” a given I-V curve to account for these effects. We then describe the fitting process these datasets using both simple single-diode models and intrinsic-adjusted models. The subsequent results section is split into three parts. The first part presents fits to simulated data from Quokka 3 under a wide range of operating conditions, the second part presents fits to measured I-V curves at a range of temperatures and finally the implications of the intrinsic-adjusted models, particularly for the temperature dependence of module power, are discussed.

### 1.1. The single-diode model

The single-diode model is the basis of almost all yield simulations. The single-diode equation for a single cell is commonly expressed as: [*V* *cell*+*IcellRS.cell*] *I* *cell*= *IphI₀ e* *nVth* 1 *Vcell*+ *IcellRS.cell*

(1)
*RSH.cell*

Where *Iph*is the photocurrent, *I*0is the dark saturation current, *RS*is the series resistance, *n* is the ideality factor and *RSH*is the shunt resistance.

* Corresponding author. *E-mail address:* p.hamer@unsw.edu.au (P. Hamer).
[https://doi.org/10.1016/j.solmat.2026.114218](https://doi.org/10.1016/j.solmat.2026.114218)

Available online 19 February 2026 Received 23 October 2025; Received in revised form 31 January 2026; Accepted 3 February 2026

0927-0248/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

*P. Hamer et al. Solar Energy Materials and Solar Cells 300 (2026) 114218* *Vth*is the thermal voltage given by: *kT* *Vth*= (2) *q* This can be extended to the module level, either by a full electrical solution of all module components or via the approximation:
[*V* *module*+*ImoduleNs RS.cell*] *nNs Vth* *Vmodule*+ *ImoduleN Rs S.cell* *I* *module*= *IphI₀ e* 1 (3) *NsRSH.cell*

Where *Ns*is the number of cells in series. If the module contains strings in parallel the same equation can be used however the values for *Iph*and *I* 0and *RS*need to be adjusted.

### 1.2. Determining the parameters of the single-diode model

While the single-diode model is near-ubiquitous, there are several distinct approaches for determining the parameters, and how they vary with operating conditions. In most cases, reference parameters are determined for STC conditions (25◦C, 1000 W/m 2 ) and then translated to different temperatures and irradiances. There is a wide range of ap proaches for fitting STC results. These may be categorized into two main approaches: analytical or numerical [13–18]. Readers are referred to the cited texts for further details. To determine the parameters away from reference conditions, several approaches exist. Of these, perhaps the best known are the De Soto, PVSyst and CEC methods [8,19,20]. While each approach has its merits we will focus on the PVSyst model. The temperature and irradi ance dependence of each of the single-diode parameters is given as follows: *G* [)] *I* *ph*= *Iph.ref*+ *αscT Tref*(4) *Gref* () ()3 *qEg* 1 1 *T nk TrefT* *I₀* =*I₀.refe* (5) *T* *ref*

*RS*= *RS.ref*(6) ) *n* = *nref*+ *μnT Tref*(7)

Where *G* is the irradiance in W.m 2, *Gref*is the STC irradiance, *Tref*is the STC temperature, *Eg*is the bandgap of silicon, *Iph.ref*, *I₀.ref*, *RS.ref*and *nref* are the single diode parameters obtained from the fit at STC conditions, *α* *sc*is the temperature coefficient of short circuit current and *μn*is the temperature coefficient of the ideality factor. It is also standard practice to adjust the shunt resistance such that it increases as incident irradiance decreases [8]. However, a recent study has highlighted that there is no physical basis for this assumption and that the apparent increase in shunt resistance is likely a measurement artifact [21]. Therefore, in this work, we will assume that:

*RSH*= *RSH.ref*(8)

The fitting parameters for this model are then: *n*0, *I*0.*ref*, *RS*.*ref*, *RSH*, *Ip*ℎ, *μ* *n*and *αsc*.

### 1.3. Intrinsic recombination and high efficiency devices

The term: [*V* *cell*+*IcellRS.cell*] *nVth* *I* *D*= *I₀ e* (9)

in the standard single-diode equation represents the voltage dependent recombination current. For most of their history silicon solar cells have been limited by Shockley-Read-Hall (SRH) recombination [22,23]. This

process is the defect-assisted recombination of a single electron-hole pair. As material quality and surface passivation of photovoltaic de vices have improved, this recombination current has decreased to the point where it no longer dominates other recombination mechanisms in modern, high-efficiency devices [20]. Intrinsic recombination is increasingly important for cells with conversion efficiencies over 26%. As the name implies, intrinsic recombination describes electrical carrier recombination processes that are inherent to silicon itself and are independent of the presence of defects. This intrinsic recombination creates an effective upper limit to device performance. Because silicon is an indirect-bandgap semiconductor, there are two intrinsic recombina tion processes that must be considered: Radiative and Auger.

### 1.4. Radiative recombination

Radiative recombination is the dominant process in *direct* bandgap semiconductors (e.g. GaAs, many perovskite materials). In this process, an electron and a hole directly recombine, releasing a photon with en ergy approximately equal to the direct bandgap energy. The full description of this recombination rate may be given by Ref. [4]: () *Rrad*= *BlowBrel*(*n,p*)1 *fPR*(*n,p,sample*)⋅*np* (10)

Where *n* and *p* are the concentrations of electrons and holes, respec tively, *fPR*(*n*,*p*,*sample*)is the carrier-dependent photon recycling factor, *Blow* is the radiative recombination coefficient at low carrier densities (4.76 × 10 15 cm 3 s 1 ) and *Brel*(*n*,*p*)accounts for the carrier dependence due to bandgap narrowing. However, Fell et al. [24] point out that when the Fermi-level splitting is known, this may be simplified to

2 Δ*ϕ*) *Rrad*= *Blowni,*0*ekT* 1 *fPR*(11)

Where Δ*ϕ* is the split in the quasi-fermi levels and *ni*is the intrinsic carrier density under equilibrium conditions. These properties are dis cussed in more detail in Appendix A. In this work, we assume that *fPR*= 0.6 [5]. Previous work [24] has suggested that this term should be temperature-dependent, which may be included in future improvements to the model. However, given that radiative recombination is a relatively small component of total intrinsic recombination. This simplification is currently considered acceptable.

#### 1.4.1. Auger recombination

Auger recombination is a process involving 3 carriers. An electron and a hole recombine, transferring the excess energy to the third carrier (either an electron or a hole), which eventually thermalizes back to the band edge. In silicon, Auger recombination is the dominant intrinsic process. It may be described by Refs. [4,5]: 2 2 *RAuger*= *Ceehgeehn p* + *Cehhgehhnp* (12)

Where *C* and *C* are the coefficients for each process (3.41 × 10 31 *ee*ℎ *e*ℎℎ cm 6 s 1 for 2 electrons and 1 hole and 1.17 × 10 31 cm 6 s 1 for 1 electron and 2 holes) and *gex*ℎare the low injection enhancement factors given by: 1 *g* *exh*=1+(*gexh.max*1) ()*αAuger*(13) 1 + *n* *N* + *ref* *p*

Where *g* (4.38 for *g* and 4.88 for *g*) are the Coulomb- enhancement *exh.max* magnitude *eeh* factors, *.max* *N* is the *ehh* Mott *.max* transition density *ref* (4× 10 cm) and *αAuger*is the empirical exponent. A key feature of the Auger recombination rate is that it depends on *n p* + *np* rather than the simple *np* product. This higher-order depen dence on the carrier concentration means that both the temperature and voltage dependence of Auger recombination differ substantially from

SRH and radiative recombination. The single-diode, as implemented in popular simulation programs, has proven very capable of describing devices where SRH is the domi nant recombination mechanism. However, the different behavior and temperature dependence of intrinsic recombination presents a new challenge, requiring adapted solutions. The concept presented in this paper is to “adjust” the electrical data of high-efficiency devices to ac count for intrinsic recombination. Studies concerning recombination mechanisms within silicon have dealt with intrinsic recombination for decades, with improved param eterizations developed every few years [4,25,26]. It is standard practice to adjust any recombination lifetime measurement to remove intrinsic recombination effects, allowing detailed studies of other defects of in terest. We applied a similar approach here.

## 2. Fitting methods and application

For numeric fitting methods and for application in yield modelling the key challenge is to generate the current for a given voltage, irradi ance and temperature. For the fitting process this allows the calculation of errors, and hence the creation of objective functions. For yield modelling it allows the generation of both current_voltage and power_ voltage curves, along with determination of key parameters such as the open-circuit voltage, maximum power point current and voltage and short circuit current.

### 2.1. Single diode i_from_v

The implicit solution of the single-diode equation is a well under stood problem and fundamental to almost all yield simulation software. For this work we make use of the open-source library pvlib-python [9], and particularly the bishop88_i_from_v function [27] The inputs to this function are the diode parameters from equations (4)–(8) for a given temperature and irradiance.

### 2.2. Intrinsic adjusted i_from_v

The creation of an intrinsic adjusted i_from_v function is a little more complicated. In addition to the diode parameters from equations (4)–(8) two additional parameters are required: the concentration of dopants in the silicon bulk and the volume of silicon in the cell. It was also found to improve the fitting accuracy if the series resistance was split into in ternal and external components such that:

*RS*= *RS.int*+ *RS.ext*(14)

The rationale behind this approach is described in Appendix A.

Fig. 1 presents the basic steps of this process when fitted to simulated

data. First, the voltage at each data point is adjusted for the external series resistance *RS*.*ext*. This allows the intrinsic recombination currents to be expressed as explicit functions of the adjusted voltage *Vadj*. Sec ondly, the recombination current due to intrinsic processes (Auger and radiative recombination) is calculated for each *Vadj*. The intrinsic recombination current is then added to the adjusted curve. Thirdly the contribution from the standard single-diode term is calculated using the bishop88_i_from_v process, with the *RS*term replaced by the internal series resistance *RS*.*int*. *Ip*ℎ, *I*0, *n, RS*.*int*and *RSH*were the fitting parame ters. In the final step the diode and intrinsic recombination currents are combined. The final equation is then: [*V* +*IR*] ))*adj S.intVadj*+ *IRS.int* *I* = *IphIradVadjIAugerVadjI₀ enVth* 1 (15) *RSH*

Where:

*Vadj*=*IRS.ext*(16)

*I* *rad*=*AwRrad*(17)

*I* *Auger*=*AwRAuger*(18)

Where *A* is the cell area and *w* is the cell width. If a single series resis tance value is used to simplify the process the equations are identical with *RS.int*set to 0.

**Fig. 1.** Generation of fitted I-V curve (25◦C, 1000 W/m2). A) adjustment of the voltage datapoints to account for RS.ext. B) Adjustment of the current datapoints to

account for intrinsic recombination. C) Single-diode fit to adjusted data. D) Final fit to original data.

The key challenge in calculating the intrinsic recombination current for a given adjusted voltage is determining the electron and hole den sities. Details of the steps involved are presented in Appendix A, along with discussion around the use of internal and external series resistances (*RS*.*ext*and *RS*.*int*). Once the intrinsic carrier density, electron density, hole density and quasi-fermi level splitting (*n²i, n, p,* Δ*ϕ*) have been determined equations (11), (12), (17) and (18) can be used to calculate the recombination currents. When performing a fitting process *Vadj*can be calculated for a given voltage using the measured/simulated current. However, when per forming yield simulations it is much simpler to determine the current for a given *Vadj*and then subsequently back out the voltage term. This still allows accurate determination of all relevant cell parameters.

### 2.3. Fitting process and model summary

Table 1 presents the four models used in this study. The “Datasheet”

approach largely attempted to mimic the description of the single-diode model within PVSyst [8], where datasheet values were used as the input. *RS*was determined based on the relative loss of efficiency under an irradiance of 200 W/m 2

c.f. 1000 W/m
2 at 25◦C. The temperature dependence of saturation currents, photocurrent and gamma were all calculated as per PVSyst. At present it is not possible to perform a similar fit for an adjusted model. The issue is that the residual single-diode curve often does not contain the two points that many analytical methods require to determine a good fit. There is no data point at open-circuit, and the maximum power point for the device does not align with the point that would give the maximum I-V product of the residual curve. All other models attempted to fit the entire I-V curve in a three-step process using the SciPy Python package scipy.minimize with a weighted RMSE as an objective. Weights of 20 and 100 were applied to the short- circuit current and maximum power point, respectively, and weights of 1 were assigned to all other values. Weighting of the open-circuit voltage was unnecessary since small errors in VOCtranslate into large errors in current at that point. These errors at each point were calculated as the difference between the target current and the output of the appropriate i_from_v function. In the first step of the fitting process, the *RS*parameter was deter mined to minimize the combined weighted RMSE at both STC and low- light conditions. For method 4 where both internal and external series resistances were being considered, a nested minimization method was used to determine the most appropriate values for *RS*.*ext*and *RS*.*int*, while maintaining the conditions of equation (14). For methods 2 and 3 the fitting process was identical except that *RS*.*int***was fixed at 0.** A further nested optimization function then determined normalized parameters for *n, Io*and *RSH*to minimize the weighted RMSE at STC for a given *RS* value. *Iph*was determined iteratively based on the other values and *ISC*. Finally, temperature coefficients *μn*and *αSC*were determined to mini mize the weighted RMSE at 50◦C, 1000 W/m 2. The authors acknowledge that it is highly likely that more advanced fitting methods would produce improved fits. Nonetheless, we contend that the current approach is sufficient to demonstrate the advantage of the “adjusted” model. The primary metrics used in this paper are the normalized root- mean-square error (n-RMSE) and the error in the maximum power (PMAXError). Normalization is carried out by dividing the RMSE (calculated between the data and the modelled current at each voltage) by the short-circuit current. To prevent errors near open-circuit voltage having an outsized impact on the results, any negative currents were replaced with 0 before calculating RMSE.

**Table 1**

Key features of the four models used in this study.

Method Fit to Include intrinsic RS terms 1: “Datasheet”ISC, VOC, VMP, IMP,No Single value Δ T I SC, ΔTPMP 2: Single-Diode I-V Curves No Single value 3: RAdjusted ) (Single I-V Curves Yes Single value

4: Adjusted S (RS.intI-V Curves Yes External and + RS.ext) Internal

## 3. Results and discussion

### 3.1. Quokka data

The first dataset used for this study was simulated data from Quokka3 [28], which is a detailed 3D device solver. Simulations were performed using a model of a previous world record cell, with a 26.81% conversion efficiency under STC conditions [29]. This 2 paper presents simulated I-V data for ◦ irradiances of 100 - 1100 W/m at temperatures between 15 and 55 C. In this instance both bulk doping and cell thickness are known parameters and fixed to their physical values. This means that method 3 has no additional fitting parameters when compared to the single diode models for this data. Method 4 introduces one additional fitting parameter, the internal series resistance (RS.int). Figs. 2 and 3 present color maps for both the n-RMSE and PMAX Error when comparing the outputs of the Quokka simulations with the four methods described above. As expected, the datasheet fit did a good job of tracking the maximum power with temperature and irradiance, with errors less than 0.4% for all conditions. However, the average n- RMSE value was more than double that of the next highest model, while the n-RMSE at STC was 3.7%. The single-diode model gave the largest PMAX Error values, particularly at low irradiances, with relative errors between 1.3 and 2.2% at irradiances below 200 W/m2. The n-RMSE values also rose at low irradiances but remained significantly lower than those from the datasheet fit. The adjusted model with a single RS value outperformed the single-diode model under all conditions, with RMSE values below 1.4% and PMAX Errors less than 0.7%. The PMAX Error did increase noticeably at lower irradiances. When external and internal series resistances were included in the model the maximum PMAX Error declined to 0.3% and the maximum RMSE was 0.93%. Higher errors were again present at low irradiances. The key parameters for each fit are presented in Table 2. The primary differences between the models were in the ideality factor, saturation current and series resistance. Because the non-adjusted models needed to account for Auger recombination (n0.67 ˜ under high injection) as part

**Table 2**

Fitting parameters for each of the four models.

PARAMETER DATASHEET SINGLE-ADJUSTED ADJUSTED FIT FIT DIODE FITFIT (RSONLY) (R R S_INT ) + S_EXT **J**

**0.REF** 1.1 × 10181.25
18 × 2.18 × 2 10142.75 × 2 1014 A/cm2 10 A/cm A/cm **n** **0** 0.763 0.766 A/cm2

1.11 1.11
**J**

**L.REF** 41.35 mA/ 41.35 mA/ 41.35 mA/ 41.35 mA/cm² cm² cm² cm² **R** **R** **SH** 7.5 kΩ cm2 2523 kΩ cm² 10 kΩ cm²
2 100 kΩ cm² **S** 0.200 Ω cm 0.160 cm² Ω 0.198 Ω cm N/A **R** **S_INT,**N/A N/A N/A 0.203, 0.134 **R** **S_EXT** Ω.cm² **μ** **N** 0.00036 K-10.00035 0.0003 K-10.00031 K-1 K -1 **α** **SC** 9.36 μA/cm²/ 9.36 μA/ 9.36 μA/ 9.36 μA/cm²/K K cm²/K cm²/K

**Fig. 2.** Error in maximum power for each model as a function of cell temperature and irradiance.

**Fig. 3.** Normalized RMSE for each model as a function of cell temperature and irradiance.

of the single-diode, the fitted ideality factors were less than 1. In curves, data points and the fits to them are presented in Fig. 4 under a contrast, for the adjusted models, the diode only had to account for non-range of conditions. It is notable that even under STC conditions, the intrinsic recombination, such that the ideality factor was greater than 1. datasheet fit was inaccurate between the maximum power point and The saturation currents are strongly affected by the ideality factor, open-circuit voltage. All three of the other models described the curve which accounts for the four orders of magnitude difference observed. more accurately under these conditions. A significant contributor to the The series resistance is noticeably lower for the single-diode fit when high n-RMSE values for the datasheet fit away from STC was the error in compared with the datasheet and adjusted fits. This allowed the single-predicting the open-circuit voltage, a previously reported issue with De diode model to fit the I-V curve at STC more accurately but resulted in Soto models [19]. The single-diode fit did not demonstrate the same greater errors at low irradiances. issue with temperature, but at low irradiances, inaccuracies were To further investigate the differences between the model's selected observed at both the maximum power point and open-circuit voltage.

**Fig. 4.** I-V data from Quokka simulations and fits to the data using the four models described in Section X. A) Under STC conditions (1000 W/m², 25◦C), B) At 1000

W/m², 50◦C, C) at 200 W/m², 25◦C.

**Fig. 5.** Weighted RMSE values at STC as a function of A) cell thickness (the red line depicts the weighted RMSE value for the standard Single Diode Fit) and B) Bulk

doping concentration (the red line shows the nominal bulk resistivity of the cell). (For interpretation of the references to color in this figure legend, the reader is

referred to the Web version of this article.)

temperatures of 25, 35, 45 and 55◦C. Light I V

### 3.2. Measured I-V data under ~1 sun illumination at set

and Suns V curves were measured at each temperature. This allowed for the determi OC nation of the series resistance at each temperature, along with a “clean” I V curve by avoiding The second dataset used in this study consisted of measured data any resistance issues from the contact probes. It also provided a direct measurement of the from a single cell in the batch reported by Yu et al. [30]. Testing was total cell series resistance. performed on a Sinton FCT 650 I-V tester. Measurements were taken One issue that was discovered during the process was a non- negligible difference in temperature between the cell and the internal chuck (i.e., set) temperatures. Set temperatures of 25, 35, 45 and 55◦C resulted in *actual* cell temperatures of 24.9 ± 0.1, 33.1 ± 0.2, 40.9 ± 0.5 and 49.9 ± 1◦C, as measured by contact thermocouples. The uncer tainty largely arises from temperature differences from the center to the edges of the cell. The cell used in this work had a stated thickness of 140 μm and bulk resistivity of 1 Ω cm. However, these numbers are almost always nom inal at best. Variations within wafer batches, as well as the impact of the saw damage removal process, can result in variations of 20% or more. In this work, we treated the bulk thickness and doping as fitting parameters for the intrinsic adjusted model and compared the accuracy of the fits obtained. In contrast, because there is no low light data the series resistance is fixed at the measured value. For this fitting we ignore the internal series resistance as per method 3.

**Fig. 6.** PMAX Error and n_RMSE values for single-diode (SD) and intrinsic Fig. 5 presents the weighted RMSE values across the entire dataset as

adjusted (Adj) fits to measured cell I-V data.

**Fig. 7.** A) Conversion efficiency and temperature coefficient of power as a function of diode saturation current and B) Relative change in efficiency as a function of

irradiance for diode saturation currents of 1.5 × 10

- 14

, 2.5 × 10

and 4 × 10

a function of assumed bulk width and doping. The immediate observa tion is that bulk doping had only a very minor effect on fit accuracy. For this device, bulk doping can be safely assumed to be equal to the nom inal value. Interestingly, there would also be no significant loss of ac curacy if a much lower doping concentration was used. If very low doping could be assumed for all devices, it would simplify the fitting process, as well as the implementation of the model within yield simu lation software. In contrast, the assumed width had an observable impact on fit ac curacy. The best result was obtained for an effective bulk thickness of 116 μm. This is less than the nominal bulk thickness but is a plausible value after saw damage etching. The preliminary conclusion from this work is that bulk doping may be neglected as a fitting parameter (and assumed to be equal to the nominal value), while thickness remains important. We therefore used a bulk thickness of 116 μm and a bulk doping concentration of 4.95 × 10 15 cm 3.

Fig. 6 presents both the PMAX error and the n_RMSE values for the

single-diode and intrinsic-adjusted model (single RS) fits to the measured I-V data. There was negligible difference in the ability of the models to predict the maximum power, but the Adjusted model demonstrates n-RMSE values that are a factor of 3 lower than the single-diode model (with the exception of the highest temperature). This is in broad agreement with the trends observed for the simulated data and in PVSyst's recent paper [12].

### 3.3. Consequences of the intrinsic adjusted model

One interesting consequence of intrinsic recombination is its effect on the temperature coefficients and low-light performance. Because Auger recombination depends, to a good approximation, on the third power of the intrinsic carrier concentration, it has a higher temperature dependence than SRH recombination. Fig. 7 presents simulations of the temperature coefficient of power and relative change in efficiency with irradiance for the intrinsic adjusted model as the diode saturation cur rent decreases. This represents improvements in cell technology to remove the remaining sources of SRH recombination. It may be observed that at a certain point, reductions in SRH recombination cease to improve the temperature coefficient, and there is even a slight in crease as Auger recombination becomes the dominant form. In contrast, reductions in saturation current density always act to improve the relative efficiency under low light conditions. This can lead to im provements in energy yield that exceed the simple increase in conver sion efficiency.

## 4. Conclusions

This paper outlines a method for using intrinsic adjusted models to improve the fitting of cell I-V data. In agreement with previous reports, intrinsic models can fit the entire I-V curve more accurately at a range of

A/cm².

temperatures and illuminations. This was demonstrated on both simu lated and measured data. For simulated data, the RMSE values could be reduced by up to an order of magnitude when compared with a single- diode model, while improvements by a factor of 3 were observed on measured data. These models may be applied at either the cell or module level. Importantly, this improvement in RMSE is not solely due to more accurate prediction of the open circuit voltage. The intrinsic adjusted models also demonstrate improved accuracy *near* the maximum power point. This is important when simulating mismatch effects at either a cell or module level. Such models will become increasingly important as mass-produced devices approach the intrinsic limit. Further improvements in fit accuracy may be possible through improved parameterization of the temperature dependence of intrinsic recombination. All studies to date assume that the coefficients for intrinsic recombination do not vary with temperature, which recent reports have found was not the case [31]. This may improve the accu racy of the intrinsic adjusted model to measured data at higher tem peratures as in Fig. 6. Future work will focus on yield simulation using our intrinsic adjusted i_from_v functions at the cell, sub-module and module level. This will include detailed investigations on differences in output when compared to standard single-diode models for current high efficiency devices, particularly under mismatch conditions.

## CRediT authorship contribution statement

**Phillip Hamer:** Writing – original draft, Methodology, Investigation, Data curation, Conceptualization. **Chris Huang:** Validation, Resources, Funding acquisition. **Daniel Chen:** Validation, Resources, Funding acquisition, Conceptualization. **Alison Lennon:** Writing – review & editing, Funding acquisition, Conceptualization. **Bram Hoex:** Writing – review & editing, Supervision, Funding acquisition.

## Declaration of competing interest

The authors declare the following financial interests/personal re lationships which may be considered as potential competing interests: Phillip Hamer reports financial support was provided by Australian Renewable Energy Agency. Phillip Hamer reports financial support was provided by Australian Centre for Advanced Photovoltaics. Phillip Hamer reports a relationship with Foresight PV that includes: equity or stocks. Bram Hoex reports a relationship with Foresight PV that in cludes: equity or stocks. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements authors would like to thank Keith McIntosh and Malcolm Abbot for

assistance with datasheet modelling and manuscript review. They would This work was supported by the Australian Government through the also like to thank Andreas Fell for input regarding the separation of Australian Renewable Energy Agency (ARENA) under Grant TRAC internal and external resistances. 2022/12 and the Australian Centre for Advanced Photovoltaics. The

## Appendix A. Calculation of Carrier Densities

The aim is to determine the intrinsic recombination rates: *Rintrinsic*= *Rrad*+ *RAuger*(A.1)

Where *Rrad*and *RAuger*are the recombination rates for radiative and Auger recombination respectively. From Equations (11) and (12) it is apparent that two main inputs are required to determine *Rintrinsic*. The first is the split in quasi-fermi energy levels (Δ*ϕ*), and fsecondly, there are the carrier concentrations *n* and *p*. Under ideal conditions the split in the quasi-fermi levels can be represented by: Δ*ϕ* = *V* + *JRS*(A.2)

Where *RS*is the series resistance of the device. However, this assumes that all the series resistance elements are *external* to the base silicon material (i.e. in the metal contacts and interfaces). Unfortunately, in a real device there are several *internal* elements of series resistance, such as lateral current transport in the base. An improved description is possible if the internal and external series resistances are separated such that: *RS*= *RS.int*+ *RS.ext*(A.3)

Δ*ϕ* = *V* + *JRS.ext*(A.4)

The split in quasi-fermi levels is also an important input for determining the electron and hole concentrations. The product of these concentrations is given by: (Δ*ϕ*) *np*=*n²i.effeVth* (A.5)

The excess carrier concentration Δ*n* and subsequently**,** both *n* and *p* can be determined as follows: √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ 2 *n₀* + *n₀* 4*np* *IF ND> NA*: *n₀* = *NDNA,* Δ*n* =*, n* = *n₀* + Δ*n, p* = Δ*n* (A.6) 2 √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ 2 *p₀* + *p₀* 4*np* *ELSE IF ND< NA*: *p₀* = *NAND,*Δ*n* =*, n* = Δ*n, p* = *p₀* + Δ*n* (A.7) 2

Where *ND*is the bulk donor concentration and *NA*is the bulk acceptor concentration. Note that this assumes perfect dopant compensation and ionization. This is a reasonable assumption for devices where the dominant doping concentration is less than 3 × 10 16 cm 3 (*>*98% dopant ionization at 300 K for either polarity) [32]. This describes all modern high-efficiency devices. The intrinsic carrier concentration is given by Ref. [33]:

15 1*.*712 *qEg* *n* *i* = 1*.*541 × 10 *T e²kT* (A.8)

The bandgap *Eg*can be determined using the formulation of Passler ¨ [34], with bandgap narrowing as described by Schenk [35]. These equations will not be presented here as they are deeply unpleasant. Interested readers are referred to the cited papers or the bandgap calculator from PVlighthouse [32]. As depicted in Figure A.1 a simplification was made to account for bandgap narrowing due to excess carriers (and hence voltage). It presents the increase in excess carrier density due to bandgap narrowing as a function of excess carrier density, along with a third-order polynomial fit to the data at STC. This approximation is not ideal away from STC and is a potential area for further improvement. Nonetheless this approximation removes the requirement for an iterative process at each data point. We only attempt to adjust for intrinsic recombination in the lightly doped silicon bulk. Auger recombination in heavily doped emitters near the device surface is excluded. This is because this low-injection Auger recombination is both very difficult to determine and has an ideality factor n = 1. This recombination can and has been accounted for as part of standard single-diode models.

**Fig. A.1.** Excess carrier enhancement due to non-equilibrium band gap narrowing. Points were calculated using the band gap calculator on PVLighthouse [32] at

temperatures between 25 and 55◦C. Also presented is the 3rd order polynomial fit used in this work.

Figure A.2 presents the excess carrier density Δ*n* as a function of device voltage for the Quokka simulations of the 26.81% efficient device at STC. Fits to this data are presented for both the single RSand RS.int+ RS.extmethods. Unsurprisingly, the simple equations can only approximate the result from the detailed 3-D device solver. While the carrier densities from the single RSfit is closer to the Quokka values for much of the curve they deviate near open circuit as shown in the inset. This creates a distinct kink in the adjusted I V curves, reducing fit accuracy. In contrast the excess carrier densities from the RS.int+ RS.extfit follow the same trend as the quokka values, with a slight and nearly constant offset. This leads to slightly better fits for the two-resistance model.

**Fig. A.2.** Excess carrier densities as a function of voltage. Curves are presented for the values calculated using Quokka 3 and as determined for the intrinsic adjusted

fitting process used in this paper. The inset zooms in on the data near open circuit.

## Appendix B. Supplementary data

Supplementary data to this article can be found online at [https://doi.org/10.1016/j.solmat.2026.114218](https://doi.org/10.1016/j.solmat.2026.114218) ([https://doi.org/10.26190/unswo](https://doi.org/10.26190/unswo) rks/32001).

## Data availability[5] L.E. Black, D.H. Macdonald, On the quantification of Auger recombination in

crystalline silicon, Sol. Energy Mater. Sol. Cell. 234 (2022) 111428. [6] M.A. Green, Silicon solar cells step up, Nat. Energy (2023), [https://doi.org/](https://doi.org/) Data will be made available on request.10.1038/s41560-023-01296-7. [7] PVLighthouse, SunSolve yield, [https://www.pvlighthouse.com.au/sunsolve-yield/](https://www.pvlighthouse.com.au/sunsolve-yield/),

## References

[8] (n.d.).

S.A. Pvsyst, Pvsyst 8 Help, 2024.
[9] W.F. Holmgren, C.W. Hansen, M.A. Mikofski, Pvlib python: a python package for [1] International Technology Roadmap for Photovoltaics (ITRPV) - 2024 Results, modeling solar energy systems, J. Open Source Softw. 3 (2018) 884, [https://doi](https://doi).

2025. org/10.21105/joss.00884.
[2] M. Green, E. Dunlop, J. Hohl-Ebinger, M. Yoshita, N. Kopidakis, X. Hao, Solar cell [10] A. Bridel-Bertomeu, M. Oliosi, A. Mermoud, B. Wittmer, Limits of the single diode efficiency tables (version 57), Prog. Photovoltaics Res. Appl. 29 (2021) 3–15, model in view of its application to the latest PV cell technologies, in: 40th [https://doi.org/10.1002/pip.3371](https://doi.org/10.1002/pip.3371). European Photovoltaics Specialist Conference, Portugal, Lisbon, 2023. [3] M.A. Green, Z. Zhou, Improved silicon solar cells by tuning angular response to [11] P. Hamer, Z. Haydous, S. Gao, F. Leyland, D. Chen, C. Huang, B. Hoex, Ultra-High solar trajectory, Nat. Commun. 16 (2025) 251, [https://doi.org/10.1038/s41467-Efficiency](https://doi.org/10.1038/s41467-Efficiency) Modules: the end of the single-diode model?, in: 18th PV Performance 024-55681-1. Modeling Workshop Salt Lake City, Utah USA, 2024. [4] T. Niewelt, B. Steinhauser, A. Richter, B. Veith-Wolf, A. Fell, B. Hammann, N. [12] L. Antognini, M. Oliosi, A. Canesse, R. Vincent, A. Mermoud, B. Wittmer, A general

E. Grant, L. Black, J. Tan, A. Youssef, J.D. Murphy, J. Schmidt, M.C. Schubert, S.
approach to model high-performance PV modules for accurate energy yield

W. Glunz, Reassessment of the intrinsic bulk recombination in crystalline silicon,
simulations, in: 42nd European Photovoltaic Solar Energy Conference and Sol. Energy Mater. Sol. Cell. (2022) 235, [https://doi.org/10.1016/j](https://doi.org/10.1016/j). Exhibition, 2025. Bilbao, Spain. solmat.2021.111467. [13] R. Abbassi, A. Abbassi, M. Jemli, S. Chebbi, Identification of unknown parameters of solar cell models: a comprehensive overview of available approaches, Renew.

Sustain. Energy Rev. 90 (2018) 453–474, [https://doi.org/10.1016/j](https://doi.org/10.1016/j). rser.2018.03.011. [14] F. Ghani, G. Rosengarten, M. Duke, J.K. Carson, The numerical calculation of single-diode solar-cell modelling parameters, Renew. Energy 72 (2014) 105–112, [https://doi.org/10.1016/j.renene.2014.06.035](https://doi.org/10.1016/j.renene.2014.06.035). [15] J.C.H. Phang, D.S.H. Chan, J.R. Phillips, Accurate analytical method for the extraction of solar cell model parameters, Electron. Lett. 20 (1984) 406–408. [16] C. Hansen, Parameter estimation for single diode models of Photovoltaic modules, United States, [https://doi.org/10.2172/1177157](https://doi.org/10.2172/1177157), 2015. [17] J. Accarino, G. Petrone, C.A. Ramos-Paja, G. Spagnuolo, Symbolic algebra for the calculation of the series and parallel resistances in PV module model, in: 2013 International Conference on Clean Electrical Power (ICCEP), IEEE, 2013, pp. 62–66. [18] M.G. Villalva, J.R. Gazoli, E.R. Filho, Comprehensive approach to modeling and simulation of photovoltaic arrays, IEEE Trans. Power Electron. 24 (2009) 1198–1208, [https://doi.org/10.1109/TPEL.2009.2013862](https://doi.org/10.1109/TPEL.2009.2013862). [19] W. De Soto, S.A. Klein, W.A. Beckman, Improvement and validation of a model for photovoltaic array performance, Sol. Energy 80 (2006) 78–88. [20] A.P. Dobos, An improved coefficient calculator for the California Energy Commission 6 parameter Photovoltaic module model, J. Sol. Energy Eng. 134 (2012), [https://doi.org/10.1115/1.4005759](https://doi.org/10.1115/1.4005759). [21] N.-P. Harder, J.C. Garcia, Apparent Intensity Dependence of Shunts in PV Modules

- revision of the Shunt Parameterization in the De Soto Model and PVsyst, in: The 41st European Photovoltaic Solar Energy Conference & Exhibition, 2024. Vienna, Austria.
[22] W. Shockley, W.T. Read Jr., Statistics of the recombinations of holes and electrons, Phys. Rev. 87 (1952) 835. [23] R.N. Hall, Electron-hole recombination in germanium, Phys. Rev. 87 (1952) 387. [24] A. Fell, T. Niewelt, B. Steinhauser, F.D. Heinz, M.C. Schubert, S.W. Glunz, Radiative recombination in silicon photovoltaics: modeling the influence of charge carrier densities and photon recycling, Sol. Energy Mater. Sol. Cell. 230 (2021) 111198, [https://doi.org/10.1016/j.solmat.2021.111198](https://doi.org/10.1016/j.solmat.2021.111198).

[25] M.J. Kerr, A. Cuevas, General parameterization of Auger recombination in crystalline silicon, J. Appl. Phys. 91 (2002) 2473–2480. [26] A. Richter, F. Werner, A. Cuevas, J. Schmidt, S.W. Glunz, Improved parameterization of auger recombination in silicon, Energy Proc. 27 (2012) 88–94, [https://doi.org/10.1016/j.egypro.2012.07.034](https://doi.org/10.1016/j.egypro.2012.07.034). [27] J.W. Bishop, Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits, Sol. Cell. 25 (1988) 73–89, [https://doi](https://doi). org/10.1016/0379-6787(88)90059-2. [28] A. Fell, P.P. Altermatt, A detailed full-cell model of a 2018 commercial PERC solar cell in Quokka3, IEEE J. Photovoltaics 8 (2018) 1443–1448, [https://doi.org/](https://doi.org/)

10.1109/JPHOTOV.2018.2863548.
[29] H. Lin, G. Wang, Q. Su, C. Han, C. Xue, S. Yin, L. Fang, X. Xu, P. Gao, Unveiling the mechanism of attaining high fill factor in silicon solar cells, Prog. Photovoltaics Res. Appl. (2024), [https://doi.org/10.1002/pip.3775](https://doi.org/10.1002/pip.3775). [30] C. Yu, K. Gao, C.-W. Peng, C. He, S. Wang, W. Shi, V. Allen, J. Zhang, D. Wang,

G. Tian, Y. Zhang, W. Jia, Y. Song, Y. Hu, J. Colwell, C. Xing, Q. Ma, H. Wu, L. Guo,
G. Dong, H. Jiang, H. Wu, X. Wang, D. Xu, K. Li, J. Peng, W. Liu, D. Chen,
A. Lennon, X. Cao, S. De Wolf, J. Zhou, X. Yang, X. Zhang, Industrial-scale deposition of nanocrystalline silicon oxide for 26.4%-efficient silicon heterojunction solar cells with copper electrodes, Nat. Energy 8 (2023) 1375–1385, [https://doi.org/10.1038/s41560-023-01388-4](https://doi.org/10.1038/s41560-023-01388-4).
[31] L.E. Black, Y. Zhu, Z. Hameiri, D.H. Macdonald, Temperature dependence of Auger recombination in crystalline silicon from 117–463 K, Sol. Energy Mater. Sol. Cell. 295 (2026) 113985, [https://doi.org/10.1016/j.solmat.2025.113985](https://doi.org/10.1016/j.solmat.2025.113985). [32] PVLighthouse, Band gap calculator ([https://pvlighthouse.com.au/bandgap](https://pvlighthouse.com.au/bandgap)), (n.d.). [33] R. Couderc, M. Amara, M. Lemiti, Reassessment of the intrinsic carrier density temperature dependence in crystalline silicon, J. Appl. Phys. 115 (2014). [34] R. Passler, ¨ Dispersion-related description of temperature dependencies of band gaps in semiconductors, Phys. Rev. B 66 (2002) 085201. [35] A. Schenk, Finite-temperature full random-phase approximation model of band gap narrowing for silicon device simulation, J. Appl. Phys. 84 (1998) 3684–3695, [https://doi.org/10.1063/1.368545](https://doi.org/10.1063/1.368545).
