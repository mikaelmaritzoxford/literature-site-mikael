##### Progress in Photovoltaics: Research and Applications

##### SPECIAL ISSUE ARTICLE OPEN ACCESS

# Comparison on Module Performance and Degradation Robustness of Two-

#, Three-, and Four-

Youri Blom | Wenang Suprayogi | Malte Ruben Vogt | Olindo Isabella | Rudi Santbergen**Terminal**

Delft University of Technology, Photovoltaic Materials and Devices Group, Delft, the Netherlands

# Perovskite Silicon Configurations Under Realistic

**Correspondence:**

# Operating Conditions

Youri Blom and Rudi Santbergen (y.blom@tudelft.nl; r.santbergen@tudelft.nl)

**Received:** 8 July 2025 | **Revised:** 11 December 2025 | **Accepted:** 22 December 2025

**Keywords:** energy losses | energy yield modelling | perovskite/silicon cells | two- terminal/three- terminal/four- **ABSTRACT**Terminal Perovskite/silicon (PS) technology includes three main configurations: two- terminal (2T), three- terminal (3T), and four-

*E*) optimization at *g* terminal
the module level for different configurations under outdoor conditions. Using opto- (4T). Previous studies have made various comparisons between these configurations, significantly advancing our understanding electrical simulations, we predict the energy *Eg*. The optimal *Eg* for the 2T, 3T, and 4T modules yield of each module at four geographical locations, with varying values of of these devices. While these studies mostly focus on simulations on cell level, we perform bandgap energy ( are 1.62, 1.80, and 1.82 eV, respectively. We also perform a loss analysis to explore the differences in power losses among the configurations. These loss differences can be attributed to the configurations having different optimal *Eg* values (affecting the thermalization losses) or different module designs (affecting the interconnection losses). Among all losses, mismatch losses play the most critical role in optimizing the bandgap. Overall, all optimized configurations have similar energy yields (all differences within 1.5%) across all locations. Finally, we compare the robustness of the different configurations against different scenarios of perovskite degradation. Our results show that the 4T module is the least sensitive to degradation in the perovskite subcell.

##### 1 | Introduction

This PS technology can come in three main configurations: two- Conventional crystalline silicon (c- terminal (2T), three- Si) cells currently dominate terminal (3T), and four- the photovoltaic (PV) market, holding a 97% market share  [1] terminal (4T) con- and achieving a power conversion efficiency (PCE) of up to figurations [9–12], as illustrated in Figure 1a.

27.3%  [2], approaching their theoretical limit of 29.5% [3, 4]. To surpass this limit, perovskite/silicon (PS) tandem cells offer a In the 2T design, the perovskite top cell is monolithically stacked promising alternative, with practical (considering reduced ion atop the silicon bottom cell, forming a wafer- density, ideal series resistance, ideal transport layers, ideal bulk
based module (as lifetime and improved optical performance [5]) and theoretical shown in Figure  1b). The top and bottom cells are connected efficiency limits of 39.5% [5] and 42% [6, 7], respectively, and a in series with a tunnel junction or recombination layer [9, 14], demonstrated record efficiency of 35.0% [8]. requiring current matching between top and bottom cell  [12]. While this design constraint limits flexibility, the intercon- nection of the cells within the module remains relatively sim- ple, as the tandem cell has the same number of terminals as a This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes. © 2026 The Author(s). Progress in Photovoltaics: Research and Applications published by John Wiley & Sons Ltd.

*Progress in Photovoltaics: Research and Applications,* 2026; 0:1–14 [https://doi.org/10.1002/pip.70066](https://doi.org/10.1002/pip.70066)

1099159x, 0, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.70066](https://onlinelibrary.wiley.com/doi/10.1002/pip.70066) by Oxford University, Wiley Online Library on [26/01/2026]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

|a)|||2 Terminal|3 Terminal|4 Terminal|b)|
|---|---|---|---|---|---|---|
|||Currentmatching Moduleinterconnection Opticalresponse Degradation|Glass Encapsulant Perovskite Silicon|Glass Encapsulant Perovskite Silicon|Glass Perovskite Encapsulant Silicon|Wafer-based module Thin-filmmodule|
|FIGURE 1|||||module interconnection, optical response, and robustness against degradation. (b) The difference between a wafer-|(a) An overview of the 2T, 3T, and 4T configurations at module level and a comparison of different aspects, such as current matching,|based and a thin-|

film module. The schematics are taken from [13].

single- junction c- Si cell. Additionally, the top cell is conformal and follows the texturing of the bottom cell, enhancing the opti- cal performance [15].

The 3T configuration introduces an additional contact, allow- ing independent current flow in each subcell and removing the need for current matching [16]. This additional contact can be placed between the subcells or at the rear of the bottom cell, as demonstrated by Warren et  al.  [17] or a heterojunction bipolar transistor (HBT) architecture can be considered [18]. This study only analyzes the option with an additional contact at the rear side. However, the 3T configuration requires more complex module interconnections, typically forming a parallel/series connection  [19], and experiences end- losses  [9]. The cause for the end- losses are discussed in Section  2.3. As the 3T module is a wafer- based, similar to the 2T configuration, it also has low optical losses.

In the 4T configuration, the top and bottom subcells are elec- trically separated, enabling each to operate at its own current. Unlike the other configurations, the perovskite layer is de- posited on the glass instead of directly on the silicon cell [20], with an encapsulant layer separating the top and bottom cells. Consequently, the 4T device consists of a wafer- based submodule for the silicon cells and a thin- film submodule for the perovskite cells, as shown in Figure 1b. This electrical separation simplifies module interconnections compared to 3T, forming two distinct series-connected strings  [9]. However, the 4T design can have more optical losses due to an additional layers [12], and the fact that top cell does not follow the same texturing as the bottom cell, as they are not stacked monolithically. Furthermore, 4T modules require an optical coupling layer to advance the optical absorption [21]. Additionally, it should be realized that if both submodules are not voltage matched, both strings need their own maximum power point tracking [9].

Each configuration also differs in robustness against degrada- tion. A study by Qian et  al.  [22] showed that 4T modules are more resilient against perovskite degradation than 2T modules. Specifically, Qian's findings indicate that for every 1% increase in degradation rate in the perovskite layer, the efficiency must

rise by 2% in 2T devices but only 1% in 4T devices to maintain performance. However, 3T modules were not considered in this comparison.

