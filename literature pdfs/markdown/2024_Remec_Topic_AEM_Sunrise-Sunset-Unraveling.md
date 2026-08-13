### <u>RESEARCH ARTICLE</u>

**www.advenergymat.de**

# From Sunrise to Sunset: Unraveling Metastability in Perovskite Solar Cells by Coupled Outdoor Testing and

# Energy Yield Modelling

## Marko Remec, Špela Tomšiˇc, Mark Khenkin,* Quiterie Emery, Jinzhao Li, Florian Scheler,

*Boštjan Glažar, Marko Jankovec, Marko Jošt, Eva Unger, Steve Albrecht, Rutger Schlatmann, Benjamin Lipovšek,* Carolin Ulbrich, and Marko Topiˇc*

#### Perovskite-based solar cells exhibit peculiar outdoor performance which is not1. Introduction

#### yet fully understood. The results of outdoor tests may contain hidden, but

The field of photovoltaic (PV) has expe- **valuable information that cannot be fully extracted from measurements alone.** rienced nearly exponential growth in re- **One such phenomenon is the effect of nighttime degradation and the** cent years and the practical power con- **subsequent light-soaking recovery, which can take from a few hours in the** versionefficiency(PCE)limitsofconven- **morning up to the entire day. In this work, long-term outdoor monitoring is** tional single-junction silicon solar cells [ 1] will soon be reached. Further progress **combined with energy yield modeling to qualitatively and quantitatively** in the field can be achieved by utilizing **investigate the effect of light-soaking recovery in both single junction and** emerging halide perovskite-based solar **tandem perovskite-based devices. Following the novel methodology presented** cells(PSCs).Inbothconfigurations–sin- **in this study, it is observed that the light-soaking effect depends not only on** gle junction (SJ) and tandem with a sil- **the daily irradiation but also on the device temperature, and it can be** icon (or other low-bandgap) bottom cell – the PCEs have already reached levels **described using a simple empirical formalism. Incorporating this dependency**[ 1,2] that are viable for commercialization, **into the energy yield model results in an excellent agreement between the** and keep increasing due to the intense **simulated and the measured outdoor data, which allows to perform long-term** research activities in this field. Device **prediction studies. The model estimates that the light-soaking metastability** operational stability remains a concern, **effect decreases the attainable annual energy yield by up to ≈5% for the** but a lot of promising development has been demonstrated recently, [ 3,4] giv- **studied single junction devices, and for tandems by up to ≈3%, depending on** ing grounds for optimism. An impor- **the geographical location, and even more for non-optimal device orientation.** tant next step in technology develop- ment is uncovering the device outdoor stability through field testing, hand in hand with accelerated indoor lifetime testing, and evaluating the

M. Remec, M. Khenkin, Q. Emery, J. Li, F. Scheler, E. Unger, S. Albrecht,
long-term production of (area-normalized) electrical energy —

R. Schlatmann, C. Ulbrich
−2 Solar Energy Division the energy yield (EY; given in kWh m) – under realistic con- Helmholtz-Zentrum Berlin für Materialien und Energie ditionsratherthanthePCEunderstandardtestconditions(STC, 12489 Berlin, Germany i.e., 25 °C, 1000 W m−2, AM1.5G spectrum). E-mail: mark.khenkin@helmholtz-berlin.de Thefirstlong-termoutdoordatasetswithin-situmonitoringof

M.Remec,Š.Tomšiˇc,F.Scheler,B.Glažar,M.Jankovec,M.Jošt,
perovskitesolarcells [ 5–7] andtandemswithsilicon, [ 8–9] werepub-

B.Lipovšek,M.Topiˇc FacultyofElectricalEngineering
lishedinrecentyears.Theyshowtheimportanceofthereversible LaboratoryofPhotovoltaicsandOptoelectronics (ormetastable)processesthatresultinperiodicchangesintheef- UniversityofLjubljana ficiency of PSCs during the day-night cycle.[ 10]One of these phe- Tržaškacesta25,Ljubljana1000,Slovenia nomenaistheso-calledlight-soakingeffect(LSE),i.e.,theprocess E-mail: benjamin.lipovsek@fe.uni-lj.si of nighttime degradation and subsequent performance recovery

