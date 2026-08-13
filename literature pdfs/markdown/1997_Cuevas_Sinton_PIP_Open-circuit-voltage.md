PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5, 79–90 (1997)

### Research

## Prediction of the Open-circuit Voltage of Solar Cells from the

## Steady-state Photoconductance

Andre´ s Cuevas¹ and Ronald A. Sinton² 1 Department of Engineering, Australian National University, Canberra, ACT 0200, Australia 2 Sinton Consulting, 4820 La Fiesta Pl, San Jose, CA 95129, USA

The steady-state photoconductance is a relevant parameter for solar cells. Minority carrier lifetimes, surface recombination velocities, diused region recombination and open-circuit voltages can be determined from an analysis of photoconductance data. Computer simulations of archetypical cases are used here to demonstrate the useful- ness of such an analysis and, in particular, the possibility of predicting device voltages from contactless photoconductance measurements. Simple theoretical models are given to provide physical insight and guide the analysis. A systematic approach is described that permits diagnosis and identification of the dominant recombination mechanisms for a given device structure. # 1997 by John Wiley & Sons, Ltd. Progr. Photovolt. 5: 79–90, 1997.

(No. of Figures: 5. No. of Tables: 4. No. of Refs: 7.)

### INTRODUCTION

he quality of a solar cell, given by its open-circuit voltage, short-circuit current and fill factor, cannot be fully assessed until the fabrication of the device has been completed. While of ultimate

# Timportance, these parameters do not provide information about the physical mechanisms that

determine the performance of the solar cell. Fundamental recombination parameters, including the minority carrier lifetime and the surface recombination velocity, are also of interest to the investigator. The two worlds of engineering and physics are frequently dicult to reconcile and relationships between material parameters and device characteristics are often not established. We present here a simple method that builds a bridge between material and device, fundamental research and applied technology. The method is based on the well-known property of photoconductivity in semiconductors, i.e. the fact that the conductance (the inverse sheet resistance) of a semiconductor changes when exposed to light. The photoconductance is a particularly important parameter for solar cells: it is directly related to the minority carrier lifetime and, on the other hand, it is also intimately related to the open-circuit voltage. It is, therefore, ideally suited to establish a close link between the final device performance and the optimization of the recombination parameters in the material. In addition, the photoconductance under steady or quasi-steady illumination can be measured in a convenient, contactless manner using very simple apparatus and procedures. 1;2

The magnitude of the photoconductance under standard 1-sun illumination conditions could be, in its own right, an appropriate figure of merit for solar cell materials and devices. A certain value of photo- conductance in siemens would not, however, be meaningful for most people. As described in this paper, it

Correspondence to: A. Cuevas, Department of Engineering, Australian National University, Canberra, ACT 0200, Australia.

Contract grant sponsor: Australian Research Council.

CCC 1062–7995/97/020079–12$17.50 Received 23 September 1996 # 1997 by John Wiley & Sons, Ltd. Revised 19 November 1996

