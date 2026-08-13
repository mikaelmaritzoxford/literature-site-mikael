### <u>RESEARCH ARTICLE</u>

www.solar-rrl.com

# Model-Chain Validation for Estimating the Energy Yield of Bifacial Perovskite/Silicon Tandem Solar Cells

## Peter Tillmann, Klaus Jäger, Asher Karsenti, Lev Kreinin, and Christiane Becker*

Technology Roadmap for Photovoltaics The power conversion efficiency of conventional silicon solar cells approaches its revised the prediction on market share for bifacial cell technology for a certain date theoretical limit. Bifacial operation and the perovskite/silicon tandem device upwards year by year and meanwhile pre- architecture are promising approaches for increasing the energy yield of pho- dicts a share of more than 75% bifacial cells tovoltaic modules. Here, an energy yield calculation tool for (bifacial) perovskite/ [3] Particularly passivated emitter in 2031. silicon tandem solar cells is presented. It uses a chain of models for irradiance, rear cell (PERC) and rear totally diffused optical absorption, and temperature-dependent electrical performance. Each step (PERT) silicon cells allow for bifacial oper- is validated with irradiance and performance data from a rooftop installation with ation, and hence more power generation at mono- and bifacial silicon solar cells in Jerusalem, Israel. Selecting the data for nearly zero additional costs. This enables the reduction of the levelized cost of elec- two days (one in summer, one in winter) and considering the high-reflective [4] tricity (LCOE) at a fast pace and opens ground of this particular installation (albedo 60%) a 20% increased energy yield up new application fields such as agricul- for a bifacial module with respect to a monofacial module is modeled. This result tural PV[5]and floating PV.[6] matches well with experimental data. When “upgrading” the silicon solar cell to a Accurate modeling of the energy yield of perovskite/silicon tandem solar cell, the case study predicts up to 40% additional bifacial solar power plants is of utmost importance as it allows to estimate the energy yield. Combining the concepts of bifacial solar operation and perovskite/ silicon tandem solar cells results in up to 60% increased energy with a high albedo ground, and is therefore a promising approach to further decrease the of planned solar power plants. Modeling levelized cost of electricity for photovoltaic electricity generation.

#### 1. Introduction

The market share of bifacial photovoltaic (PV) modules has grown remarkably in recent years. Bifacial modules not only utilize light impinging onto the front side of the PV module, but also light reaching the backside. [1,2] The International

P. Tillmann, K. Jäger, C. Becker Department Optics for Solar Energy Helmholtz-Zentrum Berlin für Materialien und Energie 12489 Berlin, Germany E-mail: christiane.becker@helmholtz-berlin.de
P. Tillmann, K. Jäger Computational Nano Optics Zuse Institute Berlin 14195 Berlin, Germany
A. Karsenti, L. Kreinin Lev Academic Center SolAround Ltd. Jerusalem 9611001, Israel The ORCID identification number(s) for the author(s) of this article can be found under [https://doi.org/10.1002/solr.202200079](https://doi.org/10.1002/solr.202200079). © 2022 The Authors. Solar RRL published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.
##### DOI: 10.1002/solr.202200079

LCOE at a certain location, which is a cru- cial figure-of-merit to judge the bankability

the energy yield from monofacial solar modules based on weather data, such as direct and diffuse solar irradiance, temper- ature, wind speed, and the geometrical arrangement and surroundings of the module, has been well- developed in the past decades. However, modeling the rear-side irradiance on a solar module is still regarded as challenging, [7]

particularly on so-called “variable” days with quickly changing cloud coverage, and more general, on shorter time scales. [8]

The reason is that the rear side of a solar module mainly receives light reflected from the ground with a timely variable pattern of directly illuminated and shadowed areas seeing more or less from the diffuse skylight. In 2019, Pelaez et al. compared five different bifacial illumination models [9] either based on ray trac- ing, [10] a view factor model, [11] or an empirical model based on a large amount of field data, [12] all predicting the front and irradi- ance on sunny days within reasonable errors. However, when taking the next step toward multijunction solar cells one has to look more closely and accurate modeling of bifacial irradiance at short time scales becomes even more important. In case of two-terminal tandem devices, which are the pre- ferred configuration in terms of minimized balance-of-system costs and low parasitic absorption losses in contact layers, current matching is required for maximal power output. Both, the PV system and the solar cells, have to be designed in such a way that an equal number of photons is absorbed in the top and bottom cells, respectively, because otherwise the whole device is limited by the subcell absorbing fewer photons. While variable weather conditions tend to average out in bifacial single-junction devices, variations of front and rear side illumination can significantly

© 2022 The Authors. Solar RRL published by Wiley-VCH GmbH Sol. RRL 2022, 6, 2200079 2200079 (1 of 12)

2367198x, 2022, 9, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/solr.202200079](https://onlinelibrary.wiley.com/doi/10.1002/solr.202200079) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

disturb current-matching in bifacial tandem solar cells. [13] Various theoretical energy-yield calculation models were developed for the currently widely discussed two-terminal perovskite/silicon tandem solar cells [14] in bifacial operation. [13,15–18] However, only very little experimental data of bifacial two-terminal perovskite/silicon tan- dem solar cells on outdoor test fields have been published so far. [19] Hence, in the medium term, the prediction of the energy yield of this technology will still rely on simulations. More impor- tant is to validate the rear-side illumination models by experimental field data, e.g., from bifacial silicon single-junction solar cells at the specific location of interest, to enable reasonable predictions for bifacial tandem solar cells as well. In this study, we combine several models to calculate the energy yield of the investigated devices. Each step in the chain of models is validated with data from a mono- and a bifacial silicon solar module. In the first step, we apply an illumination model for bifa- cial solar modules arranged as an infinitely extended array based on view-factor considerations. [20] We compare the simulations with the measured data from a bifacial solar cell module installed in a small power plant located on a rooftop in Jerusalem, Israel, on two sunny days (one in winter and one in summer) as well as one “variable” day with quickly changing cloud coverage. Comparing the measured generated current with the modeled combined irra- diance from the front and rear sides of the module allows to vali- date the optical view factor model nearly independently from module temperature and wind speed. In a second step, we imple- ment a temperature-dependent electrical model to compare mea- sured and simulated generated power. Finally, we use our validated bifacial solar cell model to predict the energy yield of perovskite/silicon tandem solar cells with the perovskite top cell on the front side, and also the configuration with perovskite cells “sandwiching” the silicon bottom cell on both, front and rear side.

#### 2. Experimental Data and Numerical Methods

2.1. Experimental Data Basis The experimental data used in this work was recorded on a roof- top installation in Jerusalem, Israel, provided by SolAround Ltd.
Figure 1a shows the rooftop installation, made of four rows of
 solar panels mounted in landscape orientation with three panels per row. A high-albedo plastic foil under the solar panels is used
(a) (b)
to increase the amount of light reflected onto the back side of the modules. The installation includes mono- and bifacial modules and sensors for measuring the global, diffuse and direct irradi- ance. K-type thermocouples are installed at the back side of solar panels to measure the cell temperature. The temperature sensor should give a good estimate of the operation conditions of the solar cells, but the actual cell temperature is likely slightly higher than the temperature measured at the back side of the panel. From the solar panels, the short-circuit current (ISC), open-circuit voltage (VOC), maximum power, and fill factor (FF) are measured each minute. Three days of data are available, August 26, 2019 (sunny summer day), February 15, 2020 (sunny winter day), and February 19, 2020 (cloudy/variable winter day). The parameters used to rep- resent the rooftop installation are summarized in Table 1.

2.2. Numerical Methods
2.2.1. Bifacial Illumination Model The first step to calculate the characteristics of the bifacial solar cells is to simulate the irradiance on the front and back sides. For the irradiance simulation, we employ a recently developed view factor illumination model,
[20,21] which was specifically designed for bifacial solar cells. In that model, the PV field is considered so large that boundary effects can be neglected. The geometry of the solar panels is simplified (the panels are assumed to be perfectly flat, with no frame) and the front and back side are modeled as per- fectly black. These assumptions are used in many view-factor mod- els and typically lead to an underestimation of the back side irradiance of 5–20%. [22,23]

Figure 1b shows the schematic illustra-

tion of the components reaching the module front and back each: direct sunlight, diffuse skylight, diffuse light from the ground orig- inating from direct sunlight reaching the ground, and diffuse light from the ground originating from diffuse skylight reaching the ground. To describe the geometry of the PV installation under investigation the model requires the module length l, mounting height h, module spacing d, and tilt angle θm. Second, also the albedo (i.e., the reflectivity) of the ground is required (see Table 1). For the rooftop location in Jerusalem, no spectrally resolved solar irradiance data is available. However, broadband direct and diffuse irradiance are measured by pyranometers with a time resolution of one minute. To emulate the spectral information

2021, The Authors. Solar RRL published by Wiley-VCH GmbH. [18] Copyright

Figure 1. a) Photograph of the mono- and bifacial silicon solar panel rooftop installation located in Jerusalem, Israel, delivering the experimental data for

