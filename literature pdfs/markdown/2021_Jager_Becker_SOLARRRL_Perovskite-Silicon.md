### <u>FULL PAPER</u>

www.solar-rrl.com

# Perovskite/Silicon Tandem Solar Cells: Effect of Luminescent Coupling and Bifaciality

## Klaus Jäger,* Peter Tillmann, Eugene A. Katz, and Christiane Becker

technologies and concepts are required to The power conversion efficiency of the market-dominating silicon photovoltaics increase the energy yield on limited areas. approaches its theoretical limit. Bifacial solar operation with harvesting additional One approach is using bifacial solar systems that not only utilize light, which light impinging on the module back and the perovskite/silicon tandem device falls onto the front side of the PV module, architecture are among the most promising approaches for further increasing the[3,4] but also light reach the back side, as energy yield from a limited area. Herein, the energy output of perovskite/silicon shown in Figure 1. Bifacial PV power tandem solar cells in monofacial and bifacial operation is calculated, for the first plants demonstrated > 20% enhanced time considering luminescent coupling (LC) between two sub-cells. For energy annual energy yield in comparison to a [5] monofacial power plant of a similar size. yield calculations, idealized solar cells are studied at both standard testing as well Modern silicon solar cell concepts with pas- as realistic weather conditions in combination with a detailed illumination model sivated emitter rear contact (PERx), hetero- for periodic solar panel arrays. Typical experimental photoluminescent quantum junction (SHJ), or integrated back contact yield values reveal that more than 50% of excess electron–hole pairs in the (IBC) enable bifacial solar cell operation perovskite top cell can be utilized by the silicon bottom cell by means of LC. As a at low additional cost. Due to these reasons, result, LC strongly relaxes the constraints on the top-cell bandgap in monolithic the International Technology Roadmap for Photovoltaics predicts nearly 70% market tandem devices. In combination with bifacial operation, the optimum perovskite bandgap shifts from 1.71 eV to the range 1.60–1.65 eV, where already high- quality perovskite materials exist. The results are very important for developing output from a PV system on limited area is optimal perovskite materials for tandem solar cells.

#### 1. Introduction

Monofacial silicon solar cells currently dominate the photovoltaic (PV) market. [1] Their practical efficiencies meanwhile approach the theoretical limit of around 29.4%, [2] such that innovative

Dr. K. Jäger, P. Tillmann, Prof. C. Becker Department Optics for Solar Energy Helmholtz-Zentrum Berlin für Materialien und Energie GmbH Albert-Einstein-Straße 16, Berlin 12489, Germany E-mail: klaus.jaeger@helmholtz-berlin.de Dr. K. Jäger, P. Tillmann Computational Nano Optics Zuse Institute Berlin Takustraße 7, Berlin 14195, Germany Prof. E. A. Katz Department of Solar Energy and Environmental Physics The Jacob Blaustein Institutes for Desert Research Ben-Gurion University of the Negev Sede Boqer Campus, Beersheba 8499000, Israel

The ORCID identification number(s) for the author(s) of this article can be found under [https://doi.org/10.1002/solr.202000628](https://doi.org/10.1002/solr.202000628).

© 2021 The Authors. Solar RRL published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

##### DOI: 10.1002/solr.202000628

[1] share for bifacial solar cells in 2030. A second method to increase the energy

the multi-junction approach where multi- ple solar cells with different bandgaps are stacked on top of each other. These dif- ferent materials exhibit complementary electronic bandgaps such that the high-energy photons of solar irradiation are absorbed by the high-bandgap materials on top, whereas the low-energy photons are absorbed by the lower bandgap material at the bottom. As a result, the excess photon energy losses are reduced and conversion efficiencies increase, significantly overcoming the efficiency limit of silicon single- junction solar cells. A currently widely investigated technology for large-scale applications is the combination of silicon and perovskite solar cells in a tandem device. [6] High efficiencies, a tunable bandgap, external photoluminescent quantum yields up to 10% [7] and low- cost fabrication processes make perovskites an attractive tandem partner for established silicon PVs. The current record efficien- [8] cies for perovskite/silicon tandem solar cells are 29.15% [9] for monolithic two-terminal (2 T) and 28.2% for stacked four- terminal (4 T) devices, respectively, bearing the potential [10] for power conversion efficiencies (PCEs) as high as ≈ 44% assum- ing radiative recombination the only recombination channel and standard test conditions (STC), i.e., 25 C temperature and 1000 W m 2 solar irradiance with AM1.5 g spectral distribu- tion. [11] The monolithic tandem configuration has (among others) the advantage of requiring only two external contacts and one maximum power point (MPP) tracker, enabling module- related costs comparable to single-junction devices. [12] Under STC, the theoretical power output of silicon-based monolithic tandem solar cells, however, reveals a sharp maximum at a

© 2021 The Authors. Solar RRL published by Wiley-VCH GmbH Sol. RRL 2021, 5, 2000628 2000628 (1 of 9)

2367198x, 2021, 3, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/solr.202000628](https://onlinelibrary.wiley.com/doi/10.1002/solr.202000628) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

(a)
(b)
Figure 1. Illustrating the illumination components reaching a bifacial solar

module in a large PV field: both the front and back sides can be illuminated by direct sunlight, diffuse skylight, and light from the ground, which can originating from direct sunlight or diffuse skylight. The PVs field is char- acterized by the module length l, height of the modules above the ground h, module tilt angle θm, distance between rows of modules d, and albedo of the ground A. [29]

top-cell bandgap around 1.71 eV, limiting the choice of available perovskite top cell materials. The reason for the sharp optimum is the current matching requirement in a monolithic series- connected tandem device, i.e., the top cell bandgap has to be tuned such that the numbers of generated electrons are the same for the top cell and the bottom cell. However, perovskites with bandgaps above 1.7 eV often suffer from low electronic quality resulting in reduced solar-cell efficiencies. [13]

Recently, bifacial perovskite/silicon tandem solar cells were extensively investigated. [14–18] In particular, Onno et al. found that the range of appropriate top-cell bandgaps broadens in a bifa- cial tandem-cell configuration. [15] This is in line with thermody- namic consideration by Khan et al. [19] Additional photons absorbed in the silicon bottom cell from rear-side illumination allow for a lower bandgap of the (perovskite) top cell at current- matching conditions. One aspect of perovskite-based tandem PV operation has not been considered so far: luminescent (or radiative) coupling between the different subcells in the device, i.e., the reabsorption of luminescent photons emitted by the high-bandgap top cell in the low-bandgap bottom cell. This effect is well-known in multi-junction solar cells based on III–V semiconductors where luminecent-coupling efficiencies above 30% were reported. [20]

Already in 2002, Brown and Green identified luminescent cou- pling (LC) as a means to reduce spectral mismatch in 2T tandem solar cells. [21] Although the effect of LC is negligible at current- matching conditions, a considerable positive effect appears in noncurrent-matched, bottom-cell limited devices. [22–25] Similar to bifacial cell operation LC, i.e., the reabsorption of luminescent photons emitted by the high-bandgap cell in the low-bandgap cell, results in more photons absorbed in the silicon bottom cell, as shown in Figure 2a. To the best of our knowledge, LC has not been investigated experimentally for perovskite-based multi- junction solar cells yet. In this study, we theoretically investigate how bifacial illumi- nation and LC affect the performance of perovskite/silicon tan- dem solar cells. We use idealized solar-cell models for these calculations: Shockley–Queisser’s (SQ) detailed balance limit [26]

for the perovskite top cell and the Richter limit [2] for the silicon

Figure 2. a) Illustrating LC in a perovskite/silicon tandem solar cell. A pho-