1099159x, 1997, 2, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/(SICI](https://onlinelibrary.wiley.com/doi/10.1002/(SICI))1099-159X(199703/04)5:2<79::AID-PIP155>3.0.CO;2-J by Oxford University, Wiley Online Library on [13/07/2026]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

80 A. CUEVAS AND R. A. SINTON

is possible to translate photoconductance values to the more familiar language of minority carrier lifetimes. The meaning of a certain minority carrier eective lifetime is, in a similar way to the photo- conductance, still subject to the specific properties of the semiconductor material being considered, including its doping level and the particular structure and boundary conditions of the sample under test. Looking for a more familiar, less restrictive figure of merit, we focus on the possibility of converting the photoconductance into an open-circuit voltage. Because it is evaluated from the photoconductance and not directly measured, we refer to this voltage as implicit. An obvious advantage of reporting the electronic quality of a sample in terms of the implicit voltage is that it is directly comparable to the final device voltage. In general, we have found a good agreement between the implicit and the actual open- circuit voltages for a number of dierent experimental crystalline silicon devices. 1;2

The prediction of the open-circuit voltage from the photoconductance is straightforward in most cases, but a few precautions must be taken. Computer modelling is used here to illustrate dierent situations and find the corresponding approximate expressions that permit the open-circuit voltage to be predicted accurately. Although the modelling refers primarily to single-crystal or multicrystalline silicon, it shows a method that might also be used for other semiconductor materials. A general applicability of the method is, however, not attempted here. To make the most out of photoconductance measurements, we have also explored the possibility of using them as a tool to diagnose where the dominant recombination mechanisms take place in a given device structure. The use of rear illumination and the use of infrared light are discussed as two possible techniques that can provide additional information and physical insight into the properties of silicon samples.

### RELATIONSHIP BETWEEN PHOTOCONDUCTANCE, EFFECTIVE MINORITY CARRIER LIFETIME AND OPEN-CIRCUIT VOLTAGE

The minority carrier lifetime of a semiconductor material is directly related to its photoconductance. Under steady-state illumination, a balance exists between the generation and the recombination of electron – hole pairs, i.e. JphJrec, expressing them as current densities. As a consequence of this balance, an excess concentration of electrons and holes is established in the material. The total recombination in a sample of thickness W can be conveniently expressed in terms of an average excess minority carrier density, Dnav, and an eective minority carrier lifetime, teff

RW <u>q</u> <u>0</u> <u>Dn dx qDnavW</u> Jph1 t effteff

which essentially is a version of the classic relationship Dn GLteff. The photogenerated excess electron and hole densities, Dn Dp, also result in an increase in the conductance of the sample. The excess photoconductance, i.e. the dierence between the conductance measured under illumination and in the dark, is given by

ZW sLq DnmnDpmpdx qDnavmnmpW 2 0

For many semiconductors the electron and hole mobilities are well known and a measurement of the photoconductance is, therefore, a nearly direct way of probing for the excess carrier density. In general, the excess carrier density is position dependent; the total number of carriers divided by the wafer thickness gives the average carrier density, Dnav, used in Equations (1) and (2). The approximation in Equation (2) assumes that the electron and hole mobilities are approximately constant across the sample and their possible carrier density dependence is accommodated for by evaluating them at the average carrier concentration. Equation (2) should be iterated to find a self-consistent set of values for both Dnav

PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79– 90 (1997) # 1997 by John Wiley & Sons, Ltd.

PREDICTION OF SOLAR CELLS FROM THE STEADY-STATE PHOTOCONDUCTANCE 81

and mnmp, although this iteration is not necessary if the photogenerated excess carrier density is much smaller than the majority carrier density. For monocrystalline silicon, the dependence of electron and hole mobilities on both the dopant density and the injection level can be found in the literature. 3;4 The application of Equation (2) to some materials might not be straightforward; for example, the mobility in some polycrystalline semiconductors might be orientation dependent. Combining Equations (1) and (2), the eective minority carrier lifetime can be determined as

<u>sL</u> t eff3 Jphmnmp

The conductance and the incident light intensity can be measured using a calibrated instrument and a reference solar cell or photodetector, respectively. For a given irradiance, the total photogeneration within the sample Jphcan be easily and accurately estimated using available computer programs⁵ or published tables and graphs. 6 The evaluation of Jphrequires that the absorption coecient and the optical properties of the sample are known. The application of Equation (3) to materials that are not as comprehensively characterized as crystalline silicon might be problematic. This is illustrated by the case of amorphous silicon, for which photoconductance measurements have been used frequently to deter- mine not the lifetime but just the mobility lifetime product. Photoconductance and voltage are both measures of the excess minority carrier density. For a p-n junction solar cell made on a p-type wafer with dopant density NA, the open-circuit voltage can be calculated from the electron and hole densities at the boundary of the space charge region

<u>kT Dn 0 NADp 0</u> Vocln 2 4 q n i

where the photogenerated electron density has been assumed to be much higher than the equilibrium electron concentration, Dn 0 neq; subject to this assumption, Equation (4) is valid for an arbitrary injection level. Note that the local excess minority carrier density, Dn 0, is not, in general, identical to the average Dnavthat can be obtained from a measurement of the photoconductance using Equation (2). The relationship between Dn 0 and Dnavis discussed in the following section.

### COMPUTER SIMULATIONS AND CONCEPTUAL EXPERIMENT

As a representative example, we have considered a p-type silicon wafer with resistivity 1 O. cm and have modelled under a variety of situations its photoconductance and open-circuit voltage using the program PC1D. 5 The sample thickness is 300 mm and its sheet conductance in the dark is 30 mS. It is considered to be illuminated by a standard 100 mW cm 2 AM1.5G solar spectrum. A zero reflectivity has been assumed at the front surface and a 99% reflectivity at the rear; the total number of electron – hole pairs generated in the 300 mm of silicon is, expressed as a current density, 41 mA cm 2. Most of this generation occurs near the front, illuminated surface. The p-n junction, where the open-circuit voltage Vocis evaluated, is located near this front surface. The following subsections discuss dierent possible cases of bulk and surface recombination. For all cases, a strong correlation exists between Vocand the photo- conductance sL, as shown in Figure 1.

#### Baseline case: electronically thin, surface-passivated samples

The most straightforward application of the method described in the previous section is for samples that present a relatively low recombination rate both at the surfaces and in their volume. The resulting minority carrier distribution is approximately uniform and Dn 0 Dnav. One of several dierent possibilities to reduce recombination at the surfaces of a p-type silicon wafer is to perform a light phosphorus diusion followed by the growth of an SiO₂ layer. In our example we have

# 1997 by John Wiley & Sons, Ltd. PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79–90 (1997)

Figure 1. Relationship between the open-circuit voltage and the photoconductance (PC1D computer simulations

for a 1-O. cm silicon wafer; illumination AM1.5G, 100 mW cm 2, 258C)

assumed that the combined recombination in the diused region plus the surface has resulted in a saturation current density J₀ 10 13 A cm 2 (at 258C) at both sides of the wafer. Such an emitter region would permit silicon solar cells to be made with Vocup to 671 mV using high-lifetime wafers. The thickness of the diused region has been made negligible in order to simplify the analysis. A finite emitter thickness does not alter significantly the main results of this modelling exercise. Given these surface boundary conditions, we have considered dierent material qualities with minority carrier lifetimes between 30 and 300 ms, the upper value being representative of the best-quality single- crystal silicon of 1 O. cm resistivity currently available. Table I lists the resulting photoconductances and open-circuit voltages and Figure 2 shows the corresponding excess minority carrier density profiles. Note the sensitivity of the excess photoconductance to the bulk minority carrier lifetime. The open-circuit voltage is determined by the product of the electron and hole densities at the front surface, relative to its equilibrium value n 2i, as described by Equation (4). Since Dn 0 is directly proportional to the photo- conductance, Vocvaries in a logarithmic fashion with sL; this can be seen in Figure 1. In our conceptual experiment we now use the photoconductances calculated with PC1D as the input for the application of the approximate analysis described in the previous section. To evaluate the implicit

Table I. Relationship between the photoconductance and the open-circuit voltage as a function of the bulk minority carrier lifetime (P-type, 1-O cm, 300-mm thick silicon wafer with diused 2

|regions on both sides; illumination AM1.5G, 100 mW cm|||, 258C)||
|---|---|---|---|---|
|J 0:1 pA cm|Computer modelling||Approximate analysis||
|t|s|V|V|t|
|(ms)|(mS)|(mV)|(mV)|(ms)|
|300|5.768|662|660|87|
|100|3.700|652|648|56|
|50|2.380|642|636|36|
|30|1.607|633|626|24|

J 0 front 0 rear 2

b L oc oc implied eff

Figure 2. Minority carrier density profiles as a function of the bulk minority carrier lifetime (see Table I).

The horizontal lines indicate the average carrier density

open-circuit voltage it is necessary to establish a relationship between the excess carrier density at the front junction and the ‘measured’ photoconductance. The simplest approach is to calculate an average carrier density using Equation (2). This Dnavis shown in Figure 2 together with the computer-modelled electron density profiles. Assuming that Dn 0 Dnavis appropriate in situations like the present one, where both the front and rear surfaces are reasonably well passivated and the minority carrier diusion length is considerably higher than the thickness of the sample, L W. The implicit open-circuit voltages, calculated using Equation (4), are in excellent agreement with the ‘exact’ values given by the numerical analysis. The highest error occurs when L and W are comparable, but even in that case it is less than 7 mV, that is, less than 1.5% for a typical silicon solar cell. The eective lifetimes, also given in Table I, have been calculated using Equation (3). The only assumption here has been that the mobility is constant across the sample, which is acceptable if the mobility value corresponding to the average carrier density is used. Note the dierence between the bulk minority carrier lifetime, which characterizes recombination in the volume of the sample, and the eective minority carrier lifetime that results from a photoconductance measurement. Even if the bulk lifetime were infinite, recombination at the two surfaces would limit the eective lifetime to a maximum of about 130 ms in our example. For the case of an essentially flat minority carrier profile, the following relation- ship describes the eective lifetime as a function of the bulk minority carrier lifetime and a recombination term due to the two surface diusions. This relationship assumes that the excess carrier density Dn is much lower than the dopant density NA(low injection)

1 1 J₀ 2 2i NA5 t efftbulkqn W

Only when teffis less than about 10 ms do the surfaces cease to be important in our case study and the measured eective lifetime starts to really reflect the bulk lifetime of the material. Obviously, dierent diusions and surface conditions (dierent J₀) will impose dierent limitations; lower emitter recombina- tion currents (or surface recombination velocities) than those assumed here are within the capabilities of crystalline silicon technology, and eective lifetimes higher than 130 ms can be, and have been, measured for 1-O. cm material.

# 1997 by John Wiley & Sons, Ltd. PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79–90 (1997)

Figure 3. Minority carrier density profiles as a function of the bulk minority carrier lifetime (see Table II).

The rectangles represent the integrated carrier density as the eective diusion length multiplied by Dn 0

It is interesting to realize that, even though the actual bulk lifetime can be dicult to determine unless the recombination at the surfaces can be eliminated or measured independently, the device voltage can be easily and accurately predicted from a measurement of the photoconductance.

#### Electronically thick samples

When the bulk minority carrier lifetime is low, the diusion length becomes smaller than the wafer thickness (L W ), i.e. the sample becomes electronically thick and some precautions in the analysis must be taken. For very low lifetimes the excess photoconductance can be quite small compared to the background level (30 mS in our example). The experimental technique¹ uses a circuit that balances o the dark conductance. The signal level can also be improved by using high intensity illumination, although this entails having to extrapolate the results down to the 1-sun operation.

Figure 3 shows the minority carrier density profiles corresponding to bulk lifetimes of 1–10 ms.

Assuming that Dn 0 Dnavis clearly not appropriate now. It can be noted, however, that the minority carrier density profile has an approximately exponential shape and its integral is approximately equal to Dn 0 L. Accordingly, a better estimate for the prediction of the open-circuit voltage in this case is Dn 0 DnavW =L. The procedure is illustrated in Figure 3, where the area of the rectangle defined by Dn 0 and L is approximately equal to the area circumscribed by the quasi-exponential profile and the abscissa. The results of this approximate procedure are given in Table II, which shows an excellent agreement between the analytical voltages and the exact voltages given by the computer simulation. The minority carrier density profiles would be true exponential functions of the diusion length if the photogeneration occurred strictly at the front surface, a condition that could be obtained experimentally using ultraviolet light. A prediction of the open-circuit voltage under UV light is, however, not repre- sentative of the normal operating conditions of a solar cell and, therefore, is not relevant. The combin- ation of the broad range of wavelengths contained in the solar spectrum and the weak absorption of crystalline silicon for some of them makes the profiles in Figure 3 dier from a pure exponential shape. This is particularly noticeable when the diusion length becomes comparable to or smaller than the average absorption depth of white light. Correspondingly, the error in predicting Vocis larger for very low lifetimes (see Table II). Nevertheless, the unfavourable situation of a diusion length shorter than both the light absorption depth and the sample thickness is not of great practical interest since solar cells

Table II. Relationship between the photoconductance and the open-circuit voltage as a function of the bulk minority carrier lifetime

J 0 frontJ0 rear0:1 pA cm 2Computer modelling Approximate analysis

t bsLVocVoc impliedteffLeff (ms) (mS) (mV) (mV) (ms) (mm)

a

||10||0.610|615|616|9.2|166|
|---|---|---|---|---|---|---|---|
||3||0.192|598|601|2.9|93|
||1||0.065|582|587|0.98|54|
|Dn 0|Dn W =L|has been used to evaluate the implicit voltage.||||||

a a

a av eff

made with low lifetime materials are usually very thin, which can make the simple procedure outlined in the baseline case applicable. Although the correction proposed here is simple and works quite well to predict the voltage, it relies on the knowledge of the minority carrier diusion length. As stressed in the previous section, a photo- conductance measurement provides an eective lifetime and therefore it can only give an eective diusion length, which we define as LeffDteff 1=2, where D is the minority carrier diusion coecient. For the cases discussed here, there is almost no dierence between L and Le.

#### High rear surface recombination

We consider next the eect that a possible high recombination velocity at the rear surface can have on the photoconductance and the predicted open-circuit voltage. To better reveal the eect of the surfaces, a good-quality material with L W is assumed. In such a case, a high recombination rate at the rear surface produces a severe non-uniformity of the carrier density profile, as shown in Figure 4. It is obvious that trying to model this profile with a constant, average electron concentration in order to evaluate the open-circuit voltage is not appropriate. For the simulation shown in Figure 4, crystalline silicon with a minority carrier lifetime of t 300 ms has been assumed. While the saturation current density of the front surface has been kept at

Figure 4. Minority carrier density profiles as a function of the saturation current density of the rear surface

(see Table III) at 258C

# 1997 by John Wiley & Sons, Ltd. PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79–90 (1997)

Table III. Eect of a high recombination at the rear surface on eective lifetimes and predicted voltages

|(bulk minority carrier lifetime t|||300 ms; illumination AM1.5G, 100 mW cm|||, 258C)|
|---|---|---|---|---|---|---|
|J 0:1 pA cm|||Computer modelling||Approximate analysis||
|Rear J₀||s|s front =|V|V|t|
|(pA cm|)|(mS)|s back|(mV)|(mV)|ms|
|0.1||5.768|1|662|660|87|
|0.2||4.445|1.05|656|653|67|
|1||1.995|1.4|640|632|30|
|2||1.464|1.8|635|628|22|
|10||0.971|3.8|629|622|14.7|
|100 ~n W =L|has been used.|0.851|7.0|627|621|12.9|
|13|2||||||

bulk 2

0 front 2

L L oc oc implied eff 2 L

a a a

a Dn 0av eff

J0 front10 A cm, we have modelled cases with rear surface saturation currents 2–1000 times higher. Note that as far as recombination mechanisms are concerned, the rear diused region can be considered to be either n-type or p-type; our analysis applies both to test samples having two n-type diusions and to solar cell precursors in which the front diusion might be n-type and the rear p-type. In low injection conditions, a saturation current density and a surface recombination velocity are interchangeable (J₀ qn 2i =NAS). For example, J₀ 10 13 A cm 2 is equivalent to an eective surface recombination velocity of 85 cm s 1 in 1 O. cm material. The analysis, therefore, also applies to rear surfaces that might be passivated by a dielectric or contacted by a metal. The range of rear surface recombination velocities considered here is from 85 to 10 5 cm s 1, approximately. The assumption that Dn 0 Dnavis still acceptable for moderate rear surface recombination rates, until the rear surface recombination parameter J0rearis approximately 10 times higher than the front one (J0front). As Table III indicates, the error in the voltage prediction is about 8 mV when J0rear1 pA. In fact, this is quite a dicult case to model analytically because the eective diusion length is precisely equal to the wafer thickness for this particular combination of front and rear recombination rates. Note in Table III that the eective lifetime decreases as the rear surface recombination increases; for t eff< 30 ms the eective diusion length becomes smaller than the wafer thickness (LeffW ). A better estimate of the open-circuit voltage is then obtained using Dn 0 DnavW =Leff). The error in the voltage prediction can thus be kept below 7 mV even for extreme situations of rear surface recombination. The rule of thumb of using the smaller of the wafer thickness or the eective diusion length to evaluate the voltage is, therefore, applicable to both the low bulk lifetime case and the high rear surface recombination cases, or a mixture of both. The case of a very high rear surface recombination (together with a high bulk lifetime) is actually quite simple to model even more accurately. The triangular shape of the carrier profile in Figure 4 indicates that Dn 0 2Dnav. If it is expected that the rear surface has a very high recombination rate, e.g. if it is totally unpassivated or contacted by a metal, this approximation would lead to a voltage prediction that is accurate to within 1 mV. This latter procedure applies best to J0 rear> 10 pA, or Srear> 10 4 cm s 1,

