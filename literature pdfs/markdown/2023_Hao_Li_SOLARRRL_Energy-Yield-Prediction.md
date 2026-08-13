### <u>RESEARCH ARTICLE</u>

www.solar-rrl.com

# Energy Yield Prediction of Bifacial Perovskite/Silicon Tandem Photovoltaic Modules

Hongwei Hao, Shan-Ting Zhang,* Kai Wang, Peizhi Yang, Jilei Wang, Liyou Yang, Linfeng Lu, and Dongdong Li*

passivating contact has reached 26.81%, [3]

##### Bifacial perovskite (PVK)/crystalline silicon (c-Si) tandem photovoltaic (PV)

which is practically approaching the limit modules provide an effective strategy to further improve the efficiency and energy of 29.4% (with the Auger recombination [4] yield (EY) of c-Si PV modules. In this work, the energy outputs of bifacial tandem taken into account). This reality has stim- ulated an explosive research interest in PV modules under outdoor conditions are analyzed by combining optical both academia and industry to develop tan- modeling, one-diode equivalent circuit model, module tilt angle, and meteoro-dem PV in which c-Si bottom cell is stacked logical data, and a detailed comparative study with bifacial silicon heterojunction with wide-bandgap top cells to better utilize (SHJ) PV modules is also performed. The bifacial PVK/c-Si tandem modules the full solar spectrum and thus to further exhibit higher EY in locations with strong direct normal irradiance regardless of boost PCE. the ground type with any albedo, while bifacial SHJ modules exhibit similar or Given the tunable bandgap, high band- edge absorption, and cost-effective fabrica- even higher EY than tandem modules in locations with strong diffuse horizontal tion process, [5,6] perovskites (PVK) solar irradiance (DHI) such as Chengdu. Considering factors such as EY and levelized cells are considered as the most promising cost of electricity, Eg_PVKin the range of 1.58–1.62 eV is suitable for most top cell candidates for silicon-based tandem application scenarios, while the deployment of bifacial SHJ PV modules is solar cells. Following the pioneering report

preferred in areas dominated by DHI, as represented by Chengdu. Herein, in 2015, PVK/c-Si tandem solar cells have [7]

experienced rapid progress and have important implications for policy making in determining the cost-effective type of[8] recently reached an efficiency of 33.2%, PV modules are provided to generate renewable electricity. which has far exceeded the theoretical limit of single-junction c-Si solar cells. Recently, remarkable progress has been made to improve the stability of PVK materials with

#### 1. Introduction

effective strategies proposed to ensure the long-term stable oper- ation of PVK-based solar cells. [9–14] Photovoltaic (PV) power generation is an important driving force It should be noted that the PCE of solar cell obtained in the in solving the global energy crisis and achieving global carbon laboratory measured under AM1.5G standard spectrum cannot neutrality. Crystalline silicon (c-Si) solar cell technology has been represent the energy yield (EY) in real-world conditions. developed over the years and has dominated more than 95% of Instead, for cells and modules operated under outdoor condi- the PV market. [1,2] The power conversion efficiency (PCE) of sili-tions, it is obliged to consider the direct normal irradiance con heterojunction (SHJ) cells deploying the concept of (DNI), diffuse horizontal irradiance (DHI), and rear-side albedo

H. Hao, L. Lu, D. Li K. Wang The Interdisciplinary Research Center Dalian National Laboratory for Clean Energy Shanghai Advanced Research Institute Dalian Institute of Chemical Physics Chinese Academy of Sciences Chinese Academy of Sciences Shanghai 201210, China Dalian, Liaoning 116023, China E-mail: lidd@sari.ac.cn
P. Yang
H. Hao, L. Lu, D. Li Key Laboratory of Advanced Technique & Preparation for Renewable School of Microelectronics Energy Materials University of Chinese Academy of Sciences Ministry of Education Beijing 100049, China Yunnan Normal University
Kunming 650500, China

