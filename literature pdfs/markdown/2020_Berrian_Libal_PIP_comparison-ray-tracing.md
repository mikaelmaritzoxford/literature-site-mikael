Received: 19 June 2019 Revised: 4 January 2020 Accepted: 11 February 2020 DOI: 10.1002/pip.3261

### <u>EU PVSEC PAPER</u>

**A comparison of ray tracing and view factor simulations of locally resolved rear irradiance with the experimental values**

**1,2 1,3**

## Djaber Berrian Joris Libal

1Module Development, International Research Center Konstanz, Rudolf-Diesel-Str. 15, **Abstract** Konstanz, 78467, Germany One of the prerequisites for a reliable energy yield prediction of bifacial photovoltaic 2Albert-Ludwigs-Universität Freiburg, Fahnenbergplatz, Freiburg im (PV) systems is the capability of modeling the backside irradiance of those systems Breisgau, Germany with high accuracy. Currently, the most important optical models used to quantify the 3Advanced Solar Cell Concepts,International reflected irradiance on the backside of a bifacial solar panel are view factor and ray Research Center Konstanz, Rudolf-Diesel-Str. 15, Konstanz, 78467, Germanytracing. The MoBiDiG simulation tool has been developed at ISC Konstanz uses the view factor (VF) concept to model the rear irradiance. In addition to the VF concept, **Correspondence** Djaber Berrian, Module Development, ray tracing (RT) has been adopted to determine the backside irradiance of bifacial International Research Center Konstanz, modules by using the open-source tool bifacial_radiance that has been developed Rudolf-Diesel-Str. 15, 78467 Konstanz, Germany. by the National Renewable Energy Laboratory (NREL). A customized monocrystalline Email: djaber.berrian@isc-konstanz.de; silicon solar panel has been built in order to evaluate the accuracy of the existing djaber.berrian@imtek.uni-freiburg.de optical models by locally resolved rear irradiance measurement. The performance **Funding information** of rear irradiance has been investigated along the rows of the customized PV The project has been funded by the EC (Horizon 2020) and by the German BMWimodule during sunny and cloudy days with typical back irradiance values of ≈50 and (FKZ 0324088A) within the Solarera.net ≈ 150 W∕m². The comparison of measured and modeled data has been carried project ‘‘Bifalo’’, Grant/Award Number: FKZ 0324088Aout on hourly, daily, and monthly basis, and the results show lower deviations for solar cells located in the center of the PV module than on the edge. Moreover, the concept of decisive solar cells has been introduced and applied to both measured and modeled data, solar cells located in the center rows were found to act as the most decisive solar cells. Finally, considering the installation configuration studied here, ie, bifacial mounting with low clearance height (below 0.2 m), both hourly RT and VF approaches are able to model long-term cumulative irradiance received by decisive solar cells with a very high accuracy ranging from ±0.5% to ±2%.

**KEYWORDS** albedo, bifacial modules, modeling, prediction, PV systems, simulation, ray tracing, view factor

locations are needed to further evaluate the existing simulation mod- **1 INTRODUCTION** els. Currently, the most important optical models used to quantify the The potential of bifacial photovoltaic (PV) systems over their monofa- irradiance on the backside of a bifacial solar panel are view factor (VF) cial counterpart—either fixed tilt or tracking—in terms of energy yield and ray tracing (RT). A comparison of simulated and measured irradi- has been widely proved by pilot installations as well by simulations.1,2 ance has been carried out using 2D VF with an unlimited shed approach However, the accuracy of energy yield prediction of bifacial PV systems is largely debated, which makes the bankability of bifacial as well as RT in Hansen et al,3where two reference solar cells were technology uncertain to some extent¹; as a result, more experiments used on the top and bottom at the backside of bifacial PV modules, and dealing with bifacial PV systems at various installation conditions and the measurement was done during one day, with an accuracy of 5%

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. © 2020 The Authors. Progress in Photovoltaics: Research and Applications published by John Wiley & Sons, Ltd. *Prog Photovolt Res Appl*. 2020; :609–620. wileyonlinelibrary.com/ journal/ pip

<u>BERRIAN AND LIBAL</u>