i.e. to a rear surface recombination parameter 100 times higher than the front surface one. The analytical Vocis then practically identical to the exact Vocand it has not been necessary to include it in Table III.
### DIAGNOSIS OF RECOMBINATION MECHANISMS

As we have seen, both a low bulk minority carrier lifetime and a high surface recombination velocity can produce a low eective lifetime. It would be desirable, after having found a low teff(such that Leff<W) from a photoconductance measurement, to be able to establish which is the physical mechanism responsible for it. We have identified two additional tests that can provide the desired information.

Figure 5. Ratio between the photoconductances measured under front and rear illumination as a function of the

ratio between the saturation current densities of the two surfaces

#### Diagnosis using rear illumination

A second measurement of the photoconductance illuminating the wafer from the opposite side can reveal a symptom that is characteristic of the case where only one of the surfaces presents a very high recombination rate. The asymmetry in surface recombination translates into a significant asymmetry in the measured photoconductance for light that is strongly absorbed near the illuminated surface. In comparison, a perfectly symmetric sample shows the same photoconductance regardless of which side is illuminated, even if the lifetime is very low.

Figure 5 and Table III show that the asymmetry factor of the photoconductance for front and rear

illumination increases with the level of asymmetry between the two surface recombination rates and is quite noticeable once the ratio between the latter exceeds a factor of 10 (this is precisely the same condition identified in the section on high rear surface recombination to produce Le<W). The example used to illustrate this technique corresponds to a negligible recombination in the bulk; the asymmetry factor is even greater if the high surface recombination rate is compounded with a low bulk lifetime. Although the modelling results shown here correspond to the white light and the standard solar spectrum, the front/rear illumination diagnostic technique can be enhanced by using blue or UV light, which is more strongly absorbed near the illuminated surface.