ton, which is generated in the perovskite top cell via radiative recombina- tion can 1) either leave the perovskite cell if its direction is within the escape cone, or 2) it undergoes total internal reflection and is redirected downward such that it can enter the silicon cell, just as 3) a photon that is emitted into the lower hemisphere. More details can be found in Section S3, Supporting Information. b) An example for J–V curves of a bottom-cell limited tandem cell (green) and the perovskite (brown) and silicon (blue) subcells illuminated under STC. Here, the perovskite is simulated with a bandgap of 1.6 eV and generates a higher photocurrent density Jph;pero than the silicon subcell with Jph;Si. At the MPP of the tandem cell, signifi- cantly less current density is extracted from the perovskite cell than gen- erated. The excess current density Jrec;perocan be reutilized via LC to increase the photocurrent density of the silicon subcell.

bottom cell, which also incorporates Auger recombination. For the perovskite cell operation under one Sun, Auger recombination is negligible. [27] Using these models, we first assess how illumina- tion from the back side and LC affect the tandem-cell performance under STCs. Then, we use optical simulations [28] to estimate how much of light from radiative recombination in the perovskite leaves the cell toward the Sun in a single-junction cell configura- tion and how much will reach the silicon subcell in a tandem stack. This allows us to relate measured external quantum photolumi- nescence efficiency in a single-junction perovskite cell to the rea- sonable internal quantum efficiency, and subsequently to evaluate which range of luminescent-coupling efficiencies is realistic in tandem devices. Finally, we estimate the energy yield using weather data from a climatic zone with high diffuse illumination ratio. For this, we apply a detailed illumination model, which takes direct sunlight, diffuse skylight, shadowing by other modules and reflection from the ground into consideration. [29] We finally

discuss how all the realistic deviations from STCs considered in this study—1) bifacial irradiation, 2) LC, and 3) weather conditions with high diffuse illumination ratio—influence the constraints for the perovskite top cell bandgap.

#### 2. Modeling Details

2.1. Electrical Solar Cell Model

|J ðV Þ¼e|AðλÞΦ|ðλÞdλ þ e|AðλÞΦ|
|---|---|---|---|
|ph;Si pero|λ LC ph;pero|f pero|0 pero|
 To calculate the current density–voltage ( J–V) characteristic of the PV modules, the irradiance values on the front and back sides are used as input for the electrical model. In this article, we use highly idealized solar cell models: For the perovskite top cell, we assume that all photons with energy higher than the cell bandgap are absorbed and every absorbed photon generates one electron–hole pair. Hence, the maximum achievable photocurrent density is given by Z
λ pero J ph;pero¼ e ΦfðλÞdλ (1) 0

where e is the elementary charge, Φfis the photon flux reaching the module at the front, and λperois the wavelength correspond- ing to the perovskite bandgap. In a monolithic tandem device, this value is only achieved in case of a limiting top cell, i.e., less or equal photons absorbed in the perovskite than in the silicon. The J–V characteristic is calculated according to the SQ limit, [26]

where only radiative recombination is considered. In the SQ limit, both external (ELQE) and internal (ILQE) luminescence quantum efficiencies are equal to 100%. The former is the num- ber of photons emitted into free space relative to the number of electron–hole pairs generated by light absorption in a solar cell. The latter is a ratio between the number of electron–hole pairs recombined radiatively to the entire number of the recombined pairs. The SQ limit is briefly summarized in Section S1, Supporting Information. For the silicon bottom cell, the perovskite top-cell acts as a fil- ter for the short wavelengths up to the perovskite bandgap. However, the perovskite cell also may emit light, which can be utilized by the bottom cell via LC, which is discussed later. In addition, Auger recombination must be considered for a sili- con cell. We implement this using an idealized model by Richter et al.; [2] the details are given in the Section S2, Supporting Information. In a high-end solar cell made of a direct bandgap semiconduc- tor, a significant fraction of the absorbed photons, which are not extracted as electrical current, will be re-emitted as light via radi- ative recombination. An electrically independent solar cell oper- ated at MPP only has a small recombination current because almost all charge carriers are extracted. However, in a 2 T tandem