being reported. Chiodetti⁴ also used single calibrated pyranometers to measure the backside irradiance on an extended stand of PV mod- ules and compare it to that of modeled values found by 2D VF, and a deviation of 3% to 5% has been achieved during 1 week of measure- ment. The assessment of 2D VF and RT in comparison with measured backside irradiance during two consecutive days at the same time of day has been shown in Pelaez et al,5and the rear irradiance was mea- sured by four irradiance sensors mounted along the slope of the solar panel, where the 2D VF model has shown a better agreement to the measured data points than has RT for the mounting height of 0.15 m. The MoBiDiG simulation tool has been developed by ISC Konstanz, which uses VF concept6,7to model the rear irradiance; ie, the rear irradiance is determined for each cell within the backside of PV module, unlike for the 2D VF, which is more suitable for large PV systems and is able to calculate the irradiance change along a direction that is perpendicular to the unlimited rows. In addition to VF concept, RT has been adopted in the current work to determine the backside irradiance of bifacial modules. We used the open-source tool bifacial_radiance that has been developed by the National Renewable Energy Laboratory (NREL).8The bifacial_radiance has specific functions that use Radiance RT software to create scenes for bifacial PV systems.9Previous bifacial validations used RT with cumulative sky approach, which is a method used to produce annual irradiation results from a single simulation, and hence, the simulation time is reduced significantly; however, this generates additional inaccuracies as reported in Robinson and Stone¹⁰; since the accuracy is of the essence for the current work, we have used RT with hourly resolved simulations. It is worth mentioning that modeling a stand-alone bifacial PV system will allow us to find out to what extent the optical models are able to model the edge effect (the variation of the rear irradiance along the rows from east to west for equator oriented mounting), while in large bifacial systems, the edge effect will be much smaller.

### 2 RESEARCH METHODOLOGY AND PROCEDURE

This research consists of simulations and experimental validation of simulation results obtained by existing simulation tools for rear irradi- ance modeling of bifacial PV systems. In the first step, a customized rear irradiance panel (as described in the following subsections) has been built and installed in outdoor conditions to measure rear irradi- ance values. In parallel, weather and irradiance data have been acquired by sensors that are located in the field nearby the mounted PV mod- ule. These weather and irradiance data have been used as inputs to the simulation tools to simulate the rear irradiance values. The qualitative and quantitative approaches have been used to compare measured and simulated results at different time resolutions (hourly, daily, and monthly). In the following subsections, the description of the research procedure is reported.

### 2.1 REAR IRRADIANCE OPTICAL MODELS

VF11-14and RT15,16models were used to model the back irradiance of bifacial PV modules, and the aforementioned optical models have been also used in the current work in order to model the rear side

**FIGURE 1** Geometrical parameters in order to calculate the

irradiation leaving the area (A₁)reachingarea(A₂) separated by a distance of S and having different orientations from their normal vector n₁ and n₂ [Colour figure can be viewed at wileyonlinelibrary.com]

irradiance received by solar cells mounted on a customized PV module. VF is known also as form factor, a shape factor, and a configuration factor, used often to solve heat transfer problems such as quantifying the amount of irradiation leaving one surface (*A₁*) reaching another surface (*A₂*) with different geometrical orientation (*𝛼*1 and *𝛼*2)through adistance(*S*) as shown in Figure 1. For the current work, the ground surface is assumed to be a Lambertian reflector, which means an isotropic scattering of irradiance by the surface regardless of the nature of the incident irradiance.13 In addition, VFs have analytical or numerical solutions¹⁷ depending on the problem that has to be solved. The VF model has been used by the MoBiDiG simulation tool, and the detailed description of that model has been discussed in our previous work.7,18We recall the most important equation in our irradiance model that counts for the ground reflected irradiance received by the rear side of the bifacial module in order to show the most important dependencies:

*E* ref,rear= *𝜌* × GHI × *FA*nsh→*A*m+ *𝜌* × DHI × *FA*sh→*A*m*,* (1)

with*𝜌*being the albedo of the ground surface, GHI the global horizontal irradiance, and DHI the diffuse horizontal irradiance. In Figure 2B, a schematic drawing of a stand-alone PV module is shown as a side view. Because of the shade beneath the bifacial modules, the model requires a separate calculation of two VFs: the VF from nonshaded areas *FA*nsh→*A*mand the VF from shaded areas *FA*sh→*A*m to the module back surface. Since the shadow position and shape change as a function of time, the VF from the shadow region has to be calculated continuously for each timestamp. In optics, RT is used to render objects by tracing many rays of light from the source to the object (forward RT) or from the object 8 to the source (backward RT). The bifacial_ radiance tool (based on 9 the backward RT), which uses the open-source software Radiance in order to model the rear irradiance received by solar cells, has been used in the current work for the RT approach. More details on how Radiance is used to model the rear irradiance of bifacial PV modules can be found in Asgharzadeh et al. A scene of the PV module under study has been created by bifacial_radiance, and an example is shown in Figure 2. On the one hand, RT requires more computation time than VF does to complete