model validation. All data for monofacial cells is measured with the left module in the second row, bifacial data is measured with the module in the middle of the second row. b) Schematic representation of the bifacial irradiance model used in this study. Adapted under terms of the CC-BY license.

Table 1. Experimental parameters of the solar panel rooftop installation in

Jerusalem.

Model parameters l module length [m] 1.0 d module spacing [m] 1.9 h module height above the ground [m] 0.8 θ mmodule tilt angle 30° A albedo of the ground 60% Solar cell parameters at standard test conditions (STC) Front-side illumination V OCOpen-circuit voltage [V] 38.8 I SCShort-circuit current [A] 9.83 FF FF [%] 74 P Power [W] 283 Rear-side illumination V OCOpen-circuit voltage [V] 38.6 I SCShort-circuit current [A] 8.35 FF FF [%] 74 P Power [W] 242

Bifaciality (Ratio rear to front power) 85% Number of cells per module 60 Cell active area (unshaded by wires) [cm²] 240 Outdoor solar panel field data V OCOpen-circuit voltage [V] I SCShort-circuit current [A] FF FF [%] P Power at maximum power point [W] Measured solar and temperature data DHI Diffuse horizontal irradiance [W m] 2 K&Z CMP11 Pyranometer with shadow ring GHI Global horizontal irradiance [W m²] K&Z CMP11 Pyranometer POA Irradiance in the plane of the Phox SOZ-03 silicon module front side [W m²] reference cell T Cell temperature Type K thermocouple at c back side of the module

net-radiation method for multilayer stacks and ray tracing for simulating scattering by pyramidal interfaces. As input, we pro- vide detailed layer stacks, the type of interface (planar or tex- tured), and the complex refractive index (nk-data) for the used materials. All detailed layer stacks and references for the used nk-data are summarized in the Supporting Information (SI) Section S5. To study how the perovskite bandgap affects the solar-cell per- formance, we performed a wavelength shift of the available nk dataset for perovskite. [26] This estimation is justified by experi- mental data. [27]

We calculated the photocurrent densities as functions of the absorption and the spectral irradiance using Z 1200 nm J ph¼ e AðλÞΦfðλÞdλ (1) 300 nm

where e is the elementary charge, AðλÞ is the absorption in the considered absorber layer, and Φfis the photon flux reaching the module. The photon flux can be calculated from the spectral irra- diance according to

<u>λ</u> ΦfðλÞ¼Eλ hc

(2)
with the spectral irradiance Eλ, the Planck constant h and the speed of light c.

2.2.3. Temperature-Dependent One-Diode Model An electrical model is used to calculate the power output of a solar cell from the absorbed photocurrent. To get a realistic esti- mation of the power output different factors such as the electrical resistance and temperature have to be accounted for. In this work, we use a one-diode model to calculate the current–voltage characteristics (IV-curves) of each solar cell. The one-diode model assumes an equivalent circuit, where an ideal current source is connected in parallel to a diode and optionally one or two resistors to model the series and shunt resistance of the solar cell. We use the following equation in our work
≥ ~ <u>V þ J ⋅ RseriesV þ J ⋅ Rseries</u> JðV Þ¼JphJ₀ exp 1 (3) kT =e Rshunt

with the dark saturation current density J₀, elementary charge e, the Boltzmann constant k, the temperature T, photon current density Jph, series resistance Rseries, and shunt resistance

R. This form of the one-diode equation has three parameters shunt that determine the IV-curve for a given illumination and temper- ature: series resistance, shunt resistance, and dark saturation current. These parameters can typically be extracted from the measured IV-curve by fitting the one-diode equation to match the experiment. While series and shunt resistance are only slightly dependent on temperature (we assume it to be constant for simplicity) the dark saturation current is strongly dependent on the temperature. Therefore, we are not fitting the dark satu- ration current directly. Using the integrated overlap of the black- body radiation and the external quantum efficiency (EQE) of a junction an idealized but temperature-dependent dark saturation current can be computed
[28,29]