#### Diagnosis using infrared illumination

An exception to the diagnostic technique discussed above is the case in which both surfaces have a very high (and similar in magnitude) recombination rate. The measured eective lifetime is then quite low and essentially the same photoconductance signal is obtained from either front or rear illumination. It is thus not possible to determine whether the low eective lifetime is due to a low-quality material or to the surfaces from a rear illumination measurement. An additional tool that is particularly useful when both surfaces are unpassivated is the use of infrared (IR) light. By creating an essentially uniform photogeneration rate in the wafer, the significance of the surfaces is reduced and the properties of the bulk are revealed more clearly. Compared to the white illumination case, IR illumination produces an increase in the eective lifetime (or, equivalently, in the photoconductance normalized to the total photogeneration) if, and only if, recombination at both

# 1997 by John Wiley & Sons, Ltd. PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79–90 (1997)

Table IV. Increase in the photoconductance by using infrared illumination in the case where both surfaces are 2

|unpassivated (intensity of IR light is 100 mW cm|||and wavelength is 1100 nm)|||
|---|---|---|---|---|---|
|S 3 10 cm s|White light||Infrared light|||
|t|s|t|s|t|t IR =|
|ms|ms|ms|ms|ms|t (white)|
|300|0.042|0.65|0.067|2.48|3.8|
|30|0.039|0.59|0.061|2.26|3.8|
|3|0.022|0.33|0.034|1.26|3.8|