Assigning a universally superior configuration is challenging, as each offers unique advantages. Several studies have used *Eg*) varies across optoelectrical simulations to quantify performance differences configurations, identifying ideal values of 1.73 eV for the 2T and among these configurations. Futscher et  al.  [

1.81 eV for both the 3T and 4T configurations. 23] calculated ef- ficiency limits for 2T, 3T, and 4T devices under standard test conditions (STC), finding maximum efficiencies of 45.1%, 45.3%, Additional studies provide insights into energy yield (EY) at the and 45.3%, respectively. These maximum efficiencies are lower cell and module levels. Gota et  al.  [24] found that the 3T con- in virtually all realistic outdoor conditions [ figuration has higher EY across various locations and demon
7]. Their study also-examined how the optimal bandgap energy ( strated greater resilience to variations in perovskite thickness and *Eg* than the 2T design. McMahon et al. [25] showed that the 3T configuration could outperform 2T in energy production at the module level, provided that a sufficient number of cells are included, such that the end- losses are small. In an optical study, Singh et al. [26] compared the average photo- generated current for 2T, 3T, and 4T modules in operating conditions, showing how the absorbed light is affected by changes in perovskite thickness and bandgap energy. Lastly, Kikelj et al. [27] concluded that 3T devices can surpass 2T devices in performance with optimized module design.

While these studies have advanced the understanding of each *E* at the module level, accounting for realistic optical and electrical configuration, certain aspects remain underexplored. Key con *g* - properties, have not been thoroughly addressed. These cell- siderations like cell- to-to- module losses include optical losses due to glass and encapsu module losses and the optimization of- lant, non- active area losses, and ohmic interconnection losses. Additionally, to the best of the authors' knowledge, the robust- ness against perovskite degradation for 3T modules has not been studied.*Progress in Photovoltaics: Research and Applications,*

This study evaluates the potential of 2T, 3T, and 4T devices at the module level. Using a PS cell from the literature as a benchmark, we simulate the EY while accounting for var- ious cell-*Eg* is determined for each configuration, and all losses are quantified to facilitate to- a comprehensive comparison. Finally, we simulate differ module losses. The optimal- ent degradation scenarios to assess the robustness of each configuration.

It is important to note that this study focuses solely on monofa- cial modules. Given that bifacial technology is expected to dom- inate in the future  [1], including in IBC module architectures, further studies on 2T, 3T, and 4T bifacial modules can be consid- ered in future work.

##### 2 | Methodology

All simulations are conducted using the PVMD Toolbox [13, 28, 29], a modeling framework for calculating the energy yield of PV modules. As described in detail by Vogt et al. [28], the PVMD Toolbox consists of sequential simulation steps, each modeling a different aspect of the PV module. First, the spec- tral response of the encapsulated solar cell is simulated. This spectral response is then used to calculate the absorbed irradi- ance, also accounting for shading by other modules in the field. To calculate the absorbed irradiance, the module orientation and the geographical location should be specified. Then, the cell temperatures are calculated by considering different heat flows. Lastly, the annual energy yield is obtained by calculat- ing the electricity production for each hour in the year based on hourly weather data and integrating over time. It is important to realize that all simulation steps are based on first- principle physics, meaning empirical fitting is only used for the model- ing of meta- stability, as explained later in this section. Here, we summarize the components relevant to this study and discuss

##### 2 Terminal 3 Terminal

the inputs used. The design of the cells within the PV modules are based on the 32.5% efficient 2T PS cell by Mariotti et al. [30] with a perovskite bandgap energy of 1.68  eV, which has been integrated in the Toolbox in earlier work [13, 29]. This bandgap energy, however, is also an input parameter that can be varied, as also demonstrated in the earlier work.

In previous work, the PVMD Toolbox was validated for STC per- formance in PS tandem cells (error lower than 2% [13]) and for outdoor performance in c- Si modules (root mean square error of

4.5% [28]) At the end of this section, we will extend the valida-
**2.1** tion to PS tandem cells under outdoor operation. **| Optical Modeling** Optical simulations were performed with GenPro [31], which applies the net radiation method  [32]. Required in- puts include the thickness (*d*) and complex refractive index (*N*(*𝜆*) = *n*(*𝜆*) + *j* ⋅ *k*(*𝜆*)) of each layer, enabling calculation of the implied photo-
current density. More details on this calculation is provided in the Supporting Information.

Figure 2 illustrates the optical structures of each configuration. The structures and reported thicknesses are based on the PS cell by Mariotti et  al.  [30] with some thicknesses slightly adjusted to have a good match between simulation and measurement. The bottom cell has texturing on both sides with pyramids of 5 µm. In the 3T configuration, which features both positive and negative contacts on the rear, a gapless Interdigitated Back Contact (IBC) architecture is considered. GenPro performs one- dimensional absorption simulations, so only one rear- side layer can be included. The Supporting Information shows that using either the positive or negative layer yields similar absorption profiles. For this study, we used the a- Si(p) layer in the optical simulations. 4 Terminal

**FIGURE 2** |

*Progress in Photovoltaics: Research and Applications,*

The structures that are used as input for the optical simulations. For the 3T case, we simply consider a gapless IBC architecture.

The 2T and 3T modules uses indium zinc oxide (IZO) as trans- parent conductive oxide (TCO), being similar to the state-

the- art reference solar cell by Mariotti et al. [30] The thin- film submodule in the 4T configuration, however, must provide sufficient lateral conductivity where cells are interconnected through a series of laser scribes. The monolithic patterning fol- lows the usual P1-P2-P3 sequence: P1 opens the front electrode, P3 separates the back electrode, and P2 bridges the back elec- trode of one cell to the front electrode of the next through the TCO layer. Together, these scribes define the individual cells and establish the series connection within the module  [33]. When connected, the current needs to be collected over the en- tire length of the cell, instead of only to the nearest metal fin 1. 0 ⋅ 10− 4Ω cm− 2[34]) compared to IZO- (ger, requiring a low resistivity for the TCO layer. Therefore, the 4. 5 ⋅ 10 − 4 Ω cm− 2[35]), is therefore better suited for thin- 4T modules uses fluorine-film modules. Additionally, the TCO thickness is larger for the 4T doped tin oxide (FTO) as TCO, as it modules, as it was found in previous work that this is beneficial has a lower resistivity ( for thin- film modules [13]. Furthermore, the perovskite subcell in the 4T modules is deposited on glass that has been prepro- cessed with Asahi U- type texturing [36].

When cells are integrated into a module, some active area is *k* *shaded*) that excludes shaded areas lost due to metallization (for wafer- from current generation. The output current ( *Iout*) is then cal- culated as based modules) or laser scribing (for thin- *I* *out* film modules). We account for this by de = (1 −*k* *shaded*) ⋅ *Acell*⋅ *Jact*, (1)- fining a shaded- where *Acell* is the cell area, and area factor ( *J* *act* is the current density of the cell's active area.

The value of *kshaded* depends on the origin of the active area losses, and is therefore different for wafer- based and thin- film modules. For wafer- based modules, these losses come from metal fingers needed for the current collection. We assumed a *k* *shaded* in wafer- metal coverage of 5%, based on the work of Rehman et al. [ 37]. However, the effective area that is lost can be 60% lower due to based modules. In thin- internal reflections  [38], leading to a value of 2% for film modules, the laser scribing *k* *shaded* to be 8%, which depends on the widths of P1, P2 and P3. Besides that connects the cells requires an area that cannot be used for these non- current collection. In previous work [ 13], we calculated active area losses due to metalization, there are also

non-

cussed in Section 2.3.

**2.2 | Electrical Modelling** As the details for the electrical framework have been fully ex- plained in previous work [13, 28, 29], we only highlight the elec- trical structures used for the simulations. Figure  3 shows the circuit representation of each configuration. Each subcell is rep- resented with a calibrated one-
diode equivalent circuit model (including own series and parallel resistors), and resistances are added to represent the current collection losses. The explanation of how the calibrated one- diode equivalent circuit models are created and used is provided in the Supporting Information. An important assumption is that the same electrical performance of the perovskite and silicon subcells is used for all configura- tions. This also means that same electrical performance is con- sidered for the 3T configuration, that employs an IBC silicon bottom cell. The reason for this assumption is that the advanced semiconductor analysis (ASA) [39], the software utilized for the semiconductor simulations, only considers one- dimension.

Since the process of current collection differs for wafer- *Rcon*,*met*based ) of

