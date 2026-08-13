# EES Solar

PAPER

Elucidating the efficiency limit of silicon-based monolithic tandem cells through the combination Cite this: EES Sol.,2025,1,1030 of Auger and Shockley–Queisser limits

Andreas Fell, * ab Oliver Fischer, ac Martin Bivour, a Christoph Messmer, ac Jonas Schön, ac Martin C. Schubert a and Stefan W. Glunz ac

Accurate theoretical efficiency limits are critical for diagnosing loss mechanisms and guiding optimization in solar cell technologies. While the Shockley–Queisser (SQ) limit remains the most widely used framework for assessing tandem and multijunction devices, its assumptions—purely radiative recombination and ideal light absorption—do not account for the intrinsic limitations of silicon (Si), the dominant photovoltaic material. In particular, Si's indirect bandgap resulting in Auger recombination imposes a lower efficiency ceiling. In this work, we present a rigorous simulation approach that combines SQ-limited top cells with an Auger-limited Si bottom cell, accounting also for luminescent coupling (LC). This hybrid modeling approach yields a maximum theoretical efficiency of 43.2% for an ideal two-terminal Si-based tandem device, compared to

45.2% using the unrealistic assumption of a SQ-limited Si bottom cell. The optimal configuration features a top cell bandgap of 1.71 eV and a 300 mm-thick Si bottom cell, with a minor efficiency penalty of only
0.1% for a more typical thickness of 120 mm. Accounting for LC values typical for perovskite top cells reduces the optimum efficiency to 42.4%. Special emphasis is placed on the interpretation of fill factor (FF), highlighting the need for correct analytical FF limit (FF₀) calculations using an appropriate ideality factor,
Received 3rd June 2025 which is 5/3 for silicon based tandem at the theoretical limit. To support future benchmarking, we provide Accepted 25th September 2025 lookup tables of current–voltage (JV) parameters for a range of top cell bandgaps, bottom cell properties, DOI: 10.1039/d5el00085h multijunction stacks with up to six subcells, and perovskite-specific top cell properties. These results offer rsc.li/EESSolar reliable efficiency limits for the evaluation of high-efficiency silicon-based tandem and multijunction solar cells.

Broader context Silicon-perovskite tandem solar cells represent the most promising path to push photovoltaic efficiencies beyond the single-junction limit, and are widely regarded as the next-generation solar technology. However, theoretical benchmarks typically rely on the Shockley–Queisser (SQ) limit, which does not accurately capture the intrinsic loss mechanisms of silicon—such as Auger recombination and weak absorption close to the bandgap. This leads to overestimated efficiency targets and hampers meaningful loss analysis and device optimization. In this work, we rigorously combine the SQ-limit model for the top cell/top cells with the latest established Auger-limit model for the silicon bottom cell, enabling physically sound efficiency limits for silicon-based tandem and multijunction architectures. We provide detailed insights into the role of ll factor and luminescent coupling, and publish tabulated JV parameters across a range of congurations. By offering a more accurate and future-proof benchmark for what is likely to remain the dominant tandem architecture for years to come, this work is expected to serve as a widely referenced standard—much like the established single-junction silicon limits by (Niewelt et al., Sol. Energy Mater. Sol. Cells, 2022, 235, 111467) and (Richter et al., Phys. Rev. B: Condens. Matter Mater. Phys., 2012, 86, 16, 165202). Our results will support researchers and developers in setting realistic targets and interpreting experimental performance with higher condence.

Introduction maximum achievable power conversion efficiency (PCE), short- circuit current density (Jsc), open-circuit voltage (Voc)andll

|Theoretical performance limits play a critical role in guiding||||||factor|(FF) under|idealized|conditions,|such limits|provide|
|---|---|---|---|---|---|---|---|---|---|---|---|
|the development of photovoltaic technologies. By dening the Fraunhofer Institute for Solar Energy Systems ISE, 79110 Freiburg, Germany. E-mail:||||||a benchmark for identifying dominant loss mechanisms in experimental ways. detailed balance limit proposed by Shockley and Queisser (SQ),|devices The most|for directing widely used|their theoretical|optimization framework|path- is the|
|andreas.fell@ise.fraunhofer.de AF Simulations GmbH, Landstr. 33a, 79232 March, Germany||||||which solar cell as a function of the absorber material's band gap.|describes|the efficiency|ceiling|for a single-junction||
|Chair|for Photovoltaic|Energy Conversion,|Department|of Sustainable|Systems|It assumes radiative recombination as the sole electrical loss||||||
|Engineering Freiburg, Germany|(INATECH),|University|of Freiburg,|Emmy-Noether-Str.|2, 79110|mechanism together with unity absorptance of all photons||||||

Theoretical performance limits play a critical role in guiding factor (FF) under idealized conditions, such limits provide

a

b c

1030 | EES Sol.,2025,1,1030–1039 © 2025 The Author(s). Published by the Royal Society of Chemistry

Paper