The ORCID identification number(s) for the author(s) of this article uponillumination,typicallyinthemorninghoursoftheday.The [ 11] can be found under [https://doi.org/10.1002/aenm.202304452](https://doi.org/10.1002/aenm.202304452) duration of the light-induced recovery can take from minutes [ 12] © 2024 The Authors. Advanced Energy Materials published by up to dozens of hours and strongly depends on the device ar- Wiley-VCH GmbH. This is an open access article under the terms of the chitecture. It was also shown to increase in magnitude with the Creative Commons Attribution License, which permits use, distribution device ageing, [ 13] potentially becoming much more of a problem and reproduction in any medium, provided the original work is properly for aged cells even if they did not show the LSE initially in their cited. fresh state. The physical origin of the LSE in PSCs is still un- **DOI: 10.1002/aenm.202304452** derinvestigation. [ 14] Themostcommonexplanationsinvolveion

*Adv. Energy Mater.*,, 2304452 **2304452 (1 of 10)** © 2024 The Authors. Advanced Energy Materials published by Wiley-VCH GmbH

16146840, 2024, 29, Downloaded from [https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202304452](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202304452) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

migration [ 15–17] trapping/detrapping of charge carriers, [ 18,19] de- fects healing, [ 20,21] and perovskite lattice expansion and strain relaxation [ 22–24] The LSE not only poses a technical challenge for accurate device characterization but also results in the underper- formance of PSCs outdoors for a certain time in the morning. Thedifferenceinmorningandafternoonefficiencyaffectssingle- celldevicesandalsoperovskitemodules. [ 25] Theexactquantifica- tion of LSE during field testing is challenging due to the con- stantly changing outdoor conditions. We will demonstrate, how- ever,thatstate-of-the-artenergyyieldmodellingcanbeharnessed as a powerful tool for LSE extraction and evaluation. MultipleEYmodelsweresuggestedforperovskite-based solar cells [ 26–29] They vary in complexity, depending on the parameters taken into account by the model (irradiance, temperature, solar spectrum, and solar cell electrical performance among others). The purpose of the models was mainly to predict and optimize EY at different geographical locations, [ 29] to compare 2-terminal and 4-terminal tandem devices, [ 30] or to improve light manage- ment by analyzing the effects of textured surfaces. [ 31] To the best of our knowledge, however, no connection with actual outdoor data has been established so far for the purpose of device char- acterization, which – as we will show – is in fact one of the most powerfulusesofenergyyieldmodelling.Namely,whenstudying the impact of nighttime degradation and light-soaking recovery, it is difficult (if not impossible) to isolate and quantitatively eval- uate the extent of the LSE solely from outdoor measurements due to the constantly changing weather conditions. However, by comparing the measured data to the simulated reference device performanceunhinderedbytheLSE,wecanquantifytheenergy harvestingdeficitassociatedwithmetastabilityinrealtimeunder any given weather and installation conditions. And finally, if the simulation model itself is extended by factoring in the observed metastability, long-term forecasting also becomes possible, and assessment of the EY losses associated with the LSE can be per- formed on an annual level. Inthiswork,weperformedlong-termoutdoortrackingofsev- eral PSCs and perovskite-silicon (PK-Si) tandem cells at two ge- ographical locations, in Berlin (Germany) and Ljubljana (Slove- nia). The selected devices that were monitored for up to 2 years exhibit decent long-term outdoor stability, yet are also subjected tothepeculiardiurnalbehaviorassociatedwiththelight-soaking effect,wherethedevicesdegradeoverthenightandthenrecover significantlyfrommorningtonoonorevening,dependingonthe weatherconditions.Bysimulatingtheexpecteddeviceoutputus- ing an in-house developed energy yield model, we obtain good matching between the model predictions and the outdoor mea- surements in the evening hours. However, we systematically ob- servedevicesunderperforminginthemornings,especiallywhen comparing the simulated and the measured voltage at the max- imum power point (*V*MPP), which we attribute to the LSE. From the extent of this difference, the energy losses associated with the observed metastability phenomenon are extracted, quanti- fied, and empirically correlated with the dose of irradiation re- ceived by a cell during the day and the cell temperature (*T*cell). Finally, we incorporate the proposed empirical correlation into the EY model and thus obtain an excellent agreement between simulation and measurements during the whole day. Using the upgradedEYmodel,wepredicttheannualenergyyieldlossesas- sociated with the studied metastability effect in both single junc-

*Adv. Energy Mater.*,, 2304452 **2304452 (2 of 10)**

tion and tandem devices and discuss the implications of device orientation and geographical location.

### 2. Outdoor Data

This work is based on the outdoor performance data of p-i- n perovskite solar cells in a single-junction (SJ) architecture as well as in a PK-Si tandem architecture, all operating at maximum power point (MPP). The single-junction devices, with a perovskite bandgap of *E*G= 1.52 eV, were struc- tured as follows: ITO/ MeO-2PACz / formamidinium lead io- dide (FAPbI₃) perovskite/ LiF/ C60/ SnO₂/ Cu and exhibited an average PCE of 16.6% after encapsulation. Tandems were manufactured using a silicon heterojunction bottom cell and a p-i-n, wide bandgap (*E*G= 1.68 eV) triple-cation perovskite (Cs0.05(FA0.77MA0.23)0.95Pb(I0.77Br0.23)3) top cell with a similar ar- chitecture as described in. [ 32] After encapsulation, an average PCE of 24.2% was measured. The selected device structures are representativeofthehigh-efficiencySJandtandemdevices,with the latter requiring a higher bandgap perovskite that is achieved through compositional engineering. All of the studied solar cells were small-size with an active area of 0.16 cm² (for single junction) and 1 cm² (for tandems). Alldeviceswereencapsulatedbasedontheglass-glasstechnique that uses butyl rubber as an edge sealant and polyolefin (POE) film as an encapsulant [ 10] (refer to the supporting information for details). One FAPbI₃ device in the batch had no POE en- capsulant, only edge sealant – this did not affect its daily behav- ior or long-term performance degradation. Encapsulated devices were mounted on a fixed optimal tilted (35°) stand facing south and connected to a maximum power point tracking system. [ 33] The long-term performance data was recorded in parallel with weather conditions, such as the absolute and spectrally-resolved irradiance in the plane of array and cell temperature (*T*cell). We performed the long-term outdoor measurements on the HZB rooftop test field located in Berlin, Germany (**Figure 1**a)) over the period of October 2020 – June 2023 (33 months or 972 days) for four SJ devices and December 2021 – November 2022 (11 months or 322 days) for four tandem devices. In both cases, these are among the largest datasets available in the literature at the moment. In Figure 1d) the data is represented as aver- aged midday outdoor PCE (PCEoutdoor) values for the devices ex- posed to the outdoor conditions in Berlin. The PCEoutdoorwas calculated based on device power output and absolute irradiance in the plane of array with no temperature or spectral mismatch correction applied in the calculations. The encapsulated SJ de- vices show good outdoor stability, retaining about 65% of the initial PCEoutdoorafter 2.5 years of outdoor exposure. Neverthe- less, seasonal changes in device performance are evident, with increased performance during the summer months and a drop in performance during the winter months. [ 34] Summer decline would have been expected due to no temperature compensation in PCEoutdoorcalculations, however, the trend is the opposite. Ad- ditionally,bycomparingsummer-to-summerpeakPCEoutdoorval- ues,arelativelyslowlong-termdegradationtrendcanbenoticed, showing promise for the long-term stable behavior of perovskite solar cells. The degradation between the winter-to-winter mini- mum is larger in the first year, with little change from the sec- ond to third winter. Tandem devices show an initial increase in