3.9 m modules and thin-Ω, as calculated by Jung et al. [ 40]. In thin-
film modules, different values of resistances film modules, are used. Wafer- cells are connected through laser scribing, with ohmic losses occurring through the TCO layer that connect the cells. Based based modules experience ohmic losses as the current needs to be collected by metal fingers on top of the cell. on the method in earlier work  [13], we have calculated that *Rcon*,*tf*) of 9.7 m This metallization is represented by a resistance ( these ohmic losses can be represented by a resistance ( Ω.

||2 Terminal R con,met|3 Terminal R con,met|4 Terminal R con,tf|
|---|---|---|---|
|Top||||
|cell|||R con,met|
|Bottom||||
|cell||R con,met||

**FIGURE 3** | The circuit representation of the electrical simulations.

##### 2.3 | Module Interconnection

As mentioned before, the various configurations have different module interconnections. Figure  4 shows the interconnection scheme of the different configurations. The 2T and 4T follow a relative simple interconnection with, respectively, one and two series- connected strings of subcells. For the 3T module, we use the interconnection proposed by McMahon et  al.  [ *m* bottom cells connect in parallel with *n* top cells, re 41],- quiring voltage matching. It can be seen that, due to this con where- nection, *m* bottom cells and *n* top cells cannot contribute to the

of-active area losses due to cell spacing. This is further dis-

power generation, representing the end losses. In our work, we assume *m* = 2 and *n* = 1, as shown in Figure  4, minimiz-0.0 mm. The value for thin-*kshaded*. ing the end losses. To justify this assumption, the Supporting film modules is taken to be 0, as all Information contains a bandgap optimization at STC for differ-non-An important characteristic that will be used in Section 4 are the ent values of *m* and *n*, showing that the chosen combination has so-called active area due to laser-*mismatch losses*, which represent the losses when in- the highest potential. Additionally, the Supporting Information dividual subcells cannot operate on their individual maximum scribing is included in provides full implementation details and validation with a cir-power point. The mismatch losses are calculated according to cuit simulator. our definition from earlier work [7] and are written as

Table  1 summarizes the module sizing for both wafer- *N* *cells*

|∑ (||) −||),|
|---|---|---|---|---|
|P =|P|I ⋅ (V|+ I ⋅ R|⋅ N|

based + *P* *mism mpp*,*top*− *i mpp*,*bot* − *i mod mod mod con cells* and thin-*i*= 1 film modules. For wafer-(2) based modules, we used G12 where *P* *mpp*,*top* and *Pmpp*,*bot* are maximum power point of the in- *i i* wafers with half- dividual top and bottom subcell, respectively, *Imod* and *Vmod* is the *Amod* does not equal cut cells, anticipated to be a dominant format *Acell*⋅ *Ncells*, as some area is lost module output current and voltage, respectively. By using this due to cell spacing and edge spacing. The cell spacing for wafer- in the coming decade [1]. The width of thin- approach, the mismatch losses include deviations in the max- based and thin- film cells is set at imum power point voltage (*Vmpp*) and maximum power point

7.5 mm, based on Castriotta et al. [ film based modules are assumed to be 0.8 and 33], adjusted slightly to en- sure equal submodule areas. It should be realized that for both submodules
# 2 Terminal

## 3 Terminal

## 4 Terminal

**FIGURE 4** | The module interconnection of the different configurations. The blue and red diodes represent the perovskite and silicon subcells,

respectively. For the 3T configuration, two bottom cells and one top cell are not connected, representing the end-losses as they cannot contribute to the power generation.

**TABLE 1** | The geometry of the wafer-

based and thin- ***Acell*(*l* × *b*) *N***film-***cells Amod*(*l* × *b*) cell spacing edge spacing** based module. **Model type [ mm₂] [-] [ m₂] [ mm] [ mm]**

##### Wafer-based 210 × 105 3.285 0.8

##### Thin-film 2540 × 7.5 3.275 0.0

*Note:* The cell spacing of the thin-*kshaded*.

film modules is 0, as the dead area due to laser scribing is fully considered by

current density (*Jmpp*), but also account for the end- losses in 3T

|||oc|
|---|---|---|
|mpp|mpp||
|sc|oc mpp|mpp mpp|

devices.

##### 2.4 | The Modeling of Meta-

##### Stability

Perovskite cells experience a reversible efficiency change during light and dark cycles [42, 43], known as the so called *meta-stability effect*. This phenomenon, where efficiency ini- tially starts lower but improves with light exposure [44], has been incorporated into the PVMD Toolbox using the meth- odology from Remec et al. [43], which models an initial volt- age loss that recovers under illumination. It should be noted that this effect is distinct from degradation, which has an irreversible effect on the efficiency. The impact of including the Light Soaking (LS) effect is discussed in the Supporting Information.

##### 2.5 | The Simulation of Different Degradation Scenarios of Perovskite Subcells

Perovskite degradation behavior remains only partially under- stood, and there is insufficient long- term performance data for PS devices at the module level. Therefore, we use a similar ap- proach as Orooji and Paetzold [45], simulating different degra- dation scenarios in the perovskite cell. This way the focus is not on physical processes and specific degradation mechanisms that are occurring, but rather the impact of cell level degradation on the module performance. The simulated degradation is applied to the electrical simulation of the perovskite cell, leaving the op- tical and electrical performance of the silicon cell unchanged.

Figure 5 illustrates the degradation scenarios considered in this work. Performance losses are modeled as reductions in short-*Isc*), open-*Voc*), or fill factor (*FF*), circuit current ( with degradation level (*kdeg*circuit voltage () representing losses specific to the

|deg|||
|---|---|---|
|sc||mpp mpp|
|oc|mpp||

perovskite top cell. *I* degradation is simulated by reducing the current source, while *V* degradation is achieved by increas- ing the diode's saturation current (*I₀*) in the equivalent circuit

(Figure 3). *FF* degradation is modeled by increasing the diode's ideality factor, with *I₀* adjusted to maintain consistent *Voc*.

Figure 5 also shows the change in *J* and *V* (indicated with crosses). Whereas degradation in *I* and *V* only affects *J* and *Vmpp*, respectively, while keeping the other quantity con- stant, the degradation in *FF* equally affects the *J* and *V*. It should be realized that degradation in *FF* can also be achieved by adjusting the resistances of the equivalent circuit, potentially changing the trajectory of the MPP, and therefore, the results. In this work, we did not employ the latter approach to solely focus on the degradation of the perovskite subcells, rather than on the eventual degradation of the perovskite interconnections.

##### 2.6 | Validation for Outdoor PS Devices

As mentioned earlier, we extend previous validations to PS tandem cells under outdoor conditions. Remec et  al. at the Helmholtz- Zentrum Berlin (HZB)  [43] reported data for a

24.2%- efficiency tandem PS cell operating in Berlin over 330 days. We used the PVMD Toolbox to simulate this device's performance. It is important to note that the cell used for validation has a lower quality (24.2% STC efficiency) compared to the reference cell (32.5% STC efficiency) used in simulations. For the valida- tion cell, an additional parallel diode was included in the elec- trical characterization to simulate extra losses at the interfaces, as explained in our previous work [13]. However, for the simu- lations, we used the higher-
quality cell without the additional diode to more accurately represent the full potential of 2T, 3T,2, which is significantly smaller than the modules in the simulations. and 4T modules manufactured with state- of- Figure 6a, b, and c compare simulated and measured the- *P*, *J*, and *V*, respectively, for 10 selected days in the first five months art techniques. Additionally it should be noted that the reference cell has an of 2022. These days have been selected such that they represent area of 1 cm

##### Degradation I

||sc||oc||
|---|---|---|---|---|
|250||250||250|
|2||2||2|
|150||150||150|
|100||100||100|
|50||50||50|
|0||0||0|
|0|1|1.5 0|1|1.5 0|

]] 200 200