**FIGURE 2** A,Frontsideofasceneofa

stand-alone photovoltaic (PV) module generated from Radiance on 21 September at 10:00 in Konstanz. B, Side view of the same scene [Colour figure can be viewed at wileyonlinelibrary.com]

irradiance simulations; on the other hand, the RT approach is claimed to be able to model complex geometries of PV systems such as shades caused by mounting structure and objects surrounding PV systems. However, in this work, the shading due the racking is not taken into account neither by VF nor by RT. It is worth mentioning that both VF and RT are using the Perez model²⁰ in order to account for diffuse irradiance distribution on the sky. The optical models studied in this paper need as inputs the time series data, which are as follows: the global horizontal irradiance (GHI), the diffuse horizontal irradiance (DHI), and the albedo. The variable albedo has been used because a previous work has shown an improved accuracy due to variable albedo in comparison with the mean measured albedo.4Other time-independent inputs are the meshing size of the solar panel, ie, the number of irradiance values to be calculated per PV module, and the geometrical configuration. The main output of the optical models is the time series of the modeled rear irradiance values. The inputs and outputs data are summarized in ablockdiagraminFigure3.

### 2.2 CUSTOMIZED REAR IRRADIANCE SOLARPANEL

A customized silicon solar panel with the size similar to that of the solar panel of 60 cells (ie, dimensions: 1.66 m × 1.0 m) has been made at ISC Konstanz, which we named as rear irradiance solar panel (RISP) and will be used as a measurement device in order to compare the locally resolved rear irradiance data found by the existing optical models with the experimental results. The module has glass on the front side, a black back sheet of polyethylene terephthalate (PET) on the backside, and ethylene-vinyl acetate (EVA) material as an encapsulant. The black back sheet has been chosen in order to avoid having other sources

**FIGURE 3** Block diagram summarizes

the inputs and outputs of rear irradiance optical models. DHI, diffuse horizontal irradiance; GHI, global horizontal irradiance

**TABLE 1** Summary of the bill of materials

**Layer Material Type Thickness, mm** Glass Float glass 3,1 Encapsulant front EVA 0.450 Cells Standard 0.200 (p-type monofacial) Encapsulant back EVA 0.450 <u>Black back sheet PET 0.220</u>

Abbreviations: EVA; ethylene-vinyl acetate; PET, polyethylene terephthalate.

of light such as internal reflections or transmitted light through the gaps to the ground. A summary of the bill of materials used are shown in Table 1, and a photograph of the customized RISP is shown in Figure A1 in the Appendix. In addition, a very-high-precision temperature sensor (PT1000) has been laminated to the backside of the center solar cell within the PV module in order to report measured cell temperature and correct the irradiance values accordingly. The RISP is able to measure 30 cells at different positions as shown in Figure 4. Monocrystalline solar cells made by Motech Industries, Inc, have been used to make the customized solar panel. Each solar cell of the rear irradiance PV module has an individual terminal; ie, they are not connected in series as usually known for commercial solar panels. In this way, we are able to measure the *I*sc(short-circuit current) of each cell separately, and through indoor calibration (*I*∕*V* character- ization), we determine the equivalent irradiance of each cell. Figure 5 shows short-circuit currents of solar cells measured indoor at Stan- dard Test Conditions (STC) (1000 W/m² at AM1.5 and 25 ◦

C) using the
h.a.l.m flasher with an uncertainty in short-circuit current of ±0.016%

**FIGURE 4** The sketch shows the rear

irradiance map of the customized solar panelaswellasthepositionsofcellswith and without data acquisition. ‘‘C’’ stands for cell [Colour figure can be viewed at wileyonlinelibrary.com]

**FIGURE 5** Short-circuit currents of the

calibrated solar cells under STC conditions, which have been used for rear irradiance determination [Colour figure can be viewed at wileyonlinelibrary.com]

and A+++ class. The solar simulator was calibrated to an ISE Fraunhofer one-cell monocrystalline Cs-Si PV module. It is worth mentioning the backside irradiance measured in outdoor conditions was determined based on the short-circuit current of each solar cell under STC conditions instead of using an averaged value of short-circuit currents. This is mainly important to exclude any variance in rear irradiance between cells due to indoor calibration. The calculated variance in short-circuit currents shown in Figure 5 is