© 2024 The Authors. Advanced Energy Materials published by Wiley-VCH GmbH

**www.advancedsciencenews.com www.advenergymat.de**

**Figure 1.** Experimental outdoor data. a) Rooftop test field in Berlin; area with lab-scale perovskite devices marked with a yellow circle. Example of

encapsulated tandem and single-junction devices mounted on the test fields in b) Ljubljana and c) Berlin. d) Long-term outdoor data for SJ perovskite (green) and PK-Si tandem (blue) devices. Dots represent average midday PCE values of the devices, calculated for irradiances higher than 150 W m−2 (the line serves as guide to the eye). Global irradiance measured in the plane of array (orange) and the temperature of a device (black) are also shown. Black dashed rectangles in d) mark the recording period that was used for EY model validation. Part of the dataset in Figure 1d) (SJ devices; top panel) was extended and adapted from our previously reported data.[ 34]

PCEoutdoorfromspringtosummer,whichislikelyduetoseasonal Inadditiontovariationsinperformanceduetoseasonalityand changesinweather,asobservedinthecaseofsingle-junctionde-long-termdegradation,bothtypesofdevicesalsoexhibitdailyre- vices. However, their performance starts to noticeably degrade versiblechanges–so-calledmetastability,whichisthemainfocus throughout the summer and autumn. High operating tempera-ofthispaper.Instudiedsolarcells,thisphenomenonismostno- tures,currentmismatchchanges,potentialencapsulation-related ticeable in the *V*MPPvalues throughout the day. **Figure 2**a)shows issues, or simply higher doses of irradiation may be among the *V*MPPandirradiancedatafortheFAPbI₃ SJdeviceoverthecourse causes of the observed acceleration in device degradation. Even of four consecutive relatively sunny days, whereas Figure 2b) though the long-term device degradation is noticeable over a demonstratesthe *V*MPPatdifferenttimesoftheday(indicatedby longer period, it is difficult to disentangle the seasonality effects color)asafunctionofincidentirradiance.Weobserveanincreas- from the actual loss of device performance just by using the ex-ing trend in *V*MPPthroughout almost the whole day that is way perimental outdoor data. Only by comparing outdoor data with steeperthanthelogarithmicvoltageincreaseexpectedsolelydue theEYmodelresults,wecanclearlydetectandquantifythelong-to higher irradiance. The comparison of morning and evening term degradation. Although quantifiable, the exact origins of the *V*MPPvaluesatthesameirradianceshowsthattheeveningvalues device degradation are beyond the scope of this paper. Here we are consistently higher than the morning ones, and also that the focus on the relatively stable parts of the datasets (marked with same *V*MPPvalues are repeatedly reached when the cell becomes blackdashedrectanglesinFigure 1d))tovalidateandtrainourEY fully light-soaked. Therefore, the increase of *V*MPP(and, conse- model that includes also short-term diurnal metastable effects. quently, PCEoutdoor) in the morning hours should be regarded as

**Figure 2.** LSE in outdoor data for FAPbI-based SJ perovskite solar cells. The maximum power point voltage (color-coded for the hour of the day) during

several days of observation as a function of a) time and b) irradiance. The irradiance during the corresponding days is shown in yellow.

*Adv. Energy Mater.*,, 2304452 **2304452 (3 of 10)** © 2024 The Authors. Advanced Energy Materials published by Wiley-VCH GmbH

LSE in outdoor data for PK-Si tandem device as well as for the reference single-junction silicon and perovskite cells with the same structure

**Figure 3.**

as the tandem sub-cells. The maximum power point voltage (color-coded for the hour of the day) during several days of observation as a function of a) time and b) irradiance. The irradiance during the corresponding days is shown in yellow.

arecoveryratherthananimprovement–light-soakingduringthe day gradually eliminates the negative effects of nighttime degra- dation and, if weather conditions allow, returns the cell’s perfor- mance to its initial (peak) state. To analyze the metastability behavior in the individual sub- cells of a tandem device, an additional set of outdoor measure- ments was conducted on a rooftop monitoring site of LPVO in Ljubljana (Slovenia). The outdoor measurements were carried out in parallel for the PK-Si tandem device as well as for the single-junction high bandgap perovskite and silicon devices that havetheexactsamestructureasthetandemtopandbottomsub- cell. **Figure 3**a) shows the *V*MPPdata for all three devices over the course of several consecutive sunny days at the beginning of the deviceoperationandFigure 3b)representsthe *V*MPPvaluesatdif- ferent times of the day (indicated by color) as a function of inci- dent irradiance. For the SJ Si solar cell, the *V*MPPis relatively unchanged throughout the day, except for a marginal decrease towards mid- day due to higher operating temperatures. Conversely, the *V*MPP values of the high bandgap perovskite SJ solar cell are affected by the LSE in a qualitatively similar way as shown for the low bandgap SJ FAPbI₃ perovskite device in Figure 2, despite hav- ing a different perovskite absorber. Such metastable behavior is then translated into the operation of the PK-Si tandem device, leading to light-soaking dynamics that are similar to those of the perovskiteSJdevices.Wecanobserveagoodcorrelationbetween the sum of the voltages of PK and Si single-junction devices and the measured *V*MPPof the PK-Si tandem device. In the evening hours, the decrease of *V*MPPoccurs earlier for the PK-Si tandem device than for the other two device types. We attribute this be- havior to the lower value of the shunt resistance (*R*SHUNT) of that particular tandem device compared to the *R*SHUNTof the SJ per- ovskite or Si solar cell. Overall, our outdoor measurements reveal that perovskite- baseddevicesloseaconsiderableamountofenergyinthemorn- ings due to the LSE. The exact extent of losses, however, re- mains unknown, since experimental data alone is not sufficient to separate the light-soaking effect from the effects of constantly changing environmental parameters that also affect the energy