needed to calculate the photocurrent we use spectrl2, a model based on radiative transfer simulations developed by Bird and [24] Riordan. spectrl2 calculates the direct and diffuse spectral irra- diance based on the solar position and several atmospheric parameters, such as precipitable water, ozone concentration, and aerosol optical depth. This model is only suitable for clear-sky conditions and therefore only applicable for describing the two sunny days August 26, 2019 and February 15, 2020.

2.2.2. Optical Solar Cell Model We use the MATLAB-based software package GenPro4
[25] to cal- culate the optical absorption, reflection, and transmission of the investigated cell architectures. GenPro4 uses the

www.advancedsciencenews.com www.solar-rrl.com

Z ∞solar modules. While the illumination on the backside is not J 0,idealðT Þ¼e EQEðλÞΦBBðλ, T Þdλ (4) 0directly measured we can use the short-circuit current of a bifa- cial module as a proxy. with the elementary charge e and the photon flux of the black Figure 2a shows the dependence between the plane-of-array body radiation ΦBB. Using arguments of reciprocity and consid-irradiance on the front side of the solar cell modules and the ering the limited external quantum efficiency EQEelof a real cell short-circuit current measured on a monofacial PERT silicon a realistic and temperature-dependent dark saturation current J₀ solar cell module. The plane-of-array irradiance is directly mea- can be calculated. [28] sured by a reference cell mounted in the same plane as the solar

<u>J</u> <u>0,idealðT Þ</u> cell modules. The silicon solar module is rated for a short-circuit J₀ðT Þ¼ (5) current ISCof 9.83 A at standard testing conditions (STC), i.e., EQEel 2 1000 W m irradiance. The red line shows the linear depen-

For details of the approach please see Supporting Information dence of the short-circuit current on the irradiance calibrated

Section S1. It should be noted that we assume a constant ideality with the STC measurement. The blue dots represent the

factor for the diode of n ¼ 1. short-circuit current measured over the course of August 26, 2019 and February 15, 2020. This shows that the short-circuit current ISCis an excellent proxy for the irradiance. Here, the data points from February 19, 2020 are excluded because the time-

#### 3. Results

stamps of the irradiance and the short-circuit current are not per-

3.1. Validation of the Bifacial Illumination Model
fectly aligned (in the temporal sense), and therefore can diverge considerably in rapidly changing cloud coverage. In a first step, we aim to validate the optical bifacial illumination Because of the nearly linear response of the short-circuit cur- model by comparing simulated with experimental data. The illu-rent with respect to the plane-of-array irradiance, we use a con- mination model calculates the intensities of the direct and dif-stant factor determined by the short circuit current measured at fuse light that are received at the front and back side of the STC for the model validation of this section

(a) (b)
(c) (d)
Figure 2. Validation of the bifacial illumination model. a) Correlation between measured module short-circuit current and measured plane of array

irradiance (blue symbols), and calibration curve from solar cell characteristics at standard testing conditions (STC (red line)). b–d) Comparison of measured and modeled short-circuit current for mono- and bifacial solar modules at one variable day (b) and two sunny days (b),(c) by combining the bifacial irradiance model with the STC calibration curve. In part (b) a 15 min rolling average is shown. The output of the irradiance model depends on the DNI and DHI readings, position of the sun and the photovoltaic (PV) installation geometry detailed in Table 1.

Sol. RRL 2022, 6, 2200079 2200079 (4 of 12) © 2022 The Authors. Solar RRL published by Wiley-VCH GmbH

<u>9.83A</u>
J ph;front¼ ⋅ Efront 1000W

<u>8.35A</u> (6)
J ph;back¼ ⋅ Eback 1000W J ph;bifacial¼ Jph;frontþ Jph;back

with Efrontand Ebackas the irradiance calculated by the irradiance model for the front and back side respectively. These calculations are based on the pyranometer readings for the DNI and DHI, as well as the position of the sun (in terms of azimuth and zenith angle) and the geometry of the PV installation detailed in Table 1.

Figure 2b–d shows the simulated and measured module

short-circuit current for a bifacial and monofacial silicon module on August 26, 2019, February 15, 2020, and February 19, 2020, respectively. For the 2 days with clear-sky conditions, the calcu- lated curves are very close to the measured lines, showing a good agreement between measurement and simulation. The variable day (February 19) is much more demanding. The results shown are 15 min rolling average because the very fast changes in irra- diance otherwise would render the graphic unreadable. Because the timestamps of the irradiance are not perfectly aligned with the short-circuit current measurements some divergence between simulation (based on the irradiance) and measurement is to be expected. Also, the underlying assumption of the illumination model (all direct sunlight originates from a point source while the diffuse light is distributed isotropically over the hemisphere) is less valid for situations with rapidly changing cloud coverage. Nonetheless, the illumination model is still able to reproduce the general trends of the short-circuit current. However, some higher differences are visible between model and measure- ment, especially for times with high and quickly changing irradiance.

3.2. Validation of the Optical Solar Cell and Spectral Models As detailed in Section 2.2, we use a three-step modeling approach to calculate the generated photocurrent density in each junction of the photovoltaic devices. First, we simulate the optical absorp- tion profile of the investigated solar cell using the material stack as input. Second, we generate spectral information from broad- band irradiance measurement and weight them with the results of the bifacial illumination model. Third, we combine spectral absorption and spectral irradiance to calculate the photocurrent density in the relevant junctions of the solar cell devices accord- ing to Equation (1).
Figure 3a shows the layer stack used for calculating absorp-
 tion, reflection, and transmission of the bifacial SolAround PERT solar cell. The details of the layer stack and the used nk-data are found in the Supporting Information, Section S5.
Figure 3b,c shows the result of the optical GenPro4 simulation
 with front side and back side illumination, respectively.
Figure 3d shows selected examples of the calculated spectral
 direct irradiance for different times on August 26, 2020. A spec- trum according to AM1.5g is added as a reference. A red shift is clearly visible for the early morning spectrum at 7:10 am resulting from the increased scattering of short-wavelength light due to the prolonged light path through the atmosphere. At 8:50, the
spectrum is already close to the 10:30 and 12:10 spectra, which are very similar and nearly identical to the AM1.5 reference spectrum. To compare the calculated photocurrent with the measured short-circuit current, the area of the solar cell and the number of cells in one module has to be considered. For a cell, we assume an active area (area of the cell that actively contributes to the absorption) of 240 cm² and 60 cells per module.