S.-T. Zhang, D. Li Zhangjiang Laboratory J. Wang, L. Yang Pudong, Shanghai 201210, China Jinneng Clean Energy Technology LTD E-mail: zhangst@zjlab.ac.cn Jinzhong 030600, China The ORCID identification number(s) for the author(s) of this article D. Li can be found under [https://doi.org/10.1002/solr.202300218](https://doi.org/10.1002/solr.202300218). Dalian National Laboratory for Clean Energy
Dalian, Liaoning 116023, China DOI: 10.1002/solr.202300218

Sol. RRL 2023, 7, 2300218 2300218 (1 of 10) © 2023 Wiley-VCH GmbH

2367198x, 2023, 15, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/solr.202300218](https://onlinelibrary.wiley.com/doi/10.1002/solr.202300218) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

radiation to correctly estimate EYs, which together with the lev- elized cost of electricity (LCOE) are the key indicator of the out- door performance or cost advantage of different PV modules. Hörantner and Snaith developed a rigorous optical model and combined it with one-diode equivalent circuit model to obtain the PCE of planar monolithic PVK/c-Si tandem solar cells and esti- mate the EY for different environments and axis tracking designs. [15] They concluded that planar monolithic PVK/c-Si tan- dem solar cells could produce more EY than single-junction SHJ solar cells by 30%. This pioneering work attracted widespread attention, but did not take into account the optical losses of the modules, and the cells were modeled in a planar structure which is inconsistent with the textured c-Si commonly used in PV industry. Following work then introduced textured c-Si to cal- culate the EY of PVK/c-Si tandem solar cells and discovered that the textured c-Si surface could efficiently improve the EY of tan- dem PV modules. [16–19] After that, the climate-dependent EY of tandem modules on a global scale was investigated, which dem- onstrated that the monofacial tandem modules are more advan- tageous than SHJ modules in terms of EY. [20] Assuming comparable lifetime of PVK materials with that of c-Si cells, the LCOE of high-efficiency PVK/c-Si tandem modules is pre- dicted more advantageous than that of single-junction c-Si modules. [21]

In the previous work, the EY and related characteristics were mainly conducted for monofacial PV modules in which SHJ was typically used as the bottom cell. [15–17,20,22,23] However, SHJ solar cells naturally possess bifacial light-receiving feature that can effectively absorb diffuse light reflected by the ground (called albedo) and by the atmosphere and surroundings. This bifaciality will result in an increase in the EY of about 25–30%. [24–26]

According to the International Technology Roadmap for Photovoltaic, the market share of bifacial modules is expected to increase from 50% in 2022 to about 85% by 2032. [27]

Without doubt, bifacial tandem solar cells will become a compet- itive player in the PV market in the future. Therefore, it is of great significance to study the EY of bifacial PVK/c-Si tandem modules for large-scale deployment. Some of the recent works have pre- dicted the EY of bifacial tandem solar cells, [19,28–30] in which the focus is mainly on how the different albedo affects the optimal bandgap and thickness of PVK layers. Little attention has been paid to performing EY and LCOE analysis for bifacial tandem PV modules installed in more typical regions and their compari- son with bifacial SHJ PV modules are barely studied. In this work, we analyzed the EY characteristics of bifacial tan- dem modules in different regions (with typical solar irradiation) and under different albedo conditions with respect to that of bifa- cial SHJ modules. In most regions, the EY of bifacial tandem modules outperforms the bifacial SHJ modules. And, the optimal Eg_PVKis suggested to be 1.62 eV or even lower to pro- duce the highest EY for bifacial PVK/c-Si tandem modules with the presence of albedo. Compared to wide-bandgap PVK (Eg_PVK= 1.67 eV or larger), narrow-bandgap PVK materials are featured with lower voltage loss, higher stability, and maturer fabrication process. [31–34] In particular, it is worth noting that in Chengdu area, which is dominant with DHI, bifacial tandem modules exhibit similar (albedo ≤ 35%) or lower (albedo > 35%) EY than that of bifacial SHJ modules. Given the considerations of

Sol. RRL 2023, 7, 2300218

EY and LCOE, tandem modules are suitable for most areas except where DHI dominates.

#### 2. Experimental Section

2.1. Optical Simulation The complete structures of the three types of solar cells, that is, bifacial SHJ (as reference), bifacial, and monofacial PVK/c-Si tan- dem, are shown in Figure S1, Supporting Information. The monofacial PVK/c-Si tandem was constructed by placing a 500 nm thick Ag on the rear side of the c-Si bottom cell to block the incident light from the rear side, which at the same time helped to recycle the incident near-infrared (NIR) photons from the front side. To evaluate the power generation and annual EY under outdoor conditions, the optical characteristics of the corresponding modules as illustrated in Figure 1a are first simulated. The optical simulations were carried out using SunSolve, [35]
which combined ray tracing with a coherent trans- fer matrix-based thin-film simulator and reproduced the optical absorption of each layer based on the optical parameters of each layer. For the optical parameters of PVK, we referred to the previously reported complex refractive indices at 1.557 eV (MAPbI₃), 1.62 eV (Cs0.17FA0.83Pb(Br0.17I0.83)3), and 1.67 eV (Cs0.25FA0.75Pb(Br0.2I0.8)3) by Manzoor et al. [36] and simulated the other bandgaps (i.e., 1.58, 1.60, and 1.70 eV) by assuming a perfect horizontal shift along the energy axis (Figure S2, Supporting Information), which was confirmed in the work of Manzoor et al. [36] The detailed method is presented in the Note S1, Supporting Information. The optical parameters of the remaining layers were obtained through literatures. [36–47]

2.2. Electrical Model Assuming that the absorption of one incident photon generated one electron–hole pair, and all electron–hole pairs contributed to the photocurrent,
[48–50] the short-circuit current densities ( Jscs) of the PVK ( Jsc_PVK) and c-Si ( Jsc_c-Si) subcells could be obtained by J sc¼ e ∫ <u>λ</u> AbsðλÞIAM1:5GðλÞdðλÞ, where e is the elemental hc charge, h is the Planck’s constant, c is the light speed in vacuum, Abs(λ) is the absorption of each material, and IAM1.5(λ) is the AM1.5G solar spectral irradiance (ASTM G-173-03). [51] Note that the values of wavelengths-dependent Abs(λ) of PVK and c-Si were equivalent to the external quantum efficiencies (EQEs) of PVK and c-Si subcells based on the aforementioned assumption. The one-diode equivalent circuit model was employed to model the current density–voltage ( J–V ) characteristics of PVK/c-Si tandem solar cells/modules with the help of LTspice software. [52] To obtain the specific J–V curves, the photogener- ated current ( JG), dark saturation current ( J₀), ideal factor (n), series resistance (Rs), and shunt resistance (Rsh) were used as input parameters, where the JGwas obtained from the Jscof the cell or module under AM1.5G illumination. The diode parameters of c-Si bottom cell ( J₀, n, Rs, Rsh) were extracted from the J–V curves in the reference. [53] In the case of PVK top cell, the J₀ for each bandgap was calculated based on the blackbody radia- tion at 300 K and the corresponding EQE. [54] The calculation details are described in the Note S2, Supporting Information.

© 2023 Wiley-VCH GmbH 2300218 (2 of 10)

Figure 1. The schematic diagrams of a) the bifacial silicon heterojunction (SHJ) module, bifacial and monofacial perovskite (PVK)/c-Si tandem modules,

) irradiance sunlight irradiating on the bifacial PVK/c-Si tandem module.

b) the direct (Idir), diffuse (Idiff), and albedo (Ialbedo The remaining parameters (n, Rs, Rsh) were extracted from the J–V curve of a single-junction PVK with an efficiency of 21.4% reported by Fan et al.
[55] Assuming that all PVK solar cells with

|, and R|, the diode param-||) top cell in|
|---|---|---|---|
|sh|s|g_PVK [15,18,22]||
||||g_PVK|

different bandgaps had the same n, R eters used for the SHJ solar cell and PVK solar cell simulations are listed in Table S1, Supporting Information. The PCE could then be rationally obtained from the maximum power point (MPP) divided by the incident power.

2.3. Calculation of Annual EY The annual EY was evaluated based on PV modules at different locations with fixed tilt angles. The direct and diffuse sky irradi- ance at different locations were derived from the hourly resolved third edition of typical meteorological year data, in combination with the cloud model and the simple model of atmospheric radi- ative transfer of sunshine.
[56,57] The front-side illuminations on cells and modules were determined by the geographical location, season, and weather, and we assumed that the spectra varied equiproportionally with the light intensity. Since c-Si cells could efficiently absorb short-wavelength light below 900 nm, the reflection from the ground could hardly contribute to the photo- current of PVK top cell, [26,28,58,59] and thus the variation of the reflected spectrum had practically little effect on the EY of the monolithic bifacial tandem PV module. [19] The rear-side illumi- nation on the bifacial PV module was determined by a combina- tion of direct solar irradiance, diffuse sunlight scattered in the surrounding and atmosphere as well as ground albedo, assum- ing that all radiation received by the rear side was isotropic.

