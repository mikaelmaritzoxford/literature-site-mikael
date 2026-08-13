## <u>PRX ENERGY 1,023005 (2022)</u>

# Accurate Optical Modeling of Monolithic Perovskite/Silicon Tandem Solar Cells and Modules on Textured Silicon Substrates

||1,*|1|2|2|1|1|
|---|---|---|---|---|---|---|
|||1|1|1|1,3|1|
|1||1,4|1|1|1,†||
|||2|||||
||3||||||
|4|||||||

Lujia Xu, Jiang Liu, Keith McIntosh, Malcolm Abbott, Erkan Aydin, Thomas Allen, Michele De Bastiani, Maxime Babics, Jingxuan Kang, Mohammed Alamer, Wenbo Yan, Wenzhu Liu, Fuzong Xu, Atteq Ur Rehman, and Stefaan De Wolf *KAUST Solar Center (KSC), Physical Sciences and Engineering Division (PSE), King Abdullah University of* *Science and Technology (KAUST), Thuwal 23955-6900, Saudi Arabia* *PV Lighthouse, Coledale, New South Wales, Australia* *Now at University of Wisconsin–Madison, Madison, Wisconsin, 53706, USA* *Now at Research Center for New Energy Technology, Shanghai Institute of Microsystem and Information* *Technology, Chinese Academy of Sciences, Jiading, Shanghai, 201800, China*

(Received 3 March 2022; revised 29 June 2022; accepted 19 July 2022; published 18 August 2022)

Light-ray tracing (RT) and the transfer matrix method (TMM) allow detailed optical simulation of single-junction silicon and perovskite solar cells, which critically aids device design towards record performance. However, their accuracy is compromised when simulating monolithic perovskite/silicon tandem devices built from textured silicon substrates, due to the resulting complex top-cell morpholo- gies. The associated front surfaces of such tandem devices are typically either roughly conformal to the textured silicon underneath (for thermally evaporated or hybrid-deposited perovskites) or flattened (for solution-processed perovskites). Here, we develop accurate optical models for each configuration. For the conformal-like morphology, we apply a texture-on-texture model to accommodate for local imperfect conformalities. Contrastingly, for the flattened morphology, we develop a multi-subcell model to solve the limitation that films must be conformal in one-step RT + TMM simulations. We verify our models with experimental light absorption and quantum efficiency data for photovoltaic cells and modules in both morphological configurations and identify primary sources of parasitic light absorption. Finally, we extend our simulations to module-scale optics and find that textured module glass can effectively suppress photon escape for both tandem-device morphologies, improving their module performance.

DOI: 10.1103/PRXEnergy.1.023005

## I. INTRODUCTION

textured [10–16]. A flat-front *c*-Si surface permits sim- pler integration of solution-processed perovskite films with Perovskite/silicon tandem (PST) solar cells have come the *c*-Si subcell, but leads to higher reflection losses, under intense research focus in the photovoltaic (PV) and hence, a lower PCE. Consequently, textured *c*-Si community due to their high power-conversion-efficiency front surfaces, which require more sophisticated per- (PCE) potential (theoretical limit ∼45% [1–3]andcur- ovskite subcell processing, but come with enhanced opti- rent record of *>*29% [4–7]) and relative ease of mono- cal gains, have received increased attention from the PV lithic integration of perovskites with conventional crys- research community; double-side-textured *c*-Si wafers are talline silicon (*c*-Si) solar cells. The employed *c*-Si wafers also standard in industrial single-junction *c*-Si solar-cell for monolithic PSTs mainly fall into two categories, manufacturing. based on their surface morphology: (i) front-side flat, Employing double-side-textured *c*-Si subcells also rear-side pyramidal textured [4,8,9] and (ii) double-side affects the perovskite top-cell-surface morphology, depend- ing on the employed perovskite-deposition method. For * lujia.xu@kaust.edu.sa instance, one possible surface morphology is relatively † stefaan.dewolf@kaust.edu.sa conformal to the textured *c*-Si bottom cells (with typ- ical feature sizes on the order of ∼5 *µ*m), as shown *Published by the American Physical Society under the terms of* in Fig. 1(a), and arises from either thermal evaporation *the Creative Commons Attribution 4.0 International license. Fur-* *ther distribution of this work must maintain attribution to the* or hybrid deposition of the perovskite [10–12]. Thermal *author(s) and the published article’s title, journal citation, and* evaporation uses different sources to coevaporate the per- *DOI.* ovskite precursors, which, due to the volatile nature of

2768-5608/22/1(2)/023005(11) 023005-1 Published by the American Physical Society

<u>LUJIA XU et al. PRX ENERGY 1,023005 (2022)</u>

**(a)**
**(b)**
**(c) (d)**
FIG. 1. Structure of hybrid- and solution-processed PST cells, their secondary electron microscope (SEM) images, and the proposed optical models to simulate them: (a) Hybrid-processed PST cell structure used in this study, and its SEM images with different magni- fication levels. Thickness of films is detailed in the Supplemental Material [17]. (b) Solution-processed PST cell structure used in this study and its SEM images. Thickness of films is detailed in Supplemental Material [17]. (c) Illustration of texture-on-texture (TOT) model. (d) Illustration of multi-subcell (MS) model with two subcells.

the organic cations, requires accurate process control. In contrast, the hybrid approach largely circumvents this issue, as it is a two-step deposition combining sequen- tial coevaporation of the largely inorganic precursors with deposition of the organic cations from solution. The sec- ond morphology consists of a largely flattened perovskite

surface, as shown in Fig. 1(b). This morphology results from the deposition of a perovskite precursor solution (either by spin-coating or blade or slot-die coating), fill- ing the valleys of the silicon texture (here with feature sizes on the order of ∼1 *µ*m), followed by film crystalliza- tion [13–16]. We note that practically even hybrid PSTs

023005-2

still come with some imperfect conformal features, such as those present at the rounded pyramid peaks, as shown in

Fig. 1(a).