yield of PV devices. For this, the energy yield model that emu- lates the device performance in real-world conditions plays a key role.

### 3. Modelling

Numerical modelling in our work was employed for two specific purposes. Firstly, to extract and quantify the losses associated with the light-soaking effect in any particular PK-based solar cell technology directly from outdoor measurements performed un- der realistic operating conditions. And secondly, to implement the LSE mechanism into the energy yield modelling framework topredict,analyzeandcomparelong-termLSElossesindifferent operating conditions. We used an in-house developed EY algorithm [ 29] that is based on three key modelling approaches (optical, thermal, and electrical). As the input data, we applied realistic optical con- stants of the materials, layer thicknesses, and interface tex- tures, as well as measured device operating temperature (*T*cell) and meteorological data (spectrally resolved global tilted irradi- ance (GTI) and direct normal irradiance (DNI), etc.) acquired on the HZB outdoor PV monitoring site. The electrical be- havior of the device was modelled based on an extensive set of *J*-*V* characteristics measured on a fresh device under well- defined indoor conditions (irradiance/temperature), following the methodology outlined in. [ 29] The measured, fresh device was completely light-soaked prior to each *J*-*V* measurement to factor out any metastable behavior. The optical part of the model was validated for the selected PK-Si tandem devices by comparing the modelled and measured external quantum effi- ciency (EQE) and short-circuit current densities (*J*sc) of the de- vice’s sub-cells under STC conditions (Figure S4, Supporting Information).

**Figure 4** showsthemeasuredandsimulateda)voltage(*V*MPP),

b)short-circuitcurrentdensity(*J*MPP),andc)power(*P*MPP)values at MPP of the investigated PK-Si tandem device over the course ofsixselecteddaysatthebeginningofthedeviceoperationalong withd)theacquiredincidentirradiance(GTI)anddevicetemper- ature(*T*cell).Whilethesimulated(redcurve)andmeasured(blue

**Figure 4.** Measured (blue curve) and simulated (red curve) a) *V*MPP,b)*J*MPP,andc)*P*MPPvalues of the PK-Si tandem device over the course of three

consecutivecloudyandthreeconsecutivesunnydays.d)Measuredtotalincidentirradiance(yellowarea)anddeviceoperatingtemperature(blackcurve) for the six selected days.

*Adv. Energy Mater.*,, 2304452 **2304452 (5 of 10)** © 2024 The Authors. Advanced Energy Materials published by Wiley-VCH GmbH

Daily energy generation losses of the tandem device attributed to the LSE effect over the course of three consecutive weeks. Also plotted are

**Figure 5.**

the daily irradiation (orange curve) and the daily average of device temperature (black curve).

curve) *J*MPPvalues in Figure 4b) show a good agreement, there is anotablediscrepancybetweenthesimulatedandmeasured*V*MPP and, consequently, also *P*MPPvalues (although less visible due to alargerspanofthe*P*MPPvertical axis). On cloudy days, the mea- sured *V*MPPvalues are lower than the simulated ones through- out the whole day. On sunny days, however, the measured val- ues deviate from the simulated ones only in the morning hours but match closely in the afternoon. We attribute this VMPPdif- ference to the LSE, since during the second half of each sunny daywhenthedeviceisfullylight-soaked,themeasurementsover- lap with the simulations. This good agreement between the re- sults obtained for fully light-soaked cells indicates the validity of our EY modelling approach, which allows us to calculate, at any given operating conditions, the predicted (ideal) power gen- eration of the device without any degradation or metastability effects.

**3.1. LSE Extraction and Quantification** IdealEYsimulationresultsincomparisontoactualoutdoormea- surements can be used to extract and quantify the extent of the LSE losses during the device operation. The results in Figure 4c)
show that energy losses are substantial in low irradiance condi- tions,amountingtoaround12%forthethreecloudydaysshown. On sunny days, however, when the device is fully light-soaked in the afternoon hours, the losses are significantly lower, totaling approximately 2% over the selected three days. The same methodology can be used also for longer time peri- ods of the outdoor operation. **Figure 5** shows the daily losses at- tributedtotheLSEoverthecourseofthreeweeks(beforeanysig- nificantirreversibledegradationofthedevicecouldbeobserved). The daily sum of the incident irradiance (daily irradiation) and thedailyaverageofdevicetemperature(*T*cell)arealsoplotted.The results show that over the course of these three weeks, the LSE lossesreducethetotalachievablegeneratedenergyobtainedwith theEYmodelby6%.Again,itcanbeobservedthatthelossesvary from day to day, but are closely correlated with the device oper- ating conditions, with larger LSE losses observed on days with lower daily irradiation and lower device temperature.

## 3.2. LSE Modelling

To predict the amount of LSE losses in different environmen- tal and installation cases, the LSE mechanism needs to be

|Figure 6. a) The difference between simulated and measured V||results (ΔV|
|---|---|---|
|(H). With the increasing cumulative irradiation H|, the difference between the simulated and measured V||
|ΔV results for five selected days (March 7|–9 ,11 and 12|). The average daily operating temperature of the tandem device (T|

MPP cum cum MPP th th th th

MPP) of the PK-Si tandem cell as a function of the cumulative irradiation MPPapproaches 0 V. b) A smaller set of *cell*) is also stated.

**Figure 7.** Measured (blue dots) and ideal simulated (red curve) *V*MPPvalues of the PK-Si tandem device over the course of six days in March 2022. For