with energies above the bandgap. While the SQ model provides valuable insight, especially for direct bandgap materials, it falls short in accurately representing the performance poten- tial of silicon (Si), the dominant material in the photovoltaic industry. Silicon's indirect bandgap introduces additional intrinsic losses, most notably Auger recombination, and also weak absorption near the band edge, necessitating thick absorbers and efficient light management schemes. These characteristics are not captured in the idealized assumptions of the SQ model, but more elaborate electro-optical device models are required to calculate intrinsic performance limits of Si solar cells. This so- called “Auger-limit” of a single-junction silicon solar cell was 2 most recently quantied to 29.4% by Niewelt et al. While the Auger-limit models are well-established for silicon single- junction cells, this more accurate limit is to date rarely applied when evaluating multijunction solar cell architectures that incorporate silicon as a bottom cell. One reason is the non- trivial combination of the analytical SQ model for the top cell with the electro-optical device simulation model of the Si bottom cell. Furthermore, there is a lack of comprehensive, tabulated data for current–voltage (JV) parameters besides effi- ciency of Si based tandem cells – even within the SQ 3–5 framework. Instead, the SQ framework resulting in an optimal efficiency of 45.2%, assuming a SQ-limited bottom cell with a bandgap of 1.12 eV, 6 is still commonly used to assess Si- based tandem cells. This leads to inconsistencies in theoretical benchmarks and hampers efforts to concisely diagnose and optimize real-world devices. Almansouri et al. 7 rst reported modeling results combining an Auger limited Si bottom cell with a SQ limited top cell, investigating a range of practical bottom cell properties. However, luminescent coupling (LC) is not considered, and no results for the specic case of a perovskite top cell are given. The study of Bowman et al. 8 focuses on analytical modeling of LC in perovskite tandem cells, and also give a maximum efficiency for an Auger limited Si bottom cell combined with an optically realistic perovskite top cell absorber as 42.0% with, and 43.0% without LC, respectively. Allen et al. 9 used a simplied equivalent-circuit model, with neglection of LC, of various Si bottom cells combined with an optically realistic perovskite top cell absorber to derive an efficiency limit of 42.45%, and a practical target of 37.8%. Besides the various simplications, all these previous works do not list JV parameters of the performance limits, except single values for efficiency for specic assumptions. In this work, we rigorously simulate the performance limits of tandem and multijunction solar cells, under the assumption of SQ-limit top cells and an Auger-limit silicon bottom cell. Our model bridges detailed balance and thickness-dependent device modeling to provide accurate, physically grounded effi- ciency limits along with complete JV parameter sets, made available as lookup tables. Particular emphasis is placed on FF, a parameter that is easily misinterpreted in tandem analysis¹⁰ due to (i) a current mismatch FF boost effect, (ii) incorrect analytical FF limit (FF₀) calculation using the tandem-level open-circuit voltage as per the popular formula by Green

© 2025 The Author(s). Published by the Royal Society of Chemistry

**View Article Online** EES Solar

et al. with an ideality factor n = 1, and (iii) the fact that Si bottom cells can show ideality factors below unity due to Auger recombination which increases their theoretical FF₀ limit. 13 We further quantify the role of LC in the theoretical limit, extend our analysis to multijunction architectures with Si bottom cells, and present efficiency limits for optically realistic perovskite top cells.

Model The top cell is modeled using the analytical detailed balance 1 framework introduced by Shockley and Queisser. The model assumes a step-function absorption at the bandgap energy and radiative recombination as the only loss mechanism. The resulting radiative recombination current density Jr,SQas a function of device voltage V and bandgap Egis given by eqn (4) 14 in Rühle: ð N <u>2pE² 1</u> J V; E ¼ f q ~ dE: r;SQ g g h³c² <u>E qV</u> E g exp 1 kT Here, k is Boltzmann's constant, T is the temperature, h is Planck's constant, c is the speed of light, fgis the geometrical factor and q is the elementary charge. Neglecting the “−1” in the denominator, which is valid up to SQ-limit open-circuit voltages that remain several kT below E, this can be rearranged andg analytically integrated to: ~ J r;SQV; Eg¼ fgJ01;SQ;mfEgexp <u>qV</u>; kT with J being the dark saturation current density at the SQ 01,SQ,mf limit quantifying the front-side radiative emission loss (repre- senting a monofacial “mf” case): h i J 01;SQ;mfEg¼ <u>2pq</u> kTEg 2þ 2ðkT Þ²Egþ 2ðkT Þ³ : h c 3 2

The geometrical factor fgquanties the total amount of radiative emission relative to the monofacial front side emis- sion. It equals 1 for zero rear-side emission, i.e. a monofacial cell with a perfect rear reector. Most commonly in SQ calcu- lations a symmetric bifacial cell is assumed, resulting in equal front and rear emission and thus fg= 2. For typical monolithic tandem cells however, the top cell is inherently asymmetric, as the upper surrounding material (air) has a different refractive index than the bottom cell material. This results in different internal reection, and means that fg= 2 is a bad assumption. As discussed e.g. in Bowman et al., 8 the difference in escape cones leads to an approximately ntop2higher rear emission relative to the front emission, with ntopbeing the refractive index of the top cell absorber material. Assuming negligible parasitic absorption and thus unity band-to-band absorption in the bottom cell of the rear emitted photons – a good assumption for high-efficient practical cells – the rear side emission equals the additional bottom cell generation by LC. By dening the LC efficiency hlcas the ratio of rear emission over total radiative emission, it is linked to the geometrical factor:

EES Sol.,2025,1,1030–1039 | 1031

EES Solar

f g¼ : 1 hlc

A direct consequence is that higher LC efficiency means substantially higher radiative emission and recombination in the top cell, and thus lower top cell power. This loss cannot be overcompensated by the additional power generation in the bottom cell due to its lower voltage, unless for strong current- mismatch conditions (see Results section). For our calculations, we distinguish two cases for rear emission and thus LC:

(a) “Monofacial” top cell with hlc= 0 and fg= 1, which
represents the upper theoretical limit; this is theoretically possible in a tandem conguration, by assuming an ideal dichroic mirror reecting all radiatively emitted photons above the top cell bandgap energy, while being fully transparent to lower energy external photons; such intermediate reectors are also implemented in experimental devices (see e.g. Callies 15 et al.);

(b) Top cell optically well coupled to the bottom cell for the
entire spectrum, with an exemplary refractive index represen- tative for a typical perovskite absorber of ntop= 2.58 (Manzoor 16 et al.), resulting in hlc= ntop2= 87% and fg= 7.7; notably, this theoretical value is close to the 85% measured by Nguyen 17 et al., and also conrmed by our ray-tracing simulations (see Results section), validating it to be a useful general value for a perovskite silicon tandem cell. Nonradiative recombination in the top cell is quantied 18 using the external radiative efficiency (ERE). For a monofacial SQ top cell we dene the monofacial ERE hext,mf, which relates front side emission J01,rfsand nonradiative recombina- tion J01,nrby <u>J</u> <u>01;SQ;mf</u> h ext;mf¼ : J 01;SQ;mfþ J01;nr

