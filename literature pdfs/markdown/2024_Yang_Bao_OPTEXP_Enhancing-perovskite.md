**Research Article** Vol. 32, No. 6 / 11 Mar 2024 / *Optics Express*

# Enhancing perovskite-silicon tandem solar cells through numerical optical and electric

# optimizations for light management

## JINPENG YANG1,3 AND QINYE BAO2,4

*1* *College of Physical Science and Technology, Yangzhou University, Jiangsu 225009, China* *2* *School of Physics and Electronic Science, East China Normal University, Shanghai 200241, China* *3* *jpyang@yzu.edu.cn* *4* *qybao@clpm.ecnu.edu.cn*

**Abstract:** We integrated optical and electrical numerical simulations to precisely investigate the effectiveness of using a pyramidal perovskite (Cs0.18FA0.82Pb(I,Br)3) nanostructured film as an example in perovskite-silicon tandem solar cells to reduce reflective losses and balance the current densities. Through our calculations, the PCE of tandem solar cells can be improved from

29.2% (the planar structures without texturing) to 36.1% in the best-performing textured tandem devices under the consistently calculated absorbed and EQE spectrum, where the predicted open-circuit voltage could reach over 2V. These findings offer valuable theoretical insights for the advancement and optimization of perovskite-silicon tandem solar cells. © 2024 Optica Publishing Group under the terms of theOptica Open Access Publishing Agreement
### 1. Introduction

Despitethecurrentdominanceofcrystallinesilicon(c-Si)devicesinthephotovoltaic(PV)market, perovskite-silicon tandem architectures have garnered significant attention due to their potential performance could surpass the Shockley-Queisser limit of single silicon. [1–5] In a typical perovskite-silicon tandem solar cell with a monolithic (two-terminal) configuration, a crystalline silicon (c-Si) bottom cell is used in combination with a perovskite top cell. [6–8] The perovskite top cell absorbs high-energy photons, while the c-Si bottom cell absorbs low-energy photons transmitted through the top perovskite layers. Recently, a PCE exceeding 31% has been reported in perovskite-silicon tandem after optimization of the optical structure and bandgap of perovskite film. [9] However, the theoretical Shockley-Queisser limit, which is based on detailed balance, suggests that PCE in perovskite-silicon tandem solar cell could reach up to 45% [10], highlighting the need for further study. Several factors could affect the PCE in perovskite-silicon tandem devices, such as parasitic absorption limited by energy bandgap, defects induced nonradiative recombination, undesirable series/shunt resistance for large modules, and structure geometry induced optical losses. In particular, reflective losses can significantly limit matched photocurrent density in fully planar tandem devices. Therefore, significant efforts have been dedicated to the development of textured nanostructures for effective light trapping. [11–15] Textured interfaces have the ability to reduce losses caused by reflection through two mech- anisms: enhancing the coupling of light into the structure, and scattering light in a way that increases the average path length within the absorber, which results in enhanced absorption, particularly in weak absorbing region. Previous numerical simulations using programs like GENPRO4, CROWM, or JCMsuite have made attempts to address the light trapping effect. [15–20] These simulations, with focusing on the optical geometry, have revealed that absorption in the perovskite top cell can significantly impact the efficiency of perovskite-Si tandem solar cells, and emphasize the importance of careful photon management. However, there is still a lack of comprehensive theoretical study that can effectively integrate two following aspects: (i) the utilization of optical structures to balance photocurrent density in perovskite-silicon tandem

#513887 [https://doi.org/10.1364/OE.513887](https://doi.org/10.1364/OE.513887) Journal © 2024 Received 2 Jan 2024; revised 12 Feb 2024; accepted 13 Feb 2024; published 26 Feb 2024

solar cells, while considering the angular dependence of incident light, (ii) accurately predicting current-voltage characteristics with considering additional electric parameters. Such separate understanding hampers the ability to further optimize and achieve the maximum PCE in realistic perovskite-Si tandem solar cells. In this study, we employ a combination of optical and electrical calculations utilizing the finite element method to investigate the influence of pyramidal nanostructures on the top perovskite sub-cell (using Cs0.18FA0.82Pb(I,Br)3as an example) on the PCE of perovskite-Si tandem solar cells. Our objective is to assess the effectiveness of these nanostructures in reducing reflective losses and balancing current densities in perovskite-Si tandem devices. We systematically studied three different architectures of perovskite layers. The results demonstrated that the best-performing nanostructured perovskite-Si tandem device exhibits a significant enhancement in PCE, reaching up to 23.8% improvement compared to its planar structure. Additionally, angular-dependent current density change indicates that the textured surface has the potential to alleviate current density mismatch issues between perovskite and silicon films in tandem solar cells.