better visualization, the *V*MPPdata are presented from 1 V onwards. Also shown are the modelled *V*MPPvalues that include light-soaking effect obtained by using Equation (1) (green curve; *A* = 0.2 V, ***𝝉*** = 1.5354 kWh m−2) and Equation (2) (orange curve; *A* = 0.2 V, *B* = 6.99*107(kWh m−2)−1, *E*a=

0.4616 eV) as well as measured device operating temperature and incident irradiance. implemented into the EY modelling algorithm. We selected sev-the device temperature. Indeed, this can already be observed in eraldaysinMarch2022andcalculatedthedifferencebetweenthe Figure 4a)forsunnydays,wheremeasuredresultsbegintoagree simulated and measured *V*MPP(Δ*V*MPP= *V*MPP,sim– *V*MPP,meas). with the simulations at different times each day, despite almost Foreachdatapoint,wealsocalculatedthecumulativeirradiation identicalirradianceconditions.Weattributethistothedifference *H*cum(*t*) that was intercepted by the tandem device from sunrise in daily *T*cellprofiles. We selected and replotted a smaller set of
∑ *t* 1200 nm previouslypresented Δ*V*MPPresultsthatrepresentsfivedayswith uptothegiventimeofday: *H*cum(*t*) = ( ∫ *GTI*(*𝜆*) *d𝜆*)⋅Δ*t*, very similar irradiance conditions, yet notably different LSE dy- *sunrise* 300 nm where *𝜆* is the wavelength of the incoming light, *t* represents the namics, as clearly shown in Figure 6b). It can be noticed that data point’s time of day and Δ*t* denotes the measurement res-Δ*V*MPPdeclinesfasterathigheraveragedailyoperatingtempera- olution. The relation between Δ*V*MPPand *H*cumis presented in ture(*T*cell;thecalculatedvaluesareindicatedinFigure 6b)),show-

**Figure 6**a). As expected, with increasing cumulative irradiation ingthattheLSEisacceleratedbythetemperature.Followingthis

*H*cumthe cell becomes more and more light-soaked, and the dif-observation,weupgradedEquation(1)sothattherateconstant *𝜏* ference between the simulated and measured *V*MPPapproaches varies with temperature according to the Arrhenius equation,[ 35] 0V. as given in Equation (2), where *k*Brepresents the Boltzmann Fortheinitialapproximation,thecorrelationbetweentheLSE-constant: induced voltage deficit Δ*V*MPPand cumulative irradiation can be − <u>H</u> <u>cum 1</u> −<u>Ea</u> modelled by fitting the data points presented in Figure 6a) with Δ*V* = *Ae𝜏*; = *Bek*B *T*cell(2) MPP *𝜏* an exponential decay function (black line):

− <u>H</u> <u>cum</u>Once again, constants *A*, *B*,and*E*awere selected to best fit Δ*V*MPP= *Ae𝜏*(1) thedatapointsinFigure 6b),andthemodelwasimplementedin our EY algorithm. The simulated *V*MPPresults obtained by using The comparison between the measured (blue dots) *V*MPPand the upgraded model are presented in Figure 7 (orange curve) to- simulated (green curve) values with LSE is presented in **Figure 7** gether with previous results. A much better agreement with the togetherwithsimulated *V*MPPvalueswithoutLSE(redcurve)and experimental values can now be observed in all cases, demon- device operating conditions. While an improvement in agree-strating the importance of including *T*cellin the LSE model. The mentisachieved,thereareneverthelesssignificantdiscrepancies remaining small discrepancy between the model and measure- betweentheresultsincertainconditions,presumablystemming ments can be attributed to other factors, for example, the spread from the scattered points around the fit in Figure 6a). of measured MPP values due to changing environmental con- It was shown in previous reports, [ 17,23] that under STC con-ditions, or the impact of the history of device conditions longer ditions, the LSE is affected not only by irradiation but also by than just one day. However, we did not investigate these factors

**Table 1.** Summary of numerical results for both solar cells and for each of the four geographical locations from distinct KGPV zones.[ 36]Tabulated are

the yearly EY values with and without LSE as well as the relative energy losses associated with the effect.

|Solar cell|PK-Si tandem|PK single-junction|
|---|---|---|
|Orientation|optimal vertical|optimal|
|Location EY without LSE|EY with LSE LSE losses EY without LSE EY with LSE|LSE losses EY without LSE EY with LSE LSE losses|
|[kWh m −2]|[kWh m −2] [%] [kWh m −2] [kWh m −2|] [%] [kWh m −2] [kWh m −2] [%]|
|Panama 463.2|457.1 1.3 161.6 155.3|3.9 313.4 307.0 2.0|
|Denver 524.4|511.6 2.4 317.2 305.2|3.8 341.5 328.4 3.8|
|Atlanta 477.8|468.7 1.9 252.1 243.5|3.4 319.3 309.7 3.0|
|Columbus 420.0|406.9 3.1 239.8 228.1|4.9 280.8 266.9 4.9|

*Adv. Energy Mater.*,, 2304452 **2304452 (7 of 10)** © 2024 The Authors. Advanced Energy Materials published by Wiley-VCH GmbH

a) The relative distribution of the calculated location-specific yearly LSE losses over different months of the year for the PK-Si tandem solar cell
**Figure 8.**

in optimal and vertical open-rack configuration as well as for the PK single-junction solar cell in optimal orientation. b) The absolute distribution of the location-specific monthly LSE losses for the PK-Si tandem solar cell.

further since we wanted to keep the model relatively simple, and especiallysincethediscrepancybetweenthesimulatedandmea- sured generated energy is already less than 0.25% for the case of the selected six days and less than 0.8% for the case of the ex- tended period of three consecutive weeks (Feb 18 th –Mar12 th ). AsimilarlygoodagreementforSJFAPbI₃ PKsolarcellisshown in (Figure S5, Supporting Information). It should be noted that the presented analysis was performed foratimeperiodwherethedevices(bothtandemandSJ)didnot show any irreversible degradation. However, under prolonged outdoor operation, solar cells are subjected to different degrada- tion mechanisms which also affect the LSE dynamics and thus the parameter values used in Equation (2). In this contribution, we focused only on the metastability detection, quantification, andmethodologyofitsinclusionintotheenergyyieldmodel.The irreversible degradation and its influence on different aspects of the device outdoor operation, including the light-soaking effect, go beyond the scope of this contribution and will be regarded in future work.

