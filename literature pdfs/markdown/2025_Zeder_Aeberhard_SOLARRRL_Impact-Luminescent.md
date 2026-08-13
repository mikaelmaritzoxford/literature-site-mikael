## Solar RRL

## RESEARCH ARTICLE

# Impact of Luminescent Coupling on Perovskite-Silicon Tandem External Quantum Efficiency Quantified by

# Comprehensive Opto-Electronic Simulation

2,3 Simon J. Zeder¹ | Tabea Krucker | Davide Moia¹ | Sandra Jenatsch¹ | Kerem Artuk³ | Christian Wolff³ | 1,4 1,2 Christophe Ballif³ | Beat Ruhstaller | Urs Aeberhard

1 2 3 Fluxim AG, Winterthur, Switzerland | ZHAW, Institute of Computational Physics, Winterthur, Switzerland | EPFL, PV-Lab, Institute of Electronic and 4 ETH Zürich, Department Information Technology & Electrical Engineering, Integrated Systems Laboratory, Microengineering, Neuchâtel, Switzerland | Zürich, Switzerland

Correspondence: Urs Aeberhard (uaeberhard@ethz.ch)

| Accepted: 17 November 2025 Received: 12 October 2025 | Revised: 5 November 2025

Keywords: drift-diffusion | luminescent coupling | mobile ions | perovskite-silicon tandem | photon recycling

ABSTRACT In this work, the effects of luminescent coupling (LC) on the external quantum efficiency (EQE) of perovskite-silicon tandem (PST) solar cells are quantified by means of monochromatic transient photocurrent measurements and comprehensive optoelec- tronic simulations that take into account both optical and electrical coupling of the subcells. It is shown that, at short wavelengths, a similar response results from both LC and silicon bottom-cell shunts. The two contributions can be discriminated and quantified based on bias voltage and light intensity-dependent measurements. Such measurements were conducted on state-of-the-art PST cells and agree well with the behavior predicted by the simulations. For the case of polychromatic EQE simulations, a quenching of the LC effects with decreasing concentration of mobile ions is found, which is explained in terms of ion-modulated recombi- nation via bulk defects.

## 1 | Introduction

With single-junction cells approaching their practical efficiency limits, research is increasingly focusing on multijunction approaches [1, 2]. A promising technology is the perovskite- silicon tandem (PST) solar cell, now reaching power conversion efficiencies of >35% [3]. As the perovskite top cell operates ever closer to the radiative limit, luminescent coupling (LC) effects (bottom cell reabsorption of photons that are emitted in the top cell; cf. Figure 1a) become increasingly important to consider, such as the beneficial impact on current matching in bottom- limited tandems [4–6]. Although these effects are generally beneficial in the context of solar cell operation, the additional energy-transfer pathway by optical means can, however, compli- cate the interpretation of certain characterization experiments. One important measurement, which is highly affected by LC, is the evaluation of subcell external quantum efficiencies

(EQE), as LC breaks the assumption of pure electronic coupling through the recombination junction [7]. While this problem has attracted a great deal of interest in the III–V multijunction solar cell community [8–14], it is less explored in perovskite-based tan- dems. Furthermore, PSTs pose additional challenges when deter- mining the subcell EQE, such as the presence of mobile ions in the perovskite [15].

The effects of LC are conventionally expressed via a LC efficiency η LCthat relates the additional photocurrent in the bottom cell due to LC to the radiative recombination current in the top cell [16], and which is usually determined as a fit parameter in equivalent circuit (EC) modeling of subcell characteristics [9]. More recently, also experiments with photoreflectance [17], three-terminal devi- ces [18], modulated photocurrent measurements [19], or a combi- nation of intensity-dependent photoluminescence (PL) and photocurrent measurements with absolute photoluminescence

the original work is properly cited. © 2025 The Author(s). Solar RRL published by Wiley-VCH GmbH.

