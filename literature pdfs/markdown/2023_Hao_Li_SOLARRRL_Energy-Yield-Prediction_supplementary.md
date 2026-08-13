# Supporting Information

## Energy yield prediction of bifacial perovskite/silicon tandem photovoltaic modules

*Hongwei Hao, Shan-Ting Zhang*, Kai Wang, Peizhi Yang, Jilei Wang, Liyou Yang, Linfeng* *Lu, Dongdong Li**

## Note S1

## Optical simulations for solar cells and their corresponding modules

A viable perovskite (PVK) thickness of 500-900 nm is investigated to obtain the optimal value. The stacked materials of both solar cells and corresponding modules are labeled in **Figure S1**, whose optical properties are modeled using a combination of ray tracing and transfer matrix methods using SunSolve TM. [1] The refractive indices of PVK with bandgap (*E*g_PVK) of

1.557, 1.62 and 1.67 eV are obtained from literature
[2]. In terms of the optical parameters for other *E*g_PVK, we use **Equation (1)** to translates n and k pairing to a new position on the wavelength axis: [2] 𝜆 𝜆𝑛𝑒𝑤= (𝜆 − 𝛥𝜆𝑏𝑎𝑛𝑑𝑔𝑎𝑝+ 10) × () (1) 1200 where 𝛥𝜆bandgap is the difference in bandgap between the PVK of a known bandgap and the desired wide bandgap material, expressed as a wavelength in nanometers.10 is an empirically determined offset. The arbitrarily chosen wavelength of 1200 nm in the stretching factor implies that the optical constants are overstretched at longer wavelengths, but this has little effect because k = 0 and n are relatively constant in the IR region. **Figure S2** shows the n and k values of PVK with bandgaps of 1.58, 1.60 and 1.70 eV after the above transformation.

## Note S2

## Detailed procedure and parameter setting of electrical simulation

The electrical simulations are performed by the LTspice software. [3] An equivalent circuit with a one-diode (inset of **Figure 2d**) is used for the simulation, where the photogenerated current (*J*G), the dark saturation current (*J₀*), the ideal factor (*n*), the series resistance (*R*S) and the shunt resistance (*R*sh) are used as input parameters. The photogenerated current can be obtained from the short-circuit current (*J*sc) of the cell or module obtained from the optical simulation. The other diode parameters of the SHJ solar cell were extracted from the *J*-*V* curves reported in the literature. [4] The dark saturation current *J₀* of the PVK solar cell is obtained by

|𝑞|∞||
|---|---|---|
|𝐸𝑄𝐸𝐸𝐿|0|𝐵𝐵 𝐵𝐵|

𝐽₀ = × ∫ 𝐸𝑄𝐸𝑃𝑉(𝐸) × 𝜙 (𝐸)𝑑𝐸 (2) where *EQE*EL is electroluminescent emission efficiency. 𝜙 is the photon flux in a blackbody at a temperature of 300 K which is a function of energy E, defined by Planck's law as:

|𝐸2||
|---|---|
|4𝜋2ℏ3𝑐2exp(𝑘𝑇)−1|𝐸|

𝜙𝐵𝐵(𝐸) = (3)

where *ħ* is Planck's constant divided by 2π, *c* the speed of light, and *k* the Boltzmann constant. We obtained the *J₀* values of PVK with different bandgaps by assuming an *EQE*EL of 0.01%. [5] The remaining parameters are also extracted from the *J*-*V* curves reported in the literature. [6] Assuming that all PVK solar cells with different bandgaps have the same *n*, *R*sh, and *R*s, the diode parameters used for the SHJ solar cell and PVK solar cell simulations are listed in **Table** **S1**. The *J*-*V* plots of single-junction SHJ solar cell and PVK sub-cells in tandem solar cells are then obtained as shown in **Figures S5 and S6** based on the above one-diode parameters and AM1.5G front side illumination. The electrical performance of the single-junction SHJ solar cell is similar to that in the literature. [4] The *J*-*V*curves of PVK top cells with different bandgaps show the same trend as in the literature. [7]

## Note S3

## The calculation of levelized cost of electricity (LCOE)