### 2. Simulation method and device structures

The optical simulations in this study are performed using the COMSOL Multiphysics software, specifically utilizing its two-dimensional model and the finite element method. The simulated domain consists of a stack of layers treated as coherent or incoherent depending on the film thickness, and embedded in semi-infinite air spaces on top and bottom, which are treated as incoherent layers. Here, we employed the actual thickness of each layer during the calculation without using any approximation, particularly in the case of thicker silicon wafers. From each simulated layer, equivalent photocurrent densities can be calculated with the following equation: ∫1200 *nm* *J* *i*= e A*i*(λ)×*AM*1.5(λ)*d*λ (1) 300 *nm*

where Jirepresents the absorbed current density corresponding to the absorption profile of the i-th layer (Ai(λ)). ΦAM1.5represents the photon flux based on the AM 1.5G spectrum [21], and e denotes the elementary charge. The photocurrent densities obtained for the perovskite and silicon layers are considered as the maximum achievable current densities. This assumption is made that all the light absorbed in the solar cell can be converted into electron-hole pairs, which are then extracted to generate electrical current. On the other hand, the current densities observed in the remaining layers represent losses attributed to parasitic absorption. The absorbed spectrum can simultaneously change with variations in the incident light angle, thereby necessitating the investigation of angular-dependent Ji. To perform accurate simulations, the complex refractive index spectra (n, k) are taken from and given in [22]Supplement 1, Fig. S1. The electric calculations were performed using software SCAPS [23–25] for one dimensional perovskite-Si tandem solar cells. The current-voltage characteristics of solar cells were simulated under a standard AM1.5G spectrum with 100mW cm −2 intensity across a voltage range of 0-2V. The electrical parameters used in this simulation are listed in Table S1. The performance of the top perovskite solar cells is directly simulated using a standard AM1.5G spectrum after filtering out reflections (utilizing results of 1-R, calculated from optical simulation). In contrast, the bottom silicon solar cells make use of the remaining incident light after passing through the layers of the top perovskite solar cells. In order to achieve a maximum PCE, we strive to achieve a nearly identical current density match for both the top perovskite and bottom silicon in monolithic tandem devices. Figure1shows the three main architectures of the perovskite-Si tandem solar cells studied in this work with flat and/or textured top c-Si surfaces. Figure1(a) illustrates a simple architecture commonly found in literature [9,26,27], featuring a “double-side” flat perovskite top cell for

a direct comparison. In Fig.1(b), only the intermediate layers between the Si absorber and perovskite absorber are textured, while the interfaces on top of the perovskite layers remain flat. In experimental setups, the spin-coating technique is employed to grow perovskite layers on textured silicon substrates, resulting in nearly flat perovskite on top. Figure1(c) depicts the architecture with a “double-side” textured perovskite top cell, where the front-side textured perovskite can be achieved through nanoimprint processes or by utilizing continuous vacuum deposition for conformal growth of the perovskite films. To enhance light trapping and absorption from silicon in the near infrared wavelength region, textured architectures obtained from experiments [26] are implemented on the back surface of c-Si. For the top perovskite sub-cell, it is assumed that all textured interfaces possess the same texture. A period of 300nm with a depth of 300nm is employed for all textured perovskite and other related layers to ensure sufficient light trapping [16,27]. Filmthicknessesarechosenbasedonexperimentaldevicesandoptimizationasdiscussed in the later section.

**Fig. 1Fig. 1.** Schematic diagram of the monolithic perovskite-Si tandem devicesSchematicdiagramofthemonolithicperovskite-Sitandemdevicesutilizedforoptical

and electric simulations. (a)- (c) are defined as “textured back-side-only” silicon, “textured

## utilized for optical and electric simulations. (a)- (c) are defined as “textured

double-side” silicon with “textured back-side” perovskite, and “textured double-side” silicon back-side-only” silicon, “textured double-side” silicon with “textured back-side”with “textured double-side” perovskite, respectively. The film thicknesses of electrodes and antireflective coating (AR-LiF) employed in the simulations are also indicated. It should