We apply this denition also in the case of non-zero rear-side emission. In this situation, hext,mfno longer strictly quanties the ERE as the ratio of total emission to total generation. However, the advantage is that a given hext,mfvalue corresponds to the same J01,nr, independently of rear-side emission, i.e., both with and without LC. In this way, hext,mfbecomes a quantity more directly linked to the nonradiative recombination prop- erties of the top cell material, consistent with the common intuitive interpretation of ERE. Combined with radiative recombination J01,r, the total top cell recombination J₀₁ is thereby given as ~ <u>1 1 hext;mf</u> J₀₁ ¼ J01;rþ J01;nr¼ J01;SQ;mfþ : 1 hlchext;mf

The silicon bottom cell is modeled using the most recent and comprehensive single-junction Auger-limited efficiency model, as established by Niewelt et al., yielding a theoretical efficiency limit of 29.4%. This model includes the latest data for the silicon absorption coefficient, combined with Lambertian

Paper

light-trapping, the Auger parameterization of Niewelt et al., 21 and radiative recombination by Fell et al., which incorporates Lambertian photon recycling. It further uses a consistent set of silicon semiconductor device properties—including bandgap, bandgap narrowing (BGN) and density of states (DOS)—as summarized in ref. 21. As in the single-junction Auger-limit of

29.4%, we consider intrinsic, i.e. undoped, Si only in this work. It was shown by Niewelt et al. that typical doping levels both for n-type and p-type of around 1 U cm result only in a moderate efficiency penalty of ∼0.2%absdue to increased Auger recom- bination. This penalty is further reduced within a tandem cell due to the lower contribution to output power, rendering it a well negligible loss. While this model incorporates a variety of physical mecha- nisms, it is referred to as the “Auger-limit” for simplicity, consistent with the literature, due to the dominant contribution of Auger recombination relative to the SQ-limit. In contrast to the top cell model, the Si bottom cell performance is inherently thickness-dependent, requiring numerical optimization to balance light absorption and recombination losses. All models are implemented within the solar cell simulation
2 soware Quokka3 (ref. 22 and 23). It was used in Niewelt et al. to compute Auger-limit of single-junction silicon devices, and therefore the latest Auger limit models are exactly incorporated in our calculations. Within this work, the tandem capabilities of Quokka3 have been extended to include a Shockley–Queisser- limited top cell, both in terms of optics (step-function absorp- tion) and recombination (detailed balance radiative recombi- nation limit with adjustable hlcand hext,mf). Notably, the bottom cell is solved by a 1D numerical dri-diffusion model instead of the 0D analytical model in previous works. This work's model accounts for transport losses, which become noticeable for the high Si bottom cell thicknesses optimal for bottom cell limited tandems. This substantially improves accuracy of optimal bottom cell thickness prediction towards lower values. The simulation outputs include full JV characteristics, providing Jsc, Vocand FF. In addition, we compute suns–Voccurves of the tandem device which gives the pseudo ll factor (pFF) derived from this pseudo JV-curve. As no current is owing, this pFF is free from 11 the well-known FF boost arising from current- mismatch. We note that in the idealized model of this work, transport, selectivity and shunt losses are negligible, which results in identical values for implied ll factor (iFF), pFF and FF, the latter however only at exact current-match conditions. An overview of the tandem model of this work is given by the sketch in Fig. 1. In order to model optics of a perovskite top cell with realistic absorption properties, we further employ ray-tracing simula- tions in Sentaurus Device, with the baseline tandem cell prop- 24 erties and modeling methodology described in Messmer et al. In a similar approach as described in Allen et al., 9 we scale the optical data of Manzoor et al. 16 along the photon energy axis in order to calculate wavelength-dependent absorption coeffi- cients for varying bandgaps. Notably, this approach has been proven accurate to match experimental external quantum effi- ciency (EQE) measurements for a range of perovskite compo- 24–27 sitions and bandgaps, including in this work (good match of

and nd only minor difference in calculated J₀₁ of <2%. Notably, f

|fg(and|LC) are|not free|parameters|but|determined|by the|
|---|---|---|---|---|---|---|
|assumed optical properties. We quantify rear side top cell IQE|||||||
|by starting randomized rays within the Si wafer towards the top|||||||
|cell, and calculate respective J₀₁. The ratio of front and rear J₀₁|||||||
|gives assumption described above. IQE and J₀₁ are then inputted into Quokka3 for tandem performance simulations.|hlc= 87%,|accurately||matching|the approximate||

g(and LC) are not free parameters but determined by the

Fig. 1 Sketch of the tandem model used in this work, which combines

a detailed balance model of the top cell (“SQ-limit”) with the latest set of models used for calculating Si single junction efficiency limits (“Auger-limit”); nonradiative recombination in the top cell is consid- ered by the external radiative efficiency assuming monofacial condi- tions hext,mf; luminescent coupling LC is considered as both increased rear side emission (i.e. radiative recombination) in the top cell and additional generation current in the bottom cell.

EQE shape in Fig. 4a). It can therefore be considered a generally valid way of modeling absorption in perovskite top cells, rendering the perovskite-specicefficiency limits presented in this work well future-proof, instead of being particular to a currently best specic material composition. We simulate the EQE of a perovskite top cell with varying thickness and bandgap, assuming negligible recombination losses at short-circuit so that optical absorption in the perov- skite equals EQE. By correcting the EQE with the simulated reection and parasitic absorption, we calculate the IQE. The IQE thereby presents an idealized top cell absorption free from reection and parasitic absorption losses. This is consistent with the SQ assumptions, with the only distinction that a real- istic optical absorption of perovskite material is used, revealing it's fundamental optical limit. We note that this is more accu- 9 rate than previous models using Lambert–Beer or geometrical 8 light-trapping models for predicting absorption, as our approach includes transfer-matrix-method (TMM) calculations for the optically thin perovskite layer. By numerically inte- grating the simulated IQE using the generalized Planck-law, we can quantify associated radiative emission and recombination in a fully consistent manner as described above: ð N 2 <u>2pE IQE</u> J₀₁ ¼ J01; rðIQEÞ¼fgq 3 2 ~dE 0h c exp <u>E</u> kT

