### <u>RESEARCH ARTICLE</u>

www.entechnol.de

# Energy Yield Modeling of Perovskite–Silicon Tandem Photovoltaics: Degradation and Total Lifetime Energy Yield

## Seyedamir Orooji and Ulrich W. Paetzold*

[2–11]

|fabrication process.||Perovskite–silicon||
|---|---|---|---|
|tandem|photovoltaics|(PV) have|gained|
|attention|by their|remarkable|efficiency|
|improvements|in|past years|and their|
|potential|for even|higher efficiency.||
|Combining|perovskite|and|silicon is|
|suitable|due to|their complementary||
|properties:|the well-known|durability|of|
|silicon properties of perovskite solar cells ensure|solar cells and|the optoelectronic||
|consistent|performance.|However,|the|
|integration|of perovskite|materials|with|

This study investigates the impact of degradation in perovskite-silicon tandem solar cells by means of energy yield (EY) modelling over the entire lifetime. First, we assess the impact on EY of degradation in the individual solar cell[12] parametersoftheperovskitetopcell.Our analysis reveals that degradation in fill factor, due to a decline in perovskite top cell shunt resistance (RSh), has the most severe impact on the EY, emphasizing the imperative to rectify perovskite imperfections in thin film processing causing RSh decline. Second, we investigate implications of degradation in the perovskite top cell on the EY of current mismatched tandem solar cells. Third, we examine critical thresholds for the “acceptable degradation levels” in the perovskite top cell with regard to silicon PV introduces new challenges, partic- degradationineachsolarcellparameter, assuming that the total loss in EY ularly concerning the long-term stability of must be comparable to the degradation in state-of-the-art silicon. Overall, our the perovskite solar cells. Silicon solar cells study highlights that degradation of the perovskite top cell needs to be assessed have undergone extensive development and optimization over the past decades, resulting with care when extrapolating the impact on the lifetime EY of perovskite-silicon tandem solar cells. The severity of degradation for different degradation [13–20] mechanisms in a single junction perovskite solar cell cannot be translated bility of perovskite PV, their economic one-to-one to tandem devices.

#### 1. Introduction

Tandem solar cells bear the potential to overcome the practical power conversion efficiency (PCE) limit of crystalline silicon [1] (c-Si) single-junction (SJ) solar cells around 29%. Perovskite semiconductors are excellent candidates for top cells in combi- nation with c-Si in tandem solar cells due to their outstanding optoelectronic properties, tunable bandgap, and inexpensive