|¼ J P|½V ðJ|ð J|
|---|---|---|
|cell mpp|cell Si rec;Si J cell|pero rec;pero|

cell, where the top and bottom cells are electrically connected in series, the same current density flows through bottom and top cell. If the generated photocurrent density and the extracted cur- rent density deviate strongly from each other, as shown in

Figure 2b, significant recombination will be present in the top

cell. If the recombination is radiative, the re-emitted light from the top cell can be absorbed and utilized by the bottom cell, which is known as LC. In perovskite/silicon tandem solar cells, we only need to consider light emitted by the perovskite cell, which can

be absorbed by the silicon bottom. The silicon cell itself will hardly emit light because of the indirect bandgap of silicon. Furthermore, the energy of the emitted photons would be close to the silicon bandgap and hence cannot be absorbed by perov- skite with a larger bandgap than silicon. For the maximum achievable short-circuit current density in the Si bottom cell, we find Z λ Z λ Si Si ph;Si pero f bðλÞdλ pero (2) þ η ½ J J ðV Þ

with the absorption in silicon AðλÞ, which we calculate accord- ingtotheTiedje–Yablonovitch limit for a silicon wafer thick- ness of 300 μm as described in Section S2, Supporting Information. JperoðVperoÞ is the current density at the working point of the perovskite cell. The term ½Jph;peroJperoðVperoÞ corresponds to excess electron–hole pairs generated in the perovskite top cell, which cannot be extracted from the monolithic tandem device, e.g., due to a limiting bottom cell. These excess electron–hole pairs can recombine radiatively and be reabsorbed by the silicon with ηLCbeing the efficiency of this LC. Here, we also accounted for light that hits the solar cell at the back, Φb. For monofacial cells, we have Φb≡ 0. Furthermore, λSiis the wavelength corresponding to the silicon bandgap. More details about LC are given in the Section S3, Supporting Information. As we assume zero series resistance and infinitely large shunt resistance of the cells, for both subcells the electric current density J can be directly calculated from the photocurrent density Jphand the voltage-dependent recombination current density Jrec

##### J¼JphJrecðV Þ (3)

where details about Jrecfor the perovskite and silicon subcells are given in Section S1 and S2, Supporting Information, respectively. For 2 T cells, where the same current density flows through both cells, we have

J cell¼ Jph;SiJrec;SiðVSiÞ¼Jph;peroJrec;peroðVperoÞ (4)

We calculate the J–V characteristic of the tandem solar cell by numerically inverting the expressions Jrec;SiðVSiÞ and J rec;peroðVperoÞ such that we have functions of Jrec;peroand J rec;Si, respectively. From the J–V curve, the output power density of the cell can be directly calculated as

ÞþV Þ

(5)
P ¼ maxðP Þ cell

Tandem solar cells can also be built in 4 T configuration, where the two subcells are electrically independent and can operate at their individual MPPs

P ¼ max½ J ⋅ V ðJ Þ þ max½ J ⋅ V ðJ Þ (6) mpp J Si Si rec;Si J pero pero rec;pero Si pero

#### 3. Results and Discussion

3.1. Tandem-Cell Operation Under Standard Testing Conditions
Figure 3 shows the effect of the top cell bandgap on the maxi-
 mum output power density of a 2 T tandem solar cell for various levels of a) backside illumination and b) LC under standard test- ing conditions. Without either backside illumination or LC, the optimal bandgap of the perovskite cell for maximum power
(a)
(c)
(b)
(d)
2.2. Optical Model To estimate the effect of LC in realistic perovskite-tandem solar cells, we apply optical modeling. In this article, we use the MATLAB-based tool GenPro4, which can calculate the absorption profile in solar-cell structures using the net radia- tion method.
[28] This tool treats light coherently in thin layers but incoherently in thick layers. Because GenPro4 only can treat light that falls onto a layer stack from the exterior, we split the simulations in two: one simulation treating the layer stack above the perovskite layer, the other layer stack treating the layers below. Details on these calculations are given in Section S4, Supporting Information.

2.3. Energy Yield Calculation We calculate the overall energy yield for different scenarios using a simulation approach that combines several sub-models. For calculating the spectral irradiance at the front and back sides of a solar module in a big PV field, we use a recently developed illumination model.
[29,30] The PV field is considered so large that boundary effects can be neglected. As schemati- cally illustrated in Figure 1, the illumination model considers four components reaching the module front: direct sunlight, diffuse skylight, diffuse light from the ground, which originates from direct sunlight reaching the ground and diffuse skylight reaching the ground. Furthermore, the same four components must be considered reaching the back-side of the module. Hence the illumination model considers eight components in total. The illumination model uses the following input parame- ters: first, the geometrical parameters of the PV field, which are shown in Figure 1: module length l,mountingheighth, module spacing d,andtiltangleθm. Second, the albedo (i.e., the reflectivity) of the ground, which is highly dependent on the material properties of the ground. Although grass typically exhibits albedo values around 20%, gray and white gravel have albedo values of 30% and 50%, respectively, and snow reaches albedo values up 70%. [31] In this work, we assume the albedo to be independent of the wavelength with A ¼ 30%, which is a rather conservative estimate with realistic room for improve- ment. Third, the (spectral) direct normal incidence (DNI) and the diffuse horizontal incidence (DHI) for different instantsoftime.WeretrievethesedatafromtheNational Solar Radiation Data Base (NSRDB) operated by NREL. [32]

