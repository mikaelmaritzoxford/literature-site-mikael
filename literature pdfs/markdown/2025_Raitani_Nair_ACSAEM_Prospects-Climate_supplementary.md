# Supporting Information Prospects for climate-specific design of

# Perovskite-Silicon tandem solar cells and influence of degradation rates

1 1

### Karthik Raitani and Pradeep R. Nair

### Department of Electrical Engineering, Indian Institute of Technology Bombay, Mumbai 400076, India

#### Email: karthikr@iitb.ac.in, prnair@ee.iitb.ac.in

## S1 Shockley–Queisser (SQ) Limit Calculations

Shockley–Queisser (SQ) or detailed balance approach estimates the maximum efficiency limit for solar cells [1]. It assumes that the solar cell absorbs every incident photon with energy exceeding the bandgap (*Eg*) and is limited only by radiative recombination within the device [2].

The net current density (*J*) extracted from the device due to the photo-generated e-h pairs which do not participate in the radiative recombination and can be estimated as

*J*(*Eg,V*) = *−q*(*Nph*(*Eg*) *− R*(*Eg,V*)) (S1a) <u>qV</u> *J*(*V*) = *−Jsc*+ *Jo*(*e* *kb T* *−* 1) (S1b)

Here, q is the electronic charge, *kb*is the Boltzmann constant, T is temperature, *Jsc* (short-circuit current density) which is given as *Jsc*= *qNph*, where *Nph*is the photon flux with *E > Eg*and V is the voltage. The other term on the RHS in equation (S1a) denotes the radiative recombination in the device, R(*Eg*,V), which relates to the dark current *Jo* in equation (S1b).

The absorbed photon flux *Nph*(*Eg*), which integrates over photon energies exceeding the bandgap of the semiconductor, is given by Z *∞* <u>ϕAM1.5G(E)dE</u> *Nph*(*Eg*) = (S2) *Eghc/λ* where, *ϕAM. G*is the measured AM1.5G solar irradiance, *h* is the Planck’s constant, *c* is speed of light and *λ* is the wavelength of the photon.

S1

In the detailed balance case, the radiative recombination calculated by assuming the solar cell as a blackbody in equilibrium at room temperature and is expressed as,

(*qV/kbT*) *R*(*V*) = *Ro*(*e −* 1)*,* (S3)

where, *Ro*at cell temperature *Tc*is given as Z *∞* 2 <u>2π E</u> *Ro*= *dE* (S4) 3 2 *E/k T* *h cEeb c−* 1 *g* For SQ limits of 2-Terminal (2-T) tandem cell, the top, and bottom are cell are connected in series. The corresponding J-V characteristics are:

<u>qVtop</u> *kb T* *Jtop*= *−Jsctop*+ *Jotop*(*e −* 1) (S5)

and,

<u>qVbottom</u> *kb T* *Jbottom*= *−Jsc*+ *Jo*(*e −* 1) (S6) *bottom bottom* The voltage across tandem is given as:

#### Vtandem= Vtop+ Vbottom(S7)

and tandem current is

#### Jtandem= Jtop= Jbottom(S8)

The maximum output power from the tandem device is then estimated as:

#### Ptandem= −min(Jtandem× Vtandem) (S9)

Note that as the *J−V* characteristics are in the 4th quadrant, the power estimated through *J×V* will be negative in sign (i.e., net power generation and not dissipation). Hence, the maximum power generated is given as the minimum value of *Jtandem× Vtandem*. The 4-T tandem characteristics can be found in similar terms.

S2

Figure S1: SQ limits for single junction, 2-T and 4-T tandem solar cells (a) *η*, *Voc*, *Jsc* and Fill factor (FF) for single junction solar cells at SQ limits. Efficiency map for 2-T, and (c) 4-T tandem solar cells at SQ limits with respect subcell bangap. (d) Efficiency limits for 2-T and 4-T tandem solar cells with Silicon as the bottom cell for varying top cell bandgap.

The variation of SQ limit efficiencies, *Jsc*, *Voc*, and *FF* with bandgap for single- junction solar cells is illustrated in Fig. S1(a). The maximum efficiency of 33*.*7% is achieved at *Eg∼* 1*.*4 eV using the AM1.5G spectrum as input.

Figure S1((b) and (c)) presents a color map showing the evolution of 2-T and 4- T tandem efficiency (*η*) as a function of the bandgaps of the top and bottom cells, respectively. For 2-T configuration with silicon as the bottom cell, the 2-T tandem cell achieves an efficiency limit of *η ∼* 45*.*0% at *Eg,*top= 1*.*73 eV as illustrated in Fig. S1(d). In contrast, the 4-T configuration demonstrates a broader range of top-cell bandgaps with SQ limit efficiencies exceeding 40%.

S3

## S2 Numerical Simulations

### S2.1 Optical Simulations

Figure S2: Scheme for optical simulations: (a) P–Si 2-T tandem solar cell; (b) Absorption and transmission in the perovskite top cell with thickness of different layers.

#### Transfer Matrix Method for Top Cell

Optical simulations are essential to quantify reflection, transmission, and parasitic ab- sorption in different layers. The device model for the P–Si 2-T tandem solar cell is shown in Fig. S2(a). The transfer matrix method (TMM) [3] is employed to simulate the wavelength-dependent optical response of the full stack. TMM uses complex refractive indices and thicknesses of each layer, as shown in Fig. S2(b), with layer thicknesses taken from literature [4].

Figure S3: Temperature-dependent bandgap and optical constants: (a) Experimentally derived optical constants at different temperatures for perovskite (*Eg*= 1*.*68 eV) from spectroscopic ellipsometry [5]; (b) Change in *Eg*(∆*Eg*) for perovskites with different Br content, from absorbance measurements [6].

S4