##### Current density [A/m Current density [A/m

0.5 0.5 Voltage [V] kdeg=0% kdeg=10%
**FIGURE 5** |

maximum power point of each IV curve is indicated with a 'x'.

##### Degradation FF

] 200

##### Current density [A/m

0.5 1 1.5
##### Voltage [V] Voltage [V]

##### kdeg=20% kdeg=30% kdeg=40%

*E* *g* of 1.62 eV is shown. The

##### Degradation V

The different degradation scenarios that are considered in this study. As example the perovskite with a

]

#### a) mSimulated Measured

[mW/c10 p mp P 0 12 01 2012 01 2012 01 2012 01 2012 000

b)2
#####] 20

10 [mA/cm p mp J 0 12 01 2012 01 2012 01 2012 01 2012 000

c)2]
5-Jan6-Jan1 1-Feb1 2-Feb1 4-Mar1 5-Mar1-Apr2-Apr1-May2-May

[V

1.5 p mp 1
V

0.5 12 01 2012 01 2012 01 2012 01 2012 000
##### Time [h]

**FIGURE 6** | The outdoor validation of a perovskite silicon cell in Berlin performed by HZB. a), b), and c) show the measured and simulated

*P* *mpp*, *Jmpp* and *Vmpp*, respectively, for 10 selected days in the first five months of the year. The RMSE between the measured and simulated output power in the first 137 days is 1.98 mW cm₂, and the weighted relative error is 12.2%.

different months, have a significant amount of irradiance, and Specifically, we simulate the module performance of 2T, 3T, the output power have been measured correctly. While *Pmpp*and 4T devices across a range of bandgap energies and geo- and *Jmpp* align closely, there are slight discrepancies in *Vmpp*, graphic locations. This section explains how the bandgap vari- likely due to temperature dependency differences between mea-ations are modeled and describes the characteristics of each surement and simulation (discussed further in the Supporting location. Information). Another parameter that could be varied for optimization is the Overall, the root mean square error (RMSE) between the sim-thickness of the perovskite layer, as it affects the current absorp- ulated and the measured output power of the first 137 days of tion in both cells. However, in previous work [13, 29] we found the experiment is 1.98 mW cm₂, and the power- that the bandgap energy has a stronger impact on the energy weighted relative yield than its thickness. The Supporting Information shows the error is 12.2%. This period was selected to avoid degradation be-energy yield of different configurations at different thicknesses, havior observed in the tandem cells later, as it could influence showing that the bandgap energy has a much bigger impact the outcome of the scenario based degradation modelling of this than the thickness. As another varying parameter would expo- paper by including an underlying specific degradation mode. nentially increase the number of simulations, the thickness of This shows that the PVMD Toolbox can be used to accurately perovskite has been kept fixed at 550 nm, being similar to the simulate the performance of perovskite silicon devices under reference cell of Mariotti et al. [30]. outdoor conditions.

It should be realized that the validation is only performed for 2T **3.1 | Varying the Bandgap Energy** devices. This is because, to the best of the authors knowledge, no publicly available data can be found that reports the outdoor The bandgap energy significantly influences both the optical and performance of 3T and 4T devices. In future work, the validation electrical performance of a device. In the optical simulations, of the PVMD Toolbox can be extended to other configurations *N*(*𝜆*) of the perovskite layer changes as a function of *Eg*. We use as well. the approach from our previous work  [46, 47] to predict *N*(*𝜆*) for all desired bandgap energies, based on measured data from **| Input for Case Studies** Manzoor et al. [48]. Since complete *N*(*𝜆*) data for the full *Eg* range is unavailable, we extrapolate from Manzoor's measurements to The methodology described in the previous section is applied cover our target bandgap range. This predicted *N*(*𝜆*) is then used to determine the optimal *Eg* for different operating conditions. in GenPro to simulate absorption profiles for each *Eg* value.

In the electrical modeling, *Eg* serves as a direct input to generate the IV curve of the perovskite cell. Our earlier studies [13, 29] demonstrated how changes in bandgap energy affect both the optical and electrical performance of a 2T PS cell. The effect of *Eg* on the cell JV curve and its circuit parameters can be found in the Supporting Information.

To illustrate the effect of *Eg* variation on the 2T, 3T, and 4T mod- ules, Figure  7 shows the power output at STC for each config- uration across different perovskite bandgap energies. Among the three, the 2T module exhibits the highest power at STC, fol- lowed by the 3T and then the 4T configurations. The optimal *Eg* is lower for the 2T configuration due to its current- matching requirements, while the 3T and 4T configurations have a similar *Eg*. A more detailed analysis of these differences is pre- sented in the next section. optimal

Köppen-Geiger-Photovoltaics (KGPV) classification [49, 50] and a machine learning based PV climate classification (ML- PV) [51]. Table 2 provides key characteristics of these locations. For each location, we consider a fixed tilt PV system with the module tilt specified in Table  2 with an inter- row spacing of 8 meters. Additionally, we obtain the hourly data of a typical mete- orological year (TMY) from Meteonorm [52].

Another characteristic of each location is the spectral irradia- tion and the average photon energy (APE). Figure 8 shows the annual spectral irradiance as received by the module in each location. The APE for each location is calculated by dividing the total irradiance over the total number of photons. Lagos and Shanghai have a higher APE than the other locations, implying a slight blue- shift for these locations. **4 | Results**