S. Orooji, U. W. Paetzold Institute of Microstructure Technology Karlsruhe Institute of Technology, Hermann-von-Helmholtz-Platz 1 76344 Eggenstein-Leopoldshafen, Germany E-mail: ulrich.paetzold@kit.edu
S. Orooji, U. W. Paetzold Light Technology Institute Karlsruhe Institute of Technology 76131 Engesserstrasse 13, Karlsruhe, Germany The ORCID identification number(s) for the author(s) of this article can be found under [https://doi.org/10.1002/ente.202400998](https://doi.org/10.1002/ente.202400998). © 2024 The Author(s). Energy Technology published by Wiley-VCH
in highly stable and efficient solar cells in the market. In contrast, due to yet limited dura-

breakthrough is only expected several years from now. Although significant efforts have been made to improve the stability of perovskites, the highest durability of perov- skite solar cells yet lags the durability of silicon solar modules [21,22] on the market by around one to two orders of magnitude. The most critical stress factors for degradation in perovskite solar cells are light, temperature, oxygen, moisture, and voltage. [23–27] While advanced encapsulation concepts omit the degradation due to oxygen and moisture ingress, the intrinsic stress of perovskite solar cells under operation due to light, tem- perature, and voltage yet cannot be omitted. [28] More understand- ing of perovskite degradation mechanisms is required to identify suitable methods to counteract these degradation mechanisms and improve stability. [29,30]

To date, research on perovskite solar cell stability mostly focuses on degradation effects determined and characterized [31,32] under standard test conditions (STC). While these analyses provide a very valuable understanding of fundamental degrada- tion mechanisms and highlight the relevance of perovskite thin film morphology, composition, or additives for enhanced dura- bility, the long-term stability of a tandem solar cell needs to be quantified considering real-world conditions. However, to date, real-world variations in irradiation spectra, temperature profiles, and angle of incidence are mostly disregarded when assessing

|© 2024|The Author(s).|Energy Technology|published|by Wiley-VCH||
|---|---|---|---|---|---|
|GmbH. This is an open access article under the terms of the Creative||||||
|Commons|Attribution-NonCommercial||License, which|permits use,||
|distribution work is properly cited and is not used for commercial purposes.|and reproduction|in any|medium, provided|the original|[33–35]|

and predicting degradation in perovskite–silicon tandem solar cells. Moreover, key performance metrics like the levelized cost of electricity or the energy payback time require reliable model- ing of the lifetime energy yield (EY) of perovskite–silicon tandem solar cells factoring in degradation.

© 2024 The Author(s). Energy Technology published by Wiley-VCH GmbH

##### DOI: 10.1002/ente.202400998

Energy Technol. 2024, 12, 2400998 2400998 (1 of 12)

21944296, 2024, 11, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/ente.202400998](https://onlinelibrary.wiley.com/doi/10.1002/ente.202400998) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

This study investigates the EY of perovskite–silicon tandem solar cell undergoing degradation in the perovskite top cell using an advanced EY modeling software named EYCalc. [36] While a recent study [37] has also examined degradation in the context of EY, this article takes a different approach to study degradation. In this study, we aim to determine how degradation in individual solar cell parameters (i.e., open-circuit voltage (VOC), short-circuit current density (JSC), and fill factor (FF)) affect the EY of perovskite–silicon tandem solar cell. In the first section, we recapitulate the effect of degradation in the individual solar cell parameter of the perovskite and silicon subcells on the solar cell performance under STC. In the second section, we build the analysis of the EY on the understanding of impact of the degradation of individual solar cell parameters on the perovskite/silicon tandem solar cell but consider realistic irradiation conditions. First, we compare the EY of perovskite– silicon tandem solar cell that exhibits degradation in individual solar cell parameters. Our analysis reveals that degradation of individual solar cell parameters results in diverse performance loss characteristics of tandem solar cells. We study degradation in individual solar cell parameters but at the level of diode param- eters, i.e., the dark saturation current density (J₀), the collection efficiency (CE), the series resistance (RS), or the shunt resistance (RSh). Although real degradation mechanisms affect multiple parameters simultaneously, we analyze the effect of each diode parameter on the tandem solar cell EY separately. This is because the simultaneous change of multiple parameters makes it diffi- cult to understand the specific impact of each individual diode parameter. To ensure the robustness of our results, we evaluate the EY of tandem solar cells across various climate zones (i.e., Phoenix (arid/desert), Seattle (temperate), and Honolulu (tropical/humid areas), see Figure SI 1 and SI 2). Next, we explore the effects of perovskite top cell degradation on the EY of mismatched tandem solar cells. This analysis aims to determine which current-mismatch scenario provides the highest EY over the entire lifetime (i.e., 30 years). This approach helps to optimize the balance between the current of perovskite top cell and the silicon bottom cell, allowing for an understand- ing of which device architecture (current-matching scenario) is optimum based on the total lifetime EY considering degradation. Finally, we examine critical thresholds for the “acceptable levels of degradation” in the perovskite top cell regarding degradation in each solar cell parameter. Our analysis aims to determine the maximum acceptable degradation such that the total EY loss over the entire lifetime of the tandem solar cell remains comparable to the degradation levels observed in state-of-the-art silicon PV (i.e., a maximum of 0.5% per year). This study is implemented at the level of diode parameters due to the lack of clarity regarding the impact of real degradation mechanisms on diode parameters. Once a definitive interrelation between degradation mechanisms and variations in diode parameters has been established by the field, our EY modeling framework (EYCalc) will be capable of making predictions concerning specific degradation mechanisms. This study is intended to be universally applicable to all types of perovskite solar cells. Therefore, specific material characteristics are not considered, and our focus is solely on the bandgap of the materials.

#### 2. Experimental Section

This study computes the EY of perovskite–silicon tandem solar cells factoring in degradation using our in-house developed EY modeling platform, EYCalc. The software is published as an open-source software project. [34] A comprehensive description of the software is provided by Schmager et al. [34] It consists of four modules: the irradiance module, the optics module, the elec- trical module, and the EY module. The irradiance module com- putes, based on data from the typical meteorological year (TMY3) [38] for various locations in the USA, the direct and diffuse irradiance spectra for each hour of the year. It feeds the meteo- rological data of the TMY3 dataset into the simplified model of atmospheric radiative transfer of sunshine [39] to compute the clear sky irradiance. Further, a basic cloud model is used to account for the weather. The optics module employs the transfer- matrix method to evaluate thin layers that are optically coherent and utilizes a series expansion based on the Beer–Lambert law for the analysis of thick layers that are optically incoherent. This approach allows for the calculation of reflectance, transmittance, and absorptance that are resolved both spectrally and angularly for each layer within the stack. Additionally, the optics module is capable of simulating stacks that include textured interfaces through the use of geometrical [40] ray-tracing, as documented by Baker–Finch and McIntosh. The electrical module determines the temperature-dependent current density–voltage ( J–V) characteristics of the perovskite– silicon tandem solar cell. In this study, we expanded the electrical module to account for degradation in the solar cell parameters VOC, JSC, and FF of the perovskite–silicon tandem solar cell. The degradation is implemented at the level of the diode param- eters (i.e., the dark saturation current density (J₀), the CE, the series resistance (RS), or the shunt resistance (RSh)), which relate back to the solar cell parameters (see Figure 1). The numerical calculations [41] are performed by a coupled two-diode model in LTspice. Finally, the core EY module calculates the EY of perovskite–silicon tandem solar cells over the entire lifetime con- sidering the solar module orientation (rotation and/or tilt of the module) and location. Thereby, we calculate the EY of perovskite– silicon tandem solar cells for up to 30 years, factoring in different degradation scenarios to assess the long-term impact on the EY. We examined the aggregated EY over 30 years across different climatic locations to further assess the degradation effects. Temperature effects are intrinsically considered, using the nomi- nal operating cell temperature (NOCT) model. [42] In our model, we assumed a NOCT of 48 °C and extracted the insolation on the cell and ambient air temperature from TMY3 data. The architecture of the reference cell used in this study, as well as the corresponding experimental and simulated electrical and optical values are shown in Figure SI 3.

#### 3. Results and Discussions

This study analyzes the EY of perovskite–silicon tandem solar cells undergoing degradation in the perovskite top cell. This study aims to reveal the extent to which degradation in the solar cell parameters (VOC, JSC, and FF) impacts the overall EY. Currently, there is no clear understanding of how the real

Figure 1. Relationship between solar diode parameters and solar cell parameters, including the widely recognized degradation mechanisms. Thick gray

arrows indicate significant impact, while the thin gray arrows highlight less prominent effects.

degradation mechanisms affect the diode parameters (i.e., J₀, CE, RS, and RShÞ. Therefore, we implement this study at the level of diode parameters. Once the field establishes clear interrelation of specific degradation mechanism and the variation in diode parameters, our EY framework (EYCalc) will be able to perform this study and make predictions with regard to the specific degradation mechanisms. However, this study establishes a foundation for the future studies in the field of degradation with regard to the EY.

Figure 1 illustrates the correlation between the diode param-

eters and the solar cell parameters to identify how specific changes in diode parameters affect key solar cell parameters. While the exact interdependences between these parameters are complex, we can observe specific trends: the decrease in J₀ predominantly affects the VOC, the CE impacts mostly the J SC, and degradation in FF is at foremost attributed to an incre- ment in RSand decline in Rsh(see Figure 1). In the following, we revisit the interrelation of prominent degradation mechanisms described in the literature and degradation in solar cell param- eters. a) Degradation of current generation in the perovskite top cell: Degradation of current generation in perovskite solar cells is effectively described by a reduction in CE that linearly correlates to the JSC. A prominent degradation mechanism attributed to a reduction in CE is halide phase segregation. Halide phase seg- regation forms localized domains with higher concentration of halide ions, leading to trapping the charge carriers and a decrease in CE. [43–45]

b) Degradation of FF in the perovskite top cell:
Degradation of FF in perovskite solar cells is well described by a reduction in RShor an increment in RS. A decrease in RShis a common problem in imperfect perovskite solar cells that can be associated, for example, with the presence of pin holes or defects in the thin film morphology that result in shunts between the top and rear electrode. Other examples of mechanisms result- ing in a decrease in RShare 1) the diffusion of hole transport layer dopants into the perovskite layer or 2) interdiffusion of metal and halide ions between the perovskite layer and the metal contact. [46–48] A prominent degradation mechanism associated with increment in RSis ion migration. Due to the accumulation