The equation above assumes that IQE is angle-independent, which is not obviously the case even for a textured Si bottom cell, as the conformal coating of the perovskite top cell might well produce signicant angular dependence. We validate this by randomizing start directions in our ray-tracing simulations,

Results and discussion Bottom cell thickness optimization The optimal thickness of the silicon bottom cell in a tandem architecture is found to be greater than that of a single-junction device. This is due to the higher relative importance of current density in the tandem conguration, and therefore more importance of near-infrared (NIR) absorption. However, the overall efficiency sensitivity to thickness variations remains low. We nd an optimal thickness of approximately 300 mm, while typical industrial thicknesses in the range of 100–150 mm incur a minor efficiency penalty of only ∼0.1%abs(see Fig. 2a). The 7–9 optimum thickness is lower than in previous studies, caused by the increased accuracy of this work's bottom cell model, which accounts for unavoidable transport losses becoming relevant at large thicknesses. For all subsequent simulations, we x the silicon bottom cell thickness to 300 mm. Although the true optimum would vary with top cell bandgap, we omit bandgap-specic thickness optimization because the associated performance improvements are marginal and the resulting optimal thicknesses in bottom-cell-limited cases would become unrealistically large.

Top cell bandgap variation The efficiency as a function of the top cell bandgap is shown in (Fig. 2b). The maximum efficiency is 43.2% at a bandgap of

1.71 eV when assuming hlc= 0, i.e. an ideal dichroic interme- diate mirror. 1.71 eV corresponds quite closely, but not exactly, to photogeneration current-matching condition (see Fig. 2c), as expected due to optimum efficiency being achieved at Jmpp rather than J match. When assuming h = 87%, the optimum sc lc efficiency is reduced to 42.4%, with a bandgap at slight bottom cell limitation. The efficiency penalty arises from the increased top cell radiative emission and therefore lower Voc(see Fig. 2d). As expected, LC plays a substantial role in bottom-cell-limited devices, where the additional bottom cell current increases the overall Jsc(see Fig. 2c). A positive effect of LC is a much lower dependence of efficiency on the bandgap for bottom cell limited devices, which is linked to a higher tolerance against current mismatch. Notably, these ndings regarding LC are qualita- tively and quantitatively consistent with the ndings of Bowman et al.
8 Furthermore, the impact of the LC effect in providing additional bottom cell current is separated from the mentioned Vocloss by the “SQ, no LC” line in Fig. 2b, for which only the additional generated current was disabled in Quokka3. While physically these two effects are fundamentally linked, the neglected bottom cell generation is oen used due to lower

Fig. 2 Performance limit of a tandem cell combining a Auger-limit silicon bottom cell and a top cell with step-function absoprtion; varied is the

top cell bandgap and its nonradiative recombination properties via the monofacial external radiative efficiency hext,mf(a value of 1 represents the SQ limit); influence of luminescent coupling (LC) is shown by assuming two different coupling efficiencies hlc, and one simulation with switched- off bottom cell generation (hext,mf= 1, no LC current); (a) variation of bottom cell thickness showing minor impact of broad variation around the optimum of 300 mm; (b) power conversion efficiency (PCE) compared with previously published limits (Bowman et al. and Allen et al. using realistic perovskite absorption data instead of SQ limit); (c) short-circuit current density Jsc, showing the impact of LC and current-match; (d) open circuit voltage Voc, showing substantial decrease for the high LC case due to increased top cell radiative recombination loss via rear-side emission.

model implementation effort. 7,9,24 This simplication is shown to be valid for top cell limited devices, and introduces only a minor error for current-match conditions, but fails for bottom cell limited devices.

Fig. 2b also illustrates the efficiency penalty resulting from

non-unity (i.e., below SQ limit) external radiative efficiency (ERE) of the top cell. The inuence of LC decreases signicantly with decreasing hext,mf. For hext,mfvalues below 10%, LC shows a small impact on Voc, and below 1% it becomes an overall minor effect even for bottom-cell limited devices. Notably, this holds for performance and JV characteristics, and does not preclude signicant impact of LC for specic measurement conditions, like e.g. quantum efficiency measurements. As found earlier, the monolithic efficiency optimum is only slightly below the optimum in a four-terminal tandem cong- uration, 3,5 which we recalculate in this work to be 43.3% for an Auger-limit silicon bottom cell and a 1.73 eV top cell.

Tabular data for the optimal bottom cell thickness of 300 mm for the two LC cases, as well as for a typical thickness of 120 mm, are given in Tables 1–3.

Fill factors – FF, pFF and FF₀ In Fig. 3a various ll factors (FF) are shown as a function of bandgap. A well-known FF dependence on current mismatch¹¹ can clearly be seen, i.e. the FF rises for increasing current- mismatch and has a steep minimum at the current-match condition. A mismatch of 0.5 mA cm −2 gives already a FF boost of around 1%abs. FF is also moderately inuenced by LC. The pFF from suns–Voccurve on the other hand (which is identical to the implied ll factor iFF as the investigated ideal device is free from transport losses) shows a smooth linear increase with bandgap. It is popular to compare the FF or pFF to the so-called FF₀ introduced by Green et al. in order to identify FF losses which

Table 1 JV parameters of tandem device with Auger limited silicon

Table 3 JV parameters of tandem device with Auger limited silicon

bottom cell and SQ limited top cell at the optimal bottom cell thick- bottom cell and SQ limited top cell at a bottom cell thickness of 120 ness of 300 mm and hlc= 0% mm and hlc= 87%