They publish hourly spectral direct and diffuse irradiance for a typical meteorological year (TMY). With the spectral irradiance on the front and back sides, we can calculate the generated photocurrent densities in the top and bottom cells using Equation (1) and (2). We calculate the full J–V characteristics for every hour in the TMY data set and take the appropriate maximum to get the maximum power output of the cell according to Equation (S14) and (S15), Supporting Information. By integrating over all hourly data points in the data set for one year, we obtain the annual energy yield.

Figure 3. Maximum output power density of 2 T tandem solar cells as

function of the top-cell bandgap for different levels of a) backside illumination and b) LC efficiencies under STCs. The insets show the optimal top-cell bandgap for different levels of c) backside illumination and d) LC efficiencies under STCs. The diamonds mark the ideal bandgap with maximum power output; the arrowheads and the dash marks span the ranges where at least 99% and 95% of the maximum output power density are achieved. Note: For the graph with varying backside illumination, no LC is assumed, and for varying LC efficiencies, no backside illumination is present. The bottom cell bandgap is 1.12 eV in all cases. For bifacial solar cells we use the output power density instead of the power conversion efficiency, because the power density of the light illuminating the solar cell, depends on the assumed albedo.

output density is 1.71 eV, where the same current densities are generated in the top and bottom cells. For other top-cell bandgaps, the generated current densities differ from each other. Only the lower current density can flow through the solar cell, while the excess current density is lost, which reduces the overall PCE of the tandem solar cell. For a silicon-based tandem solar cell, the bandgap of the top cell absorber is critical to achieve current matching between the subcells. For a top-cell bandgap higher than the optimum, the current density generated in the top cell is below that generated in the bottom cell; the tandem cell is said to be “top-cell limited”. For a top-cell bandgap lower than the optimum, the bottom-cell current density is lower; the cell is “bottom-cell limited”. With higher levels of backside illumination, as shown in

Figure 3a, the maximum power output density increases and

the optimum top-cell bandgap shifts toward lower bandgaps. The backside illumination is exclusively absorbed in the bottom cell and cannot reach the top cell, leading to more generated electron–hole pairs in the bottom-cell. To match the photocur- rent densities between the two subcells, the top-cell bandgap needs to be lowered, such that it can absorb more light. For top-cell bandgaps larger than 1.71 eV, increased back-side illumi- nation hardly affects the overall output power density, because here the tandem device is top-cell limited and the additional photocurrent generated in the bottom cell cannot be utilized. As shown in Figure 3b, increasing the LC efficiency does not shift the position and height of the maximum output power den- sity; however, the power output is increased for bandgaps below the optimum. For top-cell bandgaps above the optimum, LC does not affect the performance, because here the cells are top-cell lim- ited and the excess current in the bottom cell cannot be utilized for LC.

Figure 3c,d summarize these results. For a given scenario of

backside illumination or LC, the optimal bandgap and the range of 99% and 95% of the maximum output power density are shown. With increasing backside illumination, the optimal top-cell bandgap shifts to lower values, while sensitivity is unchanged. For LC, the optimal bandgap remains unchanged, but the 99%- and 95% bands broaden toward lower bandgaps.

3.2. Estimating Reasonable Values of Luminescent-Coupling Efficiency Now, as we have studied how LC can improve the performance of bottom-cell limited tandem solar cells (see Figure 3b,d), we inves- tigate, which LC efficiencies are realistic in perovskite/silicon tandem solar cells from an optical point of view. Increasing the PCE of solar cells toward the theoretical limit can be realized by improving the ELQE of the cell in open circuit (OC), or in the other words—by suppressing non-radiative recombination.
[33,34] Despite the direct bandgap of metal halide perovskite semiconductors, initially reported ELQE values for perovskite solar cells were extremely low (≈ 10 4 %). [35] Then, tremendous growth was demonstrated for perovskite solar cells reaching an ELQE of 0.5%. [36] which is equal to the record for silicon cells. [37] Recently, Liu et al. realized a single-junction perovskite solar cell with 8.4% ELQE [7]. Note that record ELQE values of the champion GaAs cells do not exceed 25%, [38,39] even

though ILQE values of 99.7% have experimentally been shown for GaAs devices. [40]

As a first step to estimate the LC efficiency for a cell with the experimentally measured 8.4% ELQE, we calculate the fraction E int tof light generated in the perovskite layer, which leaves the solar cell structure, using the optical simulation tool GenPro4. We assume a perovskite thickness of 400 nm and an emission wavelength of 795 nm, which corresponds to the bandgap of the perovskite methylammonium lead iodide (MAPbI3) of 1.56 eV, in accordance with the device architecture used by Liu et al. [7]

As shown in the Section S4, Supporting Information, we revealed E int t¼ 7.8% for this configuration, which is indepen- dent of the emission depths in the perovskite layer. The rest of the generated light cannot leave the solar cell structure, because it either radiates in directions outside the emission cone, which has an opening angle of 23.8 for MAPbI3 at 795 nm, [41] or it is absorbed before it can leave the solar cell. The experimental ELQE (8.4%) being larger than the numerical value E int t¼ 7.8% shows that a high ILQE was achieved. For semiconductors with high ILQE, photon recycling, [42]

i.e., the reabsorption of previ-
ously emitted photons within the perovskite, can increase the ELQE to values higher than what would be expected from the optical simulations, where photon recycling was neglected. [43]

An experimental proof of internal photon recycling in perovskite solar cells was given by Pazos–Outón et al. [44] Furthermore, Braly et al. demonstrated perovskite films with 90% ILQE. [45]

