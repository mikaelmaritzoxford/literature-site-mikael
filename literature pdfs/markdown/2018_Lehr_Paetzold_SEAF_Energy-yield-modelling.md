# Sustainable Energy & Fuels

## PAPER

## Energy yield modelling of perovskite/silicon two-terminal tandem PV modules with flat and

Cite this: Sustainable Energy Fuels, 2018, 2,2754 textured interfaces†

a b b c Jonathan Lehr,‡* Malte Langenhorst,‡ Raphael Schmager, Simon Kirner, ab ab c ab Uli Lemmer, Bryce S. Richards, Chris Case and Ulrich W. Paetzold *

Perovskite/silicon tandem photovoltaics have emerged as a new technology for highly efficient and inexpensive photovoltaics (PV). In order to maximize the energy yield (EY) and reduce the cost of generated electricity, light management concepts are of key importance for this technology. This numerical study provides a systematic EY analysis, evaluating and predicting the improvement in the EY of perovskite/silicon (Si) two-terminal (2T) PV modules employing micron-scale random pyramids at the front and/or rear surface of the PV module. The 2T tandem PV module architectures comprise an optically thick encapsulant and a module front cover glass with an anti-reflection coating. The EY is studied at various locations in the USA with different climate zones. For a perovskite top solar cell with a bandgap of around 1.72 eV, the perovskite/Si 2T tandem PV modules with textured front and rear surfaces yield the highest relative enhancement in EY of around 26–28% compared to that of a state-of- the-art crystalline Si single-junction reference. The relative enhancement in the EY of planar and rear side textured perovskite/Si 2T tandem PV modules is lower (planar: 12–14% and rear side textured: Received 18th September 2018 19–22%). Finally, the EY of the textured perovskite/Si tandem PV module is investigated with respect to Accepted 5th October 2018 the bandgap of the perovskite top solar cell. Overall, this study highlights the great promise of DOI: 10.1039/c8se00465j perovskite/Si 2T tandem PV modules under realistic irradiation conditions and emphasizes the rsc.li/sustainable-energy importance of light management textures for maximizing the EY of this technology.

### Introduction

Metal-halide perovskites are an extremely promising class of materials for highly efficient single-junction (SJ) thin-lm photovoltaics (PV) as well as for novel multijunction PV technologies. 1 Metal-halide perovskite thin lms can be deposited from inexpensive precursor materials by low-cost solution-based deposition techniques² as well as by physical vapour deposition. 3 Due to their high absorption coefficients, 4 long charge carrier diffusion lengths, 5 and bandgap tunability, 6 metal-halide perovskites are perfectly suited for the top solar cell in highly efficient perovskite/silicon (Si) tandem PV. 7 The technology builds upon the market- dominating crystalline Si PV and expands the theoretical

