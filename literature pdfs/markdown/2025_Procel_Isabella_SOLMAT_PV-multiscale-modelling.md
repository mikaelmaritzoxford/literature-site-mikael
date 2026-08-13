Solar Energy Materials & Solar Cells 293 (2025) 113864

Contents lists available at ScienceDirect

## Solar Energy Materials and Solar Cells

journal homepage: www.elsevier.com/locate/solmat

# PV multiscale modelling of perovskite / silicon two-terminal devices: from accurate cell performance simulation to energy yield prediction

a,* b b c c c d

P. Procel
, Y. Zhou, M. Verkou, M. Leonardi, D. Di Girolamo, G. Giuliano, O. Dupr´e, a a a c c c a,b

Y. Blom, M.R. Vogt
, R. Santbergen, F. Rametta, M. Foti, C. Gerardi, M. Zeman, a,b

O. Isabella a *Delft University of Technology, Mekelweg 4, 2628 CD, Delft, the Netherlands* b *PV Works B.V., Mekelweg 4, 2628 CD, Delft, the Netherlands* c *3SUN S.R.L., Contrada Blocco Torrazze Zona Industriale, 95121, Catania, Italy* d *CEA-INES, 50 Avenue du lac L*´*eman, Le Bourget-du-Lac, F-73375, France*
## ARTICLE INFO ABSTRACT

### Keywords: Recent conversion efficiency breakthroughs in double-junction (tandem) perovskite/crystalline silicon solar cells

Energy Yield demand advanced opto-thermo-electrical simulations, that are critical for translating laboratory results into Numerical Simulations realistic photovoltaic module and system performance. A holistic framework is here developed and presented, PV modules combining cell-level simulations, spectral analysis, PV module and PV system modelling. After validating the PV systems deployed physics models against measured cells and modules, hourly spectral irradiances for Delft, the Netherlands, and Catania, Italy, are generated and clustered into representative “blue-rich” and “red-rich” spectra. The effects of spectral variations on the current-matching and energy yield of tandem modules are quantified. Realistic module architectures are simulated, integrating dynamic temperature and spectrum data. Temperature coefficients are derived as a function of both irradiance and module temperature, significantly improving upon traditional indoor-derived values. Results show that standard indoor-derived coefficients under-/overestimate values in realistic conditions, highlighting the ultimate need for location-specific power matrixes. This study offers a robust pathway to predict tandem module energy yields across seasons and climates, supporting optimized design choices for industrial production and future PV installations.

## 1. Introduction

Multi-junction solar cells can achieve conversion efficiencies beyond the theoretical limit of single-junction architectures, the so-called Shockley-Queisser (SQ) limit [1]. Perovskite (PVK) on crystalline sili con (c-Si) tandem solar cells hold the greatest potential for ubiquitous photovoltaic (PV) terrestrial applications, owing to (i) much lower projected production and deployment costs than multi-junction solar cells based on III-V photovoltaic technology [2,3], (ii) conversion effi ciency already well above the SQ limit of single-junction devices and very close to 35 % [4], and (iii) TW-scale industrial basis ensured by c-Si PV market dominance [5]. Recently, 3SUN and CEA-INES demonstrated a PVK top cell combined with a silicon heterojunction (SHJ) bottom cell in a two-terminal (2T) configuration, achieving 30.8 % efficiency over a 9 cm 2 area [6]. This and many other industrial developments [7–10]

towards real-world deployment require a comprehensive approach that accounts for interactions across multiple spatial scales, from material properties and solar cell architecture to module integration and system-level operation under diverse environmental conditions and practical constraints [11]. Advanced opto-thermo-electrical modelling plays a crucial role in this respect, enabling performance assessment of design choices at the materials and cell levels, optimizing their combinations, and gauging their impact not only on module and system performance in real-world environments but also on capital and operational expenditures at the industrial level. The PVMD Toolbox [12,13] provides a holistic simu lation framework for modelling custom PV (multi-junction) cells, mod ules, and systems in various operating conditions, covering the whole PV value chain from materials to cell, modules and systems up to the AC-side yield and power output time series. That is achieved by means of