## perovskite, and “textured double-side” silicon with “textured double-side”

be noted that the thickness of the perovskite films varies depending on the optimization of

## perovskite, respectively. The film thicknesses of electrodes and antireflective matched current densities.

## coating (AR-LiF) employed in the simulations are also indicated. It should be

## noted that the thickness of the perovskite films varies depending on the

### 3. Results

## optimization of matched current densities.

To begin, we examined the effects of an antireflective coating (AR-LiF) on the absorbed spectrum in a perovskite-Si tandem device configuration where both the back side of perovskite and double **3. Results** sides of silicon are textured (depicted as (b) in Fig.1). In Fig.2(a), typical absorbed spectrum of

## To begin, we examined the effects of an antireflective coating (AR-LiF)

perovskite and silicon films are illustrated, comparing the cases with and without using AR-LiF. It can be seen that adding AR-LiF layers could result in increased absorptions for both the topon the absorbed spectrum in a perovskite-Si tandem device configuration where

## both the back side of perovskite and double sides of silicon are textured

## (depicted as (b) in Figure 1). In Figure 2(a), typical absorbed spectrum of

## perovskite and silicon films are illustrated, comparing the cases with and

## without using AR-LiF. It can be seen that adding AR-LiF layers could result in

## increased absorptions for both the top perovskite and bottom silicon films,

## suggesting the effectiveness of reducing reflection loss at the air/ITO surface

## and emphasizing the necessity of inserting low refractive index materials

## between the air and ITO, even when textured interfaces have been utilized (see

## an additional case in Figure S2(a) for device structure from Figure 1(a)).

## Furthermore, analysis of the 1-R spectra reveals that reflection losses primarily

perovskite and bottom silicon films, suggesting the effectiveness of reducing reflection loss at the air/ITO surface and emphasizing the necessity of inserting low refractive index materials between the air and ITO, even when textured interfaces have been utilized (see an additional case inSupplement 1, Fig. S2(a) for device structure from Fig.1(a)). Furthermore, analysis of the 1-R spectra reveals that reflection losses primarily occur in the wavelength range below 500nm.

## occur in the wavelength range below 500 nm. This phenomenon can be partially

This phenomenon can be partially attributed to the absorption characteristics of ITO, specifically

## attributed to the absorption characteristics of ITO, specifically its extinction

its extinction coefficient (k value).

## coefficient (k value).

**Fig. 2**

**Fig. 2.**

## illustrates the simulated absorbed and the 1-total reflection (1-R)

illustrates the simulated absorbed and the 1-total reflection (1-R) spectrum for different perovskite-Si tandem architectures. In panel (a), we observe the absorption and 1-R spectrum for different perovskite-Si tandem architectures. In panel (a), wechanges in perovskite-Si tandem devices (device structure is shown in Fig.1(b)), both with

## observe the absorption and 1-R changes in perovskite-Si tandem devices

and without the implementation of an antireflective coating (AR-LiF). Panel (b) showcases the variation in absorbed spectrum among three tandem devices from Fig.1, where shaded

## (device structure is shown in

areas give spectrum change for direct comparison. The dash-dot line denotes the impact

**Figure 1(b)**), both with and without the

implementation of an antireflective coating (AR-LiF). Panel (b) showcases theof C₆₀ absorption, and the dashed-symbol line represents absorbed spectra change in the near-infrared wavelength region due to the absence of textured back side of silicon (device

## variation in absorbed spectrum among three tandem devices from

structure is from Fig.1(b)). It is important to note that a constant perovskite film with

**Figure 1**,

where shaded areas give spectrum change for direct comparison. The dash-dot thickness of 560nm is maintained (not thickness optimized) during the calculation.

## line denotes the impact of C₆₀ absorption, and the dashed-symbol line represents

In Fig.2(b), a direct comparison is presented, illustrating the changes in absorbed spectrum for

## absorbed spectra change in the near-infrared wavelength region due to the

different interfacial structures (either with planar or textured configurations). The thickness of the perovskite films used in all of the tandem device architectures was fixed at 560nm, without any

## absence of textured back side of silicon (device structure is from Figure 1(b)).

additional thickness optimization. However, it should be noted that a typical balanced absorption

## It is important to note that a constant perovskite film with thickness of 560 nm