To investigate the full performance potential of PSTs, it is critical to model the involved light-device interaction accurately [18]. Ray tracing (RT) in combination with the transfer matrix method (TMM) is one of the most widely used tools to analyze the optical properties of all solar cells. However, in contrast to single-junction wafer-based silicon or thin-film-based perovskite solar cells, where, in both cases, all the film surfaces are conformal either to the sili- con wafer texture or the glass substrate, respectively, such absolute conformity is not guaranteed for PSTs built from textured silicon bottom cells, as stated. To date, a number of quantitative optical studies of PSTs using the RT + TMM method can be found in the literature. Several researchers have simulated PSTs with a planar silicon top surface, where the RT + TMM method could be applied accurately due to the ideal con- formity between top and bottom cells [19–25]. Some have also studied PSTs with a textured silicon top inter- face, but none of those studies verified the accuracy of the RT + TMM method by comparing the simulated results with experimentally measured device-absorption and external-quantum-efficiency (EQE) data [15,21,23, 25–27]. Experimental local imperfections, or nonconfor- mities, as evidenced in Figs. 1(a) and 1(b) were either neglected or not discussed in their simulations. Notably, Chen *et al*.[15] simulated PSTs with a blade-coated per- ovskite top cell, similar to the solution-processed PSTs shown in Fig. 1(b), where the flat top surface of the perovskite does not conform to the underlying silicon tex- ture, and therefore, is inconsistent with the fundamental assumption of the TMM, introducing a source of error into the simulations. In addition, although Jacobs *et al*. [25] discussed encapsulated PSTs with a textured silicon top interface, the verification of the photovoltaic module simulation through a comparison to the experimentally measured absorption and EQE was not included in their study. Here, by comparing the simulated and measured absorp- tion and EQE data of both cells and modules, we iden- tify an important inaccuracy in the RT + TMM approach, arising from imperfect conformities in both hybrid and solution PSTs. To accommodate for such a conformity problem, we introduce a texture-on-texture (TOT) model at the perovskite interface for hybrid-processed PSTs, and a multi-subcell (MS) model for solution-processed PSTs, respectively. After validating the TOT and MS models, we use the new optical models to analyze the sources of parasitic absorption, the optical difference between hybrid- and solution-processed PST cells and modules, and the potential improvements anticipated from applying textured glass.

## II. EXPERIMENT

We determine the complex refractive indices, real *n* and imaginary *k*, of all the stacked films for the configurations shown in Fig. 1 by spectroscopic ellipsometry (J.A. Wool- lam VUV-VASE) at room temperature in the wavelength range of 280–1200 nm. We deposit the films either onto glass (rear side is roughened to avoid rear-side reflection) or the polished side of a single-side-polished silicon wafer, depending on which substrate type enables a more uniform and smoother surface or is more compatible with relevant device-processing conditions. The samples are measured within hours after film deposition, minimizing their expo- sure to ambient air. Note that some of these samples,

e.g., the nanocrystalline silicon (nc-Si) and amorphous sil- icon (*a*-Si) films, which are employed as contact layers in hybrid PSTs [10], are comprised of a film stack rather than an individual film because the individual films can- not be deposited directly on glass or silicon without the presence of underlying layers, acting as growth templates. In those cases, we can only determine an effective refrac- tive index of the complete film stack. We use the refractive index of *c*-Si reported in the literature [28–30]. The *n* and *k* values of the characterized films are summarized in the Supplemental Material [17]. At the module level (represented by an encapsulated single-device minimodule), thermoplastic polyurethane (TPU) is used as the encapsulant material [31]. How- ever, the TPU after the lamination process is found to be too thick and rough for ellipsometry measurements. Therefore, rather than making a film sample on the sub- strate for ellipsometry characterization, we laminate mul- tiple layers of TPU by piling them between two flat Teflon boards. The TPU layers are then melted followed by solidification during the lamination process, gener- ating a thick bulk material. The bulk material is then measured by spectrophotometry (PerkinElmer LAMBDA 950 UV/Vis/NIR), involving reflectance, absorption, and transmission (RAT) measurements over the 280–1200 nm wavelength range. The refractive index data of TPU were then extracted following a published procedure [32]. The same method is applied to the front glass of our min- imodules. To assess the accuracy of the optical mod- els, the RAT of hybrid-and solution-processed PST cells and modules are experimentally measured using spectrophotometry within the 280–1200 nm wavelength range. The EQE of perovskites and silicon in the hybrid- and solution-processed PST cells and modules are mea- sured using a LOANA system from PVtools [33]. We use two metrics to evaluate the agreement between modeling and experimental absorption and EQE data:
(i) root-mean-square error (RMSE, unit of %), and (ii) AM1.5 spectrum-weighted average difference (SWAD, unit of mA/cm²; plus or minus sign is determined by simulation data minus experimental data). The SWAD
023005-3

is actually equal to the difference in integrated absorbed or collected current (if EQE) between simulation and experiment. Compared to the RMSE, the SWAD high- lights the difference at those wavelength ranges where a higher photon flux is present in the incident AM1.5 spec- trum. While SWAD provides more relevant quantities to the solar devices’ performance, i.e., generated current, it may lead to misleading information because a large dis- crepancy at wavelength ranges with a low photon flux can be easily compensated for by a small opposite discrep- ancy at the wavelength ranges with a high photon flux. Therefore, both RMSE and SWAD are used in this study.

## III. OPTICAL MODEL FOR HYBRID-PROCESSED PEROVSKITE/SILICON TANDEMS