Temperature-dependent optical simulations are performed using these temperature- resolved optical constants for the perovskite absorber. As shown in Fig. S3(a), Raja *et* *al.* reported complex refractive index data (*n* + *ik*) at various temperatures, indicating a blue shift in *k* near the band edge as temperature increases, consistent with bandgap widening. The change in bandgap ∆*Eg*for a 50 *◦* C rise is shown in Fig. S3(b). The tem- perature dependence of the bandgap is modeled using *K* = 0*.*5 meV/K for perovskites [7, 8, 9] and *K* = *−*0*.*28 meV/K for silicon [6], and described as

*Eg*(*T*) = *Eg*(25 *◦*

C) + *K*(*T −* 25
*◦*

C)*,* (S10)
Fig. S4(a) quantifies the fraction of light absorbed in each layer (ITO, ETL, perovskite,

HTL), along with the total reflectance across the solar spectrum. This modeling explicitly accounts for parasitic reflection and absorption in all layers, accounting for the optical losses. Additionally, the TMM framework calculates the spatially resolved generation profile within the perovskite layer, which is used in drift-diffusion simulations to determine the *J*–*V* characteristics and (*Jsc*) of the top cell.

#### Silicon Bottom Cell Simulations

Figure S4: Optical simulation results: (a) Light absorption and reflection in the perovskite top cell; (b) Transmitted light to silicon bottom cell.

To model the bottom cell, we use the TMM-derived transmitted spectrum *ϕT*(*λ*), shown in Fig. S4(b), which represents the photon flux reaching the silicon bottom cell after passing through the top cell. This is multiplied by the local spectra to determine the actual input. The resulting flux is then integrated with the external quantum efficiency (EQE) of a state-of-the-art silicon heterojunction cell [10], which inherently includes effects of surface texturing and back reflection, as these are part of the experimental EQE data. The short-circuit current of the silicon bottom cell is then calculated using: Z *Jsc* Si = *q EQE*(*λ*) *· ϕT*(*λ*)*dλ,* (S11)

where *EQE*(*λ*) is the measured EQE and *ϕT*(*λ*) is the TMM-derived transmitted photon flux. This approach ensures that parasitic losses are explicitly included via TMM, while texturing and back-reflection effects are implicitly included via measured EQE.

S5

#### Tandem Jscand Current Mismatch

Figure S5: Current mismatch (CM) in P–Si 2-T tandem solar cells: (a) *Jsc*of perovskite, silicon, and tandem cells at room temperature across top-cell bandgap (*EgT*); (b) Current mismatch map from TMM simulations versus temperature and *EgT*.

The resulting *Jsc*and current mismatch for the tandem cell across different *EgT*values are shown in Fig. S5(a). Near *EgT*= 1*.*68–1.70 eV, current matching is optimal at room temperature, but even small thermal perturbations can cause significant mismatch. The mismatch map in Fig. S5(b) shows that for 1*.*62 eV *< EgT<* 1*.*72 eV, the current mismatch remains below 3 mA/cm² across a wide temperature range.

### S2.2 Drift-Diffusion Simulations for Perovskite Top Cell

Methodology

Self-consistent drift-diffusion simulations, incorporating ion migration and temperature- dependent parameters, are employed to determine the steady-state *J*-*V* characteristics of the top cell. The coupled system of equations governing the device physics includes Poisson’s equation and continuity equations for electrons, holes, and mobile ions, which are solved numerically as follows:

#### Governing Equations

<u>∂</u> 2 <u>ψ −q</u> 2 = (*p − n* + *N*dop+ *NI,p− NI,n*)*,* (S12) *∂x ε*

<u>∂n 1 ∂Jn</u> = *G−Rn*+*,* (S13) *∂t q ∂x*

<u>∂p 1 ∂Jp</u> = *G−Rp−,* (S14) *∂t q ∂x*

<u>∂NI,n1 ∂JI,n</u> =*.* (S15) *∂t q ∂x* Here, *ψ* is the electrostatic potential, *q* the elementary charge, *ε* the dielectric constant, *x* the spatial coordinate, and *t* time. The variables *p* and *n* denote hole and electron

S6

concentrations, respectively; *NI,p*and *NI,n*represent positive and negative ion densities; and *N*dopis the doping concentration. *G* is the position-dependent carrier generation rate calculated using the Transfer Matrix Method (TMM). *Rn*and *Rp*are the recombination rates for electrons and holes, respectively.

#### Current Densities

Electron and hole current densities (*Jn*and *Jp*) are given by:

<u>dn</u> *Jn*= *qnµnE* + *qDn,* (S16) *dx*

<u>dp</u> *Jp*= *qpµpE − qDp,* (S17) *dx*

|||dψ|
|---|---|---|
|n|p|dx|

where *µn*and *µp*are the mobilities, *D* and *D* the diffusion coefficients, and *E* = *−* is the electric field.

#### Recombination Mechanisms

Recombination mechanism of the perovskite top cell is modelled using trap-assisted non- radiative recombination (SRH, *R*SRH)[11], band-to-band radiative recombination (*R*Rad)[1], and Auger recombination (*R*Aug) [12]. Note that radiative recombination and Auger re- combination are specified only for the active layer.

#### R = RSRH+ RRad+ RAug(S18)

<u>np − n²i</u> *R*SRH= (S19) *τn*(*p* + *p₁*) + *τp*(*n* + *n₁*)

where *n₁* = *nie* (*ET−Ei*)*/kT* and *p₁* = *nie* (*Ei−ET*)*/kT*. The radiative and Auger recombi- nation are given as: *R*Rad= *CR*(*np − n²i*) (S20)

*R*Aug= *CA*(*n* + *p*)(*np − n²i*) (S21)