after undergoing thickness optimization can be found in previously published results. [

## is maintained (not thickness optimized) during the calculation.

5,28] For the device architecture featuring “textured back-side only Si” (as shown in Fig.1(a)), relatively low absorption is observed in silicon, indicating the great loss of incident light in the 800-1200nm

## In Figure 2(b), a direct comparison is presented, illustrating the changes

wavelength range due to the reflection. The dependence of silicon absorption spectrum on in absorbed spectrum for different interfacial structures (either with planar or thickness for the device architecture with “textured back-side only Si” is also illustrated in

## textured configurations). The thickness of the perovskite films used in all of the

Supplement 1, Fig. S2(b). Notably, a significant enhancement is achieved when changing architectures from the “textured back-side only Si” to the “textured double-side Si

## tandem device architectures was fixed at 560 nm, without any additional

+ back-side PVK” (as depicted in Fig. thickness optimization. However, it should be noted that a typical balanced 1(b)), particularly in the absorption region from the silicon films, although a minor amount of reflection loss (on the top of spectra) remains. Furthermore, our

## absorption after undergoing thickness optimization can be found in previously

findings confirm that (i) the losses in the low wavelength region (below 500nm) can primarily be

## published results. [28, 29] For the device architecture featuring "textured back-

attributed to the absorption of C₆₀ films, as indicated by the dash-dot lines. It is observed that with a thinner C

## side only Si" (as shown in

60film, there is higher absorption for the perovskite film (Two different thickness

**Figure 1(a)**), relatively low absorption is observed

of C in silicon, indicating the great loss of incident light in the 800-1200 nmare compared during our calculations and presented inSupplement 1, Fig. S3). We

## wavelength range due to the reflection. The dependence of silicon absorption

## spectrum on thickness for the device architecture with "textured back-side only

have further shown exemplary comparisons between our calculations and experimental results obtained from the literature (refer to Fig. S4), revealing a high degree of agreement [8,9,29]; (ii) the implementation of a textured back-side silicon structure improves the spectral response in the 1000-1200nm infrared wavelength range (after comparing red-symbol dash line with a blue shadow), and (iii) further improvements can be achieved by changing the perovskite films to demonstrate a “textured double-side Si + PVK” architecture (also seen in Fig.1(c)), leading to the highest absorption percentage both in silicon and perovskite (highlighted with a pink shadow). Once we have gained insights into the influences of various device structures on the absorbed spectrum of top perovskite and bottom silicon sub-cells, we can proceed to calculate the “ideal” maximum absorbed current density (*Jmax* *Ph* ) generated separately by the perovskite and silicon absorbers using equation (1). To optimize the performance of perovskite-Si tandem devices, we only need to adjust the thickness of the perovskite films in order to maximize the matching point of current densities, while keeping the thicknesses of other films unchanged. The current densities of the limiting sub-cells can be determined by the following equation:

*ph ph* min(*J* *max*,*PVK*, *J* *max*,*Si* )→ max (2)

Figure3shows the evolution of perovskite film thickness (d) on the maximum absorbed current

## but rather resembles a parabolic trend. According to our simulations, the

densities of the top perovskite and bottom silicon sub-cells according to three tandem devices depicted in Fig. maximum matched current densities for the device structures shown in (a)-(c)1. The observed trends are consistent across these tandem devices: (i) a gradual *ph* 2 *ph*2 2 decrease in of **Figure 1***Jmax* are 16.43 mA/cm,*PVK*and a simultaneous increase in, 19.54 mA/cm*Jmax*, and 20.45 mA/cm,*Si*can be observed when the thickness of, respectively. perovskitefilmisreduced; (ii)therelationshipdoesnotfollowalinearpatternbutratherresembles

## These results strongly confirm the efficiency of employing textured interfaces

a parabolic trend. According to our simulations, the maximum matched current densities for the device structures shown in (a)-(c) of Fig.

## to realize light trapping and enhance absorption. Additionally, we demonstrate

1are 16.43mA/cm², 19.54mA/cm², and 20.45mA/cm², respectively. These results strongly confirm the efficiency of employing textured interfaces to that both textured interfaces, not only in the bottom silicon structure but also in realize light trapping and enhance absorption. Additionally, we demonstrate that both textured

## the top perovskite films, are highly effective, resulting in enhancements of 18.9%

interfaces, not only in the bottom silicon structure but also in the top perovskite films, are highly

## (for “textured back-side” perovskite) and 24.5% (for “textured double-side”

