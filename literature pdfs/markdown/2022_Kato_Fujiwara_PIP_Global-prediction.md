Received: 2 December 2021 Revised: 29 March 2022 Accepted: 14 April 2022 DOI: 10.1002/pip.3569

<u>RESEARCH ARTICLE</u>

Global prediction of the energy yields for hybrid perovskite/Si tandem and Si heterojunction single solar modules

|1||2|1|
|---|---|---|---|
|1||1|3|
|1|1|||
|2 1|2|||

Yoshitsune Kato | Hirotaka Katayama | Tomoya Kobayashi |

Masayuki Kozawa | Yukinori Nishigaki | Tomonao Kobayashi | 1 4 Yosuke Kinden | Kohei Oiwake | Ryo Ishihara | Taisuke Matsui | 2 2 Youichirou Aya | Taiki Hashiguchi | Daiji Kanematsu | Akira Terakawa |

## Hiroyuki Fujiwara

1 Department of Electrical, Electronic and Computer Engineering, Gifu University, Gifu,Abstract Japan A strong expectation exists for a two-terminal hybrid perovskite/silicon tandem solar 2 Energy System Division, Panasonic Corporation, Kaizuka, Japan cell for generating substantially higher output power. Nevertheless, a high tandem 3 Department of Civil Engineering, Gifu cell efficiency under the standard condition does not guarantee high power genera- University, Gifu, Japan tion in outdoor environment due to the requirement of current matching in a tandem 4 Technology Innovation Division, Panasonic device. Here, we predict the global energy yields of hybrid perovskite/Si tandem and Corporation, Moriguchi, Japan Si heterojunction single modules by establishing a new rigorous self-consistent model Correspondence that performs full device simulations incorporating all fundamental time-varying Hiroyuki Fujiwara, Department of Electrical, Electronic and Computer Engineering, Gifu parameters affecting the module power output. In particular, the temperature depen- University, 1-1 Yanagido, Gifu 501-1193, dences of the optical and electrical characteristics are modeled explicitly and reliable Japan. Email: fujiwara@gifu-u.ac.jp model parameters are extracted from an industry-compatible Si heterojunction single cell (23.27% efficiency with a 120 μm wafer thickness), whereas ideal cell characteris- tics are assumed for a hybrid perovskite top cell. Our simulation approach is justified from the remarkable agreement with experimental results. We find that the tandem architecture improves a module energy yield in all places by a maximum of 1.6 times, compared with a state-of-the-art Si heterojunction single module. Importantly, the annual energy yields of the tandem and single modules scale linearly with annual sun irradiation, even with the requirement of the current matching in the case of the tandem device, and the ratio of the tandem and single energy yields is governed essentially by the module efficiency ratio obtained under standard conditions. We have further revealed the climate-dependent energy yield variation with a magnitude of ~5% based on Köppen-Geiger climate classification. Moreover, the optimization of the top-cell band gap based on real meteorological data shows that the optimum top-cell gap needs to be increased at a place with a lower solar irradiation.

KEYWORDS current matching, global energy yield prediction, perovskite/Si tandem cells and modules, real weather conditions, Si heterojunction solar cells and modules, temperature dependence

© 2022 John Wiley & Sons Ltd. wileyonlinelibrary.com/journal/pip Prog Photovolt Res Appl. 2022;30:1198–1218.