The levelized cost of electricity (LCOE) is the ratio of the total life cycle cost of a PV system to the total energy generated during the life cycle of that system, and it can be calculated using the **Equation (4)**: [8-10] ∑𝑇𝑡=0 <u>𝐶𝑡</u> <u>𝑡</u> <u>(1+𝑟)</u> LCOE = <u>𝐸𝑌×(1−𝑑)𝑡</u>

(4)
∑𝑇𝑡=0 𝑡 (1+𝑟) where *T* is the module lifetime, *t* the year of project operation, *Ct* the total cost of the system in year *t*, EY the energy yield in year *t*, *r*the discount rate, and *d*the degradation rate of the module. The annual total cost of the system (*Ct*) can be expressed by **Equation (5)**: [11] 𝐶𝑡= 𝐼𝑡+ 𝑂𝑡+ 𝐹𝑡(5) where *It* is the installation cost, *Ot* the system operation and maintenance cost, and *Ft* the financing cost in year *t*. Note that the installation cost occurs only in the year t = 0. [12-13] To simply the calculation of LCOE, the financing costs *Ft* was not considered in our calculation, [13] also the operation and maintenance cost of the system *Ot* was estimated as ~1% of the installation cost *I₀*. [14] We assume the module lifetime of 20 years, an efficiency degradation rate of 0.75%, and a discount rate of 5%. For comparative purpose, the installation