limitofpowerconversione 8 fficiency (PCE) from around 29% 9 for Si SJ PV to well above 35%. Two competing congurations of perovskite/Si tandem PV are currently investigated and prototyped. In the 4-terminal (4T) conguration, the perovskite top solar cell with transparent contacts is simply mechanically stacked on top of the Si bottom solar cell. In this conguration, four contacts are required for the whole device, inducing optical losses but also enabling each sub-cell to be operated at its individual maximum power point (MPP). 10–14 In contrast, in the 2-terminal (2T) conguration, the perovskite top solar cell and Si bottom solar cell are mono- lithically interconnected and thus series-connected. The 2T conguration uses only one front and one rear contact layer, which reduces the associated optical losses but entails careful optimization of the layer stack in order to match the photo- current generation within both sub-cells. 15–18 Prototype perovskite/Si tandem solar cells of small area (#1cm 2 ) demonstrated PCEs of up to 26.4% (ref. 10) and 25.2% (ref. 18) for the 4T and 2T congurations, respectively. The best 2T tandem solar cells use silicon heterojunction (SHJ) solar cells as bottom cells, which allow an easy full area connection of the two sub cells. The rst fully interconnected perovskite/Si 4T tandem PV modules with an aperture area of around 4 cm demonstrated PCEs of up to 23.9%. Tremendous efforts in

This journal is © The Royal Society of Chemistry 2018

a Light Technology Institute, Karlsruhe Institute of Technology, Engesserstrasse 13, 76131 Karlsruhe, Germany. E-mail: Jonathan.Lehr@kit.edu; Ulrich.Paetzold@kit.edu b Institute of Microstructure Technology, Karlsruhe Institute of Technology, Hermann- von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany c Oxford Photovoltaics, Unit 7-8 Oxford Industrial Park, Mead Road, Oxford, OX5 1QU, UK † Electronic supplementary information (ESI) available. See DOI:

10.1039/c8se00465j ‡ These authors contributed equally to this work. 2754 | Sustainable Energy Fuels,2018,2,2754–2761

**View Article Online** Sustainable Energy & Fuels Paper

research and development are currently dedicated to further advancing the materials of the perovskite top solar cell 15,17–19 by engineering the interfaces, advancing the perovskite absorber material, and optimizing the light management and device architecture of perovskite/Si tandem PV. 13,14,16,20–23 Optimal light management is a key prerequisite for high energy yield (EY) of any PV technology, as it optimizes the harvesting of incident sunlight under realistic irradiation conditions. This is in stark contrast to the very particular “standard test conditions” (STC) used to measure the PCE of PV technologies (1000 W m 2 of the air-mass 1.5 global (AM1.5g) spectrum at normal incidence while the device is held at 25 C). 24 Light management can be achieved by various concepts, encompassing nanophotonic structures, micron- scale textures and plasmonic nanoparticles. In conventional crystalline Si PV, effective light management is achieved via micron-scale pyramids at the front and/or the rear surface. These textures improve the light in-coupling at the front and enhance the overall effective light path length by scattering light inside the Si wafer. 25–27 For example, for textured crystalline Si solar cells of 165 mm thickness, 28 the current generation is improved by 18% from 35.9 mA cm 2 to 42.3 mA cm 2

compared to that of a planar device, resulting in a similar enhancement of the PCE. A simple and widely used route to realize these micron-scale textures in crystalline Si PV relies on anisotropic wet-chemical etching of (100)-oriented Si wafers to expose the faces of the (111) crystal planes, leading to the so-

|Fig. 1|Three layer stacks of||perovskite/Si|2T tandem PV||modules|
|---|---|---|---|---|---|---|
|based a micron-scale pyramid-textured front and rear; and (III) a planar front with a micron-scale pyramid at the textured rear.|on crystalline|Si wafers|with (I)|a planar|front and|rear; (II)|

called “random pyramid texture”. 29,30 While this random pyramid texture can be easily integrated at the front surface of the crystalline Si bottom solar cell in perovskite/Si 4T and 2T tandem PV, the integration in perovskite/Si 2T tandem PV devices is more complex: 18

(1) the pyramidal texture increases
the interface area by almost ~70%, leading to more surface recombination; (2) enhanced challenges with the deposition of the top cell. However, with the front surface remaining planar, more attention has to be paid to the optical design of the device. 16 Furthermore, asymmetric (rear side only) etching is not standard for SHJ cells, which complicates the integration with the perovskite top cell, as it requires additional process steps. Considering emerging technology commercialization, it is of high importance to quantify the impact of the pyramid texture on the EY of perovskite/Si 2T tandem PV devices under realistic irradiation conditions. EY modelling of perovskite/Si PV considers realistic irradia- tion scenarios for various geographic locations. 31,32 In previous EY modelling studies, the performance of perovskite/Si tandem PV in the 4T and 2T congurations was compared only for a planar (unencapsulated) cell architecture. 33,34 The potential in overall EY improvement of planar perovskite/Si tandem PV compared to the Si SJ PV reference technology was clearly shown, demonstrating the need for architecture optimization and light management of perovskite/Si tandem PV. 31 This study comprises a systematic EY analysis of perovskite/Si 2T tandem PV modules, in order to investigate and predict the overall improvement in EY provided by light management based on the random pyramid texture. Three key architectures of perovskite/ Si 2T tandem PV devices are studied (see Fig. 1): (I) a planar

reference device architecture, (II) a double-side textured device architecture, and (III) a rear side only textured device architec- ture. This work focusses on optical aspects which imply that the investigated device architectures feature the layer sequence of a realistic solar module but disregards electrical nger grids, busbars and wiring. First, the PCEs of perovskite/Si 2T tandem PV modules under STC are compared, highlighting the need for current matching in these devices. Second, the maximum EY of the perovskite/Si 2T tandem PV modules is predicted for various locations with different climate zones. The results are refer- enced to the EY of the Si SJ PV module either in planar (I) or in textured (II and III) architectures. Finally, the role of the bandgap of the perovskite in the EY of textured perovskite/Si 2T tandem PV modules is investigated.

### Results

The EY modelling consists of an in-house developed code for the optical and electronic simulation of solar cells and for the generation of angular and wavelength-resolved irradiance data for different locations. In the optical model, the textured surfaces are treated by statistical ray-tracing following the approach suggested by Baker-Finch and McIntosh for textured Si solar cells. 35,36 The inputs for the EY model are optical

constants of all layers of the investigated textured perovskite/Si 2T tandem PV modules as well as the Si SJ PV modules, elec- trical parameters of state-of-the-art SJ reference devices, 28,37 and irradiance data of a typical meteorological year (TMY3) available from the National Renewable Energy Laboratory (NREL). 38 The detailed description of EY modelling as well as all optical constants, electrical parameters, and simulated SJ reference devices can be found in the ESI (see Fig. S1–S12†). The electrical parameters for the simulated SJ reference devices are adapted to the above-mentioned state-of-the-art SJ reference devices 28,37 (see Fig. S2 and S5†). In this study, the inuence of micron-scale random pyramid textures in perovskite/Si 2T tandem PV modules is investigated. Enhancing the light absorption by both longer effective light paths and improved light in- coupling, these textures improve the overall device perfor- mance. In order to discriminate the impact of these two effects in perovskite/Si 2T tandem PV modules, as a starting point, we discriminate the simulated absorption for normal incidence in

(i) the perovskite absorber layer of the top solar cell; (ii) the Si absorber layer of the bottom solar cell; and (iii) all parasitic losses that occur in the anti-reection coating (ARC), trans- parent contacts, charge transport layers and passivation layers,
as illustrated in Fig. 2(a). Here, the multicrystalline metal-halide perovskite top cells exhibit a bandgap of 1.72 eV, which is optimal for perovskite/Si 2T tandem PV modules under AM1.5g according to the detailed balance limit of efficiency. 9 Compared to the planar architecture (I), the absorption of near-infrared light (950–1100 nm) in the Si absorber layer is enhanced for textured perovskite/Si 2T tandem PV modules (both case II and case III) due to enhanced light trapping: the light is redirected at the random textures, leading to an enhanced light path in the absorber layers. 39 Since light of wavelengths longer than 900 nm is insufficiently absorbed during a single pass through the Si absorber layer, micron-scale textures lead to enhanced absorp- tion. In addition, the double-side textured perovskite/Si 2T tandem PV module (II) exhibits increased absorption over the entire wavelength range in the perovskite top and crystalline Si bottom absorber layers due to improved light in-coupling. The micron-scale texture enforces incident light to impinge multiple times on the front interface, leading to an overall reduced reection. Next to the absorption in the perovskite and Si absorber layers, also the parasitic absorptance losses in the transparent conductive oxides (TCO) and charge transport layers (CTL) are enhanced (see architecture (II) in Fig. 2). The

module is also shown.

Fig. 2 (a) Reflectance (R) and absorptance (A) as a function of wavelength, broken down into the perovskite top absorber layer, the crystalline Si

bottom absorber layer, and the parasitic absorption in all other layers, for all three architectures of the perovskite/Si 2T tandem PV modules as illustrated in Fig. 1. The integrated JSCfor each sub-cell is also indicated. (b) PCE of the perovskite/Si 2T tandem PV modules as a function of perovskite absorber layer thickness, compared to the PCE of the reference textured crystalline Si SJ PV module. (c) Illustration of current matching by showing the JSCof the perovskite top solar cell and the Si bottom solar cell of a perovskite/Si 2T tandem PV module with the double- side texture (II) as a function of perovskite absorber layer thickness. For comparison, half of the JSCof the reference textured crystalline Si SJ PV

de-rating factors

||SC||Table|1 Efficiency|for optimized|perovskite/Si|
|---|---|---|---|---|---|---|
|||SC|tandem PV modules with the three architectures in this study for the location Daggett Architecture||Efficiency de-rating factor (calc. for Daggett, USA)||
|||SC|||||
|2||2|(I) Planar (II) Double-side textured||1.02 0.96||
|SC|2||(III) Rear side textured||1.00||

short-circuit current density (J) calculated from the absorp- tion in the perovskite top absorber layer and the crystalline Si bottom absorber layer (see Fig. 2(a)) improves by light in- coupling, which results in a larger enhancement in J compared to the light trapping effect. Light trapping due to a textured rear surface leads to an enhancement of J from

17.8 mA cm (planar architecture (I)) to 19.1 mA cm (rear texture (III)), while the double-side textured solar cells (II) exhibit a J of 20.1 mA cm. It should be noted that for all three architectures, the thickness of the perovskite top absorber layer is different due to the constraints of current matching within the perovskite/Si 2T tandem device. In order to maintain current matching for a given architecture, we optimize the perovskite top absorber layer thickness of each architecture. This is illustrated in
Fig. 2(b), which shows the PCE of the perovskite/Si 2T tandem
 solar cells of each architecture as a function of the thickness of the perovskite absorber layer. In Fig. 2(c), the role of current matching is illustrated for the double-side textured architecture (II). With increasing perovskite absorber layer thickness, the JSC of the perovskite top solar cell increases while the JSCof the Si bottom solar cell decreases. Both JSCvalues intersect at the point of current matching, which corresponds to the maximum in PCE, given that the variations in thickness do not change the electrical parameters of the solar cell. Furthermore, Fig. 2(b) shows that the optimal thickness increases from the planar architecture (I) to the architecture with the double-side texture (III) and the architecture with the rear texture (II). The reason is that the Si bottom solar cell benets more from the improved light management by the textures in comparison to the perovskite top solar cell.
13 As a consequence, thicker perovskite absorber layers are allowed for those architectures with good light management to achieve current matching. This implies that more photons can be har- vested in the perovskite top solar cell at high voltage. Finally, we paid attention to the maximum enhancement in the PCE of the perovskite/Si 2T tandem PV modules compared to the PCE of the state-of-the-art reference Si SJ PV module. As shown in

Fig. 2(b), the planar architecture (I) yields a relative enhance-

ment of 16%, and the architecture with the rear texture (III) yields a relative enhancement of 26% in the perovskite/Si 2T tandem solar cell conguration. The highest PCE is obtained for the architecture with the double-side texture (II), which leads to a relative enhancement in PCE by 31%, corresponding to an absolute PCE of 31.6%. This is a remarkable improvement potential and in accordance with several previous theoretical and simulation based studies in the eld. 20,40 However, as mentioned in the beginning, a front side texture increases the interface area by 70%, leading—depending on the interface passivation quality—inevitability to more surface recombina- tion. This aspect is not currently accounted for in our model. However, interface recombination is believed to be the main loss contribution in perovskite solar cells. 41 Despite the promising enhancements in PCE obtained for textured perovskite/Si 2T tandem PV modules, this result is only representative for irradiation with a very specic spectrum (AM1.5g) at normal incidence. Thus, the above described

improvements in performance based on the relative increase of PCE by introducing textures into the perovskite/Si 2T tandem PV module need to be re-evaluated with regard to realistic irradiation conditions. Fig. 3(a) shows the EY of the reference Si SJ PV module with the double-side texture and the three architectures of perovskite/Si 2T tandem PV modules as intro- duced above for ve locations in the USA. The locations were selected such that they represent different climate conditions, covering hot desert climate in Daggett (California), humid subtropical climate in Miami (Florida) and temperate climate in Portland (Oregon). 42 For each architecture and location, the perovskite absorber layer thickness is again optimized for maximizing the EY. For a large perovskite absorber layer thickness in the range of the diffusion lengths of free charge carriers, the model does not account reasonably for free charge carrier recombination and, thus, we choose 750 nm as the upper limit of the simulated perovskite absorber layer thickness. Additionally the PV module tilt is optimized in order to maximize the EY. For Daggett the maximal EY is 622 kW h m 2 a 1 for architecture (I), 696 kW h m 2 a 1 for (II), 662 kW h m 2 a 1 for (III) and 554 kW h m 2 a 1 for the Si reference. The irradiance in Portland is signicantly lower due to its higher cloud coverage during the year, which results in an EY of only 423 kW h m 2 a 1

for the perovskite/Si 2T tandem PV module with the double-side texture (II). Thus, we can conclude that also with regard to EY and independent of the climate of the location, the perovskite/Si 2T tandem PV module with the double-side texture (II) is superior to the planar architecture (I) and the architecture with the rear texture (III). The main reason is the improvement of light incoupling at the front side texture, resulting in a reduced reection of light. For illustration, we show the loss in EY that can be accounted for due to reection for all investigated perovskite/ Si 2T tandem PV module architectures and locations (see

Fig. S13†). However, the relative enhancement of EY compared to

the Si SJ PV module is lower than the corresponding enhance- ment in PCE. For the perovskite/Si 2T tandem PV module with the double-side texture, the relative enhancement in EY is around 26–28%, while the enhancement in PCE is 31%. Reasons for this include apparent variations in the solar spectrum and the vari- ations of the angle of incidence, impeding optimal current matching throughout the entire course of the day and the year. Next to the overall improved EY of the perovskite/Si 2T tandem PV module with the double-side texture, this architec- ture also exhibits a signicantly enhanced angular stability as demonstrated in Fig. 3(b) for the location Daggett. The double- side textured perovskite/Si 2T tandem PV modules show a much higher EY over a wide range of perovskite absorber layer

Fig. 3 (a) Maximum EY obtained for the three architectures of the perovskite/Si 2T tandem PV modules as illustrated in Fig. 1. The maximum EY is

based on the optimization of the perovskite layer thickness and installation angle of the PV module for each of the five locations (Daggett, Miami, Nashville, Portland, and Salt Lake City). For comparison, the EY of the reference case, namely, the textured crystalline Si SJ PV module, is provided and the relative enhancement is indicated. (b) EY for each architecture of the perovskite/Si 2T tandem PV module as a function of perovskite absorber layer thickness and tilt angle at the location Daggett.

thicknesses as well as angles of incidence. This is the key to high EY, since the angle of incidence varies in the EY studies due to the apparent diffuse daylight and the course of the sun. In order to compare the performance of a multijunction PV technology and the existing market-dominating Si SJ PV tech- nology, the efficiency de-rating factor (fD) is a useful measure. 33 This factor is dened as the ratio of the annual EY and the PCE of the perovskite/Si tandem PV module to the same ratio of the Si SJ PV module with the same type of light management texture:

<u>EYtandemPCESi</u> f D¼ PCEtandemEYSi

For the planar architecture (I) at the location Daggett the efficiency de-rating factor is 1.02, which is in good agreement with the values reported by H¨orantner et al. 33 For the devices with light management texture, the efficiency de-rating factor remains high but decreases slightly to 1.00 for the architecture with the rear texture (III) and 0.96 for the architecture with the double-side texture (II) (see also Table 1). The decrease in effi- ciency de-rating factors for the textured devices is explained by

the excellent angular stability of textured Si SJ PV modules. The above discussed trend of the efficiency de-rating factors is apparent for all locations as shown in the ESI (see Table S1†). Finally, the validity of the conclusions drawn with regard to enhanced EY of textured perovskite/Si 2T tandem PV modules is investigated also for perovskite top absorber layers of various bandgaps. The ability of metal-halide perovskites to vary the bandgap by compositional engineering of the components/ elements of the crystal perovskite structure has led to a wide range of perovskite materials of PV quality. The details on the treatment of the electrical and optical parameters of the wide bandgap perovskite solar cells are reported in the ESI.† In Fig. 4, the maximum EY of the perovskite/Si 2T tandem PV modules is plotted for various bandgaps of the perovskite top solar cell (1.55–1.88 eV) as well as different locations. The Si SJ PV module reference, comprising the same architecture, namely, planar, double-side texture and rear texture, is shown for comparison.

Fig. 4(a) and (b) show the dependency of EY on perovskite

absorber layer thickness in the range of 0–750 nm for the perovskite/Si 2T tandem PV module architecture with the double-side texture (II) and planar front (I), respectively. Over- all, with increasing bandgap, the optimal thickness required for

Fig. 4 Role of perovskite bandgap: EY of the perovskite/Si 2T tandem PV modules with (a) double-side textured and (b) planar architecture for

Daggett (California) as a function of thickness of the perovskite layer and for various bandgaps of the perovskite absorber layer (EG¼ 1.55, 1.65,

1.72, 1.80, and 1.88 eV). Maximum EY of the perovskite/Si 2T tandem PV modules with a planar architecture, double-side texture, and rear texture for (c) Daggett (California) and with (d) a double-side texture for Daggett (California), Miami (Florida), and Portland (Oregon). achieving current matching and maximum EY increases, since the wavelength range of the irradiance spectra that can be harvested in the perovskite top solar cells decreases with increasing bandgap (see the indicated maxima in EY in Fig. 4(a) and (b)). The optimal thickness for the perovskite bandgaps of
1.80 eV and 1.88 eV is outside the simulated range and, thus, is cut off at 750 nm, which is already signicantly exceeding the thickness of any state-of-the-art high bandgap perovskite solar cell in the literature.
37,43 The general need for optimizing the architecture of perovskite/Si 2T tandem PV modules, i.e., adapting the perov- skite top absorber layer thickness, is apparent for each archi- tecture and perovskite bandgap (see Fig. 4(a) and (b)). However, for wide perovskite bandgaps ($1.72 eV) and the double-side textured perovskite/Si 2T tandem PV module architecture, the maximum in EY is signicantly broader with regard to the perovskite absorber layer thickness. Moreover, comparing the optimal thicknesses for different locations in this architecture, it is shown that the optimal thicknesses are similar for the locations of the most common climate conditions in the USA (see Fig. S14†). With regard to large-scale fabrication, the latter nding is very encouraging as it implies that custom optimi- zation of the architecture of perovskite/Si 2T tandem PV

modules is of lower relevance for double-side textured devices with a perovskite bandgap $1.7 eV. For the planar perovskite/Si 2T tandem PV module architecture, the maximum in EY becomes also broader with increasing perovskite bandgap, but this architecture does not provide the same robustness in EY against variations in the angle of incidence and the perovskite absorber layer thickness as discussed earlier (see Fig. 3). EY modelling for the design of perovskite/Si 2T tandem PV modules is highly relevant. When comparing the optimal thickness obtained for the maximum EY of the textured perovskite/Si 2T tandem PV module (see Fig. 4(a)) and the maximum PCE of the textured perovskite/Si 2T tandem PV module (see Fig. 2(b)), a very large difference is apparent even for a wide perovskite bandgap of 1.72 eV. Thus, despite the broad maxima in EY with regard to the perovskite absorber layer thickness, optimization of the layer stack of perovskite/Si 2T tandem PV modules exclusively based on STC will lead to signicantly mal-designed architectures with reduced power output. Finally, in accordance with the predictions from detailed balance theory, the maximum EY is determined to occur for perovskite bandgaps in the range 1.7–1.8 eV (see Fig. 4(c)). This optimal regime of bandgap is independent of whether the

perovskite/Si 2T tandem PV module exhibits a planar archi- tecture(I),adouble-sidetexture(II),orareartexture(III).The optimal bandgap is also independent of the climatic conditions of the location as shown for the perovskite/Si 2T tandem PV module with the double-side texture in Fig. 4(d). Thereby, this study conrms and underlines the importance of advancing stable perovskite absorber materials with bandgaps around 1.7–

1.8 eV for perovskite/Si tandem PV. Within recent years very signicant progress was demonstrated in this eld.
10,11,17,19 Therefore, the perovskite/Si 2T tandem PV modules with the rear texture (III) might be the economically favoured architec- ture, despite their moderately lower EY (see Fig. 3(a) and 4(c)).

### Conclusion and outlook

This work demonstrates that perovskite/Si 2T tandem PV modules exhibit a large potential to enhance the EY of the market- dominating crystalline Si PV. Even planar perovskite/Si 2T tandem PV modules show a relative enhancement in EY of 12–14% compared to the reference Si SJ PV module. Moreover, micron- scale light management textures as used today in Si PV can further enhance the EY of perovskite/Si 2T tandem PV modules. The relative enhancement in EY of 26–28% and 19–22% is shown for perovskite/Si 2T tandem PV modules with the double-side texture and the rear texture, respectively. In accordance with the predictions from detailed balance theory, the maximum EY is determined to occur for perovskite bandgaps in the range

1.7–1.8 eV. All these trends are independent of the climatic conditions of the geographic location. The perovskite/Si 2T tandem PV modules with the double side texture and a high bandgap ($1.72 eV) perovskite top solar cell exhibit a broad maximum in EY with respect to variations in the perovskite thickness as well as installation angle. As a consequence, for these devices the custom optimization of the architecture for each location is less important. However, the latter statement shall not be confused with the fact that the PCE determined under STC is not the optimal condition to design the architecture of perovskite/Si 2T tandem PV modules, as shown in this work. In summary, perovskite/Si 2T tandem PV modules with a wide bandgap (1.7–1.8 eV) and rear-side texture (III) as well as double-side texture (II) are clearly favoured. While the double-side texture provides the highest EY, depositing a high quality perovskite thin-lm top solar cell is likely a severe chal- lenge. Furthermore, the signicantly enhanced interface area will lead inevitably to higher recombination unless further progress is made in interface passivation. Therefore, rear-side textured perovskite/Si 2T tandem PV modules which show only moderately lower EY are an interesting alternative.
### Conflicts of interest

There are no conicts of interest to declare.

### Acknowledgements

The authors gratefully acknowledge nancial support of the Bundesministerium fur Bildung und Forschung (PRINTPERO, ¨ PEROSOL), the Initiating and Networking funding of the

Helmholtz Association (HYIG of Dr U.W. Paetzold; Recruitment Initiative of Prof. B.S. Richards; the Helmholtz Energy Materials Foundry (HEMF); PEROSEED; the European Union’s Horizon2020 Programme (ACTPHAST); and the Science and Technology of Nanostructures research Programme) and the Karlsruhe School of Optics & Photonics (KSOP).

### References

1 M. A. Green, A. Ho-Baillie and H. J. Snaith, Nat. Photonics, 2014, 8, 506–514. 2 S. Albrecht, M. Saliba, J. P. Correa Baena, F. Lang,

L. Kegelmann, M. Mews, L. Steier, A. Abate, J. Rappich,
L. Korte, R. Schlatmann, M. K. Nazeeruddin, A. Hagfeldt,
M. Gr¨atzel and B. Rech, Energy Environ. Sci., 2016, 9,81–88.
3D.P´erez-del-Rey, P. P. Boix, M. Sessolo, A. Hadipour and

H. J. Bolink, J. Phys. Chem. Lett., 2018, 1041–1046.
4 L. M. Pazos-Outon, M. Szumilo, R. Lamboll, J. M. Richter,

M. Crespo-quesada, M. Abdi-jalebi, H. J. Beeson,
M. Vru´cini´c, M. Alsari, H. J. Snaith, B. Ehrler, R. H. Friend and F. Deschler, Science, 2016, 351, 1430–1434.
5 S. D. Stranks, G. E. Eperon, G. Grancini, C. Menelaou,

M. J. P. Alcocer, T. Leijtens, L. M. Herz, A. Petrozza and
H. J. Snaith, Science, 2014, 342, 341–344.
6 A. Sadhanala, F. Deschler, T. H. Thomas, S. E. Dutton,

K. C. Goedel, F. C. Hanusch, M. L. Lai, U. Steiner, T. Bein,
P. Docampo, D. Cahen and R. H. Friend, J. Phys. Chem. Lett., 2014, 5, 2501–2505.
7P. L¨oper, B. Niesen, S.-J. Moon, S. Martin de Nicolas,

J. Holovsky, Z. Remes, M. Ledinsky, F.-J. Haug, J.-H. Yum,
S. De Wolf, C. Ballif, P. Loeper, B. Niesen, S.-J. Moon,
S. M. de Nicolas, J. Holovsky, Z. Remes, M. Ledinsky,
F.-J. Haug, J.-H. Yum, S. De Wolf and C. Ballif, IEEE J. Photovolt., 2014, 4, 1545–1551.
8 A. Richter, M. Hermle and S. W. Glunz, IEEE J. Photovolt., 2013, 3, 1184–1191. 9 A. De Vos, J. Phys. D: Appl. Phys., 1980, 13, 839–846. 10 T. Duong, Y. L. Wu, H. Shen, J. Peng, X. Fu, D. Jacobs,

E. C. Wang, T. C. Kho, K. C. Fong, M. Stocks, E. Franklin,
A. Blakers, N. Zin, K. McIntosh, W. Li, Y. B. Cheng,
T. P. White, K. Weber and K. Catchpole, Adv. Energy Mater., 2017, 7,1–11.
11 D. P. McMeekin, G. Sadoughi, W. Rehman, G. E. Eperon,

M. Saliba, M. T. H¨orantner, A. Haghighirad, N. Sakai,
L. Korte, B. Rech, M. B. Johnston, L. M. Herz and
H. J. Snaith, Science, 2016, 351, 151–155.
12 S. Albrecht and B. Rech, Nat. Energy, 2017, 2, 16196. 13 M. Jaysankar, M. Filipic, B. Zielinski, R. Schmager, W. Song,

W. Qiu, U. W. Paetzold, T. Aernouts, M. Debucquoy,
R. Gehlhaar and J. Poortmans, Energy Environ. Sci., 2018, 11, 1489–1498.
14 M. Jaysankar, W. Qiu, M. van Eerden, T. Aernouts,

R. Gehlhaar, M. Debucquoy, U. W. Paetzold and
J. Poortmans, Adv. Energy Mater., 2017, 7, 1602807.
15 J. Werner, C. H. Weng, A. Walter, L. Fesquet, J. P. Seif, S. De Wolf, B. Niesen and C. Ballif, J. Phys. Chem. Lett., 2016, 7, 161–166.

16 S. Albrecht, M. Saliba, J.-P. Correa-Baena, K. J¨ager, L. Korte,

A. Hagfeldt, M. Gr¨atzel and B. Rech, J. Opt., 2016, 18, 64012.
17 K. A. Bush, A. F. Palmstrom, Z. J. Yu, M. Boccard,

R. Cheacharoen, J. P. Mailoa, D. P. McMeekin,
R. L. Z. Hoye, C. D. Bailie, T. Leijtens, I. M. Peters,
M. C. Minichetti, N. Rolston, R. Prasanna, S. Soa,
D. Harwood, W. Ma, F. Moghadam, H. J. Snaith,
T. Buonassisi, Z. C. Holman, S. F. Bent and
M. D. McGehee, Nat. Energy, 2017, 2,1–7.
18 F. Sahli, J. Werner, B. a. Kamino, M. Br¨auninger,

R. Monnard, B. Paviet-Salomon, L. Barraud, L. Ding,
J. J. D. Leon, D. Sacchetto, G. Cattaneo, M. Boccard,
M. Despeisse, S. Nicolay, Q. Jeangros, B. Niesen and
C. Ballif, Nat. Mater., 2018, 17, 820–826.
19 Y. Wu, D. Yan, J. Peng, T. Duong, Y. Wan, S. P. Phang,

H. Shen, N. Wu, C. Barugkin, X. Fu, S. Surve, D. Grant,
D. Walter, T. P. White, K. R. Catchpole and K. J. Weber, Energy Environ. Sci., 2017, 10, 2472–2479.
20 B. W. Schneider, N. N. Lal, S. Baker-Finch and T. P. White, Opt. Express, 2014, 22, A1422. 21 M. H. Futscher and B. Ehrler, ACS Energy Lett., 2016, 1, 863–

868.
22 R. Santbergen, R. Mishima, T. Meguro, M. Hino, H. Uzu,

J. Blanker, K. Yamamoto and M. Zeman, Opt. Express, 2016, 24, A1288.
23 N. Tucher, O. H¨ohn, B. Bl¨asi and J. C. Goldschmidt, Proc. SPIE, 2018, 10688, 1068805. 24 S. Standard IEC 60904-3, Measurement Principles for Terrestrial PV Solar Devices with Reference Spectral Irradiance Data, International Electrotechnical Commission, Geneva,

2008.
25 P. Campbell and M. A. Green, J. Appl. Phys., 1987, 62, 243–

249.
26 A. Luque and J. C. Minano, ˜ Sol. Cells, 1991, 31, 237–258. 27 W. L. Bailey, M. G. Coleman, C. B. Harris and I. A. Lesk, Texture etching of silicon: method, US Pat., US4137123A, Motorola Solutions Inc, 1979.

28 K. Yoshikawa, H. Kawasaki, W. Yoshida, T. Irie, K. Konishi,

K. Nakano, T. Uto, D. Adachi, M. Kanematsu, H. Uzu and
K. Yamamoto, Nat. Energy, 2017, 2, 17032.
29 P. J. Holmes, The Electrochemistry of Semiconductors, Academic Press, Ltd., London, 1962. 30 H. Seidel, L. Csepregi, A. Heuberger and H. Baumg¨artel,

J. Electrochem. Soc., 1990, 137, 3612–3626.
31 U. W. Paetzold, R. Gehlhaar, J. Tait, W. Qiu, J. Bastos,

M. Debucquoy, M. Jaysankar, T. Aernouts and
J. Poortmans, in Light, Energy and the Environment, Optical Society of America, 2016.
32 M. Alonso-Abella, F. Chenlo, G. Nofuentes and M. Torres- Ram´ırez, Energy, 2014, 67, 435–443. 33 M. T. H¨orantner and H. Snaith, Energy Environ. Sci., 2017, 10, 1983–1993. 34 O. Dupr´e, B. Niesen, S. De Wolf and C. Ballif, J. Phys. Chem. Lett., 2018, 9, 446–458. 35 S. C. Baker-Finch and K. R. McIntosh, Prog. Photovoltaics, 2011, 19, 406–416. 36 K. R. McIntosh and S. C. Baker-Finch, in 38th IEEE Photovoltaic Specialists Conference, 2012, pp. 265–271. 37 X. Li, D. Q. Bi, C. Y. Yi, J. D. Decoppet, J. S. Luo,

S. M. Zakeeruddin, A. Hagfeldt and M. Gr¨atzel, Science, 2016, 353,58–62.
38 S. Wilcox and W. Marion, Renewable Energy, 2008, 51. 39 D. Redeld, Appl. Phys. Lett., 1974, 25, 647–648. 40 M. Filipiˇc, P. L¨oper, B. Niesen, S. De Wolf, J. Krˇc, C. Ballif and

M. Topiˇc, Opt. Express, 2015, 23, A263–A278.
41 J. Peng, Y. Wu, W. Ye, D. A. Jacobs, H. Shen, X. Fu, Y. Wan,

T. Duong, N. Wu, C. Barugkin, H. T. Nguyen, D. Zhong, J. Li,
T. Lu, Y. Liu, M. N. Lockrey, K. J. Weber, K. R. Catchpole and
T. P. White, Energy Environ. Sci., 2017, 10, 1792–1800.
42 M. C. Peel, B. L. Finlayson and T. A. McMahon, Hydrol. Earth Syst. Sci., 2007, 11, 1633–1644. 43 W. S. Yang, B.-W. Park, E. H. Jung, N. J. Jeon, Y. C. Kim,

D. U. Lee, S. S. Shin, J. Seo, E. K. Kim, J. H. Noh and S. Il Seok, Science, 2017, 356, 1376–1379.
