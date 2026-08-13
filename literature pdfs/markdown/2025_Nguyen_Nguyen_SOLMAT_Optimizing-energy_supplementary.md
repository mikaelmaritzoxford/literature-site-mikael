Supplementary

# Optimizing Energy Yield of Monolithic Perovskite/Silicon

# Tandem Solar Cells in Real-World Conditions: The Impact of

# Luminescent Coupling

|1|2,3|
|---|---|
|1|1|

*Khoa Nguyen¹*, Marco Ernst, Abhnil Amtesh Prasad, Thien Truong,* *4* *Ziv Hameiri,* *2* *Heping Shen,* *1* *Klaus Weber, Kylie Catchpole, Daniel Macdonald¹* and Hieu T. Nguyen¹*

**Figure S1:** (a) Comparison of direct and diffuse irradiance averaged over a year for two locations: Daggett (dark) and Denver (blue). (b) Differences between these irradiance spectra and the AM 1.5G spectrum (red) in normalized scales.

**Figure S2:** (a) The contour plot showing the difference in EY at different thicknesses of the top subcell (300 to 800 nm) and bottom subcell (100 to 450 µm) in a monolithic perovskite/silicon tandem structure, with and without

LC effects, at an external electroluminescence quantum efficiency of 25% and a perovskite bandgap of 1.64 eV. Current mismatch throughout a typical year as the top cell thickness varies from 800 nm (b) to 300 nm (c), with a 100 µm thick silicon bottom cell.

**Figure S3:** Variation in energy yield (EY) for different combinations of top and bottom subcell thicknesses in a monolithic perovskite/silicon tandem structure, calculated from TMY data in Denver, USA, with and without luminescent coupling (LC) effects, at an external electroluminescence quantum efficiency (ELQE) of 8.4% and a perovskite bandgap of 1.64 eV. Comparison of the current mismatch for the optimized thicknesses calculated for Denver (b) and Daggett (c) at this bandgap.

## Supplementary Note 1: Optical model

The optical modeling, adapted from the EYcalc[1] developed by the KIT team, utilizes optical constants for each material in the device stack, sourced from the literature and measured data. The transfer matrix method was applied to calculate the fraction of light absorbed in each layer of the device stack and treated textured surfaces using statistical ray tracing. Based on this model, the proposed modelling was developed to consider the effect of the LC and variation of the radiative recombination with the illumination intensity into the output power. In addition, the effect of temperature on the absorption spectrum of each subcell for EY calculation was considered. Due to the lack of experimental data across a complete range of perovskite bandgaps, we adjusted the absorption coefficient along the energy axis and performed a Kramers–Kronig transformation to calculate the complex refractive index (**Figure S4**). In semiconductors, bandgaps vary with temperature, notably in opposite directions for Si and perovskite materials[2]—a shift of 0.3 meV/K for the perovskite top absorber[3] and -0.27 meV/K for the silicon bottom absorber[4]. We simulated these changes by perfectly shifting the absorption coefficient horizontally along the energy axis.[5] A library of complex refractive indices at temperatures ranging from -20°C to 80°C with a resolution of 0.1°C was generated in advance to reduce computing time. **Figures S5** and **Figures S6** illustrate how the refractive index changes with temperature for the perovskite top cell and silicon bottom cell, respectively. The effect of the temperature on the absorptivity spectra of both subcell and the generated current temperature coefficient were shown in **Figures S7** and **Figures S8,** respectively. Additionally, the EY model accounts for diffuse irradiance, necessitating the inclusion of the angle of incident light’s effect on the absorptivity spectrum. A simple cloud model assumes no spectral change for the direct irradiation. However, the diffuse irradiation is assumed to be composed of direct and diffuse clear sky irradiance weighted by the cloud cover, as detailed in recent work.[6] Then, using the angle of each incoming light, the absorptivity spectrum can be

obtained. **Figure S9** demonstrates the difference in the absorptivity spectrum between direct and diffuse illumination.