With all of the required optical information obtained in Sec. II, we then simulate hybrid PST cells and modules with SunSolve [34], which applies ray tracing and thin-film optics to calculate the device’s optical behavior. We begin by treating the bottom *c*-Si surface as consist- ing of random pyramids following an approach discussed in the literature [35,36], where the pyramids have a base angle of 52° and a Phong scattering with 100% fraction using a Phong exponent *α* 100 (see the Supplemental Material for details [37]); Phong scattering is generally introduced in the simulation of random pyramids of a sili- con solar cell to improve its agreement with experimental data by emulating the scattering arising from imperfec- tions in the pyramids [36,38,39]. As shown in Fig. 2(a), this procedure gives close agreement over the entire wave- length range between our bottom *c*-Si cell’s simulated and measured reflectance. The RMSE is 3.42% and the SWAD is 0.24 mA/cm². Once the perovskite is deposited, however, a significant discrepancy (RMSE 6.53%, SWAD

2.23 mA/cm²) arises between simulation and experiment due to the imperfect conformal nature, as can be seen from
Fig. 2(b).
 We address this complication in our simulations by modifying the facets of the pyramids such that they are no longer flat but textured, using the spherical-cap model described in the literature [40–43] (where the spherical caps are upright rather than inverted). Thus, we now sim- ulate the surface with a TOT structure, as illustrated in
Fig. 1(c), thereby attempting to emulate the imperfectly
 conformal perovskite film that coats the random-pyramid textured wafer. Due to the complicated nature of creating this morphology in three-dimensional space, we treat the secondary texture (the spherical caps) as having zero thick- ness. That is, when a ray impinges upon a pyramid facet of the TOT interface, we (i) calculate the ray’s position in space, (ii) trace the ray through the unit cell of a spheri- cal cap, (iii) ascribe any film absorption to absorption at the TOT interface (neglecting any absorption occurring in the superstrate or substrate of the unit cell), (iv) determine
the direction of the ray upon exiting the spherical cap, (v) continue tracing the ray using its position from step (i) and its direction from step (iv). Thus, since the spherical caps do not change the position of the ray (only its intensity and direction), they can be considered as having zero thickness. In this way, the TOT interface behaves like a pyramidal texture covered by spherical caps. Figures 2(b) and 2(c) illustrate how this approach allows us to achieve a better fit to the experimental absorption data of the samples. We use spherical caps with a characteristic angle (defined in the literature [40,43]) of 30° for our hybrid PST cells, because this satisfactorily describes the geometry of the top surface, as detailed in the Supplemental Material [44]. The simulated and experimentally measured absorp- tion curves of hybrid-processed PST cells are shown in

Fig. 2(c). As expected, for the hybrid-processed PST cell,

the imperfect conformity, as shown in Fig. 1(a), mainly happens locally, such as at pyramid apices, so, even when using standard RT, simulated data show a good match with experimental data. Discrepancies mainly happen at short wavelengths, *<*550 nm. After applying our TOT model, we can see the discrepancy is reduced, with the RMSE dropping from 1.86% to 1.26% and the SWAD from 0.49 to 0.04 mA/cm². We also compare the experimental EQE and simulated perovskite and silicon absorption data in Figs. 3(a) and 3(c), showing*<*3.82% RMSE, which further attests the accuracy of our optical model. A similar comparison can be made for hybrid-processed PST modules. Here, good agreement between the simula- tion and experiment is found, even without applying the TOT model. This is mainly because of the presence of the cover glass and TPU at the front. They are the first two materials interacting with light and of dimensions much larger than the local nonconformal features of the *c*-Si tex- ture. Therefore, the glass and TPU dominate the optical performance in the short-wavelength range, reducing the influence of imperfect conformalities. Having established a reasonable optical model, simula- tion allows us now to evaluate the wavelength-dependent absorption within each film or stack for both hybrid- processed PST cells and modules. The results are pre- sented in Figs. 3(a) and 3(c). Figure 3(a) shows that, in our PST device, the front indium zinc oxide (IZO), act- ing as a transparent conductive oxide (TCO), dominates the parasitic absorption below 400 nm, whereas C₆₀, part of the electron-transport-layer (ETL) stack of the per- ovskite, contributes mostly in the 400–1000 nm range. Above 1000 nm, the rear ITO and front IZO are the largest contributors to the optical losses, followed by the rear Ag. The corresponding absorbed equivalent photon current densities of each film (the percentage of total photon cur- rent densities of 46.46 mA/cm²) are shown in Fig. 3(b), where photon current densities are the integrated absorp- tion shown in Fig. 3(a) for the AM1.5 spectrum. C₆₀ para- sitically absorbs 3.71% (corresponding to a current-density

023005-4

**(a)**
**(b)**
**(c)**
**(d)**
FIG. 2. Optical simulation problem caused by imperfect conformalities in hybrid-processed PSTs and the improvement made through applying the TOT structure. (a) Comparison between experiment and simulation of the bottom *c*-Si cell where the surface ′ ′ ,7,7 -tetra(N,N-di-p- is conformal. (b) Comparison between the experiment and simulation of the bottom *c*-Si cell capped by 2,2 tolyl)amino-9,9-bifluorene (spiro-TTB) and perovskite where the surface has local imperfect conformal features. Simulations with and without the TOT structure are both presented. Discrepancy between simulation and experiment in the range of 750 to 1100 nm is noted, but we do not have a definite explanation for this. It could be due to the differences in the hybrid-processed perovskite’s properties (*n* & *k*) when formed on the planar substrates (measured by ellipsometry) and on the textured bottom *c*-Si cell (measured by spectrophotometry). Because perovskite is the first layer that interacts with the incident light in these samples, the simulated absorption is much more sensitive to a small variation in the perovskite’s optics than in other cases where capping layers exist. (c) Comparison between experiment and simulation of hybrid-processed PST cells, both with and without the TOT structure. (d) Comparison between experiment and simulation of hybrid-processed PST modules, both with and without the TOT structure.

loss of 1.72 mA/cm²) of the incident photons, followed by the front IZO (3.21%, 1.49 mA/cm²), the rear ITO (2.11%,

0.98 mA/cm²), and the rear Ag (0.32%, 0.15 mA/cm²), while 3.86% (1.79 mA/cm²) escapes from the cell. The escaped photons, in the case of monofacial PSTs, include both those that are reflected externally by the front surface and those that escape from the front after a few bounces within the device. The modeling of the PST module shows a difference in the short-wavelength (*<*400 nm) range, when compared to the unencapsulated tandem cell. While the glass con- tributes slightly to the optical losses in the 300–350 nm wavelength range, the TPU film almost completely absorbs
the light for wavelengths *<*400 nm, as shown in Fig. 3(c), thereby reducing the photogenerated current in the perovskite top cell by 1.04 mA/cm² relative to the unen- capsulated device. This matches the almost-zero EQE at the module level for this range, as shown in Fig. 3(c). The current mismatch that would otherwise occur due to this decrease in the blue response of the top cell is compensated by an increase in broadband reflectance in the module from the glass and TPU. However, in the future, if a UV-transparent encapsulant could be devel- oped, with the currently employed materials, the silicon subcell would become the bottleneck for current matching. The perovskite bandgap may then have to be widened to