### 4. Analysis of Long-Term LSE Losses

Finally, the comprehensive EY modelling algorithm upgraded with LSE metastability was used to study the long-term energy losses in different environmental conditions (geographical lo- cations). The LSE dynamics was modelled according to Equa- tion (2), where it was assumed that the parameters of the decay functions do not change in time. No other degradation mecha- nisms beyond LSE were taken into consideration. WeanalyzedthefollowingtwoPVdevices,a)thecompletePK- Si tandem solar cell investigated in the previous section, and b) a high bandgap triple-cation single-junction PK solar cell that represents the top sub-cell of the tandem device. Four North America-based geographical locations were selected from dif- ferent climate zones according to the Köppen-Geiger (KGPV) classification [ 36] (zonedesignationsareprovidedinparentheses): Panama(AH),Denver(CH),Atlanta(DH),andColumbus(DM). Theselectedzoneshaveverydifferentenvironmentalconditions and cover a large area of the USA as well as Europe. All relevant meteorological data (spectrally-resolved GTI and DNI, ambient

temperature, wind speed) were obtained from the National So- lar Radiation Database [ 37] for each installation of the devices. It should be noted that Berlin, from where the outdoor measure- ments presented in previous sections were acquired, belongs to the DL KGPV climate zone. The latter has similar environmen- tal conditions to the DM zone, however it has even lower yearly insolation and ambient temperatures. TheextentoftheLSElossesforeachofthetwodevicesandfor eachoftheselectedlocationswasfirstevaluatedonayearlybasis. Both devices were studied in optimal location-specific open-rack orientation, whereas for the case of the tandem cell also verti- calconfigurationwasconsidered.Theresultsaresummarizedin

**Table 1**. For the case of optimal orientation, it can be observed

thatminimalLSElossesareachievedinPanamaforbothdevices (1.3% for the tandem and 2.0% for the single-junction device). This was expected since Panama represents a location with rel- atively high insolation and ambient temperature throughout the whole year. Both influence the LSE dynamics in a favorable way from the device performance viewpoint. In contrast, the device installed in Columbus would experience nearly 3 times higher yearly LSE losses (3.1% and 4.9%, respectively) due to the less favorable conditions;, i.e., less sun and lower temperature. In all cases,wenoticethattheLSElossesaremuchlowerinthetandem device, although both cells experience the same LSE dynamics. The reason for this is in the bottom Si sub-cell, which in a PK- Sitandemdevicecontributesone-thirdofthetotaloutputenergy and does not exhibit LSE. The results corresponding to the ver- tical configuration show that even without considering the LSE, the generated energy of the tandem cell is reduced by more than 40% in all selected locations due to a decrease in incoming solar energy. Theyearly LSElosses are increased accordingly, which is especially notable in the case of Panama (3 times higher) since thedifferencebetweentheoptimal(13°)andthevertical(90°)in- clinationofthedeviceisthelargestthere.Denverhasthesmallest difference between the inclination angles and thus the smallest increase in yearly LSE losses. Due to the pronounced influence of the LSE dynamics on the environmental conditions, it is expected that the seasonal varia- tions also affect how LSE losses are distributed over the year. To confirm and further investigate this phenomenon, we calculated

therelativedistributionofyearlyLSElossesoverthemonths.The results are presented in **Figure 8**a) for the PK-Si tandem solar cellinoptimalandverticalopen-rackconfigurationaswellasfor the SJ PK solar cell in optimal orientation (refer to Figure S6, Supporting Information for absolute distribution of yearly LSE losses over the months). In all three device-type/installation cases, we get a very similar relative distribution of losses regard- less of the geographical location. Moreover, the practically iden- tical relative distribution also applies to the devices installed in seasonal conditioned climates, represented by Denver, Atlanta, andColumbus.Theresultsforthesethreelocationsindicatethat duringwintermonths,thecontributiontototalyearlylossesis ≈ three times higher compared to the summer months due to sig- nificantlylowerinsolation,whichisdirectlyrelatedtothecombi- nation of total irradiance and ambient temperature. By contrast, sincePanamaislocatedneartheequator,theseasonalvariations in environmental conditions are very small, which results in a near-uniform relative distribution of LSE losses. Finally, the extent of LSE losses can also be evaluated on a monthly basis, which can be important for season-based inves- tigation and optimization of device operation. For this purpose, we calculated the ratio between the energy lost due to the LSE and the ideal energy generated within each month, as plotted in Figure 8b) for the PK-Si tandem device. For each selected geographical location except Panama, it is evident that in winter thedevicecanloseanotableamountofthepotentiallygenerated energy due to LSE. This is especially evident for Columbus (Lat. 40° N),whichisageographicallocationwithadistinctlyseasonal conditionedclimate.WithmonthlyLSElossesofover8%inwin- ter,theyaremorethanseventimeslargerthanthoseinsummer.

### 5. Conclusion

Reliableoutdooroperationofperovskite-basedsolarcellwithim- proved long-term stability is crucial for the industrialization of thetechnology;however,reportsofthoroughoutdoortestingand in-depth analysis of the results are still lacking. In this work, we demonstrated long-term (several months up to 2.5 years) out- door monitoring data of several single-junction perovskite and perovskite-silicon tandem devices under MPP conditions. Both typesexhibitedpromisingstability,especiallySJdeviceswith65% of the initial PCEoutdoorretained after 2.5 years of testing. In both types of devices, however, a peculiar behavior can be observed in the morning hours, particularly on cloudy days, where the solar cell performance is at first lower than expected, but then gradu- ally recovers to the initial STC performance during the day un- dersunlight.Weattributethistothemetastableprocessofnight- time degradation and the subsequent light-induced recovery of the perovskite material, which is known as the light-soaking ef- fect, LSE. To extract the parameters of LSE from outdoor measure- ments, we applied a state-of-the-art EY model calibrated with the specifics of fresh, fully light-soaked SJ and tandem solar cells thatservedastheLSE-freereferencetowhichthemeasureddata arecompared.Thisenabledustoquantifytheenergyproduction lossesassociatedwiththemetastabilityinaPK-Sitandemdevice operating in real-world conditions in Berlin over the course of three consecutive weeks, which amount to a total of 6%. Addi- tional analysis of the results revealed that the voltage drop and