We derived the refractive index (n, k) data for materials such as SnOx,[7] C60,[8] PTAA,[9] ITO,[10] and Ag[11] from the literature, while for Poly-Si and AlOx, we used data measured through spectral ellipsometry. The refractive index data for other layers were sourced from PV Lighthouse.[12] Details of the investigated monolithic tandem structure were elaborated in our previous publications[13] and the illustration for the tandem structure was described in **Figure** **S11a**. To determine the absorptivity of each absorber in a perovskite/silicon monolithic tandem solar cell, we implemented an optical model. This model calculates the absorptivity of each subcell and the reabsorption of photons at the bottom cell. Additionally, the model accounts for the nominal operating cell temperature (NOCT) and adjusts for the increase in module temperature above the ambient temperature Tambient due to solar insolation (S):[14–16]

<u>𝑁𝑂𝐶𝑇 − 20</u> (S1) 𝑇𝑚𝑜𝑑𝑢𝑙𝑒= 𝑇𝑎𝑚𝑏𝑖𝑒𝑛𝑡+ 𝑆 80 Where S is the insolation in mWcm -2.

**Figure S4:** Shifted extinction coefficients and corresponding Kramers-Kronig transformed refractive index spectra.

**Figure S5:** Extinction coefficients and refractive index spectra of the perovskite top cell at different temperatures, assuming a bandgap shift of 0.3 meV/°K due to temperature differences.

**Figure S6:** Extinction coefficients and refractive index spectra of the silicon bottom cell at different temperatures, assuming a bandgap shift of -0.27 meV/°K due to temperature differences.

**Figure S7:** The difference in simulated absorption spectra of the two subcells in the investigated monolithic perovskite/silicon tandem cell under the effect of temperature. Generated current calculated under the AM1.5G spectrum for a 550 nm perovskite subcell, a 150 µm silicon subcell, and a 1.64 eV perovskite bandgap.

**Figure S8:** Temperature-dependent generated current density and generated current temperature coefficient (𝑇𝐶𝐽𝑝) calculation of the perovskite top cell in the investigated tandem cells. The temperature coefficient is calculated using the following formula and found to be -0.036% °K -1, which agrees well with recent studies,

[17,18] proving the validity of the modeling. The temperature coefficient is normalized at 25 °C, as this is the standard reference temperature for terrestrial and most space PV technologies. <u>𝑆𝑙𝑜𝑝𝑒 𝑜𝑓 𝑡ℎ𝑒 𝑙𝑖𝑛𝑒𝑎𝑟 𝑓𝑖𝑡</u> (S2) 𝑇𝐶𝐽𝑝= × 100 𝑇𝐽𝑝@25℃

**Figure S9:** The difference in simulated absorption spectra of the two subcells in the investigated monolithic perovskite/silicon tandem cell under direct and diffuse illumination. Generated current calculated under the AM1.5G spectrum for a 550 nm perovskite subcell, a 150 µm silicon subcell, and a 1.64 eV perovskite bandgap. **Supplementary Note 2: Electrical model**

For our electrical model, we utilized a single diode equivalent circuit that incorporates the solar cell’s radiative efficiency along with the ideality factor, shunt resistance, and series resistance. We extracted these parameters from published current-voltage curves of actual measured cells. To calculate the output power of the solar module, the electrical model employs the one-diode model, which determines the J-V (current-voltage) characteristics, including series resistance (RS) and shunt resistance (RSH):

|(𝑇) − 𝐽(𝑉, 𝑇) = 𝐽|𝐽₀|(𝑇) (𝑒|𝑞(𝑉+𝐽𝑅𝑆) 𝑛𝑘𝑇|
|---|---|---|---|
|𝑝|𝐸𝑄𝐸|𝐸𝐿||
||= 𝐽 𝑝|(𝑇) − 𝐽|(𝑉, 𝑇) 𝑟𝑒𝑐|

<u>𝑉 + 𝐽(𝑉)𝑅𝑠</u>(S3) − 1) − 𝑅𝑆𝐻

Where J₀ dark saturation current density, k Boltzmann constant, n ideality factor, T temperature of the solar module.

The short circuit density JSC and the reserve saturation current (J₀) can be determine by:

|𝐽 𝑝|(𝑇) = 𝑞 ∫|∞ 𝐴(𝐸, 𝑇)𝜙|(𝐸)𝑑𝐸 𝑠𝑢𝑛|
|---|---|---|---|
|||0||
|(𝑇) = 𝐽₀|𝑞 𝐸𝐿𝑄𝐸|∞ ∫|(𝐸, 𝑇)𝑑𝐸 𝐴(𝐸, 𝑇)𝜙 𝐵𝐵|
|||0||