023005-5

**(a) (b)**
**(c) (d)**
FIG. 3. Detailed optical loss analysis: (a) Simulated stacked absorption of each film for hybrid-processed PST cells using the TOT model, and comparison between experimental EQE and simulated perovskite (PVK) and Si absorptions. White area indicates the total escaped light. (b) Distribution of equivalent photon current densities over the wavelength range of 280–1200 nm in hybrid- processed PST cells. Total incident photon current density for this wavelength range is 46.46 mA/cm². (c) Simulated stacked absorption within each film in hybrid-processed PST modules using the TOT model, and comparison between experimental EQE and simulated PVK and Si absorptions. White area indicates total escaped light. (d) Distribution of equivalent photon current densities over the wavelength range of 280–1200 nm in a hybrid-processed PST module. Total incident photon current density for this wavelength range is 46.46 mA/cm².

maintain current matching within the device. Specifically, we find for the PST module that C₆₀ (3.29%, 1.53 mA/cm²) still contributes most to the parasitic absorption, followed by TPU (2.80%, 1.30 mA/cm²), the front IZO (2.62%,

1.22 mA/cm²), the rear ITO (2.01%, 0.93 mA/cm²), the front glass (0.37%, 0.17 mA/cm²), and the rear Ag (0.31%,
0.14 mA/cm²).
## IV. OPTICAL MODEL FOR

## SOLUTION-PROCESSED PEROVSKITE/SILICON

## TANDEMS

To the best of our knowledge, a reliable RT + TMM model for monolithic PSTs built from a textured *c*-Si sub- cell, yet with a flattened perovskite surface, such as the case for solution-processed PSTs depicted in Fig. 1(b),is not yet available in the literature. For these devices, the top surface is almost flat and clearly not parallel to the textured bottom *c*-Si surface, invalidating the conformity assump- tion inherent to the conventional one-step RT + TMM method. In Figs. 4(a) and 4(b), we show the simula- tion results of solution-processed PST devices with three

conventional bottom silicon geometries: front-side planar and rear-side textured (purple), double-side textured (yel- low), and double-side planar (light blue). By comparing their simulated absorption with experimental data, we see that none of them show good agreement with experimental data over the whole studied wavelength range. The rele- vant RMSE and SWAD values are listed in Table I.The two cell architectures with front-planar surfaces show good agreement below 700 nm, but show large deviations for longer wavelengths, especially for the one with the planar rear side. In contrast, the double-side-textured geometry provides relatively good agreement above 700 nm, but a poor match for shorter wavelengths. This suggests that for the solution-processed PSTs the short-wavelength pho- tons interact mainly with the perovskite geometry, i.e., the front-planar geometry, whereas long-wavelength photons interact mostly with the *c*-Si geometry, i.e., the textured geometry. Here, we propose a general modeling method for non- conformal PSTs, called the multi-subcell (MS) model. As shown in Fig. 1(d), the key to this modeling method is to treat one solution-processed PST cell as two subcells. One

023005-6

<u>ACCURATE OPTICAL MODELING OF... PRX ENERGY 1,023005 (2022)</u>

**(a) (b)** 90 90 80 80 70 70 60 60solution PST module solution PST cell 50 50
experiment experiment 40 40 Absorption (%)simulation MS model Absorption (%)simulation MS model 30simulation front planar rear texture30simulation front planar rear texture 20simulation double-side texture20simulation double-side texture simulation double-side planar simulation double-side planar 10 10 300 400 500 600 700 800 900 1000 1100 1200 300 400 500 600 700 800 900 1000 1100 1200 Wavelength (nm) Wavelength (nm)

**(c)**100**(d)** solution PST cell

|MgF₂|n|front i-a - a Si|Si Si|41.88%||MgF₂|
|---|---|---|---|---|---|---|
|front IZO||0% 0%|||rear|i-a Si|
|SnO₂|||||0%|SnO₂ p-a Si|
|C₆₀|middle IZO|||||C₆₀ 0%|
|LiF|1.57%|||||LiF|
|PVK|2PACz|||||PVK rear IZO 2PACz|
|2PACz middle IZO n-a Si front i-a Si Si|0%|||||3.87% Ag n-a 0.15% front escaped Si rear 5.43%|
|rear i-a Si||PVK||||p-a|
|p-a Si||42.69%||||MgF₂ front IZO 0%|
|rear IZO|||LiF|C₆₀ SnO₂|2.54%|Ag|
|Ag glass|(f)||0%|1.84%|0.03%|solution PST module|
|TPU|||Si||rear i-a|glass Si|
|MgF₂ front IZO|n-a 0%|front i-a Si Si 0%|38.91%||0%|TPU p-a Si MgF 0% rear IZO|
|SnO₂||||||SnO₂ 3.03%|
|C₆₀|middle IZO|||||C₆₀ Ag|
|LiF|1.27%|||||LiF 0.12%|
|PVK|2PACz|||||PVK|
|2PACz middle IZO n-a Si front i-a Si|0%|||||escaped 2PACz 11.87% n-a glass front 0.32%|
|Si||||||Si TPU|
|rear i-a Si||PVK 38.62%||||rear 2.54% p-a MgF₂|
|p-a Si|||LiF C₆₀|SnO₂|front IZO||
|rear IZO Ag|||0% 1.51%|0.03%|1.78%|0% Ag|
 90