of halide ions in the vicinity of the charge transport layers, ion migration induces an effective barrier for the charge extraction and leads to a higher RS. [49] Another example of increased RSis the degradation of transparent and conducting electrodes. [50]

c) Degradation in voltage of the perovskite top cell: Degradation of VOCin perovskite solar cells is perfectly described by an increase in J₀. Nonradiative charge carrier recombination at the surface, in the bulk, and at grain boundaries results in a high leakage current from grain boundaries, which raises J₀. In the first part of our study, we revisit the effect of degrada- tion of individual solar cell parameters in perovskite top and sili- con bottom cells (i.e., VOC, JSC, and FF) on the performance of tandem solar cell under STC. In the second next section, we proj- ect the EY of perovskite–silicon tandem solar cells undergoing various degradation scenarios. A schematic overview of the EY modeling factoring in degradation is shown in Figure 2.We highlight that the degradation is discussed with regard to solar cell parameters (i.e., VOC, JSC, and FF), but implement the deg- radation at the level of the diode parameters, i.e., J₀, CE, RS, and RSh. It should be noted that when analyzing the impact of deg- radation on a specific solar cell parameter due to a variation in the interrelated diode parameter, the remaining diode parameters remain unchanged. For instance, when analyzing JSCdegrada- tion through a decline in CE, the other diode parameters (J₀, RS, and RSh) remain constant. By analyzing the effect of each parameter separately, we can better understand how changes in individual diode parameters affect the lifetime EY of perovskite/ silicon tandem solar cells that undergo degradation. Although real degradation mechanisms affect many parameters at once, our method helps to see the specific impacts of each individual parameter on the overall EY. This approach prevents confusion that could arise from changing multiple parameters at the same time, which can hide the true relationships.
3.1. Performance Under STC Factoring in Degradation In this section, we examine how degradation effects the perfor- mance of perovskite–silicon tandem solar cell under STC. The

Figure 2. The methodology used for this study, including 1) type of degradation, 2) modeling time-resolved EY for every hour of the 30 year lifetime, and

3) analyzing the effect of degradation on tandem solar cell EY by computing aggregated EY over 30 years in different climatic conditions. degradation is discussed for the individual solar cell parameters (VOC, JSC, and FF) and implemented at the level of the diode parameters. We recapitulate that degradation in individual solar cell parameters has diverse effects on tandem solar cell perfor- mance. a) First, we investigate the degradation in VOCdue to an increment in J₀ for each subcell. We reiterate that the superpo- sition of VOCin the subcells is maintained for tandem solar cells regardless of variations in J₀ in the subcells (see Figure SI 4). This superposition also holds true for the tandem solar cell effi- ciency (see Figure 3). Furthermore, we demonstrate that the overall effect of variation in subcells J₀ on tandem solar cell VOCscales with the relative contribution to the VOCof the sub- cells (≈14% and ≈8% drop in VOCof the tandem solar cell for a 20% degradation in the VOCof the perovskite top and silicon bot- tom cells, respectively (see Figure SI 4)). b) Second, we discuss the performance of tandem solar cell undergoing degradation in FF (due to an increment in RSor decline in RSh) in the perovskite
top cell. Our findings reveal a pronounced superlinear degrada- tion in FF and PCE of the tandem solar cell for decreased RSh(see

Figure 4). Conversely, increment in RSof the perovskite top cell

shows a linear relationship with the FF and PCE of the tandem solar cells (see Figure SI 4). However, we note that the correlation shown in Figure 4 is more complex for mismatched perovskite/Si tandem solar cells. As reported in the literature, [51] FF increases for slightly mis- matched tandem solar cells. The extent of this effect correlates with the RShof the current-limiting subcell. Reduced RShof either subcells provides an alternative current path for matching the top and bottom cell currents, which affects the overall tandem solar cell JSCand FF. In Figure 5, we discuss the impact of cur- rent mismatch on tandem solar cell FF. We indicate our result for different levels of current mismatch ( 4mAcm) and different values for the RShof the perovskite top cell. Our results reveal that the FF of the tandem solar cell increases as the RShin

of subcells and consequent degradation in tandem solar cell and A) perovskite top cell and B) silicon bottom cell PCE.

Figure 3. Variation in J₀

Figure 4. Decline in RShof the perovskite top cell and resulting FF and PCE

of the respective perovskite/Si tandem solar cell.

Figure 5. FF of perovskite/Si tandem solar cell as a function of current

mismatch for different values of the RShin the perovskite top solar cell.

the perovskite top cell increases. Moreover, the overall increase in the FF caused by current mismatch is more pronounced for tan- dem solar cells limited by current generation in the bottom sub