Figure 3e shows the photocurrent of the simulated mono- and

bifacial PERT solar module and the measured short circuit cur- rent. Simulation and measurement are in good agreement and the results are very similar to the simulated short-circuit current based on STC measurements.

3.3. Validation of the Temperature-Dependent One-Diode Model We use a one-diode model to calculate the IV-curves for a given temperature and absorbed photocurrent. From the IV-curve the open-circuitvoltage, FF, and maximum power point are derived. The details of the model are described in the numerical method section above. The measured values for VOCand FF of silicon PERT solar cells mounted at the rooftop installation were fitted to acquire the necessary parameters
2 for the one-diode 2 model. We found Rseries¼ 1.9 Ω cm, Rshunt¼ 1000 Ω cm and EQEel¼ 0.16%. Both the open-circuit voltage and the FF strongly depend on the temperature according to the one diode model (see Figure S4 in the Supporting Information). The level of irradiance also influ- ences the FF and open-circuit voltage. Higher levels of irradiance have a positive impact on the open-circuit voltage while the FF has a peak, depending on the series and shunt resistance of the cell. Higher temperatures always reduce FF and open-circuit volt- age. A more detailed discussion of these effects is given in the Supporting Information, Section S3.

Figure 4 shows the measured module temperature (Tm) and

global horizontal irradiance (GHI) (a), the measured and simu- lated power output P (b), the FF (c), and the open-circuit voltage VOC(d). Overall measured and simulated parameters of the solar cell agree very well. Over the course of the morning temperature and irradiance gradually increase. While the increasing irradi- ance leads to increasing VOChigher cell temperatures reduces it. These competing trends of temperature and irradiance on the FF and VOCare well reproduced by the model and result in good agreement for the power simulation of the solar cell modules. Larger differences are found only for very low levels of light intensity in the morning and times when either the irra- diance sensor and/or the solar panels are shaded in the evening. This confirms that the chosen simulation approach is well suited to reproduce the measured power output of the silicon based PERT modules produced by SolAround. In Section S3.1 of the Supporting Information, we show the results for the simulation of the bifacial solar cell and discuss the differences for modeled and simulated results. The main differences between results for the bifacial and monofacial solar cells are an unexpected high FF measured for the bifacial solar cell when using the same cell parameters as used for the monofacial cells. We additionally benchmarked a two-diode model assuming a constant,

Figure 3. Validation of optical solar cell modelling. a) Layer stack of the frontside textured passivatated rear totally diffused (PERT) bifacial solar cells used

to simulate absorptance, transmittance and reflectance for b) frontside and c) back side illumination with the software GenPro4. For a better clarity, the thin contact, passivation and doping layers or not show here; the respective parasitic absorption is summarized in green in part (b) and (c). The detailed layer stack can be found in the Supporting Information Section S5. d) Examples of modeled spectral direct normal irradiance according to the model spectrl2 [24] for different times on August 26, 2020 and AM1.5g spectrum for comparison. e) Comparison of measured and modeled short-circuit current for mono- and bifacial solar modules on two sunny days by combining the bifacial irradiance model (separately validated in Figure 2), spectrl2 and optical simulations using GenPro4.

temperature-independent dark saturation current for the second perovskite junctions surrounding a silicon junction in the mid- diode. The parameters were fitted for a JV curve recorded under dle, like a “sandwich,” and discuss its performance prospects. STC and results are shown in S2 and S3 in the Supporting Figure 5 illustrates the 2-terminal connected and 4-terminal Information. Due to the ambivalent results from the comparison connected tandem solar cells. The solar cell stack for 2-terminal of the one- and two-diode model we used the simpler one-diode connected tandem solar cells is based on work by Al-Ashouri model for the remainder of this work. et al. [14] that marks the highest perovskite/silicon tandem solar cell efficiency with published details of the layer stack. These tan- dem cells use a MeO-2PACz self-assembled monolayer (SAM) as

3.4. Energy Yield Predictions for Bifacial Perovskite/silicon
selective contact for hole transport. This layer is shown for com- Tandem Solar Cells pleteness in Figure 5 but it is not considered in the optical simu- lation because it is unlikely to affect the optical response due to In this section, we estimate the energy yield that would be its very small thickness (1–2 nm). Here we focus on tandem solar

|In this|section,|we estimate|the energy|yield that|would be|its very small thickness (1–2 nm). Here we focus on tandem solar||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|obtained if the bifacial solar panel array located on a rooftop||||||cells where the perovskite cell is processed on the polished side of||||||
|in Jerusalem, Israel, did not consist of mono- or bifacial silicon||||||the silicon bottom cell and the textured side facing downwards.||||||
|solar modules, but of perovskite/silicon tandem solar cells of dif-||||||This approach enables spin-coating deposition of the top cell,||||||
|ferent configurations. We introduce 2- and 4-terminal connected||||||which|shows|the highest|efficiencies|published|so far.|
|perovskite-on-silicon||tandem|solar cells,|simulate|the 2-day|From an industrial manufacturing point of view, double-sided||||||
|energy the effects of the perovskite bandgap. Later in this section, we|yield for|bifacial and|monofacial|devices and|discuss|textured future|silicon and our modeling approach is fully applicable to|bottom|cells might|be favorable|in the|
|propose|a 4-terminal|architecture|with|three junctions,|two|these kinds of cell technologies as well.||||||

[14]

[30–32] [33]

Sol. RRL 2022, 6, 2200079 2200079 (6 of 12) © 2022 The Authors. Solar RRL published by Wiley-VCH GmbH

Figure 4. Measured sensor data and parameters of monofacial solar cells over the course of August 26, 2019 and February 15, 2020. a) Measured global

horizontal irradiance and cell temperature. Comparison of simulated (one-diode model) and measured b) module power, c) fill factor (FF), and d) open- circuit voltage.

Figure 5. Schematic of the simulated bifacial tandem stack in a) 2-terminal and b) 4-terminal configuration. One side of the silicon exhibits a pyramidal

texture, the other side is planar. In the case of the 2-terminal tandem the perovskite is assumed to be processed on the planar side of the silicon bottom cell while in the 4-terminal configuration the texture is pointed upwards to minimize reflection losses under top illumination. The self-assembled mono- layer (SAM) is shown for completeness but ignored in the optical simulations due to its very small thickness (1–2 nm). The detailed stacks including all considered interlayers can be found in Supporting Information Section S5.