Sfront rear 6 1

b L eff L eff eff eff

surfaces is the limiting mechanism. If the limitation comes from a low bulk minority carrier lifetime, both IR and white light produce essentially the same result. The computer analysis results in Table IV indicate that, for wafers with a very high surface recombination velocity at both surfaces, the eective lifetime obtained with light of 1100 nm wavelength is about four times higher than the value determined when white light is used. This factor is lower for less extreme surface recombination conditions. The IR test result is significantly dierent from that for white light only when surface recombination is strong enough to make Leff< W. It should be noted that the reference detector should be calibrated at the IR wavelength used, as well as for the standard solar spectrum. Even if it provides a higher sensitivity, the use of IR illumination is not sucient, however, to deter- mine the true bulk lifetime when measuring unpassivated samples. For example, the very high surface recombination velocity of bare silicon (10 5 –10 6 cm s 1 ) limits the maximum detectable lifetime in an unpassivated, 300-mm thick wafer to about 2.5 ms. The Appendix describes several analytical expressions for the eective lifetime that show the limitations imposed by the surfaces. The uniform photogeneration produced by IR light does not present significant advantages over the case of white light for other situations. When at least one surface is well passivated, the eective lifetime is essentially independent of the light spectrum provided that the light is incident on the passivated surface. The open-circuit voltage cannot, in general, be predicted from an IR measurement.