The outlined methodology is applied to simulate the energy yield (EY) of the 2T, 3T, and 4T modules under the described operating conditions. For each location, we evaluate the module performance across various perovskite bandgap energies from

1.50 to 2.00 eV, in increments of 0.02 eV. First, we identify the optimal *Eg* for each condition. Then, we compare configurations in detail by quantifying the different types of losses in the PV module. Finally, we assess robustness under different degrada-
##### 3.2 | Different Locations

To explore how optimal bandgap energy may vary across climates, we perform the bandgap optimization for several geographic locations. We selected four distinct locations, each representing a different climate type according to the

|2T 3T 4T||tion scenarios.||
|---|---|---|---|
|2T 3T 4T [eV] E 1.62 1.78 1.82 g,opt P [W/m2] 3032 99 294 STC|3.5 /nm] 3 2 2.5 2 1.5 1 0.5 Spectral Irradiance [kWh/m||Delft, APE = 1.47 eV Lagos, APE = 1.49 eV Lisbon, APE = 1.46 eV Shanghai, APE = 1.49 eV|
|1.5 1.6 1.7 1.8 1.9 2 E [eV] g | The perovskite bandgap optimization of the different The main TMY characteristics of the selected locations.|0 FIGURE 8|500 ||1000 1500 2000 2500 Wavelength [nm] The spectral irradiation received at each location and the corresponding APE. It can be seen that both Lagos and Shanghai have a slight blue shift compared to the other locations.|
|Annual global horizontal irradiation [kW h m₂]|Weighted average ambient temperature [°C]||Optimal KPGV ML-PV module tilt [°]|
|1018 1642 1758 1271|16.2 29.4 20.6 21.7||DL Tem1 31 AH Tro2 5 DH Tem5 28 DM Tro1 17|

320] 2 300

[W/m C 280 ST P 260

240 Module

**FIGURE 7**

modules under STC.

**TABLE 2** |

##### Location

Delft

Lagos

Lisbon

Shanghai

*Note:*

irradiation for each location in a free- horizon scenario.

side

The ambient temperature is weighted with the global horizontal irradiance. This metric is chosen as, in our opinion, it better represents the operating conditions of the PV modules than the simple time average of the ambient temperature. The selected module tilts are chosen such that they maximize the annual front-

**4.1 | Optimal Bandgap Energy** is less sensitive to bandgap variations, resulting in a flatter EY
curve. This is shown in the Supporting Information, where the Figure  9 presents the annual EY across different locations for JV curve of the perovskite subcell is shown for different band- each simulated bandgap energy, with dashed lines indicating gap energies. It can be seen that the *Jsc* changes more than the the optimal *Eg* at STC. The 2T configuration shows the high-*Voc*, explaining why the 3T configuration is less sensitive to est sensitivity to deviations from its optimal *Eg* because current bandgap changes than the 2T configuration. Since 4T modules matching is required between the top and bottom cells. In the 3T do not require matching between subcells, their EY curve is the configuration, voltage matching is necessary, but this matching flattest, showing the least sensitivity to bandgap deviations.

### Delft Lagos

||] 1500 1400 1300||
|---|---|---|
|2T||2T|
|3T|EY [kWh 1200|3T|
|4T 1.61 .8 2 E [eV] g Lisbon|1100] 1200 1100|4T 1.61 .8 2 E [eV] g Shanghai|
|2T|1000|2T|
|3T|EY [kWh|3T|
|4T 1.61 .8 2 E [eV] g E The optimal and corresponding annual EY for all operating conditions, expressed in [ eV]. g|900 The bandgap optimization under outdoor operating conditions for the various configurations. The dashed lines indicate the opti-|4T 1.61 .8 2 E [eV] g|
|2T||3T 4T|
|E EY g [ eV] [kWh]|E g [ eV]|EY E EY g [kWh] [ eV] [kWh]|
|1.62 — 1.62 1081 1.62 1507 1.62 1862 1.62 1227|1.78 1.80 1.80 1.80 1.80|— 1.82 — 1088 1.82 1076 1509 1.88 1499 1864 1.82 1844 1233 1.88 1225|

#### 1100

]

#### 1000

### EY [kWh

###] 1800

#### 1600

### EY [kWh

#### 1400

**FIGURE 9** |

mums at STC.

**TABLE 3** |

##### Operating conditions

STC

Delft

Lagos

Lisbon

Shanghai

*Note:* For 2T devices, the optimal bandgap is the same for all conditions, whereas the 3T configuration has a slightly lower *Eg* for STC. In 4T devices, the optimal

bandgap fluctuates the most.

Table 3 shows the optimal *Eg* and corresponding EY for each sce- nario. The optimal bandgap at STC (as dashed lines in Figure 9) is also a good predictor for optimal *Eg* under outdoor conditions. For both the 2T and 3T configurations, the optimal *Eg* is 1.62 eV and 1.80  eV, respectively, and is consistent across locations, though the 3T device has a slightly lower optimal bandgap at STC. Only the 4T configuration shows notable variations, with an optimal *Eg* of 1.82 eV in STC, Delft, and Lisbon, but 1.88 eV in Lagos and Shanghai. This difference arises due to a more blue- rich irradiance spectrum in Lagos and Shanghai (as indicated in Figure  8), where a higher bandgap reduces thermalization losses. It should be realized that this apparent significant shift is mostly due to the relative flat shape of the 4T performance, meaning that there is little difference in EY between the differ- ent bandgap energies.

As shown in Figure  9 and Table  3, energy yields at the opti- mal *Eg* are similar across configurations, with all differences within 1.5%. Nonetheless, the 3T module, despite its end- losses, achieves the highest EY across all locations.

##### 4.2 | Comparison in Losses

To better understand the difference in performance for the dif- ferent configurations, we analyze the various losses that are present. Using the approach described in earlier work  [7], all losses in the PV module are quantified. In this approach, 16 loss components are defined and grouped into four categories (fun- damental, optical, electrical, and system losses), such that the sum of all losses and the efficiency equals 100%. Figure 10 shows the losses of the optimized PV modules in Delft. Since the losses comparison among the configurations are found to be similar for all locations, only the results of Delft are presented in the main text. The results for the other locations are reported in the Supporting Information.

It should be realized that the differences in loss distributions are caused by the configurations having different optimal band- gap energies or the configurations deploying a different module

design. Figure 11 illustrates how some highlighted losses change with *Eg* for each configuration. The trend for all losses is pro- vided in the Supporting Information. In some plots, not all lines are visible as their values are very similar across configurations. In case only two lines overlap, additional legends are placed to indicate which lines correspond to which configuration. This figure can be used to explain the differences observed in Figure 10. We discuss the four categories separately and explain what causes the differences among the configurations.