In this study, we adapt the silicon bottom cell architecture and For the cell parameters of the perovskite subcell (EQEel, Rshunt, use cell parameters of the SolAround solar cells. The PERT cells Rseries)wefit results published by Jošt et al. [34] on the temperature from SolAround are based on p-type silicon wafers and textured dependence of the efficiency and VOCof the perovskite solar cell. at the front side. For the simulation of tandem stacks a silicon Details of the fitting results can be found in the Supporting oxide interlayer was added (shown as n-SiOxin the layer stacks). Information Section S4. This silicon oxide interlayer is highly doped (for electrical con-For the 4-terminal tandem, we assume a stack consisting of a ductivity) and was used by Al-Ashouri et al. to reduce the reflec-perovskite top cell as used by Jošt et al. processed on the front tion between the perovskite and silicon subcell. glass and, separated by a layer of EVA, the silicon bottom cell

Sol. RRL 2022, 6, 2200079 2200079 (7 of 12) © 2022 The Authors. Solar RRL published by Wiley-VCH GmbH

with the textured side to the front. The copper contact of the perovskite is replaced with a 200 nm thick layer of indium zinc oxide (IZO) for transparency in the infrared region. This approach likely leads to a too optimistic estimation of the perfor- mance of the 4-terminal tandem cell because the lateral current flow through the IZO layer will cause a higher series resistance compared to the copper contact of the reference. However, we do not account for this difference because it is not quantitatively accessible. All fitted values for EQEeland resistivity for the 2-and 4-terminal configurations are summarized in Table 2. The details of the stacks with all relevant interlayers (transparent conductive oxides, charge carrier transport layers, anti-reflective coatings)

|Table 2. Summary of the fitted cells parameters (R||||, R|, and EQE|)|
|---|---|---|---|---|---|---|
|for different cell types and simulation results (η, V||||, and J|) for standard||
|testing|conditions|(25 °C, AM1.5g|illumination).|Where|appropriate||
|separate indicated with top cell value/bottom cell value.|values for R|top and R|bottom cells EQE|of the tandems η V|have been J||
||[Ω cm]|[Ω cm]|[%]|[%] [V]|[mA cm|]|
|Silicon|1.9|1000|0.16|19.3 0.655|40.7||
|Perovskite|6|1000|0.12|18.3 1.103|22.1||
|T tandem|6|1000/1000|0.16/0.12|25.3 1.735|18.8||
|T tandem|6/1.9|1000/1000|0.16/0.12|24.9 1.114/0.619|19.9/17.5||

series shunt el oc ph

and the corresponding absorption spectra calculated with GenPro4 are found in the Supporting Information, Section S5. The generated photocurrent density in the silicon and perov- skite junctions is in line with state-of-the-art 2-terminal [14] and 4-terminal [35] perovskite on silicon tandem cells. However, the power conversion is 3–4 percentage points (p.p.) below the values reported in these research articles. This is mainly due to the usage of silicon cell parameters of solar modules produced with standard industrial processes while research articles often use high-end silicon cells that are only available on small scales. Also, the parameters for the perovskite cell correspond to a lower efficiency then would be found for small-scale record cells. For all simulations of tandem solar cells, we assume that the modules are mounted in the same rooftop installation shown in

Figure 1 with the geometry detailed in Table 1 and the same

albedo of 60%. Figure 6 shows the calculated photocurrent den- sity generated in the (a þ c) perovskite and (b þ d) silicon junc- tion in a bifacial (top row) and a monofacial (bottom row) tandem for different perovskite bandgaps. Overall the photocurrent den- sity follows the irradiance over the course of the day with the highest levels around midday. Decreasing the perovskite bandgap increases the photocurrent density because more pho- tons with energies above the bandgap can be utilized. As a con- sequence, the photocurrent density in the silicon junction decreases with lower perovskite bandgaps. While the perovskite junction is unchanged for mono- or bifacial operation the silicon junction generates significantly higher current densities with

series shunt el STC oc ph 2 2 2

Figure 6. Absorbed photocurrent density Jph

installation as specified in Table 1.

of the (left) perovskite and (right) silicon subcell of 2-terminal perovskite/silicon tandem solar cells over the course of 26 August 2019 and 15 February 2020. The upper row (a,b) and lower rows (c,d) show results for a bifacial and for a monofacial tandem device, respectively. The geometrical parameters of the solar panel array as well as the albedo (60%) are identical to the parameters of the Jerusalem rooftop

back side illumination. The light reaching the back of the bifacial tandem is exclusively absorbed in the silicon cell. This is because silicon has a lower bandgap than perovskite. All light that is trans- mitted because of photon energies below the bandgap of the sili- con is also below the bandgap of the perovskite and therefore can not be absorbed there either. With a perovskite bandgap of 1.55 eV the bifacial device gen- erates roughly the same photocurrent density in the perovskite and silicon junctions and hence is at current-matching condi- tions. For the monofacial tandem solar cell, the optimal perov- skite bandgap is significantly higher. Because of the missing additional photons from the back side, the perovskite top cell needs to transmit more light into the silicon subcell to ensure current-matching conditions. For a bandgap of around

1.65 eV, both junctions generate roughly equal current densities.
Figure 7 shows the simulated energy yield over the two days
 (August 26, 2019 and February 15, 2020) of available data for one module of mono-or bifacial silicon cells (green), 2-terminal (blue) and 4-terminal (orange) perovskite/silicon tandem cells for different perovskite bandgaps (in case of the tandems). The monofacial silicon cell yields around 3.3 kWh on these two days while the bifacial equivalent yields 3.9 kWh, an increase of roughly 20%. The energy yield of the monofacial 2-terminal tandem mod- ule strongly depends on the perovskite bandgap, with an optimal bandgap of 1.66 eV. The optimal bandgap of the bifacial 2-terminal tandem is shifted to 1.56 eV and an overall increased electrical yield is found. Overall, mono- and bifacial 4-terminal tandem cells show a lower dependence on the perovskite bandgap with the opti- mum at the maximum of the chosen perovskite bandgap range. The optimal bandgap does not change under bifacial operation. We choose a range of 1.5–1.7 eV because in this range high-quality perovskite materials have been demonstrated while perovskite cells with higher bandgaps can be difficult to manufacture.
[36]

At their individual optimal bandgap, 2-terminal tandem solar cells show a slightly higher module yield compared to the