### CONCLUSIONS

Photoconductance measurements give a direct indication of the quality of solar cell materials and devices. If properly interpreted, they are also a powerful tool for device diagnosis. This can be done according to the following systematic procedure:

(i) Initially test the sample using white light. Determine the eective lifetime teffand the eective diusion length, Le. (ii) Compare the eective diusion length to the wafer thickness. If LeffW, the open-circuit voltage

|||eff|
|---|---|---|
|av|eff|oc|
 can be accurately predicted using Equations (2) and (4). (iii) If LeffW, use Dn 0 Dn W =L W to determine V. If you want to find out the physical mechanism for the low eective lifetime, continue to the next step. (iv) Proceed now to check for asymmetry by performing a measurement under rear illumination. If srear< sfront, the reason for the low eective lifetime is that rear recombination is dominant (J0rear> 10J0front). You might, at this stage, predict the voltage more accurately than in step (iii) using Dn 0 2Dnav.
(v) If there is symmetry, perform a third test under IR illumination. If teff IR> teff white, the reason for the low eective lifetime is that both surfaces have a very high recombination. (vi) If LeffW, srearsfrontand teff IRteff white, the dominant mechanism is most likely to be recombination in the bulk of the material.

Note that in case (ii) a separation between surface and bulk recombination is possible if the wafer is in high injection, using methods described elsewhere. 7