(S4)

(S5)

Where ELQE is external electroluminescence quantum efficiency, 𝜙𝑠𝑢𝑛 and 𝜙𝐵𝐵 are respectively the photon flux from the solar spectrum and the photon flux body at temperature T and energy E with 𝜙𝐵𝐵:

<u>1 𝐸²</u> (S6) 𝐽𝐵𝐵(𝐸, 𝑇) =2 3 2 4𝜋 ℏ 𝑐 <u>𝐸</u> 𝑒𝑥𝑝 ()−1 𝑘𝑇 Where c and ℏ are speed of light and Planck’s constant divided by 2𝜋, respectively.

The output power density of the cell can be calculated from the J-V as:

(S7)

|𝑃 𝑡𝑎𝑛𝑑𝑒𝑚|(𝑇) = 𝐽 𝑡𝑎𝑛𝑑𝑒𝑚|(𝑇) [𝑉|(𝐽 𝑠𝑖|(𝑇)) + 𝑉 𝑟𝑒𝑐,𝑠𝑖|(𝑇))] (𝐽 𝑠𝑖 𝑟𝑒𝑐,𝑝𝑣𝑘|
|---|---|---|---|---|---|
||𝑃 𝑚𝑎𝑥||(𝑇) = 𝑚𝑎𝑥(𝑃|𝑡𝑎𝑛𝑑𝑒𝑚|(𝑇))|

(S8)

## Supplementary Note 3: Energy yield model

**Figure S10:** Schematic flow of the modular energy yield (EY) modelling. The schematic described in **Figure S10** illustrates our comprehensive modeling approach. The irradiance function utilizes TMY3 data to generate the irradiance spectra, which serves as an input for the energy yield function. The optic function is tasked with producing the absorptivity spectra for each subcell, accounting for varying angles of incident light and the working temperature of the solar structure. The energy yield function then calculates the generated photon current based on these spectra and determines the output power. Lastly, the electrical function employs a one-diode model to define the J-V (current-voltage) characteristics, incorporating both the electrical parameters.

**Figure S11:** Illustration of (a) the investigated monolithic (2T) perovskite/silicon tandem solar cell and (b) the compared single-junction silicon solar cell. (c) Comparison of the energy yield of a monolithic tandem solar cell with varying subcell thicknesses (as shown in **Figure 1** of the main manuscript, without the effect of LC) and a single-junction silicon solar cell of the same quality at the same location.

## References

[1] Schmager R, Langenhorst M, Lehr J, Lemmer U, Richards BS, Paetzold UW. Methodology of energy yield modelling of perovskite-based multi-junction photovoltaics. Opt Express 2019;27:A507. [https://doi.org/10.1364/oe.27.00a507](https://doi.org/10.1364/oe.27.00a507).

[2] Dupré O, Vaillon R, Green MA. Physics of the temperature coefficients of solar cells. Sol Energy Mater Sol Cells 2015;140:92–100. [https://doi.org/10.1016/j.solmat.2015.03.025](https://doi.org/10.1016/j.solmat.2015.03.025).

[3] Wu K, Bera A, Ma C, Du Y, Yang Y, Li L, et al. Temperature-dependent excitonic photoluminescence of hybrid organometal halide perovskite films. Phys Chem Chem Phys 2014;16:22476–81. [https://doi.org/10.1039/c4cp03573a](https://doi.org/10.1039/c4cp03573a).

[4] Green MA. Intrinsic concentration, effective densities of states, and effective mass in silicon. J Appl Phys 1990;67:2944–54. [https://doi.org/10.1063/1.345414](https://doi.org/10.1063/1.345414).

[5] Löper P, Stuckelberger M, Niesen B, Werner J, Filipič M, Moon SJ, et al. Complex refractive index spectra of CH3NH3PbI3 perovskite thin films determined by spectroscopic ellipsometry and spectrophotometry. J Phys Chem Lett 2015;6:66–71. [https://doi.org/10.1021/jz502471h](https://doi.org/10.1021/jz502471h).

[6] Ernst M, Holst H, Winter M, Altermatt PP. SUNCALCULATOR: A program to calculate the angular and spectral distribution of direct and diffuse solar radiation. Sol Energy Mater Sol Cells 2016;157:913–22. [https://doi.org/10.1016/j.solmat.2016.08.008](https://doi.org/10.1016/j.solmat.2016.08.008).

[7] Mullings MN, Hägglund C, Bent SF. Tin oxide atomic layer deposition from tetrakis(dimethylamino)tin and water. J Vac Sci Technol A Vacuum, Surfaces, Film 2013;31:061503. [https://doi.org/10.1116/1.4812717](https://doi.org/10.1116/1.4812717).

[8] Sittinger V, Schulze PSC, Messmer C, Pflug A, Goldschmidt JC. Complex refractive indices of Spiro-TTB and C 60 for optical analysis of perovskite silicon tandem solar cells. Opt Express 2022;30:37957. [https://doi.org/10.1364/oe.458953](https://doi.org/10.1364/oe.458953).

[9] Jošt M, Köhnen E, Morales-Vilches AB, Lipovšek B, Jäger K, Macco B, et al. Textured interfaces in monolithic perovskite/silicon tandem solar cells: Advanced light management for improved efficiency and energy yield. Energy Environ Sci 2018;11:3511–23. [https://doi.org/10.1039/c8ee02469c](https://doi.org/10.1039/c8ee02469c).

[10] Holman ZC, Filipič M, Descoeudres A, De Wolf S, Smole F, Topič M, et al. Infrared light management in high-efficiency silicon heterojunction and rear-passivated solar cells. J Appl Phys 2013;113. [https://doi.org/10.1063/1.4772975](https://doi.org/10.1063/1.4772975).

[11] Jiang Y, Pillai S, Green MA. Realistic Silver Optical Constants for Plasmonics. Sci Rep 2016;6:30605. [https://doi.org/10.1038/srep30605](https://doi.org/10.1038/srep30605).

[12] “PV Lighthouse.” [Online]. Available: [https://www.pvlighthouse.com.au/](https://www.pvlighthouse.com.au/). [Accessed: 20-Jan-2024]. “PV Lighthouse.” [Online]. Available: [https://www.pvlighthouse.com.au/](https://www.pvlighthouse.com.au/). [Accessed: 20-Jan-2024]. 2024.

[13] Wu Y, Zheng P, Peng J, Xu M, Chen Y, Surve S, et al. 27.6% Perovskite/c‐Si Tandem Solar Cells Using Industrial Fabricated TOPCon Device. Adv Energy Mater 2022;2200821:2200821. [https://doi.org/10.1002/aenm.202200821](https://doi.org/10.1002/aenm.202200821).

[14] Koehl M, Heck M, Wiesmeier S, Wirth J. Modeling of the nominal operating cell temperature based on outdoor weathering. Sol Energy Mater Sol Cells 2011;95:1638–

46. [https://doi.org/10.1016/j.solmat.2011.01.020](https://doi.org/10.1016/j.solmat.2011.01.020).
[15] Asef P, Bargallo R, Hartavi Karci AE, Niknejad P, Barzegaran MR, Lapthorn AC. Correlation of solar power prediction considering the nominal operating cell

temperature under partial shading effect. Meas J Int Meas Confed 2019;147:106878. [https://doi.org/10.1016/j.measurement.2019.106878](https://doi.org/10.1016/j.measurement.2019.106878).

[16] Sun V, Asanakham A, Deethayat T, Kiatsiriroat T. A new method for evaluating nominal operating cell temperature (NOCT) of unglazed photovoltaic thermal module. Energy Reports 2020;6:1029–42. [https://doi.org/10.1016/j.egyr.2020.04.026](https://doi.org/10.1016/j.egyr.2020.04.026).

[17] Aydin E, Allen TG, De Bastiani M, Xu L, Ávila J, Salvador M, et al. Interplay between temperature and bandgap energies on the outdoor performance of perovskite/silicon tandem solar cells. Nat Energy 2020. [https://doi.org/10.1038/s41560-020-00687-4](https://doi.org/10.1038/s41560-020-00687-4).

[18] Babics M, Bristow H, Pininti AR, Allen TG, De Wolf S. Temperature Coefficients of Perovskite/Silicon Tandem Solar Cells. ACS Energy Lett 2023;8:3013–5. [https://doi.org/10.1021/acsenergylett.3c00930](https://doi.org/10.1021/acsenergylett.3c00930).