We can estimate the ILQE using a simple model for a cell in open-circuit condition where the charge carriers created by the external light source can undergo a chain of emission and reabsorption events. In a first step, the charge carriers can either recombine radiatively with probability ILQE or nonradiatively with probability ð1 ILQEÞ. In the next step, the emitted photons can either leave the cell with proba- bility E int t, be absorbed parasitically in nonactive areas with probability Aparaor reabsorbed in the perovskite with probability Apero¼ 1 E int tApara. Apero, E int t,andAparacan be extracted from the optical simulations described in the Supporting InformationI. The reabsorbed light can undergo the same pro- cesses as the directly absorbed light from an external light source. This chain of events can be represented as a geometric series to calculate the ELQE

ELQE ¼ E int t⋅ ILQE½1 þ Apero⋅ ILQE þðApero⋅ ILQEÞ² þ ::: E int t⋅ ILQE

(7)
¼ 1 A ⋅ ILQE pero

This function can be inverted to retrieve ILQE

int ~ 1 <u>Et</u> ILQE ¼ ELQE þ A pero(8)

Using Equation (8), we estimate the ILQE of the best cell from Liu et al. [7] to be around 65%. This is in line with simulations from Cho et al. on perovskite-based light emitting diodes, where they calculate that an ILQE of 60% is sufficient to reach an ELQE equal to the purely optical expectation if photon recycling is considered. [43]

Figure 4b shows the perovskite/silicon tandem solar cell struc-

ture, which we used to study coupling of emitted light by the

perovskite layer into silicon. This structure is based on recent

||max||int||
|---|---|---|---|---|
||LC||t|Si|
|max LC|Si||||
||pero||||
||max||||
||LC||Si|pero|
|||max|||
|||LC|||

high-end tandem solar cells, [46,47] but in contrast to them, we used MAPbI3 as perovskite material to be consistent with the single-junction results discussed earlier. For an emission wave- length of 795 nm, 76% of the light generated in perovskite reaches the silicon layer, as shown in Figure 4b. This value is almost independent from the emission depths in the perovskite layer, as shown in the Section S4, Supporting Information. Only 4% of the generated light leave the solar cell structure into air and 17% are reabsorbed in the perovskite layer, which can contribute to photon recycling. More details of the optical tandem-cell sim- ulations are shown in Figure S2, Supporting Information.

(a) (b)
We can estimate an upper bound for the luminescence cou- pling efficiency η by replacing E with A in Equation (7)

η ¼ A ⋅ ILQE

(9)
1 A ⋅ ILQE

For estimating η, we use the values for 150 nm emission depths, shown in Figure 4b: A ¼ 0.763 and A ¼ 0.171. Assuming ILQE ¼ 65%, just as for the single-junction cell dis- cussed earlier, we find η ≈ 56%. However, it should be noted that Liu et al. measured the ELQE with an illumination of one sun without charge-carrier extraction (open-circuit condition, in which all photo-generated carriers should recombine). When charge carriers are extracted in solar cell operation, the ratio of radiative to nonradiative recombination might change [48] considerably. Further research is needed to assess realistic radiative efficiencies at low recombination currents. In any case, we provide a positive answer on the fundamental question: a sig- nificant fraction of light emitted by the perovskite sub-cell can reach the silicon wafer. This can change a paradigm in develop- ing optimal perovskite materials for efficient tandem solar cells.

3.3. Energy Yield Under Realistic Weather Conditions Under realistic conditions, the illumination on a solar module in a large PV field consisting of periodic rows of solar panels will significantly differ from standard testing conditions. The spectral distribution and irradiance of light in the outdoors is constantly changing and the illumination on the backside is highly depen- dent on the layout of the PV field. Figure 5 shows the result of energy-yield calculations for bifacial and monofacial tandem solar modules for different bandgaps and varying levels of albedo in Seattle, USA and compares the performance of 2 T and 4 T solar cells. The 4 T cells show only a small dependence on the top-cell bandgap with the optimum at the upper limit of the
(b)
Figure 4. a) The tandem solar cell structure used for estimating the frac-

tion of photons, which are generated in the perovskite layer and reach the silicon wafer. The structure is based on recent high-end perovskite/silicon tandem solar cells. [46,47] The dotted line indicates the middle of the perov- skite layer (150 nm depths). In our calculations, we assumed the light emission from this depth. b) Relative distribution of photons with 795 nm wavelength, which are isotropically emitted in the center of the perovskite layer. Although around 76% are absorbed by the silicon wafer, around 17% are reabsorbed by the emitting perovskite layer. Only ≈4% leave the solar cell structure.

(a)
<u>(c)</u>
simulated with albedo A ¼ 0%.

Figure 5. Energy yield for bifacial and monofacial tandem power plants simulated for Seattle with a) 2 T and b) 4 T cells connection for different albedo

values. The inset c) shows the optimal top-cell bandgap for different levels of albedo. The diamonds mark the ideal bandgap with maximum energy yield; the arrowheads and the dash marks span the ranges where at least 99% and 95% of the maximum energy yield is achieved. All simulations were per- formed with a module distance d ¼ 8 m and mounting height of h ¼ 0.5 m. The tilt angle was optimized for every data point. Monofacial tandems are

Table 1. Results from energy-yield calculations of 2 T tandem cells for

(a)
different albedo scenarios using average meteorological year data for

|different albedo scenarios using average|||meteorological|year data for||
|---|---|---|---|---|---|
|Seattle with module height h ¼ 0.5 m and module distance d ¼ 8m.||||||
|Type|Albedo [%]|Bifacial gain [%]|Opt. bandgap [eV]|Energy yield [kWh m|a]|
|Monofacial|0|–|1.74|543||
|Bifacial|10|5.5|1.70|562||
||30|12.7|1.66|584||
||50|19.7|1.64|606||
||70|27.1|1.59|628||
|“Bifacial Gain” denotes the gain in irradiance.|100|37.4|1.54|664||