#### 3. Results and Discussion

There are three main sources of sunlight that irradiate on PV modules, [60] that is, direct light from the sun (Idir), diffuse sun- light scattered around and in the atmosphere (Idiff), and diffuse sunlight reflected from the ground (Ialbedo), as schematically shown in Figure 1b. In general, the Idirand Ialbedocontribute to the front- and rear-side irradiance on the PV modules, respec- tively, while the Idiffcan simultaneously interact with the front and rear side of the modules.

The optical simulations are carried out on SHJ, bifacial, and monofacial tandem solar cells, the structures of which are illus- trated in Figure S1, Supporting Information. According to pre- vious reports, the optimal bandgap of PVK (E the monofacial tandem device ranges from 1.65 to 1.70 eV under standard test condition (AM1.5G). As such, an E of

1.67 eV is first employed for the top PVK absorber. Assuming the absorption of one incident photon generates one electron–hole pair, and all electron–hole pairs contribute to the photocurrent, the Jsc_PVKand Jsc_c-Siare obtained by calculating the absorption in 300–1200 nm with an interval of 10 nm as mentioned in the method section. The optimized PVK thickness is found to be 820 nm in the monofacial tandem solar cell, under which the
2 J sc mismatch between PVK and c-Si is 0.01 mA cm (Figure S3, Supporting Information). In the subsequent modeling, the thick- ness of the PVK layer is fixed to 820 nm unless otherwise specified. The absorption spectra of each functional layer composing the monofacial and bifacial tandem solar cells with a PVK bandgap of 1.67 eV are represented in Figure S4a,b, Supporting Information, where only front-side illumination is considered. Due to the absence of Ag back reflector in the bifacial tandem solar cell, the reuse of light in the NIR region is significantly sup- pressed, resulting in a reduced absorption in both c-Si and rear 2 ITO. The Jsc_c-Siis reduced from 19.90 to 19.24 mA cm (also see Table S2, Supporting Information). The indirect bandgap characteristic of c-Si gives rise to a weak band-edge absorption [61] and thus reduced Jsc_c-Si. Similar result is also observed in PV modules (see Figure 2a,b) where₂ the equivalent Jsc_c-Siis reduced from 19.17 to 18.42 mA cm with a marginal change of Jsc_PVKwhen only front-side illumination is considered. The absolute current loss values in encapsulated modules (Figure 2a,b) compared with unencapsulated solar cells (see Figure S4a,b, Supporting Information) mainly originate from the increased front-side reflection and parasitic absorption from cover glass and ethylene vinyl acetate copolymer (see Table S2, Supporting Information for more detailed comparison). The same trend of cell-to-module loss is also found in bifacial SHJ solar cells and modules as shown in Figure S4c,d and Table S3, Supporting Information. Due to the reduced absorption of the c-Si in the bifacial tan- dem PV module, the Jsc_c-Sibecomes the limiting factor, and

Figure 2. The absorption of each layer as well as the reflection and transmission spectra of a) monofacial and b) bifacial tandem modules. c) The J

sc_PVK in monofacial and bifacial tandem modules. d) The plot of current density–voltage ( J–V) curves of bifacial tandem under AM1.5G (albedo = 0%), with the arrow pointing to increasing E g_PVK. The inset shows the equivalent circuit of the and Jsc_c-Sias a function of Eg_PVK modules with different Eg_PVK tandem solar cell.

therefore a higher Eg_PVKis required to reduce the current mis- match. The Jsc_PVKand Jsc_c-Siare then calculated as a function of Eg_PVKfrom 1.557 to 1.70 eV on both monofacial and bifacial tan- dem PV modules under AM1.5G front-side illumination as shown in Figure 2c. One can clearly see that the optimal PVK bandgap is increased to ≈1.69 eV for the bifacial case. The varia- tion of Eg_PVKwill affect both the subcell Jscand open-circuit volt- age (Voc), and thus the PCE of the tandem PV modules (Figure 2d). The equivalent circuit of a tandem solar cell is illus- trated in the inset of Figure 2d, where the one-diode models are used for each subcell. For the c-Si bottom cell, the diode param- eters (see Table S1, Supporting Information) are extracted from the J–V curve of an SHJ solar cell with a PCE of 25.11%, [53] which fits our modeled curve (Figure S5, Supporting Information) within the acceptable error range. One notes that this efficiency is a reasonable value since it is achievable in mass production, considering the recent record efficiency of 26.5%. [62] The J–V curves of PVK solar cells (Figure S6, Supporting Information) with different bandgaps are obtained by assuming the same n, Rsh, and Rsdiode parameters (see Experimental Section and Table S1, Supporting Information). [15]

Figure 2d shows the

J–V curves of the series-connected bifacial tandem modules with different Eg_PVK. Figure 2c depicts that the bifacial tandem solar cells having PVK subcells with 1.67 and 1.70 eV bandgaps render almost the same Jsc, where the current limiting subcell is

switched from c-Si to PVK. But thanks to the higher Voc, a higher module efficiency of 30.45% is achieved at an Eg_PVKof 1.70 eV. Thus, the current matching point should be for Eg_PVKof around

1.69 eV, which can deliver even higher module efficiency. In the previous discussion, however, the effect of rear-side irradiation on bifacial tandem modules was not considered, that is, albedo = 0%. The bifacial concept is known to be widely employed in c-Si modules. The SHJ solar cell with a bifaciality of more than 90% can produce a significant extra energy gain thanks to the rear-side power generation, which has been known to vary as a function of albedo.
[63,64] As such, in the following discussion, the rear-side illumination will be incorporated to assess the potential of bifacial tandem modules in generating additional power. The front illumination is kept at AM1.5G and the isotropic irradiance of the rear side is determined by the different albedo (Iback= albedo * IAM1.5G). A term so-called “pseudo-EQE” is employed to evaluate the photocurrent of the bifacial module, which is defined as the flux of electrons excited by both front- and rear-side illumination divided by the flux of photons incident on the solar cell from the front side. Take the Eg_PVKof 1.60 eV as an example,