front IZO 80 70 60solution PST cell 50 PVK EQE middle IZO 40Si EQE Si PVK simulation 30Si simulation *i*-*a* Si EQE/Absorption (%) 20 *i*-*a* Si 10 Si rear IZO 0 300 400 500 600 700 800 900 1000 1100 1200 escaped Wavelength (nm)

**(e)** 100 90 802
front IZO 70 60 50 solution PST module 40PVK EQE Si EQE middle IZO 30PVK simulation Si EQE/Absorption (%) *i*-*a* Si 20 Si simulation 10 *i*-*a* Si Si 0 300 400 500 600 700 800 900 1000 1100 1200 rear IZO Wavelength (nm) escaped

FIG. 4. Comparison of optical models for simulating solution-processed PST and optical analysis based on the MS model. (a) Com- parison between experiment and simulation of the solution-processed PST cell using different optical models. (b) Comparison between experiment and simulation of the solution-processed PST module using different optical models. (c) Simulated stacked absorption of each film in the solution-processed PST cell using the MS model. Comparison between experimental EQE and simulated PVK and Si absorptions. White area indicates total escaped light. (d) Distribution of equivalent photon current densities for the wavelength range of 280–1200 nm in solution PST cells. Total incident photon current density for this wavelength range is 46.46 mA/cm². (e) Simulated stacked absorption of each film in solution-processed PST modules using the MS model. Comparison between experimental EQE and simulated PVK and Si absorptions. White area in the plot indicates total escaped light. (f) Distribution of equivalent photon current densities for the wavelength range of 280–1200 nm in solution-processed PST modules. Total incident photon current density for this wavelength range is 46.46 mA/cm².

|subcell is a double-sided planar perovskite cell with top|The rear escaped light of the top subcell is used as the||||
|---|---|---|---|---|
|air medium and bottom perovskite medium, and another|front incident light of the bottom subcell, and the front||||
|subcell is a double-sided textured silicon cell with top|escaped light of the bottom subcell is treated as the rear||||
|perovskite medium and bottom air medium. In this case,|incident light to the top subcell. This interaction between||||
|RT and TMM can be properly applied to each subcell.|the top|and bottom|must be|iterated|

subcells multiple

023005-7

TABLE I. The RMSE and SWAD of simulations of PSTs.

SWAD Simulation RMSE (%) (mA/cm²)

hybrid PST cell absorption 1.26 0.04 with TOT hybrid PST cell absorption 1.86 0.49 without TOT hybrid PST module absorption 1.06 0.38 with TOT hybrid PST module absorption 1.33 0.19 without TOT hybrid PST cell EQE with 3.82 0.47 TOT perovskite hybrid PST cell EQE with 2.42 0.22 TOT silicon hybrid PST module EQE with 2.68 −0.41 TOT perovskite hybrid PST module EQE with 1.82 −0.47 TOT silicon solution PST cell absorption 21.75 −4.15 with double-side planar solution PST cell absorption 7.77 2.21 with double-side texture solution PST cell absorption 4.30 −0.75 with front planar rear texture solution PST cell absorption 4.09 0.69 with MS model solution PST module 21.42 −4.65 absorption with double-side planar solution PST module 4.89 2.00 absorption with double-side texture solution PST module 5.34 −1.53 absorption with front planar rear texture solution PST module 3.35 −0.74 absorption with MS model solution PST cell EQE with 3.98 0.24 MS perovskite solution PST cell EQE with 3.15 −0.61 MS silicon solution PST module EQE 3.64 0.40 with MS perovskite solution PST module EQE 3.61 −0.55 with MS silicon

−0.74 mA/cm² for modules. The simulated perovskite and silicon absorptions shown in Figs. 4(c) and 4(e) also match their experimental EQEs well with *<*4% RMSE, which further supports the MS modeling method. Please note that the MS model neglects the coherence effect between the perovskite and the layers below it, which might con- tribute to the remaining difference between the simulation and experiment, but the improvement achieved by the MS model obviously exceeds its disadvantage. We then apply the MS model to compute the losses in each component of the solution-processed PST cells and modules. The results are shown in Figs. 4(c)–4(f). For the solution-processed PST cell, the front IZO dom- inates the parasitic absorption below 400 nm, while C60, as part of the ETL stack, contributes mostly in the 400–600 nm wavelength range. Above 600 nm, the front, middle, and rear IZOs are the largest parasitic optical loss sources. More specifically, the rear IZO parasitically absorbs 3.87% (1.80 mA/cm²) of the incident photons, followed by the front IZO at 2.54% (1.18 mA/cm²), C₆₀ at 1.84% (0.85 mA/cm²), and the middle IZO at 1.57% (0.73 mA/cm²), while 5.43% (2.52 mA/cm²) escapes from the cell. Compared to the hybrid-processed PST cell, besides the fact that more TCO layers are present (three vs two), which cause more parasitic absorption, the escaped component of the solution-processed PST cell is 0.73 mA/cm² higher than that of the hybrid-processed PST cell. This highlights the optical advantage of hybrid- processed PSTs (with roughly conformal films) against solution-processed PSTs due to the textured front geometry of the former. Similar to the hybrid-processed PST module, after encapsulation, while TPU cuts off almost all the *<*400 nm wavelengths, the increased broadband reflection from glass and TPU maintains a current match between per- ovskite and silicon, although it is 1.52 mA/cm² lower than at the cell level, which is significant. In con- trast, the cell-to-module current loss for hybrid-processed PSTs is slightly lower, 1.09 mA/cm². The 0.43-mA/cm² cell-to-module current-loss difference between solution- and hybrid-processed PSTs stems from the significantly increased escaped component, which is obvious from Figs. 4(f) and 3(d). In solution-processed PSTs, the escaped photons increase from 5.43% (2.52 mA/cm²) to 11.87% (5.51 mA/cm²), which is more than doubled after encap- sulation. This again indicates how a textured geometry enhances the antireflection properties of devices. One possible way to mitigate the optically adverse effect of the planar-perovskite front surface in the solution- processed PST module is to use textured front glass. Using the MS model, we simulate the case of a front glass with a pyramid texture (54.74°, 500-*µ*m height; see the Sup- plemental Material for more details [45]), and the result is shown in Figs. 5(a) and 5(b). We find that the tex- tured glass increases the current by 0.87 mA/cm² (such

times (1000 times in this study) to represent the physi- cal process that photons keep bouncing within the device until they are absorbed or have escaped. The simulated absorption of solution-processed PST cells and modules are plotted in Figs. 4(a) and 4(b), showing a significantly reduced mismatch with experimental data, compared to the one-step simulation using the three conventional architec- tures, the RMSE and SWAD values of which are detailed in Table I. Using the MS model, the RMSE and SWAD drop to 4.09% and 0.69 mA/cm² for the cell and 3.35% and

023005-8

**(a) (b)**
**(c) (d)**
FIG. 5. (a) Comparison between solution-processed PST modules encapsulated with planar and textured glass. (b) Distribution of equivalent photon current densities over the wavelength range of 280–1200 nm in the solution-processed PST module with textured glass. Total incident photon current density for this wavelength range is 46.46 mA/cm². (c) Comparison between hybrid-processed PST modules encapsulated with planar and textured glass. (d) Distribution of equivalent photon current densities over the wavelength range of 280–1200 nm in a hybrid-processed PST module with textured glass. Total incident photon current densities for this wavelength range is 46.46 mA/cm².

that the cell-to-module current loss is decreased from

1.52 to 0.64 mA/cm²). This textured glass also improves hybrid-processed PSTs but not to the same extent as the solution-processed PSTs. As shown in Figs. 5(c) and 5(d), light escape is suppressed to a level even lower than that before encapsulation, although the parasitic absorptions of the film are slightly increased, finally resulting in a drop of the cell-to-module current losses from 1.09 mA/cm² when using planar glass to 0.51 mA/cm², reaching a 0.58- mA/cm² higher current-matching point between the top and bottom cells (19.56 mA/cm², 0.75 mA/cm² higher than that of the solution PST module using textured glass).
of the ray as if the surface of the pyramidal facets are cov- ered by spherical caps. This TOT model improves the sim- ulation accuracy of hybrid-processed PST cells, decreasing the RMSE of absorption from 1.86% (without TOT) to