a)
2 1

(b) (c)
a) simulated range (1.8 eV) and a monotonic decrease toward
1.5 eV. Increasing the albedo increases the energy yield but leaves character of the bandgap dependence unchanged. In contrast, the 2 T cells are strongly affected by changing the top-cell bandgap. Similar to the results for STC (Figure 3a), there is a well-defined maximum for the bandgap with reduced energy yield for higher or lower values. The ideal top cell bandgap for monofacial cells shifts from of 1.71 eV for STC to 1.74 eV for Seattle. With increasing albedo, the optimal top-cell bandgap shifts to lower values. The additional light impinging onto the backside is exclusively absorbed by the bottom cell. Reducing the bandgap of the top cell will increase their photocurrent density at the cost of the bottom cell. Thus, the two subcells can be made current- matched again by reducing the top-cell bandgap.
Table 1 summarizes the results from the energy-yield calcula-
 tions for PV modules with 2 T tandem cells for different albedo values. For a realistic albedo of A ¼ 30% corresponding to gray cement, [49] the optimal bandgap shows a shift of 0.08 eV with respect to a monofacial cell. In this scenario, the energy yield is increased by 7.5%, which is significantly smaller than the 12.7% gain of irradiance. One reason for the increase in energy yield being smaller than the increase in irradiance is that light reaching the back side can only be utilized with the single-junction PCE of the bottom cell. Furthermore, for 2 T tandem solar cells decreas- ing the top-cell bandgap to ensure current matching reduces the overall open-circuit voltage and hence the PCE. However, considering the electronic material quality of state- of-the-art perovskites,
[13] the effect of bandgap-shift might be rel- evant. Although in principle organic/inorganic perovskites can be fabricated with continuously tunable bandgaps, [13,50] not all bandgap-materials can be fabricated with the same electronic quality. Fabricating high-quality perovskite semiconductors with bandgaps in the range of 1.70–1.75 eV is still a very challenging task and previous results show higher quality semiconductors in the region of 1.60–1.65 eV. [12]

Operation of perovskite/silicon tandem solar cells in bifacial configuration allows to utilize 1.60–1.65 eV bandgap perovskites for optimal performance. This enables using current high-quality perovskite absorber layers in the tandem device.

Figure 6 shows the effect of the top-cell bandgap on the annual

energy yield for mono- and bifacial 2 T tandem PV modules simulated for Seattle, USA, with various levels of LC. With an

Figure 6. a) Annual energy yield for mono- and bifacial 2 T perovskite/

silicon tandem solar cell modules simulated for Seattle with various levels of LC. The subfigures shows the optimal top-cell bandgap for different lev- els of LC of b) bifacial and c) monofacial tandem cells. The diamonds mark the ideal bandgap with maximum energy yield; the arrowheads and the dash marks span the ranges where at least 99% and 95% of the maximum energy yield is achieved. All simulations were performed with a module distance d ¼ 8 m and d ¼ 0.5 m mounting height. Bifacial operation is cal- culated with albedo A ¼ 30%. The module tilt angle θmwas optimized for every data point.

increasing LC efficiency, the energy yield becomes more and more independent from the bandgap of the top cell. Also, the maximum energy yield increases slightly and shifts a bit toward lower bandgaps. As the spectral distribution of outdoor illumina- tion changes with time, there will always be situations where the top or bottom cells generate different photocurrent densities. Therefore, the optimal top-cell bandgap for outdoor performance will always be a compromise, which delivers the best balance over time. [51] With increasing LC efficiency, the losses from periods, where the cell is bottom-cell limited, will become smaller, while losses from top-cell limitation are not affected. [52] This explains the shift of the optimal bandgap to lower values, where the overall absorption in the top cell is increased. As an example, the energy yield of perovskite/silicon tandem solar cells with 1.64 eV bandgap triple-cation perovskite top cell is found to increase by 21.5% when additionally considering a LC efficiency of 30% and bifacial operation on a 30% reflective ground.

#### Conflict of Interest

The authors declare no conflict of interest.

#### Keywords

energy yields, luminescent coupling, perovskite/silicon tandem solar cells

Received: October 7, 2020 Revised: December 4, 2020 Published online: December 12, 2020

4 T tandem solar cells barely show any performance improve- ment because of LC, as both subcells are operated individually at their MPP, where only very little radiative recombination is present.

#### 4. Conclusion

In conclusion, we calculated the energy yield of perovskite/ silicon tandem solar cells considering LC between the two sub-cells and bifacial illumination of the device. To do so, we first studied idealized solar cells using the SQ limit and Richter’s limit for the perovskite and the silicon sub-cells, respectively. We found that additional backside illumination around 10–20% is sufficient to shift the optimum perovskite top-cell bandgap in 2 T tandem solar cells from 1.71 eV to the 1.60–1.64 eV range. We further found that LC can strongly reduce the current-mismatch if the tandem solar cell is bottom- cell limited. As a second step, we performed optical simulations to evaluate the relevance of LC for perovskite/silicon tandem solar cells. On the basis of experimental photoluminescent quantum yield val- ues, we found that more than 50% of excess electron–hole pairs generated in the perovskite top cell can be reused by the silicon bottom cell. Particularly for configurations with perovskite top- cell bandgaps below the current matching optimum, this signifi- cantly enhances the energy yield. Finally, we performed energy-yield calculations based on typi- cal meteorological year (TMY3) weather data of Seattle, USA, and applied an illumination model considering the spectral irradi- ance at the front and back sides of a solar module in a big PV field. In agreement with the calculations using standard testing conditions, we found that the operation of perovskite/silicon tandem solar cells in bifacial configuration allows to utilize