Figure 3a shows the pseudo-EQE curves for bifacial tandem

PV modules at albedo = 0% and 100%. As the c-Si bottom cell receives additional reflected light at albedo = 100%, its pseudo-EQE values exhibit a sharp increase over the entire

Figure 3. a) Pseudo external quantum efficiencies (pseudo-EQE) curves

for bifacial tandem modules at albedo = 0% and 100%. b) J–V curves of bifacial tandem solar module, together with corresponding PVK top cell (Eg_PVK= 1.60 eV) and c-Si bottom cell for albedo of 0% and 25%. c) The J scof bifacial tandem modules as a function of albedo and Eg_PVK. The region highlighted in gray represents the albedo of typical ground condi- tion such as grass (albedo = 25%) and concrete (albedo = 35%). The point marked with star represents the current matching point at an albedo of 25% and Eg_PVKof 1.60 eV. “illum” and “IND” are abbreviations for illu- mination and independent, respectively.

spectral range and are greater than 100% from 770 to 1040 nm. The pseudo-EQE plots for other albedo values are also shown in Figure S7, Supporting Information, for references. Figure 3b

represents the variation of the J–V curves for the bifacial tandem module with Eg_PVK= 1.60 eV. The bifacial tandem PV module shifts from a large current mismatch ( Jsc_mismatch=

4.33 mA cm
2 ) at albedo = 0% to negligible current mismatch ( Jsc_mismatch= 0.03 mA cm 2 ) at albedo = 25%, and the PCE increases from 25.83% to 32.49%. As learned from the effect of albedo and Eg_PVKon Jscshown in Figure 3c, it is found that the smaller Eg_PVK, the more obvious the increase of albedo in improving the Jscof the tandem module. In other words, for bifacial tandem modules with large albedo, PVK subcell with a lower bandgap is preferred, which is consis- tent with previous reports. [29,30,58] The region highlighted in grey corresponds to the albedo for typical ground conditions, such as green grass (albedo = 25%) and concrete (albedo = 35%). [65,66]

The PCE of the tandem module of all Eg_PVKefficiently improves after implementing green grass (albedo = 25%) at the rear side (Figure S8, Supporting Information) and the current matching is achieved for Eg_PVK= 1.60 eV giving rise to maximum PCE of

32.49%. It is worth noting that with an Eg_PVKof 1.70 eV, PVK is the current-limiting subcell and increasing the albedo does not change the Jscof the tandem module. Instead, the increase in current mismatch causes an increase in fill factor (FF), which increases the PCE of the module from 30.45% to 30.94% (Figure S8f, Supporting Information). This is consistent with the previous report which states that the lowest value of FF is located at the current matching point.
[20,29] For bifacial tandem modules with other Eg_PVKs, one also sees an increasing FF with rising current mismatch after increasing albedo (see Figure S9, Supporting Information). The previous discussions have been conducted under ideal conditions without considering the location as well as the corre- sponding solar irradiance. In the realistic outdoor operation, a variety of factors including site conditions (i.e., albedo, average sun-hour, elevation from sea level, latitude, DNI, DHI, etc.) and PV module specifications (i.e., bifaciality, efficiency under stan- dard test condition, Eg_PVK, etc.) can strongly influence the power generation and EY of the bifacial tandem PV modules. [15,67–69] It is thus a challenging task to match Jsc_PVKand Jsc_c-Siin different geographical locations and under seasonal variations. To evaluate the performance of bifacial tandem modules in different regions, the calculation of EY is conducted at six sites with typical insola- tion conditions, that is, Chengdu (30.7°N, 104.1°E) (subtropical humid monsoon climate), Shanghai (31.4°N, 121.5°E) (northern subtropical monsoon climate), London (51.5°N, 0.1°W) (temper- ate maritime climate), Yinchuan (38.5°N, 106.2°E) (temperate continental climate), Lhasa (29.7°N, 91.1°E) (highland temperate semiarid monsoon climate), and Los Angeles (34.1°N, 118.2°W) (subtropical Mediterranean climate) (see Figure S10, Supporting Information, for meteorological data). Considering the cost of practical installation, the modules are designed with a fixed tilt angle. By summing the hourly EY (that is, the product of maximum power (PMPP P )and 1 h) over the entire year, one obtains the annual EY(¼ PMPP⋅ 1h). The shadow under the PV module that reduces ground reflection could be neglected at a module installation height of 1 m or more. [19]

Since the photocurrent of PVK subcell is hardly affected by the reflected light of <900 nm as mentioned earlier, the variation in the spectral distribution of reflected light has little effect on the

PVK subcell and thus the use of average albedo is justified for outdoor EY assessment. [28] To acquire a more realistic EY, temperature-dependent module performance should be consid- ered, which needs to account for ambient temperature, wind speed, as well as heat absorption and conduction between layers of PV module in different geographic environments. In addition, the scattered irradiation received from the rear side also affects the module temperature, making it more difficult to model the module temperature. To simplify the model, the shading effect of the surrounding modules, wind speed, temperature, and module degradation as well as their temperature coefficients are not con- sidered in the simulation. The EYs of bifacial tandem PV modules in different regions with respect to the tilt angle and Eg_PVKare represented in

Figure 4, where the albedo is set to a constant value of 25% (typ-

ical ground condition). The module with the highest EY of

622.0 kWh m
2 is found in Los Angeles, where the optimal Eg_PVKand tilt angle are around 1.62 eV and 32°, respectively. The highest EY in Chengdu, on the contrary, is only 242.5 kWh m 2. Both Lhasa and Yinchuan are characterized by good solar irradi- ance, [70,71] but since Lhasa shows higher DNI and DHI than Yinchuan (see Figure S10, Supporting Information), the bifacial tandem module yields a higher EY in Lhasa. Despite a better global horizontal irradiance (GHI) in Lhasa than that of Los Angeles, Lhasa yields a lower EY due to that its share of DHI in summer (mostly from June to September) being larger than that in Los Angeles (see Figure S10 and S11, Supporting Information). The optimal tilt angle of the modules is generally slightly lower than the latitude and positively correlated with lati- tude, that is, the higher the latitude, the higher the tilt angle. By

comparing the previous results, we found that the DNI can sig- nificantly affect the optimal Eg_PVK. In regions with high DNI such as Los Angeles, Lhasa, and Yinchuan, the Eg_PVKbetween