1.26% and the SWAD from 0.49 to 0.04 mA/cm². It makes little difference to the accuracy of hybrid-processed PST modules, however, due to the existence of thick glass and TPU layers. Prior to this work, we were not aware of a reliable RT + TMM model for simulating monolithic PSTs on a textured *c*-Si subcell with a flat perovskite surface, such as in the case of solution-processed PSTs. By comparing experiment to simulation of convention- ally conformal bottom *c*-Si geometries, we demonstrate that the solution-processed PST structure cannot be accu- rately simulated by the conventional one-step RT + TMM method. We propose a MS model for simulating non- conformal PST devices. This model treats one solution- processed PST cell as two subcells. In this way, two nonconformal geometries are simulated separately in two interactive subcells, while within each subcell the confor- mity is maintained. The applicability and accuracy of the MS model is supported by comparing the simulation with
## V. CONCLUSION

The accuracy or applicability of RT + TMM is compro- mised when simulating hybrid- or solution-processed PSTs with a textured-silicon front surface, due to the imper- fect (hybrid-processed PSTs) or nonconformity (solution- processed PSTs) of the perovskite surface to the *c*-Si texture. We introduce a TOT model to modify the direction

023005-9

experiment data for both the cells and modules, whereby the RMSE of absorption is decreased from 21.75–4.30% (when using conventional one-step RT + TMM methods) to 4.09% (using the MS model) and the absolute SWAD decreases from 4.15–0.75 to 0.69 mA/cm² for solution- processed PST solar cells and from 21.42–4.89% to 3.35% and 4.65–1.53 to 0.74 mA/cm² for solution-processed PST modules. Based on simulations using TOT and MS models, it is found that C₆₀, IZO, and ITO dominate the parasitic absorption in the unencapsulated cell, while TPU is one of the main sources after encapsulation, par- asitically absorbing almost all photons below 400 nm. This indicates that replacing C₆₀ with a more transpar- ent electron-transport layer and changing IZO, ITO, and TPU to other less-absorbing materials, or even using an encapsulant-free technique [46], are likely to be effective ways to improve the optical performance of hybrid- and solution-processed PST cells and modules. In addition, it is noted that the photons escape much more in solution- than in hybrid-processed PSTs, especially after encapsu- lation. This suggests the importance of the front-surface geometry on the antireflection of devices. We also find that textured glass is a generally effective measure to improve the modular optical performance of PSTs.

## ACKNOWLEDGMENTS

The authors acknowledge the discussion and help from Nina Hong from J.A. Woollam Co., Inc. This work is supported by the King Abdullah University of Sci- ence and Technology (KAUST) Office of Sponsored Research (OSR) under Grants No. OSR-2021-4833, No. OSR-CARF/CCF-3079, No. IED OSR-2019-4580, No. OSR-CRG2020-4350, No. CRG2019-4093, and No. IED OSR-2019-4208.

L.X., J.L., and K.M. conceived ideas, designed experi-
ments, and analyzed the data; J.L. and L.X. developed the MS model; K.M. and M.A. developed the TOT model;