effective, resulting in enhancements of 18.9% (for “textured back-side” perovskite) and 24.5% (for “textured double-side” perovskite) respectively. perovskite) respectively.

**Fig. 3.** The optimization process for adjusting the perovskite thickness to achieve maximum

**Fig. 3**

matched absorbed current densities from the top perovskite and bottom silicon sub-cells.

##. The optimization process for adjusting the perovskite thickness to

achieve maximum matched absorbed current densities from the top perovskite The results are given based on three different perovskite-Si tandem devices with the changed

## and bottom silicon sub-cells. The results are given based on three different

thickness of the perovskite films (d) indicated on the inset of the figure.

perovskite-Si tandem devices with the changed thickness of the perovskite films (d) indicated on the inset of the figure.

The angular-dependent performance is also an important factor for solar cells without using active light-tracking. **Figure 4** provides valuable insights

## into this aspect by illustrating the variation of normalized maximum matched

## current density with respect to the angle of incident light for both the top

## perovskite and bottom silicon sub-cells under the consideration of three

The angular-dependent performance is also an important factor for solar cells without using active light-tracking. Figure4provides valuable insights into this aspect by illustrating the variation of normalized maximum matched current density with respect to the angle of incident light for both the top perovskite and bottom silicon sub-cells under the consideration of three optimized perovskite-Si tandem devices. The textured tandem devices (referred to as back-side

## devices. Conversely, the "double-side" flat tandem device (referred to as flat

PVK and double-side PVK) exhibit a slight decrease in normalized current densities (JPVKand

|PVK) shows different behavior for J|. In this case, a disparity between J||and|
|---|---|---|---|
|Si|sc||PVK|
|Si|PVK|Si||
|||PVK||

sc PVK J Si) when the angle of incident light increases from 0 degree to 30 degrees. Such a consistent tendency in the current densities for both J J can be observed as the incident angle varies from 30 degrees to 60 degrees,and J indicates a good match for maintaining high short-circuit current density (J indicating insufficient light absorption and clear mismatch of current densities. sc) when they are stacked in series and formed tandem devices. Conversely, the “double-side” flat tandem device (referred to as flat PVK) shows different

## Consequently, the perovskite-Si tandem solar cells under such an architecture

behavior for Jsc. In this case, a disparity between J and JSican be observed as the incident angle varies from 30 degrees to 60 degrees, indicating insufficient light absorption and clear

## would exhibit low PCE. Therefore, these discrepancies should be taken into

mismatch of current densities. Consequently, the perovskite-Si tandem solar cells under such account during structure design. Notably, the advantage in absorption and an architecture would exhibit low PCE. Therefore, these discrepancies should be taken into

## current densities provided by the textured perovskite films, whether "back-side

account during structure design. Notably, the advantage in absorption and current densities provided by the textured perovskite films, whether “back-side textured” or “double-side textured,”

## textured" or "double-side textured," is maintained over a wide-angle range. This

is maintained over a wide-angle range. This finding supports the application of using textured

## finding supports the application of using textured interfaces/surfaces for tandem

interfaces/surfaces for tandem solar cells. solar cells.

**Fig.4** The angular dependence of the normalized maximum matched current**Fig. 4.** The angular dependence of the normalized maximum matched current densities

## densities for both the top perovskite (J

for both the top perovskite (JPVK) and bottom silicon (J PVK) and bottom silicon (J Si) sub-cells in three perovskite-Si Si) sub-cells in tandem solar cells with architectures depicted in Fig.1.

## three perovskite-Si tandem solar cells with architectures depicted in Figure 1.

Finally, we performed calculations of the current density-voltage characteristics to estimate

## Finally, we performed calculations of the current density-voltage

the potential PCE of the tandem solar cells after combining our obtained optically simulated characteristics to estimate the potential PCE of the tandem solar cells after results and assuming the all absorbed photons could be efficiently converted into electric current.

## combining our obtained optically simulated results and assuming the all

Therefore, our calculated electrical results represent the “ideal” maximum value of device performance that can be obtained by combining the absorption from optical calculations, without

## absorbed photons could be efficiently converted into electric current. Therefore,

considering any defects. The detailed semiconductor parameters for device simulations are listed

## our calculated electrical results represent the "ideal" maximum value of device

in performance that can be obtained by combining the absorption from opticalSupplement 1, Table S1. In Fig.5, the left side displays the calculated current density-voltage curves of three different perovskite-Si tandem solar cells, where the tandem architectures are