|ness of 300 mm and h||= 0%||||
|---|---|---|---|---|---|
|Bandgap [eV]|PCE [%]|V [V]|J [mA cm|] FF [%]|pFF [%]|
|1.58|34.7|2.03|18.3|93.6|90.0|
|1.6|36.4|2.05|19.0|93.4|90.0|
|1.62|37.9|2.07|19.6|93.2|90.1|
|1.64|39.0|2.09|20.1|93.1|90.2|
|1.66|40.6|2.11|20.7|92.8|90.2|
|1.68|42.0|2.13|21.4|92.2|90.3|
|1.7|43.0|2.15|22.0|91.1|90.4|
|1.712|43.23|2.159|22.08|90.69|90.41|
|1.72|43.2|2.17|21.9|91.1|90.4|
|1.74|42.8|2.19|21.3|91.8|90.5|
|1.76|42.1|2.21|20.7|92.2|90.6|
|1.78|41.4|2.22|20.1|92.5|90.6|
|1.8|40.7|2.24|19.6|92.7|90.7|
|1.82|40.0|2.26|19.1|92.8|90.8|
|1.84|39.2|2.28|18.5|93.0|90.8|
|1.86|38.4|2.30|17.9|93.1|90.9|

|mm and h|= 87%|||||
|---|---|---|---|---|---|
|Bandgap [eV]|PCE [%]|V [V]|J [mA cm|] FF [%]|pFF [%]|
|1.58|40.2|2.01|21.6|92.4|89.9|
|1.6|40.6|2.03|21.7|92.3|90.0|
|1.62|41.0|2.05|21.7|92.3|90.0|
|1.64|41.4|2.06|21.7|92.2|90.1|
|1.66|41.6|2.08|21.8|91.8|90.2|
|1.68|41.9|2.10|21.8|91.6|90.2|
|1.7|42.2|2.12|21.9|91.1|90.3|
|1.712|42.3|2.13|21.9|90.7|90.3|
|1.72|42.2|2.14|21.8|90.4|90.4|
|1.74|41.9|2.16|21.3|91.1|90.4|
|1.76|41.3|2.18|20.7|91.6|90.5|
|1.78|40.6|2.20|20.1|91.9|90.6|
|1.8|40.0|2.21|19.6|92.2|90.6|
|1.82|39.3|2.23|19.1|92.4|90.7|
|1.84|38.5|2.25|18.5|92.5|90.7|
|1.86|37.8|2.27|17.9|92.7|90.8|

−2 −2 <u>oc</u> sc <u>oc sc</u>

the individual cells' ideality factors, as can be shown e.g. for the

Table 2 JV parameters of tandem device with Auger limited silicon

case of a tandem (subscript tnd): bottom cell and SQ limited top cell at the optimal bottom cell thick- ~ ness of 300 mm and hlc= 87%

|ness of 300 mm and h||= 87%||||
|---|---|---|---|---|---|
|Bandgap [eV]|PCE [%]|V [V]|J [mA cm|] FF [%]|pFF [%]|
|1.58|40.5|1.99|22.0|92.4|89.8|
|1.6|40.9|2.01|22.0|92.3|89.9|
|1.62|41.3|2.03|22.1|92.2|90.0|
|1.64|41.7|2.05|22.1|92.1|90.0|
|1.66|42.0|2.07|22.1|91.8|90.1|
|1.68|42.3|2.09|22.2|91.3|90.2|
|1.7|42.4|2.11|22.2|90.5|90.3|
|1.72|42.1|2.13|21.9|90.8|90.3|
|1.74|41.7|2.14|21.3|91.3|90.4|
|1.76|41|2.16|20.7|91.7|90.4|
|1.78|40.4|2.18|20.1|92.0|90.5|
|1.8|39.7|2.2|19.6|92.2|90.6|
|1.82|39.1|2.22|19.1|92.4|90.6|
|1.84|38.3|2.24|18.5|92.5|90.7|
|1.86|37.5|2.26|17.9|92.7|90.8|

||n kT|J ~|||
|---|---|---|---|---|
|from which follows by basic algebra: and|¼ q ln n kT ¼ q ln ntnd|J ¼ V J ~ n J þ = ntop+ n|þ V kT q ln bot|J ~ J|
||J ¼ J|J|:||

tnd Vtnd bot top 0;tnd −2 <u>oc</u> sc top bot 0;top 0;bot

are not related to ideal recombination losses corresponding to the measurable Voc. The derivation of the FF₀ formula assumes a single-diode model with xed ideality factor n, which is most commonly assumed to be 1. <u>v</u> <u>oclnðvocþ 0:72Þ</u> FF₀ ¼; v ocþ 1 with <u>qVoc</u> v oc¼ : nkT

It is stressed that for multijunction devices, the FF₀ formula must not directly be applied with n = 1. For a series-connection of multiple cells, the ideality factor of a single diode model representing the multijunction device instead equals the sum of

<u>n</u> <u>top</u> tnd <u>n</u> <u>bot</u> tnd 0;tnd 0;topn 0;botn

Wrongly applying n = 1 for a tandem device to calculate FF₀ results in strong overestimation of achievable FF. Using n = 2 would be appropriate for a tandem device with both sub cells following ideal n = 1 recombination. For an Auger-limited Si bottom cell however, the ideality factor instead is 2/3, see e.g. Sinton et al., 13 and consequently n = 5/3 must be assumed when calculating FF₀ for a tandem cell with an Auger-limited Si bottom cell. This is evidenced by the excellent agreement of FF₀ (n = 5/3) with the simulation results in Fig. 3a. Notably, while record single-junction silicon cells indeed showing ideality factors below 1, typical experimental Si bottom cells are not yet largely Auger dominated, and so for experimental silicon based tandem cells n = 2 could be more appropriate when calculating FF₀. Most accurate would be to rst determine the ideality factor of the silicon bottom cell under 0.5 suns generation, by matching FF₀ with the measured iFF of a single-junction or subcell-selective measurement. Subsequently, this ideality factor can be increased by 1 and then be applied to the tandem cell V to calculate the FF of the experimental tandem cell. As oc an approximative alternative, a lookup for tandem efficiency and JV parameter limits for the case of a given silicon bottom

Fig. 3 (a) fill factors as a function of top cell bandgap and at its radiative limit; the FF shows strongly the well-known current mismatch artifact,