* Corresponding author. *E-mail address:* p.a.procelmoya@tudelft.nl (P. Procel).
[https://doi.org/10.1016/j.solmat.2025.113864](https://doi.org/10.1016/j.solmat.2025.113864)

Available online 30 July 2025

This article is part of a special issue entitled: SiliconPV 2025 published in Solar Energy Materials and Solar Cells.

Received 12 May 2025; Received in revised form 18 July 2025; Accepted 22 July 2025

0927-0248/© 2025 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

*P. Procel et al. Solar Energy Materials and Solar Cells 293 (2025) 113864*
**Fig. 1.** Flow diagram of the in-house developed simulation framework adopted in this study, illustrating the sequential stages from spectra clustering (stage 0) and

optical modelling (stage 1) to AC energy yield and power series analysis (stage 7). Besides some preliminary inputs, each numbered (time-resolved) stage integrates

key computational processes, accepts certain inputs from previous stages and carries out outputs for next stage(s).
 a multi-step modelling approach, wherein each step addresses a distinct spatial scale (interface, cell, module, system). The outputs from one step function as consistent inputs for the next, ensuring an integrated anal ysis of the causal relationships between design decisions and resulting performance metrics. This methodology, that we call *PV multi-scale* *modelling*, enables precise tracking, analysis, and optimization of sin gle- and multi-junction solar cells behavior, allowing for targeted im provements in real-world system applications. Through accurate simulations, the *PVMD Toolbox* provides critical insights into material and structural configurations, enabling the optimization of power output at the module level and energy yield at the system level. Multiple studies have demonstrated that the PVMD Toolbox can be used to optimize monofacial and bifacial multi-junction devices [14,15]. Addi tionally, it has been applied to the simulation of floating PV systems [16] and photovoltaic-thermal systems [17], highlighting the versatility of the toolbox. Ultimately a comprehensive understanding of how design choices influence real-world performance is provided, supporting the advancement of high-efficiency tandem solar technologies with enhanced robustness, reliability, and suitability for practical deploy ment. Key novel features include the implementation of spectral clus tering routines, the ability to simulate arbitrary module typologies and the consistent incorporation of geometric layout and electronic protec tion. While specific aspects for energy yield simulations of tandem solar cells have been addressed in previous studies [18–23], the novelty of the PVMD Toolbox lies in the holistic integration of these elements within a single, coherent platform. This enables detailed performance evaluation at the cell, module and system levels, with consistent physical coupling across the entire simulation chain. In this work, we validate the PVMD Toolbox with respect to 3SUN’s SHJ cells and modules, as well as 3SUN/CEA-INES 2T tandem cells, to analyze the performance of yet-to-be-fabricated tandem modules first under standard test conditions (STC) and then as function of spectral irradiance. Specifically, we investigate the effects of various surface texturing, wafer formats (M2 vs. G12), wafer cuts (double-cut vs. triple- cut vs. no-cut), module topologies (standard sub-module strings vs. butterfly configurations), and locations on the energy yield in two lo cations. The first part of this study focuses on validating our modelling approach for both single-junction and tandem solar cells. Based on our
validated parameterization, we then optimize the solar cells and compare their light management by analyzing the current densities of different tandem device architectures as function of the interface morphology between the top and bottom solar cells. In the second part, we extend our validation and analysis efforts to the module level, where we develop module archetypes based on both single-junction and tan dem solar cells. We simulate their performance and power output under STC, assessing the impact of different design configurations. In the third part, we transition to the system level, where we simulate the perfor mance of PV systems endowed with previously set up modules in real- world locations. This step ensures the technological consequences of all production choices made at the cell level are reflected all the way through to the system level, allowing for a comprehensive evaluation of their impact. In the last part of our study, our holistic simulation framework is employed to study the effect of spectral irradiance on the performance of 2T tandem-based PV modules, demonstrating that the temperature coefficients of such PV modules in realistic conditions do depend on the spectral irradiance too. This approach not only deepens the understanding of spectral effects on photovoltaic systems but also supports the design of more robust and location-adaptive solar technologies.

## 2. Methodology

Fig. 1 presents a flow diagram outlining the in-house developed

simulation framework employed in this study (the so-called PVMD toolbox). The diagram illustrates the stages of the modelling framework, beginning with optical simulations and progressing through to the AC- side energy yield analysis. Each step integrates essential computa tional processes, including spectral irradiance clustering, ray tracing, irradiance transposition, thermal modelling, semiconductor physics simulation, and lumped element method for power output evaluation. This holistic framework enables a detailed and integrated performance assessment of custom photovoltaic systems under realistic operating conditions. The optical system is initially defined in stage 1 by specifying the optical layer stack. Ray and wave optics modelling are then applied using our in-house developed software, GenPro4 [24], to compute the

**Fig. 2.** Flowchart of Stage 5 (Semiconductor Physics). Among the input parameters we enlist permittivity (*ε*), temperature (T), mobility (μ), electron affinity (χ),

band gap (Eg), tunneling mass of electrons and holes (mt(•)), carriers’ density or doping concentration (N(•)), density of states (DOS). The input parameters are fed to

various physical models and are coupled with the semiconductor equations: the Poisson equation and the continuity equation, where J(•)stands for the current

density of electron or holes. Such equations are solved consistently with the Fermi-Dirac statistics, where E, EFand kBare energy, Fermi energy, and Boltzmann

constant, respectively. The results are represented as band diagrams, spectral response spectra, current density – voltage (J–V) curve, and losses breakdown. This

figure is adapted from Ref. [38].

absorption profile in each layer of the (multi-junction) solar cell. The resulting output is used as input for stage 2, where the absorptance in the cell (or in each sub-cell in case of a multi-junction solar cell) is quantified as a function of wavelength and incident angle, and as the generation profile used as input for stage 5. The incident light spectrum (also known as spectral irradiance) is used as input for stage 1. Initially assumed to be the standard AM1.5 spectrum, this input can be varied in stage 0, known as *spectra clustering* (see Section 2.5), which is employed in the last part of this work to study the impact of spectral variations on tandem PV modules performance (see Section 3.5). In general, our modelling framework can be adapted to employ specific spectral irradiances enabling the modelling of a wide range of applications from space environment to any global terrestrial locations. In stage 2, the computed absorption profile is utilized by the system’s ray-tracing software, Lux, which is another in-house developed tool. Incorporating key parameters such as module dimensions, mounting height, azimuth, tilt, and environmental boundary conditions, such as albedo [25], Lux calculates a *sensitivity map*, which characterizes the absorptance in each solar (sub-)cell for every element in which the sky is meshed (*sky element*) as a function of wavelength, including ground-related reflection. This methodology enables the simulation of entire PV module arrays extending computations in both lateral (left- right) and longitudinal (forward-backward) directions. The resulting data are used as input for the next computational stage. Knowing tilt and azimuth, setting the mounting location, and considering the skyline profile [26], stage 3 introduces time-dependent simulation of irradiance on the plane of array using the transposition model approach. The Perez model [27] is employed to reconstruct the *sky map* [25] for each hour of the year (or other needed time step), enabling dynamic simulations. A sky map quantifies the irradiance contribution from each sky element. Here, we use location-dependent direct normal irradiance and diffuse horizontal irradiance obtained from Meteonorm [28] and the *Simple Model of the Atmospheric Radiative* *Transfer of Sunshine* (SMARTS) [29] to account for the spectrum of irradiance. More recently, we have also implemented a version

incorporating SBDART [30], which provides spectral shaping while accounting for cloud cover and illumination-dependent spectral varia tions. The transposition model integrates the various irradiance com ponents onto the plane of the array. At this stage, we compute the absorbed irradiance at the module level, which is the primary output of this stage. Additionally, the second key output of the transposition model is the implied photocurrent density of the (sub-)cell(s), which is used in subsequent modelling stages. The absorbed irradiance from stage 3 is then used as an input for the thermal model in stage 4. Our PVMD toolbox can employ multiple thermal models, ranging from simple empirical models such as the Sandia [31] and Faiman [32] models to advanced fluid dynamics-based models [33]. These models require additional inputs, including ambient temperature, wind speed, convective heat transfer coefficients, and the coefficient of vertical diffusion [33] of the module’s glass. A key feature of the thermal models is their capability to calculate the temperature of each individual solar cell, allowing for the assessment of temperature variations caused by potential shading effects. The primary output of this stage is the temperature distribution across the solar cells composing the PV module. In stage 5, we use the generation profile from stage 1 along with the electronic parameters of the materials in the solar cell. This stage ac counts for semiconductor physics, employing a finite element method (FEM) using either TCAD Sentaurus [34] for 2D and 3D simulation do mains or our in-house developed Advanced Semiconductor Analysis (ASA) software [35–37] for 1D simulation domains. Here, we solve the fundamental semiconductor equations governing solar cell operation. The result is a set of current density-voltage (J-V) curves as a function of irradiance (G) and temperature (T) ranges. From these J-V curves, we extract the parameters describing the one-diode model of solar cell for any given irradiance and temperature within the previously modelled ranges. In stage 6, we employ a calibrated compact model that integrates outputs from the semiconductor physics block (stage 5), the trans position model block (stage 3), and the thermal model block (stage 4) to

**Fig. 3.** Sketch of single- and double-junction solar cells used in this work: (a) baseline bifacial SHJ, (b) mono-like bifacial SHJ (also known as monofacialized), and

(c) tandem solar cell consisting of a top perovskite solar cell and a bottom SHJ solar cell. Note, despite being sketched as flat for ease of representation, both single-

junction SHJ cells employ front and rear textured c-Si bulk. On the other hand, the tandem solar cell is evaluated for different interface morphologies at the front,

between the top and bottom cells, and at the rear bottom cell interface. The configurations considered are: F/F – flat interfaces at both the top/bottom junction and

the rear side, with a conformal top cell; F/T – a flat interface between the top and bottom cells and a textured rear side with a conformal top cell; T/T – both interfaces

are textured with a conformal perovskite layer; and T/T R – both interfaces are textured, with a repleted top cell.

ensure a comprehensive assessment of the interdependencies between irradiance, temperature, and electrical performance, enhancing the ac curacy of the overall PV module simulation. This model further in corporates module-specific properties, such as module dimensions (consistent with stage 2) and interconnection characteristics, which model resistive losses at soldering points and bypass diodes. The primary output of this stage is the digital twin of a PV module, which may contain solar cells that are either already commercially available or under development, such as tandem solar cells. Notably, stage 6 allows us to simulate PV modules that do not yet exist, providing a powerful tool for predictive performance and energy-yield analysis. Selecting different boundary conditions, this stage outputs the power output of the PV module in STC, defined as AM1.5 spectral irradiance, irradiance equal to 1000 W/m 2, 25◦C cell temperature, and zero wind speed, or in realistic conditions, where irradiance and temperature vary dynamically over time according to meteorological input. Since this stage is time- resolved, a dynamic evaluation of power output under realistic opera tional scenarios is enabled, accounting for environmental fluctuations throughout the day. Finally, in stage 7, we introduce different inverter types and models, allowing for the conversion of power flow from direct current (DC) to alternate current (AC). This stage enables the simulation of the AC-side energy yield (EYAC) and provides a time-series analysis of power output. In this study, we do not extend our analysis to stage 7. Instead, we focus on evaluating the power output and energy yield at the DC side (EYDC) of our devices. In the following sub-sections, we provide a detailed description of the semiconductor physics stage (stage 5), the compact modelling approach (stage 6), the input parameters required for PV module characterization (stage 2), the input information from module to PV system calculations in stage 6 and the spectral clustering approach used to estimate the time-dependent incident spectra. These components are critical for accurately modelling the opto-thermo- electrical behavior of the PV system and ensuring self-consistent reli able energy yield predictions.

### 2.1. Semiconductor physics simulations

To accurately model the opto-electrical behavior of advanced solar cell architectures, we employ the FEM approach to numerically solve the fundamental semiconductor equations. In this study, we utilize a 2D

simulation domain and, therefore, employ TCAD Sentaurus for model ling. This approach is particularly critical, as state-of-the-art solar cells exhibit ultra-low recombination currents (J0), minimal contact re sistivities, and high minority carrier lifetimes. Consequently, meaningful modelling must accurately capture the complex physical phenomena governing the performance of different solar cell architectures under evaluation. The flowchart depicting the simulation process for the semi conductor equations is shown in Fig. 2. The semiconductor equations require an extensive set of input parameters, including both geometrical configuration and optoelectronic properties of the materials constituting the solar cell under study. These parameters are incorporated into GenPro4 for optical modelling and into other physical models to accu rately simulate the physics of heterointerfaces, which is especially essential in multi-junction solar cells. Such models are then self- consistently coupled with the semiconductor equations and the Fermi- Dirac statistics, ensuring a rigorous representation of carrier distribu tion, charge transport, recombination mechanisms, and electrostatic potential variations. More details about this methodology are discussed elsewhere [38]. The primary simulation outputs include energy band diagrams, spectral response, J-V characteristics, losses breakdown, which are computed for each irradiance-temperature pair. This approach provides a comprehensive evaluation of solar cell performance under varying operating conditions. In this study, we analyze SHJ and perovskite/SHJ solar cells. Three solar cell architectures are investigated in this work. The first is the baseline bifacial SHJ solar cell, which allows light absorption from both the front and rear sides (see Fig. 3a). The second is the mono-like bifacial SHJ solar cell, a modified bifacial SHJ design featuring a mono-facial-like structure, aimed at improving the light absorption from only one side of the solar cell while using similar bifacial configuration as in the first architecture (see Fig. 3b). The third is the tandem solar cell, a double-junction solar cell architecture consisting of a perovskite top cell stacked on a SHJ bottom cell (see Fig. 3c). In the latter case, different interface morphologies are considered at three key interfaces: the front surface, the interface between the top and bottom cells, and the rear interface of the bottom cell (see Fig. 3d). These morphologies result in the following additional solar cell architectures.

**Table 1**

Summary of models and input material parameters. SRV stands for surface

recombination velocity.

|Crystalline Silicon (c-Si)||||||
|---|---|---|---|---|---|
|Bandgap narrowing|Schenk [42]|Intrinsic carrier density|9 3 cm at 9.65 × 10 300 K [43]|||
|Mobility|Klaassen [44]|SRV|0.01 cm/s|||
|SRH lifetime|40 ms [45]|Resistivity|2 Ω cm|||
|Thickness|160 μm|||||
|Crystalline Silicon (c-Si) (Bottom) SHJ solar cell|ITO [46]|Rear TCO|i-a-Si:H [46]|n-a-Si: H [46]|p-a-Si: H [46]|
|Electron affinity (eV)|4.9|4.9|3.9|3.9|3.9|
|Band gap (eV) (front/ rear)|3.1|3.1|1.93/ 1.86|1.84|1.69|
|Electron/hole mobility ¡1 ¡1 (cm² V s )|39/39|55/55|20/4|25/5|25/5|
|Relative permittivity|4|4|11.9|11.9|11.9|
|Electron/hole tunneling mass (m₀ *)|0.1|0.1|0.1|0.1|0.1|

⁃ **Flat/Flat (F/F)**: Both the interface between the top and bottom cells and the rear side of the bottom cell are considered flat, with a conformal perovskite layer; ⁃ **Flat/Textured (F/T)**: A flat interface between the top and bottom cells with a textured rear surface of the SHJ bottom cell. The oxide (ITO) as transparent conductive oxide (TCO) layer. As for the top perovskite top cell is conformally deposited over the flat interface cell of the double-junction device, the ETL stack consists of MgF2, C60, [39]; BCP, and ITO, while the HTL is based on the self-assembled monolayer ⁃ **Textured/Textured (T/T)**: The interface between the top and bot (SAM) 2PACz. The tunnel recombination junction is formed by the ITO tom cells as well as the interface at the rear side of the bottom cell are (part of the ETL of the bottom cell) and the SAM layer from the top cell. textured. The perovskite top cell is also conformally textured [40]; ⁃ **Textured/Textured Repleted (T/T R)**: Similar to the previous configuration, but with a repleted perovskite top cell [41].

These architectures are systematically evaluated to determine their impact on the performance of the solar cell in terms of J-V curves, fol lowed by the analysis at the module level in terms of power output, and ultimately at the system level in terms of energy yield. The electron and hole transport layer (ETL and HTL) stacks of both the single-junction SHJ solar cells and the bottom SHJ cells are based on hydrogenated intrinsic amorphous silicon (i-a-Si:H) passivating layer, n-type or p-type doped hydrogenated amorphous silicon (a-Si:H) layers, and indium tin

**Fig. 6.** Different module archetypes considered in this study: M2 endowed with either 1J or 2J solar cells, and G12-0, G12-1, G12-2, and G12-3 endowed with only

2J solar cells.

The physical models, the electronic parameters and the thicknesses used to simulate these solar cells are summarized in Tables 1 and 2.

### 2.2. Solar cell to PV module compact modelling

The compact modelling approach is used to parameterize the elec trical behavior of the solar cell based on the results obtained from the semiconductor physics simulation. Each J-V curve computed in the semiconductor physics stage (see Fig. 4) is utilized to extract the pa rameters of the compact model, which follows an equivalent circuit with single-diode representation of the solar cell as Fig. 5 illustrates. The one- diode model, represented by the following equation: [ ()] *q*(*V I*⋅*Rs*) *V I*⋅*RS* *I* = *Ioexp* 1 + *Iph*(1) *n*⋅*kB*⋅*T Rp*

is characterized by five parameters: I0stands for the reverse saturation current, Iphfor the photogenerated current, n for diode ideality factor, Rs for the series resistance and Rpfor the shunt resistance. These parame ters are determined through a numerical fitting procedure, where each parameter is expressed as a function of irradiance and temperature. The resulting functional dependencies allow for the reconstruction of the J-V characteristics at any given moment, dynamically adjusting according to irradiance and temperature variations based on a specific meteorolog ical input. For power output analysis, this methodology extends beyond STC by allowing irradiance and temperature to vary while maintaining perpendicular illumination to the PV module. This approach, often referred to as pseudo-STC, provides a more realistic assessment of PV module performance under real-world conditions, bridging the gap be tween standardized testing and dynamic operational environments. Moreover, this parameterization framework is not limited to STC but is designed to account for a wide range of operating conditions, enabling

**Table 3**

Module archetype name Properties M2 G12-0 **Wafers size** Triple-cut M2 Triple-cut G12 **Wafers number** 216 120 **Configuration** Three strings in parallel per half-Three strings in parallel per half- module module **Bypass diode** 3 3

**(s)**
**Layout** Butterfly Butterfly **Cells type** 1J Bifacial, Monofacialized 2J T/T 2J F/F, F/T, T/T, T/T R **Area** 1.904 m² 1.896 m²

accurate modelling of PV module behavior across varying environ mental scenarios. In this study, whichever spectral irradiance used as input of stage 1, that once integrated over the wavelength range yields a certain irradiance value, is scaled up or down with a wavelength- independent constant value to account for the spectral richness of the input light while allowing to seamlessly simulate the solar cell behavior from low light to high light illumination regimes:

∫ *λ* 2 *Gs*= *s*⋅*G* = *s*⋅ E(*λ*)*dλ* [2] *λ* 1

where G is the *scaled* irradiance (W⋅m 2 ), s is the scaling factor, which is s a real number greater than 0, G is input irradiance value, E(λ) is the input spectral irradiance (W⋅m 2 ⋅nm 1 ), λ and λ are the wavelength 1 2 boundaries. By implementing this parameterization strategy, the compact model is used as a computationally efficient yet highly accurate representation of the solar cell’s electrical performance. This approach ensures that dynamic variations in operating conditions, such as fluctuations in irradiance, temperature, and environmental factors, are accurately captured in time-resolved simulations, providing a robust foundation for subsequent energy yield predictions and system-level analysis.

### 2.3. PV modules design

To comprehensively assess the modelling of PV modules under par tial shading conditions, various module configurations are considered for both single-junction and double-junction solar cells. The module archetypes evaluated in this study are presented in Fig. 6. The M2 reference module is used as the baseline for simulating single-junction (1J) bifacial or monofacialized solar cells as well as double-junction (2J) devices. This module consists of 216 triple-cut M2

G12-1 G12-2 G12-3 Half-cut G12 Full size G12 Full size G12 80 40 40 One string per half-One string per half-One string per module module module 1 1 1

Butterfly Butterfly Standard 2J T/T 2J T/T 2J T/T

1.996 m² 1.989 m² 1.997 m²
Summary of properties and solar cell types used in various module archetypes considered in this study.

**Fig. 7.** Average red-rich spectral irradiance (red-solid line) recorded between 9:00 and 10:00 on the June 6, 2022 at the PV outdoor monitoring station of Delft

University of Technology in Delft (the Netherlands). Colored-dashed curves are modelled spectral irradiance curves for the same location and different moments of

the day. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

wafers, arranged in three strings in parallel per half-module (i.e. 36 triple-cut wafers per string), and incorporates three bypass diodes to mitigate shading-induced losses. Each bypass diode connects one string from the top half-module to the related string from the bottom half- module. The total area of the module - edge-to-edge including the aluminum frame-is 1.904 m 2. For double-junction (2J) architectures, we also consider other four PV module archetypes based on the G12 wafer size, see Table 3. All module archetypes but G12-3 include a middle section width of 13.6 mm to accommodate the bypass diode(s). All module archetypes are glass-to-glass while the M2 module based on 1J monofacialized SHJ cell is glass-to-back sheet. Each glass sheet is 2- mm thick and endowed with ARC [54]; the EVA layers employed are UV-transparent. In this study we have not adjusted the cell ARC to better match the module encapsulation.

### 2.4. PV systems configuration

The PV system configuration is set at stage 2 of our modelling framework (see Fig. 1). This study specifically considers PV systems deployed in two distinct geographical locations: Delft (the Netherlands) and Catania (Italy). Fig. 8 presents a schematic view of the archetype PV system. As both sites are situated in the Northern Hemisphere, the PV arrays are oriented with an azimuth angle directed southward to optimize solar energy capture. The tilt angle is location-dependent and is typically chosen for optimizing annual production. However, in this study we fixed the tilt angle value to 25◦, which maximizes annual production during summer in both locations. This is because differences in latitude matter less in summer as both locations have relatively high solar ele vations (up to 61◦in Delft and 73◦in Catania). The height at which the module is mounted (hM) is set to 1.5 m, which is the distance between ground and the bottom edge of the PV module and ensures a uniform treatment of the ground-reflected irradiance component [55]. The al bedo (α) is set to 0.2, implying that 20 % of the incident solar irradiance on the ground is reflected. That is, no explicit assumptions are made regarding the ground surface material, since the reflected spectral irra diance has the same shape as the front incident spectral irradiance with the value of the wavelength-integrated reflected irradiance being 20 % of the value of the front incident irradiance. This is a numerical process just like that previously reported in Equation (2). The horizon is considered free from obstructions, ensuring an unre stricted sky view factor for the PV module and system. Nevertheless, the

**Fig. 8.** Schematic view of PV system scene as input in stage 2 of our model

ling framework.

model is fully capable of integrating scenarios with obstructed horizons, such as those encountered in urban or complex terrain environments, allowing for the calculation of shading effects and their impact on sys tem performance. The modelling methodology for PV system simula tions has been rigorously validated and previously reported in Refs. [56, 57] ensuring the accuracy and reliability of the presented results.

### 2.5. Clustering of spectral irradiances

Multi-junction solar cells, especially in 2T configuration, are highly sensitive to the incident spectral irradiance, which varies significantly with geographic location, time of day, and atmospheric conditions. Accurately capturing and analyzing these spectral variations is essential for realistic performance assessment and further optimization. In this study, we present a spectral clustering methodology to classify irradi ance data into representative spectral profiles, specifically, *blue-rich* and *red-rich* types, thus enabling a more precise evaluation of their impact on tandem device behavior while minimizing the computational efforts. In the initial stage, the SMARTS model [58] is used to generate hourly spectral irradiance data for a specific location over the course of

**Fig. 9.** Modelled hourly spectra assigned to the corresponding time slots, where each row represents the month of the year, and each column represents the hour of

the day. The number in each cell indicates the number of unique spectra modelled by SMARTS at the each (month, hour) pair in Delft, the Netherlands. 4497 spectral

irradiances were modelled for Delft at each hour of each month of the year. The white-colored cells bear no information, as the sun disk was below the horizon, so no

spectral irradiance could be extracted.

an entire year. This model computes clear-sky spectral irradiance based on user-defined atmospheric conditions. In essence, it captures the ef fects of atmospheric variability, such as temperature, pressure, aerosol concentration, and water vapor content, on the spectral distribution of solar irradiance across different wavelengths. An example of how the spectral irradiance can be different than the standard AM1.5 spectrum and varies during a certain day in a certain location can be found in

Fig. 7.

The resulting spectral outputs are organized into a time-resolved matrix, where hourly spectra for each day of the year are grouped into predefined time slots. Fig. 9 illustrates such a spectral clustering approach for the location of Delft. In this matrix, each row represents a month of the year, and each column corresponds to an hour of the day. For instance, the cell at the (January, 10) intersection contains all modelled spectra for 10:00 time across the 31 days of January. The number of spectra in each cell indicates how frequently those specific spectral conditions occur at that time during the month. Following this, the spectra within each time-cell are aggregated to produce a single representative spectrum, calculated as the global hor izontal irradiance (GHI)-weighted spectrum. This process involves the following three key steps. First, calculate the GHI for each spectrum by integrating the spectral irradiance over the defined wavelength range:

∫ *λ* 2 *GHI*(*i*) = *E*(*i, λ*)*dλ* (3) *λ* 1 Second, determine the weight of each spectrum, w(i), by normalizing the related GHI to the total GHI within the (month, hour) pair, which contains *n* spectra:

*GHI*(*i*) *w*(*i*) = *i*=*n*

(4)
∑ *GHI*(*i*) *i*=1 Third, compute the GHI-weighted average spectral irradiance by applying the weights to each spectrum and summing over all *n* spectra:

∑ *i*=*n* *E* *w*

(*λ*) = *w*(*i*)⋅*E*(*i, λ*) (5) *i*=1
where *E* (*i*,*λ*) is the spectral irradiance of the *i*-th spectrum within a given (month, hour) pair, w(i) denotes the corresponding weight, *n* is the total number of different spectral found per month, and *Ew*(*λ*) is the GHI-

**Table 4**

Blu-rich and red-rich classification conditions applied to representative

spectral irradiances.

Blue-rich Red-rich *GHIw,s,blue* *>* *GHIw,s,redGHIw,s,blue* *<* *GHIw,s,red* *GHIAM*15*,blueGHIAM*15*,redGHIAM*15*,blueGHIAM*15*,red*

weighted spectrum representative of that (month, hour) pair. This pro cess reduces the number of spectra within each cell to a single GHI- weighted spectrum, enabling a more computationally efficient and yet representative analysis of spectral variation effects on tandem devices. In total, for Delft location, we could reduce the total number of spectral irradiances from 4497 to 159. Each GHI-weighted spectrum is subse quently scaled (E) to match the reference AM1.5 spectrum (1000 W/ m 2 ): w,s

4000 ∫ *E* *AM*1*.*5*G*(*λ*)*dλ* 2801000 *E* *w,s*(*λ*) =4000⋅*Ew*(*λ*) = ⋅*Ew*(*λ*) (6) ∫ *GHIw* *E* *w*

(*λ*)*dλ*
280 The representative GHI-weighted spectra are integrated into two spectral regions: blue (300 – cutoff wavelength nm) and infrared (IR) (cutoff wavelength – 1200 nm). The cutoff wavelength corresponds to the wavelength at which the spectral response of the top cell is exceeded by that of the bottom cell in our tandem configuration (see Section 3.1.2 for this specific study). To determine the spectral “richness,” the GHI contributions for both spectral regions are computed by integrating the spectral irradiance over their respective wavelength intervals: *λ* ∫ *cutoff* *GHIw,s,blue*= *Ew,sdλ* (7) 300

1200 ∫ *GHIw,s,red*= *Ew,sdλ* (8) *λ* *cutoff* By comparing these values to those obtained from the reference AM1.5 spectrum, each spectrum is classified as either blue-rich or red-

**Fig. 10.** Classification of the 159 representative hourly spectral irradiances as blue-rich (light blue cells) or red-rich (light red cells) in Delft, the Netherlands. The

yellow-highlighted column indicates the set of 3 red-rich and 9 blue-rich spectral irradiances at 13:00 h (one per each month of the year). This is used for a sanity

check of our modelling approach of 2J solar cells (see Section 3.1.2). (For interpretation of the references to color in this figure legend, the reader is referred to the

Web version of this article.)

**Fig. 11.** Representative blue-rich and red-rich spectral irradiances modelled for Delft, the Netherlands (left) and Catania, Italy (right). The described pair-wise

clustering approach finally led to 8 spectra for Delft: 1 for blue-rich and 7 for red-rich. In the case of Catania, 7 representative spectra were found: 1 for blue-

rich and 6 for red-rich. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

rich according to the conditions in Table 4, based on the relative enhancement in the corresponding wavelength region. For instance, assuming a cutoff wavelength of 740 nm, the classifi cation results for blue-rich and red-rich spectra in Delft are presented in

Fig. 10. Red-rich spectra predominantly occur during the winter months

and in the early morning or late afternoon hours, periods when the sun is low on the horizon. Conversely, blue-rich spectra are more common during the summer months and around midday. This distribution aligns with physical expectations, as low solar elevation angles result in longer atmospheric paths, which increase scattering and absorption of shorter wavelengths, thereby enriching the red component of the spectrum. Due to the large number of unique spectra generated, which signif icantly impacts the computational time required for subsequent energy yield simulations, we implemented a further clustering strategy within each spectral group (blue-rich and red-rich). Specifically, we performed a pairwise comparison of spectral shapes using two statistical parame ters: the coefficient of determination (R 2 ) to assess shape similarity, and the root mean square error (RMSE) to evaluate intensity differences. For the Delft location, by applying a clustering threshold of R 2 = 0.90, we were able to reduce the 73 unique blue-rich spectra to a single repre sentative spectrum, and the 86 red-rich spectra to 7 representative spectra, with corresponding RMSE values of about 0.1 W/m /nm in both cases. The representative spectral irradiances found for Delft and

Catania after the described clustering process are reported in Fig. 11. The spectral clustering methodology introduced in this work pro vides a novel and accurate alternative to conventional irradiance modelling by accounting for both the total incident power and its spectral shape. This level of detail is particularly critical for 2T 2J solar cells, which are highly sensitive to spectral variations driven by geographic location, time of day, and atmospheric conditions. Unlike simplified approaches that rely solely on scaled AM1.5 spectra, our method enables the classification of real-world irradiance data into representative spectral profiles thereby providing a more realistic and nuanced understanding of how spectral quality influences device behavior and energy yield. Finally, it is worth mentioning that the simulations presented in this study are based on a representative fabricated device and follow a deterministic approach. However, the PVMD Toolbox is equipped to incorporate statistical input distributions, allowing for uncertainty and sensitivity analyses across the full simulation stack, from material and device to module and system levels.

**Table 5**

External parameters of the modelled solar cell relative to the baseline SHJ de

vice. The “Optimized” column reflects performance gains after iterative device-

level enhancements, while the “Monofacialized” column includes additional

improvements obtained by simulating a monofacial configuration with a

reflective white backsheet.

External Measured Modelled Optimized Monofacialized

|External|Measured|Modelled|Optimized|Monofacialized|
|---|---|---|---|---|
|Parameter|Baseline|Baseline|||
|ΔJ [mA/cm²]|0.48|0.00|+0.160|+0.800|
|ΔV [V]|0.00|0.00|+0.005|+0.000|
|ΔFF []|0.00|0.00|+0.019|+0.019|
|Δη [%]|0.29|0.00|+0.780|+1.170|

SC OC

abs

**Fig. 12.** EQE comparison between simulated and measured spectra of the

tandem solar cell.

**Table 6**

Comparison of measured external parameters of the tandem 2T baseline solar

cell relative to those of the modelled tandem 2T baseline solar cell.

External Measured Modelled Parameter Baseline Baseline 2 ΔJSC[mA/cm] 0.110 0.00 ΔVOC[V] 0.020 0.00 ΔFF [] 0.008 0.00 Δηabs[%] 0.460 0.00

## 3. Results and discussion

### 3.1. Validation of solar cells and PV modules modelling

#### 3.1.1. SHJ solar cells

In the cell level simulations (stage 5 of our modelling framework), the initial step involves validating the model by comparing the simu lated performance and external parameters with experimental data ob tained from the baseline bifacial c-Si SHJ solar cell. In Table 5, the simulated external parameters (short-circuit current density, JSC, open- circuit voltage, VOC, fill factor, FF, and conversion efficiency, η) of the baseline device are considered as the reference, and their variation is reported with respect to the values measured from the fabricated base line device. The comparison shows a deviation of only 0.3 % absolute from the measured performance of VOCand FF. This almost perfect match indicates excellent agreement between the results of our model ling framework and the reference solar cell, implying the appropriate capturing of the physics and charge carriers transport mechanisms at play in such types of solar cells. The optical bifaciality factor, that is the ratio of the implied photo-current density (Jph) at the rear side over the J phat the front size (Jph-rear/Jph-front), is 92.91 % as calculated for normal incidence of light. Subsequently, we apply a series of iterative processes to enhance the performance of the baseline device. This optimization process is carried out under industrially feasible conditions. Specifically, we consider three optimization steps: (i) transport layer thickness modification, (ii) adjustment of the c-Si bulk resistivity, and (iii) implementation of a higher mobility TCO as an alternative to ITO. Following these im provements, we evaluate the performance of the resulting so-called best- performing solar cell. We observe that the calculated external parameter values exhibit a significant improvement across all metrics compared to the simulated baseline solar cell, except for VOC, which exhibits only marginal enhancement. For comparison, we also simulate a mono-facial version of the best-performing (originally bifacial) solar cell. To this end, an EVA encapsulant and a highly reflective back sheet, modelled as a Lambertian scatterer (white back sheet simulation), are included on the rear side of the solar cell. The calculated external parameters for this mono-like configuration show a further enhancement compared to the bifacial *best-performing* cell, particularly with an increase of 0.8 mA/cm in JSCand a 1.17 % absolute gain in overall efficiency.

**Fig. 13.** J-V curves of calibrated tandem solar cell as function of twelve spec

tral irradiances representing illumination input in Delft at 13:00 h.

#### 3.1.2. Tandem perovskite/SHJ solar cells

For the validation of the simulated tandem solar cell, we use as a reference a previously reported device exhibiting a certified power conversion efficiency of 27.1 % [59]. The standard tandem stack con sists of a perovskite top cell monolithically integrated with a bottom c-Si SHJ solar cell, as illustrated in Fig. 3c. At this stage, all interfaces within the tandem architecture are simulated as flat.

Table 6 presents the differences between the modelled and measured

external parameters of the tandem solar cell, using the simulated values as the reference. The discrepancies are minimal, indicating a reasonable agreement between the fabricated and simulated devices. It is worth noting that our simulation platform includes a detailed analysis of the perovskite top cell, accounting for surface recombination, passivation effects, and charge transport mechanisms consistently coupled at het erointerfaces [60,61]. The opto-electronic model of the tandem device is further validated by comparing the simulated and measured EQE spec tral response, as shown in Fig. 12. We observe an almost perfect match between the top, bottom, and tandem solar cells across the entire wavelength range of interest (300–1200 nm), indicating that the model accurately replicates the physics of the tandem structure. Note that for the tandem device simulations, the SAM/ITO interface play a crucial role on device performance due to its influence on the energy alignment

**Table 7**

Dependency of the tandem solar cell JSCon blue-rich and red-rich spectra. In all months but February the JSCvalues of the

of the sub-cell limiting the spectral response of the tandem device.

tandem device align with the JSC

**Table 8**

Summary short-circuit current

density (J of ) theSCand absolute efficiency gains for different

tandem solar cell morphologies, relative to the

flat/flat (F/F) reference structure and the

monofacial single-junction reference device.

between the top and bottom solar cells in the tandem architecture. Simulations indicate that variations in this alignment can lead to sig nificant changes in tandem efficiency. The configurations analyzed in this work correspond to conditions consistent with the experimentally observed device behavior (see Fig. 13). To further validate our modelling approach, we simulate our cali brated tandem solar cell using as input the twelve spectral irradiances highlighted in Fig. 10 at 13:00 h of the day in Delft, the Netherlands, while forcibly keeping the solar cell temperature at 300 K. Note, each of these location-related spectra is the representative spectrum for each month of the year at a given time. This means every day of a specific month (e.g. 31 days in January) would have the same spectrum at a specific time. The purpose of this test is to isolate the effect that blue-rich and red-rich spectral irradiances have on the device JSC. Specifically, as we can calculate the spectral response of both sub-cells and compute their photo-current density, we can observe which sub-cell limits the JSC of the whole tandem solar cell and verify if expectations are met. As blue-rich (red-rich) spectrum provides more (less) input light to the top cell, the JSCof the tandem device is expected to be limited by that realized by the bottom (top) sub-cell. For this test, we used 740 nm as cutoff wavelength (see Equations (7) and (8)) as visible in Fig. 12. The resulting J-V curves of this consistency check are reported in Fig. 1, aligning well with the variation of illumination condition from low (January) to high (June) to low (December) spectral amplitude. In

Table 7 we report the dependency of the tandem solar cell JSCon

different input spectra. In all months we note the JSCvalue of the tandem device is very close to the JSCvalue of the sub-cell limiting the spectral response of the tandem device. In the months of February and October the difference between JSC-topand JSC-botis the smallest, resulting in either opposite (February) or undecided (October) solution. Following the validation of our simulation methodology and using

the reference tandem solar cell, we investigate the impact of different interface morphologies on the performance of the tandem solar cell.

Fig. 3d schematically represents the four configurations under analysis:

F/F, F/T, T/T, and T/T R (see Section 2.1). In this study, for modelling the top sub-cell, we assume the same electrical parameters across all tandem configurations; thus, the primary differences are in JSCdue to differences in light management.Table 8 summarizes the variation in JSC relative to the F/F structure, which is used as the reference. A significant enhancement in JSCis observed upon introducing any form of interface texturing, particularly under current-matching conditions. As expected, the highest improvement is achieved with the T/T structure, yielding an increase of 2.35 mA/cm 2 compared to the reference F/F device. For comparative purposes, we also evaluate the performance of all tandem configurations against the monofacial version of the best-performing single-junction solar cell. All simulated tandem devices demonstrate a minimum absolute efficiency gain of 2.51 % over the monofacial reference, as seen in the F/F configuration. Specifically, the F/T, T/T, and T/T R morphologies achieve further efficiency improvements of

3.27 %, 4.41 %, and 3.41 % absolute, respectively.
#### 3.1.3. Validation of PV module simulations

To validate stage 6 of our modelling framework, we simulate a commercial monofacial PV module under our partial shading scenarios (see Fig. 14). The PV module consists of 144 M2-sized half-cut solar cells, each featuring six busbars with fingers. The electrical topology is butterfly-type with two half-modules, six sub-strings connected in par allel (three per half-module), each pair of top and bottom strings pro tected by bypass diodes (three in total). The dimensions are 1938 mm in height and 978 mm in width, for a total area of 1.895 m 2. This PV module configuration closely matches the topology used in our M2 archetype (see Fig. 6). A specific shading pattern with different transparency is applied across the surface of the PV module surface to emulate the effect of a shading object. In this case, we use a material that attenuates approxi mately 50 % of the incident light. The current-voltage (I-V) and power- voltage (P-V) characteristics of the shaded module are then measured and compared against the corresponding simulation results. In Fig. 14 we show the results related to the shading pattern number 12, where the characteristic activation of the bypass diodes is clearly observed, resulting in altered PV module’s behavior compared to the fully illu minated reference case at 1000 W/m 2. Our simulation platform suc cessfully replicates the module’s electrical response, showing reasonable agreement with the measured data, despite (i) not having used the spectral transmittance of the shading element and (ii) not having precise information at our disposal on the bypass diodes employed in the commercial module. It is worth noting that this validation is successful in all other tested shading patterns.

**Fig. 14.** Visual rendering of the front (a) side of the investigated commercial monofacial PV module under specific partial shading (pattern number 12 with fully or

partially light-blocking material). Comparison between measured and simulated current–voltage (I–V) (b–c) and power–voltage (P–V) (d–e) characteristics in un

shaded condition, full light block pattern 12 and 50 % light block pattern 12 (half-shaded).

**Fig. 15.** Simulated relative power output variation (ΔPout, %) for different PV module archetypes under standard test conditions (STC). Note that the M2-type

module with bifacial SHJ is used as reference (0 %). The comparison includes both single-junction (1J) and tandem (2J) configurations, as well as advanced

G12-based modules based on tandem cells with T/T morphology.

### 3.2. PV module simulations in standard test conditions (STC) The reference point (0 %) corresponds to the power output under STC of

the M2-type module employing the best-performing monofacial SHJ After having successfully validated the modelling stages pertaining solar cell. The analyzed M2 module configurations include both 1J and to solar cells and PV modules, we can move on by calculating (and 2J solar cell technologies (see Table 3). For 1J solar cells, we simulate comparing) the performance of the five PV module archetypes reported M2 modules using the best-performing SHJ solar cells in both mono in Fig. 6. Fig. 15 illustrates their relative power output variation (ΔPout). facial and bifacial layouts. For 2J solar cells, we evaluate M2 modules

**Fig. 16.** Horizon profiles used in the PV system simulations. The curves represent altitude angles as a function of azimuth, corresponding to two scenarios: (left) an

unobstructed (free horizon) and (right) an urban skyline profile.

incorporating various interface morphologies: F/F, F/T, T/T, and T/T R. Beyond the M2-based modules, four G12-type modules are simulated: G12-0, G12-1, G12-2, and G12-3. They are all endowed with 2J solar cells with T/T morphology (see Table 3). Focusing on the M2 modules, switching from 1J to 2J solar cell technology brings a solid boost in power output. To the net of eventual changes in electrical performance of the top cell due to the presence of surface texturing, the performance of the 2J-based M2 modules endowed with the different morphologies follows the same trend as the one presented in Table 8. Also at the module level, the 2J T/T solar cells yield the highest performance. Then, comparing the 2J T/T solar cell technology across our five PV modules archetypes, the G12-0 module achieves the highest simulated performance, with a relative power output increase of 29.9 % with respect to reference 1J M2 monofacial module. This performance enhancement results not only from the inte gration of higher-efficiency tandem cells but also from a well-optimized current-voltage balance, which aligns with the electrical and geomet rical design constraints of the G12 module architecture. Between the M2 (T/T) module (216 triple-cut cells) and the G12- 0 module (120 triple-cut cells), they exhibit similar power outputs, with the G12-0 performing slightly better. Although the current in the M2 configuration is lower compared to that of the G12-0, the overall power output remains comparable. The G12-0 module has a lower number of series-connected cells (and thus a lower number of associated

soldering points) than the M2 module but also realizes a higher current level due to larger wafer cuts. Such a higher current level increases Joule effect-related ohmic losses that partially offset the advantage of having a lower number of soldering points where additional resistive losses may occur. Furthermore, increasing the cell size from triple-cut (G12-0) to half-cut (G12-1) and full-size formats (G12-2 and G12-3) results in reduced power output. This degradation is attributed to larger ohmic losses from higher operating currents, which in turn lower the FF and overall module efficiency.

### 3.3. Simulation of PV systems endowed with SHJ solar cells

In this section we show that our modelling framework allows quantifying the benefit in terms of energy yield of transitioning the production of SHJ cells from the baseline version to the optimized one. The simulations incorporate two types of M2 modules: one using half-cut baseline SHJ solar cells and the other using triple-cut optimized SHJ solar cells. Two environmental scenarios are considered: a free horizon and an urban skyline profile in Delft, the Netherlands, and Catania, Italy.

Fig. 16 illustrates the horizon profiles used in these calculations, rep

resenting the point of view of the PV module in terms of altitude angles across different azimuths. In the free horizon scenario, we calculate energy yield improvements of 5.48 % and 3.60 % from M2 modules endowed with optimized SHJ

**Fig. 17.** Simulated annual energy yield improvement (ΔEY) at the DC level for various PV module archetypes, relative to the M12 monofacial reference module.

Results are shown for two European locations: Delft (northern Europe, solid bars) and Catania (southern Europe, patterned bars). The analysis includes M2 modules

with monofacial, bifacial, and tandem (2J) configurations featuring different interface morphologies (F/F in blue, F/T in red, T/T in yellow, T/T Rin green), as well as

G12-type modules with T/T tandem cells. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

cells for Delft and Catania, respectively, relative to the baseline configuration in the same locations. In the urban skyline scenario, which includes realistic partial shading conditions and bypass diode activation, the improvement reaches 5.45 % in Delft and 3.68 % in Catania. These results highlight the capability of our simulation platform to evaluate PVsystem performance across varying environmental conditions and geographical locations, supporting data-driven PVmodules design for industrial and marketing purposes.

### 3.4. Simulation of PV systems endowed with 2J solar cells

This section presents the simulation results of PV systems endowed with our five PV module archetypes in Delft, the Netherlands, and Catania, Italy. Fig. 17 shows the relative energy yield difference (ΔEY) at the DC side for various module types, referenced against the M2 module archetype using the best-performing monofacialized SHJ solar cell. Note that the bar styles in Fig. 17 distinguish between Delft (solid fill) and Catania (patterned fill). Such calculations (i) use the AM1.5 spectrum as a reference with the incident irradiance scaled to emulate different irradiance conditions (see Equation (2)) and (ii) are performed on an hourly basis over a full year. Overall, the energy yield is higher in Catania than in Delft across all PV systems configurations, driven by the greater solar irradiance in the South of Italy. Notably, although the bifacial 1J M2 module has a lower power output than the monofacial 1J M2 module (see Fig. 15), it ach ieves higher energy yield due to the increased total irradiance captured as well from rear side. Comparing the performance of PV systems based on monofacial 1J and 2J modules, we observe a significant improvement of at least 15 % in energy yield across all simulated archetypes. The energy yield advantage of 2J modules over 1J modules is basically due to the higher conversion efficiency of the employed 2J solar cells but also marginally due to the lower operating current levels, which reduce the interconnection losses at the module level. Interestingly, the energy yield gain in the case of 2J M2 modules based on F/F, F/T and T/T R morphologies is only 2–4 % higher than that ascribed to the PV systems based on the bifacial 1J M2 module. This effect is attributed to the fact that the cumulated irradiance captured by bifacial SHJ modules effectively compensates for the enhanced light absorption achieved in 2J tandem modules that are not endowed with the better optically performing T/T morphology. In fact, PV systems with modules based on T/T morphology consistently outperform all other tandem morphologies, with the G12-0 T/T module scoring energy yield improvements of 22.1 % and 22.6 % in Delft and Catania, respectively, relative to the monofacial 1J M12 module reference. It is worth mentioning that transitioning from M2 triple-cut wafers to G12 triple-cut wafers (G12-0 archetype) or G12 half-cut wafers (G12-1 archetype) provides marginal benefit in terms of energy yield. At the same time, although the energy yield differences are minimal, PV sys tems based on G12-0 and G12-1 modules achieve slightly better energy yield than those using full G12 wafers (G12-2 and G12-3 archetypes), whose larger operating current levels due to larger solar cells area re sults in higher interconnection losses than their triple-cut and half-cut counterparts.

### 3.5. Effects of irradiance spectra clustering and temperature

In the initial phase of our analysis, we adopt a simplified approach by scaling the AM1.5 reference spectrum to emulate variations in irradi ance caused by time of day, weather conditions, and geographic loca tion. While this method offers a practical starting point for assessing irradiance-dependent performance, it fails to capture the spectral complexity inherent to real-world scenarios. Recognizing this limitation, we have introduced the methodology of clustering of spectral irradi ances in Section 2.5 that accounts for both spectral distribution and total incident power, enabling a more accurate and robust representation of the operating environment of tandem solar cells. Such a methodology is

**Table 9**

Temperature coefficients of Jsc, Voc, and output power (POUT) of F/F 2T tandem

solar cell and module as

simulated under standard AM1.5 spectrum shape, an

irradiance of 1000 W/m and in the temperature range from 10 C to 90 C.◦ ◦

AM1.5 kJsc[%/◦C] kVoc[%/◦C] kPout[%/◦C] Cell 0.002 0.199 0.218 Module 0.003 0.211 0.229

particularly relevant given that real-world conditions involve simulta neous variations in irradiance and temperature, unlike STC. Therefore, to realistically simulate the behavior of 2T tandem solar cells and modules, the external electrical parameters must be calculated as functions of both irradiance and temperature. The analysis in this section focuses on the calibrated F/F 2T tandem solar cells and on a PV module archetype similar to G12-2 but endowed with 60 full-sized G12 wafers instead of 40. Following up on the sanity check reported in Section 3.1.2, the cutoff wavelength used to classify spectral irradiances is again set to 740 nm. The primary objective is to evaluate the temperature coefficients at the cell, module, and PV system levels. Understanding these coefficients is essential, not only because they quantify the sensitivity of JSC, VOC, and the output power (Pout) to temperature variations but also because we expect a certain dependency on continuous fluctuation of spectral irradiance. To establish a baseline for assessing temperature-dependent behavior, we first calculate POUTof both the tandem cell and the module under STC and then we vary the temperature of the device to extract from the J-V curves the temperature coefficients. Table 9 summarizes the calculated temperature coefficients k Jsc, KVocand kPoutat both the cell and module levels, providing a reference point under well-defined thermal and spectral conditions. Across all cases, the module-level temperature coefficients are found to be consistent with values reported in the literature [58], and only slightly higher than those observed at the cell level. This increase is primarily attributed to additional thermal effects caused by the encap sulation and interconnection of the cells. While the kVocand KPoutof the 2J devices are in line with industry-standard SHJ modules, the addition of a perovskite top cell eventually turns the kJscfrom a positive value to a negative one, albeit almost negligible. From solar cell and module tested under STC, modelling the external parameters as jointly dependent on irradiance and temperature provides a more accurate representation of actual operating conditions. The simulated hourly electrical outputs of the 2J module under location- specific conditions, specifically, JSC(t) and Pout(t), were fitted using a bivariate linear model:

*Y* = *a* + *b*⋅*T* + *c*⋅*G* (9)

where T is the module operating temperature (◦C) and G is the irradi ance on the plane of the array (W/m 2 ). Both linear regressions achieved a high level of accuracy, with R 2 values exceeding 99 %, as shown in

Fig. 18. From the fitted equations, the typically negative coefficient *b*

was extracted. The temperature coefficients of both JSCand Poutwere then calculated by normalizing *b* with respect to the corresponding reference values at 25◦C and 1000 W/m 2 irradiance. Taking Pout(t) as an example, the units of the linear fit are:

- ◦[ / /2)] [ /2]
*Y* [*W*] =*a* [*W*] +*b* [*W / C*] ⋅*T* [ *C*] +*c W W m* ⋅*G W m* (10)