corresponding 4-terminal configuration at the same bandgap. However, the 4-terminal configurations have a higher energy yield at the maximum bandgap. Please note that the results shown in Figure 7 should only be regarded as a rough estimation of optimum perovskite bandgaps. We regarded the EQEelas a constant parameter in our simulations neglecting its dependence on temperature, injection, and particularly, the perovskite bandgap. This might lead to an underestimation of the tandem energy yield for lower-bandgap perovskites where much higher EQEelvalues have been reported, [37] and to an overestimation of the yield when the tandem solar cells comprise wide-bandgap perovskite top cells, which often suffer from photo-induced phase segregation deteriorating the open-circuit voltage. [38]

This might especially impact 4-terminal tandem solar cells where an optimum perovskite bandgap at the upper edge of the investigated range was found. For more detailed energy yield cal- culations the individual performance of the perovskite top cell in terms of EQEelhas to be considered. The addition of a perovskite, wide-bandgap top cell atop a silicon bottom cell enables obtaining higher power conversion efficiencies owing to a reduction of thermalization losses of high energy photons. As this concept might also work for light impinging on the backside of the solar module, we also propose a triple-junction, 4-terminal perovskite/silicon-perovskite “sandwich” architecture. Figure 8a shows the schematic stack of this solar cell configuration. The top perovskite and the middle silicon cell are connected in series and form two electrical con- tacts (terminals) of the cell. The bottom perovskite is insulated by a layer of EVA, similar to the perovskite cell in the conventional 4-terminal tandem, and is connected with two separate terminals. The two top junctions will absorb similar photocurrent densities when the perovskite bandgap is chosen properly while the bottom perovskite will only absorb a fraction of the light due to the significantly lower irradiance at the back side of the module.

Figure 8b shows the effect of the top and bottom perovskite

bandgap and the 2-day energy yield. The effect of the top cell bandgap is much larger and an optimum is found at around

1.63 eV. The optimal bottom cell bandgap is found at the lower bound at 1.50 eV. It seems to be beneficial to absorb as much light as possible in the bottom perovskite junction. Figure 8c shows the calculated photocurrent density in the top-, middle- and bottom- junctions over the course of August 26, 2019 for a “sandwich” solar cell with a top and bottom cell bandgap of 1.63 and
1.50 eV, respectively. The photocurrent density of the top perov- skite and the silicon junction is quite well matched, resulting in optimal utilization of the impinging light. In contrast, the bottom perovskite cell absorbs only a fraction of the photocurrent densi- ties due to the lower irradiance at the back side of the module.
Figure 8d shows the IV-curves of the “sandwich” at 1 pm on
 August 26, 2019. Due to the low intensity of light absorbed in the bottom perovskite junction, the open-circuit voltage is rather low, and therefore the power conversion efficiency is reduced.
3.5. Discussion In this final section, we compare the results and discuss the pros- pects of different cell designs. Figure 9 shows the combined energy yield of the two sunny days (August 26, and
Figure 7. Simulated two-day (August 26, 2019 and February 15, 2020)

energy yield of one module for different solar cell technologies as function of the perovskite bandgap (in case of tandems). The geometrical param- eters of the solar panel array as well as the albedo (60%) are identical to the parameters of the Jerusalem rooftop installation as specified in Table 1.

Figure 8. Simulation setup and results for 4-terminal sandwich configuration. a) Stack of the simulated “sandwich” solar cell. The upper perovskite and

the silicon cell form a 2-terminal tandem, the lower perovskite is electrically independent with its own 2-connection terminals. b) Two-day energy yield for various bandgaps of the top (x-axis) and bottom (y-axis) perovskite. c) Absorbed photocurrent density J phover the course of August 26, 2019 for the three junctions of the device. d) Example IV-curves for August 26, 2019, 13:00. Because top perovskite and silicon subcells are connected in series they share one IV-curve as a tandem.

Figure 9. Two-day (August 26, 2019 and February 15, 2020) energy yield

comparison of one module for all investigated solar cell architectures. The first two bars show the experimental result for mono and bifacial silicon solar cells. For all tandem solar cells the best performing perovskite bandgap was selected. The shown relative gains in percentage all refer to the experimental monofacial result.

February 15, 2020) with measured data for one module on the Jerusalem rooftop solar panel array installation, and with simu- lated estimates for different solar cell technologies. The first two bars show the measured energy yield of the monofacial and bifa- cial PERT silicon solar cell module. Compared to the monofacial module (reference) the bifacial module yielded 22% higher energy outputs. It has to be noted that the most common surfaces below bifacial solar power plants exhibit lower albedo values than 60% as in the case of the specific Jerusalem rooftop installation. Therefore, and considering the short timeframe of this study, the bifacial gain cannot be generalized and the þ20% should be regarded as an upper bound for the bifacial energy yield gain. Simulated results for the silicon cells show similar numbers, however, the difference between the monofacial and the bifacial is lower, with only 16% gain due to bifaciality. We use the same cell parameters for the mono- and bifacial module, however, the FF of the bifacial cell seems to be higher (See Figures S5 and S6 in the Supporting Information). This results in an underestima- tion of the generated power and explains some of the differences between simulated and measured bifacial gain. Another factor can be found in the assumption of the model, where rows are infinitely wide and infinitely many rows are present. In the roof- top installation, however, there are only four rows with three modules each, where some light will shine in from the sides or the front, which is not considered by our model.

When switching to monofacial perovskite-on-silicon tandem technology, the results show an increase in the energy yield of 42%, which is significantly higher than the gain possible with silicon bifacial technology. This result is comparable with a study by Lehr et al. [16] who calculated around 40% increased energy yield for a monofacial tandem solar cell. The bifacial 2-terminal tandem is even able to produce 54% more energy than the silicon reference. This is a 13 p.p. increase with bifaciality, compared to the 16 p.p. from the simulated silicon cell results. This is in agreement with our earlier study [18] and findings by Onno et al. [13]. Because of the lower perovskite bandgap for current- matching in the bifacial tandem solar module, the voltage of the cell is also reduced. The lower cell voltage reduces the power conversion efficiency of light received at the front side compared to a monofacial tandem with a higher bandgap, and therefore the yield gain of 13 p.p. with bifaciality is the lowest for all considered technologies. Because the perovskite and the silicon subcells are electrically independent in the 4-terminal configuration, the bifacial opera- tion does not affect the consideration of the perovskite top cell bandgap. This results in a 43% and 61% higher energy yield for the mono-and bifacial 4-terminal tandem, respectively, an increase of 18 p.p. by bifacial operation. This shows that 4-terminal tandems can utilize bifacial operation slightly better than 2-terminal connections. Finally, we discuss the results for the 4-terminal “sandwich,” a design that includes two perovskite junctions with a silicon cell in between. Such a configuration is only sensible in bifacial opera- tion because under monofacial operation no light would reach the bottom perovskite cell. Our results suggest that such a device