**4.2.1** | **Differences in Fundamental Losses** The fundamental losses only depend on the fundamental prop- erties of the device, such as *Eg*. Therefore, these losses (as shown in Figure 11) only depend on the bandgap energy, but are similar among the configurations. The differences, visible in Figure 10, for this category are solely caused by the configurations having different bandgap energies. For example, the higher thermaliza- tion losses (19.7%) in the 2T configuration, compared to the 3T and 4T configurations (18.6%), are caused by its lower bandgap energ y.
**4.2.2** | **Differences in Optical Losses** In contrast to the fundamental losses, differences in optical losses are mostly caused by differences in module design. As the 2T and 3T have a similar module design, these configurations have similar optical losses, while the 4T module shows higher optical losses. The higher losses for the 4T module can be at- tributed to greater contact shading losses (due to a larger *kshaded* in thin- film modules), and more reflection losses, due to its less effective texture morphology and non-
optimal optical coupling layer between the top and bottom subcells.

On the contrary, however, the 4T module has lower cell- spacing losses, due to the lower cell spacing in thin- film modules, and lower parasitic absorption losses. The lower parasitic absorption in 4T modules can mainly attributed to the higher reflection

**FIGURE 10** |

plane irradiation on the module area.

The loss analysis for the 2T, 3T, and 4T modules operating in Delft. 16 loss components are grouped into four categories such that the sum of all losses and the efficiency equals 100%, which is equal to the in-

##### Thermalization Cell spacing

##### Contact shading Reflection

##### 4T 4T

] 3 [% 20 2T 3T

1.5
1 2T 3T 2 Loss 19 2T 3T 4T 18 1 0 1

1.61.8 2 E [eV] g
##### Parasitic absorption Cell interconnection

##### Mismatch

3 1 10] 3T 2T 2 0.5 5 Loss [% 4T

1 0 0

1.61.8 2 1.61.8 2
##### 1.61.8 2

E [eV] E [eV] E [eV] g g g 2T 3T 4T The value for the highlighted losses at different bandgap energies for all modules located in Delft. For each configuration, the op-

**FIGURE 11** |

timal bandgap energies in Delft are indicated with dotted lines. The titles in all figures indicate the losses category according to the color scheme in Figure 10. For some plots, not all configurations are visible, as the lines overlap due to similar values. In case only 2 lines overlap, additional legend are provided to identify the curves.

values, as shown by the absorption profiles which can be found in the Supporting Information.

**4.2.3** | **Differences in Electrical Losses** As shown in Figure  10 and Figure  11, the electrical losses are very similar for the different configurations. This is because the electrical losses account for all losses introduced by the compo- nents of the equivalent circuit, combining both recombination and resistive losses within the cell. Losses caused by differences in layer stacks and cell interconnections are instead captured by the optical and system losses, respectively. The electrical parame- ters are derived from the same equivalent circuit model, meaning that design variations among configurations have little impact on electrical losses. The only minor differences observed are primar- ily due to the modules operating at different bandgap energies.
**4.2.4** | **Differences in System Losses** Lastly, there are variations in the cell interconnection and mis- match losses. Interconnection losses are the highest in 4T due to *Rcon*,*tf* being larger than *Rcon*,*met*. The 3T device experiences more interconnection losses than the 2T configuration due to added rear- side contact resistance. Mismatch losses in the 2T and 3T modules significantly depend *Eg* (Figure 11, bottom right), as it affects current and voltage matching, respectively, explaining why the optimal on *Eg* closely aligns with the values that minimize mismatch losses. The 4T device, requiring no current or voltage matching, has the lowest mismatch losses. The small, but non-
zero, mismatch losses are caused by the fact that the contact resistance slightly influences the operating point of the cells.

##### 4.3 | Robustness Against Degradation

Lastly, we examine the robustness of each configuration against each degradation scenario. As mentioned before, this compar- ison has already been made for 2T and 4T devices in litera- ture  [22], but to the best of the authors' knowledge not for 3T devices.

For all scenario's described in Section 2.5, we rerun annual EY simulations on the optimized modules at different *kdeg* values.

Figure  12 shows the degradation impact on annual EY for the PV modules in Delft, with results for other locations available in the Supporting Information. For comparison, the energy yield of a single- junction module (Module STC efficiency of 20.4%) com- posed solely of silicon heterojunction (SHJ) cells is represented by a dashed line. These SHJ cells are based on the bottom cell of the considered PS tandem cell and it is assumed that they have no degradation.

In all scenarios, the energy yield of the undegraded tandem *kdeg*= 0), as the config- urations have similar efficiencies in Figure modules are approximately similar (see 10. This similarity will remain for values of *kdeg* up to around 10%. However, these energy yields will differ for larger values of *kdeg*, depending on the type of degradation. When degradation affects *Isc*, the 2T configuration shows the largest EY drop due to its current- matching requirement. For *Voc* degradation, the 3T configura- tion is most affected, due to its voltage- *FF* degradation, the 2T and 3T configurations are sim matching requirement.- ilarly affected, as losses in Under *FF* cause both losses in *Jmpp* and *Vmpp*. Overall, the 4T configuration proves least vulnerable to perovskite cell degradation in all scenarios, as its top and bottom subcells operate independently. This independence makes the 4T module the most robust against degradation.

##### Degradation Voc

##### Degradation Isc

##### Degradation FF

|EY SHJ|1200 1100] 1000 900 800 700 Energy yield [kWh 600|EY SHJ|1200 1100] 1000 900 800 700 Energy yield [kWh 600|EY SHJ|
|---|---|---|---|---|
|01 02 03 04 kdeg perovskite [%] | Si module. For all scenarios, the tandem modules outperform the SHJ for k up to 30%. deg It should be realized, however, that the actual degradation rate of perovskite can be different for different bandgap ener- gies. As higher bandgap perovskites tend to be less stable [53], it is possible that 3T or 4T modules reach faster high values than 2T modules. This aspect should be kept in mind when comparing the degradation robustness of the different|500 0|01 02 03 04 kdeg perovskite [%] 2T 3T 4T The energy yield for all modules in Delft after different degradation scenarios. The dashed line indicates the energy yield for a single modules for values of|500 0 k deg|01 02 03 04 kdeg perovskite [%] Finally, we quantify the degradation resilience of each config- uration by simulating various degradation scenarios, being a relevant aspect to consider when comparing the configurations. Results show that 2T and 3T modules are most sensitive to cur- rent and voltage losses, respectively. Across all scenarios, the 4T configuration proves instead to be the most robust against degradation. Overall, the tandems outperform single junction up to 30%.|

1100] 1000