Here *n*, *p* are electron and hole concentrations, *ni*is the intrinsic carrier concentration, and *τn*= *τp*= *τ* is the minority carrier lifetime. *ET*denotes the trap energy level and *Ei* denotes the intrinsic energy level. For midgap traps, *ET*= *Ei*and thus *n₁* = *p₁* = *ni*. *CR* is the radiative recombination parameter and *CA*is the Auger recombination parameter. Effective lifetime *τeff*with interface recombination velocity (*Sv*) is given by [13, 14]:

1 1 2*Sv* = + (S22) *τ*eff*τ*bulk*W*

where *W* is the absorber thickness and *Sv*is the interface recombination velocity.

#### Boundary Conditions

- Ions are confined to the perovskite layer with Neumann boundary conditions en- suring no ion flux across interfaces.
- Ohmic boundary conditions are assumed at metal contacts to both p-type and n-type regions.
S7

#### Numerical Implementation and Validation

The coupled steady-state equations are solved self-consistently. Poisson’s equation is discretized using a finite difference scheme, while the current terms in the continuity equations are evaluated using the Scharfetter-Gummel discretization method to ensure numerical stability and accuracy [15]. Newton’s iterative method is employed to solve the nonlinear system and achieve self-consistency between the electrostatic potential and carrier densities. All the scripts were written and compiled using MATLAB simulation software. Through this simulation framework, our group has addressed multiple system-level concerns in previous studies, including phase segregation [16], ion-induced passivation of grain boundaries [17], pinhole-induced efficiency variation [18], predicting the scal- ing exponents of capacitance-voltage characteristics [19], self-doping induced efficiency degradation [20], electrostatic effects of trapped charges [21], dark current-voltage char- acteristics [22], large signal switching [23], efficiency limits with n-type hole extraction layers [24], and ionic imbalance issues [25].

Parameters

All relevant material parameters, including temperature dependencies, mobilities, recom- bination coefficients, and doping concentrations, are listed in Table S1.

Table S1: Material Parameters for HTL, Perovskite, and ETL layers.

|Parameter||HTL|Perovskite||ETL|
|---|---|---|---|---|---|
|Thickness (nm)||30|||30|
|N (cm|)|10|-||-|
|N (cm|)|-|-||10|
|N (cm|)|-|10||-|
|E (eV)||2.55|1.58-1.77||2.55|
|Electron Affinity (eV)||2.865|4||4.1|
|Dielectric constant (ε) (ref.[26], [28])||3|6.6||9|
|µ (cm²/Vs) (ref.[29])||10|10||10|
|µ (cm²/Vs) (ref.[29])||-|10||-|
|τ (SRH) (sec)||10|10||10|
|τ (SRH) (sec)||10|10||10|
|Bimolecular recombination coefficient (k₂) (cm³/s) (ref.[30])||-|10||-|
|Auger recombination Coefficient (C) (cm⁶/s) (ref.[31])||-|10||-|
|Effective density of states (N||10|3 × 10|[32]|10|

500 (ref.[26], [27]) *a* *−*3 18

*d* *−*3 18

*ion* *−*3 18

*g*

*n* *−*2 *−*2

|µ (cm²/Vs) (ref.[29])||10|10|10|
|---|---|---|---|---|
|ion|||−8||
|n||−7|−5|−7|
|p||−7|−5|−7|
||||−10||
||||−29||
||c v|19|18|19|

*p* *−*2 *−*2 *−*8

, *N* (cm *−*3 ))

### S2.3 Simulation for Silicon bottom cell

The temperature dependent Silicon bottom cell *J*-*V* characteristics is calculated using the analytical solar cell diode equation given as

*J*(*T,V*) = *−Jsc*(*T*) + *Jo*(*e* (*qV/nkbT*) *−* 1) (S23)

where, J is the current density, V is the voltage, *Jo*is the dark current and n is the ideality factor of the bottom cell. The estimation of *Jsc*for the bottom cell is described in the

S8

previous section. This approach incorporates temperature coefficients for (*Jsc*), (*Voc*), of commercial Silicon modules to model the *J*-*V* characteristics at elevated temperatures [33, 34]. The temperature coefficients and other parameters for silicon such as *Voc*, *Jo*and n chosen as per industry standards [35, 36] as shown in table S2.

Table S2: Temperature Coefficients and other parameters for Silicon bottom cell

|Parameter||Values|
|---|---|---|
|V|(V )|0.72|
|J|(mA/cm²)|2.2 × 10|
|n||1.1|
|T|(%/K)|-0.0440|
|T|(%/K)|-0.28|

*oc* *o* *−*9

*J* *sc* *V* *oc*

### S2.4 Numerical simulation of P/Si tandem solar cells

#### Calibration with Experimental Results

To validate our simulation framework, here we compare the steady-state *J*-*V* charac- teristics obtained from our model with recent experimental data reported by Liu *et al.* [37]. The device parameters used for both simulation and experiment are summarized in Table S3. As shown in Fig. S6, the simulated *J*-*V* curve closely matches the experimental data.

Data set *Jsc*(mA/cm²) *Voc*(V) Fill Factor (%) Efficiency (%) Experiment 20.67 1.98 83.2 34.08 Simulation 20.10 2.00 88.3 35.53 Simulation with R*s*20.10 2.00 83.00 33.39

Table S3: Device parameters for the experimental and simulated *J*-*V* characteristics.

S9

Figure S6: Normalized J-V curves for *EgT∼* 1.68 eV. Dotted lines show simulation and solid line show experimental data from Liu *et al*[37]. The red dotted line shows the simulated J-V curve considering the series resistance, which is in good agreement with the experimental data.

### Temperature dependent Tandem JV characteristics

Figure S7: Temperature dependent characteristics for P-Si 2-T tandem obtained from drift-diffusion simulations (a) for 1.58, 1.62 and 1.66 eV and (b) 1.68, 1.71 and 1.77 eV top cell bandgap.