0.013 A. The measured data were collected every 5 minutes in 1 month. In order to determine the measurement uncertainty of the RISP, one solar cell from the same batch (ie, featuring very similar *I*∕*V* characteristics) as the solar cells used to build up the RISP has been mounted on the horizontal position to measure the GHI next to a high-accuracy commercial pyranometer for the entire period, and the results of calibrated solar cell were within agreement of ±3% (see Figure A2 in the Appendix) with the pyranometer measurement. Hence, we assume
that the solar cells within the RISP have a measurement uncertainty of ±3%. For the first use of the RISP, we were able to monitor 14 positions (solar cells) out of 30 positions as shown in Figure 4. The RISP was mounted on the flat rooftop at ISC Konstanz as a stand-alone PV module as shown in Figure 6. The front side of the module (the glass side) is looking towards the ground in order to measure the amount of irradiance received by each solar cell of the module. A photograph of the backside, as well as the mounting structure, is shown in Figure 7. As it is shown in Figure 3, we used as input for the optical models the installation configuration as well as the irradiance data (GHI and DHI), which have been collected by the meteorological instruments at the test site at ISC Konstanz for a period of month during September 2018, the site of which is located at 47.66 N9.18E.

- ◦
Another important input for the optical models is the albedo, which was measured on the site by two calibrated monofacial monocrystalline

**FIGURE 6** The rear irradiance solar

panel mounted on the roof of ISC Konstanz. The mounting configuration and the geometrical parameters such as tilt angle, clearance height, and orientation are shown [Colour figure can be viewed at wileyonlinelibrary.com]

**FIGURE 7** A photograph shows the

backside of the rear irradiance photovoltaic (PV) module as well as the racking system [Colour figure can be viewed at wileyonlinelibrary.com]

**TABLE 2** Summary of rows height above the

ground **Row Number Height Above the Ground, m**

10.19 2 0.28
30.44 4 0.53
<u>50.61</u>
solar cells mounted on a horizontal position (one looks upwards and other looks downwards), elevated at 1-m height; the ratio of short-circuit current measured by these two solar cells defines the albedo. A white sheet has been placed underneath the RISP to enhance the albedo; the mean measured albedo of the white sheet during 1 month is 50% as shown in the histogram in Figure 8. The uncertainty of the albedo measurement is ±2%. For the modeling purposes, the area of the RISP is meshed into 60 elements using the optical models, and for each element, the corresponding rear irradiance is simulated. The results presented either measured or modeled are hourly averaged data unless otherwise stated.

**FIGURE 8** Frequency distribution of measured albedo values for

1 month of September 2018. Approximately 50% is the mean measured albedo [Colour figure can be viewed at wileyonlinelibrary.com]

### REAR IRRADIANCE PERFORMANCE ON

### SUNNY AND CLOUDY DAYS

We used the measured data set from the RISP to analyze the perfor- mance of rear irradiance along the rows of different heights. We have

**FIGURE 9** The rear irradiance received by each row during a sunny

day (12 September 2018). Around noon, the bottom rows (rows 1 and 2) produce higher irradiance than the top row (row 14). The center rows (rows 3 and 4) produce the lowest irradiance [Colour figure can be viewed at wileyonlinelibrary.com]

chosen cells from the center columns (columns 5 and 6) as shown in

Figure 4 in order to represent the back irradiance of each row, which

is situated at different heights as it is summarized in Table 2. This meansthatcellsC3,C4,C8,C9,andC14representrows1,2,3,4,and 5, respectively. Figure 9 shows the back irradiance measured for each row as a function of the hour during a sunny day (low diffuse fraction). As can be seen, the rows have virtually the same irradiance in the early morning and late evening; however, around noontime (10:00 to 14:00), the irradiance discrepancy between rows becomes visible. For this scenario, the bottom rows (row 1 and row 2) produce higher back 2 irradiance (*>*140 W/m) than the top row (row 5), while the center rows (rows 3 and 4) observe the lowest back irradiance (approximately 120 W/m²). There are several factors that affect how much irradiance is received by a row, such as the distance of the row to the ground, the view angle of the row to the sky, and whether or not the ground portion viewed by the row is under shade. For the analyzed scenario, the row-to-ground distance increases along the rows (see Table 2), and the view angle of a row to the sky increases along the rows; ie, row 5 has a higher view angle to the sky than row 1. The results of Figure 9 show that row 1 yields the highest rear irradiance. This is because row 1 is closer to the ground than other rows, and in this situation (with a clearance height of 0.15 m), the area located directly beneath row 1 has no shade as can be seen in Figure 6. Row 5 had higher back irradiance than the center rows even though row 5 is farther from the ground than the center rows, and this can be explained by the fact that row 5 has a higher view angle to the sky and sees less shaded area on the ground than the center rows do, even though they are closer to the ground. Another behavior was captured in Figure 9: it is the overlap seen between row 3 and row 4 before and afternoon. Row 3 receives higher rear irradiance than row 4 before noon, and in the afternoon, this relationship becomes exactly the opposite. The reason behind this behavior is the position of the self-shaded area on the ground during the day. Before noon, the self-shadow cast of the RISP is located in the western side of the module, which gives row 3 (represented by cell 8) the advantage of viewing more area on