1.60 and 1.64 eV can match well with c-Si bottom cell to obtain a high output power and thus EY. In regions with high DHI (e.g., Shanghai, London, and Chengdu), the reflection from the front surface of the module is increased due to the oblique incidence, resulting in less photons reaching the PVK absorber. In addition, the DHI can also contribute to the photocurrent of c-Si cell, fur- ther enlarging the current mismatch between top and bottom subcells. In this case, lower Eg_PVK(1.56–1.60 eV) is better employed to achieve the current matching by enhancing the PVK absorption of photons with longer wavelengths to compen- sate for the reflection loss from the front side and the photocur- rent gain of the c-Si bottom cell. Finally, we modeled the EY of the bifacial PVK/c-Si tandem modules by varying the albedo to simulate different ground con- ditions (albedo = 9% for gray sandstone, albedo = 25% for grass, albedo = 35% for concrete, albedo = 64% for bright sandstone, and albedo = 88% for snow
[72] ) for the above locations with different meteorological conditions (see Figure 5 and S12, Supporting Information). The EY of the bifacial SHJ module is also calculated as a reference (see the gray bars in Figure 5a–c and S12, Supporting Information). For bifacial tandem modules with all values of Eg_PVK, increasing albedo leads to improved EY: the increase is more significant for the tandem modules with lower Eg_PVK. For tandem modules with Eg_PVKof 1.70 eV, despite the increasing current mismatch with increasing albedo, the EY still shows slow enhancement with higher albedo. This is mainly due to the increase in FF caused by the increase in

respect to the tilt angle and Eg_PVK.

Figure 4. The energy yields (EYs) of bifacial tandem modules in different regions (Chengdu, Shanghai, London, Yinchuan, Lhasa, and Los Angeles) with

Figure 5. A comparison of EY for bifacial SHJ modules and bifacial PVK/c-Si tandem modules in a) Chengdu, b) Shanghai, and c) Los Angeles. The power-

= 1.557 eV) at different albedo conditions in a summer day in d) Chengdu, e) Shanghai, and generation density (PGD) of bifacial tandem modules (Eg_PVK f ) Los Angeles, along with their meteorological characteristics.

current mismatch. [29] It is noted that for albedo = 0%, although the highest PCE is achieved with an Eg_PVKof 1.70 eV under stan- dard AM1.5G condition (Figure 2d), the highest EYs is achieved by the tandem modules with an Eg_PVKof 1.67 eV. This is because, during outdoor operation with albedo of 0%, the diffuse light from the surrounding atmosphere not only shines onto the PVK top cell but also contributes to the photocurrent of the c-Si bottom cell from the rear side. In this case, the tandem cells with an Eg_PVKof 1.67 eV feature better current matching and there- fore higher EYs. In all locations we studied, Eg_PVKof 1.557 eV results in the highest EY for all tandem modules when the albedo reaches 64% or higher (typical for bright sandstone or snow ground). To obtain the maximum EY for albedo = 25%, Eg_PVK in the range of 1.58–1.62 eV is strongly recommended.

It is known from literature that the PVK solar cells with lower Eg_PVKare characterized with lower voltage loss, higher stability, and maturer fabrication process. [31–34] Therefore, employing PVK top cells with reduced Eg_PVKin bifacial tandem modules is favorable for large-scale application. In areas with strong DHI (e.g., Chengdu) compared to areas with strong DNI (e.g., Los Angeles), more oblique incident light results in lower pho- tocurrent in the subcells. Whereas, the rear-side illumination on the bifacial tandem solar modules only contributes to the Jsc_c-Si enhancement, which is mainly determined by GHI and albedo, and is characterized by isotropy and less dependence on DNI. Thus, under relatively moderate albedo conditions (25–35%), regions with stronger DHI prefer narrower bandgaps to increase the absorption of PVK top cells.

Figure 6. Ratios between levelized cost of electricity (LCOE) and

tandem LCOESHJas a function of albedo. Cincrepresents the different installation cost increments (Cinc: 10% red, 13% yellow, 15% blue).

installation cost on the LCOE, that is, the higher the installation cost the greater the LCOE, which is consistent with previous [21,73] reports.

The power-generation densities (PGDs) of bifacial tandem modules with narrow bandgap PVK (Eg_PVK= 1.557 eV) are com- pared under different albedo conditions (Figure 5d–f ) for one summer day in Chengdu, Shanghai, and Los Angeles areas. The PGD is found to increase with increasing albedo, gradually saturating after albedo ≥ 35%. This trend can also be observed for EYs of bifacial tandem modules in different regions and with different Eg_PVK(see Figure S12 and S13, Supporting Information). This is because increasing the albedo only contributes to the pho- tocurrent of the c-Si bottom cell, and after an increase to a certain level, with the PVK top cell becoming the current limiting one, further increasing the albedo only leads to the current mismatch thus limiting the rapid growth of EY. In addition, DNI shows a stronger influence than DHI in determining the PGD of bifacial modules. Compared to Shanghai and Los Angeles, Chengdu shows the lowest DNI during day time thus its PGD also being the lowest. Meanwhile the fluctuation of DNI from 12:00 to 16:00 in Chengdu correlates well with the fluctuation of PGD. Since there is no current mismatch issue for bifacial SHJ modules, their EY increases linearly with the growth of albedo (see Figure S13, Supporting Information). In regions with large DHI such as Chengdu, London, and Shanghai, the EYs of SHJ modules are higher than those of tandem modules at albedo = 88%. Especially in Chengdu, the tandem PV modules are not superior in terms of EY at 35% albedo (ground condition of con- crete), and the EY is significantly smaller than that of the SHJ modules when the albedo is further increased (see Figure 5a and S12a, Supporting Information). Previous studies have shown that the manufacture cost of PVK/c-Si tandem PV module is about 121.18 $ m 2, which is 35% (31.59 $ m 2 in absolute value) higher than that of c-Si modules due to the additional materials and deposition process required for PVK. [21] The man- ufacture cost of single-junction c-Si modules is about 37% of the total installed costs. [1] Assuming the PVK/c-Si tandem modules holding the same fraction of manufacture cost, their total installed cost is estimated to be approximately 13% higher than of the c-Si counterpart. For ease of comparison, we have deployed a ratio (LCOEtandem/LCOESHJ)asdefined by the LCOE of bifacial PVK/c-Si tandem system divided by the LCOE of bifacial SHJ system, the ratio LCOEtandem/LCOESHJless than 1 means that the tandem system brings higher revenue. The calculation details are represented in Note S3, Supporting Information. The ratio of LCOE in six typical regions (see Figure 6 for the Chengdu and Los Angeles and Figure S14, Supporting Information, for other regions) has been calculated assuming the total installed cost of PVK/c-Si tandem modules being higher than that of SHJ mod- ules by 10%, 13%, and 15%, respectively. In conjunction with the previous discussion, the Eg_PVKis set to be 1.58 eV for regions with a large portion of DHI (e.g., Chengdu, London, Shanghai) and 1.62 eV for regions with a large portion of DNI (e.g., Yinchuan, Lhasa, Los Angeles). As shown in Figure 6 and S14, Supporting Information, it is seen that bifacial tandem modules possess cost advantages when installed in Los Angeles with high DNI share and albedo between 9% and 35%. And, the tandem module no longer has the advan- tage over SHJ module when albedo exceeds 40%. More intrigu- ingly, deploying bifacial SHJ modules in Chengdu, which has dominant DHI, is always an economical choice regardless of the albedo value. Figure 6 also demonstrates the impact of the