The series connection of the subcells governs the P-Si 2-T tandem Characteristics. Figure S7(a) and (b) illustrate the efficiency *η*, fill factor (FF), *Jsc*, and *Voc*of the P-Si tandem for various top-cell bandgaps and elevated temperatures. For relatively narrow bandgaps, the Silicon bottom cell dominates. This dominance is evident from the increase in *Jsc* with temperature, which also influences other parameters, particularly the fill factor. Conversely, for a top-cell bandgap of 1.66 eV, the dominance shifts with temperature, resulting in both an increase and decrease in, *Jsc*as the temperature rises. This signif- icantly impacts the FF of the tandem. Figure S7(b) focuses on tandem parameters for wider bandgaps, where the Perovskite top cell dominates. The maximum efficiency (*η*) is achieved for bandgaps of 1.68 and 1.71 eV across the entire temperature range. The

S10

efficiency (*η*) reduction with rise in temperature can be observed for each case. However, this decrease is less pronounced for narrower bandgaps as compared to others.

Figure S8: P–Si 2-T tandem efficiency at elevated temperatures. (a) Variation of effi- ciency with top-cell bandgap (*EgT*) at different temperatures, based on numerical simu- lations, illustrating the impact of temperature dependence, recombination, and ion mi- gration. (b) Efficiency map of the P–Si tandem cell as a function of temperature and *EgT*, highlighting the range of maximum efficiency (*η*) and its temperature sensitivity, as indicated by the temperature coefficient.

Fig. S8 (a) and (b) addresses the temperature dependence of *η* for different top cell *Eg*.

At room temperature, the maximum efficiency is achieved for a small range of *EgT*values around 1.68–1.70 eV, where the curve is skewed. However, as the temperature increases, the efficiency curve flattens. The temperature coefficients for each case, provided in the Fig.S8(b), show an increasing trend with *EgT*and demonstrate a strong sensitivity to current mismatch. Notably, this behavior is inversely related to the current mismatch (see

Fig. S5(a) and (b)). The temperature sensitivity is highest near *Eg*values of 1.68–1.70

eV, as current mismatch is negligible at room temperature, but even small temperature- induced changes lead to significant mismatch, thereby impacting device performance.

### S2.5 Effect of recombination parameters

The results shared in the main manuscript illustrated how the efficiencies of 2-T P/Si tandem solar cells vary as a function of *EgT*. To obtain such a comparative analysis, we used the same set of values for bimolecular (*k*rad) and trap-assisted (*k*SRH) recombina- tion coefficients for all all top-cell bandgaps (*E*gT) (see Table S1). However, in reality, these parameters may vary with the process conditions, and improvements in recom- bination properties can significantly enhance device performance. As shown in Fig. S9, lower recombination coefficients lead to higher efficiencies. In particular, narrow-bandgap perovskites could be more competitive in both performance and stability compared to wider-bandgap counterparts with a significant relative improvement in their recombina- tion parameters-in addition to that of the degradation rates.

S11

Figure S9: Efficiency of P-Si tandem as a function of recombination parameters. *krad*is the bimolecular recombination coefficient and *kSRH*is the trap assisted (or monomolecu- lar) recombination coefficient in the top perovskite cell. These calculations are done for *EgT*=1.68 eV.

### S2.6 Experimental efficiencies and stability results

Fig. S10 is a compilation of experimental efficiencies for various *EgT*as reported in liter-

ature. The maximum efficiency is observed near *EgT∼* 1*.*66–1*.*70 eV, consistent with the trends from numerical simulations. The corresponding experimental stability parameters (i.e., the *T₈₀*, time taken for efficiency to degrade 80% of initial value) are summarized in Table S4.

The reported stability benchmarks differ significantly in their testing protocols and conditions (e.g., encapsulation, illumination source and intensity, temperature, and atmo- sphere). As a result, direct quantitative comparison is challenging. Standardized stability tests over the full *EgT*range would enable more credible and systematic assessments. As of now, significant efforts have been reported for *EgT∼* 1*.*66–1*.*70 eV range for P–Si tandems. Similar focused research on narrower top-cell bandgaps will help in optimizing the full accessible range.

S12

Figure S10: Efficiency vs *EgT*for P-Si tandems, line plots show simulated tandem ef- ficiency at 300 K and 330 K, while the symbols show experimental values for tandem efficiency from literature for various bandgap measured at STP (*∼* 300K) and in some cases certified from accredited labs. The references for the above experimental data is provided in Table. S4 with stability data.

|S.no|Symbol|E (eV) gT|η (%)|Stability remarks|ref|
|---|---|---|---|---|---|
|1. 2. 3. 4. 5. 6. 7. 8. 9.|*|1.59 1.62 1.63 1.65 1.66 1.67 1.68 1.69 1.70|26.00 28.51 25.20 28.60 29.80 30.70 32.50 33.90 31.25|T₉₃ = 1000 hrs (MPPT at STP in ambient conditions) T₉₀ = 130 hrs (MPPT under 1-Sun unencap- sulated) T₉₀ = 270 hrs (MPP under constant illumi- nation) T₉₃ = 550 hrs (MPP at 25°C, 1-Sun) T₈₀ = 300 hrs (MPPT in air unencapsulated) T₉₇ = 1000 hrs (MPPT –ISOS L1 procedure) T₉₀ = 870 hrs (MPPT under 1-Sun) T₈₀ = 1200 hrs (MPPT under 1-Sun) T₈₀ = 66 hrs (ISOS-L2) (after one year of dark storage)|[38] [39] [40] [41] [42] [43] [44] [37] [45]|

Table S4: Summary of experimental efficiencies and stability benchmarks for P–Si tandem solar cells with different *EgT*values. Stability tests vary in protocol, encapsulation, illumination intensity, and temperature, which affects direct comparability.

## S3 Energy Yield Estimation