**FIGURE 10** The rear irradiance received by each row during a

cloudy day (4 September 2018). The irradiance received by a row increases uniformly along the rows from the bottom to top row [Colour figure can be viewed at wileyonlinelibrary.com]

the ground without shade than row 4 (represented by cell 9). In the afternoon, the self-shadow cast of the RISP is located in the eastern side; hence, this time, row 4 has the advantage of viewing less shaded area on the ground than row 3. The behavior of back irradiance has been also analyzed on a cloudy day and shown in Figure 10. Unlike the sunny day, the rear irradiance received by a row increases uniformly along the rows from the bottom row (row 1) to the top row (row 2

5). Approximately 120 and 20 W/m have been recorded around noon as the highest and lowest back irradiance during the cloudy day, respectively. In a cloudy day, the influence of shaded area on the ground on the rows is reduced a lot since the light is mostly diffuse (ie, very small portion of direct light); in this case, the effect of the viewing angle of a row to the sky dominates in terms of rear irradiance generation by a given row. Therefore, the uniform increase seen in back irradiance is related to the uniform increase of viewing angle to the sky from row 1 through row 5.
### 4 VALIDATION OF REAR IRRADIANCE

### OPTICAL MODELS

In this section, a comparison of simulated results using the optical models (VF and RT) to the measured data of the RISP device is analyzed and discussed on hourly, daily, and monthly basis.

Figure 11 shows the results of measured and modeled back irra-

diance of each row as a function of the hour of the day. As can be seen, in comparison with measured results (red dotted line), both VF (blue solid line) and RT (green solid line) have well modeled the trend of back irradiance over the day and for all rows. VF models better the back irradiance at early hours (from 7 AM to 10 AM) than the RT model does. It has been also seen that the discrepancy between mea- suredandmodeledvaluesishigharoundnoontimeandespeciallyat late hours of the afternoon for both RT and VF. The discrepancy seen between the measured and modeled values from around 5 PM to 6 PM is highly possible because of the shade cast by nearby objects (cabling and ISC building) located on the western side of the RISP device; these shades are not taken into account within the optical models; the black dotted line in Figure 11 shows when the interference of those artifacts

**FIGURE 11** Measured and modeled back irradiance using view factor and ray tracing for each row of the rear irradiance photovoltaic (PV)

module as a function of time on 12 September 2018. A-E, The results for rows 1 through 5, respectively. RT, ray tracing; VF, view factor [Colour figure can be viewed at wileyonlinelibrary.com]

**FIGURE 12** Measured and modeled

accumulated rear irradiance during 1 day (12 September 2018) as well as the corresponding deviations between measured and modeled data for each row and model. RT, ray tracing; VF, view factor [Colour figure can be viewed at wileyonlinelibrary.com]

starts; accordingly, the data points corresponding to the timestamps RT failed to model row 3 as good as the other rows. The comparison after 5 PM have not been taken into account for the validation on between the back irradiance modeled by VF (blue solid line) and RT daily and monthly bases. It is also seen in Figure 11 that both VF and (green solid line) has shown a good match at the early and late hours

**FIGURE 13** Measured and modeled

accumulated rear irradiance during 1 mo (September 2018) as well as the corresponding deviations between measured and modeled data for each row and model. RT, ray tracing; VF, view factor [Colour figure can be viewed at wileyonlinelibrary.com]

of the day. However, around noon (when the irradiance is high), the RT model yields higher back irradiance than the VF model. ThebarchartinFigure12showstheaccumulatedmeasuredand modeled (VF and RT) back irradiance of each row during one day, as well as the corresponding deviation between the measured and modeled values for each optical model including the measurement uncertainty. Both RT and VF models have shown a good agreement to the measured data (see Figure 12). That is, rows 1, 2, and 5 have higher accumulated back irradiance (approximately 870 Wh) than rows 3 and 4 (approximately 720 Wh). As can be also seen, the deviation between the measured and modeled data depends on the row for a given optical model. The highest deviation (∼±6%) is recorded for row 1—which is very close to the mounting rack—using both RT and VF; this deviation is possibly due to reflection and shading caused by the racking, which is not taken into account in the optical models. It is also observed that the relative deviations of the VF model show a slope as a function of rows. Similar to the results that are presented in Figure 12, we show in