cell. This is because the RShof the silicon bottom cell is much larger compared to the perovskite top cell. The discussion high- lights that reducing current mismatch in a top-limited tandem solar cell does not necessarily lead to a decrease in FF. If the RShof the perovskite top cell is relatively low, FF may increase instead of an expected decrease (see Figure 5, compare RSh= 1.3 kΩ cm² and RSh= 4.3 kΩ cm²Þ. Furthermore, it is important to note that given a relatively low RShof the perovskite top cell, the FF of the perovskite-limited tandem solar cell is even lower than that of the current-matched cell. c) Third, we discuss the performance of tandem solar cell undergoing JSCdegradation (due to a decline in CE) in the perovskite top and the silicon bot- tom cells. As shown in Figure 6, the PCE of the tandem solar cell does not decrease linearly with decreasing CE of perovskite top and silicon bottom cells. While a reduction in CE results in an expected linear decrement in tandem solar cell JSCof the respec- tive subsolar cell, the overall impact on PCE is much more com- plex. The monolithic interconnection implies that the impact on the PCE highly depends on whether the tandem solar cell is lim- ited by the perovskite top cell, or the Si bottom cell (see Figure 6). Tandem solar cells with limited current generation in the top cell experience a significantly enhanced degradation in JSCcompared to current-matched or bottom-limited tandem cells if the CE of the perovskite top cell decreases. While there is a slight incre- ment in FF for the top-limited cells due to low RSh(compared to a decrease for other current-matching conditions), the degra- dation in JSCoutweighs the mild increase in FF. Overall, the top- limited cell experiences more substantial decline in PCE with respect to other current-matching scenarios (see Figure 6A). On the other hand, if the CE of the silicon bottom cell is reduced instead, a similar overall effect in JSCis observed, indi- cating that bottom-limited devices are more vulnerable to changes in JSC. However, the overall impact is substantially dif- ferent because FF improves for all current-matching conditions. This results in a reduced decline in normalized PCE compared to corresponding perovskite top cell cases (see Figure 6B).

3.2. EY Modeling and Degradation Here, we investigate the EY of perovskite–silicon tandem solar cells factoring in degradation in different solar cell parameters of the perovskite top solar cell. The focus is set on the implication

Figure 6. Impact of 5% decline in CE of the perovskite top solar cell A) and silicon bottom solar cell B) on the solar cell parameters (J

SC, FF, and PCE) of the perovskite–silicon tandem solar cell. Different scenarios of current matching are considered. To facilitate the comparison, we compare the normalized solar cell parameters.

of degradation on the EY of various tandem solar cell architec- tures. As highlighted in the previous section, degradation of SJ solar cell parameters of perovskite top solar cell cannot be translated one-to-one to tandem devices. Moreover, degradation in EY of tandem solar cells varies between locations, due to the interdependencies of the individual solar cell parameters and environmental factors such as irradiation intensity and spec- trum. To shed light on these interdependencies, we focus on three distinct geographical locations (see Figure SI 1 and SI

2): Phoenix (arid/desert location), Seattle (temperate location), and Honolulu (tropical/humid).
3.2.1. EY of Tandem Solar Cells with Degradation across Various Locations First, we assess the EY of tandem solar cells undergoing uniform degradation of 10% in individual perovskite top cell solar cell parameters. The EY is evaluated for various locations. This study
enables us to determine the one solar cell parameter whose deg- radation has the highest impact on tandem solar cell EY. Our analysis reveals that a 10% degradation in the FF of the perov- skite top cell due to a decline in RShand an increment in RS, respectively, shows the highest and lowest impact on tandem solar cell EY regardless of location (see Figure 7 and Figure SI 5). This result emphasizes the importance of rectifying perovskite imperfections in thin film processing causing RShdecline. In real-world conditions, there is an interdependency between degra- dation mechanisms and their effects on diode parameters, as well as between the variations in one diode parameter and others. However, isolating and assessing the impact of each diode param- eter separately is insightful to understand how variation in individual diode parameter affects the overall EY. The observations are consistent with the analysis of degrada- tion under STC, i.e., the observed superlinear relationship between the performance of the tandem solar cell and the decline in RShof the perovskite top cell (see Figure and 5). Furthermore, the minimal impact of an increase in RSon

Figure 7. Relative degradation in tandem solar cell EY undergoing 10%

degradation of the VOC, JSC, and FF implemented by variation in the diode parameters (J₀, CE, RS, and RSh) of the perovskite top cell in Phoenix, Seattle, and Honolulu.

tandem solar cell EY aligns with the linear relationship between tandem solar cell performance and RSincrement (see Figure SI

5). This effect also aligns with its relatively minor impact on other solar cell parameters, such as VOCand JSC. Moreover, the varia- tion in the impact of degradation in JSCand VOCof the perovskite top cell on the tandem solar cell EY in different locations was anticipated due to the established proportional relationship between JSC, VOC, and light intensity.
[52]

3.2.2. EY of Current-Mismatched Tandem Solar Cells with Degradation Next, we investigate the EY of tandem solar cells with different current-matching conditions undergoing degradation. This study aims to reveal how different current-matching conditions of our tandem solar cell under STC affect the lifetime EY con- sidering degradation. It is crucial to highlight that the different current-matching configurations examined in this study refer to cells that are initially mismatched under STC. Subsequently, their performance is evaluated under realistic irradiation conditions. To provide different levels of current mismatch over time, we incorporate two distinct levels of CE decline rates (1% and 2% annually). We compare the lifetime EY of a tandem solar cell installed in Phoenix (see Figure 8A,B) which exhibit three levels of initial current mismatch. The current mismatch is determined under STC. The top-limited tandem solar cell with a 10% current mis- match (≈2mAcm
2 ) experiences the most significant reduction in EY due to linear degradation in JSCof the tandem solar cell. In contrast, the bottom-limited counterpart exhibits the lowest decline (see Figure 8A,B). In the first 12–15 years, the current- matched tandem solar cell shows the highest EY, while the bottom-limited counterpart shows the lowest EY. However, in the second half of the lifetime, the EY of the current-matched tandem device is much lower compared to the EY of the bottom-limited solar cells. For a more detailed dataset

Figure 8. EY of perovskite–silicon tandem solar cell as well as c-Si SJ solar cell

[55] located in Phoenix undergoing a current generation decline in the

SCdegradation with annual CE decline rate of C) 1% and D) 2%. perovskite top cell: A) 1% annual decline in CE and B) 2% annual decline in CE. Lifetime EY (30 years) for different levels of initial current mismatch of the perovskite-silicon tandem solar cell in Phoenix, Seattle, and Honolulu factoring in J

encompassing more increments in current mismatch of the tan- dem solar cell and various locations, we refer to Figure SI 7. Over the entire lifetime, bottom-limited tandem solar cell with ≈5% current mismatch, undergoing JSCdegradation, exhibits the highest cumulative EY over 30 years. It is highlighted that this cumulative EY is even higher than that for an optimum tandem solar cell architecture, i.e., a current-matched tandem solar cell (see Figure 8C,D). The findings are consistent across different locations (see Figure SI 7). In summary, this study shows that a moderate initial current limitation of the bottom solar cell by around 5–10% is optimal for a 30 year lifetime if the top solar cell undergoes JSCdegradation (≈1% and ≈2% annual). Furthermore, considering degradation in current generation of the top solar cell results in a rather broad optimal device archi- tecture with regard to the current matching, if the device is initially moderately bottom limited.