The National Solar Radiation Database (NSRDB) provides on-demand spectral data, which includes hourly spectral irradiance across wavelengths along with temperature, wind speed, and other atmospheric parameters [46]. The spectral irradiance is integrated over the wavelength range to calculate the incident power density. The module temper- ature is derived using King’s model [47], based on the ambient temperature data, and is

S13

expressed as: *Tm*= *E · e* *a*+*b·WS* + *Ta*(S24)

where *Tm*represents the module temperature ( *◦*

C), *Ta*is the ambient temperature (
*◦*

C),
*E* denotes the incident solar irradiance on the module (*W/m²*), and *WS* is the wind speed (*m/s*). The parameters *a* and *b* are empirically derived constants with *a* = *−*3*.*47 and *b* = *−*0*.*594. The efficiency is a function of temperature *η*(*T*) and is calculated at each module temperature (*Tm*). A cell-to-module conversion loss of 7% is assumed (e.g., for c-Si solar cells with an efficiency of 25%, the corresponding module efficiency is taken as 23.25%) [48, 49].

Figure S11: Equivalent circuit model for P-Si Tandem. The JV curve (dotted lines) for *EgT*= 1.68 eV obtained through the equivalent circuit model aligns perfectly with the numerical simulations (solid lines) at different temperatures. The optical simulations remain the same for both cases.

To reduce the computational complexity associated with annual EY calculations, the following methodology is used. The numerically simulated JV characteristics of Per- ovskite top cell is described in terms of an equivalent circuit (two-diode model) [50] which is calibrated with the numerical simulations discussed in the previous section (see

Fig. S11). The two diode model can be described as