L.X. and W.L. analyzed the ellipsometry and extracted the *n*,*k* of materials; L.X. did all simulations and did the RAT measurement; L.X. and K.M. wrote the paper; T.A.,
K.M., M.D.B., and S.D.W. polished the language; E.A.,
J.L., F.X., J.K., W.L., and T.A. prepared the ellipsometry samples; E.A. and J.L. prepared the top perovskite cells of PSTs; A.U.R. and T.A. prepared the bottom *c*-Si cells of PSTs; M.D.B, M.B., and L.X. encapsulated the PSTs;
M.D.B, M.B., and L.X. prepared the TPU RAT sample;
L.X., J.K., W.L., M.A., J.L., W.Y., and F.X. did the ellip- sometry measurement; S.D.W. supervised the project. All authors contributed to paper revision and result discussion.
[2] A. S. Brown and M. A. Green, Detailed balance limit for the series constrained two terminal tandem solar cell, Phys. E **14**, 96 (2002). [3] M. H. Futscher and B. Ehrler, Efficiency limit of perovskite/Si tandem solar cells, ACS Energy Lett. **1**, 863 (2016). [4] A. Al-Ashouri, E. Köhnen, B. Li, A. Magomedov, H. Hempel, P. Caprioglio, J. A. Márquez, A. B. Morales Vilches, E. Kasparavicius, J. A. Smith, *et al.*, Mono- lithic perovskite/silicon tandem solar cell with *>*29% effi- ciency by enhanced hole extraction, Science **370**, 1300 (2020). [5] Oxford PV hits new world record for solar cell, https:// www.oxfordpv.com/news/oxford-pv-hits-new-world-reco- rd-solar-cell (Accessed 2022.05.01). [6] Best Research-Cell Efficiency Chart, [https://www.nrel.gov/](https://www.nrel.gov/) pv/cell-efficiency.html (Accessed 2022.05.01). [7] J. Liu, M. D. Bastiani, E. Aydin, G. T. Harrison, Y. Gao,

R. R. Pradhan, M. K. Eswaran, M. Mandal, W. Yan, A. Seitkhan, *et al.*, Efficient and stable perovskite-silicon tan- dem solar cells through contact displacement by MgFx, Science **377**, 302 (2022).
[8] J. Xu, C. C. Boyd, Z. J. Yu, A. F. Palmstrom, D. J. Witter,

B. W. Larson, R. M. France, J. Werner, S. P. Harvey, E. J. Wolf, *et al.*, Triple-halide wide-band gap perovskites with suppressed phase segregation for efficient tandems, Science **367**, 1097 (2020).
[9] D. Kim, H. J. Jung, I. J. Park, B. W. Larson, S. P. Dun- field, C. Xiao, J. Kim, J. Tong, P. Boonmongkolras, S. G. Ji, *et al.*, Efficient, stable silicon tandem cells enabled by anion-engineered wide-bandgap perovskites, Science **368**, 155 (2020). [10] E. Aydin, T. G. Allen, M. De Bastiani, L. Xu, J. Ávila,

M. Salvador, E. Van Kerschaver, and S. De Wolf, Interplay between temperature and bandgap energies on the outdoor performance of perovskite/silicon tandem solar cells, Nat. Energy **5**, 851 (2020).
[11] F. Sahli, J. Werner, B. A. Kamino, M. Bräuninger, R. Monnard, B. Paviet-Salomon, L. Barraud, L. Ding, J. J. Diaz Leon, D. Sacchetto, *et al.*, Fully textured monolithic perovskite/silicon tandem solar cells with 25.2% power conversion efficiency, Nat. Mater.**17**, 820 (2018). [12] M. Roß, S. Severin, M. B. Stutz, P. Wagner, H. Köbler,

M. Favin-Lévêque, A. Al-Ashouri, P. Korb, P. Tockhorn,
A. Abate, *et al.*, Co-evaporated formamidinium lead iodide based perovskites with 1000 h constant stability for fully textured monolithic perovskite/silicon tandem solar cells, Adv. Energy Mater.**11**, 2101460 (2021).
[13] Y. Hou, E. Aydin, M. De Bastiani, C. Xiao, F. H. Isik- gor, D.-J. Xue, B. Chen, H. Chen, B. Bahrami, and

A. H. Chowdhury, Efficient tandem solar cells with solution-processed perovskite on textured crystalline sili- con, Science **367**, 1135 (2020).
[14] E. Aydin, J. Liu, E. Ugur, R. Azmi, G. T. Harrison, Y. Hou,

B. Chen, S. Zhumagali, M. De Bastiani, M. Wang, *et al.*, Ligand-bridged charge extraction and enhanced quantum efficiency enable efficient *n*–*i*–*p* perovskite/silicon tandem solar cells, Energy Environ. Sci.**14**, 4377 (2021).
[15] B. Chen, Z. J. Yu, S. Manzoor, S. Wang, W. Weigand, Z. Yu,G.Yang,Z.Ni,X.Dai,Z.C.Holman,*et al.*,Blade- coated perovskites on textured silicon for 26%-efficient

[1] C. H. Henry, Limiting efficiencies of ideal single and multi- ple energy gap terrestrial solar cells, J. Appl. Phys., 4494 (1980).

023005-10

monolithic perovskite/silicon tandem solar cells, Joule, 850 (2020). [16] A. S. Subbiah, F. H. Isikgor, C. T. Howells, M. De Bas- tiani, J. Liu, E. Aydin, F. Furlan, T. G. Allen, F. Xu,