3.2.3. Comparing Degradation in EY and STCs Next, we indicate the difference between degradation impact on the tandem solar cell performance under STC and its EY. We also investigate the tandem solar cell EY undergoing degradation in different solar cell parameters at different rates. We examine the EY in two scenarios: (1) matching the degradation rate of the
perovskite top cell to that of state-of-the-art c-Si solar cells (0.5% per year [53] ) and (2) a significantly higher degradation rate of 2% per year. To discriminate the effect of degradation in different solar cell parameters on the EY and its efficiency, we compare the scenar- ios where degradation rates of 0.5% and 2% are solely caused by degradation in VOC, JSC, or FF. For rather low degradation rates of 0.5%, similar to previous analyses (see Figure 7), we find that the EY of the tandem solar cell decreases linearly but at different rates for each degradation scenario. The tandem solar cell EY exhibits fastest degradation for a decline in the perovskite top cell’s RSh. Conversely, the impact of FF degradation caused by an increment in perovskite top cell’s RSis the lowest (see

Figure 9A). Interestingly, for degradation rates exceeding the

degradation of state-of-the-art silicon PV (e.g., 2%), the degrada- tion in FF due to a decline in RShshows an asymptotic behavior (see Figure 9B). For low RShin the perovskite top solar cell, the tandem solar cell is effectively shunted, and the EY of the tandem solar cell approaches the EY of the silicon bottom cell only. Thus, the asymptotic behavior must not be confused with stabilization or a deceleration in degradation. Furthermore, we compare the degradation in EY to the deg- radation in PCE (see Figure 9C). The direct comparison of the lifetime EY and lifetime degradation in PCE of tandem solar cells (see Figure 9C) highlights that the performance under STC does

Figure 9. Tandem solar cell EY undergoing degradation with absolute annual degradation of A) 0.5% and B) 2% in perovskite top cell in Phoenix.

C) Comparison between the effect of 0.5% and 2% absolute annual degradation in perovskite top cell on tandem solar cell PCE and EY (Phoenix).

not accurately reflect realistic irradiation conditions. For exam- ple, considering a 2% degradation per year in the FF of the perov- skite top solar cell due to an increment in RS, the extrapolation performance degradation of PCE predicts a loss of almost 32%, while the actual loss in lifetime EY due to degradation is only around 22%. The reason for this enormous discrepancy is the wide variation in solar intensity that is considered in EY calcu- lations which consider real-world irradiation scenarios but disre- garded in the assessment of the PCE determine under STC. Similar but less severe differences in lifetime PCE and lifetime EY are apparent for the FF degradation due to decline in RSh.

3.2.4. Permissible Level of Degradation in Top Cell Solar Cell Parameters Next, we examine critical thresholds for the “acceptable levels of degradation” in the perovskite top solar cell with regard to deg- radation in each solar cell parameter, assuming that the total loss in EY over the lifetime of a perovskite tandem must be compa- rable to the degradation in state-of-the-art silicon PV (≈0.5% in performance [53]
). For comparison, to date, one of the lowest reported degradation rates of perovskite PV is in the range of

1.4% in only 1000 h.
[54] This discrepancy highlights the tremen- dous efforts that are required in the upcoming years to improve the durability of perovskite PV. However, to date, it is not even clear what is the sufficient stability, i.e., the “acceptable level of degradation”, for the perovskite top solar cell, considering that the degradation in the top solar cells does not linearly impact the EY of the tandem solar cell. In response, we flip the perspective in this last section and determine backward the acceptable level of degradation in a sin- gle solar cell parameter of the perovskite top solar cell assuming a maximum overall degradation of 0.5% per year in the tandem solar cell. To discriminate the effect of degradation in different solar cell parameters, we compare the scenarios where degrada- tion is solely caused by degradation in VOC, JSC, or FF (see

Figure 10). Our results show that if the stated loss is attributed

solely to degradation in VOC(resulting from an increase in J₀), there is overall a rather low level of VOCdegradation at the end of the lifetime of up to ≈18% which can vary depending on climate zone. This degradation in VOCcorresponds to ≈3000-fold increase in J₀, which is significant as it leads to higher leakage current and increased degradation over time. Conversely, if the mentioned loss is due to JSCdegradation (resulting from a decline in CE), the acceptable JSCdegradation exceeds 15%, con- tingent upon the climate zone. This 15% JSCdegradation equates to an approximate 18% decline in CE. However, when the speci- fied decline in tandem solar cell EY results from FF degradation, the acceptable level of FF degradation varies depending on whether it arises from a decrease in RShor an increase in R .S In summary, our study reveals that the permissible degrada- tion level in the perovskite top cell varies depending on climate zone and the solar cell parameter responsible for the degradation.

#### 4. Conclusion

Perovskite/Si tandem PV has emerged as a promising technol- ogy due to its potential for high efficiency and low-cost produc- tion. However, integrating perovskite materials with silicon presents new challenges concerning the yet limited durability of the perovskite material. While previous research on the stabil- ity of perovskite provides valuable understanding in this topic, studying degradation in real-world conditions is often disre- garded. This study shows how degradation in individual solar cell parameters (i.e., VOC, JSC, and FF) of the perovskite top cell affects the EY of perovskite–silicon tandem solar cell. We assess long-term tandem solar cell EY undergoing different degradation scenarios. First, we assess tandem solar cell EY undergoing deg- radation of individual solar cell parameter (VOC, JSC, and FF) in the perovskite top cell. However, as to date there is no clear understanding of how degradation mechanisms interrelate with

Figure 10. Permissible levels of degradation in VOC, JSC

, RS, and RSh,, and FF and corresponding variation in the contributing diode parameters, i.e., CE, J₀ respectively, for 0.5% annual degradation in tandem solar cell EY over 30 years in different climatic conditions.