The numerical examples shown in this paper refer to crystalline silicon and a particular set of assump- tions, and their validity is not general. Additional modelling and experimental work should be carried out to further assess the applicability of the method to other materials or device structures. These examples show, nevertheless, the main trends and dependencies of the photoconductance with the dierent possible recombination components in a given sample. The methodology proposed here for the analysis and interpretation of photoconductance measurements should be of general interest. In particular, it provides guidance to predict the operating voltage of solar cells in open-circuit conditions.

### APPENDIX: Analytical expressions for photoconductance in the uniform photogeneration case

Determining the photoconductance of a semiconductor sample for the case of a constant generation rate is relatively simple. A practical way to replicate such a generation in practice is, for example, to use a silicon wafer as a filter; a 200-mm thick wafer transmits light in the 1050 –1100 nm range, which is ideal to produce an essentially constant absorption rate in the silicon wafer under test. The analysis starts by solving the continuity equation for electrons (assuming a p-type semiconductor) subject to some boundary conditions at the surfaces. Recombination at the surfaces is characterized by a surface recombination velocity S; as noted in the main text, an alternative characterization can be made in terms of a saturation current density. The excess photoconductance is then obtained by integrating the excess electron density over the thickness of the wafer. Since, for the case of IR illumination, we are interested in studying the limitations due to the surfaces, we assume that bulk recombination is negligible,

