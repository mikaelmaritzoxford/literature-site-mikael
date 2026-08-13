Silicon [https://doi.org/10.1007/s12633-025-03618-8](https://doi.org/10.1007/s12633-025-03618-8)

### RESEARCH

**Ray Tracing of Light Trapping Strategies in Thin Silicon Solar Cells based on Tunnel Oxide Passivated Contact (TOPCon)**

**1,2** **Mohamad Fathul Bari Mohd Fuad¹· Mohd Marzaini Mohd Rashid¹· Mohd Zamir Pakhuruddin**

Received: 31 July 2025 / Accepted: 26 December 2025 © The Author(s) 2026

### Abstract

Tunnel oxide passivated contact (TOPCon) silicon (Si) solar cells, which utilise n-type silicon wafers, thin oxide layers, and polycrystalline silicon, are gaining popularity in photovoltaic industry due to its high efficiency potential. While 160 μm Si wafers are often used in current mass production, thinner wafers are projected to become mainstream in the future to reduce production costs. However, the decrease in the Si thickness reduces light absorptance, leading to lower device efficiency. Light-trapping strategies are utilised to enhance light absorptance in thin TOPCon cells and compensate for the efficiency loss. This work investigates light-trapping strategies in 100 μm-thin TOPCon cells using SunSolve. Upright pyramids with various heights and double layer anti-reflective coating (DLARC) silicon dioxide/silicon nitride (SiO2/SiNx), silicon oxyni- tride/silicon nitride (SiOxNy/SiNx) and aluminium oxide/silicon nitride (Al2O₃/SiNx) with various thicknesses are examined to produce optimise average reflectance (Ravg), short-circuit current density (Jsc) and efficiency (η). From the results, the device with 5 μm front upright pyramids, SiO2/SiNx DLARC (60 nm/60 nm), and 1 μm rear upright pyramids exhibits Ravg, −2 J and η of 15.61%, 38.40 mA and 21.02% respectively. The results demonstrate that the light-trapping strategies suc- sc cessfully enhance the efficiency of the thin TOPCon solar cells. cm

**Keywords** Silicon · Thin solar cells · TOPCon · SunSolve

## 1 Introduction

The International Technology Roadmap for Photovoltaics (ITRPV) reported that n-type silicon (Si) solar cells domi- nated the photovoltaic (PV) market in 2024, and their market share is expected to increase over the next decade [1]. For high-efficiency Si solar cells, the tunnel oxide passivated contact (TOPCon) cells gained a high reputation due to its high efficiency over the past few years with the standard 160 μm thickness of Si wafer [2]. TOPCon dominates the industry due to its capability to withstand high-temperature processes, compared to passivated emitter and rear cells (PERC) and heterojunction with intrinsic thin layers (HIT) counterparts [1, 3–6]. TOPCon, which includes ultra-thin

* Mohd Zamir Pakhuruddin zamir@usm.my 1 Photovoltaic Materials and Devices, School of Physics, Universiti Sains Malaysia, 11800 Penang, Malaysia Institute of Nano Optoelectronics Research and Technology (INOR), Universiti Sains Malaysia, 11800 USM Penang, Malaysia
(< 2 nm) tunnel oxide (SiO₂) and phosphorus-doped poly- crystalline-Si (poly-Si), increases the open-circuit voltage (Voc), enhances passivation and electrical conductivity, hence increasing efficiency (η) [7]. The tunnel oxide also reduces the recombination current in the rear metal contact (J₀< 5 fA −2 ) and suppresses contact resistivity (ρc< 10 mΩ cm²) [cm 5]. The primary advantages of thin TOPCon cells share their cost-effectiveness and environmental friendliness, resulting from reduced material consumption. However, thin TOPCon cells suffer from poor light absorptance due to the thinner absorber layer, resulting in lower device efficiency. Light trapping strategies such as front surface texturing, anti- reflective coating (ARC) and rear surface texturing/rear reflector compensate for the efficiency loss due to the thin- ner Si absorber layer and poor light absorptance, making the efficiency of the thin TOPCon cells (< 150 μm) to be com- parable with the conventional wafer thickness [8, 9]. Light coupling is vital for increasing absorptance and efficiency in the thin TOPCon cells by introducing micron- or sub- micron-scale structures on the device's surface, which was first inspired by the moth eye (protrusion array) to enhance

sensitivity [10–12]. Since Si has appropriate hardness and reacts to chemical solutions (acid and alkaline), almost all kinds of manufacturing technologies can be used to fabricate surface texturing, including wet etching, dry etching, nano- imprinting and laser interference lithography [13–15]. The most famous geometrical shape used for surface texturing in industry is the upright pyramids, and it is not limited to other structures such as cylinders, cones, inverted pyramids, hem- ispheres, and three other advanced geometries, including mosaics, roses, and zigzags [16]. Apart from surface textur- ing, refractive index mismatch between the Si substrate and air can be mitigated by introducing an ARC [10]. Using the √ refractive index (n) matching, *n₁* = *n₀ns*, of air (n = 1.0) and Si (n = 3.94), quarter-wavelength theory, *nd* = *𝜆* 4 where *d* is thickness, the best ARC material for Si solar cells is sili- con nitride (SiNx) (n = 1.99) with 75 nm thickness. However, this method only reduces the reflectance within a narrow and selective wavelength. To achieve lower average reflec- tance (Ravg) across the 300–1200 nm spectrum, double layer anti-reflective coating (DLARC) is a superior method due to further reduction of abrupt changes in the refractive index to the Si substrate, which introduces more control points for interference and allows more complex destructive interfer- ence patterns that flatten the reflectance curve within the 300–1200 nm wavelength region [17]. Ultimately, in addi- tion to using surface texturing to refract light at the front surface, the geometrical optics method also reflects light into the device from the rear of the cells. The rear reflector forms a specific angle with the front surface of the device, which reflects light to the front surface, thereby increasing the opti- cal path length and enhancing photocurrent generation. This occurs when the incident angle exceeds the critical angle, resulting in total internal reflectance in the device [10]. The International Technology Roadmap for Photovoltaics (ITRPV) predicts that the wafer thickness of TOPCon cells will be reduced towards 110 μm by 2035, resulting in reduced material consumption and costs [1, 10, 18–21]. To date, the thinnest TOPCon cells recorded is 120 μm Si with an effi- ciency of 24%, using an M10 (182 mm) wafer, as reported by the Fraunhofer Institute for Solar Energy Systems (Fraunhofer ISE) in 2024 [22]. In 2025, Wang et al. fabricated 130 μm TOPCon cells that utilised laser-enhanced contact optimisa- tion (LECO) to reduce contact resistance (Rc) between the front metallisation and Si wafer, with efficiency of 25.7% [23]. Another work on 130 μm Si wafer (M10) by Wang et al. utilised Jollywood’s Special Injected Metallization (JSIM), a

||1|i|2|t|
|---|---|---|---|---|
|s||i||t|
||||i||
|s|1|i|2|t|

derivation of LECO, with an efficiency of 25.1% [24]. The highest recorded efficiency for TOPCon is 26.58% with large- area solar cells, surpassing those of PERC and HIT technolo- gies [10, 25–27]. The TOPCon solar cells employed n-type industrial TOPCon (i-TOPCon) configuration, typically

Silicon

featuring wafer thickness of around 140 μm [28]. However, there is no published work on the optical optimisation of thin TOPCon solar cells (with 100 μm thickness). The optimisation performed on the 100 μm-thin TOPCon cells in this work can be applied to current TOPCon technologies while advancing towards thinner wafers at an industrial scale, in line with the ITRPV trends. In this work, SunSolve simulation platform is used to inves- tigate the optical and electrical performance of 100 μm-thin TOPCon Si solar cells. Using SunSolve, the effects of upright pyramids heights for front surface texturing, DLARC with SiNx underlayer, and upright pyramids heights for rear surface texturing on the optical and electrical performance are inves- tigated within 300–1200 nm wavelength region. Optical per- formance, such as reflectance (R), absorptance (A), transmit- tance (T), and electrical performance such as external quantum efficiency (EQE),oc, short-circuit current densitysc), fill factor (FF) and η as well as current density–voltage (JV) are V (J simulated. The optimum settings for all the three light trap- ping strategies combined are compared to the standard planar 160 μm and 100 μm thin TOPCon without any light trapping strategies (i.e. as a reference). The optimisations conducted on the 100 μm-thick TOPCon cells in this study can be incor- porated into existing experimental TOPCon cells thinner than 150 μm to further enhance the efficiency.

## 2 Methodology

SunSolve is widely used among researchers and manufacturers within the PV community. The software extracts the optical and electrical performance of semiconductor materials and PV technologies. SunSolve solves optical simulations using Monte Carlo ray tracing for features comparable and larger than the wavelength of the incident light, such as surface texturing (1–10 μm). Individual light rays are traced from the front sur- face, refracted and reflected off textured surfaces (front and rear), and absorbed through different layers with decreasing intensities. The thin-film optics (Transfer Matrix Method) solves thin layers, such as ARC, silicon dioxide (SiO₂) passi- vation layers and poly-Si films, where wave interference effects dominate. It accurately calculates reflectance, transmittance and absorptance for planar multi-layer stacks. Both methods work simultaneously and solve the Fresnel equations (Eqs. 1, 2, 3 and 4) and the Beer-Lambert Law (5) as given below.

<u>n cos𝜃 − n cos𝜃</u> *r* = (1) *n₁*cos*𝜃* + *n₂*cos*𝜃*

*t* = <u>2n₁cos𝜃</u> *n* cos*𝜃* + *n* cos*𝜃*

(2)

Silicon

|n₂cos𝜃|− n₁cos𝜃|||
|---|---|---|---|
|p|i i|t t||
||i|||
|p|i −𝛼x|t|2 3|
||||x|

*r* = (3) *n₂*cos*𝜃* + *n₁*cos*𝜃*

<u>2n₁cos𝜃</u> *t* = (4) *n₂*cos*𝜃* + *n₁*cos*𝜃*

*I*(*x*) = *I*(0)*e* (5)

The derivation yields equations for the amplitude reflec- tance coefficient (r) and amplitude transmittance coefficient

(t) for both s-polarisation and p-polarisation, where1 and n₂ are the refractive indices of medium 1 and medium 2, n respectively, θi is the angle of incidence, and θt is the angle of transmittance. Beer-Lambert Law describes exponential decrease in light intensity with depth, where I(x) is the light intensity at depth x, I(0) is the light intensity at x = 0, ɑ is the absorption coefficient and x is the depth or optical path length. As for electrical simulation, SunSolve integrates with other tools, such as PC1D, which solves the drift–diffusion equations (Eqs. 6 and 7) for charge carriers and Poisson’s equation (Eq. 8) below, to calculate the internal electric field. It is also integrated with Quokka for modelling current flow and recombination in complex geometry, and Griddler, which focuses on electrical losses due to the metal grid. SunSolve also solves the current continuity equations (Eqs. 9 and 10) as shown below. <u>𝜕Ec 𝜕n</u> *J* *n*= *q𝜇cn* + *qDn*(6) *𝜕x 𝜕x* <u>𝜕Ev𝜕p</u>

|J = q𝜇|p − qD|SiN /Al₂O₃/c-Si/SiO₂/poly-Si/SiN||stack||
|---|---|---|---|---|---|
|p c||x||x||
||||||x|
|r||||||
||||2 x|||
|n p|n|x|x x y x|x||
||p|||||
 *p c p*(7) *𝜕x 𝜕x* *d* <u>𝜕y</u> *𝜀₀𝜀* = = *q*(*n* − *p*) (8) *dx 𝜕x* [] <u>𝜕J 𝜕p</u> = *q R* − *G* + (9) *𝜕x 𝜕x* [] <u>𝜕J 𝜕p</u> =−*q R* − *G* + (10) *𝜕x 𝜕x* The electrostatic potential approximation, Poisson's equation, and the Shockley–Read–Hall (SRH) formalism are collectively employed in the model to simulate electro- static behaviour, carrier recombination, and trap-assisted processes, enabling a detailed representation of trap state distributions and accurate device-level modelling [29]. In this work, SunSolve platform is used to simulate thin TOPCon cells with monocrystalline silicon (c-Si) wafer thickness of 100 μm and a cell areac) of 441. For the
(A cm

simulation, the spectrum is set to sunlight of air mass 1.5G (AM1.5G) with 100 mW cm −2 illumination, and the operat- ing temperature is set at 25 ˚C [29]. The incident angle is set to 0˚, and the location is set to “Full area”. The device struc- ture for TOPCon fixed parameters is extracted from Chen et al. and remains constant across the whole research [30]. The thickness of aluminium oxide (AlO ) passivation layer, + tunnel oxide, N poly-Si and SiN dielectric layer is set to 8 nm, 1.5 nm, 100 nm and 90 nm, respectively [30]. The fixed layer thicknesses of the TOPCon cells are adopted and optimised following the methodology and results reported by Chen et al. The scattering parameters for the thin film and c-Si are set to fixed values with a fraction of 1, using the Lambertian distribution. The parameter at the optical interfaces of the electrodes is maintained with fixed scat- tering, incorporating optical shading fraction of 0.8 [31]. The simulation resolved the absorptance in each thin film layer, explicitly accounting for parasitic losses. Figure 1 (a) shows the configuration for a textured (front and rear) thin TOPCon solar cell with DLARC, while Fig. 1 (b) shows the configuration for a standard planar thin TOPCon solar cell with single-layer anti-reflective coatings (SLARC). Regarding the electrical fixed parameters in the electrode and circuit tab within SunSolve, the contact layout for both the front and rear is set to “Grid”. The fingers and busbars parameters are set as in Table 1, and the series resistance and solar cells circuit are set as in Table 2. Figure 2 shows the flow chart outlining the research process used to optimise the thin TOPCon cells in this work. For the first experiment, the front surface texturing geometry used is random upright pyramids (54.74˚) with heights of 1 μm, 3 μm and 5 μm. The simulated TOPCon cells comprise ax x from front to rear. The structure includes a 75 nm SiN ARC, a front silver (Ag) contact, and a rear aluminium (Al) contact. With the best results from the first experi- ment, top layer DLARC thicknesses of 20 nm, 40 nm and 60 nm are used, which are SiO /SiN DLARC, silicon oxynitride 40% nitrogen (N)/SiN (SiO N /SiN DLARC) and Al₂O₃/SiN DLARC, with the SiN underlayer set to 60 nm. The n and extinction coefficient (k) for all materi- als are sourced from the PV Lighthouse library. Table 3 provides the corresponding references for each material employed in the thin TOPCon cells simulated in this study. Finally, with the best DLARC, rear surface texturing of upright pyramids (54.74˚) with heights of 1 μm, 3 μm and 5 μm is incorporated to the device. R curves, A curves, T curves, EQE curves, Voc, Jsc, FF, and JV curves are simu- lated in the wavelength range of 300–1200 nm. With the R curves and JV characteristics, the Ravg and η are calculated respectively. All data points are simulated using 100,000 rays per simulation run, with results averaged to yield a representative value. The numerical precision is governed

Silicon

**Fig. 1** Configuration of (**a**)

textured (front and rear) thin TOPCon solar cell with DLARC and (**b**) standard planar thin TOPCon solar cell with SLARC

by the number of rays used in the simulation, where higher the front and rear surfaces to emulate the surface mor- numbers of rays leads to higher numerical precision (i.e. phology achieved in large-scale manufacturing via wet lower noise). Random texturing is implemented on both

Silicon

**Table 1** Parameters for fingers and busbars set in this simulation

|Parameters|Fingers|Busbars|
|---|---|---|
||Front|Rear Front Rear|
|Number|128|168 12 12|
|Cross section|Rounded rectan- gular|Rounded Rectangular Rectangular rectan- gular|
|Height (μm)|15|15 15 15|
|Width (μm)|35|35 150 150|
|Finger pitch (cm)|0.1641|0.1250 NA NA|
|Finger spacing (cm)|0.1606|0.1215 NA NA|
|Pads|NA|NA 9 9|
|Pads length (μm)|NA|NA 1 1|
|Pad width (μm)|NA|NA 150 150|

**Table 2** Series resistance and solar cells circuit parameters set in this

simulation

|Parameters|Constant|
|---|---|
|(Ω cm²) Calculated series resistance, R sc 2 (Ω cm) Additional series resistance, R sa (Ω cm²) Total series resistance, R s −1) Front skin sheet resistance (Ω sq −1) Rear skin sheet resistance (Ω sq Base resistance, 100 μm (Ω cm) Front electrode resistivity (Ω cm) Rear electrode resistivity (Ω cm) −2 Light-collected current, J (mA cm) L −2 (pA cm) Saturation current, J 01 (Ω cm²) Ideality factor 1, m 1 2 Shunt resistance (kΩ cm)|0.6932 0.3350 1.0282 110 40 2 –6 6.0 × 10 –6 2.6 × 10 38.40 0.08 1 20|

chemical texturing, consistent with the crystallographic orientation of the Si wafer.

## 3 Results and Discussion

Figure 3 (a), (b) and (c) show the R, A and T results for front surface texturing using the upright pyramids geometry with different heights of 1 μm, 3 μm and 5 μm. For the first parameter, thex thickness used is 75 nm, based on the quarter-wavelength theory at a wavelength of 600 nm [ SiN 38]. Middle wavelengths are considered for the first parameter, as the visible light spectrum ranges from 400–800 nm. From Fig. 3 (a), at 600 nm wavelength, the lowest reflectance is achieved by 3 μm upright pyramids with an R value of

4.55%, followed by 1 μm and 5 μm with R values of 5.29% and 5.36%, respectively. As for Ravg on the wavelength
range of 300–1200 nm, 5 μm exhibits the lowest value of

18.69%. However, the difference in average reflectance from other heights is marginal. Compared to the planar front sur- face, the upright pyramids successfully reduce the R in the shorter wavelengths region (< 600 nm), specifically in the blue, green, and ultraviolet (UV) regions. This is because the shorter wavelengths have a very high ɑ value, as mentioned in the Beer-Lambert Law, where the light intensity drops rapidly with depth into the absorber layer [39, 40]. Hence, the upright pyramids front surface texturing is very impor- tant, especially in coupling shorter wavelengths light into the TOPCon cells to be absorbed by the c-Si on the first few hundred nanometres (surface) as shown in Fig. 3 (b), instead of being reflected away. The average absorptance (Aavg) is directly proportional to the upright pyramids’ heights. As shown in Fig. 3 (c), the transmittance spikes in the longer wavelengths region. This is because c-Si has a bandgap of
1.12 eV at room temperature, which means only photons with energies greater than or equal to the c-Si bandgap will be absorbed [41]. This corresponds to wavelengths shorter than 1100 nm, and longer wavelengths will have insuffi- cient energy to excite an electron across the bandgap, hence the higher transmittance [9, 42]. The difference in average transmittance (Tavg) for all the upright pyramids heights and planar front surfaces is very marginal, making surface tex- turing and ARC insignificant in reducing transmittance in the longer wavelengths region [43]. Figure 4 depicts the JV characteristics and Fig. 5 illus- trates the EQE for front surface texturing using the upright pyramids geometry with heights of 1 μm, 3 μm and 5 μm respectively. From the reflectance curves, Jsc and EQE can be related to reflectance using the integral of the spectral generation rate and EQE equation, as shown in Eqs. 11 and 12 below. *𝜆₂* *J* *sc*= *q EQE*(*𝜆*) ⋅ *𝜙photon*(*𝜆*)*d𝜆* (11) ∫ *𝜆* 1 *EQE*(*𝜆*)=(1 − *R*(*𝜆*) − *Tparasitic*(*𝜆*))×*IQE*(*𝜆*) (12) where q is the elementary charge (coulomb), ɸphoton is the incident photon flux of the solar spectrum, Tparasitic(λ) is the transmittance through non-active layers or unabsorbed light through the active layer and IQE is the internal quantum efficiency. Higher reflectance results in lower EQE, assum- ing another factor is held constant, which also leads to lower J sc. From the equation above,sc is directly proportional to the number of absorbed photons. With 5 μm upright pyra J- mids, which demonstrates the lowest Ravg, the Jsc value is the highest (37.69 mA
−2 ) with the highest value of η (20.64%) when compared to 1 μm and 3 μm. Compar cm- ing the EQE to the absorptance results, the EQE is lower in the blue/UV and infrared (IR) regions. In the blue/UV

Silicon

**Fig. 2** Flow chart on optimisation of thin TOPCon cells

**Table 3** Corresponding references for materials in the thin TOPCon

cells

|Material|Reference|
|---|---|
|Ag SiO₂ N SiO x y O₃ Al₂ SiN x O₃ (passivation) Al₂ c-Si Poly-Si Al|Jia16 [32] Pal85e [33] SOPRA Kim97 [34] Dut12 [35] Kum09 [36] Gree22 [37] Gre22 [37] Pal85b [33]|

region, photons are absorbed close to the surface, making the response sensitive to front-surface recombination and parasitic absorptance. Poor surface passivation and signifi- cant parasitic absorptance reduce the EQE in the blue/UV region despite higher absorptance [2, 30]. In the IR region, photons penetrate deeply into the wafer and depend on long minority-carrier diffusion lengths and efficient rear-side collection [23, 44]. However, limited bulk lifetime, insuf- ficient rear collection, or parasitic absorptance in the rear poly-Si and contact reduce the carrier collection probability and, consequently, the EQE at long wavelengths [23, 44]. Front surface texturing with 5 μm upright pyramids, when compared to lower heights, is more effective in reducing reflectance for shorter wavelengths. This is due to enhanced light absorptance since the 5 μm upright pyramids are much

larger than the wavelengths of the incident light [45]. This is explained by geometrical optics, where multiple reflectance occurs when the incident lights strike the pyramid facets and undergo several internal reflectance before eventually being coupled into the TOPCon cells and for increased absorptance [46]. A decrease in upright pyramids heights (same order of magnitude as the wavelength of the incident light) results in light behaving like a wave, where diffrac- tion effects become more dominant and increase the reflec- tance [46]. Experimentally, it is feasible to fabricate upright pyramids of approximately 5 μm in height on 100 μm-thin TOPCon cells. Terheiden et al. demonstrated 100 μm Si solar cells (including ∼5 μm pyramids), achieving an effi- ciency of 20% [47]. Apart from that, Woo et al. successfully incorporated pyramid textures ranging from 3 to 10 μm on 50 μm-thick wafers [48]. Figure 6 (a), (b), (c) show the R, A and T results for SiO2/ SiNx, SiOxNy/SiNx and Al2O₃/SiNx DLARC replacing the 75 nm SiNx ARC, with 5 μm upright pyramids (from first parameter). The thickness used for SiNx is reduced to 60 nm, as quarter-wavelength theory does not apply in DLARC, since the primary purpose is to minimise reflectance in the broadband range, rather than at a single wavelength. From Fig. 6 (a), all three DLARC reflectance curves with a 20 nm top layer are too thin to have an effect as optimised DLARC [49]. The reflectance is significantly higher than that of the SLARC in both the short wavelengths range (< 325 nm) and the longer wavelengths range (> 600 nm) until the IR range. The 40 nm thick top layer exhibits a mid-effect, and a 60 nm thick layer yields the most promising results in

Silicon

reducing reflectance, with Ravg values of 16.18% (SiO₂/ SiNx), 15.99% (SiOxNy/SiNx), and 15.58% (Al₂O₃/SiNx). This also indicates that a less abrupt change in the refrac- tive index of a thin film yields better DLARC materials. From the SunSolve library, the refractive index for the thin films at 600 nm is 1.46 for SiO2 and 1.62 for SiOxNy and Al₂O₃ [33, 34]. As for the absorptance shown in Fig. 6 (b), the average performance for a 20 nm thick top layer is the lowest among the other thicknesses. The absorptance of SiOxNy/SiNx and Al2O₃/SiNx at 40 nm and 60 nm is slightly lower than the SLARC in the mid-visible light spectrum, but then increases at longer wavelengths until the IR range. Meanwhile, for SiO2/SiNx, the absorptance is slightly higher compared to the other two DLARC in the mid-visible light spectrum, but barely higher than the SLARC at the longer wavelengths region, especially for 40 nm thickness. All three DLARCs with a 60 nm top layer depict an improvement in absorptance from 650 to 1050 nm, where the difference is marginal between each other. As for Tavg shown in Fig. 6 (c), the behaviour is the same as that of the previous parameter, which is 0% on most shorter wavelengths and increases in the near-infrared (NIR) and IR regions. The thickness of the top layer thin films for2/SiNx, SiOxNy/SiNx, and2O₃/ SiNx is inversely proportional to the SiO Ravg and directly pro Al- portional to the Aavg [50]. So far, the TOPCon cells with 5 μm upright pyramids and Al₂O₃/SiNx (60 nm/60 nm) DLARC demonstrates the best optical performance. Figure  7 illustrates the JV characteristics and Fig.  8 shows the EQE for2/SiNx, SiOxNy/SiNx and2O₃/SiNx DLARC with 20 nm, 40 nm and 60 nm top layer thicknesses. SiO Al For 20 nm, the J

|and η,|SiO₂/SiN|is slightly underper-||
|---|---|---|---|
|sc||x||
|x y|x|||
|x|sc|||

formed, while SiON /SiN is on par with the SLARC. As for 20 nm Al₂O₃/SiN, the J and η perform better, but only with a slight improvement. Given the optical performance of a 20 nm thickness for the top layer, it is insufficient to compensate for the reduced efficiency of the thin TOPCon cells. The Jsc for all three DLARC reached a peak value at a 60 nm top layer thickness, with the2/SiNx DLARC (60 nm/60 nm) outperforming the other two DLARCs. SiO Although the SiO₂/SiNx DLARC exhibits higher reflectance and lower absorptance (by a small margin), η is the high- est, with a value of 21.00%, due to its significantly higher J sc value. The EQE curve exhibits behaviour similar to that observed in the previous experiment, showing lower values in the blue/UV and near-IR regions when compared with the absorptance curve. However, the 60 nm/60 nm DLARC for all material combinations are able to trap light more effec- tively, as indicated by the higher EQE values compared with the SLARC. Table 4 below presents the JV characteristics and Ravg for SiO₂/SiNx, SiOx y x and Alx

||N /SiN|O₃/SiN|DLARC with|
|---|---|---|---|
||x y|2|x|
|Fig. 3 (a) Reflectance (b) absorptance and (c) transmittance for upright pyramids front surface texturing with 1 μm, 3 μm, and 5 μm heights||x|oc|

60 nm thickness on top of 60 nm SiN. The V value is the same, while FF only shows a slight difference between the

Silicon

**Fig. 4** JV characteristics for

upright pyramids front surface texturing with 1 μm, 3 μm, and 5 μm heights

**Fig. 5** EQE for upright

pyramids front surface textur- ing with 1 μm, 3 μm and 5 μm heights

Silicon

**Fig. 6** (**a**) Reflectance (**b**) absorptance and (**c**) transmittance for DLARC (SiO2/SiNx, SiOxNy/SiNx and Al2O₃/SiNx), with the top layer thick-

nesses of 20 nm, 40 nm and 60 nm, and the bottom layer thickness of 60 nm

three DLARC. The EQE for a 60 nm top layer thickness, region. Meanwhile, for SiOxNy/SiNx and Al₂O₃/SiNx, the in the shorter wavelength range, indicates that SiO₂/SiNxpeak is higher, then decreases to a level lower than SLARC has a smaller peak in the region below 400 nm but consist-at around the 425 nm region. Although the TOPCon cells ently remains higher than SLARC until around the 475 nm with 5 μm upright pyramids and Al₂O₃/SiNx (60 nm/60 nm)

Silicon

(SiO₂/SiNx x y x x), with the top layer thicknesses of 20 nm, 40 nm and 60 nm, and

|Fig. 8 EQE for DLARC|/SiN, SiO|N /SiN and|O₃/SiN|
|---|---|---|---|
|layer thickness of 60 nm (SiO|||Al|

|Fig. 7 JV characteristics for DLARC|, SiO N /SiN|and Al₂O₃/SiN|
|---|---|---|
|the bottom layer thickness of 60 nm|||

2 x x y x 2 x), with the top layer thicknesses of 20 nm, 40 nm and 60 nm, and the bottom

avgSiO₂/SiNxintroduces additional negative fixed charges and impede

|Table 4 JV characteristics and R||for DLARC for|,|
|---|---|---|---|
|SiO N /SiN SiN|and Al₂O₃/SiN|with 60 nm thickness on top of 60 nm||
||||2 3|

x y x x the hydrogen diffusion, leading to reduce passivation on the xAl O /c-Si interface [53, 54].

|Materials|η (%) J|(mA/cm²) SC|V (mV) OC|FF (%)|R avg (%)|
|---|---|---|---|---|---|
|SiN SLARC20.64 x SiO DLARC21.00 2 SiO N x y DLARC Al O DLARC 2 3|20.90 20.94|37.69 38.37 38.18 38.25|691 691 691 691|79.31 79.23 79.25 79.24|18.69 16.18 15.99 15.58|

Figure 9 (a), (b), (c) depict the R, A and T results for rear surface texturing using the upright pyramids geometry with different heights of 1 μm, 3 μm and 5 μm. For the last parameter, the SiO2/SiNx (60 nm/60 nm) DLARC, with 5 μm upright pyramids, is used. Rear surface texturing is vital in reducing the reflectance in the longer wave- lengths region [43]. In Fig. 9 (a), the difference in reflec- tance reduction between the rear upright pyramids and the DLARC exhibit the best optical performance, the SiO₂/ rear planar is increasing towards the 1200 nm wavelength SiNx (60 nm/60 nm) DLARC demonstrates the best electri-region, with 5 μm having the lowest Ravg of 15.47%, fol- cal performance and is considered for the third parameter. lowed by 1 μm (15.61%) and 3 μm (15.85%). Figure 9 (b) This is believed to be due to enhanced chemical passivation shows that the absorptance curves at longer wavelengths (lower interface defect density (Dit)) and reduction in sur-(> 1100 nm) for all rear upright pyramids with different face recombination velocity (SRV) at the p + emitter surface heights are significantly higher compared to the planar [51, 52]. The reduction in Dit and SRV improves the Jsc of rear counterparts, but there is little difference among them. the SiO₂/SiNx DLARC. Meanwhile, Al O₃/SiNx DLARC Although 5 μm height has the lowest Ravg, 1 μm height

Silicon

outperforms in terms of Aavg by 0.01%. A similar case is observed in the transmittance curve in Fig. 9 (c), where 1 μm height has the least average transmittance (4.16%) due to light being reflected into the TOPCon cells from the rear, thereby increasing the light optical path length and allowing the absorber layer to absorb more light [44, 55]. In addition to the indirect bandgap and low absorption coefficient of Si, the thin Si layer in the TOPCon cells also weakly absorbs photons in the longer wavelengths region, allowing many photons to have a second pass through the device from the back [44]. Hence, rear surface textur- ing works by reflecting the light and increasing the light absorptance, especially in the longer wavelengths region, compared to previous parameters that focus on shorter wavelengths and broadband wavelengths [21, 44, 56]. Figure  10 shows the JV characteristics and Fig.  11 shows the EQE for rear surface texturing using the upright pyramids geometry with different heights of 1 μm, 3 μm and 5 μm. The highest Jsc and η are observed for the 1 μm −2 rear upright pyramids height, which are 38.40 mA and 21.02%, respectively. Then, the performance is fol cm- −2 lowed by 5 μm height, with a 0.01 mA and 0.01% marginal difference, and 3 μm as the least performing, cm −2 with 0.21 mA cm difference and 0.11% difference for η. Comparing the Ravg and η for both 1 μm and 5 μm rear upright pyramids, the 1 μm texture performs better despite having higher average reflectance than the 5 μm pyramids, due to improved passivation and lower recombination rate at the rear surface [57]. The 5 μm features possess a larger surface area with higher defect density at the tunnel oxide interface [58–63]. As for the EQE, the difference is also minimal, with the highest EQEavg being 76.41% by 1 μm rear upright pyramids height. Like other param- eters, the EQE curves are lower at shorter wavelengths and approach zero towards wavelength of 1200 nm due to the absorptance cut-off towards the bandgap of the c-Si. Figure  12 shows the performance comparison for 100 μm thin TOPCon cells with optimised light trapping strategies from all the parameters, with non-optimised 100 μm and 160 μm standard TOPCon cells. The per- formance of the thin TOPCon cells surpassed that of the conventional 160 μm TOPCon cells, despite the absorber layer being reduced by 60 μm. The highest recorded η is achieved by 100 μm optimised TOPCon cells, with

21.02% ± 0.06%, with the lowest recorded Ravg of 15.61%. Therefore, the absolute efficiency gain of 0.29% obtained in the optimised 100 μm TOPCon cells is a meaningful enhancement, especially when considering its potential impact in the context of mass production of the solar cells [64]. The results demonstrate that the light-trapping strat- egies work efficiently by reducing optical losses within
**Fig. 9** (**a**) Reflectance (**b**) absorptance and (**c**) transmittance results forbroadband wavelengths and by compensating for the effi-

rear surface texturing (upright pyramids) with 1  μm, 3  μm, and 5  μm ciency loss in the thin TOPCon solar cells [65]. heights

Silicon

**Fig. 10** JV characteristics for

rear surface texturing (upright pyramids) with 1 μm, 3 μm, and 5 μm heights

**Fig. 11** EQE for rear surface

texturing (upright pyramids) with 1 μm, 3 μm, and 5 μm heights

Silicon

**Fig. 12** Comparison of η and Ravg for 100 μm optimised light trapping strategies TOPCon cells with 100 μm non-optimised standard and 160 μm

non-optimised standard TOPCon cells

## 4 Conclusion

This work aims to determine the optimal light-trapping strat- egies settings for 100 μm-thin TOPCon cells. Firstly, the front surface texturing with 5 μm upright pyramids is chosen because it reduces the Ravg to 18.69% and increases the η to

20.64%, surpassing the results achieved with 1 μm and 3 μm heights. The front surface texturing mitigates the optical loss in the shorter wavelength region when compared to the pla- nar front surface. Then, with 5 μm upright pyramids on the front surface texturing, a SiO2/SiNx (60 nm/60 nm) DLARC is incorporated to the device due to its highest η value of
21.00% when compared toxNy/SiNx and2O₃/SiNx DLARCs. Although Al₂O₃/SiN SiOx (60 nm/60 nm) DLARC Al exhibits the lowest Ravg of 15.58%, SiO₂/SiNx (60 nm/60 nm) DLARC demonstrates higher Jsc of 38.37 mA
−2, hence the higher efficiency value. Introducing DLARC over cm SLARC reduces reflectance curves in the 300–1200 nm wavelength region for the thin TOPCon cells. The overall performance of the thin TOPCon cells is increased by a small amount with the introduction of rear surface texturing with 1 μm upright pyramids. The upright

pyramids, with a height of 1 μm, yield the highest η value of

21.02% when compared to other heights, due to the improve- ments in optical performance in the longer wavelengths region. It has been observed that rear surface structuring increases the absorptance in the NIR and IR regions and decreases the transmittance by reflecting the light into the device, thereby increasing the optical path length for the light to be absorbed again by the absorber layer. The opti- mised 100 μm-thin TOPCon cells is equipped with 5 μm upright pyramids on the front surface texturing, SiO2/SiNx (60 nm/60 nm) DLARC and 1 μm upright pyramids on the rear surface texturing, surpassing the performance of a 100 μm standard TOPCon cells and a standard conven- tional 160 μm TOPCon cells. The optimal light-trapping strategies developed in this work can be incorporated into the real 100 μm-thin TOPCon cells to enhance both optical and electrical performance. **Acknowledgements** Authors would like to acknowledge Ministry of Higher Education (MoHE) Malaysia for funding this research through Fundamental Research Grant Scheme (FRGS) with Project Code: FRGS/1/2024/STG07/USM/02/4. Besides, authors would like to thank Universiti Sains Malaysia (USM) for supporting this research.

**Author Contribution** The following items are the contributions of each author to the manuscript: Mohamad Fathul Bari Mohd Fuad: Con- ception, Data Curation, Investigation, Analysis, Writing Paper (Draft) Mohd Marzaini Mohd Rashid: Supervision Mohd Zamir Pakhuruddin: Conception, Resources, Analysis, Writing Paper (Validation), Supervi- sion, Corresponding Author.

**Funding** Open access funding provided by The Ministry of Higher Education Malaysia and Universiti Sains Malaysia. Authors would like to acknowledge Ministry of Higher Education (MoHE) Malaysia for funding this research through Fundamental Research Grant Scheme (FRGS) with Project Code: FRGS/1/2024/STG07/USM/02/4.

**Data Availability** Data will be made available by authors upon request.

### Declarations

**Competing Interests** The authors declare no competing interests.

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and repro- duction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://crea-](http://crea-) tivecommons.org/licenses/by-nc-nd/4.0/.

Silicon

transport characteristics. Sol Energy Mater Sol Cells 120:270–

274. [https://doi.org/10.1016/j.solmat.2013.09.017](https://doi.org/10.1016/j.solmat.2013.09.017)
8. Richter A, Hermle M, Glunz SW (2013) Reassessment of the lim- iting efficiency for crystalline silicon solar cells. IEEE J Photovolt 3:1184–1191. [https://doi.org/10.1109/JPHOTOV.2013.2270351](https://doi.org/10.1109/JPHOTOV.2013.2270351)
9. Battaglia C, Cuevas A, De Wolf S (2016) High-efficiency crystal- line silicon solar cells: status and perspectives. Energy Environ Sci 9:1552–1576. [https://doi.org/10.1039/C5EE03380B](https://doi.org/10.1039/C5EE03380B)
10. Liu H, Du Y, Yin X, Bai M, Liu W (2022) Micro/nanostructures for light trapping in monocrystalline silicon solar cells. J Nano- mater 2022:8139174. [https://doi.org/10.1155/2022/8139174](https://doi.org/10.1155/2022/8139174)
11. Parker AR, Hegedus Z, Watts RA (1998) Solar–absorber antire- flector on the eye of an Eocene fly (45 Ma). Proc R Soc Lond B Biol Sci 265:811–815. [https://doi.org/10.1098/rspb.1998.0364](https://doi.org/10.1098/rspb.1998.0364)
12. DeNatale JF, Hood PJ, Flintoff JF, Harker AB (1992) Fabrication and characterization of diamond moth eye antireflective surfaces on Ge. J Appl Phys 71:1388–1393. [https://doi.org/10.1063/1](https://doi.org/10.1063/1). 351259
13. Ray S, Mitra S, Ghosh H, Mondal A, Banerjee C, Gangopad- hyay U (2021) Novel technique for large area n-type black sili- con solar cell by formation of silicon nanograss after diffusion process. J Mater Sci Mater Electron 32:2590–2600. [https://doi](https://doi). org/10.1007/s10854-020-05027-6
14. Park JE, Han C-S, Choi WS, Lim D (2021) Effect of various wafer surface etching processes on c-Si solar cell characteris- tics. Energies (Basel) 14:4106. [https://doi.org/10.3390/en141](https://doi.org/10.3390/en141) 44106
15. Kim M, Min KH, Park S, Song H, Lee JI, Jeong KT, Park J, Kang MG (2020) Study on efficiency improvement of multi-crystalline silicon solar cell by removing by-product and plasma induced damage generated during reactive ion etching. Curr Appl Phys 20:519–524. [https://doi.org/10.1016/j.cap.2020.01.013](https://doi.org/10.1016/j.cap.2020.01.013)
16. Gjessing J, Sudbø AS, Marstein ES (2011) Comparison of peri- odic light-trapping structures in thin crystalline silicon solar cells. J Appl Phys 110:034501. [https://doi.org/10.1063/1.3611425](https://doi.org/10.1063/1.3611425)
17. Poitras D, Dobrowolski JA (2004) Toward perfect antireflection coatings 2 theory. Appl Opt 43:1286–1294. [https://doi.org/10](https://doi.org/10). 1364/AO.43.001286
18. Jeong S, McGehee MD, Cui Y (2013) All-back-contact ultra- thin silicon nanocone solar cells with 13.7% power conversion efficiency. Nat Commun 4:2950. [https://doi.org/10.1038/ncomm](https://doi.org/10.1038/ncomm) s3950
19. Yang Z, Li X, Wu S, Gao P, Ye J (2015) High-efficiency photon capturing in ultrathin silicon solar cells with front nanobowl tex- ture and truncated-nanopyramid reflector. Opt Lett 40:1077–1080. [https://doi.org/10.1364/OL.40.001077](https://doi.org/10.1364/OL.40.001077)
20. Sun T, Shi H, Cao L, Liu Y, Tu J, Lu M, Li H, Zhao W, Li Q, Fu T, Zhang F (2020) Double grating high efficiency nanostruc- tured silicon-based ultra-thin solar cells. Results Phys 19:103442. [https://doi.org/10.1016/j.rinp.2020.103442](https://doi.org/10.1016/j.rinp.2020.103442)
21. Li N, Fratalocchi A (2024) Innovative strategies for photons management on ultrathin silicon solar cells. Glob Challenges 8:2300306. [https://doi.org/10.1002/gch2.202300306](https://doi.org/10.1002/gch2.202300306)
22. Bellini E (2024) Fraunhofer ISE unveils M10 TOPCon solar cell with 24.0% efficiency. PV Magazine, May 29. [https://www.pv-](https://www.pv-) magazine.com/2024/05/29/fraunhofer-ise-unveils-m10-topcon- solar-cell-with-24-0-efficiency/
23. Wang Q, Guo K, Gu S, Wu W, Li L, Erişen DE, Yong G, Ding J (2025) Impact of laser-enhanced contact optimization on n-TOP- Con solar cells’ performance and efficiency: experimental and simulated insights. Sol Energy Mater Sol Cells 285:113526. [https://doi.org/10.1016/j.solmat.2025.113526](https://doi.org/10.1016/j.solmat.2025.113526)
24. Wang X, Yuan J, Wu X, Nie J, Zhang Y, Zhang X, Yang W, Li F, Hoex B (2025) Higher-efficiency TOPCon solar cells in mass production enabled by laser-assisted firing: advanced loss analysis
## References

1. International Technology Roadmap for Photovoltaic (ITRPV) (2025) ITRPV 2024 Result. Frankfurt, Germany
2. Richter A, Müller R, Benick J, Feldmann F, Steinhauser B, Reichel C, Fell A, Bivour M, Hermle M, Glunz SW (2021) Design rules for high-efficiency both-sides-contacted silicon solar cells with balanced charge carrier transport and recombination losses. Nat Energy 6:429–438. [https://doi](https://doi). org/ 10. 1038/ s41560-021-00805-w
3. Wang X, Sen C, Wu X, Chang Y-C, Wang H, Khan MU, Hoex B (2025) Alleviating contaminant-induced degradation of TOP- Con solar cells with copper plating. Sol Energy Mater Sol Cells 282:113444. [https://doi.org/10.1016/j.solmat.2025.113444](https://doi.org/10.1016/j.solmat.2025.113444)
4. Kafle B, Goraya BS, Mack S, Feldmann F, Nold S, Rentsch J (2021) TOPCon – technology options for cost efficient industrial manufacturing. Sol Energy Mater Sol Cells 227:111100. https:// doi.org/10.1016/j.solmat.2021.111100
5. Yan D, Cuevas A, Michel JI, Zhang C, Wan Y, Zhang X, Bullock J (2021) Polysilicon passivated junctions: the next technology for silicon solar cells? Joule 5:811–828. [https://doi.org/10.1016/j](https://doi.org/10.1016/j). joule.2021.02.013
6. Gu N, Ji X (2022) Research on optimization of annealing process based on N-type TOPCon solar cell. IOP Conf Ser Earth Environ Sci 983:012061. [https://doi](https://doi). org/ 10. 1088/ 1755-1315/ 983/1/ 012061
7. Feldmann F, Bivour M, Reichel C, Hermle M, Glunz SW (2014) Passivated rear contacts for high-efficiency n-type Si solar cells providing high interface passivation quality and excellent

Silicon

and near-term efficiency potential. Prog Photovolt Res Appl 33:771–781. [https://doi.org/10.1002/pip.3921](https://doi.org/10.1002/pip.3921)

25. Green MA, Dunlop ED, Yoshita M, Kopidakis N, Bothe K, Siefer G, Hao X, Jiang JY (2025) Solar cell efficiency tables (version
65). Prog Photovolt Res Appl 33:3–15. [https://doi.org/10.1002/](https://doi.org/10.1002/) pip.3867
26. Shaw V (2024) Trina Solar claims record-breaking efficiency of
26.58% for TOPCon solar cell. PV Magazine International, Nov. [https://www.pv-magazine.com/2024/11/21/trina-solar-claims-](https://www.pv-magazine.com/2024/11/21/trina-solar-claims-) record-breaking-efficiency-of-26-58-for-topcon-solar-cell/
27. EU/Trinasolar (2024) Announces efficiency of 26.58% for its n-type TOPCon cells, setting a new world record. Trina Solar. [https://static.trinasolar.com/eu-en/resources/newsroom/eu-trina](https://static.trinasolar.com/eu-en/resources/newsroom/eu-trina) solar-announces-efficiency-2658-its-n-type-topcon-cells-setti ng-new-world
28. Chen Y, Chen H, Zhang S, Wang L, Liu C, Chen D, Xu J, Alter- matt P, Feng Z, Verlinden P (2023) 690 WP N-Type i-TOPCon modules in mass production with >25% efficiency solar cells based on large-area 210 mm wafers. In: 2023 IEEE 50th Photo- voltaic Specialists Conference (PVSC), pp 1–1. [https://doi](https://doi). org/
10.1109/PVSC48320.2023.10359700
29. Mohd Fuad MFB, Rammely N, Pakhuruddin MZ (2024) Simula- tion of perovskite solar cell with transparent contacts for solar windows. Phys Scr 99:085562. [https://doi.org/10.1088/1402-](https://doi.org/10.1088/1402-) 4896/ad63d7
30. Chen W, Liu X, Liu W, Yu Y, Wang W, Wan Y (2023) Optimi- zation of activated phosphorus concentration in recrystallized polysilicon layers for the n-TOPCon solar cell application. Sol Energy Mater Sol Cells 252:112206. [https://doi.org/10.1016/j](https://doi.org/10.1016/j). solmat.2023.112206
31. Khan KM, Tahir S, Ahmad W, Almufarij RS, Shokralla EA, Alrefaee SH, Fahmy MA, Ragab I, Ashfaq A, Abd-Elwahed AR (2024) Optimization of electrical and optical losses in thin c-Si bifacial PERC solar cells to module level through modeling. SILICON 16:5649–5664. [https://doi.org/10.1007/](https://doi.org/10.1007/) s12633-024-03104-7
32. Jiang Y, Pillai S, Green MA (2016) Realistic silver optical con- stants for plasmonics. Sci Rep 6:30605. [https://doi](https://doi). org/ 10. 1038/ srep30605
33. Palik ED (1985) Handbook of Optical Constants of Solids, vol.
1. Elsevier. [https://doi.org/10.1016/C2009-0-20920-2](https://doi.org/10.1016/C2009-0-20920-2)
34. Kim Y, Lee SM, Park CS, Lee SI, Lee MY (1997) Substrate dependence on the optical properties of Al2O3 films grown by atomic layer deposition. Appl Phys Lett 71:3604–3606. https:// doi.org/10.1063/1.120454
35. Duttagupta S, Ma F, Hoex B, Mueller T, Aberle AG (2012) Optimised antireflection coatings using silicon nitride on tex- tured silicon surfaces based on measurements and multidimen- sional modelling. Energy Procedia 15:78–83. [https://doi](https://doi). org/ 10. 1016/j.egypro.2012.02.009
36. Kumar P, Wiedmann MK, Winter CH, Avrutsky I (2009) Optical properties of Al2O3 thin films grown by atomic layer deposition. Appl Opt 48:5407–5414. [https://doi](https://doi). org/ 10. 1364/ AO. 48. 005407
37. Green MA (2022) Improved silicon optical parameters at 25°C, 295 K and 300 K including temperature coefficients. Prog Photo- volt Res Appl 30:164–179. [https://doi.org/10.1002/pip.3474](https://doi.org/10.1002/pip.3474)
38. Ji C, Liu W, Bao Y, Chen X, Yang G, Wei B, Yang F, Wang X (2022) Recent applications of antireflection coatings in solar cells. Photonics 9:906. [https://doi.org/10.3390/photonics9120906](https://doi.org/10.3390/photonics9120906)
2 absorption limit – application to IBC solar cells. Small

41. Al-Ezzi AS, Ansari MNM (2022) Photovoltaic solar cells: a 19:2302250. [https://doi.org/10.1002/smll.202302250](https://doi.org/10.1002/smll.202302250) review. Applied System Innovation 5:67. [https://doi](https://doi). org/ 10. 3390/
46. asi50 Baker-Finch SC, McIntosh KR (2011) Reflection of normally inci 40067- dent light from silicon solar cells with pyramidal texture. Prog
42. Dong X, Qiao R, Wang T, An Y, Wang Y (2022) Engineering a Photovolt Res Appl 19:406–416. [https://doi](https://doi). org/ 10. 1002/ pip. 1050 bandgap-regulable intermediate-band material based on diamond.
47. Carbon N Y 191:106–111. Terheiden B, Ballmann T, Horbelt R, Schiele Y, Seren S, Ebser J, [https://doi](https://doi). org/ 10. 1016/j. carbon. 2022.
01. Hahn G, Mertens V, Koentopp MB, Scherff M, Müller JW, Holman 048 ZC, Descoeudres A, De Wolf S, de Nicolas SM, Geissbuehler J, Ballif
43. Sai H, Jia H, Kondo M (2010) Impact of front and rear texture of C, Oswald W (2015) Manufacturing 100-µm-thick silicon solar cells thin-film microcrystalline silicon solar cells on their light trapping with efficiencies greater than 20% in a pilot production line. Phys properties. J Appl Phys 108:043105. Status Solidi A 212:13–24. [https://doi.org/](https://doi.org/)
https://

10.1002/ doi.pssa. org/20143 10.1063/1.
1241 3467968

48. Woo J-H, Kim Y-C, Kim S-H, Jang J, Han HN, Choi KJ, Kim
44. Saive R (2021) Light trapping in thin silicon solar cells: a review I, Kim J-Y (2017) Critical bending radius of thin single-crystal- on fundamentals and technologies. Prog Photovolt Res Appl line silicon with dome and pyramid surface texturing. Scr Mater 29:1125–1137. 140:1–4. [https://https://](https://https://) doi.org/
doi.

10.org/ 1016/j.
10.1002/ scrippip. tamat. 3440
2017.06.047
45.
49. Garín M, Pasanen TP, López G, Vähänissi V, Chen K, Martín I, Wei YS, Xu SH, Yuan LG, Wang B, Liu SL, Fei GT (2020) Savin H (2023) Black ultra-thin crystalline silicon wafers reach Double-layer anti-reflection coating of SiO2–TiO2/SiO2–TiO2- the PEG300 with high transmittance and super-hydrophilicity. Mater 4n Res Express 7:096402. [https://doi](https://doi). org/ 10. 1088/ 2053-1591/ abb499
50. Hamdan NAN, Yusof N, Yusoff MZM (2023) Ray tracer simula- tion of si-based solar cells using Al2O3/ITO as double layers anti reflective coating. Trends Sci 20:5881. [https://doi.org/10.48048/](https://doi.org/10.48048/) tis.2023.5881
51. Gatz S, Hannebauer H, Hesse R, Werner F, Schmidt A, Dullweber T, Schmidt J, Bothe K, Brendel R (2011) 19.4%-efficient large- area fully screen-printed silicon solar cells. Phys Status Solidi RRL 5:147–149. [https://doi.org/10.1002/pssr.201105045](https://doi.org/10.1002/pssr.201105045)
52. Terlinden NM, Dingemans G, Vandalon V, Bosch RHEC, Kessels WMM (2014) Influence of the SiO2 interlayer thickness on the density and polarity of charges in Si/SiO2/Al2O3 stacks as studied by optical second-harmonic generation. J Appl Phys 115:034103. [https://doi.org/10.1063/1.4857075](https://doi.org/10.1063/1.4857075)
53. Richter A, Benick J, Hermle M, Henneck S, Hörteis M, Glunz SW (2010) Firing stable Al2O3/SiNx layer stack passivation for the front side boron emitter of n-type Si solar cells. [https://www](https://www). researchgate.net/publication/234125543
54. Helmich L, Walter DC, Bredemeier D, Schmidt J (2020) Atomic- layer-deposited Al2O3 as effective barrier against the diffusion of hydrogen from SiNx:H layers into crystalline silicon during rapid thermal annealing. Phys Status Solidi RRL 14:2000367. https:// doi.org/10.1002/pssr.202000367
55. Guan L, Shen G, Liang Y, Tan F, Xu X, Tan X, Li X (2019) Double-sided pyramid texturing design to reduce the light escape of ultrathin crystalline silicon solar cells. Opt Laser Technol 120:105700. [https://doi.org/10.1016/j.optlastec.2019.105700](https://doi.org/10.1016/j.optlastec.2019.105700)
56. Moys BA (1974) The theory of double-layer antireflection coat- ings. Thin Solid Films 21:145–157. [https://doi](https://doi). org/ 10. 1016/ 0040-

Silicon

silicon surface morphology and its effect on poly-Si/SiOx contact passivation for silicon solar cells. IEEE J Photovolt 9:1513–1521. [https://doi.org/10.1109/JPHOTOV.2019.2937230](https://doi.org/10.1109/JPHOTOV.2019.2937230)

58. Kato Y, Takao H, Sawada K, Ishida M (2006) Improvement of metal-oxide semiconductor interface characteristics in comple- mentary metal-oxide semiconductor on Si(111) by combination of fluorine implantation and long-time hydrogen annealing. Jpn J Appl Phys 45:L108. [https://doi.org/10.1143/JJAP.45.L108](https://doi.org/10.1143/JJAP.45.L108)
59. Razouk RR, Deal BE (1979) Dependence of interface state density on silicon thermal oxidation process variables. J Electrochem Soc 126:1573–1581. [https://doi.org/10.1149/1.2129333](https://doi.org/10.1149/1.2129333)
60. Larionova Y, Turcu M, Reiter S, Brendel R, Tetzlaff D, Krügener J, Wietler T, Höhne U, Kähler J-D, Peibst R (2017) On the recombina- tion behavior of p+-type polysilicon on oxide junctions deposited by different methods on textured and planar surfaces. Phys Status Solidi A 214:1700058. [https://doi.org/10.1002/pssa.201700058](https://doi.org/10.1002/pssa.201700058)
61. Baker-Finch SC, McIntosh KR (2011) The contribution of planes, vertices, and edges to recombination at pyramidally textured sur- faces. IEEE J Photovolt 1:59–65. [https://doi.org/10.1109/JPHOT](https://doi.org/10.1109/JPHOT) OV.2011.2165530
62. McIntosh KR, Johnson LP (2009) Recombination at textured silicon surfaces passivated with silicon dioxide. J Appl Phys 105:123711. [https://doi.org/10.1063/1.3153979](https://doi.org/10.1063/1.3153979)
63. Cousins PJ, Cotter JE (2006) Minimizing lifetime degradation associated with thermal oxidation of upright randomly textured silicon surfaces. Sol Energy Mater Sol Cells 90:228–240. https:// doi.org/10.1016/j.solmat.2005.03.008
64. Jolywood (2025) Jolywood’s laser-assisted firing process increases TOPCon solar cell efficiency by 0.6%, says UNSW research. PV Magazine International. [https://www.pv-magazine.com/2025/](https://www.pv-magazine.com/2025/) 05/02/jolywoods-laser-assisted-firing-process-increases-topcon- solar-cell-efficiency-by-0-6-says-unsw-research/
65. Nasser H, Borra MZ, Çiftpınar EH, Eldeeb B, Turan R (2022) Fourteen percent efficiency ultrathin silicon solar cells with improved infrared light management enabled by hole-selective transition metal oxide full-area rear passivating contacts. Prog Photovolt Res Appl 30:823–834. [https://doi](https://doi). org/ 10. 1002/ pip. 3510 **Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