simulated EY data. This comparison will be instrumental while designing experiments replicating the simulation conditions and providing a robust benchmark, enabling a deeper understanding of degradation mechanisms and their impact on EY. While the experimental datasets on EY of perovskite/silicon tandem PV are limited today, we expect that the number of such datasets will strongly increase in the near future, given rise to many research questions that can be addressed with our EY framework (EYCalc). We believe that an industrial implementation to the analyses conducted in this study, such as the analysis of initially mismatched tandem solar cells, with the objective of identifying the optimal device architecture (current-matching scenario) based on total lifetime EY, represents a fruitful avenue for future research.

#### Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

the diode parameters, we perform our study at the level of diode parameters (i.e., J₀, CE, RS, and RSh). This analysis provides the foundation for the future studies. Once a definitive interrelation between real degradation mechanisms and variation in diode parameters identified, our EY modeling framework will be able to perform analysis in the context of specific degradation mechanisms. Our results demonstrate that degradation in FF of perovskite top cell due to a decline in RShand an increment in RShas the most and least significant effect on tandem solar cell EY, respectively. This shows the importance of rectifying perovskite imperfections in thin film processing as the leading cause of RShdecline. Furthermore, our analysis reveals that the influence of degradation on tandem solar cell EY varies across different climatic zones, providing region-specific insights for optimization. Next, we demonstrate the EY of mismatched tandem solar cells undergoing degradation. We focus on JSCdegradation in this analysis, as it modifies the current mismatch over time and effectively represents the interplay between mismatched tan- dem solar cell EY and degradation. Based on our research, a slightly bottom-limited cell, undergoing JSCdegradation, has the highest cum EY over 30 years across various climate zones. Furthermore, we illustrate that keeping the initial current mis- match of a bottom-limited cell, undergoing JSCdegradation, within a 10% margin results in minimal EY loss. Understanding the precise value (referring to a 5% bottom-lim- ited scenario) and margin (5–10%) for bottom limitations despite degradation ensures minimal EY loss of tandem solar cells, which is crucial for industrial implementation. This analysis helps manufacturers optimize device architecture for maximum lifetime EY, enhance durability by selecting materials and designs suited for various climate zones, and maintain perfor- mance stability by controlling initial current mismatch. Next, we assess long-term tandem solar cell EY when the perovskite top cell undergoes degradation rates equal to or higher than the observed degradation rate in c-Si solar cells (0.5% and 2% annually, respectively). Our analysis reveals a potential exclu- sion of the perovskite top cell from the tandem solar cell when the degradation rate of the perovskite top cell surpasses a certain threshold (>2% annually). Finally, we examine critical thresholds for the “acceptable lev- els of degradation” in the perovskite top solar cell with regard to degradation in each solar cell parameter. This analysis is done by assuming that the total EY loss over the lifetime of a perovskite- silicon tandem must be comparable to the degradation in c-Si solar cells (i.e., max. 0.5% per year). This analysis provides a com- prehensive understanding of EY degradation in perovskite– silicon tandem solar cells and the overall impact of degradation in the individual solar cell parameters. This analysis aids manufacturers in designing solar cells suitable for different cli- mate zones by considering the impact of environmental factors such as light intensity, humidity, and temperature on diode parameters. Understanding the acceptable degradation rate in each parameter provides target values for optimizing the materials used in solar cells ensuring enhanced durability and performance. In future research, we foresee to compare the experimental

|M.|T. Hörantner,|A. Haghighirad,|N. Sakai,|L. Korte,|B. Rech,|
|---|---|---|---|---|---|
|M. B. Johnston, L. M. Herz, H. J. Snaith, Science 2016, 351, 151.||||||

stability data of perovskite–silicon tandem solar cells with the

#### Acknowledgements

Financial support by the Initiating and Networking funding of the Helmholtz Association (Project Zeitenwende and the Solar Technology Acceleration Platform (Solar TAP)), the program-oriented funding IV of the Transition, Helmholtz Topic Association 1: Photovoltaics (Materials andandWind Technologies Energy, Code: for the

38.01.04), Energy
the German Federal Ministry for Economic Affairs and Climate Action (BMWK) through the project 27Plus6 (03EE1056B) and SHAPE (03EE1123A), and the Karlsruhe School of Optics and Photonics (KSOP) is gratefully acknowledged. The project was further supported by the European Commission through HORIZON EUROPE Research and Innovation Actions under grant agreement no. 101 075 330, project NEXUS. Open Access funding enabled and organized by Projekt DEAL.

#### Conflict of Interest

The authors declare no conflict of interest.

#### Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### Keywords

degradation, energy yield, perovskite stability, perovskite/silicon tandem solar cells

Received: May 16, 2024 Revised: July 15, 2024 Published online: August 24, 2024

[1] L. C. Andreani, A. Bozzola, P. Kowalczewski, M. Liscidini, L. Redorici, Adv. Phys. X 2019, 4, 1548305. [2] D. P. McMeekin, G. Sadoughi, W. Rehman, G. E. Eperon, M. Saliba,

M. T. Hörantner, A. Haghighirad, N. Sakai, L. Korte, B. Rech,

[3] E. Aydin, T. G. Allen, M. De Bastiani, L. Xu, J. Ávila, M. Salvador,

E. Van Kerschaver, S. De Wolf, Nat. Energy 2020, 5, 851.
[4] L. Wang, Q. Song, F. Pei, Y. Chen, J. Dou, H. Wang, C. Shi, X. Zhang,

R. Fan, W. Zhou, Z. Qiu, J. Kang, X. Wang, A. Lambertz, M. Sun,
X. Niu, Y. Ma, C. Zhu, H. Zhou, J. Hong, Y. Bai, W. Duan,
K. Ding, Q. Chen, Adv. Mater. 2022, 34, 2201315.
[5] H. Zhou, Q. Chen, G. Li, S. Luo, T. Song, H.-S. Duan, Z. Hong, J. You,

Y. Liu, Y. Yang, Science 2014, 345, 542.
[6] F. Sahli, J. Werner, B. A. Kamino, M. Bräuninger, R. Monnard,