Figure 13 the measured and modeled accumulated back irradiance

for a period of 4 weeks including cloudy and sunny days. Overall, the trend has been well modeled by VF and RT. In comparison with VF, RT has overestimated the irradiance of row 1. The VF model has shown less deviation than RT for most of the rows for 1 month. The

lowest deviation has been recorded for the center rows (rows 3 and

4), which is very important for a better prediction of the overall energy yield of bifacial PV systems as it is discussed and demonstrated in the following paragraphs. In practice, solar panels, including bifacial ones, are made up of cells connected in series. Therefore, the overall energy yield of a bifacial solar panel is limited by the cell with the lowest current, ie, the lowest irradiance. We call ‘‘a decisive solar cell’’ a solar cell that—out of all solar cells of the 60 cell matrix of the solar module—has the lowest irradiance for a given timestamp. In order to find out which solar cells act as decisive, we have proceeded in two steps, as follows:
- **** We calculate for each timestamp (ie, every 5 min) and for a period of 1 month the frequency of cell *X* of being the decisive solar cell.
- **** Each time the decisive solar cell is found, we add up its irradiance value and weight out the frequency calculated in step 1. We have applied steps 1 and 2 on the measured and modeled data set, taking into account the uncertainty of the measured data. It is important to note that the measured data set had only 14 cells (as shown in Figure 4) from which decisive solar cells are determined, while the modeled data have been created for 60 cells using the optical model (VF) for the same time period as the measured data set. VF from the MoBiDiG tool has been chosen as the optical model for this purpose

because it is possible to model data with the minutewise timestamp, while RT from bifacial_radiance tool can model only hourlywise data. The heat map plots in Figure 14 show that the solar cells behave like a decisive solar cell found through measurement using the RISP device and with optical modeling using VF. The frequency is normalized and represented in a color bar: the darker the color, the higher the frequency of a given solar cell of being decisive. We can observe the consistency in Figure 14. In Figure 14A,B, both measured and modeled approaches predicted that row 4 has decisive solar cells. In addition, C5 and C9 are very close solar cells to each other and have shown the most decisive solar cells by measurement and modeling, respectively. As can be in seen Figure 14A,B, the cells in rows 1, 2, and 5 do not act as decisive solar cells; this finding has been confirmed by both approaches. C1 is found by measured data to produce frequently low irradiance and has been excluded as, according to the optical modeling, this is not possible since C1 is located on the bottom and sees most of the time no shade. The possible reason for C1 producing low irradiance is racking and some artifacts nearby the western side of the RISP, which intercept the reflected irradiance from the ground to reach C1. The main difference between the modeled and measured approach in terms of decisive cells is that cells C5 and C8 in row 3

**FIGURE 14** Heat maps show the position of

decisive solar cells during September 2018. The dark red solar cells act most of the time as the decisive solar cell. A, Decisive solar cells found by measurement. B, Decisive solar cells found by modeling [Colour figure can be viewed at wileyonlinelibrary.com]

have been found by measured data to act sometimes as decisive solar cells, while the modeled data do not predict that. Combing the findings of Figure 14A,B, the solar cells (C5, C6, C8, C9, and C12) that are in rows 3 and 4 and located within the rectangle shown in Figure 14A have been deemed as the most decisive solar cells. The bar chart plot of Figure 15 shows the accumulated rear irradiance of the decisive solar cells measured and modeled as well as the relative deviation of each optical model. The agreement between measured and modeled data in terms of the trend as a function of decisive solar cells is well seen in Figure 15. Interestingly, the deviation of decisive solar cells is very low, from ±0.5% to ±3%, and both VF and RT models tend to underestimate slightly the accumulated irradiance of decisive solar cells, whereby the VF model has shown less relative deviation than RT for the 1-month data. The low relative deviation of the modeled data of decisive solar cells in comparison with measured data is particularly important for the accurate prediction of overall energy yield production of the bifacial solar panel. The root-mean-square deviations of each measured and modeled solar cell are summarized in Table A1 in the Appendix.

**FIGURE 15** Measured and modeled

accumulated rear irradiance during 1 mo (September 2018) for the most decisive solar cells as well as the corresponding deviations between measured and modeled data for each model. RT, ray tracing; VF, view factor [Colour figure can be viewed at wileyonlinelibrary.com]