1.60–1.65 eV bandgap perovskites for optimal performance and LC further minimizes the impact of current-mismatch in case of (silicon) bottom-cell limited devices, i.e., less photons absorbed in the silicon than in the perovskite absorber layer. The results are very important for developing the optimum perovskite material for tandem solar cells.
#### Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

#### Acknowledgements

K.J. and P.T. contributed equally to this work. P.T. thanks the Helmholtz Einstein International Berlin Research School in Data Science (HEIBRiDS) for funding. The authors acknowledge the support from the SNaPSHoTs project in the framework of the German–Israeli bilateral R&D cooperation in the field of applied nanotechnology (grant no. 01IO1806) funded by the German Federal Ministry for Education and Research (BMBF) and the National Technological Innovation Authority of the State of Israel. The results were obtained at the Berlin Joint Lab for Optical Simulations for Energy Research (BerOSE) and the Helmholtz Excellence Cluster SOLARMATH of Helmholtz-Zentrum Berlin für Materialien und Energie, Zuse Institute Berlin and Freie Universität Berlin. Open access funding enabled and organized by Projekt DEAL.
[1] ITRPV, 11th edition of the international technology roadmap photo- voltaics, Technical report, VDMA, 2020, [https://itrpv.vdma.org](https://itrpv.vdma.org) (accessed: August 2020). [2] A. Richter, M. Hermle, S. W. Glunz, IEEE J. Photovolt. 2013, 3, 1184. [3] R. Kopecek, J. Libal, Nat. Energy 2018, 3, 443. [4] T. S. Liang, M. Pravettoni, C. Deline, J. S. Stein, R. Kopecek,

J. P. Singh, W. Luo, Y. Wang, A. G. Aberle, Y. S. Khoo, Energy Environ. Sci. 2019, 12, 116.
[5] N. Ishikawa, S. Nishiyama, presented at 3rd Bifi PV Workshop, Miyazaki, Japan, September 2016. [6] J. Werner, B. Niesen, C. Ballif, Adv. Mater. Interfaces 2018, 5, 1700731. [7] Z. Liu, L. Krückemeier, B. Krogmeier, B. Klingebiel, J. A. Márquez,

S. Levcenko, S. Öz, S. Mathur, U. Rau, T. Unold, T. Kirchartz, ACS Energy Letters 2019, 4, 110.
[8] A. Al-Ashouri, E. Köhnen, B. Li, A. Magomedov, H. Hempel,

P. Caprioglio, J. A. Márquez, A. B. M. Vilches, E. Kasparavicius,
J. A. Smith, N. Phung, D. Menzel, M. Grischek, L. Kegelmann,
D. Skroblin, C. Gollwitzer, T. Malinauskas, M. Jošt, G. Matic,ˇ
B. Rech, R. Schlatmann, M. Topic,ˇ L. Korte, A. Abate,
B. Stannowski, D. Neher, M. Stolterfoht, T. Unold, V. Getautis,
S. Albrecht, Science 2020, 370, 1300.
[9] B. Chen, S.-W. Baek, Y. Hou, E. Aydin, M. D. Bastiani, B. Scheffel,

A. Proppe, Z. Huang, M. Wei, Y.-K. Wang, E.-H. Jung, T. G. Allen,
E. V. Kerschaver, F. P. G. de Arquer, M. I. Saidaminov,
S. Hoogland, S. D. Wolf, E. H. Sargent, Nat. Commun. 2020, 11, 1257.
[10] T. Leijtens, K. A. Bush, R. Prasanna, M. D. McGehee, Nat. Energy 2018, 3, 828. [11] IEC:60904-3: Photovoltaic devices – Part 3: Measurement principles for terrestrial photovoltaic (PV) solar devices with reference spectral irradiance data, 2008. [12] M. Jošt, L. Kegelmann, L. Korte, S. Albrecht, Adv. Energy Mater. 2020, 1904102. [13] E. L. Unger, L. Kegelmann, K. Suchan, D. Sörell, L. Korte, S. Albrecht,

J. Mater. Chem.A 2017, 5, 11401.
[14] R. Schmager, M. Langenhorst, J. Lehr, U. Lemmer, B. S. Richards,

U. W. Paetzold, Opt. Express 2019, 27, A507.
[15] A. Onno, N. Rodkey, A. Asgharzadeh, S. Manzoor, Z. J. Yu, F. Toor,

Z. C. Holman, Joule 2020, 4, 580.
[16] H. Imran, I. Durrani, M. Kamran, T. M. Abdolkader, M. Faryad,

N. Z. Butt, IEEE J. Photovolt. 2018, 8, 1222.
[17] O. Dupre, A. Tuomiranta, Q. Jeangros, M. Boccard, P.-J. Alet, C. Ballif, IEEE J. Photovolt. 2020, 10, 714. [18] R. Asadpour, R. V. K. Chavali, M. Ryyan Khan, M. A. Alam, Appl. Phys. Lett. 2015, 106, 243902. [19] M. Ryyan Khan, M. A. Alam, Appl. Phys. Lett. 2015, 107, 223502. [20] A. W. Walker, O. Höhn, D. N. Micha, L. Wagner, H. Helmers,

A. W. Bett, F. Dimroth, J. Photon. Energy 2015, 5, 053087.

[21] A. Brown, M. Green, in Conf. Record of the Twenty-Ninth IEEE Photovoltaic Specialists Conf., IEEE, Piscataway, NJ 2020, pp. 868–871. [22] M. A. Steiner, J. F. Geisz, Appl. Phys. Lett. 2012, 100, 251106. [23] M. Z. Shvarts, M. A. Mintairov, V. M. Emelyanov, V. V. Evstropov,

V. M. Lantratov, N. K. Timoshina, AIP Conf. Proc. 2013, 1556, 147.
[24] N. L. A. Chan, T. Thomas, M. Fuhrer, N. J. Ekins-Daukes, IEEE J. Photovolt. 2014, 4, 1306. [25] D. J. Friedman, J. F. Geisz, M. A. Steiner, IEEE J. Photovolt. 2014, 4, 986. [26] W. Shockley, H. J. Queisser, J. Appl. Phys. 1961, 32, 510. [27] Z. Wang, Q. Lin, B. Wenger, M. G. Christoforo, Y.-H. Lin, M. T. Klug,

M. B. Johnston, L. M. Herz, H. J. Snaith, Nat. Energy 2018, 3, 855.
[28] R. Santbergen, T. Meguro, T. Suezaki, G. Koizumi, K. Yamamoto,

M. Zeman, IEEE J. Photovolt. 2017, 7, 919.
[29] K. Jäger, P. Tillmann, C. Becker, Optics Express 2020, 28, 4751. [30] P. Tillmann, K. Jäger, C. Becker, Sustain. Energy Fuels 2020, 4, 254. [31] S. Chunduri, M. Schmela, Bifacial solar technology report 2018 edition, Technical report, TaiYang News, 2018. [32] S. Wilcox, W. Marion, Users manual for TMY3 data sets, Technical Report NREL/TP-581-43156, National Renewable Energy Laboratory,

2008.
[33] U. Rau, Phys. Rev. B Condens. Matter Mater. Phys. 2007, 76, 085303. [34] O. D. Miller, E. Yablonovitch, S. R. Kurtz, IEEE J. Photovolt. 2012, 2, 303. [35] K. Tvingstedt, O. Malinkiewicz, A. Baumann, C. Deibel, H. J. Snaith,

V. Dyakonov, H. J. Bolink, Sci. Rep. 2014, 4,1.
[36] D. Bi, W. Tress, M. I. Dar, P. Gao, J. Luo, C. Renevier, K. Schenk,

A. Abate, F. Giordano, J. P. Correa Baena, J. D. Decoppet,
S. M. Zakeeruddin, M. K. Nazeeruddin, M. Grätzel, A. Hagfeldt, Sci. Adv. 2016, 2, e1501170.
[37] M. A. Green, Progr. Photovolt. Res. Appl. 2012, 20, 472. [38] B. M. Kayes, H. Nie, R. Twist, S. G. Spruytte, F. Reinhardt, I. C. Kizilyalli,

G. S. Higashi, in Conf. Record of the IEEE Photovoltaic Specialists Conf., IEEE, Piscataway, NJ 2011, pp. 000004–000008.
[39] A. Braun, E. A. Katz, D. Feuermann, B. M. Kayes, J. M. Gordon, Energy Environ. Sci. 2013, 6, 1499. [40] I. Schnitzer, E. Yablonovitch, C. Caneau, T. J. Gmitter, Appl. Phys. Lett. 1993, 62, 131. [41] J. A. Guerra, A. Tejada, L. Korte, L. Kegelmann, J. A. Töfflinger,

S. Albrecht, B. Rech, R. Weingärtner, J. Appl. Phys. 2017, 121, 173104.
[42] R. Brenes, M. Laitz, J. Jean, D. W. Dequilettes, V. Bulovi´c, Phys. Rev. Appl. 2019, 12, 014017. [43] C. Cho, B. Zhao, G. D. Tainter, J. Y. Lee, R. H. Friend, D. Di,

F. Deschler, N. C. Greenham, Nat. Commun. 2020, 11, 611.
[44] L. M. Pazos-Outón, M. Szumilo, R. Lamboll, J. M. Richter,

M. Crespo-Quesada, M. Abdi-Jalebi, H. J. Beeson, M. Vru ini,
M. Alsari, H. J. Snaith, B. Ehrler, R. H. Friend, F. Deschler, Science 2016, 351, 1430.
[45] I. L. Braly, D. W. deQuilettes, L. M. Pazos-Outón, S. Burke,

M. E. Ziffer, D. S. Ginger, H. W. Hillhouse, Nat. Photon. 2018, 12, 355.
[46] M. Jošt, E. Köhnen, A. B. Morales-Vilches, B. Lipovšek, K. Jäger,

B. Macco, A. Al-Ashouri, J. Krc,ˇ L. Korte, B. Rech, R. Schlatmann,
M. Topic,ˇ B. Stannowski, S. Albrecht, Energy Environ. Sci. 2018, 11, 3511.
[47] E. Köhnen, M. Jošt, A. B. Morales-Vilches, P. Tockhorn, A. Al-Ashouri,

B. Macco, L. Kegelmann, L. Korte, B. Rech, R. Schlatmann,
B. Stannowski, S. Albrecht, Sustain. Energy Fuels 2019, 3, 1995.
[48] J. Jia, Y. Miao, Y. Kang, Y. Huo, M. Mazouchi, Y. Chen, L. Zhao,

H. Deng, P. Supaniratisai, S. H. AlQahtani, J. S. Harris, Opt. Express 2015, 23, A219.
[49] R. Levinson, H. Akbari, Cement Concrete Res. 2002, 32, 1679. [50] G. E. Eperon, S. D. Stranks, C. Menelaou, M. B. Johnston, L. M. Herz,

H. J. Snaith, Energy Environ. Sci. 2014, 7, 982.
[51] M. T. Hörantner, H. J. Snaith, Energy Environ. Sci. 2017, 10, 1983. [52] B. M. Yu Jeco, K. Yoshida, R. Tamaki, N. Ahsan, Y. Okada, in 33rd European Photovoltaic Solar Energy Conf. and Exhibition, WIP, München, Germany 2017, pp. 1236–1240.