while pFF is artifact free and also not impacted by LC; FF₀ calculated from the device’ Vocmatches pFF only when using an ideality factor of n = 5/ 3; (b) multijunction cell efficiency limit comparing the unconstrained Shockley Queisser (SQ) limit with the cases a 1.12 eV SQ-limit and an Auger- limit silicon bottom cell; adaption of Fig. 1 of Schygulla et al.; the bandgap values shown are the optimal bandgaps for an Auger-limit silicon bottom cell as calculated in this work.

cell with a known Vocbelow the Auger limit is given in Table 4. Here we introduce an extrinsic recombination contribution J 01,extrto the silicon bottom cell with a typical thickness of 120 mm. It is thereby assumed that the extrinsic recombination has an ideality factor of 1, which can be considered a reasonable approximation for typical high-efficiency bottom cells. It can be seen that the ideality factor, which fullls FF₀ = FF for the bottom cell, quickly approaches 1 with increasing extrinsic recombination. Notably, with zero extrinsic recombination, i.e. at the Auger-limit, the ideality factor does not exactly equal 2/3 but 0.71. This is partly due to radiative recombination with n = 1 having a non-negligible contribution.

Multiple top cells Furthermore, we calculate efficiency limits for multiple cells on top of a Si bottom cell, which can currently not be directly

Table 4 JV parameters of 120 mm thick Si bottom cell with additional

extrinsic recombination J01,extr(assuming ideality factor of 1), with a current-matched 1.72 eV bandgap SQ-limit top cell with mlc= 87%; shows appropriate bottom cell ideality factors and tandem fill factor limits for devices with realistic bottom cells; ideality factor nSiis determined by solving FF₀(Voc,Si,nSi) = FFSi; the respective tandem ideality factor for FF₀ calculation is nSi+1 −2 <u>J</u> <u>01,extr[fA cm] Voc,Si[V] FFSi[%] nSi[] PCE [%] FF [%]</u> 0 0.742 88.8 0.71 42.3 90.5 2 0.737 87.5 0.81 41.9 90.0 4 0.732 86.7 0.87 41.7 89.7 7 0.726 86.1 0.92 41.5 89.4 10 0.721 85.7 0.96 41.3 89.3

0.714 85.2 0.98 41.1 89.1
0.708 85.0 41.0 89.0
0.703 84.8 1.01 40.8 88.9
0.699 84.7 1.02 40.7 88.9
0.693 84.5 1.03 40.6 88.8
performed in Quokka3. As described by Schygulla et al., 6 we rst assume that the total absorbed photon ux is xed regardless of the number of cells, which is 44.37 mA cm −2 in our tandem simulations. Note that this value is higher than in the single junction Auger limit of Niewelt et al., 2 because of the higher optimum thickness (300 mm vs. 100 mm). We then assume perfect photogeneration current-match, i.e., that the current is evenly distributed between the sub cells. This denes the bandgaps of the top cells, and their J₀₁ values. We then perform a single-junction Si JV curve simulation in Quokka3 for the bottom cell with the respective generation current density, and nd the total JV curve by summing all sub cell voltages for each current density point calculated from the respective single diode model. This approach neglects bottom cell thickness optimization and LC, which however has been shown in the tandem case to be a minor effect at the efficiency optimum. With this data, we adapt Fig. 1 of Schygulla et al. 6 to include an Auger-limited Si bottom cell instead of a 1.12 eV SQ-limited bottom cell, providing more accurate and substantially lower theoretical limits for such devices, see results in Fig. 3b and

Table 5.

Table 5 JV parameters of multijunction device with Auger limited

silicon bottom cell and multiple SQ limited sub cells with their bandgaps optimized for current-match and thus maximum efficiency <u># of junctions PCE [%] V [V] J [mA cm</u> −2 <u>]FF[%]</u> <u>oc sc</u> 1 (Niewelt et al.) 29.4 0.757 43.4 89.5 2 43.2 2.16 22.2 90.3 3 48.4 3.61 14.8 90.7

51.3 5.09 11.1 90.9
52.9 6.55 8.87 91.0
54.0 8.02 7.39 91.0

Fig. 4 (a) comparison of simulated EQEs and IQEs using ray-tracing for exemplary perovskite absorber bandgap and thickness (lines) with the

measured top cell EQE of the 33.9% tandem cell by Longi; (b) efficiency at the optimal bandgap as a function of perovskite absorber thickness, compared with the SQ limit, in all cases assuming hlc= 87%.

Perovskite top cell Finally, we investigate the efficiency potential implied when considering a perovskite top cell with realistic absorption properties instead of the innitely sharp absorption edge assumption within the SQ calculations. As described in the modeling section, our approach ensures that the only difference to the SQ limit is the intrinsic absorption capability of the perovskite absorber with the given bandgap and thickness, by using the IQE which is free from reection and parasitic absorption losses. An overview of exemplary EQEs and IQEs is given in Fig. 4a, compared to the Longi 33.9% top cell EQE digitized from Liu et al. 28 It can be seen that using the nominal bandgap of 1.69 eV of the Longi cell, along with a realistic thickness value of 800 nm, the absorption around the bandgap, as well as the general EQE shape is well reproduced. This vali- dates our optical modeling approach to be able to represent best-in-class experimental perovskite top cell absorbers. In Fig. 4b the resulting efficiency at the optimum bandgap is plotted as a function of perovskite absorber thickness. Overall, the efficiency potential implied in the optical absorption prop- erties of realistic perovskite material is close to the SQ limit. For practically achievable thicknesses around 1 mm the funda- mental efficiency penalty associated with imperfect absorption is below 0.5%, with only little headroom for larger thicknesses. At 630 nm thickness, our simulations result in an efficiency of 41.5%. The difference to the practical limit of 39.5% pub- lished by Er-Raji et al., 26 which used the same optical modeling approach, is explained mostly by reection and parasitic absorption losses, and also by non-radiative recombination losses in the perovskite absorber.

Conclusions We have presented a rigorous and physically grounded model for evaluating the theoretical efficiency limits of tandem and multijunction solar cells incorporating a silicon bottom cell. By combining the state-of-the-art Auger-limit model for silicon