|(qV/k|T )|(qV/2k|T|
|---|---|---|---|
|o1||o2||

*J*(*V,T*) = *−Jsc*(*T*) + *J* (*T*)(*e* *b* *−* 1) + *J* (*T*)(*e* *b* *−* 1) (S25)

where, *Jo*1= *qkradn²iW* (S26)

and *Jo*2= *qksrhniW* (S27)

Here, *krad*and *ksrh*are the respective bimolecular and trap assisted recombination coefficient, *ni*is the intrinsic carrier density and W is the thickness of the perovskite. All parameters and their temperature (T) dependence are similar in both analytical and numerical simulations. The equivalent circuit description for the bottom cell is detailed in the previous section. The series connection of top and bottom cell characteristics is

S14

analyzed in terms of the equivalent circuits of the top and bottom cell (as shown in the inset of Fig. 1 of main manuscript) at the respective module temperature. Here the *JSC*of each cell is determined through the TMM calculations with the location specific incident spectra at the corresponding time of the year (with the corresponding tempera- ture dependent refractive indices). This calibrated approach reduces the computational complexity thus enabling facile estimation of EY at multiple geographic locations

## S4 LCOE Calculations

The Levelized cost of electricity or LCOE is defined as the ratio of total cost to the total energy output over the lifetime as defined below:

*Cm*+ *CL*+ *BOSf* *LCOE* = P*n*

||||n|t|−t||
|---|---|---|---|---|---|---|
||m|l|t=0|||f|
|||m|||||
|m mn|l|||mo m,om|lo l,om|Ln|

*t −t* (S28) *EY* (1 *− d*) (1 + *r*)

where, C and C represent the effective module and land costs, respectively. BOS col- lectively accounts for other fixed balance-of-system costs, which are considered negligible compared to C and C*l*. In the denominator, *EY* represents the initial annual energy yield, *d* is the degradation rate, and *r* is the discount factor. C and C consist of a fixed initial cost component (C and C) and recurring costs over time, such as operation and maintenance costs (C and C). Additionally, C and C represent the residual costs recovered after selling the land and module at the end of the tandem’s lifetime [51]. These relationships are further detailed in Eqs. (S29) and (S30).

X *n*

|C = C|+ (||C (t)(1 + r)|− C|(1 + r)|)|
|---|---|---|---|---|---|---|
|L|Lo||L,om||Ln||
|||t=0|||||
|||n||−t||−n|
|m|mo||m,om||mn||
|||t=0|||||
|||||||f|
|||||||r|

*L Lo L,om* *−t* *Ln* *−n* (S29)

X *C* = *C* + ( *C* (*t*)(1 + *r*) *− C* (1 + *r*)) (S30)

The effective cost can be split into a fixed cost component C which represents the sum of the first two time invariant terms from equation (S29) and (S30). While the time-varying components in the above equation is given by C, representing recurring costs, where the time variation is accounted using the discount factor *r*. Using these components, Eq. (S28) can be rewritten as

*Cf*+ *Cr* *LCOE* = P*n* *t −t* (S31) *t*=0 *EY* (1 *− d*) (1 + *r*)

The recurring cost is assumed to be a fixed percentage (X) of the initial fixed cost, where X is typically around 1% based on reference plants in the literature and may vary with geographical location [52]. Finally, LCOE can be simplified to: P

||n|−t|
|---|---|---|
|f|t=0||
|n t=0||−t|

<u>C (1 + X(1 + r))</u> *LCOE* = P *t* (S32) *EY* (1 *− d*) (1 + *r*)

S15

Figure S12: LCOE calculation parameters (a) LCOE vs *η* for P-Si tandem for *d* = 0*.*8% and *n* = 25 years as reported by Lisa et al [52]. (b) Variation of fixed cost with energy yield for different LCOE values, While at LCOE=0.036, Silicon and tandem become competitive (a 26% P-Si Tandem has similar LCOE of a 22% Si.)

The fixed cost (*Cf*) is estimated as follows. Lisa *et al.* ([52]) reported the dependence of efficiency (*η*) on the Levelized Cost of Electricity (LCOE) for Silicon, Perovskite, and P-Si 2-T tandem solar cells in residential and utility-scale installations in Southern Ger- many. The tandem LCOE from their calculations is presented in Fig. S12(a). These calculations were based on an annual solar irradiation of 1300 *kWh/m²* on the module plane, a system lifetime of 25 years, and a degradation rate of 0.8%. The energy yield (EY) in this context is the product of annual irradiation and *η*, which defines the rela- tionship between LCOE and EY.

A P-Si 2-T tandem with *η* = 26% becomes competitive with a silicon solar cell of *η* = 22% at LCOE = 0.036 (see Fig. S12(a)). *Cf*for a 26% efficient tandem is then calculated as 145 ($*/m²*) from equation S32 and is illustrated in Fig. S12(b). For LCOE calculations under varying degradation rates and lifetimes, we fix *Cf*= 145 ($*/m²*).

S16

## S5 Location specific estimates for EY and target degra- dation rates

Here we provide additional details on the location specific EY estimates. Fig. S13 shows the variation of target degradation rates for *N* = 18 years. Figs S14-S15 provides the solar insolation (daily) as well as monthly EY for various cities.

Figure S13: Normalized degradation rates (*d*norm.) which results in similar EY. These rates are normalized against *d₁* = 3%, the value chosen for *EgT*= 1*.*71 eV with *N* = 18 years.

S17

Figure S14: Calculated maximum module temperature per day and mean incident power density per month throughout the year (2019) for Riyadh (a) and (b), Seattle (c) and (d) and Tokyo (e) and (f).

S18

Figure S15: Calculated maximum module temperature per day and mean incident power density per month throughout the year (2019) for Frankfurt (a) and (b), Miami (c) and

(d).
## References

[1]W. Shockley and H. J. Queisser, “Detailed balance limit of efficiency of p-n junction solar cells,” *Journal of Applied Physics*, vol. 32, no. 3, pp. 510–519, 03 1961.

[2]T. Markvart, “Shockley: Queisser detailed balance limit after 60 years,” *Wiley In-* *terdisciplinary Reviews: Energy and Environment*, vol. 11, no. 4, p. e430, 2022.

[3]G. F. Burkhard, E. T. Hoke, and M. D. McGehee, “Accounting for interference, scattering, and electrode absorption to make accurate internal quantum efficiency measurements in organic and other thin solar cells,” *Advanced Materials*, vol. 22, no. 30, pp. 3293–3297, 2010.

[4]S. Manzoor, J. H¨ausele, K. A. Bush, A. F. Palmstrom, J. Carpenter III, Z. J. Yu,

S. F. Bent, M. D. Mcgehee, and Z. C. Holman, “Optical modeling of wide-bandgap perovskite and perovskite/silicon tandem solar cells using complex refractive indices for arbitrary-bandgap perovskite absorbers,” *Optics express*, vol. 26, no. 21, pp. 27 441–27 460, 2018.
[5]W. Raja, T. G. Allen, A. A. Said, O. Alharbi, E. Aydin, M. De Bastiani, and

S. De Wolf, “Temperature-dependent optical modeling of perovskite solar cells,” *The Journal of Physical Chemistry C*, vol. 126, no. 33, pp. 14 366–14 374, 2022.
S19

[6]E. Aydin, T. G. Allen, M. De Bastiani, L. Xu, J. Avila, M. Salvador, E. Van Ker- ´ schaver, and S. De Wolf, “Interplay between temperature and bandgap energies on the outdoor performance of perovskite/silicon tandem solar cells,” *Nature Energy*, vol. 5, no. 11, pp. 851–859, 2020.

[7]B. J. Foley, D. L. Marlowe, K. Sun, W. A. Saidi, L. Scudiero, M. C. Gupta, and

J. J. Choi, “Temperature dependent energy levels of methylammonium lead iodide perovskite,” *Applied physics letters*, vol. 106, no. 24, 2015.
[8]T. Moot, J. B. Patel, G. McAndrews, E. J. Wolf, D. Morales, I. E. Gould, B. A. Rosales, C. C. Boyd, L. M. Wheeler, P. A. Parilla *et al.*, “Temperature coefficients of perovskite photovoltaics for energy yield calculations,” *ACS Energy Letters*, vol. 6, no. 5, pp. 2038–2047, 2021.

[9]C. Quarti, E. Mosconi, J. M. Ball, V. D’Innocenzo, C. Tao, S. Pathak, H. J. Snaith,

A. Petrozza, and F. De Angelis, “Structural and optical properties of methylammo- nium lead iodide across the tetragonal to cubic phase transition: implications for perovskite solar cells,” *Energy & Environmental Science*, vol. 9, no. 1, pp. 155–163,
2016.
[10]H. Lin, M. Yang, X. Ru, G. Wang, S. Yin, F. Peng, C. Hong, M. Qu, J. Lu, L. Fang *et al.*, “Silicon heterojunction solar cells with up to 26.81% efficiency achieved by electrically optimized nanocrystalline-silicon hole contact layers,” *Nature Energy*, vol. 8, no. 8, pp. 789–799, 2023.

[11]R. L. Milot, G. E. Eperon, H. J. Snaith, M. B. Johnston, and L. M. Herz, “Temperature-dependent charge-carrier dynamics in ch3nh3pbi3 perovskite thin films,” *Advanced Functional Materials*, vol. 25, no. 39, pp. 6218–6227, 2015.

[12]A. Paulke, S. D. Stranks, J. Kniepert, J. Kurpiers, C. M. Wolff, N. Sch¨on, H. J. Snaith, T. J. Brenner, and D. Neher, “Charge carrier recombination dynamics in perovskite and polymer solar cells,” *Applied Physics Letters*, vol. 108, no. 11, 2016.

[13]G. B. Lush, H. MacMillan, B. Keyes, D. Levi, M. R. Melloch, R. Ahrenkiel, and

M. S. Lundstrom, “A study of minority carrier lifetime versus doping concentration in n-type gaas grown by metalorganic chemical vapor deposition,” *Journal of applied* *physics*, vol. 72, no. 4, pp. 1436–1442, 1992.
[14]K. L. Luke and L.-J. Cheng, “Analysis of the interaction of a laser pulse with a silicon wafer: Determination of bulk lifetime and surface recombination velocity,” *Journal of Applied Physics*, vol. 61, no. 6, pp. 2282–2293, 1987.

[15]D. L. Scharfetter and H. K. Gummel, “Large-signal analysis of a silicon read diode oscillator,” *IEEE Transactions on electron devices*, vol. 16, no. 1, pp. 64–77, 1969.

[16]A. Singareddy, U. K. R. Sadula, and P. R. Nair, “Phase segregation induced efficiency degradation and variability in mixed halide perovskite solar cells,” *Journal of Applied* *Physics*, vol. 130, no. 22, 2021.

[17]V. Nandal and P. R. Nair, “Ion induced passivation of grain boundaries in perovskite solar cells,” *Journal of Applied Physics*, vol. 125, no. 17, 2019.

S20

[18]S. Agarwal and P. R. Nair, “Pinhole induced efficiency variation in perovskite solar cells,” *Journal of Applied Physics*, vol. 122, no. 16, 2017.

[19]V. Nandal and P. R. Nair, “Anomalous scaling exponents in the capacitance–voltage characteristics of perovskite thin film devices,” *The Journal of Physical Chemistry* *C*, vol. 122, no. 49, pp. 27 935–27 940, 2018.

[20]N. Chatterji and P. R. Nair, “Electron versus hole extraction: self doping induced performance bottleneck in perovskite solar cells,” *IEEE Electron Device Letters*, vol. 40, no. 11, pp. 1784–1787, 2019.

[21]V. Nandal, S. Agarwal, and P. R. Nair, “Deciphering the capacitance frequency technique for performance-limiting defect-state parameters in energy-harvesting per- ovskites,” *Physical Chemistry Chemical Physics*, vol. 23, no. 42, pp. 24 421–24 427,

2021.
[22]S. Agarwal, M. Seetharaman, N. K. Kumawat, A. S. Subbiah, S. K. Sarkar, D. Kabra,

M. A. Namboothiry, and P. R. Nair, “On the uniqueness of ideality factor and voltage exponent of perovskite-based solar cells,” *The Journal of physical chemistry letters*, vol. 5, no. 23, pp. 4115–4121, 2014.
[23]T. Saketh Chandra, A. Singareddy, K. Hossain, D. Sivadas, S. Bhatia, S. Singh,

D. Kabra, and P. R. Nair, “Ion mobility independent large signal switching of per- ovskite devices,” *Applied Physics Letters*, vol. 119, no. 2, 2021.
[24]D. Sivadas, S. Bhatia, and P. R. Nair, “Efficiency limits of perovskite solar cells with n-type hole extraction layers,” *Applied Physics Letters*, vol. 119, no. 20, 2021.

[25]D. Sivadas, A. Singareddy, C. G. Vinod, and P. R. Nair, “Ionic charge imbalance in perovskite solar cells,” *The Journal of Physical Chemistry C*, vol. 127, no. 46, pp. 22 766–22 774, 2023.

[26]S. Manzoor, J. H¨ausele, K. A. Bush, A. F. Palmstrom, J. Carpenter III, Z. J. Yu,

S. F. Bent, M. D. Mcgehee, and Z. C. Holman, “Optical modeling of wide-bandgap perovskite and perovskite/silicon tandem solar cells using complex refractive indices for arbitrary-bandgap perovskite absorbers,” *Optics express*, vol. 26, no. 21, pp. 27 441–27 460, 2018.
[27]P. Tockhorn, J. Sutter, A. Cruz, P. Wagner, K. J¨ager, D. Yoo, F. Lang, M. Grischek,

B. Li, J. Li *et al.*, “Nano-optical designs for high-efficiency monolithic perovskite– silicon tandem solar cells,” *Nature Nanotechnology*, vol. 17, no. 11, pp. 1214–1221,
2022.
[28]S. Karthick, S. Velumani, and J. Boucl´e, “Experimental and scaps simulated for- mamidinium perovskite solar cells: A comparison of device performance,” *Solar* *Energy*, vol. 205, pp. 349–357, 2020.

[29]Y. Zhai, K. Wang, F. Zhang, C. Xiao, A. H. Rose, K. Zhu, and M. C. Beard, “Indi- vidual electron and hole mobilities in lead-halide perovskites revealed by noncontact methods,” *ACS Energy Letters*, vol. 5, no. 1, pp. 47–55, 2019.

S21

[30]D. Bi, W. Tress, M. I. Dar, P. Gao, J. Luo, C. Renevier, K. Schenk, A. Abate,

F. Giordano, J.-P. Correa Baena *et al.*, “Efficient luminescent solar cells based on tailored mixed-cation perovskites,” *Science advances*, vol. 2, no. 1, p. e1501170, 2016.
[31]J.-X. Shen, X. Zhang, S. Das, E. Kioupakis, and C. G. Van de Walle, “Unexpect- edly strong auger recombination in halide perovskites,” *Advanced Energy Materials*, vol. 8, no. 30, p. 1801027, 2018.

[32]A. Razzaq, A. Ullah, A. S. Subbiah, and S. De Wolf, “Practical fill factor limits for perovskite solar cells,” *ACS Energy Letters*, vol. 9, no. 11, pp. 5635–5638, 2024.

[33]M. Green, K. Emery, and A. Blakers, “Silicon solar cells with reduced temperature sensitivity,” *Electronics Letters*, vol. 18, no. 2, pp. 97–98, 1982.

[34]J. Zhao, A. Wang, S. Robinson, and M. Green, “Reduced temperature coefficients for recent high-performance silicon solar cells,” *Progress in Photovoltaics: Research* *and Applications*, vol. 2, no. 3, pp. 221–225, 1994.

[35]H. Wang, X. Cheng, and H. Yang, “Temperature coefficients and operating temper- ature verification for passivated emitter and rear cell bifacial silicon solar module,” *IEEE Journal of Photovoltaics*, vol. 10, no. 3, pp. 729–739, 2020.

[36]P.-J. Ribeyron, “Crystalline silicon solar cells: Better than ever,” *Nature Energy*, vol. 2, no. 5, pp. 1–2, 2017.

[37]J. Liu, Y. He, L. Ding, H. Zhang, Q. Li, L. Jia, J. Yu, T. W. Lau, M. Li, Y. Qin *et al.*, “Perovskite/silicon tandem solar cells with bilayer interface passivation,” *Nature*, vol. 635, no. 8039, pp. 596–603, 2024.

[38]E. K¨ohnen, M. Joˇst, A. B. Morales-Vilches, P. Tockhorn, A. Al-Ashouri, B. Macco,

L. Kegelmann, L. Korte, B. Rech, R. Schlatmann *et al.*, “Highly efficient monolithic perovskite silicon tandem solar cells: analyzing the influence of current mismatch on device performance,” *Sustainable Energy & Fuels*, vol. 3, no. 8, pp. 1995–2005, 2019.
[39]Q. Xu, B. Shi, Y. Li, L. Yan, W. Duan, Y. Li, R. Li, N. Ren, W. Han, J. Liu *et al.*, “Conductive passivator for efficient monolithic perovskite/silicon tandem solar cell on commercially textured silicon,” *Advanced Energy Materials*, vol. 12, no. 46, p. 2202404, 2022.

[40]F. Sahli, J. Werner, B. A. Kamino, M. Br¨auninger, R. Monnard, B. Paviet-Salomon,

L. Barraud, L. Ding, J. J. Diaz Leon, D. Sacchetto *et al.*, “Fully textured monolithic perovskite/silicon tandem solar cells with 25.2% power conversion efficiency,” *Nature* *materials*, vol. 17, no. 9, pp. 820–826, 2018.
[41]G. Yang, Z. Ni, Z. J. Yu, B. W. Larson, Z. Yu, B. Chen, A. Alasfour, X. Xiao, J. M. Luther, Z. C. Holman *et al.*, “Defect engineering in wide-bandgap perovskites for efficient perovskite–silicon tandem solar cells,” *Nature Photonics*, vol. 16, no. 8, pp. 588–594, 2022.

[42]P. Tockhorn, J. Sutter, A. Cruz, P. Wagner, K. J¨ager, D. Yoo, F. Lang, M. Grischek,

B. Li, J. Li *et al.*, “Nano-optical designs for high-efficiency monolithic perovskite– silicon tandem solar cells,” *Nature Nanotechnology*, vol. 17, no. 11, pp. 1214–1221,
2022.
S22

[43]L. Qiao, T. Ye, T. Wang, W. Kong, R. Sun, L. Zhang, P. Wang, Z. Ge, Y. Peng,

X. Zhang *et al.*, “Freezing halide segregation under intense light for photostable perovskite/silicon tandem solar cells,” *Advanced Energy Materials*, vol. 14, no. 7, p. 2302983, 2024.
[44]E. Aydin, E. Ugur, B. K. Yildirim, T. G. Allen, P. Dally, A. Razzaq, F. Cao,

L. Xu, B. Vishal, A. Yazmaciyan *et al.*, “Enhanced optoelectronic coupling for per- ovskite/silicon tandem solar cells,” *Nature*, vol. 623, no. 7988, pp. 732–738, 2023.
[45]X. Y. Chin, D. Turkay, J. A. Steele, S. Tabean, S. Eswara, M. Mensi, P. Fiala, C. M. Wolff, A. Paracchino, K. Artuk *et al.*, “Interface passivation for 31.25%-efficient perovskite/silicon tandem solar cells,” *Science*, vol. 381, no. 6653, pp. 59–63, 2023.

[46]M. Sengupta, Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby, “The national solar radiation data base,” *Renewable and sustainable energy reviews*, vol. 89, pp. 51–60, 2018.

[47]J. A. Kratochvil, W. E. Boyson, and D. L. King, “Photovoltaic array performance model.” Sandia National Laboratories (SNL), Albuquerque, NM, and Livermore, CA..., Tech. Rep., 2004.

[48]J. Roy, “Comprehensive analysis and modeling of cell to module (ctm) conversion loss during c-si solar photovoltaic (spv) module manufacturing,” *Solar Energy*, vol. 130, pp. 184–192, 2016.

[49]C. Ballif, F.-J. Haug, M. Boccard, P. J. Verlinden, and G. Hahn, “Status and perspec- tives of crystalline silicon photovoltaics in research and industry,” *Nature Reviews* *Materials*, vol. 7, no. 8, pp. 597–616, 2022.

[50]K. Hossain, D. Sivadas, D. Kabra, and P. R. Nair, “Perovskite solar cells dominated by bimolecular recombination how far is the radiative limit?” *ACS Energy Letters*, vol. 9, no. 5, pp. 2310–2317, 2024.

[51]M. T. Patel, R. Asadpour, M. Woodhouse, C. Deline, and M. A. Alam, “Lcoe*: Re- thinking lcoe for photovoltaic systems,” in *2019 IEEE 46th Photovoltaic Specialists* *Conference (PVSC)*. IEEE, 2019, pp. 1711–1713.

[52]L. A. Zafoschnig, S. Nold, and J. C. Goldschmidt, “The race for lowest costs of electricity production: techno-economic analysis of silicon, perovskite and tandem solar cells,” *IEEE Journal of Photovoltaics*, vol. 10, no. 6, pp. 1632–1641, 2020.

S23