### 5 CONCLUSION

We have presented results of a comparison of VF and RT simulations for locally resolved rear irradiance with the experimental data. A customized rear irradiance PV module has been made as a device for assessing the accuracy of existing optical models as well as for analyzing the lateral distribution of rear irradiance. The PV module has been mounted on the flat roof of ISC Konstanz with a clearance height of 0.15 m. The rows along the PV module receive the back irradiance differently during sunny and cloudy days. It is found that for a sunny day, the bottom rows collect more back irradiance than the center rows, while during a cloudy day, the rear irradiance received by a row increases uniformly from the bottom to the top row. The hourly validation of the optical models (VF and RT) has shown a good agreement apart from increased discrepancy around noontime. It is also found that the deviation between measured and modeled results becomes smaller as we move from hourly to daily to monthly validations. Both measured and modeled data reported that rows 1, 2, and 5 have higher back irradiance than the other rows. The concept of decisive solar cells has been introduced, and it is concluded that for a 6 × 10 solar panel with the roof mounting configuration investigated in the present study, solar cells located in rows 3 and 4 act as the most decisive solar cells, hence the accurate energy yield prediction of the PV module rely on the good modeling of those solar cells. For

the installation configuration studied here, ie, bifacial mounting with low clearance height, both hourly RT (ie, none cumulative RT) and VF models are able to model the rear irradiance of the decisive solar cells for the long term with a very high accuracy ranging from ±0.5% to ±2%. In a future publication, we will study the impact of the clearance height on the accuracy of VF- and RT-based optical models.

**ACKNOWLEDGMENTS**

This work has been funded by the EC (Horizon 2020 Framework Pro- gramme) and by the German BMWi (Bundesministerium für Wirtschaft und Energie FKZ 0324088A) within the Solar-era.net project ‘‘Bifalo.’’

**ORCID**