with an SQ-limit for top cells and accounting for luminescent coupling (LC), we provide an accurate picture of the perfor- mance potential of these architectures. Our results give a maximum theoretical efficiency of 43.2% for a silicon-based tandem device assuming an ideal intermediate dichroic mirror, i.e. free from LC—signicantly lower than the 45.2% obtained when incorrectly applying the SQ limit to the bottom cell. For realistic LC conditions typical for perovskite top cells, the efficiency drops to 42.4% due to the increased radiative emission of the top cell. Assuming realistic absorption proper- ties of a perovskite top cell with an absorber thickness of 1 mm and full LC, the maximum efficiency is with 42.0% less than

0.5%absbelow the theoretical limit, conrming the excellent tandem performance potential. We identify an optimal silicon bottom cell thickness of 300 mm, as opposed to the 100 mm optimum for single-junction Auger-limited silicon, and an optimal top cell bandgap of
1.71 eV. Our analysis shows that performance is relatively insensitive to moderate variations in bottom cell thickness down to the range of typical Si cell thicknesses. The additional bottom cell current generation from LC needs to be explicitly included in the modeling only in bottom-cell-limited devices, and when the monofacial external radiative efficiency hext,mfof the top cell exceeds approximately 1%. Above hext,mfof approximately 10%, luminescent coupling signicantly decreases Vocdue to the increased rear side radiative emission of the top cell. In evaluating ll factor (FF), we emphasize the importance of using an appropriate ideality factor when applying the analyt- ical FF limit (FF₀). For an Auger-limited silicon bottom cell the appropriate ideality factor is n = 2/3, which gives a total ideality factor of n = 5/3 to accurately predict the tandem FF₀, aligning with our simulations. Additionally, we emphasize that FF0 should be preferably compared to the pseudo or implied ll factor rather than the FF from JV measurement, which is aver- sively impacted by current-mismatch, to avoid misleading loss interpretations.

For realistic assumptions of optical absorption for the case of a perovskite top cell, we show that the related efficiency penalty compared to the Shockley–Queisser limit is only ∼0.5%absfor an absorber thickness of 1 mm. To support future modeling and device benchmarking efforts, we provide tabulated current–voltage (JV) parameters for tandem congurations across a range of top cell properties, as well as for multijunction stacks comprising up to six subcells. These results serve as reliable limits for performance bench- marking, loss analysis, and strategic design of high-efficiency silicon-based multijunction solar cells.

Author contributions Andreas Fell: conceptualization, methodology, formal analysis, writing – original dra. Oliver Fischer: conceptualization, vali- dation, writing – review and editing. Martin Bivour: method- ology, project administration, writing – review and editing. Christoph Messmer: investigation, validation, writing – review and editing. Jonas Schön: methodology, validation, writing – review and editing. Martin Schubert: supervision, funding acquisition, writing – review and editing. Stefan Glunz: super- vision, funding acquisition, writing – review and editing.

Conflicts of interest There are no conicts to declare.