|for Optical|Simulations|for Energy|Research|(BerOSE)|and the|
|---|---|---|---|---|---|
|Helmholtz|Excellence|Cluster SOLARMATH||of Helmholtz-Zentrum||
|Berlin Universität Berlin (grant no. ExNet-0042-Phase-2-3). Open Access funding enabled and organized by Projekt DEAL.|für Materialien|und Energie,|Zuse Institute|Berlin|and Freie|

does not improve the energy yield compared to conventional tandem devices. Both, the standard bifacial 2-terminal and 4-terminal tandem solar cells, show higher energy yields. The increased complexity and cost of an additional perovskite junction do not translate into higher energy gains. This is because of the low voltage of the bottom perovskite cell associated with the low light intensity at the back side of the solar cell module.

#### 4. Conclusion

In this work, we presented measured and simulated results for a solar panel array installed on a rooftop in Jerusalem, Israel. Irradiance and solar cell performance data for two sunny days, one in summer, one in winter, were available. We used the exper- imental performance data of the PERT silicon solar cells to vali- date the different steps in our model chain. We validated the illumination on the front and back side of the model, the absorbed photocurrent based on optical simulations of the solar cell stack, and finally the electrical performance calculated from a temperature-dependent one-diode model to model the cells open-circuit voltage, FF, and power at maximum power point. In this study, we confirm earlier findings, that bifacial opera- tion significantly alters the ideal bandgap for 2-terminal tandem solar cells, favoring the potentially more stable lower perovskite bandgaps, while 4-terminal tandem solar cells only show a weak dependence on the bandgap.

|[2] T. S. Liang,|M. Pravettoni,|C. Deline,|J. S. Stein,|R. Kopecek,|
|---|---|---|---|---|
|J. P. Singh, Environ. Sci. 2019, 12, 116.|W. Luo, Y.|Wang, A. G.|Aberle, Y. S.|Khoo, Energy|

Finally, we compared the measured and simulated energy yield of PERT silicon solar cells for two days, and calculated

the expected gain for a situation where the conventional silicon solar panels were replaced by 2-terminal and 4-terminal perov- skite/silicon tandem solar cells in mono- and bifacial configura- tion at the same location. Assuming that current results for small-area perovskites cells can be scaled up in the future, mono- facial 2- and 4-terminal tandems could result in 40–45% higher energy yields than monofacial silicon solar cells. Using bifacial tandem solar cells and albedo increasing measures can further increase the power output, with even 54–63% energy yield gain compared to a monofacial silicon solar module. A 4-terminal “sand- wich” configuration was introduced, with two perovskite junctions surrounding one silicon cell in the center, but no additional gain was found. The low light intensity in the bottom perovskite possibly limitstheperformanceandoverallthedeviceshowednogaincom- pared to classical 2- or 4-terminal tandem cells.

#### Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

#### Acknowledgements

P.T. thanks the Helmholtz Einstein International Berlin Research School in Data Science (HEIBRiDS) for funding. The authors acknowledge the sup- port from the SNaPSHoTs project in the framework of the German–Israeli bilateral R&D cooperation in the field of applied nanotechnology (grant no. 01IO1806) funded by the German Federal Ministry for Education and Research (BMBF) and the National Technological Innovation Authority of the State of Israel. The results were obtained at the Berlin Joint Lab for Optical Simulations for Energy Research (BerOSE) and the
#### Conflict of Interest

The authors declare no conflict of interest.

#### Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### Keywords

bifacial solar cells, energy yield calculations, perovskite/silicon tandem solar cells

Received: January 27, 2022 Revised: May 3, 2022 Published online: June 23, 2022

[1] R. Kopecek, J. Libal, Nat. Energy 2018, 3, 443. [2] T. S. Liang, M. Pravettoni, C. Deline, J. S. Stein, R. Kopecek,

[3] ITRPV, Technical Report, VDMA 2021, itrpv.vdma.org (accessed: July

2021).
[4] R. Kopecek, J. Libal, Energies 2021, 14, 2076, number: 8 Publisher: Multidisciplinary Digital Publishing Institute. [5] A. Weselek, A. Ehmann, S. Zikeli, I. Lewandowski, S. Schindele,

P. Högy, Agron. Sustainable Dev. 2019, 39, 35.
[6] G. M. Tina, F. Bontempo Scavo, L. Merlo, F. Bizzarri, Appl. Energy 2021, 281, 116084. [7] T. Katsaounis, K. Kotsovos, I. Gereige, A. Basaheeh, M. Abdullah,

A. Khayat, E. Al-Habshi, A. Al-Saggaf, A. E. Tzavaras, Renewable Energy 2019, 143, 1285.
[8] D. Berrian, J. Libal, Prog. Photovoltaics Res. Appl. 2020, 28, 609. [9] S. A. Pelaez, C. Deline, S. M. MacAlpine, B. Marion, J. S. Stein,

R. K. Kostuk, IEEE J. Photovoltaics 2019, 9, 82, conference Name: IEEE Journal of Photovoltaics.
[10] C. W. Hansen, J. S. Stein, C. Deline, S. MacAlpine, B. Marion,