#### 4. Conclusion

In this work, we have investigated the EY characteristics of bifa- cial PVK/c-Si tandem modules and compared them with bifacial SHJ modules under realistic outdoor operation conditions (i.e., meteorological data of installation sites, albedo, etc.). The photo- current of the subcells and the optimal Eg_PVKfor monofacial and bifacial modules were obtained based on the light absorption of PVK and c-Si in the tandem solar cells and modules. Rear-side irradiation only boosts the photocurrent of the c-Si bottom cell, so increasing the rear-side irradiation intensity enables the employ- ment of PVK materials with smaller bandgaps for more light absorption from the front side. For example, at typical ground conditions with albedo = 25%, the current matching is achieved for Eg_PVK= 1.60 eV, and the module efficiency reaches 32.49%. We then examined the EY of six typical regions under different albedo conditions. The optimal Eg_PVKwas found to be 1.62 eV or even lower for albedo greater than 25%. In areas with a high DNI such as Yinchuan and Los Angeles, bifacial tandem modules deliver higher EY regardless of ground type with or without albedo, while in areas with a high DHI such as Chengdu, bifacial SHJ modules exhibit similar or even higher EY than that of tan- dem modules. Given the LCOE considerations, we recommend deploying bifacial SHJ modules under strong DHI or high albedo conditions rather than tandem ones. Overall, the bifacial tandem modules with Eg_PVKin the range of 1.58–1.62 eV are suitable for most application scenarios. The PVK solar cells with lower Eg_PVKare characterized with lower voltage loss, higher sta- bility, and maturer fabrication process, which would further pro- mote the large-scale application of bifacial tandem PV modules. Bifacial PVK/c-Si tandem modules have the potential to gen- erate additional energy output by receiving reflected light from the ground, thus provide an effective strategy to further improve the efficiency and EY of PV modules. However, the EY generated

by bifacial PVK/c-Si tandem modules under realistic outdoor operation varies with installation locations and conditions (such as albedo etc.). Our work provides important implications for pol- icy making in determining the correct type of PV modules in delivering cost-effective renewable electricity.

#### Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

#### Acknowledgements

This work was supported by the National Key R&D Program of China (Grant no. 2022YFB4200204), Natural Science Foundation of Shanghai (grant no. 20520760700), the Shanxi Science and Technology Department (grant no. 20201101012), the DNL Cooperation Fund, CAS (Grant no. DNL202015), the National Natural Science Foundation of China (grant no. 22279140), and the Key Applied Basic Research Program of Yunnan Province (grant no. 202201AS070023).

#### Conflict of Interest

The authors declare no conflict of interest.

#### Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### Keywords

albedo, bandgaps, bifacial modules, energy yield, perovskite/silicon tandem solar cells

Received: March 21, 2023 Revised: May 21, 2023 Published online: June 8, 2023