700 Energy yield [kWh 600

500 0

**FIGURE 12**

junction c-

values of

of *kdeg*

configurations.

##### 5 | Conclusion

The perovskite/silicon technology is a promising candidate to further improve the efficiency of PV modules, that can come in different configurations. This study compares the outdoor per- formance of 2T, 3T, and 4T devices at the module level, consid- ering cell- to- module losses that have not been addressed before. Using the PVMD Toolbox, the performance of a 2T PS device under outdoor conditions is validated. Then, we simulate the energy yield of each configuration across various geographical locations, identifying the optimal bandgap energies for 2T, 3T, *E* *g* across and 4T modules of 1.62, 1.80, and 1.82 eV, respectively. Only for locations. the 4T module there are small variations in optimal To understand the difference among the configurations, we quantify the various energy losses of all optimized modules. Additionally, the trends for all losses with respect to *Eg* are calculated. This shows that the differences in losses can be caused by different configuration designs (interconnection losses) or different optimal *Eg* (thermalization losses). The mismatch losses are the most sensitive to changes in bandgap energy, meaning they play an important role for determining the optimal *Eg*. Overall, all optimized configurations have similar energy yields (all differences within 1.5%) across all locations.

**Acknowledgments**

During the preparation of this work the author used ChatGPT in order to paraphrase sentences and improve the language and readability. After using this tool/service, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication.

**References**

1. VDMA, “International Technology Roadmap for Photovoltaics (ITRPV),” 2024.
2. 35 solar cells. 2025.
3. A. Richter, M. Hermle, and S. W. Glunz, “Reassessment of the Limit- ing Efficiency for Crystalline Silicon Solar Cells,” *IEEE Journal of Pho-* *tovoltaics* 3, no. 4 (2013): 1184–1191.
4. S. Schafer and R. Brendel, “Accurate Calculation of the Absorptance Enhances Efficiency Limit of Crystalline Silicon Solar Cells With Lam- bertian Light Trapping,” *IEEE Journal of Photovoltaics* 8, no. 4 (2018): 1156–1158.
5. O. Er- raji, C. Messmer, A. J. Bett, et  al., “Loss Analysis of Fully- Extured Perovskite Silicon Tandem Solar Cells, Characterization Meth- ods and Simulation Toward the Practical Efficiency Potential,” *Solar* *RRL* 7, no. 24 (2023): 2300659.
6. A. D. Vos, “Detailed Balance Limit of the Efficiency of Tandem Solar Cells,” *Journal of Physics D, Applied Physics* 13, no. 5 (1980): 839–846.
7. Y. Blom, M. R. Vogt, C. M. Ruiz Tobon, R. Santbergen, M. Zeman, and O. Isabella, “Energy Loss Analysis of Two-
Terminal Tandem PV

8. “34.85%! LONGi Breaks World Record for Crystalline Silicon- Systems Under Realistic Operating Conditions Revealing the Impor- tance of Fill Factor Gains,” *Solar RRL* 7, no. 8 (2023): 2200579. Perovskite Tandem Solar Cell Efficiency Again,” [https://www.longi](https://www.longi). com/en/news/silicon-perovskite-tandem-solar-cells-new-world-effic ienc y/, 2025. accessed on 2025-11-05.
9. K. Alberi, J. J. Berry, J. J. Cordell, et al., “A Roadmap for Tandem Pho- tovoltaics,” *Joule* 8, no. 3 (2024): 658–692.
10. S. Akhil, S. Akash, A. Pasha, et al., “Review on Perovskite Silicon Tandem Solar Cells, Status and Prospects 2T, 3T and 4T for Real World Conditions,” *Materials & Design* 211 (2021): 110138.
11. Y. Shi, J. J. Berry, and F. Zhang, “Perovskite/Silicon Tandem Solar Cells,” *Insights and Outlooks. ACS Energy Letters* 9, no. 3 (2024): 1305–1330.
12. E. Raza and Z. Ahmad, “Review on two- Terminal Crystalline-
Silicon/Perovskite Tandem Solar Cells, Prog- ress, Challenges, and Future Perspectives,” *Energy Reports* 8 (2022): 5820–5851.

13. Y. Blom, M. R. Vogt, H. Uzu, et al., “Exploring the Potential of Per- ovskite/Perovskite/Silicon Triple-
Junction Pv Modules in Two- and Four-Terminal Configuration,” *Solar RRL* 9, no. 5 (2025): 2400613.

14. F. Fu, J. Li, T. C. J. Yang, et al., “Monolithic Perovskite-
Silicon Tan- dem Solar Cells, From the Lab to Fab?,” *Advanced Materials* 34, no. 24 (2022): 2106540.

15. X. Luo, H. Luo, H. Li, et  al., “Efficient Perovskite/Silicon Tandem Solar Cells on Industrially Compatible Textured Silicon,” *Advanced Ma-* *terials* 35, no. 9 (2023): 2207883.
16. R. Santbergen, H. Uzu, K. Yamamoto, and M. Zeman, “Optimization of Three- Terminal Perovskite/Silicon Tandem Solar Cells,” *IEEE Jour-* *nal of Photovoltaics* 9, no. 2 (2019): 446–451.
17. E. L. Warren, W. E. McMahon, M. Rienäcker, et  al., “A Taxonomy for Three- Terminal Tandem Solar Cells,” *ACS Energy Letters* 5, no. 4 (2020): 1233–1242.
18. G. Giliberti, F. Di Giacomo, and F. Cappelluti, “Three Terminal Per- ovskite/Silicon Solar Cell With Bipolar Transistor Architecture,” *Ener-* *gies* 15, no. 21 (2022): 8146.
19. H. Schulte-
Huxel, R. Witteck, S. Blankemeyer, and M. Köntges, “Optimal Interconnection of Three- Terminal Tandem Solar Cells,” *Progress in Photovoltaics, Research and Applications* 31, no. 12 (2023): 1350–1359.

20. M. Hull, J. Rousset, V. S. Nguyen, P. P. Grand, and L. Oberbeck, “Pro- spective Techno-
Economic Analysis of 4T and 2T Perovskite on Silicon Tandem Photovoltaic Modules at GW- Scale Production,” *Solar RRL* 7, no. 23 (2023): 2300503.

21. Y. Zhao, R Santberge, D Zhang, et  al., “Optical Design Strategies for High- Efficiency Monofacial and Bifacial Four-
Terminal Perovskite- Silicon Tandem Modules,” In, 2023.

22. J. Qian, M. Ernst, N. Wu, and A. Blakers, “Impact of Perovskite Solar Cell Degradation on the Lifetime Energy Yield and Economic Viability of Perovskite/Silicon Tandem Modules,” *Sustainable Energy & Fuels* 3, no. 6 (2019): 1439–1447.
23. M. H. Futscher and B. Ehrler, “Efficiency Limit of Perovskite/Si Tan- *Progress in Photovoltaics: Research and Applications,* dem Solar Cells,” *ACS Energy Letters* 1, no. 4 (2016): 863–868.
24. F. Gota, M. Langenhorst, R. Schmager, J. Lehr, and U. W. Paetzold, “Energy Yield Advantages of Three-
26. M. Singh, R. Santbergen, I. Syifai, A. Weeber, M. Zeman, and O. Isa- bella, “Comparing Optical Performance of a Wide Range of Perovskite/ Silicon Tandem Architectures Under Real-
World Conditions,” *Nano* 10, no. 8 (2020): 2043–2057.

27. M. Kikelj, L. L. Senaud, J. Geissbühler, et al., “Do All Good Things Really Come in Threes? The True Potential of 3-
Terminal Perovskite- Silicon Tandem Solar Cell Strings,” *Joule* 8, no. 3 (2024): 852–871.

28. M. Vogt, C. R. Tobon, A. Alcañiz, et al., “Introducing a Comprehen- sive Physics- Based Modelling Framework for Tandem and Other PV Systems,” *Solar Energy Materials and Solar Cells* 247 (2022): 111944.
29. Y. Blom, M. R. Vogt, O. Isabella, and R. Santbergen, “Optimization of
2, F Conductive Glass by Indonesian Local Stannic Chloride Precursors,” the Perovskite Cell in a Bifacial Two- *IOP Conference Series, Materials Science* *and Engineering* 541, no. 1 (2019): 012022. Terminal Perovskite/Silicon Tan- dem Module,” *Solar Energy Materials and Solar Cells* 282 (2025): 113431.

35. S. M. Kim, S. J. Park, H. H. Yoon, H. W. Choi, and K. H. Kim,
30. S. Mariotti, E. Köhnen, F. Scheler, et  al., “Interface Engineering “Preparation of ITO and IZO Thin Films by Using Facing Target Sput- tering (FTS) Method,” for High-
*Journal of the Korean Physical Society* 55, no. 5(1) (2009): 1996–2001. Performance, Triple- Halide Perovskite Silicon Tandem Solar

36. Cells,” K. Sato, Y. Goto, Y. Wakayama, Y. Hayashi, K. Adachi, H. Nishimura., *Science* 381, no. 6653 (2023): 63–69. “Highly Textured SnO, F TCO films for a-
31. R. Santbergen, T. Meguro, T. Suezaki, G. Koizumi, K. Yamamoto,2
Si Solar Cells,” 1993. and M. Zeman, “GenPro4 Optical Model for Solar Cell Simulation and

37. Its Application to Multijunction Solar Cells,” A. Rehman, E. P. Van Kerschaver, E. Aydin, W. Raja, T. G. Allen, *IEEE Journal of Photovol-* and S. De Wolf, “Electrode Metallization for Scaled Perovskite/Silicon *taics* 7, no. 3 (2017): 919–926. Tandem Solar Cells, Challenges and Opportunities,”
32. R. Siegel, “Net Radiation Method for Transmission Through Par
*Progress in Photo-* - *voltaics, Research and Applications* tially Transparent Plates,” *Solar Energy* 31, no. 4 (2023): 429–442. 15, no. 3 (1973): 273–276.

38.
33. L. A. Castriotta, M. Zendehdel, N. Yaghoobi Nia, et al., “Reducing
R. Witteck, H. Schulte-
Losses in Perovskite Large Area Solar Technology, Laser Design Opti Huxel, H. Holst, et al., “Optimizing the Solar-Cell Front Side Metallization and the Cell Interconnection for High mization for Highly Efficient Modules and Minipanels,” *Advanced En-* Module Power Output,” *ergy Materials* 12, no. 12 (2022): 2103420. *Energy Procedia* 92 (2016): 531–539.

39. M. Zeman, J. Heuvel van den, M. Kroon, et al., *Advanced Semicon-* *ductor Analysis*
34. T. Arini, L. H. Lalasari, F. Firdiyono, et al., “The Effect of Deposition
. tech. rep. (Delft University of Technology, 2019). Times on Preparation of SnO

40. T. Jung, H. Song, H. Ahn, and G. Kang, “A Mathematical Model for Cell- to- Module Conversion Considering Mismatching Solar Cells and the Resistance of the Interconnection Ribbon,” *Solar Energy* 103 (2014): 253–262.
41. W. McMahon, H. Schulte-
Huxel, J. Buencuerpo, et al., “Homogenous Voltage- Matched Strings Using Three- Terminal Tandem Solar Cells, Fundamentals and End Losses,” *IEEE Journal of Photovoltaics* 11, no. 4 (2021): 1078–1086.

42. M. V. Khenkin, K. M. Anoop, I. Visoly-
Fisher, et al., “Reconsidering Figures of Merit for Performance and Stability of Perovskite Photovolta- ics,” *Energy & Environmental Science* 11 (2018): 739–743.

43. M. Remec, Š. Tomšič, and M. Khenkin, “From Sunrise to Sunset, Unraveling Metastability in Perovskite Solar Cells by Coupled Outdoor Testing and Energy Yield Modelling,” *Advanced Energy Materials* 14,
Terminal and Four-

44. C. Zhao, B. Chen, X. Qiao, L. Luan, K. Lu, and B. Hu, “Revealing Underlying Processes Involved in Light Soaking Effects and Hysteresis Phenomena in Perovskite Solar Cells,” *Advanced Energy Materials* 5, no. 14 (2015): 1500279.
45. S. Orooji and U. W. Paetzold, “Energy Yield Modeling of Perovskite Silicon Tandem Photovoltaics, Degradation and Total Lifetime Energy Yield,” *Energy Technology* 12, no. 11 (2024): 2400998.
46. Y. Blom, M. Ruben Vogt, O. Isabella, and R. Santbergen, “Method for Bandgap Interpolation of Perovskites Spectral Complex Refractive Index,” *Optics Express* 32, no. 3 (2024): 4365.
47. Y. Blom, “YBlom1999/InterpolationNK-
YB, Final,” 2024.

48. S. Manzoor, J. Häusele, K. A. Bush, et  al., “Optical Modeling of Wide- Bandgap Perovskite and Perovskite/Silicon Tandem Solar Cells Using Complex Refractive Indices for Arbitrary-
Bandgap Perovskite Absorbers,” *Optics Express* 26, no. 21 (2018): 27441.

49. M. Kottek, J. Grieser, C. Beck, B. Rudolf, and F. Rubel, “World Map of the Köppen-
Geiger Climate Classification Updated,” *Meteorologische* *Zeitschrif* 15, no. 3 (2006): 259–263.

50. J. Ascencio-
Vásquez, K. Brecl, and M. Topič, “Methodology of Köppen- Geiger- Photovoltaic Climate Classification and Implications to Worldwide Mapping of PV System Performance,” *Solar Energy* 191 (2019): 672–685.

51. F. J. T. de las Heras, O. Isabella, M. R. Vogt, “A Machine Learning Approach to PV-
A Machine Learning Approach to PV,” 2024.

52. J. Remund, S. Müller, M. Schmutz, P. Graf. “Meteonorm Version
7.2,” METEOTEST (www. meteotest. com), 2020.
53. K. Hossain, S. Nayak, and D. Kabra, “Challenges and Opportunities in High Efficiency Scalable and Stable Perovskite Solar Cells,” *Applied* *Physics Letters* 125, no. 17 (2024): 170501. **Supporting Information** Additional supporting information can be found online in the Supporting Information section. Comparison_2T_3T_4T_PiP_Supporting_ Information.pdf. Optimal_STC.csv. Optimal_EY_Shanghai.csv. Optimal_EY_Lisbon.csv. Optimal_EY_Lagos.csv. Optimal_EY_Delft. csv. Losses_4T_Delft.csv. Losses_3T_Delft.csv. Losses_2T_Delft.csv.