S. Zhumagali, *et al.*, High-performance perovskite single- junction and textured perovskite/silicon tandem solar cells via slot-die-coating, ACS Energy Lett.**5**, 3034 (2020).
[17] See the Supplemental Material at [http://link.aps.org/supple](http://link.aps.org/supple) mental/10.1103/PRXEnergy.1.023005 for device details. [18] L. Xu, J. Liu, F. Toniolo, M. De Bastiani, M. Babics, W. Yan, F. Xu, J. Kang, T. Allen, A. Razzaq, *et al.*, Monolithic perovskite/silicon tandem photovoltaics with minimized cell-to-module losses by refractive-index engineering, ACS Energy Lett.**7**, 2370 (2022). [19] S. Albrecht, M. Saliba, J.-P. Correa-Baena, K. Jäger, L. Korte, A. Hagfeldt, M. Grätzel, and B. Rech, Towards opti- cal optimization of planar monolithic perovskite/silicon- heterojunction tandem solar cells, J. Opt. **18**, 064012 (2016). [20] H. Shen, D. Walter, Y. Wu, K. C. Fong, D. A. Jacobs, T. Duong, J. Peng, K. Weber, T. P. White, and K. R. Catchpole, Monolithic perovskite/Si tandem solar cells: Pathways to over 30% efficiency, Adv. Energy Mater. **377**, 1902840 (2020). [21] R. Santbergen, R. Mishima, T. Meguro, M. Hino, H. Uzu, J. Blanker, K. Yamamoto, and M. Zeman, Minimizing optical losses in monolithic perovskite/*c*-Si tandem solar cells with a flat top cell, Opt. Express **24**, A1288 (2016). [22] D. T. Grant, K. R. Catchpole, K. J. Weber, and T. P. White, Design guidelines for perovskite/silicon 2-terminal tan- dem solar cells: An optical study, Opt. Express **24**, A1454 (2016). [23] F. E. Subhan, A. D. Khan, A. D. Khan, N. Ullah, M. Imran, and M. Noman, Optical optimization of double- side-textured monolithic perovskite–silicon tandem solar cells for improved light management, RSC Adv.**10**, 26631 (2020). [24] J. Zheng, C. F. J. Lau, H. Mehrvarz, F.-J. Ma, Y. Jiang,

X. Deng, A. Soeriyadi, J. Kim, M. Zhang, L. Hu, *et* *al.*, Large area efficient interface layer free monolithic perovskite/homo-junction-silicon tandem solar cell with over 20% efficiency, Energy Environ. Sci.**11**, 2432 (2018).
[25] D. A. Jacobs, M. Langenhorst, F. Sahli, B. S. Richards, T.

P. White, C. Ballif, K. R. Catchpole, and U. W. Paetzold, Light management: A key concept in high-efficiency per- ovskite/silicon tandem photovoltaics, J. Phys. Chem. Lett. **10**, 3159 (2019).
[26] O. Dupré, A. Tuomiranta, Q. Jeangros, M. Boccard, P. Alet, and C. Ballif, Design rules to fully benefit from bifaciality in two-terminal perovskite/silicon tandem solar cells, IEEE

J. Photovolt.**10**, 714 (2020).
[27] S. Manzoor, J. Häusele, K. A. Bush, A. F. Palmstrom, J. Carpenter, Z. J. Yu, S. F. Bent, M. D. McGehee, and Z. C. Holman, Optical modeling of wide-bandgap perovskite and perovskite/silicon tandem solar cells using complex refrac- tive indices for arbitrary-bandgap perovskite absorbers, Opt. Express **26**, 27441 (2018).

[28] M. A. Green, Self-consistent optical parameters of intrin- sic silicon at 300 K including temperature coefficients, Sol. Energy Mater. Sol. Cells **92**, 1305 (2008). [29] S. C. Baker-Finch, K. R. McIntosh, D. Yan, K. C. Fong, and T. C. Kho, Near-infrared free carrier absorp- tion in heavily doped silicon, J. Appl. Phys. **116**, 063106 (2014). [30] J. Isenberg and W. Warta, Free carrier absorption in heavily doped silicon layers, Appl. Phys. Lett. **84**, 2265 (2004). [31] M. De Bastiani, M. Babics, E. Aydin, A. S. Subbiah, L. Xu, and S. De Wolf, All set for efficient and reliable per- ovskite/silicon tandem photovoltaic modules?, Sol. RRL **6**, 2100493, (2021). [32] K. R. McIntosh, G. Lau, J. N. Cotsell, K. Hanton, D. L. Bätzner, F. Bettiol, and B. S. Richards, Increase in external quantum efficiency of encapsulated silicon solar cells from a luminescent down-shifting layer, Prog. Photovolt.**17**, 191 (2009). [33] LOANA Solar cell analysis system, [http://www.pv-tools](http://www.pv-tools). de/products/loana-system/loana-start.html [34] PVlighthouse, [https://www.pvlighthouse.com.au/](https://www.pvlighthouse.com.au/) [35] S. C. Baker-Finch and K. R. McIntosh, Reflection of nor- mally incident light from silicon solar cells with pyramidal texture, Prog. Photovolt.**19**, 406 (2011). [36] T. H. Fung, M. U. Khan, Y. Zhang, N. J. Western, D. N.

R. Payne, K. R. Mclntosh, and M. D. Abbott, Improved ray tracing on random pyramid texture via application of Phong scattering, IEEE J. Photovolt.**9**, 591 (2019).
[37] See the Supplemental Material at [http://link.aps.org/supple](http://link.aps.org/supple) mental/10.1103/PRXEnergy.1.023005 for the Phong expo- nent. [38] B. T. Phong, Illumination for computer generated pictures, Commun. ACM **18**, 311 (1975). [39] O. Höhn, N. Tucher, and B. Bläsi, Theoretical study of pyramid sizes and scattering effects in silicon photovoltaic module stacks, Opt. Express **26**, A320 (2018). [40] K. R. McIntosh, T. G. Allen, S. C. Baker-Finch, and M. D. Abbott, Light trapping in isotextured silicon wafers, IEEE

J. Photovolt.**7**, 110 (2017).
[41] S. C. Baker-Finch, K. R. McIntosh, and M. L. Terry, Iso- textured silicon solar cell analysis and modeling 1: Optics, IEEE J. Photovolt.**2**, 457 (2012). [42] Y. Li, Z. Li, Y. Zhao, and A. Lennon, Modelling of light trapping in acidic-textured multicrystalline silicon wafers, Int. J. Photoenergy **2012**, 369101 (2012). [43] K. R. McIntosh, M. D. Abbott, and B. A. Sudbury, Ray Tracing Isotextured Solar Cells, Energy Procedia **92**, 122 (2016). [44] See the Supplemental Material at [http://link.aps.org/supple](http://link.aps.org/supple) mental/10.1103/PRXEnergy.1.023005 for the characteristic angle of spherical caps. [45] See the Supplemental Material at [http://link.aps.org/supple](http://link.aps.org/supple) mental/10.1103/PRXEnergy.1.023005 for the glass texture. [46] J. Dupuis, E. Saint-Sernin, O. Nichiporuk, P. Lefillastre, D. Bussery, and R. Einhaus, in *2012 38th IEEE Photovoltaic* *Specialists Conference* (2012), pp. 003183.

023005-11