cost of tandem PVK/*c*-Si module is assumed to be higher than that of SHJ PV modules by 10%, 13%, and 15% respectively.

## Figures and Tables

**Figure S1**. Schematic diagram of the structure of (a) bifacial SHJ solar cell, bifacial and monofacial PVK/*c*-Si tandem solar cell, as well as the (b) corresponding modules.

**Figure S2.** Optical constants of PVK with bandgaps of 1.557 eV, 1.58 eV, 1.60 eV, 1.62 eV,

1.67 eV, and 1.70 eV as input for optical analysis and full simulation of solar cells and PV modules.

**Table S1**. Parameters of the absorber materials used as input in the LTspice electrical simulations.

|Solar cells|J₀ -2 (mA·cm )|n|R s (Ω·cm² )|R sh (Ω·cm² )|
|---|---|---|---|---|
|SHJ|1.60e-13|0.87|0.1|2100|
|Perovskite 1.557 eV|1.98e-17|1.17|4.2|3000|
|Perovskite 1.58 eV|6.87e-18|1.17|4.2|3000|
|Perovskite 1.60 eV|4.18e-18|1.17|4.2|3000|
|Perovskite 1.62 eV|2.82e-18|1.17|4.2|3000|
|Perovskite 1.67 eV|4.94e-19|1.17|4.2|3000|
|Perovskite 1.70 eV|1.51e-19|1.17|4.2|3000|

**Figure S3.** The *J*sc_PVK and *J*sc_*c*-Si in monofacial tandem solar cells as a function of perovskite layer thickness, with the bandgap of perovskite material set as 1.67 eV. The inset is a magnified view of 800 nm to 850 nm.

**Figure S4**. Optical loss analysis of (a) monofacial, (b) bifacial PVK/*c*-Si tandem solar cell, (c) bifacial SHJ solar cell, and (d) bifacial SHJ PV module.

**Table S2**. Current losses of monofacial and bifacial PVK/*c*-Si tandem solar cells and corresponding modules

|Material|References of refractive indices|Monofacial solar cell|Bifacial solar cell|Monofacial PV module|Bifacial PV module|
|---|---|---|---|---|---|
|||Equivalent current density -2 (mA·cm )|Equivalent current density -2 (mA·cm )|Equivalent current density -2 (mA·cm )|Equivalent current density -2 (mA·cm )|
|MgF2|Ref. [15]|0.56|0.53|N/A|N/A|
|IZO|Ref. [16]|1.97|1.88|1.58|1.45|
|ALD SnO2|Ref. [17]|0.04|0.04|0.03|0.03|
|C60|Ref. [2]|0.75|0.75|0.72|0.72|
|Perovskite ( E g = 1.67 eV)|Ref. [2]|19.89|19.90|19.31|19.32|
|PTAA|Ref. [18]|0|0|0|0|
|ITO front|Ref. [19]|0.11|0.10|0.11|0.09|
|a-Si (n)|Ref. [20]|0|0|0|0|
|a-Si (i)|Ref. [20]|0|0|0|0|
|a-Si (p)|Ref. [20]|0|0|0|0|
|c -Si|Ref. [21]|19.90|19.24|19.17|18.42|
|ITO rear|Ref. [19]|1.64|1.00|1.65|0.99|
|Ag|Ref. [22]|0.22|N/A|0.22|N/A|
|Glass|Ref. [23]|N/A|N/A|0.73|0.82|
|Glass ARC|Ref. [24]|N/A|N/A|0|0.94|
|EVA|Ref. [25]|N/A|N/A|0.89|N/A|

**Table S3**. Current losses of bifacial SHJ solar cells and corresponding modules

|Material|References of refractive indices|Bifacial solar cell|Bifacial PV module|
|---|---|---|---|
|||Equivalent current density -2 (mA·cm )|Equivalent current density -2 (mA·cm )|
|MgF₂|Ref. [15]|0.57|N/A|
|ITO front|Ref. [19]|1.05|0.78|
|a-Si (n)|Ref. [20]|0.97|0.81|
|a-Si (i)|Ref. [20]|0.65|0.56|
|a-Si (p)|Ref. [20]|0|0|
|c -Si|Ref. [21]|39.00|37.55|
|ITO rear|Ref. [19]|1.09|1.07|
|Glass|Ref. [23]|N/A|0.96|
|Glass ARC|Ref. [24]|N/A|0|
|EVA|Ref. [25]|N/A|0.85|

**Figure S5**. The solid line is the *J*-*V* curve of a single-junction SHJ solar cell from Ref. [4]. The dashed line is the *J*-*V* curve of the single-junction SHJ solar cell obtained by fitting with LTspice software.

**Figure S6**. *J*-*V* curve of PVK sub-cells in tandem solar cells fitted by LTspice software

**Figure S7**. Pseudo-EQE curves of bifacial tandem modules for different albedo conditions.

**Figure S8**. *J*-*V* curves for bifacial tandem modules at albedo = 0% and 25%. IND stands for independent.

**Figure S9**. Current mismatch (*J*sc_mismatch = *J*sc_PVK-*J*sc_*c*-Si) versus *FF* for bifacial tandem PV modules with different *E*g_PVK for albedo = 0% and 25%, with *J*sc_PVK as the limiting current for *J*sc_mismatch < 0 and *J*sc_*c*-Si for *J*sc_mismatch > 0. The larger the current mismatch the higher the *FF*.

**Figure S10**. Meteorological data for (a) Chengdu, (b) London, (c) Shanghai, (d) Yinchuan, (e) Lhasa, and (f) Los Angeles. DNI and DHI are abbreviations for Direct Normal Irradiance and Diffuse Horizontal Irradiance, respectively.

**Figure S11.** (a) The global horizontal irradiance (GHI) of Lhasa and Los Angeles. (b) The EY comparison between Lhasa and Los Angeles for all seasons at an albedo of 25% and *E*g_PVK of

1.62 eV. The inset shows the annual EY comparison.
**Figure S12**. EY of bifacial SHJ modules with bifacial PVK/*c*-Si tandem modules in (a) Chengdu, (b) London, (c) Shanghai, (d) Yinchuan, (e) Lhasa, and (f) Los Angeles.

**Figure S13**. EY as a function of albedo for bifacial SHJ modules and bifacial PVK/*c*-Si tandem modules of different *E*g_PVK in (a) Chengdu, (b) London, (c) Shanghai, (d) Yinchuan, (e) Lhasa, and (f) Los Angeles.

**Figure S14**. Ratio of LCOE for bifacial tandem (LCOEtandem) and bifacial SHJ modules (LCOESHJ) as a function of albedo. *C*inc represents the installation cost increments (*C*inc: 13%).

References [1] PV Lighthouse, [https://www.pvlighthouse.com.au/sunsolve](https://www.pvlighthouse.com.au/sunsolve), accessed: **2022**. [2] S. Manzoor, J. Hausele, K. A. Bush, A. F. Palmstrom, J. Carpenter, Z. J. Yu, S. F. Bent,

M. D. McGehee, Z. C. Holman, *Opt Express* **2018**, 26, 27441.
[3] LTspice, [https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-) simulator.html, accessed: **2022**. [4] X. Ru, M. Qu, J. Wang, T. Ruan, M. Yang, F. Peng, W. Long, K. Zheng, H. Yan, X. Xu, *Solar Energy Materials and Solar Cells* **2020**, 215, 110643. [5] K. Tvingstedt, O. Malinkiewicz, A. Baumann, C. Deibel, H. J. Snaith, V. Dyakonov, H.

J. Bolink, *Sci Rep* **2014**, 4, 6071.
[6] H. Fan, F. Li, P. Wang, Z. Gu, J. H. Huang, K. J. Jiang, B. Guan, L. M. Yang, X. Zhou,

Y. Song, *Nat Commun* **2020**, 11, 5402.
[7] M. T. Hörantner, H. J. Snaith, *Energy & Environmental Science* **2017**, 10, 1983. [8] K. Branker, M. J. M. Pathak, J. M. Pearce, *Renewable and Sustainable Energy Reviews* **2011**, 15, 4470. [9] Z. Li, Y. Zhao, X. Wang, Y. Sun, Z. Zhao, Y. Li, H. Zhou, Q. Chen, *Joule* **2018**, 2, 1559. [10] C. Messmer, B. S. Goraya, S. Nold, P. S. C. Schulze, V. Sittinger, J. Schön, J. C. Goldschmidt, M. Bivour, S. W. Glunz, M. Hermle, *Progress in Photovoltaics: Research* *and Applications* **2020**, 29, 744. [11] Z. N. Song, C. L. McElvany, A. B. Phillips, I. Celik, P. W. Krantz, S. C. Watthage, G. K. Liyanage, D. Apul, M. J. Heben, *Energy & Environmental Science*, 10, 1297.

[12] M. De Bastiani, A. S. Subbiah, M. Babics, E. Ugur, L. Xu, J. Liu, T. G. Allen, E. Aydin,

S. De Wolf, *Joule*, 6, 1431.
[13] K. Branker, M. J. M. Pathak, J. M. Pearce, *Renew Sust Energ Rev* **2011**, 15, 4470. [14] M. Bolinger, Joachim Seel, and Dana Robson., Utility-Scale Solar: Empirical Trends in Project Technology, Cost, Performance, and PPA Pricing in the United States: 2019 Edition, [https://escholarship.org/uc/item/336457p8](https://escholarship.org/uc/item/336457p8), accessed: **2022**. [15] J. M. Siqueiros, R. Machorro, L. E. Regalado, *Appl Opt* **1988**, 27, 2549. [16] M. Morales-Masis, S. Martin De Nicolas, J. Holovsky, S. De Wolf, C. Ballif, *IEEE* *Journal of Photovoltaics* **2015**, 5, 1340. [17] M. N. Mullings, C. Hagglund, S. F. Bent, *J Vac Sci Technol A* **2013**, 31, 061503. [18] R. Santbergen, R. Mishima, T. Meguro, M. Hino, H. Uzu, J. Blanker, K. Yamamoto, M. Zeman, *Opt Express* **2016**, 24, A1288. [19] Z. C. Holman, M. Filipič, A. Descoeudres, S. De Wolf, F. Smole, M. Topič, C. Ballif, *Journal of Applied Physics* **2013**, 113, 013107. [20] Z. C. Holman, A. Descoeudres, L. Barraud, F. Z. Fernandez, J. P. Seif, S. De Wolf, C. Ballif, *IEEE Journal of Photovoltaics* **2012**, 2, 7. [21] H. T. Nguyen, F. E. Rougieux, B. Mitchell, D. Macdonald, *Journal of Applied Physics* **2014**, 115, 043710. [22] Y. Jiang, S. Pillai, M. A. Green, *Sci Rep* **2016**, 6, 30605. [23] M. R. Vogt, H. Hahn, H. Holst, M. Winter, C. Schinke, M. Kontges, R. Brendel, P. P. Altermatt, *IEEE Journal of Photovoltaics* **2016**, 6, 111. [24] M. R. Vogt, *PhD Thesis*, Delft University of Technology, **2015**. [25] K. R. McIntosh, J. N. Cotsell, J. S. Cumpston, A. W. Norris, N. E. Powell, B. M. Ketola, presented at *2009 34th IEEE Photovoltaic Specialists Conference (PVSC)*, 7-12 June,

**2009**.