Solar RRL, 2025; e202500823 [https://doi.org/10.1002/solr.202500823](https://doi.org/10.1002/solr.202500823) 1of9

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided

2367198x, 0, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/solr.202500823](https://onlinelibrary.wiley.com/doi/10.1002/solr.202500823) by University Of Oxford, Wiley Online Library on [09/12/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

(a)
(b)
(a) Schematic representation of the backside-textured PST solar cell device stack layout and of the reabsorption processes for photons
FIGURE 1 |

emitted by the perovskite absorber. (b) The EC describing the idealized electronic transport model. The lumped current source consists of three current sources for generation due to external sources, PR, and LC. The lumped recombination diode includes radiative, Shockley–Read–Hall (SRH), and Auger recombination. LC and PR are dependent current sources, interacting with the radiative recombination diode as depicted by the dashed arrows.

quantum yield (PLQY) [7] have been used to assess this quantity. The main contribution to the LC efficiency, the optical transfer from top to bottom cell, has been approximated using optical mod- els ranging from ray-optical estimates in thick absorbers [20]to transfer-matrix-method (TMM) approaches in thin films [21]or a combination of ray-tracing with TMM [6].

Here, the quantification and analysis of LC effects in PST solar cells are addressed using a comprehensive opto-electronic simula- tion framework. At the core of the approach lies a consistent and rigorous optical model for absorption and luminescence in solar cell devices under consideration of coherent and incoherent pho- ton propagation including scattering at interface textures [22]. The results are fed to electrical models ranging from simplified ECs [23] to a full-fledged drift-diffusion charge transport framework including mobile ion physics at steady state [24] and in transient mode [25, 26]. The optical model provides local absorption, emis- sion, and reabsorption rates throughout the device. These rates act as source/sink terms in the electronic model, allowing for a con- sistent treatment of both photon recycling (PR) and LC contribu- tions under arbitrary optical and electrical bias. Fitting this model to measured EQE data from state-of-the-art PST solar cells fabri- catedatEPFLPV-Lab[27, 28] as a function of illumination inten- sity or bias voltage then allows us to identify and separate the various mechanisms responsible for the observed behavior. Most importantly, the model enables discrimination between contribu- tions to the short-wavelength response that are due to either LC or low shunt resistance in the bottom cell [8, 12, 29].

The article is organized as follows. In Section 2, details on the mul- tiscale simulation approach are provided. The intensity- and bias- dependent EQE measurement procedure is reported in Section 3, and the results of both are compared and analyzed in Section 4.

[30] describes emission, reabsorption, and coherent propagation within the thin films. It is fully compatible with local and global detailed balance and is free from unphysical divergence in the dipole power emitted within the absorbing media. This picture is coupled to a net-radiation type optical model for emission, reabsorption, and incoherent propagation in optically thick media, such as the Si absorber, where additionally incoherent light scattering can be taken into account [22]. In addition to the photogeneration rate Gextdue to external irradiation with photon flux ϕext, numerical evaluation of the coupled models provides the normalized profile of local internal emission Rem,0and reabsorption Greabs,0as well as the local photon flux S₀ due to internal emission, which needs to be scaled using the local quasi-Fermi level splitting (QFLS) ΔF. The latter is pro- vided by the electronic transport model and constitutes the elec- tronic to optical coupling. Explicit expressions of the internal rates as a function of the Green tensor can be found in Ref. [23]. The profiles of local emission and reabsorption rates, as well as the photon energy flux associated with propagating modes originating from internal emission in the stack displayed in

Figure 1a, are given in Figure 2a,b, respectively. The local rates

reveal not only signs of coherent emission in the perovskite, but also significant reabsorption in the top cell, while the Poynting vector shows a strong asymmetry favouring coupling of light to the silicon bottom cell over out-coupling at the top. As shown in

Figure 2c, PR dominates over LC in this case. LC amounts to 36%

of the photons emitted by the top cell, which is very close to the LC efficiency of 35% found experimentally in [7] for a very simi- lar structure with large ratio of bottom to top emission. However, in [7], the LC efficiency includes also nonradiative losses via the radiative efficiency as a factor in PLQY.

To go beyond optics and capture the impact of electronic losses on the extraction of photogenerated charge carriers, two approaches of different rigor are considered. The most general case is covered by a drift-diffusion-Poisson model to properly take into account any nonidealities in terms of electronic transport, as well as mobile ions, in steady-state, transient, and small-signal AC regimes [24]as implemented in the device simulation tool SETFOS [31]. In this

Solar RRL, 2025

## | Simulation Approach

The multiscale optical model used consists of two coupled com- ponents: a recently developed dyadic Green tensor formalism

2of9

(a) <u>(b)</u>
(c)
Optical assessment of quantities related to internal emission: (a) Profiles of emission and reabsorption rates (to be scaled by the

FIGURE 2 |

Boltzmann factor with the QFLS). (b) Poynting vector of propagating modes from internal emission, showing a dominant coupling of light to the silicon bottom cell. (c) In this device, PR dominates over LC, while the shares of outcoupling and parasitic absorption are marginal.

context, the optical to electronic coupling enters the equations through radiative recombination (emission) and secondary photo- generation (reabsorption) rates in the continuity equations for electrons and holes. Similar combinations of optical and charge transport models have been used previously to address LC in III–V multijunction solar cells [32–34], albeit with less rigor regarding the consideration of the optical density of states in the emission and the impact of longitudinal modes, and without light scattering. On the other hand, the advanced optical model can also be used to parametrize the LC term in a simplified EC approach which is suitable for extensive parameter studies to obtain qualitative insight and for the fitting of experimental data. The generation currents in the EC scheme shown in Figure 1b include the photocurrents due to external illumination determined based on the active layer absorptance as well as the nonlinear dependent current sources for PR and LC, where the optical to electronic coupling enters in the definition of the corresponding saturation current prefactors obtained from the spatial integration of Greabs,0with appropriate choice of source domain

igen iext iPR iLC J = J + J + J, i = top, bot (1)

iext R i J = ηcoldEγA ðEγÞϕextðEγÞ (2)

no iPR i0PR ireabs,0 →i <u>qV</u> i J = J G exp k B T − 1 (3)

no j J iLC = J i0LC G jreabs,0 →i exp k <u>qV</u> B T − 1 (4)

where ηcolis the carrier collection efficiency and V i, i ∈ ftop, botg are the internal subcell voltages. The recombination term con- tains the contributions due to radiative, SRH and Auger recom- bination, which are expressed in the usual way via the respective dark saturation currents and ideality factors

J irec = J irad + J iSRH + J iAug, i = top, bot (5)

no i J i = J i R i exp <u>qV</u> − 1 (6) rad 0rad em kBT

no i J iSRH = J i0SRH exp <u>qV</u> − 1 (7) 2kBT

i i no <u>3qV</u>i J Aug= J0Augexp2kBT− 1 (8)

As compared to the framework presented in Ref. [35], we neglect the current component related to reverse bias breakdown and the subcell voltage-independent LC current related to PL, as both are minor relative contributions at the operating point of the tandem solar cell considered here. Also, the PR and LC saturation cur- rents may contain respective collection efficiencies to enable bridging the optical limit—where transport is idealized and quasi-Fermi levels are flat—and compact models that consider nonradiative losses also at short circuit. With respect to the above optical currents, the LC efficiency is defined as¹

i h j→i i jLC→i J 0LCGreabs,0 η = <u>h i</u> (9) J j R j 0rad em,0

Due to the small overlap of the bottom cell emission spectrum with the top cell absorptance, only η top→bot is evaluated. The total LC current density per subcell then reads

J i = − J igen + J irec + J ish, i = top, bot (10)

where shunt conductance is considered as an additional subcell i current element via the internal parallel resistance Rsh, i ∈ ftop, botg in the form of the shunt currents J ish = V i =R ish. The sub- cell voltages are related to the externally applied bias voltage V and the global series resistance Rsvia

V = V top + V bot + Rs⋅ J (11)

J = J top = J bot(12)

direction (high to low intensities) yielded nearly identical results in Equations (11) and (12) form a nonlinear system of equations for initial tests (see Figure S1b). To ensure homogeneous illumination the subcell voltages as a function of the external illumination ϕext of the active area, a light mixing rod (LMR) is placed between the and the applied bias voltage V, which is solved using a Brentq LED and the PST solar cell. The LMR leads to a slightly higher algorithm, similar to the optical-limit computations in Refs. increase of the EQE at high light intensities (Figure S1c). To fur- [36] and [23]. The model described above is computationally ther verify the EQE trend observed at low light intensities, addi- highly efficient, as the expensive determination of the nonlocal tional measurements were performed using neutral density filters reabsorption rate needs to be performed only once for the param- to reduce the intensity from the LED. The two approaches yielded etrization of the current prefactors related to radiative processes. comparable results (Supporting Information Figure S1d). At very low intensities, the filtered data suggest the formation of a plateau, in agreement with the theoretical prediction for the shunt regime as shown below. 3 | Measurement Procedure

Irradiance-dependent monochromatic EQE was measured on five different PST samples with nominally identical structure as shown in Figure 1a. All measurements were conducted using the Paios system (Fluxim AG) equipped with a blue monochro- matic LED with a peak wavelength at 405 nm. The PST solar cells used in this study were provided by EPFL PV-Lab, Neuchâtel. EQE was determined via transient photocurrent (TPC) measure- ments at constant applied bias voltage. A sequence of 405 nm LED light pulses with varying intensities (from low to high and reverse) was applied to the devices. The TPC signal of the measured samples is shown in Figure 3a for the case of maximum irradiance (751 W/m²) and vanishing applied voltage: Each light pulse lasted for 1 s and was preceded by a settling time of 5 s and followed by a recover time of 1 s. The current response was con- tinuously recorded throughout the entire sequence. To minimize external light exposure, the device was covered with a black lid and the entire setup was additionally enclosed with a black towel.

In the raw data, it can be observed that during the light pulse (especially at high intensities) a steady state is not reached within the 1s of illumination. This can be verified in Figure 3b that dis- plays the signal under varying irradiance for a single sample. Consequently, the results might indicate features in the EQE sim- ply because the cells do not reach a quasi-steady state during the measurements. To rule out this possibility, extended measure- ments with a light pulse duration of 100 s were conducted, and the currents were extracted from different time windows within the pulse. The results show that although a steady state is still not reached, the observed EQE behavior remains consis- tent (Supporting Information Figure S1a).

The full set of measurements was performed only in the forward direction (that is, from low to high light intensities), as the reverse

(a)
## 4 | Results and Discussion

It is common to assume that the short-circuit current density (JSC) of a tandem solar cell is given by the minimum of both sub- cell JSC’s due to the exclusively electronic series connection through the recombination junction: Any excess optical genera- tion in one of the two subcells is dissipated through local recom- bination and hence is lost. This assumption results in a spectral EQE (if no bias light is applied) that is given by the minimum of the subcell absorptances (assuming unity internal quantum effi- ciency). These are shown in Figure 4a with dashed (perovskite subcell) and dash-dotted (silicon subcell) grey lines, respectively. In the figure, this minimum is highlighted by thick black lines. For a highly luminescent top cell—, i.e., considering increasing values of internal radiative efficiency ηrad—however, LC leads to a finite EQE signal at short wavelengths, as the perovskite acts effectively as a down-converter. Dissipation of the excess gener- ation in the top cell through radiative recombination generates photons that are reabsorbed in the Si bottom cell, which results in optical generation and, hence, a secondary photocurrent. In this situation, where an incident photon absorbed in the top cell needs to generate currents in both subcells the EQE is bounded by half of the top-cell EQE (absorptance) in the limit where no emission is lost due to out-coupling at the front. Since the mag- nitude of the internal emission rate depends exponentially on the top-cell voltage, PR—which increases the local QFLS—boosts the LC signal, as can also be verified in Figure 4a, where the sub- stantially reduced EQE without PR (i.e., without secondary pho- togeneration due to reabsorption in the perovskite) is indicated with dotted lines. To assess the accuracy of the EC model, full

(b)
FIGURE 3 |

current signal under illumination with varying irradiance.

(a) Determination of the monochromatic tandem EQE via transient photocurrent measurements using the all-in-one solar cell char-
acterization platform PAIOS. The relevant signal is extracted from the last 0.2 s under illumination where the current has stabilized. (b) Transient

(c)
(a) (b)
(a) Spectral tandem EQE response under monochromatic illumination as simulated with the EC model as a function of radiative
FIGURE 4 |

efficiency. Without LC or bottom cell shunts this is given by the minimum of the absorptances, min(A pero, ASi), shown as thick black curves. The LC signal without PR is strongly reduced (dotted lines). (b) The EC model agrees closely with the full DD results for the limit of zero reabsorption (black filled diamonds) and the radiative limit (green filled circles), and nonradiative losses (red filled squares) are well reproduced by a lower radiative efficiency in the top cell. (c) Same as (a), but for the case of a reduced bottom cell shunt resistance.

drift-diffusion (DD) simulations were performed for the situation considered here. As shown in Figure 4b, both the limit of vanish- ing reabsorption (black diamonds) and the radiative limit (green circles) are perfectly reproduced by the simplified model without transport. Even the DD result for finite LC and nonradiative losses (red squares) can be reproduced remarkably well just by reducing the radiative efficiency in the top cell, which justifies the assumption of unit carrier collection efficiency made in the EC model.

Importantly, a similar signal can result from bottom cell shunt currents, depicted in Figure 4c, as the top cell excess generation does not need to recombine with any bottom-cell charges, and instead flows directly through the ohmic connection. In this case, the top-cell contribution to the bottom-cell EQE is bounded by the top-cell absorptance. However, as evident from their expres- sions in the EC model, these two contributions to the monochro- matic bottom cell EQE exhibit strongly differing subcell voltage dependencies, with the shunt current being proportional to the bot- tom cell voltage, Jsh∝ Vbot, and the LC current proportional to the radiative recombination in the top cell, JLC∝ exp ½qVtop=ðkBTÞ.

|||top,∗ top|top|
|---|---|---|---|
|||0rad 0rad||

By employing a variational approach, such as illumination inten- sity or bias voltage applied to the tandem, the two contributions can hencebedistinguished.

Application of the optical model, coupled to the simplified EC model, allows for a prediction of the expected behavior for the PST solar cell device considered, providing a theoretical EQE response as a function of monochromatic (405 nm wavelength) illumination intensity as shown in Figure 5a for the case of the radiative limit. At such short wavelengths it can be assumed that all light is absorbed in the perovskite top cell, as the corre- sponding bottom-cell absorptance vanishes. The EQE is then eval- uated by normalizing the difference of current under illumination and dark current (which vanishes for V = 0 V) to the incident pho- ton flux. Selectively turning on LC and shunt conductance via the radiative efficiency and the bottom-cell shunt resistance, respec- tively, reveals two distinct regimes with respect to the light inten- sity: At high irradiance levels, LC—which does not depend on light intensity in the absence of nonradiative loss channels— dominates, while shunt current starts contributing only towards

low irradiance levels, but eventually dominates the response at the lowest light intensities. Similarly, there is no dependence on exter- nal bias voltage for the LC contribution, while such dependence is pronounced for the shunt contribution, especially at low irradiance, asshowninFigure5b. This can again be understood in terms of the dependence of the photocurrent on subcell voltage: the top-cell voltage governing LC is barely affected in the range of bias voltages applied, whereas the bottom-cell voltage determining the shunt current changes significantly (cf. Supporting Information Figure S2a). To reproduce the measured EQE characteristics— shown are the measurement results for one specific sample as filled triangles—the bottom cell shunt resistance is adjusted (Figure 5c) and the SRH saturation current is increased (Figure 5d), the latter primarily reducing the LC current at lower irradiance. Together, R bot and J top provide already an excellent fit sh 0SRH at low to intermediate light intensity. At high irradiance, however, an overestimation of LC current is found that cannot be removed by increasing bulk SRH recombination without compromising the quality of the fit at lower light intensities. However, if an addi- tional nonradiative loss current with ideality factor close to one is introduced via J top,∗ = J top =IQE top with IQE top < 1, a perfect 0rad 0rad fit is possible. Such an LC-quenching loss term can be attributed to interface recombination [37], which was indeed found to rep- resent a limiting process in high-quality perovskite solar cells and which is also included in the full DD model of the tandem.

The resulting fit of the EQE measurements of different samples using the EC model is shown in Figure 6a: although the differences between the samples are sizable—especially at low irradiance— the individual EQE curves are well reproduced, except for a few data points at very low light intensity, where the measurement accuracy is limited. The parameters obtained from the fit are listed in the Supporting Information in Table S1. Next, the EC model was applied to EQE measurements that were conducted at constant Vbiasvalues ranging from –0.3 to 1.2 V. The results displayed in

Figure 6b confirm that the increase in EQE at high light intensities

is independent of Vbias, suggesting that shunts in the bottom cell are unlikely to be the cause. At lower light intensities, the EQE varies with Vbias, showing a minimum around the VOCof the top cell, which at the lowest intensities is reduced to around 0.85 V

(a) (b)
(c) (d)
FIGURE 5 | Analysis of the monochromatic EQE signal under illumination with photons of 405 nm wavelength: (a) At the radiative limit, con-

tributions from LC do not depend on intensity and dominate at high irradiances, while contributions from low bottom-cell shunt resistance increase strongly at low irradiance. (b) LC is insensitive to bias voltage, whereas shunt contributions show a strong voltage dependence. (c) Increasing shunt resistance shifts the shunt contribution to lower irradiance levels. (d) Defect-mediated (SRH) recombination reduces LC contributions strongly, espe- cially at lower irradiance.

(b)
(a)
FIGURE 6 | Fitting of the monochromatic EQE experiments with the EC model: (a) Reproduction of the data (filled symbols) from different samples

exhibiting a large variation in shunt resistance, but similar LC efficiency. (b) The variation of the shunt contribution to the EQE with bias voltage is reproduced semiquantitatively with the model calibrated at 0 V. The downward bending behavior at maximum voltage can be reproduced with a slight mismatch in the dark current correction (dashed line).

(cf. Supporting Information Figure S2c). Using the EC model for physical processes and of their theoretical description used. this specific sample calibrated at V = 0 V, an almost quantitative Inspecting again the subcell voltages and implied subcell JV curves reproduction of the observed behavior is obtained, which further as a function of applied external voltage reveals that the initial validates the underlying assumptions regarding the dominant decrease of the shunt contribution is directly related to the

## 6of9 Solar RRL, 2025

(a) (b)
FIGURE 7 | Assessment of LC effects in polychromatic EQE measurements of PSTs with full drift-diffusion simulation (at V = 0 V): (a) Subcell EQE

computed using broadband bias light tuned to drive the measured cell into current limitation. The bottom cell EQE shows the expected increase at short wavelengths and decrease at long wavelengths. As in the case without bias light, the limits of vanishing reabsorption and exclusively radiative recom- bination are perfectly reproduced by the EC model (solid lines) in the range of top-cell absorption. However, only the radiative limit agrees fully with DD in the wavelength range of bottom-cell absorption, in the presence of nonradiative losses, these are not fully captured without transport. At reduced concentration of mobile ions, there is a pronounced quenching of the LC signal. (b) Ionic modulation of the radiative and defect-mediated recombination channels explaining the quenching of LC shown in (a).

||||ion 19|− 3|
|---|---|---|---|---|
|||17 − 3|ion|18 − 3|

reduction of the reverse bias on the bottom cell driving the shunt mobile ionic vacancies of N = 10 cm is assumed (red filled current, while the subsequent increase reflects the evolution of the squares). If this is reduced to N = 10 cm (orange squares) currents in the dark and under illumination when the bottom cell and N ion= 10 cm (yellow squares), the effect of LC is reduced is driven into the forward bias regime (Supporting Information in the entire wavelength range. Since the same change in ionic Figure S2(c) and (d)). density does not modify the radiative limit, the effect must be Finally, the model is applied to the more complex case of the attributed to a modified quenching of LC via defects. Indeed, polychromatic EQE measurements (i.e., with bias light to selec-inspection of the recombination rate profiles inside the perov- tively measure individual subcell EQE) mentioned in Section 1, skite (Figure 7b) reveals that in this particular case, a high but now for a PST. Figure 7a shows the subcell EQE as computed concentration of mobile ions leads to strongly reduced SRH using full drift-diffusion simulation (SETFOS) with AM1.5g bias-recombination due to trap saturation in the bulk and boosts radi- light modified with an increment at wavelengths of either 540 nm ative recombination, which provides an intriguing example for (for the top cell, blue bias) or 900 nm (for the bottom cell, NIR the ionic modification of electronic losses [39]. bias) to enforce current limitation by the measured cell. These two spectra give the reference current under the two bias light conditions. The sensing current is computed with the same spec- 5 | Conclusions trum to which a much smaller increment is added at the sensing wavelength that is scanned over the whole range of interest (350– The combined impact of reabsorption effects in state-of-the-art 1150 nm). Without loss of generality with respect to the relevant perovskite silicon solar cells is quantified using a combination features to be investigated, the simulation is performed for a pla-of monochromatic EQE measurements and rigorous opto- nar structure. As for the monochromatic EQE, filled black dia-electronic device simulation based on an advanced treatment monds show the subcell EQEs without reabsorption, while filled of internal emission. The approach provides values for LC effi- circles give the result with PR and LC at the radiative limit. As ciency and top-to-bottom emission ratio that are consistent with expected, the top-cell EQE is not affected by reabsorption effects. previous experimental findings. Intensity and voltage depen- For the bottom cell, the predictions from the EC model are given dence of the EQE measurements are reproduced quantitatively with solid lines and the same color code as before for varying by an equivalent-circuit model including contributions from radiative efficiency. While at the radiative limit, the models agree reabsorption and finite bottom cell shunt resistance and with also in this case, the presence of nonradiative losses leads to dis-effects of bulk and interface recombination. Full drift-diffusion crepancies at wavelengths corresponding to absorption in the simulations reveal that in this particular case, a high concentra- bottom cell. One aspect that is not captured by the EC model, tion of mobile ions amplifies LC effects as radiative processes are but is considered in the DD simulation, is the impact of mobile enhanced due to ionic modification of defect-mediated recombi- ions [38]. In the original calibrated model, a concentration of nation loss.

Solar RRL, 2025 7of9

Acknowledgments The authors acknowledge financial support from the Swiss National Science Foundation via SINERGIA project “RADICALS”, grant no. CRSII5_216647. Open access publishing facilitated by Eidgenossische Technische Hochschule Zurich, as part of the Wiley-Eidgenossische Technische Hochschule Zurich agreement via the Consortium Of Swiss Academic Libraries.

Funding This study was supported by Swiss National Science Foundation(Grant CRSII5_216647).

Conflicts of Interest SJZ, DM, SJ, BR, and UA are employed by the company Fluxim AG that commercializes the simulation software tool SETFOS and the measure- ment setup PAIOS that are used in the study.

Data Availability Statement The data that support the findings of this study are available from the corresponding author upon reasonable request.

Endnotes 1 Sometimes, the LC efficiency is defined wrt the net emission in the top cell, i.e., after subtraction of the fraction reabsorbed in the top cell (PR). In contrast to Ref. [16], the definition used here does not include the ratio of radiative and nonradiative recombination with ideality factor n id= 1, which renders our LC efficiency a purely optical quantity.

References

1. X. Y. Chin, D. Turkay, J. A. Steele, et al., “Interface Passivation for
31.25%-Efficient Perovskite/Silicon Tandem Solar Cells,” Science 381 (2023): 59–63.
2. S. Mariotti, E. Köhnen, F. Scheler, et al., “Interface Engineering for High-Performance, Triple-Halide Perovskite-Silicon Tandem Solar Cells,” Science 381 (2023): 63–69.
3. H. Wu, L. Xie, J. Wei, M. Yu, F. Luo, Y. Liu, X. Tang, Z. Huang, S. Yin,
Q. Tang, F. Peng, J. Duan, F. Ye, Y. Li, Y. Yuan, J. Chen, X. Ru, M. Qu,
J. Wang, M. Yang, J. Lu, C. Xue, L. Fang, X. Xu, Z. Li, all from LONGi Clean Energy, Xi’An, China “Hybrid Interdigitated Back Contact Silicon Solar Cells with Superior Efficiency,” presented at 42nd EU PVSEC Bilbao, (2025).
4. A. Pusch, P. Pearce, and N. J. Ekins-Daukes, “Analytical Expressions for the Efficiency Limits of Radiatively Coupled Tandem Solar Cells,” IEEE Journal of Photovoltaics 9, no. 3 (2019): 679–687.
5. A. R. Bowman, F. Lang, Y.-H. Chiang, et al.,"Relaxed Current Matching Requirements in Highly Luminescent Perovskite Tandem Solar Cells and Their Fundamental Efficiency Limits,"ACS Energy Letters 6 (2021): 612–620.
6. K. Jäger, P. Tillmann, E. A. Katz, and C. Becker, “Perovskite/Silicon Tandem Solar Cells: Effect of Luminescent Coupling and Bifaciality,” Solar RRL 5 (2021): 2000628.
7. K. Nguyen, O. Fischer, C. Messmer, et al., “The Role of Luminescent Coupling in Monolithic Perovskite/Silicon Tandem Solar Cells,” Small 20 (2024): 2403461.
8. J. J. Li, S. H. Lim, C. R. Allen, D. Ding, and Y. H. Zhang, “Combined Effects of Shunt and Luminescence Coupling on External Quantum
Efficiency Measurements of Multijunction Solar Cells,” IEEE Journal of Photovoltaics 1, no. 2 (2011): 225–230.

9. M. A. Steiner, J. F. Geisz, T. E. Moriarty, et al., “Measuring IV Curves and Subcell Photocurrents in the Presence of Luminescent Coupling,” IEEE Journal of Photovoltaics 3, no. 2 (2013): 879–887.
10. J. J. Li and Y. H. Zhang, “Elimination of Artifacts in External Quantum Efficiency Measurements for Multijunction Solar Cells Using a Pulsed Light Bias,” IEEE Journal of Photovoltaics 3, no. 1 (2013): 364–369.
11. S. H. Lim, J.-J. Li, E. H. Steenbergen, and Y.-H. Zhang, “Luminescence Coupling Effects on Multijunction Solar Cell External Quantum Efficiency Measurement,” Progress in Photovoltaics: Research and Applications 21 (2013): 344–350.
12. V. Paraskeva, M. Hadjipanayi, M. Norton, M. Pravettoni, and
G. E. Georghiou, “Voltage and Light Bias Dependent Quantum Efficiency Measurements of GaInP/GaInAs/Ge Triple Junction Devices,” Solar Energy Materials 116 (2013): 55–60.
13. M. Sugai, M. Imaizumi, T. Nakamura, and T. Ohshima, “The effect of luminescence coupling in external quantum efficiency measurement of multi- junction solar cells,” in 2015 IEEE 42nd Photovoltaic Specialist Conference (PVSC) (2015), 1–6, [https://doi.org/10.1109/PVSC.2015.7356075](https://doi.org/10.1109/PVSC.2015.7356075).
14. O. Höhn, P. Schygulla, R. Müller, et al., “Effect of luminescence cou- pling on EQE measurements of high efficiency multi-junction solar cells,” in Proc. SPIE Photonics West 2024, (2024), PC130140C, [https://doi.org/10](https://doi.org/10). 1117/12.3022002.
15.C.Messmer,D.Chojniak,A.J.Bett,etal.,“Toward More Reliable Measurement Procedures of Perovskite-Silicon Tandem Solar Cells: The Role of Transient Device Effects and Measurement Conditions,” Progress in Photovoltaics: Research and Applications 33 (Jan. 2025): 126–142.
16. M. A. Steiner, and J. F. Geisz, “Non-Linear Luminescent Coupling in Series-Connected Multijunction Solar Cells,” Applied Physics Letters 100 (2012): 251106.
17. D. Fuertes Marrón, E. Barrigón, M. Ochoa, and I. Artacho, “Quantitative Determination of Luminescent Coupling in Multijunction Solar Cells from Spectral Photovoltage Measurements,” Physical Review Applied 6 (2016): 014001.
18. T. Tayagaki, K. Makita, R. Oshima, H. Mizuno, and T. Sugaya, “Analysis of Luminescence Coupling Effect in Three-Terminal Tandem Solar Cells,” Journal of Photonics for Energy 8 (2018): 045503.
19. N. Márquez Peraca, P. M. Haney, and B. H. Hamadani, “The Effect of Luminescent Coupling on Modulated Photocurrent Measurements in Multijunction Solar Cells,” Applied Physics Letters 115 (2019): 083506.
20. M. A. Steiner, J. F. Geisz, I. García, et al., “Effects of Internal Luminescence and Internal Optics on Vocand Jscof III–V Solar Cells,” IEEE Journal of Photovoltaics 3, no. 4 (2013): 1437–1442.
21. V. M. Emelyanov, E. D. Filimonov, S. A. Kozhukhovskaia,
M. A. Mintairov, and M. Z. Shvarts, “Simulation of the Photo-Luminescent Coupling Transfer Function in Multijunction Nanoheterostructure Solar Cells,” AIP Conference Proceedings 1748 (2016): 050001.
22. S. J. Zeder, B. Blülle, B. Ruhstaller, and U. Aeberhard, “Optical Multiscale Model for Quantification of Photon Recycling including Incoherent Light Scattering,” Optics Express 32 (2024): 34154–34171.
23. S. J. Zeder, B. Blülle, B. Ruhstaller, and U. Aeberhard, “Optimizing Perovskite LEDs and Tandem PV Cells: The Role of Photon-Recycling and Luminescent Coupling in Presence of Strong Light Scattering,” APL Energy 3 (2025): 026110.
24. S. Zeder, B. Ruhstaller, and U. Aeberhard, “Assessment of Photon Recycling in Perovskite Solar Cells by Fully Coupled Optoelectronic Simulation,” Physical Review Applied 17 (2022): 014023.
25. S. Zeder, B. Ruhstaller, and U. Aeberhard, “Fully-coupled opto-electronic simulation of transient photoluminescence in perovskite-based cell structures

including photon recycling in a full wave picture,” in 13th International Conference on Hybrid and Organic Photovoltaics (HOPV), (2021), [https://doi.org/10.29363/nanoge.hopv.2022.086](https://doi.org/10.29363/nanoge.hopv.2022.086).

26. S. J. Zeder, U. Aeberhard, B. Ruhstaller, and W. Tress, “18 - Photon Recycling in Metal Halide Perovskites: Its Modeling and Relevance to Optoelectronic Devices, Metal Halide Perovskites for Generation, Manipulation and Detection of Light, ed. J. P. Martínez-Pastor,
P. P. Boix and G. Xing (Elsevier, 2023).507–545, Photonic Materials and Applications.
27. D. Turkay, K. Artuk, X.-Y. Chin, et al., “Synergetic Substrate and Additive Engineering for over 30%-efficient Perovskite-si Tandem Solar Cells,” Joule, 8 (2024): 1735–1753.
28. K. Artuk, A. Oranskaia, D. Turkay, et al., “60 cm² Perovskite-Silicon Tandem Solar Cells with an Efficiency of 28.9% by homogeneous Passivation,” Nature Communications 16, no. 1 (2025): 8672.
29. M. Meusel, C. Baur, G. Létay, A. W. Bett, W. Warta, and E. Fernandez, “Spectral Response Measurements of Monolithic GaInP/Ga(In)As/Ge Triple-Junction Solar Cells: Measurement Artifacts and Their Explanation,” Progress in Photovoltaics: Research and Applications 11 (2003): 499–514.
30. U. Aeberhard, S. Zeder, and B. Ruhstaller, “Reconciliation of Dipole Emission with Detailed Balance Rates for the Simulation of Luminescence and Photon Recycling in Perovskite Solar Cells,” Optics Express 29 (2021): 14773–14788.
31. Fluxim AG, Setfos v5512, [https://www.fluxim.com/setfos](https://www.fluxim.com/setfos), (Accessed: August, 2025).
32. A. W. Walker, O. Höhn, D. N. Micha, et al., “Impact of Photon Recycling and Luminescence Coupling on III–V Single and Dual Junction Photovoltaic Devices,” Journal of Photonics for Energy 5, no. 1 (2015): 1–11.
33. M. Wilkins, C. E. Valdivia, A. M. Gabr, D. Masson, S. Fafard, and
K. Hinzer, “Luminescent Coupling in Planar Opto-Electronic Devices,” Journal of Applied Physics 118 (2015): 143102.
34. Z. Ren, J. P. Mailoa, Z. Liu, et al., “Numerical Analysis of Radiative Recombination and Reabsorption in GaAs/Si Tandem,” IEEE Journal of Photovoltaics 5, no. 4 (2015): 1079–1086.
35. J. F. Geisz, M. A. Steiner, I. García, et al., “Generalized Optoelectronic Model of Series-Connected Multijunction Solar Cells,” IEEE Journal of Photovoltaics 5, no. 6 (2015): 1827–1839.
36. U. Aeberhard, S. J. Zeder, and B. Ruhstaller, “Effects of Photon Recycling and Luminescent Coupling in All-Perovskite Tandem Solar Cells Assessed by Full Opto-Electronic Simulation,” Solar RRL 8 (2024): 2400264.
37. O. J. Sandberg, M. Kumar, M. Stolterfoht, D. Neher, and A. Armin, “Analytical Model for Interface Recombination Limited Ideality Factors in p-i-n Perovskite Solar Cells,” APL Energy 3 (2025): 036107.
(after 10/30/60/90 s). (b) Invariance of the monochromatic EQE with respect to the intensity ramp order (forward: low to high intensity).

(c) Impact of the light mixing rod on the monochromatic EQE measure- ment. (d) Measurements with different EQE to lower irradiance, but do not modify the intensity dependence.
neutral density filters shift the

Supporting Fig. 2: (a) Dependence of the internal subcell voltages on externally applied bias voltage as obtained at the radiative limit of the EC model for the intensity-dependent monochromatic EQE displayed in Fig. 5(b) of the main text. Shown are the values for an intensity of

0.01 suns. While the top-cell voltage governing the LC contribution in the absence of bottom cell shunts (blue solid line) does not vary with applied voltage, the bottom-cell voltage governing the shunt current in the absence of LC (red dash-dotted line) varies linearly with voltage.
(b) Subcell voltages for the fit of the experimental EQE curves shown in Fig. 6(b) of the main text. The subcell voltages are shown for the lowest intensity of the monochromatic illumination, where the shunt contribu- tions are strongest. (c) Subcell current-voltage characteristics at lowest irradiance, for the sensing light (solid lines) and in the dark (dashed lines). (d) Excess current generated by the sensing light as a function of externally applied voltage, exhibiting a minimum close to the VOC of the top cell. Supporting Table 1: Parameters of the EC model obtained from the fit of the monochromatic EQE measurements for the different perovskite-silicon tandem samples. The IQE
top parameter is introduced to reproduce the interface recombination by enhancing the n =1 recombination current via multiplication of the corresponding saturation current by 1/IQE id top.

|38. M. T.|Neukom, A.|Schiller, S. Züfle,|et al.,|“Consistent|Device|
|---|---|---|---|---|---|
|Simulation|Model Describing|Perovskite|Solar Cells|in Steady-State,||
|Transient, Interfaces 11 (2019): 23320–23328.|and Frequency|Domain,”|ACS Applied|Materials|&|
|39. D.|Moia, “Equivalent-Circuit||Modeling|of Electron-Hole||
|Recombination|in Semiconductors||and Mixed|Ionic-Electronic||

Conductors,” Physical Review Applied 23 (2025): 014055.

Supporting Information Additional supporting information can be found online in the Supporting Information Section. Details on the experimental procedure for the monochromatic EQE measurement, subcell voltages and current-voltage characteristics as obtained from the EC model, EC fitting parameters for the monochromatic EQE measurements. Supporting Fig. 1: (a) Independence of the monochromatic EQE from the exact position of the 0.2 second data extraction window within the pulse of 100 s duration