i.e. L W, where L is the electron diusion length and W the sample thickness. Analytical expressions that include bulk recombination are also relatively easy to obtain. The following approximate solutions for the photoconductance correspond to dierent situations of front and rear surface recombination conditions. In all the expressions the total photogeneration is expressed as GLW Jph=q, where GLis the constant generation rate.
(i) Identical, finite surface recombination velocity S at both surfaces
<u>W W</u> 2 sLmnmpJphA1 2S 12Dn

(ii) Zero recombination at one surface and finite recombination at the other, Sfront0, SrearS

<u>W W</u> 2 sLmnmpJphA2 S 3Dn

(iii) Zero recombination at one surface, infinite recombination at the other, Sfront0, Srear1

<u>W</u> 2 sLmnmpJphA3 3Dn

(iv) Infinite recombination at both surfaces, SfrontSrear1

<u>W</u> 2 sLmnmpJphA4 12Dn

This expression shows than an IR measurement of the photoconductance in a sample where recombination at both surfaces has deliberately been made very high can be used to measure the electron/hole mobility ratio.

# 1997 by John Wiley & Sons, Ltd. PROGRESS IN PHOTOVOLTAICS: RESEARCH AND APPLICATIONS, VOL. 5: 79–90 (1997)

The eective minority carrier lifetime can be obtained by dividing the photoconductance by Jphmnmp. Perhaps the most interesting case is when SfrontSrear1. The eective lifetime is then

<u>W</u> 2 t effA5 12Dn

It is interesting to note the similarity of Equation (A5) with the expression that gives the eective lifetime measured with a transient photoconductance decay method for this type of sample, teffW 2 = p²Dn. Equation (A5) implies that in a 300-mm silicon wafer with infinite recombination surfaces and an approximate electron diusion coecient Dn30 cm² s 1, the measurable eective lifetime is limited to approximately 2.5 ms. Frequently, even unpassivated surfaces have a finite S, e.g. due to the native oxide that grows on silicon, and higher lifetimes can be measured. According to Equation (A1), a surface recombination velocity of S 10 4 cm s 1 would permit lifetimes up to 4 ms to be measured; S 10 3 cm s 1 would give eective lifetimes up to 17.5 ms, etc. The above expressions are only approximate, since they are based on neglecting any bulk recom- bination. The approximation is reasonable when surface recombination is dominant over bulk recombination; this will be the case if tefftbulk.

Acknowledgement

This work has been partially supported by the Australian Research Council.

### REFERENCES

1. R. A. Sinton, A. Cuevas and M. Stuckings, ‘Quasi-steady-state photoconductance, a new method for solar cell material and device characterization’, Proc. 25th IEEE Photovoltaics Specialist Conference, Washington, 1996., IEEE, New York, 1996, pp. 457 – 460.
2. R. A. Sinton and A. Cuevas, ‘Contactless determination of current – voltage characteristics and minority-carrier lifetimes in semiconductors from quasi-steady-state photoconductance data’, Appl. Phys.Lett., 69, 2510 – 2512, (1996).
3. G. Massetti, M. Severi and S. Solmi, ‘Modeling of carrier mobility against carrier concentration in arsenic-, phosphorus-, and boron-doped silicon’, IEEE Trans. Electron Dev., ED-30, 764 – 769 (1983).
4. F. Dannhauser, Solid State Electron., 15, 1371– 1376 (1972).
5. P. A. Basore and D. A. Clugston, University of New South Wales, Australia, 1996.
6. M. A. Green, Silicon Solar Cells, Centre for Photovoltaic Devices and Systems, USNW, Australia, 1995.
7. D. E. Kane and R. M. Swanson, ‘Measurement of the emitter saturation current by a contactless photo- conductivity decay method’, Proc. 18th IEEE Photovoltaics Specialist Conference, Las Vegas, 1985, p. 578. IEEE, New York, 1985.