Data availability The most relevant result values of this article have been included as part of the main article as tables. For reproduction of the model, settings les for the solar cell simulation soware Quokka3 are available on [https://www.quokka3.com/support/](https://www.quokka3.com/support/) examples/efficiency-limit/.

Acknowledgements The authors acknowledge funding by the Federal Ministry for Economic Affairs and Climate Action within the Project “PERLE” (03EE1182A and 03EE1182B).

References 1 W. Shockley and H. J. Queisser, Detailed Balance Limit of Efficiency of p–n Junction Solar Cells, J. Appl. Phys., 1961, 32, 510–519. 2 T. Niewelt, B. Steinhauser, A. Richter, B. Veith-Wolf, A. Fell,

B. Hammann, N. E. Grant, L. Black, J. Tan, A. Youssef,
J. D. Murphy, J. Schmidt, M. C. Schubert and S. W. Glunz, Reassessment of the intrinsic bulk recombination in crystalline silicon, Sol. Energy Mater. Sol. Cells, 2022, 235, 111467.
3 A. S. Brown and M. A. Green, Detailed balance limit for the series constrained two terminal tandem solar cell, Phys. E, 2002, 14,96–100.

4 M. H. Futscher and B. Ehrler, Efficiency Limit of Perovskite/ Si Tandem Solar Cells, ACS Energy Lett., 2016, 1, 863–868. 5 S. Rühle, The detailed balance limit of perovskite/silicon and perovskite/CdTe tandem solar cells, Phys. Status Solidi A, 2017, 214, 1600955. 6 P. Schygulla, R. Müller, D. Lackner, O. Höhn, H. Hauser,

B. Bl¨asi, F. Predan, J. Benick, M. Hermle, S. W. Glunz and
F. Dimroth, Two-terminal III–V//Si triple-junction solar cell with power conversion efficiency of 35.9 % at AM1.5g, Prog. Photovoltaics, 2022, 30, 869–879.
7 I. Almansouri, A. Ho-Baillie, S. P. Bremner and M. A. Green, Supercharging Silicon Solar Cell Performance by Means of Multijunction Concept, IEEE J. Photovoltaics, 2015, 5, 968–

976.
8 A. R. Bowman, F. Lang, Y.-H. Chiang, A. Jim´enez-Solano,

K. Frohna, G. E. Eperon, E. Ruggeri, M. Abdi-Jalebi,
M. Anaya, B. V. Lotsch and S. D. Stranks, Relaxed Current Matching Requirements in Highly Luminescent Perovskite Tandem Solar Cells and Their Fundamental Efficiency Limits, ACS Energy Lett., 2021, 6, 612–620.
9 T. G. Allen, E. Ugur, E. Aydin, A. S. Subbiah and S. De Wolf, A Practical Efficiency Target for Perovskite/Silicon Tandem Solar Cells, ACS Energy Lett., 2025, 10(1), 238–245. 10 O. Fischer, A. J. Bett, Y. Zhu, C. Messmer, A. D. Bui,

P. Schygulla, A. Fell, O. Er-raji, B. P. Kore, F. Schindler,
D. Macdonald, Z. Hameiri, S. W. Glunz and
M. C. Schubert, Revealing charge carrier transport and selectivity losses in perovskite silicon tandem solar cells, Matter, 2025, 102404.
11 M. Meusel, R. Adelhelm, F. Dimroth, A. W. Bett and

W. Warta, Spectral mismatch correction and spectrometric characterization of monolithic III–V multi-junction solar cells, Prog. Photovoltaics, 2002, 10, 243–255.
12 M. A. Green, Solar cell ll factors: General graph and empirical expressions, Solid-State Electron., 1981, 24, 788–

789.
13 R. A. Sinton and R. M. Swanson, Recombination in highly injected silicon, IEEE Trans. Electron Devices, 1987, 34, 1380–1389. 14 S. Rühle, Tabulated values of the Shockley–Queisser limit for single junction solar cells, Sol. Energy, 2016, 130, 139–147. 15 A. Callies, M. Hanser, J. C. Goldschmidt, B. Bl¨asi and

O. Höhn, Structuring of perovskite-silicon tandem solar cells for reduced reectance and thermalization losses, Opt. Express, 2023, 31, 19428–19442.
16 S. Manzoor, J. H¨ausele, K. A. Bush, A. F. Palmstrom,

J. Carpenter, Z. J. Yu, S. F. Bent, M. D. Mcgehee and
Z. C. Holman, Optical modeling of wide-bandgap perovskite and perovskite/silicon tandem solar cells using complex refractive indices for arbitrary-bandgap perovskite absorbers, Opt. Express, 2018, 26, 27441–27460.
17 K. Nguyen, O. Fischer, C. Messmer, Y. Zhu, D.-T. Nguyen,

A. D. Bui, Z. Hameiri, F. Schindler, M. C. Schubert,
H. Shen, K. Weber, K. Catchpole, D. Macdonald and
H. T. Nguyen, The Role of Luminescent Coupling in Monolithic Perovskite/Silicon Tandem Solar Cells, Small, 2024, 20, e2403461.

18 U. Rau, Reciprocity relation between photovoltaic quantum efficiency and electroluminescent emission of solar cells, Phys. Rev. B:Condens. Matter Mater. Phys., 2007, 76, 085303. 19 M. A. Green, Improved silicon optical parameters at 25°C, 295 K and 300 K including temperature coefficients, Prog. Photovoltaics Res. Appl., 2022, 30(2), 164–179. 20 M. A. Green, Lambertian light trapping in textured solar cells and light-emitting diodes, Prog. Photovoltaics Res. Appl., 2002, 10, 235–241. 21 A. Fell, T. Niewelt, B. Steinhauser, F. D. Heinz,

M. C. Schubert and S. W. Glunz, Radiative recombination in silicon photovoltaics: Modeling the inuence of charge carrier densities and photon recycling, Sol. Energy Mater. Sol. Cells, 2021, 230, 111198.
22 A. Fell, J. Schön, M. C. Schubert and S. W. Glunz, The concept of skins for silicon solar cell modeling, Sol. Energy Mater. Sol. Cells, 2017, 173, 128–133. 23 A. Fell, O. Schultz-Wittmann, C. Messmer, M. C. Schubert and S. W. Glunz, Combining Dri-Diffusion and Equivalent-Circuit Models for Efficient 3D Tandem Solar Cell Simulations, IEEE J. Photovoltaics, 2022, 12, 1469–1476. 24 C. Messmer, B. S. Goraya, S. Nold, P. S. Schulze, V. Sittinger,

J. Schön, J. C. Goldschmidt, M. Bivour, S. W. Glunz and
M. Hermle, The race for the best silicon bottom cell: Efficiency and cost evaluation of perovskite–silicon tandem solar cells, Prog. Photovoltaics Res. Appl., 2021, 29, 744–759.
25 M. Heydarian, C. Messmer, A. J. Bett, M. Heydarian,

D. Chojniak, O. S ¨ ¸. Kabaklı, L. Tutsch, M. Bivour, G. Siefer,
M. C. Schubert, J. C. Goldschmidt, M. Hermle, S. W. Glunz and P. S. C. Schulze, Maximizing Current Density in Monolithic Perovskite Silicon Tandem Solar Cells, Sol. RRL, 2023, 7(7), 2200930.
26 O. Er-raji, C. Messmer, A. J. Bett, O. Fischer, S. K. Reichmuth,

F. Schindler, M. Bivour, O. Schultz-Wittmann, J. Borchert,
M. Hermle, J. Schön, F. D. Heinz, M. C. Schubert,
P. S. C. Schulze and S. W. Glunz, Loss Analysis of Fully- Textured Perovskite Silicon Tandem Solar Cells: Characterization Methods and Simulation toward the Practical Efficiency Potential, Sol. RRL, 2023, 7, 2300659.
27 L. Restat, C. Messmer, M. Heydarian, M. Heydarian,

J. Schoen, M. C. Schubert and S. W. Glunz, Optoelectrical Modeling of Perovskite/Perovskite/Silicon Triple-Junction Solar Cells: Toward the Practical Efficiency Potential, Sol. RRL, 2024, 8(5), 2300887.
28 J. Liu, Y. He, L. Ding, H. Zhang, Q. Li, L. Jia, J. Yu, T. W. Lau,

M. Li, Y. Qin, X. Gu, F. Zhang, Q. Li, Y. Yang, S. Zhao, X. Wu,
J. Liu, T. Liu, Y. Gao, Y. Wang, X. Dong, H. Chen, P. Li,
T. Zhou, M. Yang, X. Ru, F. Peng, S. Yin, M. Qu, D. Zhao,
Z. Zhao, M. Li, P. Guo, H. Yan, C. Xiao, P. Xiao, J. Yin,
X. Zhang, Z. Li, B. He and X. Xu, Perovskite/silicon tandem solar cells with bilayer interface passivation, Nature, 2024, 635, 596–603.