A. Asgharzadeh, F. Toor, in 2016 IEEE 43rd Photovoltaic Specialists Conf. (PVSC), IEEE, Portland, OR, USA 2016, pp. 0138–0143, [https://doi.org/10.1109/PVSC.2016.7749564](https://doi.org/10.1109/PVSC.2016.7749564).
[11] B. Marion, S. MacAlpine, C. Deline, A. Asgharzadeh, F. Toor, D. Riley,

J. Stein, C. Hansen, in 2017 IEEE 44th Photovoltaic Specialist Conf. (PVSC), IEEE, Piscataway, NJ 2017.
[12] J. E. Castillo-Aguilella, P. S. Hauser, IEEE Access 2016, 4, 498, confer- ence Name: IEEE Access. [13] A. Onno, N. Rodkey, A. Asgharzadeh, S. Manzoor, Z. J. Yu, F. Toor,

Z. C. Holman, Joule 2020, 4, 580.
[14] A. Al-Ashouri, E. Köhnen, B. Li, A. Magomedov, H. Hempel,

P. Caprioglio, J. A. Márquez, A. B. M. Vilches, E. Kasparavicius,
J. A. Smith, N. Phung, D. Menzel, M. Grischek, L. Kegelmann,
D. Skroblin, C. Gollwitzer, T. Malinauskas, M. Jošt, G. Matic,ˇ
B. Rech, R. Schlatmann, M. Topic,ˇ L. Korte, A. Abate,
B. Stannowski, D. Neher, M. Stolterfoht, T. Unold, V. Getautis,
S. Albrecht Science 2020, 370, 1300.
[15] R. Schmager, M. Langenhorst, J. Lehr, U. Lemmer, B. S. Richards,

U. W. Paetzold, Opt. Express 2019, 27, A507, publisher: Optical Society of America
[16] J. Lehr, M. Langenhorst, R. Schmager, F. Gota, S. Kirner, U. Lemmer,

B. S. Richards, C. Case, U. W. Paetzold, Sol. Energy Mater. Sol. Cells 2020, 208, 110367.
[17] O. Dupré, A. Tuomiranta, Q. Jeangros, M. Boccard, P.-J. Alet, C. Ballif, IEEE J. Photovoltaics 2020, 10, 714. [18] K. Jäger, P. Tillmann, E. A. Katz, C. Becker, Sol. RRL 2021, 5, 2000628. [19] M. De Bastiani, A. J. Mirabelli, Y. Hou, F. Gota, E. Aydin, T. G. Allen,

J. Troughton, A. S. Subbiah, F. H. Isikgor, J. Liu, L. Xu, B. Chen, E. Van Kerschaver, D. Baran, B. Fraboni, M. F. Salvador, U. W. Paetzold,
E. H. Sargent, S. De Wolf, Nat. Energy 2021, 6, 167.
[20] K. Jäger, P. Tillmann, C. Becker, Opt. Express 2020, 28, 4751.

[21] P. Tillmann, K. Jäger, C. Becker, Sustainable Energy Fuels 2019, 4, 254. [22] S. A. Pelaez, C. Deline, B. Marion, B. Sekulic, J. Parker, B. McDanold,

J. S. Stein, in Conf. Record of the IEEE Photovoltaic Specialists Conf., Vol. 2020-June, IEEE, Calgary, AB, Canada, ISBN 9781728161150, ISSN 01608371, 2020, pp. 1757–1759, [https://doi.org/110.1109/](https://doi.org/110.1109/) PVSC45281.2020.9300379.
[23] N. Riedel-Lyngskær, D. Berrian, D. Alvarez Mira, A. Aguilar Protti,

P. B. Poulsen, J. Libal, J. Vedde, Appl. Sci. 2020, 10, 8487.
[24] R. E. Bird, C. Riordan, J. Clim. Appl. Meteorol. 1986, 25, 87. [25] R. Santbergen, T. Meguro, T. Suezaki, G. Koizumi, K. Yamamoto,

M. Zeman, IEEE J. Photovoltaics 2017, 7, 919.
[26] K. Jäger, L. Korte, B. Rech, S. Albrecht, Opt. Express 2017, 25, A473. [27] D. P. McMeekin, G. Sadoughi, W. Rehman, G. E. Eperon, M. Saliba,

M. T. Hörantner, A. Haghighirad, N. Sakai, L. Korte, B. Rech,
M. B. Johnston, L. M. Herz, H. J. Snaith, Science 2016, 351, 151.
[28] U. Rau, Phys. Rev. B 2007, 76, 085303. [29] M. T. Hörantner, H. J. Snaith, Energy Environ. Sci. 2017, 10, 1983. [30] B. Chen, S.-W. Baek, Y. Hou, E. Aydin, M. D. Bastiani, B. Scheffel,

A. Proppe, Z. Huang, M. Wei, Y.-K. Wang, E.-H. Jung, T. G. Allen,
E. V. Kerschaver, F. P. G. de Arquer, M. I. Saidaminov,
S. Hoogland, S. D. Wolf, E. H. Sargent, Nat. Commun. 2020, 11, 1257.
[31] Y. Hou, E. Aydin, M. De Bastiani, C. Xiao, F. H. Isikgor, D. J. Xue,

B. Chen, H. Chen, B. Bahrami, A. H. Chowdhury, A. Johnston,
S. W. Baek, Z. Huang, M. Wei, Y. Dong, J. Troughton, R. Jalmood,
A. J. Mirabelli, T. G. Allen, E. Van Kerschaver, M. I. Saidaminov,
D. Baran, Q. Qiao, K. Zhu, S. De Wolf, E. H. Sargent, Science 2020, 367, 1135.
[32] F. Sahli, J. Werner, B. A. Kamino, M. Bräuninger, R. Monnard,

B. Paviet-Salomon, L. Barraud, L. Ding, J. J. Diaz Leon,
D. Sacchetto, G. Cattaneo, M. Despeisse, M. Boccard, S. Nicolay,
Q. Jeangros, B. Niesen, C. Ballif, Nat. Mater. 2018, 17, 820.
[33] R. Santbergen, M. R. Vogt, R. Mishima, R. Mishima, M. Hino, H. Uzu,

D. Adachi, K. Yamamoto, M. Zeman, O. Isabella, Opt. Express 2022, 30, 5608.
[34] M. Jošt, B. Lipovšek, B. Glažar, A. Al-Ashouri, K. Brecl, G. Matic,ˇ

A. Magomedov, V. Getautis, M. Topic,ˇ S. Albrecht, Adv. Mater. 2020, 10, 2000454.
[35] A. Rohatgi, K. Zhu, J. Tong, D. H. Kim, E. Reichmanis, B. Rounsaville,

V. Prakash, Y. W. Ok, IEEE J. Photovoltaics2020, 10, 417.
[36] M. Jošt, L. Kegelmann, L. Korte, S. Albrecht, Adv. Mater. 2020, 10, 1904102. [37] J. J. Yoo, G. Seo, M. R. Chua, T. G. Park, Y. Lu, F. Rotermund,

Y. K. Kim, C. S. Moon, N. J. Jeon, J. P. Correa-Baena, V. Bulovi´c,
S. S. Shin, M. G. Bawendi, J. Seo, Nature 2021, 590, 587.
[38] E. L. Unger, L. Kegelmann, K. Suchan, D. Sörell, L. Korte, S. Albrecht,

J. Mater. Chem. A 2017, 5, 11401.