## calculations, without considering any defects. The detailed semiconductor

depicted in Fig.1. To provide detailed comparison, we also include the individual current density-voltage curves of the top perovskite and bottom silicon sub-cells. On the right side

## parameters for device simulations are listed in Table S1. In Figure 5, the left

of Fig. side displays the calculated current density-voltage curves of three different5, we present the calculated external quantum efficiency (EQE) obtained through our electric simulations using SCAPS, along with the absorptions and reflections (1-R) derived

## perovskite-Si tandem solar cells, where the tandem architectures are depicted in

from optical simulations for better comparison. In the perovskite-silicon tandem solar cell

**Figure 1**. To provide detailed comparison, we also include the individual

## current density-voltage curves of the top perovskite and bottom silicon sub-cells.

## On the right side of Figure 5, we present the calculated external quantum

featuring a planar perovskite film (right side of Fig.5(a)), we could achieve a PCE of 29.20%, which is accompanied by a Jscof 16.19mA/cm², open-circuit voltage (Voc) of 2.10V, and fill factor (FF) of 85.8%. A significant enhancement in the PCE can be observed, reaching 34.61% (Fig.5(b)), when we change top perovskite sub-cells from a planar to a “back-side textured” structure. The noteworthy improvement in PCE is primarily attributed to a substantial increase in the Jscwhich reaches 19.32mA/cm², while having a negligible impact on the Vocand FF. A slight additional enhancement could be further observed when top perovskite sub-cell changes from “back-side textured” to a “double-side textured” structure, leading to a minor increase in the J scfrom 19.32mA/cm² to 20.18mA/cm², as illustrated in Fig.5(c). Table1provides a summary of the calculated results on the tandem device performance obtained from Fig.5. On the right side of Fig.5, we observe a strong agreement between the External Quantum Efficiency (EQE) and absorbed spectra, both from top perovskite and bottom silicon sub-cells. This agreement serves as further confirmation of the accuracy from our electric calculations, which appropriately incorporated optically simulated results. Furthermore, three exemplary comparisons given in Supplement 1, Fig. S5 highlight the importance of high crystallinity and low defects in preparing perovskite films for achieving higher PCE in tandem solar cells. A detailed study on defects and other electrical parameters that could affect device performance will be continuously studied in the future.

**Fig. 5**

**Fig. 5.**

## Calculated current-voltage characteristics of perovskite-Si tandem solar

Calculated current-voltage characteristics of perovskite-Si tandem solar cells with “planar or textured” perovskite films, displaying both the individual and total contributions cells with "planar or textured" perovskite films, displaying both the individualfrom the top perovskite and bottom silicon sub-cells. The left side of the figure includes

## and total contributions from the top perovskite and bottom silicon sub-cells. The

(a)-(c), which correspond to the same device architectures illustrated in (a)-(c) of Fig.1. The right side of figure presents the calculated External Quantum Efficiency (EQE), as well as
## left side of the figure includes (a)-(c), which correspond to the same device

the absorptions and reflections (1-R) exhibited by these three tandem solar cells. Note that architectures illustrated in (a)-(c) ofour calculation does not take into account any additional impacts on defects.**Figure 1**. The right side of figure presents

## the calculated External Quantum Efficiency (EQE), as well as the absorptions

## and reflections (1-R) exhibited by these three tandem solar cells. Note that our

## calculation does not take into account any additional impacts on defects.

**Table 1.** A summary of the calculated results on the tandem device performance obtained from Figure 5.

## Voc (V) Jsc (mA/cm²) FF PCE

**Table 1. A summary of the calculated results on the tandem device performance obtained from Fig.5.**

|||Voc(V)|Jsc(mA/cm|2) FF|PCE|
|---|---|---|---|---|---|
|Planar||2.10|16.19|85.8%|29.17%|
|Back-side textured||2.10|19.32|85.3%|34.61%|
|Double-side textured||2.10|20.18|85.3%|36.14%|

### 4. Conclusions and outlook