*Djaber Berrian* [https://orcid.org/0000-0003-4608-4978](https://orcid.org/0000-0003-4608-4978)

**REFERENCES**

1. Kopecek R, Libal J. *Bifacial Photovoltaics: Technology, Applications and* *Economics*: Inst Eng Technol; 2018.
2. Liang TS, Pravettoni M, Deline C, Stein JS, Kopecek R, Singh JP, et al. A review of crystalline silicon bifacial photovoltaic performance characterisation and simulation. *Energy Environ Sci*. 2019;12(1):116-148.

3. HansenCW,SteinJS,DelineC,MacalpineS,MarionB,Asgharzadeh
A. Analysis of irradiance models for bifacial PV modules. *IEEE Pvsec*. **How to cite this article:** Berrian D, Libal J. A comparison 2016:138-143.
of ray tracing and view factor simulations of locally resolved

4. Chiodetti M. *Bifacial PV plants: performance model development and*
rear irradiance with the experimental values. *Prog Photovolt* *optimization of their configuration*: M.S. Thesis, KTH Royal Institute of *Res Appl*. 2020;28:609–620. <u>[https://doi.org/10.1002/pip.3261](https://doi.org/10.1002/pip.3261)</u> Technology, Stockholm, Sweden; 2015.

5. Pelaez SA, Deline C, MacAlpine SM, Marion B, Stein JS, Kostuk RK. Comparison of bifacial solar irradiance model predictions with field validation. *IEEE J Photovoltaics*. 2018:17.
**APPENDIX A**

6. Shoukry I. Master of science thesis bifacial modules—simulation and experiment, Stuttgart University; 2015.
7. Berrian D, Libal J, Klenk M, Nussbaumer H, Kopecek R. Performance of bifacial PV arrays with fixed tilt and horizontal single-axis tracking: comparison of simulated and measured data. *IEEE J Photovoltaics*. 2019;9(6):1583-1589.
8. Marion W, Deline C, Silvana A. Bifacial_Radiance, 17 Dec. 2017. Web. [https://doi.org/10.11578/dc.20180530.16](https://doi.org/10.11578/dc.20180530.16) [https://www.osti](https://www.osti). gov/doecode/biblio/6869
9. Ward GJ. The radiance lighting simulation and rendering system. In: Proceedings of the 21st annual conference on computer graphics and interactive techniques; 1994:459-472.
10. Robinson D, Stone A. Irradiation modelling made simple: the cumu- lative sky approach and its applications. In: The 21st Conference on Passive and Low Energy Architecture, Eindhoven, The Nether- lands; 2004:15. https:// www.solemma.net/references/PLEA2004_ RobinsonAndStone.pdf
11. Chiodetti M, Lindsay A, Dupeyrat P, Binesti D, Lutun E, Radouane K, Mousel S. PV bifacial yield simulation with a variable albedo model. In: EU PVSEC Proceedings; 2016:1449-1455.
12. Marion B, MacAlpine S, Deline C, Asgharzadeh A, Toor F, Riley D, et al. A practical irradiance model for bifacial PV modules. In: 44th IEEE Photovoltaic Specialists Conference; 2017:1537-1542. https:// www.nrel.gov/docs/fy17osti/67847.pdf
13. Krenzinger A, Lorenzo E. Estimation of radiation incident on bifacial albedo-collecting panels. *Int J Solar Energy*. 1986;4(5):297-319.
14. Yusufoglu UA, Lee TH, Pletzer TM, Halm A, Koduvelikulathu LJ, Com- parotto C, et al. Simulation of energy production by bifacial modules with revision of ground reflection. *Energy Procedia*. 2014;55:389-395.
15. Reise C, Schmid A. Realistic yield expectations for bifacial PV systems an assessment of announced, predicted and observed benefits. *6th* *PVPMC Workshop, Freiburg*. 2015.
16. Soria B, Gerritsen E, Lefillastre P, Broquin J. A study of the annual performance of bifacial photovoltaic modules in the case of vertical facade integration. *Energy Science and Engineering*. 2016;4(1):52-68.
17. Gross U, Spindler K, Hahne E. Shapefactor-equations for radiation
**FIGURE A1** A photograph of the rear irradiance solar panel under heat transfer between plane rectangular surfaces of arbitrary position STCmeasurementatISCKonstanz and size with parallel boundaries. *Lett in Heat and Mass Transfer*. 1981;8(3):219-227.

18. Shoukry I, Libal J, Kopecek R, Wefringhaus E, Werner J. Modelling of bifacial gain for stand-alone and in-field Installed bifacial PV modules. *Energy Procedia*. 2016;92:600-608. [https://doi.org/10.1016/j.egypro](https://doi.org/10.1016/j.egypro).
2016.07.025
19. AsgharzadehA,MarionB,DelineC,HansenC,SteinJS,ToorF.A sensitivity study of the impact of installation parameters and sys- tem configuration on the performance of bifacial PV arrays. *IEEE J* *Photovoltaics*. 2018;8(3):798-805.
20. Perez R, Seals R, Michalsky J. All-weather model for sky luminance distribution—preliminary configuration and validation. *Sol Energy*. 1993;50(3):235-245.

**TABLE A1** Mean measured (MeanMea) and **Cell MeanMea,** mean modeled (MeanMod) as well **W/m²** root-mean-square deviation (RMSD) for modeled values of the rear irradiance for all monitored solar cells using hourly data measured 1 126.5 in Konstanz for the month of September 2018 2 122.3 3 127.4 4 120.3 5 110.0 6 118.2 8 112.3 9 114.7 10 143.5 11 129.8 12 122.2 14 125.5 15 126.2 16 137.7

**MeanMod** **VF,** **W/m²**

110.2
101.9
124.2
113.8
111.2
116.7
112.1
114.4
148.2
113.8
119.4
124.2
123.0
134.4 **MeanMod** **RT,** **W/m²**
132.0
114.0
135.6
114.0
106.8
114.4
111.7
114.4
144.3
122.3
119.1
126.3
121.1
131.3 **RMSD RMSD Relative Relative** **VF, RT, Mean Mean** **W/m² W/m² Deviation Deviation**
**VF, % RT, %**

33.7 13.8 −12.9 4.3
33.7 25.4 −16.7 −6.7
29.7 14.7 −2.4 6.5
29.2 18.9 −5.4 −5.2
23.2 21.8 1.2 −2.9
24.8 30.9 −1.2 −3.2
24.1 15.5 −0.2 −0.6
24.2 19.7 −0.3 −0.3
26.9 14.6 3.3 0.6
30.3 17.1 −12.3 −5.8
25.8 13.7 −2.3 −2.5
26.4 15.9 −1.0 0.6
25.7 23.5 −2.6 −4.0
26.6 36.5 −2.4 −4.6
**FIGURE A2** Scatter plot of measured irradiance by the calibrated solar cell versus the irradiance measured by the reference pyranometer. The data were measured every 5 min for a period of 1mo.*r²* represents the coefficient of determination [Colour figure can be viewed at wileyonlinelibrary.com]

Abbreviations: RT, ray tracing; VF, view factor.