In contrast, VOC(G,T) was better fitted using a bivariate logarithmic model, reflecting the known logarithmic relationship between open- circuit voltage and irradiance:

*VOC*= *d* + *e*⋅*log*(*T*) + *f*⋅*log*(*G*) (11)

This fitting achieved an R value greater than 95 %, which is consistent with physical expectations. To determine the temperature coefficient kVoc, the fitted function was used to generate a set of VOC values at a constant irradiance of 1000 W/m, while varying the

**Fig. 18.** Irradiance, Temperature (G,T) fitting surfaces for computing (a) kJsc(G,T), (b) kVoc(G,T) and (c) kPout(G,T) coefficients of F/F 2J tandem module as

simulated in Delft (NL) under realistic operative conditions and in free horizon.

**Table 10**

Temperature coefficients and annual energy yield at the DC side (EY) of the F/

F 2J tandem module simulated in Delft (NL) and Catania (IT) for both free and

DC

urban horizon.

**Delft (NL) kJsc[%/ C]**◦**kVoc[%/ C]**◦**kPout[%/ C]**◦**EYDC[kWh/** **y]** *Free Horizon* 0.024 0.204 0.054 754.05 *Urban Horizon* 0.033 0.206 0.054 649.51 **Catania (IT) kJsc[%/ C]**◦**kVoc[%/ C]**◦**kPout[%/ C]**◦**EYDC[kWh/** **y]** *Free Horizon* 0.058 0.141 0.132 1288.02 *Urban Horizon* 0.067 0.149 0.135 1155.05

temperature from 10◦C to 90◦C in increments of 10◦C. Note that depending on the intended application, the 2D temperature coefficients can be computed using different reference irradiance levels: for 2 example, 800 W/m to reflect nominal operating cell temperature (NOCT) conditions. Based on the fittings, we demonstrate that the temperature co efficients of 2J modules under realistic conditions exhibit bidimensional variability, k(.) (G,T). These can be directly retrieved from our PVMD toolbox. Note, the dependency on irradiance has a deeper meaning than just the value in W/m 2 per se, since our simulations consider variable spectral irradiance. Therefore, assuming the spectra clustering method, we can estimate more realistic energy yield predictions. Table 10 sum marizes the calculated temperature coefficients from Equations (10) and

(11) and the EYDCof the 2J tandem module simulated in Delft and Catania for free and urban horizon (see Fig. 17). Regarding the EYDC values, those obtained under free horizon conditions are, as expected, higher than those under urban horizon conditions Fig. 19 illustrates. Furthermore, the consistently higher EYDCvalues observed in Catania reflect the higher average solar irradiance compared to Delft. Thus far we have employed two modelling approaches regarding the input spectral irradiance: (i) a simplified method using the AM1.5 spectrum scaled to different irradiance levels, and (ii) a spectral clus tering approach that accounts for both incident power and spectral distribution. A direct comparison between these two approaches is presented in Fig. 19, reporting the percentage difference in annual en ergy yield (ΔEY) for both Delft and Catania under free and urban hori zon scenarios and using the AM1.5-based method as reference. Overall, the differences in energy yield are lower than 0.9 %, with larger de viations observed for Delft. This may be attributed to differences in solar incident angles. In Catania, a greater number of daylight hours match with solar elevation angles close to that of the AM1.5 reference (~42 ),◦ resulting in better spectral alignment with the standard spectrum.

Fig. 20 illustrates the temperature coefficients at the cell, module,

and system levels for the case of Delft. At the cell and module levels, the coefficients were determined under indoor STC. The PV module exhibits temperature coefficients that slightly exceed those at the cell level, primarily due to additional thermal resistances and losses introduced by encapsulation and interconnection. At the system level, kJscis higher, reflecting the influence of irradiance variability in the fitting process, which directly affects JSC. In contrast, kVocremains largely consistent

both free and urban horizon conditions.

**Fig. 19.** Percentage difference in annual energy yield (ΔEY) calculated using two spectral approaches: (i) the standard AM1.5 spectrum scaled to different irradiance

levels (reference), and (ii) a spectral clustering method incorporating both spectral distribution and incident power. Results are shown for Delft and Catania under

**Fig. 20.** Tandem devices temperature coefficients, from cell & module to system level for the location of Delft under free-horizon and urban-like horizon scenarios.

Note the negative sign on the y-axis title.

**Fig. 21.** Tandem devices temperature coefficients, from cell & module to system level for the location of Catania under free-horizon and urban-like horizon sce

narios. Note the negative sign on the y-axis title.

across all levels. However, kPoutis significantly reduced at the system level, due to the lower average operating temperatures and reduced thermal fluctuations under the specific climatic conditions in Delft. Like the previous illustration, Fig. 21 presents the corresponding temperature coefficients at cell, module, and system levels for the case of Catania. In comparison to Delft, both kJscand kPoutvalues at the system level are higher, while kVocis lower. These trends are attributed to the higher temperatures and greater irradiance variability characteristic of the Catania climate, which amplify the thermal and spectral effects influencing device performance. Note, the results presented in Figs. 20 and 21 refer to values reported in Tables 9 and 10. The proposed modelling framework enables the extraction of tem perature coefficients for custom multi-junction photovoltaic modules under (i) a broad range of irradiance conditions, (ii) geographically diverse locations, and (iii) varying horizon profiles. This capability of fers valuable insight for optimizing 2T tandem module designs, allowing for their adaptation to specific market segments and deployment envi ronments across different climatic and geographic contexts.

### 3.6. Location-dependent power matrix

The IEC 61853-1 standard [62] defines how to measure the perfor mance of a PV module under different irradiance and temperature conditions beyond STC. Based on the AM1.5 spectral irradiance and a scaling process in line with Equation (2), a so-called *power matrix* can be compiled. Such a power matrix shows the expected power output values of a PV module operating in realistic conditions. Using our PVMD toolbox, we could compute the power matrix of the modelled F/F 2J

**Table 11**

Power

61853-1

matrix

standard.

(W) of the modelled F/F 2J module compiled according to the IEC

Temperature [ C]◦ Irradiance [W/m²] 15 25 50 75 **100** 66.37 64.83 NA NA **200** 136.60 133.53 NA NA **400** 269.49 263.88 250.48 NA **600** 397.11 389.37 369.86 350.86 **800** 534.22 524.34 498.32 470.77 **1000** 681.46 669.53 636.64 599.00 **1100** NA 737.60 701.60 658.43

module discussed in the previous section according to the IEC 61853-1 standard (see Table 11). Also using the PVMD toolbox, we can plot the yearly operating points (G,T) of such a module for both Delft and Cat ania (see Fig. 22 for the case of free horizon). Compared with the (G,T) pairs of the IEC 61853-1 standard, it appears that the power matrix from the standard does not represent the eventual outdoor behavior of the PV module in both locations. To address this issue, we propose to issue location-dependent power matrixes that can be computed via numerical modelling as presented in this work. From an annual PV system simulation, considering the abovementioned (G,T) operating points, it is possible to carry out the distribution of annual energy production [%] at different temperatures and irradiances for a certain location. We did this calculation for both Delft and Catania, yielding Fig. 23 (a) and 23b, respectively. They show

**Fig. 22.** Irradiance, Temperature (G,T) operating points across the year of the modelled F/F 2J module in free horizon condition for the case of Delft (left) and

Catania (right). The yellow circles indicate the G,T pairs of the IEC 61853-1 standard. (For interpretation of the references to color in this figure legend, the reader is

referred to the Web version of this article.)

**Fig. 23.** Percentage distribution of annual energy production [%] at different temperatures and irradiances for (a) Delft and (b) Catania.

that the (G,T) pair at which most of the power production occurs is

**Table 12**

different, (500, 25) for Delft and (900, 45) for Catania. Setting up a

Range of irradiance and temperature values for carrying out the power matrix

threshold of 1 % of the annual energy output and considering bins of

according to the IEC 61853-1 standard or location-dependent power matrix in

irradiance from the smallest to the largest, including those around the

Delft, the Netherlands, and Catania, Italy.

one causing the maximum power production, one could isolate a range Location Irradiance [W/m] Temperature [ C]◦ of (G,T) pairs that better represent the largest part of power production of a PV module at a given location. In Table 12 we report the suggested**IEC 61853**– 100, 200, 400, 600, 800, 1000, 1100 15, 25, 50, 75 **Delft** 100, 300, 400, 500, 600, 700, 1000 5, 15, 25, 35, 45 (G,T) pairs to compute location-dependent matrixes for Delft and Cat **Catania** 200, 400, 600, 800, 900, 1000 15, 25, 35, 45, 55 ania of the modelled F/F 2J module.

## 4. Conclusions

We have presented a holistic cell-to-system modelling framework. At the cell level, we have firstly validated our semiconductor equations numerical modelling with respect to a reference bifacial SHJ solar cell. Then, we optimized that solar cell towards a monofacial-like configu ration. Next, we validated our model with respect to a fabricated 2T tandem device. We evaluated different interface morphologies (F/F, F/ T, T/T and F/T R), with the T/T one exhibiting the best optical perfor mance. At the module level, we assessed five PV module archetypes (M2, G12-0, G12-1, G12-2 and G12-3), with the G12-0 one, featuring 2J solar cells with T/T morphology, showing the highest power output under STC. That is ~30 % higher than the one calculated for M2 module based on optimized monofacial-like SHJ solar cells. At the system level, we observed a similar trend in terms of energy yield. The PV system with module type G12-0 (2J T/T) shows more than 22 % higher energy yield for both locations (Delft, the Netherlands, and Catania, Italy) with respect to a PV system formed by the same abovementioned M2 archetype based on optimized monofacial-like SHJ solar cells. Our modelling approach allows us to consider also variable spectral irradi ance, which is crucial not only to determine current (mis-) matching in 2T tandem solar cells and modules. We also show that the temperature coefficients of future 2T tandem modules change from indoor STC to realistic conditions. In the latter case, the temperature coefficients need to be derived from both irradiance and temperature. Finally, for the same reason, we demonstrate that the power matrix based on the IEC 61853-1 standard does not seem to represent the expected performance of a PV module in realistic conditions, at least of 2T tandem modules as studied here. To address this issue, we propose a procedure to compute location-dependent power matrixes. In this way companies could set pairs of irradiance and temperature at the testing level to better gauge how their products will perform at specific locations.

## CRediT authorship contribution statement

**P. Procel:** Writing – original draft, Validation, Methodology, Inves
tigation, Conceptualization. **Y. Zhou:** Writing – review & editing, Visualization, Validation, Data curation. **M. Verkou:** Visualization, Methodology, Data curation. **M. Leonardi:** Writing – review & editing.

**D. Di Girolamo:** Writing – review & editing. **G. Giuliano:** Writing – review & editing. **O. Dupre:** ´ Writing – review & editing, Validation. **Y.** **Blom:** Writing – review & editing, Methodology. **M.R. Vogt:** Writing – review & editing. **R. Santbergen:** Writing – review & editing. **F.** **Rametta:** Writing – review & editing. **M. Foti:** Writing – review & editing, Conceptualization. **C. Gerardi:** Writing – review & editing. **M.** **Zeman:** Writing – review & editing, Supervision, Project administration, Methodology, Funding acquisition, Conceptualization. **O. Isabella:** Writing – review & editing, Supervision, Resources, Project adminis tration, Methodology, Funding acquisition, Formal analysis, Data cura tion, Conceptualization.
## Declaration of interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence

the work reported in this paper.

## Data availability

Data will be made available on request.

## References

[1] W. Shockley, H.J. Queisser, Detailed balance limit of efficiency of p-n junction solar cells, J. Appl. Phys. 32 (3) (Mar. 1961) 510–519, [https://doi.org/10.1063/](https://doi.org/10.1063/)

1.1736034.
[2] K.A. Horowitz, T.W. Remo, B. Smith, A.J. Ptak, A Techno-Economic Analysis and Cost Reduction Roadmap for III-V Solar Cells, Nov. 2018, [https://doi.org/10.2172/](https://doi.org/10.2172/)

[3] 1484349

J.J. Cordell,. Golden,
M. Woodhouse, CO (United
E.L. States). Warren, Technoeconomic analysis of perovskite/
silicon tandem solar modules, Joule 9 (2) (Feb. 2025) 101781, [https://doi.org/](https://doi.org/)

10.1016/j.joule.2024.10.013.
[4] Press Perovskite Release tandem LONGi, solar

34.85%! cell efficiency LONGi breaks again. world [https://www.longi.com/en/news/](https://www.longi.com/en/news/)
record for crystalline silicon-

silicon-perovskite-tandem-solar-cells-new-world-efficiency/. [5] F. Institute for Solar Energy Systems ISE, “Fraunhofer ISE-Annual Report 2024/

[6]

25. Press ”. Release, Tandem Perovskite-Silicon: 29.8% new efficiency record for a 9 cm
2 tandem cell. [https://www.ines-solaire.org/en/news/tandem-perovskite-silicon-2](https://www.ines-solaire.org/en/news/tandem-perovskite-silicon-2)

9.8-new-efficiency-record-for-a-9-cm-tandem-cell/.
[7] Press com/news/oxford-pv-sets-new-solar-cell-world-record Release, Oxford PV sets new solar cell world record.. [https://www.oxfordpv](https://www.oxfordpv).

[8] Press Release QCells, Qcells achieves world record efficiency for commercially scalable perovskite-silicon tandem solar cell. [https://us.qcells.com/blog/qcells-](https://us.qcells.com/blog/qcells-) tandem-cell-world-record-efficiency/. [9] Press Release JinkoSolar, “JinkoSolar’s Perovskite Tandem Solar Cell Based on N- type TOPCon Sets New Record with Conversion Efficiency of 33.84%,”. [https://ir](https://ir). jinkosolar.com/news-releases/news-release-details/jinkosolars-perovskite-tande m-solar-cell-based-n-type-topcon-0. [10] Press module, Release ushering TrinaSolar, in a new Trinasolar era. [https://static.trinasolar.com/us/resources/n](https://static.trinasolar.com/us/resources/n) develops world’s first 800W+ Tandem

ewsroom/Worlds-First-800W-Tandem-Module. [11] H. Ziar, P. Manganiello, O. Isabella, M. Zeman, Photovoltatronics: intelligent PV- based (2021) devices 106–126, for [https://doi.org/10.1039/D0EE02491K](https://doi.org/10.1039/D0EE02491K) energy and information applications, Energy. Environ. Sci. 14 (1)

[12] Y. Blom, M.R. Vogt, C.M. Ruiz Tobon, R. Santbergen, M. Zeman, O. Isabella, Energy loss analysis of two-terminal Tandem PV systems under realistic operating conditions—revealing the importance of fill factor gains, Sol. RRL 7 (8) (Apr.

2023), [https://doi.org/10.1002/solr.202200579](https://doi.org/10.1002/solr.202200579).
[13] M.R. Vogt, et al., Introducing a comprehensive physics-based modelling framework for tandem and other PV systems, Sol. Energy Mater. Sol. Cell. 247 (Oct. 2022)

[14] 111944,

Y. Blom, [https://doi.org/10.1016/j.solmat.2022.111944](https://doi.org/10.1016/j.solmat.2022.111944) M.R. Vogt, O. Isabella, R. Santbergen, Optimization
. of the perovskite cell in a bifacial two-terminal perovskite/silicon tandem module, Sol. Energy Mater. Sol. Cell. 282 (Apr. 2025) 113431, [https://doi.org/10.1016/j](https://doi.org/10.1016/j). solmat.2025.113431. [15] Y. Blom, et al., Exploring the potential of Perovskite/Perovskite/Silicon triple- junction Pv modules in two- and four-terminal configuration, Sol. RRL 9 (5) (Mar.

2025), [https://doi.org/10.1002/solr.202400613](https://doi.org/10.1002/solr.202400613).
[16] H. Ziar, et al., Innovative floating bifacial photovoltaic solutions for inland water areas,

10.1002/pip.3367 Prog. Photovoltaics
. Res. Appl. 29 (7) (Jul. 2021) 725–743, [https://doi.org/](https://doi.org/)

[17] Z. Ul-Abdin, M. Zeman, O. Isabella, R. Santbergen, Investigating the annual performance of air-based collectors and novel bi-fluid based PV-thermal system, Sol. solener.2024.112687 Energy 276 (Jul.. 2024) 112687, [https://doi.org/10.1016/j](https://doi.org/10.1016/j).

[18] M. De Bastiani, et al., Efficient bifacial monolithic perovskite/silicon tandem solar cells via bandgap engineering, Nat. Energy 6 (2) (Jan. 2021) 167–175, [https://doi](https://doi). org/10.1038/s41560-020-00756-8. [19] F. Gota, R. Schmager, A. Farag, U.W. Paetzold, Energy yield modelling of textured perovskite/silicon tandem photovoltaics with thick perovskite top cells, Opt. Express 30 (9) (Apr. 2022) 14172, [https://doi.org/10.1364/OE.447069](https://doi.org/10.1364/OE.447069). [20] W.E. comparing McMahon, the energy

J.F. Geisz, production
J. Buencuerpo, of photovoltaic
E.L. Warren, modules A framework using 2-, 3-,
for and 4-ter minal tandem cells, Sustain. Energy Fuels 7 (2) (2023) 461–470, [https://doi.org/](https://doi.org/)

10.1039/D2SE01167K.
[21] M.T. Horantner, ¨ H.J. Snaith, Predicting and optimising the energy yield of perovskite-on-silicon tandem solar cells under real world conditions, Energy Environ. Sci. 10 (9) (2017) 1983–1993, [https://doi.org/10.1039/C7EE01232B](https://doi.org/10.1039/C7EE01232B). [22] K. Jager, ¨ P. Tillmann, E.A. Katz, C. Becker, Perovskite/Silicon tandem solar cells: effect of luminescent coupling and bifaciality, Sol. RRL 5 (3) (Mar. 2021), https://

[23] doi.org/10.1002/solr.202000628

S. ˇ Tomˇsiˇc, M. Joˇst, K. Brecl, M. Topi
. ˇc, B. Lipovˇsek, Energy yield modeling for optimization and analysis of perovskite-silicon Tandem solar cells under realistic outdoor conditions, Adv. Theory Simul. 6 (4) (Apr. 2023), [https://doi.org/](https://doi.org/)

10.1002/adts.202200931.
[24] R. Santbergen, T. Meguro, T. Suezaki, G. Koizumi, K. Yamamoto, M. Zeman, GenPro4 optical model for solar cell simulation and its application to multijunction

solar cells, IEEE J. Photovoltaics 7 (3) (2017) 919–926, [https://doi.org/10.1109/](https://doi.org/10.1109/) JPHOTOV.2017.2669640. [25] R. Santbergen, V.A. Muthukumar, R.M.E. Valckenborg, W.J.A. van de Wall, A.H.

M. Smets, M. Zeman, Calculation of irradiance distribution on PV modules by combining sky and sensitivity maps, Sol. Energy 150 (Jul. 2017) 49–54, https:// doi.org/10.1016/j.solener.2017.04.036.
[26] A. Calcabrini, H. Ziar, O. Isabella, M. Zeman, A simplified skyline-based method for estimating the annual solar energy potential in urban environments, Nat. Energy 4

(3) (Feb. 2019) 206–215, [https://doi.org/10.1038/s41560-018-0318-6](https://doi.org/10.1038/s41560-018-0318-6).
[27] R. Perez, R. Seals, J. Michalsky, All-weather model for sky luminance distribution—Preliminary configuration and validation, Sol. Energy 50 (3) (Mar.

1993) 235–245, [https://doi.org/10.1016/0038-092X(93](https://doi.org/10.1016/0038-092X(93))90017-I.
[28] A.G. Meteotest, Meteonorm, Bern, Jan. 05, 2025. [29] C.A. Gueymard, V. Lara-Fanego, M. Sengupta, Y. Xie, Surface albedo and reflectance: review of definitions, angular and spectral effects, and intercomparison of major data sources in support of advanced solar irradiance modeling over the Americas, Sol. Energy 182 (Apr. 2019) 194–212, [https://doi](https://doi). org/10.1016/j.solener.2019.02.040. [30] P. Ricchiazzi, S. Yang, C. Gautier, D. Sowle, SBDART: a research and teaching software tool for plane-parallel radiative transfer in the earth’s atmosphere, Bull. Am. Meteorol. Soc. 79 (10) (Oct. 1998) 2101–2114, [https://doi.org/10.1175/](https://doi.org/10.1175/) 1520-0477(1998)079*<*2101:SARATS*>*2.0.CO;2. [31] D.L. King, E.E. Boyson, J.A. Kratochvil, Photovoltaic Array Performance Model, Sandia National Laboratories, 2004. Albuquerque: SAND2004-3535. [32] D. Faiman, Assessing the outdoor operating temperature of photovoltaic modules, Prog. Photovoltaics Res. Appl. 16 (4) (Jun. 2008) 307–315, [https://doi.org/](https://doi.org/)

10.1002/pip.813.
[33] M.K. Fuentes, A simplified thermal model for flat-plate photovoltaic arrays [Online]. Available: [https://www.osti.gov/biblio/6802914](https://www.osti.gov/biblio/6802914), Apr. 1987. [34] Synopsys, TCAD Sentaurus: Sentaurus Device User Guide, 2023. [35] M. Zeman, J. van den Heuvel, B.E. Pieters, M. Kroon, J. Willemen, Advanced Semiconductor Analysis, TU Delft, 2003. [36] A. Ingenito, O. Isabella, S. Solntsev, M. Zeman, Accurate opto-electrical modeling of multi-crystalline silicon wafer-based solar cells, Sol. Energy Mater. Sol. Cell. 123 (Apr. 2014) 17–29, [https://doi.org/10.1016/j.solmat.2013.12.019](https://doi.org/10.1016/j.solmat.2013.12.019). [37] M. Zeman, O. Isabella, S. Solntsev, K. Jager, ¨ Modelling of thin-film silicon solar cells, Sol. Energy Mater. Sol. Cell. 119 (Dec. 2013) 94–111, [https://doi.org/](https://doi.org/)

10.1016/j.solmat.2013.05.037.
[38] P. Procel-Moya, Y. Zhao, O. Isabella, “Unlocking the potential of carrier-selective contacts: key insights for designing c-Si solar cells with efficiency beyond 28 %,”, Sol. Energy Mater. Sol. Cell. 285 (Jun. 2025) 113504 [https://doi.org/10.1016/j](https://doi.org/10.1016/j). solmat.2025.113504. [39] A. Al-Ashouri, et al., Monolithic perovskite/silicon tandem solar cell with *>*29% efficiency by enhanced hole extraction, Science (1979) 370 (6522) (2020) 1300–1309, [https://doi.org/10.1126/science.abd4016](https://doi.org/10.1126/science.abd4016). [40] X.Y. Chin, et al., Interface passivation for 31.25%-efficient perovskite/silicon tandem solar cells, Science (1979) 381 (6653) (Jul. 2023) 59–63, [https://doi.org/](https://doi.org/)

10.1126/science.adg0091.
[41] E. Aydin, et al., Enhanced optoelectronic coupling for perovskite/silicon tandem solar cells, Nature 623 (7988) (Nov. 2023) 732–738, [https://doi.org/10.1038/](https://doi.org/10.1038/) s41586-023-06667-4. [42] A. Schenk, Finite-temperature full random-phase approximation model of band gap narrowing for silicon device simulation, J. Appl. Phys. 84 (7) (Oct. 1998) 3684–3695, [https://doi.org/10.1063/1.368545](https://doi.org/10.1063/1.368545). [43] P.P. Altermatt, A. Schenk, F. Geelhaar, G. Heiser, Reassessment of the intrinsic carrier density in crystalline silicon in view of band-gap narrowing, J. Appl. Phys. 93 (3) (Feb. 2003) 1598–1604, [https://doi.org/10.1063/1.1529297](https://doi.org/10.1063/1.1529297). [44] D.B.M. Klaassen, A unified mobility model for device simulation—I. Model equations and concentration dependence, Solid State Electron. 35 (7) (Jul. 1992) 953–959, [https://doi.org/10.1016/0038-1101(92](https://doi.org/10.1016/0038-1101(92))90325-7. [45] H. Lin, et al., Silicon heterojunction solar cells with up to 26.81% efficiency achieved by electrically optimized nanocrystalline-silicon hole contact layers, Nat. Energy (May 2023) 14–16, [https://doi.org/10.1038/s41560-023-01255-2](https://doi.org/10.1038/s41560-023-01255-2).

[46] P. Procel, et al., The role of heterointerfaces and subgap energy states on transport mechanisms in silicon heterojunction solar cells, Prog. Photovoltaics Res. Appl. 28

(9) (Sep. 2020) 935–945, [https://doi.org/10.1002/pip.3300](https://doi.org/10.1002/pip.3300).
[47] J. Madan, Shivani, R. Pandey, R. Sharma, Device simulation of 17.3% efficient lead-free all-perovskite tandem solar cell, Sol. Energy 197 (Feb. 2020) 212–221, [https://doi.org/10.1016/j.solener.2020.01.006](https://doi.org/10.1016/j.solener.2020.01.006). [48] S. Wang, T. Sakurai, R. Kuroda, K. Akimoto, Energy band bending induced charge accumulation at fullerene/bathocuproine heterojunction interface, Appl. Phys. Lett. 100 (24) (Jun. 2012), [https://doi.org/10.1063/1.4728996](https://doi.org/10.1063/1.4728996). [49] Z. Yu, et al., Simplified interconnection structure based on C60/SnO2-x for all- perovskite tandem solar cells, Nat. Energy 5 (9) (Sep. 2020) 657–665, [https://doi](https://doi). org/10.1038/s41560-020-0657-y. [50] Z.T. Liu, C.Y. Kwong, C.H. Cheung, A.B. Djuriˇsi´c, Y. Chan, P.C. Chui, The characterization of the optical functions of BCP and CBP thin films by spectroscopic ellipsometry, Synth. Met. 150 (2) (Apr. 2005) 159–163, [https://doi.org/10.1016/j](https://doi.org/10.1016/j). synthmet.2005.02.001. [51] C.T. Trinh, et al., Electrical and optical simulation of perovskite/silicon tandem solar cells using Tcad-Sentaurus, in: Conference Record of the IEEE Photovoltaic Specialists Conference, Institute of Electrical and Electronics Engineers Inc., Jun. 2021, pp. 2324–2327, [https://doi.org/10.1109/PVSC43889.2021.9519104](https://doi.org/10.1109/PVSC43889.2021.9519104). [52] A. Al-Ashouri, et al., Conformal monolayer contacts with lossless interfaces for perovskite single junction and monolithic tandem solar cells, Energy Environ. Sci. 12 (11) (Nov. 2019) 3356–3369, [https://doi.org/10.1039/c9ee02268f](https://doi.org/10.1039/c9ee02268f). [53] I. Levine, et al., Charge transfer rates and electron trapping at buried interfaces of perovskite solar cells, Joule 5 (11) (Nov. 2021) 2915–2933, [https://doi.org/](https://doi.org/)

10.1016/j.joule.2021.07.016.
[54] M.R. Vogt, Development of physical models for the simulation of optical properties of solar cell modules, Gottfried Wilhelm Leibniz Universit¨at Hannover (2015). Hannover. [55] D. Berrian, J. Libal, M. Klenk, H. Nussbaumer, R. Kopecek, Performance of bifacial PV arrays with fixed tilt and horizontal single-axis tracking: comparison of simulated and measured data, IEEE J. Photovoltaics 9 (6) (Nov. 2019) 1583–1589, [https://doi.org/10.1109/JPHOTOV.2019.2924394](https://doi.org/10.1109/JPHOTOV.2019.2924394). [56] Y. Blom, et al., Exploring the potential of Perovskite/Perovskite/Silicon triple- junction Pv modules in two- and four-terminal configuration, Sol. RRL 9 (5) (Mar.

2025), [https://doi.org/10.1002/solr.202400613](https://doi.org/10.1002/solr.202400613).
[57] Y. Blom, M.R. Vogt, O. Isabella, R. Santbergen, Optimization of the perovskite cell in a bifacial two-terminal perovskite/silicon tandem module, Sol. Energy Mater. Sol. Cell. 282 (Apr. 2025) 113431, [https://doi.org/10.1016/j](https://doi.org/10.1016/j). solmat.2025.113431. [58] T. Sam, S. Henry, Examining the influence of temperature coefficients of perovskite tandem photovoltaics under real-world conditions, in: Q. Shen, J. Ryan (Eds.), Proceedings of Asia-Pacific International Conference on Perovskite, Organic Photovoltaics and Optoelectronics (IPEROP24), 2024. Tokyo. [59] Press Release, Tandem Perovskite-Silicon: Enel green power and CEA improve their efficiency record to 27.1% on 9 cm2. [https://www.ines-solaire.org/en/news/enel](https://www.ines-solaire.org/en/news/enel) -green-power-and-cea-improve-their-efficiency-record-to-27.1-on-9-cm/. [60] R. van Heerden, P. Procel, L. Mazzarella, R. Santbergen, O. Isabella, Slow shallow energy states as the origin of hysteresis in perovskite solar cells, Frontiers in Photonics 3 (4) (May 2022) 401–435, [https://doi.org/10.3389/](https://doi.org/10.3389/) fphot.2022.889837. [61] P. Procel, et al., Opto-electrical modelling and roadmap for 2T monolithic Perovskite/CIGS tandem solar cells, Sol. Energy Mater. Sol. Cell. 274 (May) (2024), [https://doi.org/10.1016/j.solmat.2024.112975](https://doi.org/10.1016/j.solmat.2024.112975). [62] Photovoltaic (PV) Module Performance Testing and Energy Rating. Part 1, Irradiance and Temperature Performance Measurements and Power Rating = Essais De Performance Et Caract´eristiques Assign´ees D’Energie ´ Des Modules Photovoltaïques (PV). Partie 1, Mesures De Performance En Fonction de l’´eclairement et de la Temp´erature, et Caract´eristiques de Puissance, IEC, Geneva, Switzerland, 2011.