the rate of recovery associated with the LSE depends on the daily cumulative irradiation as well as the operating temperature, and all three parameters can be empirically interconnected using an Arrhenius equation. In the final part of our study, we incorporated the empirical relation of the LSE dynamics into our EY model, which allowed us, for the first time, to model long-term real-world device operation by taking the effects of the studied metastability fully into account. Using the upgraded EY model, we analyzed the energy harvesting losses associated with the LSE over the course of one typical meteorological year, for different types of devices operatingindifferentgeographicallocationsandindifferentori- entation/installation cases. Results showed that, depending on the location/climate, yearly LSE losses can amount to up to 3% in an optimally oriented PK-Si tandem solar cell, and monthly even up to 8%. This not only highlights the notable impact of LSEandthenecessity foritsaccurateevaluation, butalsoreveals that in geographic regions with pronounced seasonal variations, wintertime performance of perovskite-based solar cells can be significantly lower than summertime performance – contrary to conventional PV technologies. With the presented methodology of combined outdoor measurement and EY modelling, both can be easily evaluated, leading to faster development of perovskite solar cells on their road towards commercialization.

### Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

### Acknowledgements

M. R. and Š. T contributed equally to this work. The authors thank the Helmholtz Association for fundingthe project TAPAS (Tandem Perovskite And Silicon solar cells—Advanced optoelectrical characterization, mod- elling and stability) within the EU partnering program. C.U. and R.S. ac- knowledge the support by the Helmholtz Association,Germany under the program “Energy System Design”. The authors acknowledge the finan- cial support from the Slovenian Research Agency (program P2-0415 and project J2-1727). Š.T. also thanks the Slovenian Research Agency for her Ph.D. funding. Open access funding enabled and organized by Projekt DEAL.
### Conflict of Interest

The authors declare no conflict of interest.

### Data Availability Statement

The data that support the findings of this study are available from the cor- responding author upon reasonable request.

### Keywords

energy yield modelling, light-soaking effect, outdoor monitoring, perovskite-based solar cells, realistic operating conditions

Received: December 22, 2023 Revised: April 19, 2024 Published online: May 9, 2024