B. Paviet-Salomon, L. Barraud, L. Ding, J. J. Diaz Leon,
D. Sacchetto, G. Cattaneo, M. Despeisse, M. Boccard, S. Nicolay,
Q. Jeangros, B. Niesen, C. Ballif, Nat. Mater. 2018, 17, 820.
[7] H. Shen, S. T. Omelchenko, D. A. Jacobs, S. Yalamanchili, Y. Wan,

D. Yan, P. Phang, T. Duong, Y. Wu, Y. Yin, C. Samundsett,
J. Peng, N. Wu, T. P. White, G. G. Andersson, N. S. Lewis,
K. R. Catchpole, Sci. Adv. 2018, 4, eaau9711.
[8] D. Kim, H. J. Jung, I. J. Park, B. W. Larson, S. P. Dunfield, C. Xiao,

J. Kim, J. Tong, P. Boonmongkolras, S. G. Ji, F. Zhang, S. R. Pae,
M. Kim, S. B. Kang, V. Dravid, J. J. Berry, J. Y. Kim, K. Zhu,
D. H. Kim, B. Shin, Science 2020, 368, 155.
[9] J. Liu, M. De Bastiani, E. Aydin, G. T. Harrison, Y. Gao, R. R. Pradhan,

M. K. Eswaran, M. Mandal, W. Yan, A. Seitkhan, M. Babics,
A. S. Subbiah, E. Ugur, F. Xu, L. Xu, M. Wang, A. Rehman,
A. Razzaq, J. Kang, R. Azmi, A. A. Said, F. H. Isikgor, T. G. Allen,
D. Andrienko, U. Schwingenschlögl, F. Laquai, S. De Wolf, Science 2022, 377, 302.
[10] S. Mondal, M. Chaudhury, P. Chakrabarti, S. Maity, Energy Fuels 2023, 37, 12301. [11] S. Mondal, A. Jain, S. Maity, Sol. Energy Mater. Sol. Cells 2024, 271, 112869. [12] National Renewable Energy Laboratory, Best Research-Cell Efficiency Chart, [https://www.nrel.gov/pv/cell-efficiency.html](https://www.nrel.gov/pv/cell-efficiency.html). [13] E. Commission, J. R. Centre, A. Jäger-Waldau, PV Status Report 2018, Publications Office of the European Union, Luxembourg, 2018, ISBN 978-92-79-97466-3, [https://doi.org/10.2760/924363](https://doi.org/10.2760/924363), JRC113626. [14] P.-J. Ribeyron, Nat. Energy 2017, 2, 17067. [15] Y. Li, B. Shi, Q. Xu, L. Yan, N. Ren, Y. Chen, W. Han, Q. Huang,

Y. Zhao, X. Zhang, Adv. Energy Mater. 2021, 11, 2102046.
[16] M. A. Green, A. Ho-Baillie, H. J. Snaith, Nat. Photonics 2014, 8, 506-514. [17] F. Schackmar, H. Eggers, M. Frericks, B. S. Richards, U. Lemmer,

G. Hernandez-Sosa, U. W. Paetzold, Adv. Mater. Technol. 2021, 6, 2000271.
[18] J. Roger, L. K. Schorn, M. Heydarian, A. Farag, T. Feeney,

D. Baumann, H. Hu, F. Laufer, W. Duan, K. Ding, A. Lambertz,
P. Fassl, M. Worgull, U. W. Paetzold, Adv. Energy Mater. 2022, 12, 2200961.
[19] G. Yang, M. Wang, C. Fei, H. Gu, Z. J. Yu, A. Alasfour, Z. C. Holman,

J. Huang, ACS Energy Lett. 2023, 8, 1639.
[20] VDMA, International Technology Roadmap for Photovoltaic, https:// vdma.org. [21] G. Grancini, C. Roldán-Carmona, I. Zimmermann, E. Mosconi, X. Lee,

D. Martineau, S. Narbey, F. Oswald, F. De Angelis, M. Graetzel,
M. K. Nazeeruddin, Nat. Commun. 2017, 8, 15684.
[22] A. Mei, Y. Sheng, Y. Ming, Y. Hu, Y. Rong, W. Zhang, S. Luo, G. Na,

C. Tian, X. Hou, Y. Xiong, Z. Zhang, S. Liu, S. Uchida, T.-W. Kim,
Y. Yuan, L. Zhang, Y. Zhou, H. Han, Joule 2020, 4, 2646.
[23] Y. Kato, L. K. Ono, M. V. Lee, S. Wang, S. R. Raga, Y. Qi, Adv. Mater. Interfaces 2015, 2, 1500195. [24] J. A. Schwenzer, L. Rakocevic, R. Gehlhaar, T. Abzieher,

S. Gharibzadeh, S. Moghadamzadeh, A. Quintilla, B. S. Richards,
U. Lemmer, U. W. Paetzold, ACS Appl. Mater. Interfaces 2018, 10, 16390.
[25] D. Zhang, D. Li, Y. Hu, A. Mei, H. Han, Commun. Mater. 2022, 3, 58. [26] B. Chen, J. Song, X. Dai, Y. Liu, P. N. Rudd, X. Hong, J. Huang, Adv. Mater. 2019, 31, 1902413. [27] R.-Y. Hsu, Y.-J. Liang, Y.-J. Hung, Y.-C. Lin, Mater. Sci. Semicond. Process. 2022, 152, 107100. [28] X. Zhang, X. Chen, Y. Chen, N. A. Nadege Ouedraogo, J. Li,

X. Bao, C. B. Han, Y. Shirai, Y. Zhang, H. Yan, Nanoscale Adv. 2021, 3, 6128.
[29] M. V. Khenkin, E. A. Katz, A. Abate, G. Bardizza, J. J. Berry, C. Brabec,

F. Brunetti, V. Bulovi´c, Q. Burlingame, A. Di Carlo, R. Cheacharoen,
Y.-B. Cheng, A. Colsmann, S. Cros, K. Domanski, M. Dusza, C. J. Fell,
S. R. Forrest, Y. Galagan, D. Di Girolamo, M. Grätzel, A. Hagfeldt,
E. von Hauff, H. Hoppe, J. Kettle, H. Köbler, M. S. Leite, S. Liu,
Y.-L. Loo, J. M. Luther, C.-Q. Ma, M. Madsen, M. Manceau,
M. Matheron, M. McGehee, R. Meitzner, M. K. Nazeeruddin,
A. F. Nogueira, Ç. Odabaşı, A. Osherov, N.-G. Park, M. O. Reese,
F. De Rossi, M. Saliba, U. S. Schubert, H. J. Snaith, S. D. Stranks,
W. Tress, P. A. Troshin, V. Turkovic, S. Veenstra, I. Visoly-Fisher,
A. Walsh, T. Watson, H. Xie, R. Yıldırım, S. M. Zakeeruddin,
K. Zhu, M. Lira-Cantu, Nat. Energy 2020, 5, 35.
[30] Z. Ni, H. Jiao, C. Fei, H. Gu, S. Xu, Z. Yu, G. Yang, Y. Deng, Q. Jiang,

Y. Liu, Y. Yan, J. Huang, Nat. Energy 2022, 7, 65.
[31] T. A. Chowdhury, M. A. Bin Zafar, M. Sajjad-Ul Islam,

M. Shahinuzzaman, M. A. Islam, M. U. Khandaker, RSC Adv. 2023, 13, 1787.
[32] Z. Shen, Q. Han, X. Luo, Y. Shen, Y. Wang, Y. Yuan, Y. Zhang,

Y. Yang, L. Han, Nat. Photonics 2024, 18, 450.
[33] F. Gota, R. Schmager, A. Farag, U. W. Paetzold, Opt. Express 2022, 30, 14172. [34] R. Schmager, M. Langenhorst, J. Lehr, U. Lemmer, B. S. Richards,

U. W. Paetzold, Opt. Express 2019, 27, A507.
[35] J. Lehr, M. Langenhorst, R. Schmager, S. Kirner, U. Lemmer,

B. S. Richards, C. Case, U. W. Paetzold, Sustain. Energy Fuels 2018, 2, 2754.
[36] R. Schmager, U. W. Paetzold, M. Langenhorst, F. Gota,

J. Lehr, [https://doi.org/10.5281/ZENODO.4696257](https://doi.org/10.5281/ZENODO.4696257) (accessed: May
2024).
[37] M. Remec, Š. Tomšic,ˇ M. Khenkin, Q. Emery, J. Li, F. Scheler,

B. Glažar, M. Jankovec, M. Jošt, E. Unger, S. Albrecht,
R. Schlatmann, B. Lipovšek, C. Ulbrich, M. Topic,ˇ Adv. Energy Mater. 14, 2304452.
[38] S. Wilcox, W. Marison, User Manual for TMY3 Dataset, National Renewable Energy Laboratory, Golden, CO 2008. [39] C. A. Gueymard, Sol. Energy 2001, 71, 325. [40] S. C. Baker-Finch, K. R. McIntosh, Prog. Photovolt. Res. Appl. 2011, 19,

406.
[41] Analog Devices, Inc. LTSpice [Computer software] (n.d.) https:// www.analog.com/en/design-center/design-tools-and-calculators/ ltspice-simulator.html (accessed May 2024). [42] M. C. Alonso García, J. L. Balenzategui, Renew. Energy 2004, 29, 1997. [43] J. T. DuBose, P. V. Kamat, Mater. Res. 2022, 3, 761. [44] A. F. Gualdrón-Reyes, S. J. Yoon, I. Mora-Seró, Curr. Opin. Electrochem. 2018, 11, 84. [45] P. Darvishzadeh, G. Redzwan, R. Ahmadi, N. E. Gorji, Org. Electron. 2017, 43, 247. [46] D. Glowienka, Y. Galagan, Adv. Mater. 2022, 34, 2105920. [47] C. Xiao, F. Zhang, Z. Li, S. P. Harvey, X. Chen, K. Wang, C.-S. Jiang,

K. Zhu, M. Al-Jassim, Matter 2020, 2, 261.
[48] G. Jeong, D. Koo, J. Seo, S. Jung, Y. Choi, J. Lee, H. Park, Nano Lett. 2020, 20, 3718. [49] H. Zai, Y. Ma, Q. Chen, H. Zhou, J. Energy Chem. 2021, 63, 528. [50] L. M. Shaker, A. Alamiery, W. N. R. W. Isahak, W. K. Al-Azzawi, J. Opt.

2023.

www.advancedsciencenews.com www.entechnol.de

|[51] E. Köhnen,|M. Jošt,|A. B. Morales-Vilches,|P.|Tockhorn,|
|---|---|---|---|---|
|A. Al-Ashouri,|B. Macco,|L. Kegelmann,|L. Korte,|B. Rech,|
|R. Schlatmann, 2019, 3, 1995. [52] M. T. Islam, A. Kumar, A. K. Thakur, J. Electron. Mater. 2021, 50, 3603. [53] F. Carigiet, C. J. Brabec, F. P. Baumgartner, Renew. Sustain. Energy Rev. 2021, 144, 111005.|B. Stannowski,|S. Albrecht,|Sustain. Energy|Fuels|

[54] K. Liu, S. Rafique, S. F. Musolino, Z. Cai, F. Liu, X. Li, Y. Yuan,

Q. Bao, Y. Yang, J. Chu, X. Peng, C. Nie, W. Yuan, S. Zhang,

|Q. Bao,|Y. Yang, J. Chu,|X. Peng, C.|Nie, W. Yuan,|S. Zhang,|
|---|---|---|---|---|
|J. Wang,|Y. Pan, H.|Zhang, X. Cai,|Z. Shi, C.|Li, H. Wang,|
|L. Deng, J. E. Wulff, A. Yu, Y. Zhan, Joule 2023, 7, 1033.|T. Hu, Y. Wang,|Y. Wang,|S. Chen, L.|Shi, P. Ayala,|
|[55] X. Ru, M.|Qu, J. Wang,|T. Ruan, M.|Yang, F. Peng,|W. Long,|
|K. Zheng, 215, 110643.|H. Yan, X.|Xu, Sol. Energy|Mater. Sol.|Cells 2020,|

Energy Technol. 2024, 12, 2400998 2400998 (12 of 12) © 2024 The Author(s). Energy Technology published by Wiley-VCH GmbH