To fully unlock the potential of perovskite-Si tandem solar cells, optimizing their optical performance is crucial. In this manuscript, we present the results of current density optimization for perovskite-Si tandem solar cells using Cs0.18FA0.82Pb(I,Br)3as an example with considering three different textured perovskite top sub-cells: “double-side flat,” “back-side textured,” and “double-side textured” perovskite films. Because the textured structures can reduce the reflective losses and increase light absorption, higher balanced Jsceven with large angular dependence of tolerance in perovskite-Si tandem devices are obtained. An additional cumulative Jscwith >3mA/cm² can be generated in the two sub-cells with respect to the regular tandem architecture of a “double-side flat” perovskite film. To achieve maximal matched current densities for both the top perovskite and back silicon sub-solar cells, perovskite films with double-sided textured architectures are recommended. Through our research, we have observed that employing this “double-sided textured” perovskite-silicon tandem solar cells can lead to maximum matched current densities of up to 20.18mA/cm², representing an improvement of up to 24.6% compared to the planar structure. In “double-side flat” perovskite films, reflection loss emerges as a major obstacle to effectively utilizing incident light. To address this issue, light management techniques must be employed. Firstly, applying an antireflective coating on the front side is essential. Secondly, implementing light trapping methods such as texturing not only on the back side of the bottom silicon sub-cell to enhance c-Si absorption in the infrared wavelength range but also on the front perovskite sub-cell can increase the average path length within the absorber and balance the photon generated current densities. Thirdly, by texturing both sides of the perovskite films, the reflective loss can be further reduced compared to only texturing the back side of the perovskites. The double-side textured tandem structures facilitate current matching, thereby maximizing the overall photocurrent density (as well as PEC) in perovskite-silicon tandem. This could lead to an increase in the maximum PEC from 29.20% in the optimized planar reference to 36.14% in the best-performing textured tandem device. Additionally, it is important to change the angles of incident light to study the evolution of “ideally” generated maximum current densities independently for the top perovskite and bottom silicon sub-cells. Maintaining consistent changes in the maximum generated current densities between the top and bottom sub-cells as the incident angle varies is also crucial. Tandem solar cells with textured architectures can help achieve this consistency. **Funding.** National Natural Science Foundation of China (62375234, 62322407, 22279034, 52261145698); National Key Research and Development Program of China (2022YFB3803300); Science and Technology Innovation Plan Of Shanghai Science and Technology Commission (22ZR1418900). **Acknowledgments.** We would like to acknowledge Professor Yadong Xu from Soochow University for the support of Electromagnetic simulations. **Disclosures.** The authors declare no conflicts of interest. **Data availability.** Data underlying the results presented in this paper are not publicly available at this time but may be obtained from the authors upon reasonable request. **Supplemental document.** SeeSupplement 1for supporting content.

**References**