1099159x, 2022, 10, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.3569](https://onlinelibrary.wiley.com/doi/10.1002/pip.3569) by University Of Oxford, Wiley Online Library on [08/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License KATO ET AL.

## | INTRODUCTION

In realizing a clean energy world that does not rely on fossil fuels, the development of high-efficiency solar cell modules is vital. A key strategy for increasing solar cell efficiency to a value exceeding the Shockley-Queisser radiative limit (34%) is the adaptation of a tandem cell architecture. 1,2 In particular, Si-based single cell technologies enter a maturing stage and the cost effective approach for improving Si module efficiency becomes increasingly scarce. Thus, a tandem cell design, established based on current low-cost Si cells, is a quite attractive alternative for aiming a drastic increase of module output. 1–6 An emerging hybrid perovskite compound, 7–9 exhibiting strong light absorption 9,10 and quite long carrier lifetime, 11 is a strong candidate for a wide-gap top cell with a band gap of Eg~ 1.7 eV¹² in a double tandem structure formed with a Si bottom cell (Eg= 1.1 eV). Fortunately, monolithic two-terminal hybrid perovskite/Si tandem cells with high efficiencies have already been developed, 1,2,4–6,13–18 showing a remarkable 29.8% efficiency, 19 which is higher than a record efficiency of a Si single cell (η = 26.7%). 20 Nevertheless, in the case of two-terminal tandem cells, a high cell efficiency recorded under the standard test condition does not guarantee that actual energy yield of the solar module is satisfactory due to the requirement of current matching between the top and bottom cells. More specifi- cally, the incident sun spectrum and device operating temperature vary strongly in outdoor environment, changing the current matching condition and thus reducing short-circuit current density (Jsc). 21,22 Accordingly, the energy rating based on true meteorological data is critical in assessing the real potential of tandem modules. To reveal the outdoor performance of the tandem devices, the theoretical energy-yield calculations of the tandem cells and modules have been performed widely. 22–32 Such an approach is quite impor- tant as a state-of-the-art perovskite/Si tandem cell exhibits strong degradation in outdoor environment, 33 and the reliable energy-rating characterization is difficult at this stage. The important insight obtained in earlier tandem energy-yield studies is a significant spectral effect induced by the seasonal variation of incoming sun light; a bluer spectrum during summer (or a redder spectrum during winter) gener- ates a spectral mismatch, leading to a seasonal variation of tandem power generation. 22,23,28 Thus, in addition to a daily spectral variation caused by clouds, a spectral mismatch induced by the seasonal spec- tral change also generates the current mismatch in the tandem device, affecting the device efficiency notably. In many tandem energy-yield estimations, 24,26–28,30,32 however, the effect of device temperature is neglected completely. As con- firmed already, 9,21,34 the Egof hybrid perovskite top-cell materials shows an anomalous increase with temperature, while that of the Si bottom cell exhibits an opposite trend. 35,36 Accordingly, the device operating temperature unbalances the top- and bottom-cell currents significantly²¹ and the temperature effect needs to be accounted for explicitly. In some energy yield calculations, 23,25,29,31 the influence of the temperature has been approximated by response functions of diode parameters, while neglecting the spectral effect. In tandem

devices operating on current matching, the incorporation of the spec- tral response into the energy yield calculation is crucial and more com- plete approach is vital for obtaining accurate energy yield, allowing detailed discussions of tandem-device outdoor performance. Moreover, in earlier attempts, 23–30,32 the energy yields of only a few specific places have been evaluated. Although these studies confirmed a higher energy yield in a place with stronger sun irradiation, 23–27,29 overall trends and detailed climate effects remain ambiguous. On the other hand, Liu et al. have calculated the world energy yields for various types of tandem devices. 31 For this study, however, the energy yields have been calculated without implementing device optical calculation and the tandem perfor- mances have been estimated based on fixed external quantum efficiency (EQE) spectra obtained from experiments by neglecting the spectral variation due to temperature and incident angle changes. Thus, the results of such a simple approach further need to be justified. In this article, we have predicted the global energy yields of hybrid perovskite/Si tandem and Si single modules based on a rigor- ous self-consistent method that implements full EQE spectral calcula- tion by incorporating temperature and incident angle as variables. In the proposed method, all major device/module and meteorological factors have been considered precisely for exact textured structures established in experiments, in an attempt to establish the true poten- tial of the tandem module relative to a state-of-the-art Si hetero- junction module. To the best of our knowledge, no previous study has performed the energy yield calculations of tandem and single cells/modules over a wide area by performing full EQE calculation and the consequential device parameter modeling. In contrast to earlier theoretical efforts for perovskite/Si tandem cells, 23–25,27–32 we justify our energy yield calculations by excellent fitting to experimental data obtained in real cells formed with double-sided pyramid Si textures, while assuming ideal top-cell electrical characteristics. Our prediction model reveals that the energy yield of a hybrid perovskite tandem module scales linearly with annual total sun-light irradiation and a maximum 1.6 times increase in annual energy yield is possible in the tandem module, compared with a Si heterojunction module. The cal- culation of the energy yield ratio for the tandem and single modules further shows that the tandem architecture improves the energy yield uniformly by a factor determined essentially from the module effi- ciency ratio obtained under standard conditions, while slightly better tandem performance is observed in warmer regions. By applying real weather conditions, we further establish that the optimum top cell Eg varies with a sun-light irradiation condition.

## 2 | ENERGY YIELD CALCULATION

2.1 | Overview of the proposed method Figure explains the procedure of a self-consistent energy yield calculation proposed in this study. The exact calculation procedures are explained in details in Section 2.3. In the initial stage of this

FIGURE 1 Self-consistent model established for the prediction of the energy yields for Si single and perovskite/Si tandem modules in this

study. In this figure, the calculation procedure for the Si heterojunction device is schematically shown. The incident angle (θin) is calculated from the altitude (θa) and azimuth (ϕ) of the sun and the solar panel tilt angle (θpv), which further determine the photon-density sun spectrum [φsun(λ)] and sun irradiance to the panel (κsun). The module temperature (T) is deduced from κsun, wind speed and ambient temperature. For the optical response calculation of a double-sided pyramid-shaped Si texture, the double reflection model (DRM) 37 was employed. In the DRM, the optical response of the texture is calculated by employing flat optical models show by the dotted squares. The calculation procedures of EQE, Jsc, J₀, and V ocare described in Section 2.3. For J₀ of the Si cell, the radiative (J0,rad) and non-radiative (J0,nonrad) components are considered. The temperature dependences of the series resistance (Rs), shunt resistance (Rsh) and diode factor (n) are also considered in the Si energy yield calculation. The module power density (Pmod) is calculated from five T-dependent parameters of Jsc(T), Voc(T), Rs(T), Rsh(T), and n(T)

calculation (green squares in Figure 1), the input parameters are deter-light absorption in absorbers is represented by a few flat optical mined. Specifically, from the sun altitude (θa), sun azimuth (ϕ), and models with different incident angles. 37 For the EQE calculation of solar panel tilt angle (θpv), the module incident angle (θin) is calculated, the tandem module, the DRM requires only 1 s, which is far shorter which further determines the photon-density sun spectrum (φsun(λ)) than a ray-tracing method combined with wave optical calculation for the module plane. From φsun(λ), a wind speed (Swind), and an ambi-(~2 min in Schmager et al. 29 ). The very fast EQE calculation within ent temperature (Ta), the module temperature (T) is deduced assuming DRM is particularly important when implementing energy yield calcu- an open-rack configuration. The resulting three factors (i.e., θin, φsun(λ), lations in a vast scale. Moreover, the DRM is fully compatible with the and T) define input data in our energy yield calculation. θin-dependent EQE calculation. We obtained the EQE of a module In the second stage of the procedure (blue squares in Figure 1), structure assuming a standard configuration of glass/EVA (ethylene the various model calculations are performed. For the optical vinyl acetate)/cell/backsheet. The variation of the absorber Egwith response calculation of the Si pyramid texture, we adopted a low T is fully incorporated into the model calculation, leading to the EQE computational cost method, double reflection model (DRM), in which variation particularly in the long-λ region. By multiplying φsun(λ) with

the θin- and T-dependent module EQE spectrum (i.e., EQE (θin, T, λ)), perovskite top cell, while applying the experimentally verified parame- Jsc(T) is calculated. The reverse saturation current density J₀(T), con-ters for the Si bottom cell. In the tandem calculation, we obtain two sisting of radiative (J0,rad) and non-radiative (J0,nonrad) components, is J-V characteristics for the top and bottom cells, from which the

|sisting of radiative (J||) and non-radiative (J|) components, is||J-V characteristics|for the|top and bottom|cells, from|which the|
|---|---|---|---|---|---|---|---|---|---|
|further estimated from the EQE spectrum and an additional model|||||tandem P|is estimated. In Section 4.2, we further discuss the influ-||||
|established in this work, respectively. Based on J open circuit voltage V|(T) can directly be obtained.||(T) and J₀(T), the||ence of the top-cell non-ideal parameters on P To date, a variety of energy-yield calculation methods have been|||.||
|In the developed scheme, to perform the rigorous energy yield calculation for an industry-compatible Si heterojunction module, the|||||proposed. previous schemes are|The improvements|in|calculation|method over|
|explicit T-dependent shunt resistance R state-of-the-art Si cell (120 μm in thickness) with a certified efficiency of 23.27% (Figure S1). From five T-dependent active parameters of|diode (T), and diode factor n(T)) are extracted from a|parameters|(i.e., series resistance|R (T),|1. Exact T- and θ adopting the fast-speed calculation method of DRM, 2. Model calculations are made in a self-consistent manner by linking|-dependent EQE calculations have been made by||||
|J (T), V|(T), R (T), and n(T), we calculate the J-V characteristic||||EQE, J|, J₀, and V explicitly,||||
|of the Si single module, from which the module power density (P|||||3. T-dependent solar cell parameters (i.e., J|||(T) and V|(T)) are fully|
|is determined.|The above|procedure|is repeated|using different|modeled based on the T-induced EQE and J₀ variations caused by|||||
|hourly-based data of the year 2018 and the annual energy yield is estimated by simply integrating the hourly P|input data|obtained directly values.|from the|meteorological|absorber simple separate models are applied for J in earlier studies,|E changes,|while temperature|effect is (T) and J₀(T) calculations|neglected or|
|In the calculation of a perovskite/Si tandem module, to derive a|||||4. Reliable|T-dependent|model parameters|are extracted|for a Si|
|possible|tandem|energy|ideal diode|parameters|heterojunction|bottom|cell based|on the|experimental|
|(i.e., R (T) = 0,|R (T) = ∞,|and n(T) = 1)|are assumed|for the|T-dependent EQE and J-V characteristics,|||||

mod sc mod oc 23–32 our

s sh in

sc oc(T), Rs sh sc oc mod)sc oc

g sc 23–32 mod

maximum yield, s sh

FIGURE 2 Model structures of (A) a Si

heterojunction single solar cell and (B) a hybrid perovskite/Si tandem solar cell, which are considered in the module structures. The layer thicknesses adopted in the energy yield calculations are also indicated. The thicknesses of the Si single- cell constituent layers in (A) were determined from the EQE analyses described in Section 3.1. In (B), the thicknesses of the top cell were chosen based on 13,14,40 the design of experimental tandem cells, whereas for the Si bottom cell the same layer thicknesses as the Si single cell in (A) were adopted. For the perovskite absorber, Cs0.17FA0.83Pb(I, Br) is assumed with two layer thicknesses of 1 μm and 500 nm

5. Module energy yield, rather than a cell energy yield, is estimated by assuming the exact module structure, as considered also in

|by assuming|the exact module|structure,|as considered|also in|
|---|---|---|---|---|
|some studies.|||||

27–29

2.2 | Device structures and optical constants
2.2.1 | Cell structures
Figure 2A,B shows the structures of a Si heterojunction cell and a
 hybrid perovskite/Si heterojunction tandem cell, which are considered in the module structures. The Si cell has a standard structure with
38,39 hydrogenated amorphous silicon (a-Si:H) p-i and i-n layers, whereas In₂O₃:W (IWO) layers were employed as transparent conduc- tive oxide (TCO). The thicknesses of the Si single-cell constituent layers in Figure 2A were determined from the EQE analyses described in Section 3.1. The tandem structure shown in Figure 2B was constructed based 14 on an experimental perovskite/Si tandem cell reported earlier. For the perovskite absorber, a cesium-formamidinium lead iodide-bromide 9,12 alloy (i.e., Cs0.17FA0.83Pb(I, Br)3) is assumed, and as tunneling junction layers, nano-crystalline Si (nc-Si:H) layers are 14,40 incorporated. In the top cell, C₆₀ and sprio-OMeTAD are the electron and hole transport layers, respectively. The LiF acts as the passivation⁴¹ and shunt-blocking¹³ layer, whereas SnO₂ is a 13 protective layer for the sputtered TCO (InZnO: IZO) layer. The formation of similar perovskite top cell structures on fully textured Si bottom cells has already been demonstrated by a two-step process¹⁴ 18 or a co-evaporation process. For the tandem cell of Figure 2B, the proper layer thicknesses were chosen based on the design of experi- 13,14,40 mental tandem cells, whereas for the Si bottom cell the same layer thicknesses as the Si single cell in Figure 2A were adopted.

2.2.2 | Optical constants For the EQE calculations, the optical constants (refractive index n and extinction coefficient k) of all the constituent layers are necessary and we employed those extracted from experimental spectroscopic ellipsometry measurements. Specifically, we adopted the optical constants of a-Si:H,
42 Si, 42 Ag, 42 MgF₂, 42 IZO, 42 SnO₂, 42 C₆₀, 43 LiF, 42 Spiro-OMeTAD, 10 and nc-Si:H. 42 For IWO, the optical constants extracted from an IWO layer (Figure S2) were used. As the optical constants of the front glass and EVA, those reported in Fujiwara and Collins⁴² were adopted. In this study, to maximize the energy yield of the tandem module, the Egof the perovskite top cell has been optimized. To express the variation of the Cs0.17FA0.83Pb(I, Br)3optical constants with Eg(or Br content), we employed the optical function parameterized by the Tauc-Lorentz model. It has been demonstrated that the dielectric functions (or n and k spectra) of all hybrid perovskite materials can be expressed by combining the Tauc-Lorentz transition peaks 9,42 and, if all the energies of the Tauc-Lorentz transition peaks are increased,

FIGURE 3 Refractive index (n) and extinction coefficient (k)

spectra of Cs0.17FA0.83Pb(I, Br)3with three different Egvalues (1.60,

1.71, and 1.80 eV), together with the corresponding absorption coefficient (α) spectra. For this calculation, the Tauc-Lorentz model
9 parameters reported for Cs0.17FA0.83Pb(I0.7Br0.3)3with Eg= 1.71 eV were employed

the high-energy shift of a hybrid perovskite dielectric function with Br content can be expressed properly. 9

Figure 3 shows the (n, k) and absorption coefficient (α) spectra

of CsFAPb(I, Br)3alloys with different Eg(1.60, 1.71, and 1.80 eV). For this calculation, Tauc-Lorentz model parameters reported for Cs0.17FA0.83Pb(I0.7Br0.3)3with Eg= 1.71 eV were employed, whereas the Egof this alloy changes with the Br content x with Eg(x) = 1.54 + 0.57x eV. 9 It can be seen that the α spectrum slides toward higher energy with increasing Eg, as confirmed experimentally. 45

2.3 | Model calculations
2.3.1 | Input parameters From θaand ϕ of the sun, the sun position at a place is calculated. In our calculation, solar panels are oriented toward south in the northern hemisphere (i.e., ϕpv= 180 ) and north in the southern hemisphere (ϕpv= 0 ). Moreover, the panel tilt angle (θpv) is treated equivalent to the latitude of the calculated place. In this case, the incident angle of the sun light to the module (θin) is calculated by θ in¼ cos sin θacos θpvþ cos θasin θpvcos ϕ ϕ : ð1Þ
pv

FIGURE 4 Variation of the module operation temperature (T)

with wind speed (Swind) for different panel-plane integrated irradiance (κsun) when the ambient temperature is Ta= 300 K, calculated from the model of Equation (2) with a = 3.56 and b = 0.075 s/m

Once θinis determined, the module-plane sun irradiance spectrum (κsun(λ)) is calculated. From κsun(λ), a steady-state module operating temperature (T) is further estimated by a reported model⁴⁶:

T ¼ κsunexpðÞþ a bSwindTa, ð2Þ

where κsun, Swind, and Taare the panel-plane integrated irradiance with a unit of W/m², a wind speed with a unit of m/s and ambient temper- ature, respectively. The a and b in Equation (2) are conditional param- eters and, in an open-rack panel installation condition, a = 3.56 and b = 0.075 s/m can be employed. 46 In our simulation, the cell tempera- ture is assumed to be equal to the module temperature calculated by Equation (2). Figure 4 shows the variation of the module temperature T with Swindand κsunwhen Ta= 300 K. At a constant Swind, T increases with κsundue to the module heating caused by the sun irradiance. At 1-sun illumination (κsun= 1000 W/m²) with Swind= 0, T increases to 328 K (55 C), which is the same T range observed in the outdoor operation of a perovskite/Si tandem cell. 21

collection is assumed. For the optical response calculation of the Si bottom cell, the incoherent light absorption in a thick Si wafer is also taken into account. 47 The strong light scattering that occurs in the textured Si rear interface has also been considered in the DRM and the rear light scattering effect is modeled by incorporating two adjust- able parameters of a light-pass-length enhancement factor (s) and an optical confinement factor (f). 37 In this study, the DRM is further extended to include the optical calculation for θin>0. Specifically, the optical passes in the front-side Si pyramid texture are fully categorized and each optical response is expressed by combining a few flat optical models with different light incident angles (Figure S3). Moreover, the calculated results obtained for each optical pass are weighted according to the probabilities estimated directly from the geometrical consideration (Table S1). In the EQE calculation of the module structure (i.e., glass/EVA/ cell/Ag), the effects of (i) the glass front light reflection and (ii) the light absorption in an EVA coating (100 μm) are incorporated. For the front light reflection, only the first light reflection that occurs at the air/glass interface is considered and thus the weak influence of multiple light reflections within a thick glass substrate was neglected. 42 For the EVA light absorption, only the influence of one-optical pass length within the EVA layer is incorporated into the calculation to simplify the modeling. In the experimental Si cell shown in Figure 2A, the area ratio of the front metal grid electrode (i.e., S in Equation (3)) is 3.54%, whereas a reported shadow loss of 2.3% 14 was adopted for the perovskite/Si tandem simulation.

2.3.2 | Jsccalculation The Jsc(T) of the cells and modules is evaluated by a standard formula:
J scðÞ¼ T ðÞ 1 S e EQEðÞ θin, T, λ φsunðÞ λ dλ ð3Þ ð

where S, e, EQE (θin, T, λ), and φsun(λ) indicate the shadow loss of the cell, electron charge, θin-and T-dependent EQE spectrum, and photon-density spectrum obtained from the sun irradiance spectrum (i.e., φsun(λ) = κsun(λ)λ/(hc)), respectively. The EQE spectra of textured Si single and perovskite/Si tandem modules were obtained from the absorptance spectra calculated using the DRM and thus 100% carrier

2.3.3 | J₀ and Voccalculations In general, J₀ of solar cells can be expressed as the sum of two contributions induced by J0,radand J0,nonradcomponents⁹:
J₀ðÞ¼ T J0,radðÞþ T J0,nonradðÞ T : ð4Þ

The J0,radcan be estimated from the EQE spectrum 48,49 and, from the blackbody radiation, J0,radis calculated as

J 0,radðÞ¼ T ðÞ 1 S e EQE o ðÞ T, λ φ ðÞ T, λ dλ, ð5Þ ð 0 BB

where EQE₀o ðÞ T, λ represents the T-dependent EQE spectrum obtained assuming θin= 0. 49 The φBB(T, λ) shows the photon density spectrum for the blackbody radiation at T, expressed by the following equation⁹:

≥ ~1 <u>2πc hc</u> φ BBðÞ¼ T, λ exp : ð6Þ λ λkBT

In this study, to express the J0,nonrad(T) of the Si heterojunction solar cell, we have established a new exponential model described by

~ <u>B</u> Radiation Database (NSRDB) developed by NREL for the year 2018. J 0,nonradðÞ¼ T eA exp, ð7Þ k T B This database summarizes κsun(λ) under clear-sky or cloudy-sky conditions, calculated by applying the Fast All-sky Radiation Model for Solar applications with Narrowband Irradiances on Tilted surfaces where A and B are adjustable parameters. On the other hand, 52,53 (FARMS-NIT). J In our simulation, 8760 spectra are employed for 0,nonrad(T) of the perovskite cell is assumed to be zero to derive a theoretical maximum efficiency. the prediction of an annual energy yield of one place and such a From Jsc(T) and J₀(T) obtained from Equations (3) and (4), Vocis calculation is repeated for a total of 762 places in America. obtained by a general formula assuming an ideal diode factor of n = 1:

≥ <u>k</u> <u>T JscðÞ T</u> <u>B</u> VocðÞ¼ T ln þ 1 ð8Þ e J₀ðÞ T

2.3.4 | Pmodand energy yield calculations The J(T)-V(T) characteristics of the modules are calculated by a well- known formula⁵⁰:
~ <u>eV T</u> ½ <u>ðÞ JT ðÞR ðÞsT</u> JT ðÞ¼ J₀ðÞ T exp 1 nT ðÞkBT ð9Þ <u>VT ðÞR ðÞsT JT ðÞ</u> J scðÞþ T, R shðÞ T

where J₀(T) is defined from Jsc(T), Voc(T), and n(T)as

, ≥ <u>eVocðÞ T</u> J₀ðÞ T ¼ JscðÞ T exp 1 : ð10Þ nT ðÞkBT

As a result, the J-V curve is calculated from five independent parameters of Jsc(T), Voc(T), Rs(T), Rsh(T), and n(T). Note that J₀(T) defined by Equations (4) and (8) in Section 2.3.3 is different from J₀(T) that appears in Equations (9) and (10) since n(T) = 1 is assumed for Equations (4) and (8). To calibrate J₀(T) for n(T) > 1, the form of Equation (10) has been adopted. In the case of the tandem module, the J-V curve is estimated as

VJ ðÞ¼VtopðÞþ J VbottomðÞ J, ð11Þ

where Vtop(J) and Vbottom(J) are the inverse functions of Jtop(V) and J bottom(V) calculated for the top and bottom cells using Equation (9). In the estimation of V(J) using Equation (11), the current matching condition is also considered. From the calculated J-V characteristic, the maximum power density of the module structure (Pmax,mod) is obtained. To estimate the realistic power generation in the modules, we assume the effective cell coverage area of 94% (i.e., A = 0.94) on the module surface. Consequently, the module power density (Pmod) is calculated as P mod= APmax,mod(i.e., Pmod= 0.94 JscVocFF [fill factor]). The annual energy yields of the tandem and single modules are calculated by integrating Pmodat points in North and South America based on hourly irradiance spectra (i.e., κsun(λ)) and meteorological data (Swindand Ta), obtained from the National Solar

2.3.5 | Modeling of diffused sun light The contribution of incident sun light can be separated into two factors of direct and diffused light components. In our method, how- ever, the effect of the θinvariation in the diffused light is neglected and all the incoming light is assumed to have a single θinvalue deter- mined by the direct component, in an attempt to reduce the compu- tational cost. While the same assumption was made in some tandem energy-yield calculations,
23,25,31 many studies have taken the effect of the diffused sun component into account. 24,26–30,32 Unfortunately, detailed meteorological data that include the direct and diffused sun spectra are not currently available widely and, in many previous studies, 24,27–30 these spectral contributions were obtained based on model calculations. Nevertheless, such a sun-spectral calculation generates extra complications and increases the computational cost significantly. In our case, the total computational time for the energy yield calculation at 762 points is roughly 1 month for each module structure and the incorporation of the weather spectrum calculation and the following diffused-light effect calculation increases the computational time notably. In this study, therefore, the simplified calculation is adopted, but we have justified our energy-yield calcula- tions by comparing the results obtained with and without considering diffused sun-light components for selected weather conditions (Section 4.2). For the calculation of Jscincorporating both direct and diffused sun-light contributions, we use the general expression of

J scðÞ T ¼ Jsc,dirðÞ T þ Jsc,diffðÞ T : ð12Þ

Here, Jsc,dirand Jsc,diffshow the Jsccomponents generated by direct and diffused sun spectra:

J sc,dirðÞ¼ T ðÞ 1 S e EQEðÞ θin, T, λ φ ðÞ θin, λ dλ, ð13Þ ð dir

"# X N J sc,diffðÞ T ¼ ðÞ 1 S e P θjEQE θj, T, λ φdiffðÞ λ dλ, ð14Þ ðj¼1

where φdirand φdiffindicate the photon-density spectra for direct and diffused sun lights. Moreover, P (θj) in Equation (14) represents the isotropic (Lambertian) probability function considered for the diffused component²⁹: <u>π</u> P θj¼ sin 2θj, ð15Þ 2N

where θjis defined by θj= [π/(2 N)]j and N denotes the total number of division in the diffused component calculation. In our case, N = 90 (i.e., 1 resolution) was adopted. Equation (14) can be derived by considering a semi-spherical integration for isotropic diffused compo- P nents and P (θj) = 1.

## 3 | RESULTS

3.1 | Modeling of the Si heterojunction cell
Figure 5A shows the J(T)-V(T) characteristics of the Si cell. The open
 circles indicate the measured values, whereas the solid lines represent the results of the fitting analyses using Equation (9), from which the five device parameters of Jsc(T), Voc(T), Rs(T), Rsh(T), and n(T) are extracted. The precise Jsc(T) modeling has further been implemented according to the T-dependent EQE spectra shown in Figure 5B. The open circles show the experimental EQE(T) with θin= 0, whereas the solid lines represent the DRM simulation results. For T = 25 C, the corresponding reflectance (R) spectrum is also shown. In the
FIGURE 5 Temperature variations
 of (A) J-V, (B) EQE, (C) J₀, and (D) Rs, Rsh, and n characteristics of a Si heterojunction solar cell with a certified efficiency of 23.27%. The open circles show the experimentally derived data, whereas solid lines indicate the fitted results calculated from Equation (9) (A), the DRM simulation (B), Equation (7) (C), and linear models (D). In (B), the open squares show the experimental 1 R data (25 C), and the corresponding simulation result is also shown. In (C), the contributions of J0,radand J0,nonrad are shown. Note that J₀ ~ J0,nonrad. In (D), the linear coefficients are given for each Rs, Rsh, and n
calculations, to describe the EQE(T) accurately, we adapt a Eglinear variation model, in which Egof a Si crystal varies with Eg(T) = 4.6 10 4 (T 300 K) + 1.1134 eV. In this modeling, the optical function of the reported Si spectrum⁴² is shifted horizontally in the energy direction according to the established Eg(T). Our simulations reproduce the measured EQE(T) and R(T) almost perfectly when two arbitrary model parameters of DRM are adjusted to s = 4.03 and f = 1.34. It should be noted that this 23.27% cell is formed using a small pyramid texture of ~5 μm and this state-of-the-art Si cell can be modeled perfectly within DRM. In the DRM simulation, however, the front a-Si:H layer thickness (4.4 nm in Figure 5B) is slightly under- estimated, compared with the experimental thickness. As indicated in Equation (8), Voc(T) is calculated from Jsc(T) and J₀(T). The Jsc(T) can simply be calculated from the EQE simulation of

Figure 5B, while the J₀(T) calculation of Si solar cells is not straightfor-

ward; namely, indirect Si cells exhibit strong nonradiative Auger recombination 54,55 (i.e., J0,nonrad), in addition to the radiative recombi- nation (J0,rad). Figure 5C shows the J₀(T) modeling result based on Equations (4)–(7). The open circles show J₀(T) estimated directly from the experimental data of Voc(T) and Jsc(T) by applying Equation (8)

of high-efficiency Si heterojunction cells shows a small Rscontribution 56 of ~0.002 Ω. Thus, zero Rsin Figure 5D should be interpreted as a nominal value obtained as a consequence of our parameterization scheme under the assumption of the single diode model.

Figure 6 summarizes the variations of Voc, Jsc, FF, and maximum

power density (Pmax) of the Si cell with T. The open circles show the experimental results for the 23.27% cell, whereas the solid lines repre- sent the data obtained from our model calculation. In this particular simulation, instead of the module structure of Figure 1, the cell struc- ture of Figure 2A was considered and thus Pmax≠ Pmod. As confirmed from Figure 6, the experimental Pmaxcan be reproduced quite accu- rately from our model with an error less than 0.3%.

assuming n = 1, whereas the black and red lines indicate the calcula- tion results of J0,radand J0,nonradobtained from Equations (5) and (7), respectively. In Si cells, J0,nonrad(T) is far larger than J0,rad(T) due to the strong effect of Auger recombination and thus J₀(T) ~ J0,nonrad(T). If we set A = 3.839 10 29 s 1 cm 2 and B = 2.063 10 19 J in the exponential model, the experimental J₀ variation can be expressed almost perfectly. Accordingly, by using the established model, Voc(T) can be calculated from Jsc(T) and J₀(T) = J0,nonrad(T).

Figure 5D shows Rs(T), Rsh(T), and n(T) extracted from the J-V

analyses of Figure 5A. We find that Rs, Rsh, and n show clear depen- dence on T and all these values decrease linearly with increasing T up to ~310 K. The linear coefficients for each Rs, Rshand n are indicated in Figure 5D. The Rsreduction with increasing T can be interpreted by the enhanced conductivity in the a-Si:H i layers, 56 while the physics of the Rshand n reductions is more difficult to interpret. In Figure 5D, although Rsbecomes zero at T > 309 K, the detailed characterization

3.2 | Characteristics of the ideal perovskite/Si device
3.2.1 | Optimization of the perovskite top cell The module efficiency of the ideal perovskite/Si device was derived by optimizing the Egof CsFAPb(I, Br)3under our standard calculation condition (SCC) of T = 300 K and 1 sun illumination (100 mW/cm², AM1.5G). To justify our calculation procedure, we first fit the experi- mental EQE of a reported perovskite/Si tandem device¹⁴ shown in
Figure 2B using the DRM method. Figure 7A shows the experimental
 EQE and 1 R spectra (open symbols) and the corresponding calcula- tion results (solid lines). In this EQE analysis, the optical constants of the CsFAPb(I, Br)3top cell were varied as modeled in Figure 3, so that the calculated spectrum provides a best matching to the experimental spectra. If we assume that the top cell absorber Eg(Eg,top) is 1.61 eV (Br ~ 12 at.%), the experimental data are reproduced almost perfectly using the DRM method. From the calculated EQE spectra, the J-V curves for the top and bottom cells can be calculated separately using Equation (9), from which the J-V curve of the whole tandem device can further be derived based on Equation (11). For the direct-transition perovskite, the contribution of Auger recombination can be neglected. However, J 0,nonradof hybrid perovskite cells still shows a finite value controlled primarily by the interface recombination.
57,58 For the perovskite top cell, however, we adopted ideal parameters of J0,nonrad= 0, Rs= 0, R sh= ∞, and n = 1 to estimate the maximum possible module power density, while adopting the realistic Si bottom-cell parameters indicated in Figure 5.

Figure 7B shows the Pmodcalculated for the tandem module

structure as a function of Eg,top. The results obtained for different top absorber thicknesses (i.e., dpero= 500 nm or 1 μm) are also shown. The optimum Eg,topincreases from 1.643 eV to 1.697 eV with increas- ing dperofrom 500 nm to 1 μm. The corresponding top-cell and bottom-cell EQE spectra obtained with dpero= 500 nm and 1 μm are shown in Figure 7C. The optical loss analysis result for d = 1 μmis pero also shown in Figure S4. In Figure 7C, it can be seen that dperoaffects only the intermediate λ region (λ = 500–800 nm) and the sufficient top-cell light absorption in a thicker top cell shifts the Eg,toptoward

FIGURE 6 Variation of Voc, Jsc, FF, and maximum power density

(Pmax) of the Si heterojunction cell with T. The open circles show the experimental results for the 23.27% cell, whereas the solid lines represent the data obtained from the model calculation. In this particular simulation, the cell structure of Figure 2A was considered (i.e., Pmax≠ Pmod)

FIGURE 7 Simulation results

obtained for a fully textured tandem structure of CsFAPb(I, Br)3/Si shown in

Figure 2B. (A) Experimental and

simulated EQE spectra of the tandem cell. The open circles and squares show the experimental EQE and reflectance (1 R) spectra, 14 where the solid lines indicate the simulation results obtained assuming Eg,top= 1.61 eV. (B) Variation of module power density (Pmod) with a top-cell band gap (Eg,top) for top-cell absorber thicknesses of 500 nm and 1 μm. The closed circles show the maximum Pmod. (C) Module EQE spectra calculated for the optimized Eg,top values of 1.643 eV (dpero= 500 nm) and 1.697 eV (dpero= 1 μm).

(D) Variations of the tandem module parameters with Eg,topwhen d pero= 1 μm. The closed circles show the optimum condition of E g,top= 1.697 eV with P mod= 31.84 mW/cm²
shown in Figure 2A,B. The Pmaxand Pmodvalues in Table 1, obtained for the cell and module structures, respectively, also correspond to their efficiencies. The Pmodis smaller than the Pmaxby ~10% partly due to the Jscreduction caused by the module structure (i.e., glass light reflection and light absorption in EVA). The Jscof the tandem device is approximately half of that of the single device but the Voc increases significantly in the tandem device, with a top-cell Vocand a bottom cell Vocof 1.405 and 0.721 V in the module, respectively. The FF of the tandem device is also notably higher, compared with the sin- gle device. We mention that a very high FF of 86% has experimentally been obtained in a CH₃NH₃PbI₃ perovskite single cell. 60 The variations of the tandem module parameters with Eg,top (dpero= 1 μm) are also summarized in Figure 7D. These results show the important fact that the maximum Pmodis obtained in the current mismatching condition indicated by closed circles; in Figure 7D, the J scshows the highest value at Eg,top= 1.676 eV, which is slightly lower than the Pmod-optimized Eg,topof 1.697 eV. In other words, in this tandem module, Jscis limited by the top cell; specifically, the top-cell Jsc(17.97 mA/cm²) is smaller than the bottom-cell Jsc (19.11 mA/cm²). Importantly, FF shows the lowest value at the current matching condition particularly due to the effect of non-ideal factors considered for the Si bottom cell (i.e., finite values of Rs, Rsh and n) and a relatively low Rsh(~0.9 kΩcm²) of the bottom cell is problematic. In contrast, ideal diode parameters are assumed in the top cell and FF increases with Eg,topas the influence of the non-ideal Si bottom cell is suppressed in the synthesized tandem J-V character- istic limited by a top-cell Jsc(see Section 4.1 for more detail). Accord- ingly, the Eg,topthat provides the best Pmodis determined by the balance between Jscand FF and the optimum Eg,topis quite sensitive to the assumed diode parameters. In earlier studies of the tandem

TABLE 1 Characteristics of the Si single and hybrid perovskite/Si

tandem solar cells and modules calculated from the established model under SCC of T = 300 K

Single Tandem

Parameters Cell Module Cell Module P max, Pmod(mW/cm ) 2

23.06 20.81 35.84 31.84
J sc(mA/cm ) 2

38.51 37.06 19.02 17.97
V oc(V) 0.740 0.739 2.129 2.126 FF 0.810 0.809 0.885 0.887

Note: For the efficiency calculation of the cells, the structures shown in

Figure 2A,B are assumed. In the calculation of the modules, the structure

of glass/EVA/cell/metal is considered. The module power density (Pmod)is calculated as Pmod= 0.94 JscVocFF, where 0.94 shows a cell occupancy area in the modules.

shorter λ. It should, however, be emphasized that the optimum Eg,top varies strongly with other factors including Si wafer thickness 9,59 and light absorption in EVA and TCO. In recent perovskite/Si tandem studies, 14,15,17,21 the Si wafer with a thickness of ~260 μm has been applied. However, this wafer thickness is far thicker than that of com- mercialized cells (~120 μm). When the Si wafer is thin, the weaker light absorption in the bottom cell pushes the Eg,toptoward higher energy. 9,59 In contrast, when the light absorption in the EVA and TCO front layers is considered, the weaker short-λ EQE response lowers the Eg,topas the current matching is established in lower Jscin this case. In this study, we have assumed Eg,top= 1.697 eV with d pero= 1 μm as optimum parameters. Table 1 summarizes the calcu- lated cell and module performances of the single and tandem devices

devices, higher FF values in the current mismatch condition have also 24 been confirmed experimentally⁶¹ and theoretically.

3.2.2 | Modeling of T-dependent tandem characteristics We have further established the T-dependent Pmodcalculation for the tandem module. As mentioned above,
9,21,34 hybrid perovskite com- pounds exhibit a unique increase in Egwith T and we have modeled the Eg,top(T) of CsFAPb(I, Br)3as Eg,top(T) = 3.950 10 4 (T 300 K) + 1.697 eV by adopting the T-dependent Egcoefficient of FAPbI₃₆₂ and an optimum top-cell Egat 300 K (i.e., Eg,top- = 1.697 eV as determined in Figure 7B). Figure 8A shows the Eg(T) modeling results for CsFAPb(I, Br)3and Si absorbers. The Egshift of Si was obtained from the EQE analyses shown in Figure 5B. It can be seen that the Egof the perovskite shifts in an opposite direction, if compared with Si.

Figure 8B shows the EQE spectra of the top and bottom cells in

the module, calculated for different T under the optimized condition. When T increases, the longer-λ response in the top cell decreases due to the Eg,topwidening, while the EQE response of the Si cell increases in both short- and long-λ regions because of the enhanced light trans- mission in the top cell and the Egreduction of Si, respectively, as con- firmed experimentally. 21 Accordingly, establishing current matching becomes increasingly difficult when T varies.

Figure 9 shows the calculated performance of the perovskite/Si

module as a function of T. The Vocdecreases linearly with T (dVoc/ dT = 2.47 mV/K), primarily due to the increase of J₀ with T. In the Si single module, the coefficient of dVoc/dT becomes slightly smaller ( 1.82 mV/K) as the absolute Vocis smaller. In Figure 9, Jscshows the maximum at the current matching condition (T = 268 K), and FF shows the lowest value at this condition, as discussed in Figure 7D. Consequently, Pmodexhibits a unique non-linear variation with T.

FIGURE 8 (A) Variations of band gap with T assumed for the

perovskite and Si absorbers. The Si result was obtained from the EQE analyses of Figure 5B assuming the linear model, whereas the perovskite Egwas also obtained from the linear model. (B) Variation of top- and bottom-cell EQE spectra with T, obtained assuming the Eg variations of (A)

3.3 | T and θindependent module characteristics
Figure 10A compares Pmodcalculated for the perovskite/Si tandem
 and Si single devices. At SCC of T = 300 K, Pmodof the ideal tandem module is 1.5 times higher than that of the single module (see also
Table 1). In the Si module, the variation of Pmodwith T is almost linear
 with a temperature coefficient (TC) of 0.269 %/K, whereas the tandem module shows a nonlinear behavior at low temperatures due to the current mismatching but indicates an even better TC of 0.174 %/K. A similar TC of 0.197 %/K has also been reported for a
FIGURE 9 Calculated performance of the perovskite/Si module
 as a function of T. This module is under the current mismatch condition at T = 300 K, and the current matching condition is established at T = 268 K

interfaces. It should be emphasized that, in the case of Si simulated flat tandem structure. The estimated TC is consistent with heterojunction solar cells, the TC improves in a cell with a higher Voc an experimental TC reported for a single-junction perovskite cell 63 64 ( 0.17 %/K). For an experimental perovskite/Si cell, however, a due to the suppression of interface defects. 21 higher TC of 0.26 %/K has been reported. This experimental tan-

Figure 10B compares the θin-dependences of Pmod. The variations

dem cell shows a large Vocreduction with T (dVoc/dT = 3.66 mV/K), of Pmodfor the tandem and single modules are essentially similar. The compared with the theoretical value of 2.47 mV/K in Figure 9, changes of the tandem and single EQE spectra with θinare summa- which likely originates from the T-enhanced carrier recombination at rized in Figure S5. For the Si module, we have further calculated the angular response function, defined by RA(θin)=Jsc(θin)/(Jsc,0cosθin), where Jsc,0indicates Jscobtained at θin= 0 and cosθinrepresents 65 the projected area component. In Figure 10C, RAof the Si module calculated from the analysis of Figure 10B is compared with that of an 65 experimental large-area Si module. The result of Figure 10C confirms that the Jscangular response calculated from the DRM approach is consistent with the experimental result.

FIGURE 10 Variations of module power density (Pmod) with

module temperature (T) and incident angle (θin). (A) Changes of Pmod with T for the CsFAPb(I, Br)3/Si tandem and Si single modules. The temperature coefficient (TC) of each module is also indicated. The TC of the tandem module was calculated in a range of 300–350 K.

(B) Changes of Pmodwith θinfor the CsFAPb(I, Br) /Si tandem and Si3 single modules. (C) Angular response (RA) versus θinfor Si single modules. The open circles show the reported RAmeasured from an experimental large-area Si module,
65 where the solid line indicates the simulated values

3.4 | Energy yields of perovskite/Si and Si modules
Figure 11 shows the calculated annual energy yields of the (A) Si
 single and (B) perovskite/Si tandem modules and (C) ratio of the tan- dem and single module energy yields (Ry= Ytandem/Ysingle) in North and South America. Surprisingly, the energy yield maps obtained for the Si and perovskite/Si modules are quite similar, although the abso- lute energy yield is substantially higher in the tandem module. In other words, the tandem architecture uniformly increases the actual energy yield, independent of detailed weather conditions, even though the current matching needs to be satisfied in the tandem module. Indeed, Ryshown in Figure 11C, calculated from the results of
Figure 11A,B, is rather homogeneous. Note that, in Figure 11C, Ry
 obtained directly from SCC module efficiencies shown in Table 1 (Ry= 31.84%/20.81% = 1.53) is indicated by white and the areas with Ry> 1.53 and Ry< 1.53 are shown by red and blue, respectively. It can be seen that many regions show Ry~ 1.53 and, therefore, Ryis governed essentially by the SCC module efficiencies; however, Ry becomes higher than 1.53 near the equator with a maximum Ryof 1.6, while Rydecreases, compared with the SCC ratio, in northern region.
FIGURE 11 Predicted energy yields of the Si single and CsFAPb(I, Br)

energy yield (Ytandem), defined by Ry= Ytandem/Ysingle. Ry SCC module efficiencies in Table 1 (i.e., Ry R y< 1.53, respectively

/Si tandem modules for the year 2018. (A) Annual energy yield of the single) to the tandem

y> 1.53 and

Si single module. (B) Annual energy yield of the hybrid perovskite/Si tandem module. (C) Ratio of the single energy yield (Y = 1.53, indicated by white, defines the energy yield ratio calculated directly from the = 31.84%/20.81% = 1.53), whereas red and blue regions depict the areas with R

FIGURE 12 (A) Variation of the

annual energy yield with the annual total irradiation for the perovskite/Si tandem and Si single modules,

(B) change of Ryfor the annual total irradiation, (C) box plots for the energy yield of the Si single module,
(D) box plots for the energy yield of the perovskite/Si tandem module, and
(E) box plots for Ryin north and South America, categorized by Köppen- Geiger climate classification (A: tropical, B: dry, C: temperate, D: continental, E: polar). The inset of
(A) shows the actual classification map of America, which is indicated by the same colors of A–E. The dotted line in (E) indicates the SCC-module- efficiency ratio of Ry= 1.53
Figure 12A summarizes the annual energy yield of the tandem

and single modules as a function of the annual total sun irradiation, categorized by Köppen-Geiger climate classification (A: tropical, B: dry, C: temperate, D: continental, E: polar), for the selected 762 places in North and South America. The inset shows the actual climate classi- fication map of America. The Köppen-Geiger climate classification has been adopted to interpret the performance of Si 66,67 and perovskite/ Si³¹ devices. The striking results of Figure 12A are that (i) the energy yields of both single and tandem modules are predominantly governed by the total irradiation and (ii) the tandem module guarantees substan- tial increase in the energy yield by ~50% for all the climates and places. However, there is in fact a weak climate effect and, in

Figure 12B, we show the Ryvalues obtained for the 762 points as a

function of total irradiation. In Figure 12C–E, the box plots for the annual energy yield in the Si and perovskite/Si modules and Ry, summarized for different climates, are shown. The dotted line in

Figure 12E indicates the SCC-module-efficiency ratio of Ry= 1.53,

confirming that Ryimproves slightly in the tropical (A), dry (B), and temperate (C) areas, compared with the SCC ratio. Interestingly, Ryof the tropical region (A) is slightly higher than the dry (B) and temperate (C) areas, which can be explained by the fact that the TC of the tandem module is better than that of the single module (see Figure 10A) and higher temperatures in the tropical region reduce the single-cell efficiency more severely, compared with the tandem-cell efficiency. In contrast, the lower Ryobserved for the low temperature regions (i.e., continental [D] and polar [E] areas) can be interpreted by a relative power loss in the tandem module, compared with the single module.

In an earlier study, 31 the performance ratio of the tandem module has been reported to increase in cold regions (i.e., D and E areas), while that decreases in the tropical region (A). This result simply reflects the temperature effect, which increases the Pmodat lower T. The result of Figure 12E further shows that, if the ratio of Ryis considered, the relative performance of the tandem module improves in the opposite trend; that is, Rybecomes better in the warmer regions of A–C. We find that the energy yield of the single and tandem modules can be approximated by a quite simple linear function, given by

Y¼CA EItotal, ð16Þ

where CA-Eand Itotalare the climate-classified yield coefficient and annual total irradiation, respectively. Actual C values obtained from the analyses of the single module (Figure S6) and tandem module (Figure S7) are summarized in Table 2. The CAllin the table indicates a linear coefficient obtained using all the data and this corresponds to an effective efficiency under outdoor environment (CAll= 29.99% for the tandem module and 19.45% for the single module). These effec- tive efficiencies are only slightly smaller than the corresponding Pmod values listed in Table 1, confirming quite high outdoor performances of these modules. The result of Table 2 further shows that the influ- ence of the climate classification on the energy yield is ~5%. Our results indicate clearly that if the climate effect (i.e., CA-E) and Itotalof a calculating point are known, the annual energy yield can be calculated from the simple linear relation of Equation (16). From this simple method, we have predicted the global energy yields of the single and tandem modules (Figure 13A,B) and the global Ry(Figure 13C) based

|KATO|.|||
|---|---|---|---|
|TABLE 2 perovskite/Si tandem modules|Climate-classified yield coefficients of the Si single and|||
|Coefficient||Single|Tandem|
|C||0.1907|0.2979|
|C||0.1956|0.3030|
|C||0.1944|0.3007|
|C||0.2002|0.3004|
|C||0.1987|0.2921|
|C the symbol of Köppen-Geiger climate classification (A: tropical, B: dry, C: temperate, D: continental, E: polar), whereas C coefficient obtained using all the data.||0.1945|0.2999|

Note: The coefficient is defined by Equation (16). The subscript of C shows

ET AL

A B C D E All

Allindicates a linear

on the reported Itotalfor the year 2018 (Figure S8) and Köppen-Geiger climate classification map (Figure S9). It can be confirmed that the results of Figure 13A,B reproduce the results obtained from the detailed calculations of Figure 11A,B. In a previous study that calcu- lated the world tandem energy yield from a simple method using 31 experimental EQE spectra, a trend similar to Figure 13 has been reported. This is based on the simple fact that the tandem energy yield is primarily governed by the annual irradiation. In the Rymap of

Figure 13C, the value was governed by the fixed CA-Ecoefficients of

Table 2 and, therefore, the Rydistribution essentially reflects the

climate classification.

3.5 | Optimization of the top-cell Eg The results described above are obtained assuming Eg,top= 1.697 eV, which is derived based on our SCC of T = 300 K and dpero= 1 μm.
22,24 However, as pointed out previously, the optimum cell design, including top cell absorber Egand thickness, changes depending on the external irradiation and weather conditions. Thus, by applying the meteorological data of 2018, we have further performed a systematic investigation of the optimum Eg,topfor different climate regions with the variation of sun irradiation. Figure 14A shows the variation of the tandem-module energy yield with Eg,top. In particular, these calcula- tions have been performed for five representative places in America, with different total irradiations obtained for each climate classifica-

FIGURE 13 Global energy yields of (A) the Si single module and

tion. The closed squares and circles indicate the optimum Eg,top (B) the perovskite/Si tandem module and (C) global energy yield ratio obtained for dpero= 500 nm and 1 μm, respectively. Interestingly, the of Ry, predicted by a linear model of Equation (16) using the climate- optimum Eg,topshifts toward higher energy with decreasing sun irradi-classified yield coefficients of Table 2 and reported annual irradiance of the year 2018 ation. This trend can be confirmed more clearly in Figure 14B, which summarizes the irradiation-dependent optimum Eg,topcalculated for several different places for each climate classification. The dotted lines indicate the positions of the Eg,topoptimized under SCC. When that the average T during the module operation decreases notably the meteorological data are applied, Eg,topincreases substantially at a from 315 to 270 K as the total irradiation decreases from 2000 to low sun irradiation, with a weak effect of the climate classification. 500 kWh/m² (Figure 14C). Note that a low T reduces the Eg,top This can be interpreted by (i) the blue-rich sun spectrum of cloudy and (Figure 8A). Under the blue-rich and low T conditions, therefore, a rainy weathers, compared with the AM1.5G spectrum, and (ii) the wider top cell is required to enhance the bottom-cell current. It low T in low sun irradiation areas. Specifically, our calculation shows should, however, be emphasized that the tandem-module energy yield

|changes rather weakly with E|||(Figure 14A) and a lower E||than|
|---|---|---|---|---|---|
|the optimum can still be employed for the module production to avoid||||||
|the light-induced degradation observed in wide-gap hybrid perovskite||||||
|alloys|with high|Br contents.|Although|the photo-stable||
|perovskite top cells with E||~ 1.68 eV have been reported,|||it is|
|generally|difficult|to electronically|optimize|perovskites|at E|
|approaching wide-gap perovskites are not necessary for many regions, particularly when d perovskites. Moreover, to lower optimum E bifacial tandem architecture can further be adopted.|or exceeding = 500 nm, thus relaxing the requirement of wider E|1.7 eV.|Our result|indicates down to 1.6 eV, a|that the|

g,top g,top

69,70

g,top 15,71

g 6,9

pero g,top g,top 30,32,72

## 4 | DISCUSSION

4.1 | Tandem device efficiency In this study, the global energy yield was derived by assuming an ideal perovskite top cell (i.e., J0,nonrad= 0, Rs= 0, Rsh= ∞, n = 1). How- ever, non-ideality of the top cell reduces the module efficiency and the resulting energy yield. Here, we quantitatively discuss the influ- ence of the top cell non-ideality factors on the module efficiency. In particular, to express the effect of J0,nonradin the top cell, we define the quantum yield described as a J₀ component ratio:
J 0,rad Q₀ ¼ : ð17Þ J 0,radþ J0,nonrad

Thus,

<u>1 Q₀</u> J 0,nonrad¼ J0,rad: ð18Þ Q₀

When Q₀ « 1 (i.e., J0,nonrad» J0,rad), Equation (18) reduces to J₀ = J0,rad/Q, as proposed previously. 73 Unfortunately, the direct observation of Q₀ is difficult, but the quantum yield evaluated from photoluminescence (QPL) or electroluminescence (QEL) can be adopted as the Q₀ value.

Figure 15 shows the variations of the tandem module

FIGURE 14 Optimization of the top-cell band gap (Eg,top) based efficiency with (A) n, (B) Rs, (C) Rsh, and (D) Q₀ of the perovskite top

on actual weather data. (A) Variation of the energy yield with Eg,topcell at the standard testing condition of T = 25 C. In the obtained for five different places with various total irradiation and calculation of Figure 15, the optimized tandem structure in Figure 7D climate classification (A–E). The results obtained for a top-cell (i.e., Eg,top= 1.697 eV and dpero= 1 μm) was adopted and the effects absorber thickness of 1 μm are indicated by solid lines, whereas those of the top-cell n, Rsand Rshwere determined by applying Equation (9). obtained for a thickness of 500 nm are shown by dotted lines.

(B) Optimum Eg,topderived from several different places for each
In the case of Figure 15D, J0,nonradis determined from Equation (18). Köppen-Geiger climate classification, with different total irradiations. It can be seen that the increase in n and Rsreduces the efficiency The results for top-cell absorber thicknesses of 1 μm (closed circles) quite linearly, while the efficiency shows a saturation at Rsh≥ 1 and 500 nm (closed squares) are shown. The dotted lines indicate the kΩcm². For the increase of Q₀, the efficiency improves gradually. optimum Eg,topobtained for absorber thicknesses of 1 μm and 500 nm To obtain realistic maximum cell and module efficiencies, the under the standard calculation condition (i.e., T = 300 K and 100 mW/cm² [AM 1.5G]). (C) Average temperature during the module appropriate values of n, Rs, Rsh, and Q₀ are necessary. For the n of the operation as a function of the total irradiation. This result was perovskite cell, the significant role of the interface recombination has calculated from the corresponding places shown in (B) recently been reported; in an interface-optimized perovskite cell, a quite low value of n = 1.26 has been realized. On the other hand,

|FIGURE 15|Variations of the tandem module efficiency with (A) n, (B) R||, (C) R, and (D) Q₀ of the perovskite top cell at the standard testing|
|---|---|---|---|
|condition of T = 25 C and (E) J-V characteristics of the tandem module obtained assuming the top cell non-ideality factors of n = 1.26, R||||
|Ωcm², R|= 2.4 kΩcm² and Q₀ = Q|= 0.92, extracted from experimental perovskite cells.||
|parameters of E|= 1.697 eV and d|= 1 μm were assumed||

s sh = 0 s 15,60,74 For the calculation, the optimized tandem sh PL g,top pero

FF is influenced strongly by the grain size, 9 and a very high FF of 86% has been reported for a CH₃NH₃PbI₃ single cell (η = 21%) with a large grain size of 1.5 μm. 60 From this high-FF cell, we have extracted Rs and Rshby performing the J-V fitting analysis using Equation (9), which results in Rs= 0 Ωcm² and Rsh= 2.4 kΩcm². Finally, for a surface- passivated CH₃NH₃PbI₃ layer that exhibits a quite long carrier lifetime (~8 μs), 11 a quite high internal QPLof 92% has been reported. 74 The above best parameters (i.e., n = 1.26, Rs=0Ωcm², Rsh= 2.4 kΩcm², and Q₀ = QPL= 0.92) are indicated by circles in Figure 15.By adopting these experimentally derived parameters, we obtained the realistic device characteristics of the tandem cell (η = 34.69%, J sc= 19.04 mA/cm², Voc= 2.132 V, FF = 0.855) and the module (η = 30.76%, Jsc= 17.99 mA/cm², Voc= 2.129 V, FF = 0.855). In

Figure 15E, the corresponding tandem module J-V characteristics are

shown. As mentioned in Section 3.1, one problem of the Si bottom cell is a small Rsh(~0.9 kΩcm²), which is lower than the perovskite top cell (Rsh= 2.4 kΩcm²). From Figure 15E, it can be seen that the influ- ence of the low Rshin the bottom cell is almost completely eliminated in the top-cell limited condition. The above result shows that the effect of the non-ideal factors is not strong if experimental best values are achieved, although the cell non-ideality reduces the cell and mod- ule efficiencies by ~1% in efficiency, compared with the values shown in Table 1. In earlier perovskite/Si theoretical studies, lower tandem cell efficiencies of 27.6–32.5% have been reported, 24–26,28,32 whereas a very high efficiency of ~45% is obtained if an ideal Shockley-Queisser type assumption is made. 22,23 For the tandem module, a consistent

module efficiency of ~31% has been estimated. 27,31 In addition, previ- ous studies show that the tandem energy yield increases by 26–40%, compared with Si modules. 24,27,31 However, our estimate for the improved energy yield in the tandem device over the single device is higher than those of the earlier results, as confirmed from Figure 12B. It should be emphasized that the tandem cell/module efficiencies vary significantly with numerous parameters, including the device geome- try (flat, single-and double-side texture), 26–28 device structure (Si wafer 9,57 and layer thicknesses), diode parameters (n, Rs, Rsh, J₀)of the top and bottom cells. We mention that, in our calculation, all the device and structural parameters were extracted from the state-of-the-art Si and perovskite solar cells and the estimated tandem efficiencies of η = 34.69% (cell) and 30.76% (module) are realistically possible.

4.2 | Influence of diffused sun light In the energy yield calculations of Section 3, both direct and diffused sun light components were assumed to have a single incident angle (θin) determined from the direct sun light contribution and the influ- ence of the θinvariation in the diffused sun light was neglected completely. To justify our calculation results in Section 3, we have implemented calculations by considering both direct and diffused components using Equation (12). Here, results obtained using experi- mentally measured irradiance spectra of κdir(λ)(=φdir(λ)hc/λ) and κdiff(λ) (=φdiff(λ)hc/λ) are presented.

|Figure|16 shows|four irradiance|spectra|of κ (λ),|κ (λ),|each spectrum|of Figure|16. The|J indicates|the J estimated||
|---|---|---|---|---|---|---|---|---|---|---|---|
|and κ|(λ) calculated|for (A) AM1.5G|and measured|for|(B) a|assuming that all the sun light is direct component, whereas J||||||
|sunny sky|(Sunny),|(C) a cloudy|sky (Cloudy1),|and (D)|a heavy|represents|the J obtained|from|the exact|calculation|using|
|cloudy|sky (Cloudy2).|The κ|simply shows|a total given|by|Equation (14). In the table, the ratios of J|||and J|calculated for||
|κ (λ) = κ Cloudy2 were measured at midday (12:00) at Gifu city in Japan in|(λ) + κ|(λ). The sun|spectra of Sunny,|Cloudy1|and|each weather are also shown. It can be confirmed that (i) the calcula- tion error is less than 1% when the sky is clear and (ii) the difference||||||
|March 2012–2013. In particular, we have selected the spectral data of the cloudy skies so that the irradiance becomes half (Cloudy1) and one-third (Cloudy2) of the clear sky. The diffused sun spectra are blue||||||between incoming light is diffused. Accordingly, the J θ is a reasonable assumption, which allows the drastic reduction of|J and J|is still less|than 10% calculation by a single|even when|all the|
|rich, compared|with|the direct sun|spectra, due|to stronger|light|the calculation cost, and the results of Table 3 strongly support the||||||
|scattering similar to AM1.5G, although κ|in shorter|λ. The irradiance spectrum (λ) is slightly different. In Cloudy1, the||of Sunny|is quite|validity of our energy yield calculations described in Section 3. The small difference between J|||and J|can be understood||
|contribution|of κ|(λ) is dominant|and κ (λ)|is essentially|zero|from the weak dependence of the EQE spectrum on θ||||. Figure 17||
|in Cloudy2. Table 3 summarizes the J with the J|of the top cell (J|values of the tandem module, together ) and bottom cell (J||) obtained for||compares (θ = 0 ) and diffused component in (A) the single module and (B) the tandem module. In particular, to express the influence of the diffused|the EQE spectra|calculated|for the|direct component||

total dir dir sc sc diff dir sc þdiff sc total dir sc sc dirþdiff

total dir diff

dir sc sc dirþdiff

sc in

diff dir sc sc dirþdiff

diff dir in

sc in sc top bottom

FIGURE 16 Total (κtotal), direct (κdir)

and diffused (κdiff) components of irradiance spectra calculated for

(A) AM1.5G and measured for (B) a sunny sky (Sunny), (C) a cloudy sky (Cloudy1), and (D) a heavy cloudy sky (Cloudy2). The spectra of Sunny, Cloudy1, and Cloudy2 were measured at midday (12:00) at Gifu city in Japan in March 2012–2013. The irradiances of Cloudy1 and Cloudy 2 are half and one-third of the clear sky, respectively
TABLE 3 Jscvalues of the tandem module obtained from the simple calculation assuming a single θinof the direct sun component and the

exact calculation of Equation (14) assuming the direct and diffused sun components

Direct (single θin) Direct + diffused dir 2 2 2 dir 2 2 2 <u>J</u>dir <u>sc</u> Weather Jsc(mA/cm) Jtop(mA cm) Jbottom(mA/ cm) Jsc þdiff(mA/cm) Jtop(mA/ cm) Jbottom(mA/ cm) J dirþdiff sc AM1.5G 17.97 17.97 19.11 17.81 17.81 19.01 1.009 Sunny 18.09 18.09 18.67 17.96 17.96 18.57 1.008 Cloudy1 10.67 10.67 11.33 10.03 10.03 10.68 1.064 Cloudy2 4.65 4.98 4.65 4.30 4.60 4.30 1.082

Note: The Jscvalues of the tandem module obtained by considering the θinof direct and direct + diffused are shown as J

dir scand J dir sc þdiff, respectively. The J topand Jbottomdenote the Jscof the top and bottom cells, respectively. The calculation results for the different weather conditions of Figure 16 are shown.

Accordingly, in a place where a cloudy weather is more frequent, the energy yield is slightly overestimated. We, however, mention that the power generation decreases drastically under cloudy weather condi- tions and the overall effect of the energy-yield overestimation under cloudy weathers is expected to be minor.

FIGURE 17 EQE spectra of (A) the single and (B) the tandem

modules, calculated for the direct component (θin= 0 ) and diffused component (EQEeff). For the diffused light EQE, the effective EQE P spectrum calculated by EQEeff= P (θ)EQE (θ, T, λ) usingj j Equation (14) is shown

light contribution, the effective EQE spectrum for the diffused light P was calculated as EQEeff= P (θj)EQE (θj, T, λ) from Equation (14). It can be confirmed that both EQE spectra calculated for the direct and diffused components are essentially similar, even though the magni- tude of EQEeffreduces by ~8%, compared with EQE (θin= 0 ). This EQEeffreduction by ~8% explains J dir sc=J dir sc þdiff~ 8% (Cloudy2) in

Table 3.

Our result is consistent with an earlier study, 26 which indicated that the direct and diffused lights result in similar EQE spectra in the case of a double textured Si structure. The small variation of EQE with θ inhas been reported earlier, 75 and this result can be confirmed directly from Figure 10C, which shows a high RAof >80% in a wide range of 0 < θin<70. A similar trend can further be seen for θ in -dependent EQE spectra shown in Figure S5. On the other hand, the result of Table 3 does show that the energy yields in Section 3 are slightly overestimated under cloudy weather conditions due to the simple assumption of a fixed incident angle, which leads to a slightly higher EQE shown in Figure 17.

## 5 | CONCLUSION

To predict the global energy yields of fully textured hybrid perov- skite/Si tandem and Si heterojunction single modules, we have devel- oped a new general self-consistent scheme, which incorporates all fundamental device and weather factors. In the developed approach, in contrast to earlier studies, full EQE calculations are performed by explicitly incorporating the effects of module temperature and incident-angle variations in optical device calculations. In our model, the sun spectrum, sun incident angle, and module temperature are calculated from meteorological data as input variables, from which the incident-angle and temperature dependent module characteristics are determined by fully performing EQE, Jsc, J₀, and Voccalculations. To extract the reliable temperature-dependent diode parameters (i.e., J₀, R s, Rsh, and n) for an industry-compatible Si heterojunction solar cell with a 23.27% efficiency, the complete analyses of the temperature- dependent J-V and EQE characteristics are performed. The proposed calculation model has been justified from the excellent fitting of calcu- lated J-V and EQE to experimental data measured for real Si single and perovskite/Si tandem cells. From the exact optical-constant modeling of CsFAPb(I, Br)3top cell, we have performed the top-cell Egoptimization in a double-sided textured structure with realistic constituent layers, which results in E g,top= 1.697 eV for the top- and bottom-cell absorber thicknesses of 1 μm and 120 μm, respectively. When ideal device parameters are assumed for the perovskite top cell, we obtain the maximum cell efficiency of 35.84% and the corresponding module efficiency of

31.84% under a current mismatching condition that enhances FF. A theoretical temperature coefficient for the perovskite/Si module is found to be 0.174 %/K, which is notably lower than that of the Si heterojunction module ( 0.269 %/K). The rigorous energy yield calculations have been implemented at 762 places in North and South America by applying hourly irradi- ance and meteorological data for the year 2018. We find that, com- pared with a state-of-the-art Si heterojunction module, the tandem architecture improves the module energy yield uniformly with a maximum factor of 1.6. Our global energy estimation shows that the energy yields of the tandem and single modules scale linearly with total irradiation at sites. From the analysis based on Köppen- Geiger climate classification, we have further verified an influence of climate with a magnitude of ~5%. By considering the annual sun irradiation and climate effect, the global energy yields of the tandem and single modules are predicted. We further find that, when the actual weather conditions are considered, the optimum top cell Eg increases substantially, compared with that derived under the stan- dard conditions.

ACKNOWLEDGEMENTS The authors acknowledge Drs. Yoshihiro Hishikawa and Masahiro Yoshita of National Institute of Advanced Industrial Science and Technology (AIST) for their contribution of measuring temperature dependent J-V and EQE of the Si heterojunction solar cell.

CONFLICT OF INTEREST The authors declare no conflict of interest.

DATA AVAILABILITY STATEMENT The data of this study are available from the corresponding author upon reasonable request.

REFERENCES

1. Eperon GE, Hörantner MT, Snaith HJ. Metal halide perovskite tandem and multiple-junction photovoltaics. Nat Rev Chem. 2017;1(12):0095. doi:10.1038/s41570-017-0095
2. Leijtens T, Bush KA, Prasanna R, McGehee MD. Opportunities and challenges for tandem solar cells using metal halide perovskite semi- conductors. Nat Energy. 2018;3(10):828-838. doi:10.1038/s41560- 018-0190-4
3. Yu ZJ, Leilaeioun M, Holman Z. Selecting tandem partners for silicon solar cells. Nat Energy. 2016;1(11):16137. doi:10.1038/nenergy.
2016.137
4. Chen B, Zheng X, Bai Y, Padture NP, Huang J. Progress in tandem solar cells based on hybrid organic–inorganic perovskites. Adv Energy Mater. 2017;7(14):1602400. doi:10.1002/aenm. 201602400
5. Werner J, Niesen B, Ballif C. Perovskite/silicon tandem solar cells: marriage of convenience or true love story?—an overview. Adv Mater Interfaces. 2018;5(1):1700731. doi:10.1002/admi. 201700731
6. Jošt M, Kegelmann L, Korte L, Albrecht S. Monolithic perovskite tandem solar cells: a review of the present status and advanced characterization methods toward 30% efficiency. Adv Energy Mater. 2020;10(26):1904102. doi:10.1002/aenm.201904102
7. Huang J, Yuan Y, Shao Y, Yan Y. Understanding the physical proper- ties of hybrid perovskites for photovoltaic applications. Nat Rev Mater. 2017;2(7):17042. doi:10.1038/natrevmats.2017.42
8. Jena AK, Kulkarni A, Miyasaka T. Halide perovskite photovoltaics: background, status, and future prospects. Chem Rev. 2019;119(5): 3036-3103. doi:10.1021/acs.chemrev.8b00539
9. Fujiwara H. Hybrid Perovskite Solar Cells: Characteristics and Operation. Weinheim, Germany: Wiley-VCH; 2022.
10. Shirayama M, Kadowaki H, Miyadera T, et al. Optical transitions in hybrid perovskite solar cells: ellipsometry, density functional theory, and quantum efficiency analyses for CH₃NH₃PbI₃. Phys Rev Appl. 2016;5(1):014012. doi:10.1103/PhysRevApplied.5.014012
11. deQuilettes DW, Koch S, Burke S, et al. Photoluminescence lifetimes exceeding 8 μs and quantum yields exceeding 30% in hybrid perovskite thin films by ligand passivation. ACS Energy Lett. 2016;1(2): 438-444. doi:10.1021/acsenergylett.6b00236
12. McMeekin DP, Sadoughi G, Rehman W, et al. A mixed-cation lead mixed-halide perovskite absorber for tandem solar cells. Science. 2016;351(6269):151-155. doi:10.1126/science.aad5845
13. Bush KA, Palmstrom AF, Yu ZJ, et al. 23.6%-efficient monolithic perovskite/silicon tandem solar cells with improved stability. Nat Energy. 2017;2(4):17009. doi:10.1038/nenergy.2017.9
14. Sahli F, Werner J, Kamino BA, et al. Fully textured monolithic perovskite/silicon tandem solar cells with 25.2% power conversion
efficiency. Nat Mater. 2018;17(9):820-826. doi:10.1038/s41563- 018-0115-4

15. Al-Ashouri A, Köhnen E, Li B, et al. Monolithic perovskite/silicon tandem solar cell with >29% efficiency by enhanced hole extraction. Science. 2020;370(6522):1300-1309. doi:10.1126/ science.abd4016
16. Hou Y, Aydin E, Bastiani MD, et al. Efficient tandem solar cells with solution-processed perovskite on textured crystalline silicon. Science. 2020;367(6482):1135-1140. doi:10.1126/science.aaz3691
17. Isikgor FH, Furlan F, Liu J, et al. Concurrent cationic and anionic perovskite defect passivation enables 27.4% perovskite/silicon tandems with suppression of halide segregation. Joule. 2021;5(6): 1566-1586. doi:10.1016/j.joule.2021.05.013
18. Roß M, Severin S, Stutz MB, et al. Co-evaporated formamidinium lead iodide based perovskites with 1000 h constant stability for fully textured monolithic perovskite/silicon tandem solar cells. Adv Energy Mater. 2021;11(35):2101460. doi:10.1002/aenm.202101460
19. NREL. Best research-cell efficiency chart. Accessed March 2022. [https://www.nrel.gov/pv/cell-efficiency.html](https://www.nrel.gov/pv/cell-efficiency.html)
20. Yoshikawa K, Kawasaki H, Yoshida W, et al. Silicon heterojunction solar cell with interdigitated back contacts for a photoconversion effi- ciency over 26%. Nat Energy. 2017;2(5):17032. doi:10.1038/nenergy.
2017.32
21. Aydin E, Allen TG, Bastiani MD, et al. Interplay between temperature and bandgap energies on the outdoor performance of perovskite/silicon tandem solar cells. Nat Energy. 2020;5(11):851-
859. doi:10.1038/s41560-020-00687-4
22. Dupré O, Niesen B, Wolf SD, Ballif C. Field performance versus stan- dard test condition efficiency of tandem solar cells and the singular case of perovskites/silicon devices. J Phys Chem Lett. 2018;9(2):446-
458. doi:10.1021/acs.jpclett.7b02277
23. Futscher MH, Ehrler B. Efficiency limit of perovskite/Si tandem solar cells. ACS Energy Lett. 2016;1(4):863-868. doi:10.1021/acsenergylett. 6b00405
24. Hörantner MT, Snaith HJ. Predicting and optimising the energy yield of perovskite-on-silicon tandem solar cells under real world conditions. Energ Environ Sci. 2017;10(9):1983-1993. doi:10.1039/ C7EE01232B
25. Futscher MH, Ehrler B. Modeling the performance limitations and prospects of perovskite/Si tandem solar cells under realistic operating conditions. ACS Energy Lett. 2017;2(9):2089-2095. doi:10.1021/ acsenergylett.7b00596
26. Jošt M, Köhnen E, Morales-Vilches AB. Textured interfaces in mono- lithic perovskite/silicon tandem solar cells: advanced light manage- ment for improved efficiency and energy yield. Energ Environ Sci. 2018;11(12):3511-3523. doi:10.1039/C8EE02469C
27. Lehr J, Langenhorst M, Schmager R, et al. Energy yield modelling of perovskite/silicon two-terminal tandem PV modules with flat and textured interfaces. Sustain Energy Fuels. 2018;2(12):2754-2761. doi:10.1039/C8SE00465J
28. Tucher N, Höhn O, Murthy JN, et al. Energy yield analysis of textured perovskite silicon tandem solar cells and modules. Opt Express. 2019; 27(20):A1419-A1430. doi:10.1364/OE.27.0A1419
29. Schmager R, Langenhorst M, Lehr J, Lemmer U, Richards BS, Paetzold UW. Methodology of energy yield modelling of perovskite- based multi-junction photovoltaics. Opt Express. 2019;27(8):A507- A523. doi:10.1364/OE.27.00A507
30. Onno A, Rodkey N, Asgharzadeh A, et al. Predicted power output of silicon-based bifacial tandem photovoltaic systems. Joule. 2020;4(3): 580-596. doi:10.1016/j.joule.2019.12.017
31. Liu H, Rodriguez-Gallegos CD, Liu Z, Buonassisi T, Reindl T, Peters IM. A worldwide theoretical comparison of outdoor potential for various silicon-based tandem module architecture. Cell Rep Phys Sci. 2020;1(4):100037. doi:10.1016/j.xcrp.2020.100037

32. Jäger K, Tillmann P, Katz EA, Becker C. Perovskite/silicon tandem solar cells: effect of luminescent coupling and bifaciality. Sol RRL. 2020;5(3):2000628. doi:10.1002/solr.202000628
33. Bastiani MD, Kerschaver EV, Jeangros Q, et al. Toward stable monolithic perovskite/silicon tandem photovoltaics: a six-month out- door performance study in a hot and humid climate. ACS Energy Lett. 2021;6(8):2944-2951. doi:10.1021/acsenergylett.1c01018
34. Davies CL, Filip MR, Patel JB, et al. Bimolecular recombination in methylammonium lead triiodide perovskite is an inverse absorption process. Nat Commun. 2018;9(1):293. doi:10.1038/s41467-017- 02670-2
35. Fujiwara H, Collins RW. Spectroscopic Ellipsometry for Photovoltaics: Vol.1: Fundamental Principles and Solar Cell Characterization. Cham, Switzerland: Springer; 2018. doi:10.1007/978-3-319-75377-5_1.
36. Lautenschlager P, Garriga M, Vina L, Cardona M. Temperature dependence of the dielectric function and interband critical points in silicon. Phys Rev. 1987;36(9):4821-4830. doi:10.1103/PhysRevB.
36.4821
37. Nishigaki Y, Nagai T, Nishiwaki M, et al. Extraordinary strong band- edge absorption in distorted chalcogenide perovskites. Sol RRL. 2020; 4(5):1900555. doi:10.1002/solr.201900555
38. Taguchi M, Yano A, Tohoda S, et al. 24.7% record efficiency HIT solar cell on thin silicon wafer. IEEE J Photovolt. 2014;4(1):96-99. doi:10.1109/JPHOTOV.2013.2282737
39. Taguchi M, Kawamoto K, Tsuge S, et al. HIT™ cells—high-efficiency crystalline Si cells with novel structure. Progress in Photovoltaics: Research and Applications. 2000;8(5):503-513. doi:10.1002/1099- 159X(200009/10)8:53.0.CO;2-G
40. Sahli F, Kamino BA, Werner J, et al. Improved optics in monolithic perovskite/silicon tandem solar cells with a nanocrystalline silicon recombination junction. Adv Energy Mater. 2017;8(6):1701609. doi:10.1002/aenm.201701609
41. Stolterfoht M, Wolff CM, Márquez JA, et al. Visualization and suppression of interfacial recombination for high-efficiency large- area pin perovskite solar cells. Nat Energy. 2018;3(10):847-854. doi:10.1038/s41560-018-0219-8
42. Fujiwara H, Collins RW. Spectroscopic Ellipsometry for Photovoltaics: Vol.2: Applications and Optical Data of Solar Cell Materials. Cham, Switzerland: Springer; 2018. doi:10.1007/978-3-319-95138-6.
43. Wynands D, Erber M, Rentenberger R, et al. Spectroscopic ellipsometry characterization of vacuum-deposited organic films for the application in organic solar cells. Org Electron. 2012;13(5):885-
893. doi:10.1016/j.orgel.2012.01.036
44. Jellison GE Jr, Modine FA. Parameterization of the optical functions of amorphous materials in the interband region [published erratum appears in Appl Phys Lett. 1996;69:2137]. Appl Phys Lett. 1996;69:
371. doi:10.1063/1.118064
45. Tejada A, Braunger S, Korte L, Albrecht S, Rech B, Guerra JA. Optical characterization and bandgap engineering of flat and wrinkle-textured FA0.83Cs0.17Pb(I1–xBrx)3perovskite thin films. J Appl Phys. 2018; 123(17):175302. doi:10.1063/1.5025728
46. King DL, Boyson WE, Kratochvil JA. Photovoltaic Array Performance Model. Technical Report SAND2004–3535. Sandia National Labs, USA; 2004.
47. Nakane A, Fujimoto S, Fujiwara H. Fast determination of the current loss mechanisms in textured crystalline Si-based solar cells. J Appl Phys. 2017;122(20):203101. doi:10.1063/1.4997063
48. Yao J, Kirchartz T, Vezie MS, et al. Quantifying losses in open-circuit voltage in solution-processable solar cells. Phys Rev Appl. 2015;4(1): 014020. doi:10.1103/PhysRevApplied.4.014020
49. Kato Y, Fujimoto S, Kozawa M, Fujiwara H. Maximum efficiencies and performance-limiting factors of inorganic and hybrid perovskite solar cells. Phys Rev Appl. 2019;12(2):024039. doi:10.1103/ PhysRevApplied.12.024039
50. Smets AHM, Jaeger K, Isabella O, Swaaij RV, Zeman M. Solar Energy: The Physics and Engineering of Photovoltaic Conversion, Technologies and Systems. Cambridge, England: UIT Cambridge; 2016.
51. National Renewable Energy Laboratory. NSRDB data viewer. Accessed January 2021. [https://maps.nrel.gov/nsrdb-viewer](https://maps.nrel.gov/nsrdb-viewer)
52. Xie Y, Sengupta M. A fast all-sky radiation model for solar applica- tions with narrowband irradiances on tilted surfaces (FARMS-NIT): part I. The clear-sky model. Solar Energy. 2018;174:691-702. doi:10. 1016/j.solener.2018.09.056
53. Xie Y, Sengupta M, Wang C. A fast all-sky radiation model for solar applications with narrowband irradiances on tilted surfaces (FARMS-NIT): part II. The cloudy-sky model. Solar Energy. 2019;188: 799-812. doi:10.1016/j.solener.2019.06.058
54. Tiedje T, Yablonovitch E, Cody GD, Brooks BG. Limiting efficiency of silicon solar cells. IEEE Trans Electron Devices. 1984;31(5):711-716. doi:10.1109/T-ED.1984.21594
55. Green MA. Limits on the open-circuit voltage and efficiency of silicon solar cells imposed by intrinsic Auger processes. IEEE Trans Electron Devices. 1984;31(5):671-678. doi:10.1109/T-ED.1984.21588
56. Taguchi M, Maruyama E, Tanaka M. Temperature dependence of amorphous/crystalline silicon heterojunction solar cells. Jpn J Appl Phys. 2008;47(2):814-818. doi:10.1143/JJAP.47.814
57. Stolterfoht M, Caprioglio P, Wolff CM, et al. The impact of energy alignment and interfacial recombination on the internal and external open-circuit voltage of perovskite solar cells. Energ Environ Sci. 2019; 12(9):2778-2788. doi:10.1039/C9EE02020A
58. Sarritzu V, Sestu N, Marongiu D, et al. Optical determination of Shockley-Read-Hall and interface recombination currents in hybrid perovskites. Sci Rep. 2017;7(1):44629. doi:10.1038/srep44629
59. Köhnen E, Wagner P, Lang F, et al. 27.9% efficient monolithic perovskite/silicon tandem solar cells on industry compatible bottom cells. Sol RRL. 2021;5(7):2100244. doi:10.1002/solr. 202100244
60. Chiang CH, Wu CG. A method for the preparation of highly oriented MAPbI₃ crystallites for high-efficiency perovskite solar cells to achieve an 86% fill factor. ACS Nano. 2018;12(10):10355-10364. doi:10.1021/acsnano.8b05731
61. Köhnen E, Jošt M, Morales-Vilches AB, et al. Highly efficient mono- lithic perovskite silicon tandem solar cells: analyzing the influence of current mismatch on device performance. Sustain Energy Fuels. 2019; 3(8):1995-2005. doi:10.1039/C9SE00120D
62. Wright AD, Verdi C, Milot RL, et al. Electron–phonon coupling in hybrid lead halide perovskites. Nat Commun. 2016;7(1):11755. doi:10.1038/ncomms11755
63. Jošt M, Lipovšek B, Glažar B, et al. Perovskite solar cells go outdoors: field testing and temperature effects on energy yield. Adv Energy Mater. 2020;10(25):2000454. doi:10.1002/aenm.202000454
64. Taguchi M, Terakawa A, Maruyama E, Tanaka M. Obtaining a higher V ocin HIT cells. Progress in Photovoltaics: Research and Applications. 2005;13(6):481-488. doi:10.1002/pip.646
65. Herrmann W, Schweiger M, Rimmelspacher L. 29th European Photovoltaic Solar Energy Conf. and Exhibition. Amsterdam, Niederlande; 2014:2403-2406.
66. Peters IM, Buonassisi T. Energy yield limits for single-junction solar cells. Joule. 2018;2(6):1160-1170. doi:10.1016/j.joule.2018.
03.009
67. Ascencio-Vásquez J, Brecl K, Topič M. Methodology of Köppen-Geiger-Photovoltaic climate classification and implications to worldwide mapping of PV system performance. Sol Energy. 2019;191: 672-685. doi:10.1016/j.solener.2019.08.072
68. Ishii T, Otani K, Takashima T, Xue Y. Solar spectral influence on the performance of photovoltaic (PV) modules under fine weather and cloudy weather conditions. Progress in Photovoltaics: Research and Applications. 2013;21:481-489.

69. Hoke ET, Slotcavage DJ, Dohner ER, Bowring AR, Karunadasa HI, 75. Ba L, Wang T, Wang J, Shen W. Perovskite/c-Si monolithic tandem McGehee MD. Reversible photo-induced trap formation in mixed-solar cells under real solar spectra: improving energy yield by oblique

|incident|J Phys Chem|C. 2019;123(47):28659-28667.|
|---|---|---|
|doi:10.1021/acs.jpcc.9b10186|||
 halide hybrid perovskites for photovoltaics. Chem Sci. 2015;6(1):613-incident optimization. J Phys Chem C. 2019;123(47):28659-28667.
617. doi:10.1039/C4SC03141E
70. Brennan MC, Draguta S, Kamat PV, Kuno M. Light-induced anion phase segregation in mixed halide perovskites. ACS Energy Lett. 2018; 3(1):204-213. doi:10.1021/acsenergylett.7b01151 SUPPORTING INFORMATION
71. Xu J, Boyd CC, Yu ZJ, et al. Triple-halide wide–band gap perovskites
Additional supporting information may be found in the online version with suppressed phase segregation for efficient tandems. Science. of the article at the publisher's website. 2020;367(6482):1097-1104. doi:10.1126/science.aaz5074

72. Bastiani MD, Mirabelli AJ, Hou Y, et al. Efficient bifacial monolithic perovskite/silicon tandem solar cells via bandgap engineering. Nat Energy. 2021;6(2):167-175. doi:10.1038/s41560-020-00756-8 How to cite this article: Kato Y, Katayama H, Kobayashi T,
73. Vandewal K, Tvingstedt K, Gadisa A, Inganäs O, Manca JV. On the et al. Global prediction of the energy yields for hybrid origin of the open-circuit voltage of polymer–fullerene solar cells. Nat perovskite/Si tandem and Si heterojunction single solar Energy. 2009;8(11):904-909. doi:10.1038/nmat2548
modules. Prog Photovolt Res Appl. 2022;30(10):1198‐1218.

74. Braly IL, deQuilettes DW, Pazos-Outon LM, et al. Hybrid perovskite ~
doi:10.1002/pip.3569 films approaching the radiative limit with over 90% photo- luminescence quantum efficiency. Nat Photonics. 2018;12(6):355-

361. doi:10.1038/s41566-018-0154-z