[1] ISE, [https://www.ise.fraunhofer.de/content/dam/ise/de/documents/](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/) publications/studies/Photovoltaics-Report.pdf (accessed: May 2022). [2] X. Qu, Y. He, M. Qu, T. Ruan, F. Chu, Z. Zheng, Y. Ma, Y. Chen, X. Ru,

X. Xu, H. Yan, L. Wang, Y. Zhang, X. Hao, Z. Hameiri, Z.-G. Chen,
L. Wang, K. Zheng, Nat. Energy 2021, 6, 194.
[3] At 26.81%, [https://www.longi.com/en/news/propelling-the-](https://www.longi.com/en/news/propelling-the-) transformation/ (accessed: November 2022). [4] W. Shockley, H. J. Queisser, J. Appl. Phys. 1961, 32, 510. [5] Q. Ou, X. Bao, Y. Zhang, H. Shao, G. Xing, X. Li, L. Shao, Q. Bao, Nano Mater. Sci. 2019, 1, 268. [6] E. L. Unger, L. Kegelmann, K. Suchan, D. Sörell, L. Korte, S. Albrecht,

J. Mater. Chem. A 2017, 5, 11401.
[7] J.P.Mailoa,C.D.Bailie,E.C.Johlin,E.T.Hoke,A.J.Akey,W.H.Nguyen,

M. D. McGehee, T. Buonassisi, Appl. Phys. Lett. 2015, 106, 121105.
[8] KAUST, [https://www.kaust.edu.sa/news/kaust-team-sets-world-record-](https://www.kaust.edu.sa/news/kaust-team-sets-world-record-) for-tandem-solar-cell-efficiency (accessed: May 2023). [9] E. H. Jung, N. J. Jeon, E. Y. Park, C. S. Moon, T. J. Shin, T. Y. Yang,

J. H. Noh, J. Seo, Nature 2019, 567, 511.
[10] J. A. Schwenzer, L. Rakocevic, T. Abzieher, D. Rueda-Delgado,

S. Moghadamzadeh, S. Gharibzadeh, I. M. Hossain, R. Gehlhaar,
B. S. Richards, U. Lemmer, U. W. Paetzold, IEEE J. Photovoltaics 2020, 10, 777.
[11] W. Xiang, S. Liu, W. Tress, Energy Environ. Sci. 2021, 14, 2090. [12] H. Ma, M. Wang, Y. Wang, Q. Dong, J. Liu, Y. Yin, J. Zhang, M. Pei,

L. Zhang, W. Cai, L. Shi, W. Tian, S. Jin, J. Bian, Y. Shi, Chem, Eng. J. 2022, 442, 136291.
[13] Q. Jiang, J. Tong, Y. Xian, R. A. Kerner, S. P. Dunfield, C. Xiao,

R. A. Scheidt, D. Kuciauskas, X. Wang, M. P. Hautzinger,
R. Tirawat, M. C. Beard, D. P. Fenning, J. J. Berry, B. W. Larson,
Y. Yan, K. Zhu, Nature 2022, 611, 278.
[14] G. Li, Z. Su, L. Canil, D. Hughes, M. H. Aldamasy, J. Dagar,

S. Trofimov, L. Wang, W. Zuo, J. J. Jeronimo-Rendon,
M. M. Byranvand, C. Wang, R. Zhu, Z. Zhang, F. Yang, G. Nasti,
B. Naydenov, W. C. Tsoi, Z. Li, X. Gao, Z. Wang, Y. Jia, E. Unger,
M. Saliba, M. Li, A. Abate, Science 2023, 379, 399.
[15] M. T. Hörantner, H. J. Snaith, Energy Environ. Sci. 2017, 10, 1983. [16] J. Lehr, M. Langenhorst, R. Schmager, S. Kirner, U. Lemmer,

B. S. Richards, C. Case, U. W. Paetzold, Sustainable Energy Fuels 2018, 2, 2754.
[17] N. Tucher, O. Hohn, J. N. Murthy, J. C. Martinez, M. Steiner,

A. Armbruster, E. Lorenz, B. Blasi, J. C. Goldschmidt, Opt. Express 2019, 27, A1419.
[18] E. Aydin, T. G. Allen, M. De Bastiani, L. Xu, J. Ávila, M. Salvador,

E. Van Kerschaver, S. De Wolf, Nat. Energy 2020, 5, 851.
[19] J. Lehr, M. Langenhorst, R. Schmager, F. Gota, S. Kirner, U. Lemmer,

B. S. Richards, C. Case, U. W. Paetzold, Sol. Energy Mater. Sol. Cells 2020, 208, 110367.
[20] Y. Kato, H. Katayama, T. Kobayashi, M. Kozawa, Y. Nishigaki,

T. Kobayashi, Y. Kinden, K. Oiwake, R. Ishihara, T. Matsui, Y. Aya,
T. Hashiguchi, D. Kanematsu, A. Terakawa, H. Fujiwara, Prog. Photovoltaics Res. Appl. 2022, 30, 1198.
[21] Z. Li, Y. Zhao, X. Wang, Y. Sun, Z. Zhao, Y. Li, H. Zhou, Q. Chen, Joule 2018, 2, 1559. [22] D. A. Jacobs, M. Langenhorst, F. Sahli, B. S. Richards, T. P. White,

C. Ballif, K. R. Catchpole, U. W. Paetzold, J. Phys. Chem. Lett. 2019, 10, 3159.
[23] F. Gota, M. Langenhorst, R. Schmager, J. Lehr, U. W. Paetzold, Joule 2020, 4, 2387. [24] R. Guerrero-Lemus, R. Vega, T. Kim, A. Kimm, L. E. Shephard, Renewable Sustainable Energy Rev. 2016, 60, 1533. [25] R. Kopecek, J. Libal, Nat. Energy 2018, 3, 443. [26] T. S. Liang, M. Pravettoni, C. Deline, J. S. Stein, R. Kopecek,

J. P. Singh, W. Luo, Y. Wang, A. G. Aberle, Y. S. Khoo, Energy Environ. Sci. 2019, 12, 116.
[27] International Technology Roadmap for Photovoltaic (ITRPV), https:// itrpv.vdma.org (accessed: May 2022). [28] A. Onno, N. Rodkey, A. Asgharzadeh, S. Manzoor, Z. J. Yu, F. Toor,

Z. C. Holman, Joule 2020, 4, 580.
[29] M. De Bastiani, A. J. Mirabelli, Y. Hou, F. Gota, E. Aydin, T. G. Allen,

J. Troughton, A. S. Subbiah, F. H. Isikgor, J. Liu, L. Xu, B. Chen, E. Van Kerschaver, D. Baran, B. Fraboni, M. F. Salvador, U. W. Paetzold,
E. H. Sargent, S. De Wolf, Nat. Energy 2021, 6, 167.
[30] K. Jäger, P. Tillmann, E. A. Katz, C. Becker, Sol. RRL 2021, 5, 2000628. [31] A. Rajagopal, R. J. Stoddard, S. B. Jo, H. W. Hillhouse, A. K. Jen, Nano Lett. 2018, 18, 3985. [32] G. Yang, Z. Ren, K. Liu, M. Qin, W. Deng, H. Zhang, H. Wang,

J. Liang, F. Ye, Q. Liang, H. Yin, Y. Chen, Y. Zhuang, S. Li,
B. Gao, J. Wang, T. Shi, X. Wang, X. Lu, H. Wu, J. Hou, D. Lei,
S. K. So, Y. Yang, G. Fang, G. Li, Nat. Photonics 2021, 15, 681.
[33] L. Qiu, S. He, L. K. Ono, S. Liu, Y. Qi, ACS Energy Lett. 2019, 4,

2147.
[34] J. P. Correa-Baena, M. Saliba, T. Buonassisi, M. Gratzel, A. Abate,

W. Tress, A. Hagfeldt, Science 2017, 358, 739.

[35] P. V. Lighthouse, [https://www.pvlighthouse.com.au/sunsolve](https://www.pvlighthouse.com.au/sunsolve) (accessed: May 2022). [36] S. Manzoor, J. Hausele, K. A. Bush, A. F. Palmstrom, J. Carpenter,

Z. J. Yu, S. F. Bent, M. D. McGehee, Z. C. Holman, Opt. Express 2018, 26, 27441.
[37] J. M. Siqueiros, R. Machorro, L. E. Regalado, Appl. Opt. 1988, 27,2549. [38] K. R. McIntosh, J. N. Cotsell, J. S. Cumpston, A. W. Norris,

N. E. Powell, B. M. Ketola, presented at 2009 34th IEEE Photovoltaic Specialists Conf. (PVSC), Philadelphia, PA, USA June
2009.
[39] Z. C. Holman, A. Descoeudres, L. Barraud, F. Z. Fernandez, J. P. Seif,

S. De Wolf, C. Ballif, IEEE J. Photovoltaics 2012, 2,7.
[40] Z. C. Holman, M. Filipic,ˇ A. Descoeudres, S. De Wolf, F. Smole,

M. Topic, C. Ballif, ˇ J. Appl. Phys. 2013, 113, 013107.
[41] M. N. Mullings, C. Hagglund, S. F. Bent, J. Vac. Sci. Technol. A 2013, 31, 061503. [42] H. T. Nguyen, F. E. Rougieux, B. Mitchell, D. Macdonald, J. Appl. Phys. 2014, 115, 043710. [43] M. Morales-Masis, S. Martin De Nicolas, J. Holovsky, S. De Wolf,

C. Ballif, IEEE J. Photovoltaics 2015, 5, 1340.
[44] M. R. Vogt, PhD Thesis, Delft University of Technology, 2015. [45] Y. Jiang, S. Pillai, M. A. Green, Sci. Rep. 2016, 6, 30605. [46] R. Santbergen, R. Mishima, T. Meguro, M. Hino, H. Uzu, J. Blanker,

K. Yamamoto, M. Zeman, Opt. Express 2016, 24, A1288.
[47] M. R. Vogt, H. Hahn, H. Holst, M. Winter, C. Schinke, M. Kontges,

R. Brendel, P. P. Altermatt, IEEE J. Photovoltaics 2016, 6, 111.
[48] J. M. Ball, S. D. Stranks, M. T. Hörantner, S. Hüttner, W. Zhang,

E. J. W. Crossland, I. Ramirez, M. Riede, M. B. Johnston,
R. H. Friend, H. J. Snaith, Energy Environ. Sci. 2015, 8, 602.
[49] Q. Lin, A. Armin, R. C. R. Nagiri, P. L. Burn, P. Meredith, Nat. Photonics 2014, 9, 106. [50] S. Lin, H. Tseng, S. Hsu, Y. Chen, C. Lin, presented at 2015 Int. Symp. on Next-Generation Electronics (ISNE), Taipei, Taiwan May 2015. [51] NREL, [https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html](https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html) (accessed: May 2022). [52] LTspice, [https://www.analog.com/en/design-center/design-tools-and-](https://www.analog.com/en/design-center/design-tools-and-) calculators/ltspice-simulator.html (accessed: May 2022). [53] X. Ru, M. Qu, J. Wang, T. Ruan, M. Yang, F. Peng, W. Long, K. Zheng,

H. Yan, X. Xu, Sol. Energy Mater. Sol. Cells 2020, 215, 110643.
[54] K. Tvingstedt, O. Malinkiewicz, A. Baumann, C. Deibel, H. J. Snaith,

V. Dyakonov, H. J. Bolink, Sci. Rep. 2014, 4, 6071.
[55] H. Fan, F. Li, P. Wang, Z. Gu, J. H. Huang, K. J. Jiang, B. Guan,

L. M. Yang, X. Zhou, Y. Song, Nat. Commun. 2020, 11, 5402.
[56] S. W. a. W. Marion, [https://www.nrel.gov/docs/fy08osti/43156.pdf](https://www.nrel.gov/docs/fy08osti/43156.pdf) (accessed: May 2022). [57] C. A. Gueymard, Sol. Energy 2001, 71, 325. [58] J. Chantana, Y. Kawano, T. Nishimura, A. Mavlonov, T. Minemoto, Sol. Energy 2021, 220, 163. [59] Y. Zhang, Y. Yu, F. Meng, Z. Liu, IEEE J. Photovoltaics 2020, 10, 296. [60] P. Tillmann, K. Jäger, A. Karsenti, L. Kreinin, C. Becker, Sol. RRL 2022, 6, 2200079. [61] S. H. Zaidi, J. M. Gee, D. S. W. Ruby, S. R. J. Brueck, in SPIE’s 44th Annual Meeting and Exhibition, Denver, CO (US) July 1999. [62] E. BELLINI, [https://www.pv-magazine.com/2022/06/24/longis-](https://www.pv-magazine.com/2022/06/24/longis-) heterojunction-solar-cell-hits-26-5/ (accessed: July 2022). [63] A. Cruz, D. Erfurt, P. Wagner, A. B. Morales-Vilches, F. Ruske,

R. Schlatmann, B. Stannowski, Sol. Energy Mater. Sol. Cells 2022, 236, 111493.
[64] G. J. M. Janssen, B. B. Van Aken, A. J. Carr, A. A. Mewe, Energy Proc. 2015, 77, 364. [65] PVPMC, Albedo, [https://pvpmc.sandia.gov/modeling-steps/1-weather-](https://pvpmc.sandia.gov/modeling-steps/1-weather-) design-inputs/plane-of-array-poa-irradiance/calculating-poa-irradiance/ poa-ground-reflected/albedo/ (accessed: May 2022). [66] T. Markvart, L. Castaner, ˜ Practical Handbook of Photovoltaics: Fundamentals and Applications, Elsevier Science, Amsterdam (Netherlands) 2003. [67] C. Gao, D. Du, W. Shen, Carbon Neutrality 2022, 1,9. [68] L. Ba, T. Wang, J. Wang, W. Shen, J. Phys. Chem. C 2019, 123, 28659. [69] M. H. Futscher, B. Ehrler, ACS Energy Lett. 2017, 2, 2089. [70] Z. Zeng, Z. Wang, K. Gui, X. Yan, M. Gao, M. Luo, H. Geng, T. Liao,

X. Li, J. An, H. Liu, C. He, G. Ning, Y. Yang, Earth Space Sci. 2020, 7, e2019EA001058.
[71] Solar resource maps of China, [https://solargis.com/maps-and-gis-](https://solargis.com/maps-and-gis-) data/download (accessed: May 2022). [72] A. M. Baldridge, S. J. Hook, C. I. Grove, G. Rivera, Remote Sens. Environ. 2009, 113, 711. [73] M. De Bastiani, A. S. Subbiah, M. Babics, E. Ugur, L. Xu, J. Liu,

T. G. Allen, E. Aydin, S. De Wolf, Joule 2022, 6, 1431.