1. P. Löper, S.-J. Moon, S. M. de Nicolas, *et al.*, “Organic-inorganic halide perovskite/crystalline silicon four-terminal tandem solar cells,”Phys. Chem. Chem. Phys.**17**(3), 1619 (2014).
2. T. Todorov, T. Gershon, O. Gunawan, *et al.*, “Perovskite-kesterite monolithic tandem solar cells with high open-circuit voltage,”Appl. Phys. Lett.**105**(17), 173902 (2014).
3. M. H. Futscher and B. Ehrler, “Modeling the performance limitations and prospects of perovskite/Si tandem solar cells under realistic operating conditions,”ACS Energy Lett.**2**(9), 2089 (2017).
4. K. Bush, A. Palmstrom, Z. Yu, *et al.*, “23.6%-efficient monolithic perovskite/Silicon tandem solar cells with improved stability,”Nat. Energy **2**(4), 17009 (2017).
5. J. Werner, C.-H. Weng, A. Walter, *et al.*, “Efficient monolithic perovskite/silicon tandem solar cell with cell area >1 cm2,”J. Phys. Chem. Lett.**7**(1), 161 (2016).
6. Hui Li and Wei Zhang, “Perovskite tandem solar cells: from fundamentals to commercial deployment,”Chem. Rev. **120**(18), 9835 (2020).
7. L. Duan, D. Walter, N. Chang, *et al.*, “Stability challenges for the commercialization of perovskite-silicon tandem solar cells,”Nat. Rev. Mater.**8**(4), 261 (2023).
8. S. Mariotti, E. Köhnen, F. Scheler, *et al.*, “Interface engineering for high-performance triple-halide perovskite–silicon tandem solar cells,”Science **381**(6653), 63 (2023).
9. X. Y. Chin, D. Turkay, J. A. Steele, *et al.*, “Interface passivation for 31.25%-efficient perovskite/Silicon tandem solar cells,”Science **381**(6653), 59 (2023).
10. M. H. Futscher and B. Ehrler, “Efficiency limit of perovskite/Si tandem solar cells,”ACS Energy Lett.**1**(4), 863 (2016).
11. R. Santbergen, R. Mishima, T. Meguro, *et al.*, “Minimizing optical losses in monolithic perovskite/c-Si tandem solar cells with a flat top cell,”Opt. Express **24**(18), A1289 (2016).
12. D. T. Grant, K. R. Catchpole, K. J. Weber, *et al.*, “Design guidelines for perovskite/silicon 2-terminal tandem solar cells: an optical study,”Opt. Express **24**(22), A1454 (2016).
13. K. Jager, L. Korte, B. Rech, *et al.*, “Numerical optical optimization of monolithic planar perovskite-silicon tandem solar cells with regular and inverted device architectures,”Opt. Express **25**(12), A473 (2017).
14. L. Mazzarella, M. Werth, K. Jager, *et al.*, “Infrared photocurrent management in monolithic perovskite/Silicon heterojunction tandem solar cells by using a nanocrystalline silicon oxide interlayer,”Opt. Express **26**(10), A488 (2018).
15. M. Filipič, P. Löper, B. Niesen, *et al.*, “CH3NH3PbI3 perovskite/Silicon tandem solar cells: characterization based optical simulations,”Opt. Express **23**(7), A263 (2015).
16. D. Chen, P. Manley, P. Tockhorn, *et al.*, “Nanophotonic light management for perovskite–silicon tandem solar cells,”
J. Photonics Energy **8**(02), 022601 (2018).
17. S. Albrecht, M. Saliba, J. P. Correa-Baena, *et al.*, “Towards optical optimization of planar monolithic peerovskite/silicon-heterojunction tandem solar cells,”J. Opt.**18**(6), 064012 (2016).
18. B. Lipovsek, J. Krc, and M. Topic, “Optical model for thin-film photovoltaic devices with large surface textures at the front side,” J. Microelectron. Electron. Components Mater.**41**, 264 (2011).
19. R. Santbergen and R. J. C. van Zolingen, “The absorption factor of crystalline silicon PV cells: A numerical and experimental study,”Sol. Energy Mater. Sol. Cells **92**(4), 432 (2008).
20. D.Zhang,W.Verhees,M.Dorenkamper, *et al.*,“Combinationofadvancedopticalmodelingwithelectricalsimulations for performance evaluation of practical 4-terminal perovskite/c-Si tandem modules,”Energy Procedia **92**, 669 (2016).
21. IEC: 60904–3: Photovoltaic device−Part 3: Measurements principles for terrestrial photovoltaic (PV) solar devices with reference spectral irradiance data (2008).
22.M. Polyanskiy, Refractive Index INFO (2008).[https://refractiveindex.info/](https://refractiveindex.info/)
23. M. Burgelman, P. Nollet, and S. Degrave, “Modelling polycrystalline semiconductor solar cells,”Thin Solid Films **361**, 527 (2000).
24. K. Decock, P. Zabierowski, and M. Burgelman, “Modeling metastabilities in chalcopyrite-based thin film solar cells,”
J. Appl. Phys.**111**(4), 043703 (2012).
25. M. Burgelman, K. Decock, S. Khelifi, *et al.*, “Advanced electrical simulation of thin film solar cells,”Thin Solid Films **535**, 296 (2013).
26. P. Tockhorn, J. Sutter, A. Cruz, *et al.*, “Nano-optical designs for high-efficiency monolithic perovskite–silicon tandem solar cells,”Nat. Nanotechnol.**17**(11), 1214 (2022).
27. A. Callies, M. Hanser, J. C. Goldschmidt, *et al.*, “Structuring of perovskite-silicon tandem solar cells for reduced reflectance and thermalization losses,”Opt. Express **31**(12), 19428 (2023).
28. C. Messmer, B. S. Goraya, S. Nold, *et al.*, “The race for the best silicon bottom cell: Efficiency and cost evaluation of perovskite–silicon tandem solar cells,”Prog. Photovolt. Res. Appl.**29**, 744 (2021).
29. M. De Bastiani, R. Jalmood, J. Liu, *et al.*, “Monolithic perovskite/silicon tandems with >28% efficiency: role of silicon-surface texture on perovskite properties,”Adv. Funct. Mater.**33**, 2205557 (2023).