[1] “Best Research-Cell Efficiency Chart.” [Online]. [https://www.nrel](https://www.nrel). gov/pv/cell-efficiency.html,July**2022**. [2] M. A. Green, E. D. Dunlop, G. Siefer, M. Yoshita, N. Kopidakis, K. Bothe, X. Hao, *Prog. Photovolt. Res. Appl.***2023**,*31*,3. [3] X. Zhao, T. Liu, Q. C. Burlingame, T. Liu, R. Holley, G. Cheng, N. Yao,

F. Gao, Y.-L. Loo, *Science* **2022**,*377*, 307.
[4] Q. Jiang, R. Tirawat, R. A. Kerner, E. A. Gaulding, Y. Xian, X. Wang, J.

M. Newkirk, Y. Yan, J. J. Berry, K. Zhu, *Nature* **2023**,*623*, 313.
[5] M. Jost, B. Lipovsek, B. Glazar, A. Al-Ashouri, K. Brecl, G. Matic, A. Magomedov, V. Getautis, M. Topic, S. Albrecht, *Adv. Energy Mater.* **2020**,*10*, 2000454. [6] Q. Emery, M. Remec, G. Paramasivam, S. Janke, J. Dagar, C. Ulbrich,

R. Schlatmann, B. Stannowski, E. Unger, M. Khenkin, *ACS Appl.* *Mater. Interfaces* **2022**,*14*, 5159.
[7] J. Li, J. Dagar, O. Shargaieva, O. Maus, M. Remec, Q. Emery, M. Khenkin, C. Ulbrich, F. Akhundova, J. A. Márquez, T. Unold, M. Fenske, C. Schultz, B. Stegemann, A. Al-Ashouri, S. Albrecht, A. T. Esteves, L. Korte, H. Köbler, A. Abate, D. M. Többens, I. Zizak, E. J.

W. List-Kratochvil, R. Schlatmann, E. Unge, *Adv. Energy Mater.***2023**, *13*, 2203898.
[8] M. Babics, M. De Bastiani, E. Ugur, L. Xu, H. Bristow, F. Toniolo, W. Raja, A. S. Subbiah, J. Liu, L. V. Torres Merino, E. Aydin, S. Sarwade,

T.G. Allen,A. Razzaq, N. Wehbe, M.F. Salvador,S.De Wolf, *Cell Rep.* *Phys. Sci.***2023**,*4*, 101280.
[9] M. De Bastiani, E. Van Kerschaver, Q. Jeangros, A. Ur Rehman, E. Aydin, F. H. Isikgor, A. J. Mirabelli, M. Babics, J. Liu, S. Zhumagali,

E. Ugur, G. T. Harrison, T. G. Allen, B. Chen, Y.i Hou, S. Shikin, E. H. Sargent, C. Ballif, M. Salvador, S. De Wolf, *ACS Energy Lett.***2021**,*6*,
2944.
[10] M. V. Khenkin, A. K. M., I. Visoly-Fisher, Y. Galagan, F. Di Giacomo,

B. R. Patil, G. Sherafatipour, V. Turkovic, H.-G. Rubahn, M. Madsen,
T. Merckx, G. Uytterhoeven, J. P. A. Bastos, T. Aernouts, F. Brunetti,
M. Lira-Cantu, E. A. Katz, *Energy Environ. Sci.***2018**,*11*, 739.
[11] C. Zhao, B. Chen, X. Qiao, L. Luan, K. Lu, B. Hu, *Adv. Energy Mater.* **2015**,*5*, 1500279. [12] M. V. Khenkin, A. K. M., I. Visoly-Fisher, S. Kolusheva, Y. Galagan, F. Di Giacomo, O. Vukovic, B. R. Patil, G. Sherafatipour, V. Turkovic, H.

G. Rubahn, M. Madsen, A. V. Mazanik, E. A. Katz, *ACS Appl. Energy* *Mater.***2018**,*1*, 799.
[13] L.Jiang,J.Lu,S.R.Raga,J.Sun,X.Lin,W.Huang,F.Huang,U.Bach,

Y.i-B. Cheng, *Nano Energy* **2019**,*58*, 687.
[14] L. Lin, L. Yang, G. Du, X. Li, Y.-N. Li, J. Deng, K. Wei, J. Zhang, *ACS* *Appl. Energy Mater.***2023**,*6*, 10303. [15] B. Roose, *RSC Adv.***2021**,*11*, 12095. [16] J. Herterich, M. Unmüssig, G. Loukeris, M. Kohlstädt, U. Würfel, *En-* *ergy Technol.***2021**,*9*, 2001104.

[17] B. Li, M. Lin, C. Kan, P. Hang, Y. Yao, Z. Hu, Y. Wang, Y. Zhang, W. Zhong, D. Yang, X. Yu, *Sol. RRL* **2022**,*6*, 2200050. [18] J. Peng, Y. Sun, Y. Chen, Y. Yao, Z. Liang, *ACS Energy Lett.* **2016**, *1*,

1000.
[19] B.Cai,X.Yang,Z.eYu,Y.Liang,Y.uShan,A.Hagfeldt,L.Sun, *J.Power* *Sources* **2020**,*472*, 228506. [20] E. Mosconi, D. Meggiolaro, H. J. Snaith, S. D. Stranks, F. D. Angelis, *Energy Environ. Sci.***2016**,*9*, 3180. [21] J. Wang, X. Duan, W. J. Yin, *J. Phys. Chem. Lett.***2021**,*12*, 9328. [22] H. Tsai, R. Asadpour, J. C. Blancon, C. C. Stoumpos, O. Durand, J. W. Strzalka, B.o Chen, R. Verduzco, P. M. Ajayan, S. Tretiak, J. Even, M.

A. Alam, M. G. Kanatzidis, W. Nie, A. D. Mohite, *Science* **2018**,*360*,
67.
[23] X. Wu, J. Ma, M. Qin, X. Guo, Y. Li, Z. Qin, J. Xu, X. Lu, *Adv. Funct.* *Mater.***2021**,*31*, 2101287. [24] X. Zhang, S. H. Wei, *Phys. Rev. Lett.***2022**,*128*, 136401. [25] T. J. Silverman, M. G. Deceglie, I. R. Repins, T. Zhu, Z. Song, M. J. Heben,Y.Yan,C.Fei,J.Huang,L.T.Schelhas, *IEEEJ.Photovolt.***2023**, *13*, 740. [26] J. Lehr, M. Langenhorst, R. Schmager, S. Kirner, U. Lemmer, B. S. Richards,C.Case,U.W.Paetzold, *Sustain. Energy Fuels* **2018**,*2*,2754. [27] R. Schmager, M. Langenhorst, J. Lehr, U. Lemmer, B. S. Richards, U.

W. Paetzold, *Opt. Express* **2019**,*27*, A507.
[28] P.Tillmann,K.Jäger,A.Karsenti,L.Kreinin,C.Becker, *Sol. RRL* **2022**, *6*, 2200079. [29] Š. Tomšiˇc, M. Jošt, K. Brecl, M. Topiˇc, B. Lipovšek, *Adv. Theory Simul.* **2023**,*6*, 2200931. [30] M. T. Hörantner, H. J. Snaith, *Energy Environ. Sci.***2017**,*9*, 1983. [31] F. Gota, R. Schmager, A. Farag, U. W. Paetzold, *Opt. Express* **2022**,*30*, 14172. [32] A. Al-Ashouri, E. Köhnen, B. Li, A. Magomedov, H. Hempel, P. Caprioglio, J. A. Márquez, A. B. Morales Vilches, E. Kasparavicius,

J. A. Smith, N. Phung, D. Menzel, M. Grischek, L. Kegelmann, D. Skroblin, C. Gollwitzer, T. Malinauskas, M. Jošt, G. Matiˇc, B. Rech, R. Schlatmann, M. Topiˇc, L. Korte, A. Abate, B. Stannowski, D. Neher,
M. Stolterfoht, T. Unold, V. Getautis, S. Albrecht, *Science* **2020**,*370*,
1300.
[33] H. Köbler, S. Neubert, M. Jankovec, B. Glazar, M. Haase, C. Hilbert, M. Topic, B. Rech, A. Abate, *Energy Technol.* **2022**, *10*, 2200234. [34] M. Khenkin, H. Köbler, M. Remec, R. Roy, U. Erdil, J. Li, N. Phung,

G. Adwan, G. Paramasivam, Q. Emery, E. Unger, R. Schlatmann, C. Ulbrich, A. Abate, *Energy Environ. Sci.***2023**,*17*, 602.
[35] S. Arrhenius, *Z. Für Phys. Chem.***1889**,*4*, 96. [36] J. Ascencio-Vásquez, K. Brecl, M. Topiˇc, *Sol. Energy* **2019**,*191*, 672. [37] M. Sengupta, Y. Xie, A. Lopez, A. Habte, G. Maclaurin, J. Shelby, *Re-* *new. Sustain. Energy Rev.***2018**,*89*, 51.
