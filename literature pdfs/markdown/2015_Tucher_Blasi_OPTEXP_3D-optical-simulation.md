# 3D optical simulation formalism OPTOS for textured silicon solar cells

### Nico Tucher,

**1,5,*** **Johannes Eisenlohr,** **1,4,5** **Peter Kiefel,** **1** **Oliver Höhn,** **1** **Hubert Hauser,** **1**

### Marius Peters,

**2** **Claas Müller,** **3** **Jan Christoph Goldschmidt,** **1 and Benedikt Bläsi¹** *1* *Fraunhofer Institute for Solar Energy Systems ISE, Heidenhofstr. 2, 79110 Freiburg, Germany* *2* *Massachusetts Institute of Technology, Department of Mechanical Engineering, 77 Massachusetts Avenue,* *Cambridge, MA 02139, USA* *3* *Albert-Ludwigs-University, IMTEK Laboratory for Process Technology, Georges-Köhler-Allee 103, 79110* *Freiburg, Germany* *4* *johannes.eisenlohr@ise.fraunhofer.de* *5* *These authors contributed equally to this work.* * *nico.tucher@ise.fraunhofer.de*

**Abstract** In this paper we introduce the three-dimensional formulation of the OPTOS formalism, a matrix-based method that allows for the efficient simulation of non-coherent light propagation and absorption in thick textured sheets. As application examples, we calculate the absorptance of solar cells featuring textures on front and rear side with different feature sizes operating in different optical regimes. A discretization of polar and azimuth angle enables a three-dimensional description of systems with arbitrary surface textures. We present redistribution matrices for 3D surface textures, including pyramidal textures, binary crossed gratings and a Lambertian scatterer. The results of the OPTOS simulations for silicon sheets with different combinations of these surfaces are in accordance with both optical measurements and results based on established simulation methods like ray tracing. Using OPTOS, we show that the integration of a diffractive grating at the rear side of a silicon solar cell featuring a pyramidal front side results in absorption close to the Yablonovitch Limit enhancing the photocurrent density by 0.6 mA/cm² for a 200 µm thick cell. ©2015 Optical Society of America **OCIS codes:** (040.5350) Photovoltaic; (050.1950) Diffraction gratings; (080.1753) Computation methods.

### References and links

1. R. Brendel, “Sunrays. A versatile ray tracing program for the photovoltaic community,” in *Proceedings of the* *12th European Photovoltaic Solar Energy Conference 1994*, pp. 1339–1342.
2. S. C. Baker-Finch and K. R. McIntosh, “Reflection of normally incident light from silicon solar cells with pyramidal texture,” Prog. Photovolt. Res. Appl. **19**(4), 406–416 (2011).
3. S. C. Baker-Finch, K. R. McIntosh, and M. L. Terry, “Isotextured silicon solar cell analysis and modeling 1. optics,” IEEE J. Photovolt. **2**(4), 457–464 (2012).
4. P. Sheng, “Wavelength-selective absorption enhancement in thin-film solar cells,” Appl. Phys. Lett. **43**(6), 579 (1983).
5. C. Heine and R. H. Morf, “Submicrometer gratings for solar energy applications,” Appl. Opt. **34**(14), 2476–2482 (1995).
6. M. Peters, M. Rüdiger, H. Hauser, M. Hermle, and B. Bläsi, “Diffractive gratings for crystalline silicon solar cells—optimum parameters and loss mechanisms,” Prog. Photovolt. Res. Appl. **20**(7), 862–873 (2012).
7. H. Hauser, A. Mellor, A. Guttowski, C. Wellens, J. Benick, C. Müller, M. Hermle, and B. Bläsi, “Diffractive backside structures via nanoimprint lithography,” Energy Procedia **27**, 337–342 (2012).
8. A. Mellor, H. Hauser, C. Wellens, J. Benick, J. Eisenlohr, M. Peters, A. Guttowski, I. Tobías, A. Martí, A. Luque, and B. Bläsi, “Nanoimprinted diffraction gratings for crystalline silicon solar cells: implementation, characterization and simulation,” Opt. Express **21**(S2 Suppl 2), A295–A304 (2013).
9. K. Yee, “Numerical solution of initial boundary value problems involving maxwell’s equations in isotropic media,” IEEE Trans. Antenn. Propag. **14**(3), 302–307 (1966).

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

OSA Nov 23, | OPTICS EXPRESS A1720

10. A. Taflove and S. C. Hagness, *Computational electrodynamics. The Finite-Difference Time-Domain Method*, 3rd (Artech House, 2005).
11. M. G. Moharam, E. B. Grann, D. A. Pommet, and T. K. Gaylord, “Formulation for stable and efficient implementation of the rigorous coupled-wave analysis of binary gratings,” J. Opt. Soc. Am. A **12**(5), 1068–1076 (1995).
12. L. Li, “New formulation of the fourier modal method for crossed surface-relief gratings,” J. Opt. Soc. Am. A **14**(10), 2758–2767 (1997).
13. J. Eisenlohr, N. Tucher, O. Höhn, H. Hauser, M. Peters, P. Kiefel, J. C. Goldschmidt, and B. Bläsi, “Matrix formalism for light propagation and absorption in thick textured optical sheets,” Opt. Express **23**(11), A502– A518 (2015).
14. A. Mellor, I. Tobias, A. Marti, and A. Luque, “A numerical study of bi-periodic binary diffraction gratings for solar cell applications,” Sol. Energy Mater. Sol. Cells **95**(12), 3527–3535 (2011).
15. A. Mellor, I. Tobias, A. Marti, M. J. Mendes, and A. Luque, “Upper limits to absorption enhancement in thick solar cells using diffraction gratings,” Prog. Photovolt. Res. Appl. **19**(6), 676–687 (2011).
16. R. Rothemund, T. Umundum, G. Meinhardt, K. Hingerl, T. Fromherz, and W. Jantsch, “Light trapping in pyramidally textured crystalline silicon solar cells using back-side diffractive gratings,” Prog. Photovolt. Res. Appl. **21**, 747–753 (2012).
17. A. K. Chu, J. S. Wang, Z. Y. Tsai, and C. K. Lee, “A simple and cost-effective approach for fabricating pyramids on crystalline silicon wafers,” Sol. Energy Mater. Sol. Cells **93**(8), 1276–1280 (2009).
18. A. Goetzberger, “Optical confinement in thin Si-solar cells by diffuse back reflectors,” in *Proceedings of the* *15th IEEE Photovoltaic Specialists Conference* (1981), pp. 867–870.
19. J. Eisenlohr, B. G. Lee, J. Benick, F. Feldmann, M. Drießen, N. Milenkovic, B. Bläsi, J. C. Goldschmidt, and M. Hermle, “Rear side sphere gratings for improved light trapping in crystalline silicon single junction and silicon- based tandem solar cells,” Sol. Energy Mater. Sol. Cells **142**, 60–65 (2015).
20. N. Tucher, J. Eisenlohr, H. Hauser, J. Benick, M. Graf, C. Müller, M. Hermle, J. C. Goldschmidt, and B. Bläsi, “Crystalline silicon solar cells with enhanced light trapping via rear side diffraction grating,” Energy Procedia **77**, 253–262 (2015).
21. E. Yablonovitch, “Statistical ray optics,” J. Opt. Soc. Am. **72**(7), 899–907 (1982).
22. C. Leiner, W. Nemitz, S. Schweitzer, F. P. Wenzl, P. Hartmann, U. Hohenester, and C. Sommer, “Multiple interfacing between classical ray-tracing and wave-optical simulation approaches: a study on applicability and accuracy,” Opt. Express **22**(13), 16048–16060 (2014).
23. R. Branke and A. Heimsath, “Raytrace3D power tower-a novel optical model for central receiver systems,” in *SolarPACES 2010, 16th Solar Power And Chemical Energy Systems International Symposium* (2010).
24. P. Lalanne and M. P. Jurek, “Computation of the near-field pattern with the coupled-wave method for transverse magnetic polarization,” J. Mod. Opt. **45**(7), 1357–1374 (1998).
25. J. P. Hugonin and P. Lalanne, “Reticolo code 2D for the diffraction by stacks of lamellar 2D crossed gratings,” Institut d'Optique, Plaiseau, France (2005).
26. “PV-Lighthouse,” www.pvlighthouse.com.au.
27. P. Campbell and M. A. Green, “Light trapping properties of pyramidally textured surfaces,” J. Appl. Phys. **62**(1), 243–249 (1987).
28. Gergö Létay (personal communication, 2015).
29. P. A. Basore, “Numerical modeling of textured silicon solar cells using PC-1D,” IEEE Trans. Electron. Dev. **37**(2), 337–343 (1990).
30. S. Baker-Finch and K. R. McIntosh, “One-dimensional photogeneration profiles in silicon solar cells with <u>pyramidal texture,” Prog. Photovolt. Res. Appl. 20, 1–11 (2011).</u>
### 1. Introduction

Surface textures can significantly improve the anti-reflection and light trapping properties of silicon solar cells. Both effects lead to an absorptance enhancement within the absorber material and, thereby, to a potentially higher energy conversion efficiency. There is a variety of techniques for the calculation of optical solar cell properties, which vary in their computational complexity and which have different areas of applicability. Standard textures such as the so called isotexture or pyramidal textures are usually treated with ray optical methods due to the large dimensions compared to the relevant wavelengths [1–3]. For textures with smaller feature sizes, such as diffraction gratings, which also aim at a light trapping enhancement, wave optical effects must be taken into account [4–8]. This can be achieved by wave optical methods such as the finite difference time domain (FDTD) [9,10] or the rigorous coupled wave analysis (RCWA) [11,12]. The OPTOS formalism allows for the efficient, incoherent coupling of arbitrary simulation techniques to calculate “Optical Properties of Textured Optical Sheets” with low computational effort [13]. This is especially relevant for surface structures operating in

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

different optical regimes. Previous matrix-based simulation approaches are restricted to certain structure combinations [14,15]. Ray optical methods can in principle be extended with wave optical techniques via reflectance distribution functions [16]. However, the change of parameters like sheet thickness and angle of incidence or the variation of surface texture combinations always requires a new ray tracing process of the whole system. Using OPTOS, all of those variations can be calculated within seconds once the matrix calculation has been done. A thorough introduction to the two-dimensional formulation of OPTOS and the validation by comparison to other simulation techniques and experimental data was presented in [13]. Many systems, which are relevant to silicon solar cells, can, however, only be described accurately in three dimensions, which implies a higher complexity for the formalism itself and strongly increased computation time, depending on the used simulation methods. This paper introduces the methods and parameters necessary to describe three- dimensional structures in section 2. This is followed by a convergence analysis and a strategy to consider the absorptance within the three-dimensional surface structure. Within the OPTOS formalism, the interaction of light with a surface is described by a redistribution matrix. As these matrixes are highly relevant to the overall formalism, we present redistribution matrices for surface structures of high importance for silicon solar cells in Section 3. These include the matrices for (i) pyramidal textures, which are the industrial standard for the front side of solar cells based on monocrystalline silicon [17], for (ii) a Lambertian scatterer, which has been suggested as rear side light trapping structure already in 1981 [18], and for (iii) a binary crossed grating, as an example for diffractive rear side structures that have recently resulted in efficiency enhancements on solar cell level [19,20]. In Section 4, the formalism is validated by comparing OPTOS absorptance results and generation profiles to results by other techniques and measurement data of various three-dimensional exemplary systems. To demonstrate the ability of the OPTOS formalism to model systems that feature different surface textures with very different feature sizes and thus operate in different optical regime, in Section 5, we apply the formalism to an optical system with a pyramidal front side texture and a diffractive grating and a mirror at the rear side. Such a system approaches the Yablonovitch limit [21] and therefore has the potential for a very high efficiency when applied in a silicon solar cell.

### 2. Methods

*2.1 OPTOS simulation sequence* The working principle of the OPTOS is the same for the 3D as for the 2D formulation, which is described in detail in [13]. Therefore, we present the overall simulation sequence only briefly in this paper. All relevant definitions and formulas are additionally summarised in the appendix. When light impinges on a thick sheet with a textured front and rear surface, every surface interaction leads to a redirection of the light. This means that the corresponding power is distributed into different angles. By dividing the angle space into a discrete number of channels the resulting power distribution inside the sheet can be described by the so called power distribution vector **v**. This vector consists of one entry for every angle channel and polarisation direction while the value represents the power fraction related to the total incoming power. Propagation through an absorbing material reduces the value of the entries of the power distribution vector according to Lambert-Beers law. Reflection or transmission at a textured surface leads to a redistribution of the power between the different angle channels. Both, propagation and redistribution can be described by matrix multiplications of the power distribution vector with a propagation or a redistribution matrix, respectively. Via consecutive

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

multiplications or by using an approach based on the geometric series, optical properties like reflectance, absorptance or transmittance of the textured sheet can be determined [13]. A thorough validation of the OPTOS formalism has already been carried out in two dimensions comparing it to reference simulation techniques and experimental data. Very good agreement has been demonstrated for all investigated systems [13].

*2.2 Three-dimensional angle discretization and system symmetry* In the two-dimensional case, the relevant angle channels could be defined by the polar angle θ only. In three dimensions, also the azimuth angle φ has to be taken into account. These angle parameters allow for changing the direction of the light. However, there is no information concerning the actual position of light-surface interactions within x-y-plane. Thus, OPTOS is not a full 3D-method but it is tailored to sheets, with homogeneous in-plane properties. This will be further discussed for regular and random pyramids in Section 4.b). The size of the polar angle intervals was kept the same as in the 2D-case, with constant sin(θ) intervals between the channel centers. The spacing of the azimuth angles was chosen in a way that again the projection of the angle channels onto the surface plane, which is depicted in Fig. 1, shows nearly equal areas for all channels (aside from the innermost channel and rounding effects).
Fig. 1. Angle discretization for three-dimensional OPTOS calculations. Figure a) shows the
 discretized surface of the three-dimensional half sphere and figure b) its projection onto the surface plane. The channels vary in polar and azimuth angle. The discretization is chosen in a way to exhibit angle channels with equal area and symmetry elements as highlighted in red and depicted in figure b). These symmetry elements can be used to reduce the number of calculations. This discretization leads to a linear relation between the polar angle interval index, *rpolar*, and the associated number of azimuth angle intervals, *Nazimuth*. We call the proportionality constant *cazimuth*.
*Ncrazimuth*=⋅ éê*azimuth polar*ùú (1)

A higher value for *cazimuth* corresponds to a finer discretization. The case depicted in Fig. 1

corresponds to a *cazimuth* of 1. If *cazimuth* is chosen smaller than one, *Nazimuth* is rounded to the next larger integer. In case of *cazimuth* = ¼ this results in one azimuth angle interval for the first four polar angle intervals, and in two azimuth angle intervals for the second four polar angle intervals. The azimuth angle channels associated to one polar angle interval are placed next to each other in our representation of the redistribution matrices **B** and **C** as shown in Eq. (2).

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

æö (,) θϕ11→→ (,) (,) θϕ11θϕ1 2(,) θϕ11K (, ) θ ϕ*nm*→ (,) θϕ11 ç÷ (, ) θϕ →→ (, ) θϕ (, ) θϕ (, ) θϕ K (, θ ϕ)→ (, ) θϕ **B, C** = ç÷ 11 12 12 12 *nm* 12

(2)
ç÷ MMOM ç÷ èø (, ) θϕ11→→ (, θϕ*nm*) (, ) θϕ1 2(, θϕ*nm*) K (, θϕ*n m*)→ (, θϕ*nm*) For systems incorporating rotational or mirror symmetries with regard to the azimuth angle, it is not necessary to calculate the systems response for light incoming from all angles of the chosen discretization between 0° and 360°. For example the calculation of a crossed grating redistribution matrix requires only a simulation of azimuth angles between 0° and 45° since all information about other incoming angles can be determined by using the rotational and mirror symmetries of the system. While making use of the symmetry, care has to be taken that the chosen angle discretization has the same symmetry. For a 45° symmetry element, this is depicted in Fig. 1 with a *cazimuth* chosen equal to 1 and the inner four polar angle intervals up to *rpolar*=4.

*2.3 Convergence analysis of a three-dimensionally textured sheet* The introduction of an additional angle variable to describe three-dimensional surfaces can lead to a significantly increased need of computational resources. In addition to the use of system symmetries to reduce the computation time, we conducted a convergence analysis concerning the required angle resolution for azimuth and polar angle. The system used for this study was a silicon sheet with planar front side and a binary crossed grating at the rear side (grating period: 990 nm, grating depth: 160 nm, area related fill factor: 0.25, perfect rear reflector). Since the number of different light paths is finite in this case, the absorptance can also be calculated using the formalism of Mellor et al. [15]. This result is exact with regard to the angle channel resolution, because all occurring light paths are known and can be used as angle channels. Therefore, this method can be used as reference for the convergence analysis. In order to determine a sufficient angle resolution for the OPTOS simulations, we first calculated redistribution matrices with a polar angle resolution of 100 intervals and varied the number of azimuth angle channels. The resulting total absorptance for a system with 100 µm sheet thickness is depicted in Fig. 2 for different values of *cazimuth*. Sufficiently small differences between the exact solution and the simulation are reached for a proportionality constant of ¼.
Fig. 2. Results of the azimuth angle convergence analysis. The total absorptance of a system
 with planar front and diffractive grating at the rear side was calculated for different numbers of azimuth angle channels and compared with an exact discretization.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

A similar convergence analysis was carried out for the number of polar angle intervals. Based on this analysis we chose 75 intervals for all following simulations.

*2.4 Absorptance inside texture* In [13], only the redistribution properties of the surface structures were considered during the OPTOS simulation but not the absorptance within the structures themselves. Therefore, the bulk thickness of all investigated systems was chosen to be large compared to the structure dimensions. However, the use of redistribution matrices, which take the absorptance within the texture into account, is possible. As first step, the absorptance within the texture needs to be determined for every incoming angle during the calculation of the redistribution matrices. This information is then contained in an absorptance vector **v***abs*. By multiplication of the known power distribution reaching a surface before the redistribution with the absorptance vector **v***abs* the total absorption during the surface interaction can be calculated. This procedure allows for the modelling of systems where the absorption inside the texture cannot be neglected and it is in principle valid for all kinds of surface textures. One can also distinguish the absorptance in the substrate bulk and in the texture (or even every single texture interaction) without introducing additional simulation steps to the OPTOS formalism. To quantify the influence of the absorptance within the texture on the total absorptance we investigated one two-dimensional exemplary system, with and without absorption inside the texture (Si wafer with V-grooved front side with base length of 10 µm and opening angle of
54.79°, perfectly reflecting rear side). The results showed that already for bulk thickness larger than 100 µm the total absorptance difference is below 1% for all relevant visible and infrared wavelengths. If the sheet thickness is adapted in a way that the volume of the absorbing material is kept constant, there is no significant difference between the absorption spectra even for sheet thicknesses down to 10 µm. However, this might be different for other material systems with strongly absorbing layers on top of the silicon. One has to keep in mind that the OPTOS formalism is based on incoherent coupling which corresponds to an averaged treatment of interference effects. Even for planar wafer based silicon solar cells with thicknesses down to 40 µm neither the optical properties of silicon nor the spectral data change significantly over the period of the Fabry-Perot oscillation. Surface textures further decrease interference effects. For systems beyond wafer- based solar cells, the potential influence of high frequency oscillations caused by interference has to be evaluated carefully. A detailed analysis to approximate the potential error caused by an incoherent treatment has been given in [22].
### 3. Calculation of redistribution matrices

All investigated surface structures, namely inverted pyramids, diffractive crossed gratings and the Lambertian scatterer feature a 90° rotational symmetry concerning the azimuth angle φ and within one 90°-element a mirror symmetry with regard to φ = 45°. Therefore an azimuth angle discretization from 0 to 45° was considered for all matrices, as depicted in Fig. 1. Pyramidal textures formed by intersecting <111> crystal planes are the state of the art surface texture of monocrystalline silicon solar cells [17]. For commercial products mostly random pyramids are fabricated due to the feasibility of the wet chemical process in an alkaline solution for mass production. For this paper, we calculated the redistribution matrix for regular inverted pyramids (characteristic angle: 54.7°) because the existence of a symmetry element reduces the computational complexity. As the structure dimensions are relatively large compared to the relevant wavelengths, the redistribution matrix was calculated using ray optical methods, namely the in-house ray tracing tool Raytrace3D [23]. Due to its complexity and size the complete matrix is difficult to interpret. Figure 3(b), therefore, shows a simplified version where all φ-values corresponding to the same polar angle θ have been summed up (wavelength: 1100 nm, sin(θ): from 0 to 1, φ: from 0 to 45°).

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

With respect to light trapping properties such a representation might be most helpful as the polar angle corresponds to the light path length inside the solar cell. The resulting matrix shows power peaks at distinct reflection angles resulting from single or multiple reflections within the structure. Furthermore reabsorption of light that couples out and re-enters the silicon structure at another pyramid flank occurs.

Fig. 3. Redistribution matrix for a regular inverted pyramid front side at wavelength of 1100

nm calculated via ray tracing. (a) shows a sketch of light interaction with the silicon-air surface

(b) shows a simplified version of the matrix where all entries of different φ-values have been summarized only into the dependency of θ.
A Lambertian surface scatters the light independently of the incoming angle equally into all directions. This means that the incoming power is redistributed uniformly among the angle channels, if they have the same projected area (see Fig. 1). Our discretization with equally distributed sin(θ)-values for the polar angle and the symmetry constraints for the azimuth angle (see Section 2) results in very similar but not in exactly equal angle channel sizes. We calculated the redistribution matrix analytically. As depicted in Fig. 4 (b) this leads to a matrix with an almost uniformly distributed power over the channels. In Fig. 4(b) the complete matrix is shown for all angle channels (discretized in φ and θ). In Fig. 4(c) the simplified version of the matrix depending only on the polar angle θ as presented in the previous examples is shown. Diffraction gratings can be incorporated into solar cells on the rear side to enhance the light trapping via redirection of the light into large polar angles. This leads to a significant short circuit current density (JSC) increase in the near infrared wavelength region for cells with planar front side [19,20]. As the structure dimensions of the gratings (grating period: 1 µm, grating depth: 110 nm, area related fill factor: 0.33) are similar to the wavelengths of interest, RCWA [24,25] was used to calculate the diffraction efficiencies for the redistribution matrix. Figure 5(b) shows the simplified version of the matrix. The experimental samples used for the validation exhibit also planar surfaces. The corresponding redistribution matrix is a diagonal matrix as there is no redistribution between different angle channels. For angles showing total internal reflection at the silicon-air interface the matrix entries are equal to one. Inside the angular escape cone, outcoupling of light into air is allowed and leads to diagonal elements calculated by Fresnel’s equations.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

Fig. 4. Redistribution matrix for a Lambertian scatterer calculated analytically. (a)

schematically shows the interaction of light at a Lambertian surface. (b) shows the complete redistribution matrix with all polar and azimuth angles. (c) shows the simplified version where all entries of different φ-values have been summed up for each given angle θ.

Fig. 5. Redistribution matrix for a binary crossed grating structure on the rear side with a

period of 1 µm at a wavelength of 1100 nm. (a) shows a sketch of light interaction with the silicon-air surface (b) shows a simplified version of the matrix where all entries of different φ- values have been summarized only into the dependency of θ.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

### 4. Calculation of absorptance and validation

For the validation of the OPTOS simulation formalism and its results we fabricated samples with planar surface, pyramidal texture and diffractive grating. The optical characterization was carried out using a Fourier spectrometer. By comparing the measurement data with the simulated absorptance of a silicon sheet with different combinations of these textures we validate the calculation of the matrices and also the simulation sequence for the absorptance determination.

*4.1 Planar front side – crossed grating rear side* The first analyzed system is a 200 µm thick silicon sheet with planar front surface and a crossed grating at the rear side. For comparison with experimental data, the grating was fabricated via Nanoimprint Lithography for the realization of an etching mask with defined structure on top of a monocrystalline silicon substrate. For the following structure transfer to the silicon plasma etching with SF₆ as etching gas was used. A detailed description of the process chain can be found elsewhere [7]. The absorption data of textured samples and planar references are depicted in Fig. 6. The structure dimensions needed for the RCWA simulation were determined by Atomic Force Microscope measurements. Due to an inhomogeneous structure height between 100 nm and 140 nm the corresponding simulation parameter was adapted in that range. The parameters used for the graph were square pillars with a grating depth of 120 nm, a period of 1 µm and an area related fill factor of 0.36.
Fig. 6. Absorptance of a silicon wafer with a planar front side and a binary crossed grating rear
 side. Since the measurement was carried out with an incoming angle of 8°, we used this angle for the simulation as well. The differences in absorptance between 1170 nm and 1200 nm are attributed to measurement artefacts. Overall, measurement and simulation results agree very well for both, the planar reference as well as the textured sample with diffractive rear side grating.
*4.2 Pyramidal front side – planar rear side* The second system for validation of the formalism is the standard case for monocrystalline silicon solar cells: pyramidal front side and planar rear side. In Fig. 7 we compare OPTOS simulation results obtained using a redistribution matrix calculated via ray tracing of regular inverted pyramids with the results obtained with the PV-Lighthouse wafer ray tracing tool for regular inverted and for random inverted pyramids. The simulated wafer thickness was 200 µm with a pyramid height of 3.6 µm, and 500,000 rays were traced [26]. Furthermore, the

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

measured absorptance of a sample with random upright pyramids is shown. According to the results depicted in Fig. 7, all these systems show a very similar front side reflectivity. One can see that the OPTOS result and the PV-Lighthouse ray tracing for random inverted pyramids also match the measurement data in the long wavelength range, while the PV-Lighthouse ray tracing data for the regular pyramids shows lower absorptance for wavelength above 1050 nm. The fact that the OPTOS results, which used the input data for regular inverted pyramids, match the simulation results and experimental data, respectively, for random pyramids can be understood as follows: The light trapping properties of pyramidal structures are significantly influenced by the spatial distribution of the light impinging on the front surface from within the wafer at subsequent interactions and the resulting amount of light that couples out of the wafer. This spatial distribution differs between regular and random arrangements [27]. In a random arrangement, there is no fixed relation between the position and the direction of a ray after the first interaction at the front surface and the position and facet the ray hits at subsequent interactions. When averaged over many pyramids, this corresponds to a uniform distribution at the pyramid base. In the calculation of the redistribution matrices we use uniformly distributed light at the pyramid base. Hence, the OPTOS results correspond to the random case, which explains the good agreement.

Fig. 7. Simulated and measured absorptance of a silicon wafer with a pyramidal front side

texture (inverted (inv), upright (up), random (rand) or regular (reg) pyramids) and a planar rear side.

*4.3 Pyramidal front side – crossed grating rear side* We also fabricated samples with random upright pyramids at the front and a diffraction grating at the rear side using the same structure parameters as described above. Since the only purpose of these experimental samples is the validation of simulations, they are kept as simple as possible and neither incorporate an anti-reflection coating nor a rear side reflector. Both can change the optical properties significantly and have to be considered for conclusions concerning the performance of the textures in a solar cell context. In Fig. 8, OPTOS simulation results and measurement data for sheets with pyramidal front side and diffractive rear side grating are compared. The introduction of the diffractive grating leads to an absorptance gain. Both experiment and simulation show the peak of this at a similar position. However, the simulation predicts a larger gain. This might be due to variations of the grating geometry (as already mentioned in Section 4.a) between different samples leading to deviations between fabricated and simulated grating parameters, and not due to inaccuracies of the simulation method.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

Fig. 8. Simulated (closed symbols) and measured (open symbols) absorptance for a silicon
 sheet with pyramidal front side and planar reflector (orange) or binary crossed diffraction grating (green) at the rear side. The peak of the absorptance gain (blue, right scale) due to the rear side grating occurs at a similar wavelength in the simulation as in the experiment, whereas the total gain is larger for the simulated system. Summarizing the convergence analysis and the absorptance validation procedure of the OPTOS formalism with three-dimensional structures, the simulation results are in a good agreement with established wave-optical and ray-optical reference techniques as well as with measurement results obtained from the system with planar front surface and grating rear side. For the samples with pyramidal front and grating rear side there is a qualitatively good agreement to the measurements, while we attribute the quantitative differences to non- uniform grating parameters.
*4.4 Absorption profile* The iterative calculation of the power distribution vectors after each pass of the sheet allows also for the determination of a z-dependent absorption profile [13]. In the context of photovoltaics the generation profile, which is closely related to the absorption profile, is an important input for electrical solar cell simulations. It contains the information how many electron hole pairs are generated due to photon absorption between a certain depth z and z + dz. In Fig. 9, we present an exemplary generation profile for near infrared light in a silicon wafer with inverted pyramids at the front and a planar rear side. In general, the *z*-coordinate refers to the vertical direction. However, in electrical simulations, the distance from the surface (or from the pn-junction) *ζ* is a more relevant parameter. Therefore, electrical simulation tools like Sentaurus Device use generation profiles in the form *G*(*ζ*) [28]. To be compatible with such tools, it is desirable to convert the *z-* dependent generation profile determined by OPTOS to a *ζ*-dependent generation profile. For systems with planar front and rear, *z* and *ζ* are equal, but for a three-dimensional surface structure like a pyramidal surface there is a larger fraction of volume close to the surface. The conversion can be done by a geometrical transformation valid only for a specific surface topography. By re-scaling the total absorptance is kept constant.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

Fig. 9. Simulated generation profile for a silicon sheet with pyramidal front side and planar
 rear side. In OPTOS the front surface is considered as effective two-dimensional surface that redistributes light. This leads to the profiles *G*(*z*). By geometrical considerations the data can be transformed to the profiles G(ζ), where ζ denotes the distance to the pyramid surface. Data of G(ζ) obtained with OPTOS is in good agreement with data obtained with the Sentaurus Device ray tracing tool. For the pyramidal texture the geometrical correction and re-scaling leads to an enhanced generation for small distances to the surface, as can be seen in Fig. 9. The enhancement factor directly at the surface is approximately 1.7 due to the 1.7 times larger surface area of a pyramidal texture compared to a planar surface. The larger the distances from the surface, the smaller gets the difference between G(z) and G(ζ). For comparison, a generation profile G(ζ) generated with the ray tracer of Sentaurus Device is shown in Fig. 9. The data obtained with the different methods are in good agreement. Note, that this procedure is only appropriate for long wavelength light with optical penetration depths much larger than the texture size. In this case, the polar angle (angle to the *z*-axis) as defined in OPTOS is the relevant angle. For short wavelength light, where a significant fraction is absorbed within the texture, however, the angle to the surface normal has to be considered instead. In this case approaches like the Basore model [29] or ray tracing [30] can be used.
### 5. Approaching the Lambertian limit for silicon solar cells

Pyramidal front side textures show very good anti-reflection properties for silicon solar cells, especially in combination with additional anti-reflective coatings. Nevertheless, the light trapping properties of front side textured cells can be further improved with a rear side structure. In Fig. 10, we show OPTOS absorptance results for 200 µm thick silicon solar cells incorporating a regular inverted pyramid front side with double layer ARC (50 nm SiNx, 90 nm MgF₂) and different rear surface structures in combination with a perfect reflector. The binary diffraction grating with improved parameters compared to the fabricated structure described before (square shape, period: 1 µm, depth: 200 nm, material related fill factor: 0.5) and the Lambertian surface at the rear side show almost the same absorptance and a significant gain compared to the planar rear surface. Weighted with the AM1.5g spectrum this increase corresponds to a photo current density gain of 0.6 mA/cm². The whole system almost reaches the Yablonovitch limit for a system with unity transmittance at the front surface. This makes the combination of a pyramidal front and a diffraction grating rear side very promising to reach highest efficiencies with silicon solar cells.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

Fig. 10. Absorptance calculated with OPTOS of a 200 µm thick silicon solar cell with inverted

pyramidal front with double layer ARC and different rear surface structures combined with a perfect reflector. The diffraction grating (orange) and Lambertian (dark green) rear lead to an absorptance gain (blue, right scale) due to increased light trapping compared to the planar rear (light green). Both systems approach the Yablonovitch limit for a system with zero reflectance.

### 6. Summary and outlook

We presented the three-dimensional formulation of the OPTOS (Optical Properties of Textured Optical Sheets) formalism, which has several advantages. Firstly, arbitrary surface textures can be combined also if they are operating in different optical regimes. Secondly, all calculated matrices can be re-used and thus variations like a thickness change or a change of the angle of incidence can be calculated efficiently with very low computation effort. We discretized the angular half space in a finite number of angle channels, each described by polar and azimuth angle. The discretization was chosen with regard to symmetries of the structures, in order to minimize the calculation effort. It can as well be adapted to structures with other symmetries. As exemplary structures, we calculated redistribution matrices for different surfaces of silicon solar cells: inverted pyramids, crossed gratings and a Lambertian scatterer. Using OPTOS, we determined the absorptance for systems with different combinations of these structures. For the system with a planar front and a grating rear side we found very good agreement between measurements and calculations. For pyramidal front side textures and planar rear sides we compared OPTOS results, ray tracing and measurements. They are in good accordance, but one has to keep in mind the discussed optical properties of different types of pyramids that have been used for the different methods. Finally, OPTOS was used to calculate a system combining surface structures operating in different optical regimes: pyramidal front surface and diffractive grating rear surface. The incorporation of the binary crossed grating is shown to further enhance the absorptance of a silicon wafer with pyramidal front side texture. This system exhibits an absorptance very close to the Yablonovitch limit. The result, that the grating can further enhance the absorption also in silicon solar cells with a textured front, has also been confirmed by optical measurements, which qualitatively fit to the OPTOS results. The method, as presented here, is limited to sheets with two surfaces. However, the OPTOS formalism can also be extended by introducing one or more additional interfaces. This will allow for a combined optical simulation of (potentially textured) module glass, encapsulation layer and solar cell with textures on both sides and a rear reflector. Interested readers who intend to use the OPTOS formalism may contact the corresponding author. A basic example of the OPTOS source code can be made available.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

### Appendix

The following formulas are needed during the simulation procedure. They define the power distribution inside the system, the redistribution matrices and the absorptance calculation. All formulas were introduced and explained in more detail elsewhere [13]. The power distribution among the *n* angle channels with polar angle θ*i* and *m* azimuth angles ϕ*j* inside the system is represented by the vector **v**. The propagation of light is

represented by the multiplication of the propagation matrix **D** and the power distribution vector. As only absorption and no redistribution takes place during the propagation, this matrix has a diagonal form and contains the Lambert-Beer factor with the absorption coefficient.

æö *p*(, ) θϕ11 ç÷ *p*(, ) θϕ ç÷12 −αθ *d* /cos1

|ç÷ ç÷ M|æö e|L 0|
|---|---|---|
|vD == ç÷ p(, θϕ);|ç÷ ç÷ MOM (3)||
|ç÷ ç÷ p(, ) θϕ|ç÷ 0|L e|
|ç÷ p(, ) θϕ ç÷ M|èø||

1 *m*

21 −αθ *d* /cos*n*

ç÷ ç÷ *p*(, ) θϕ èø *nm*

The power distribution at different positions of the textured sheet and its calculation starting from the initial distribution **v**'0 is depicted in Fig. 11 and the following equations.

Fig. 11. Scheme of the power redistribution and the nomenclature for the matrices and the

power distribution vector.

**v** == **DCDv**'; **v**' (**BDCD**) *ii* **v**'; **v** = (**DBDC**)**Dv**' 202 *ii* 02 +1 0 **v**'(21 *ii* +== **CDBD**) '; *ii* **CDv**0**v₂** ( **DCDB**) −1 **v₂** (4)

*PP*'(');*iijiij*==åå**vv** () *jj* The total absorptance, *Abs*, can be calculated by comparing the remaining power before and after propagation through the sheet and adding up the results.

æö *ii* maxæömax *Abs* =+= *Abs*down*Abs*up ç÷ åå(' *P*2*ii*−+ *P*2 +− 1) ç÷ (' *P*2*i* 1− *P*2*i*) (5) èø *ii* == 01 èø

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|

*Abs* =−+ −+ −+ −+ *P₀₁ P P*'''...12*P P*23*P P*34*P*

æö ∞∞ ∞ ∞ =−+− () **BDCD** *ii* **v** () **DBDC Dv** () **CDBD** *i* **CDv** () **DCDB** *i* **DCDv**

## åå ç÷ 00 å å 0 å 0

*ji* èø == 00 *i i* = 0 *i* = 0 *j*

### = ((åI −BDCD)

−− 11 **v**00−− (**I DBDC**) **Dv** +− (**I CDBD**) − 1 **CDv**0−− (**I DCDB**) − 1 **DCDv**0)*j* *j*

For the calculation of the absorption and generation profile, depth-dependent matrices for propagation and absorptance (downwards and upwards) are needed.

æö *e* −αθ *z*/cos1 L 0 ç÷ **D**() *z* = ç÷ MOM (6) ç÷ 0 L *e*−αθ *z*/cos*n* èø

æö 101 −− *ee* −− αθ *zd* /cos1 LL æ α ( − *z*)/cosθ1 0 ö ç÷ ç ÷ **AA**dn() *zz* == ç÷ MOM;up() ç M O M÷ ç÷ 01 LL −− *ee*−αθ *z*/cos*n* ç 0 1−− α (*dz*)/cosθ*n* ÷ èø è ø

(7) The cumulative absorption for down- and upwards propagating light is then given by:
æöæö *ii* max max *Abs*dn() *z* ==åå ç÷ç÷ **Av**dn() ' *z*2*ii* å**A**dn() *z*å**v**'2 (8) *ji* èøèø == 00 *jj j i*

æöæö *ii* max max *Abs*up() *z* ==åå ç÷ç÷ **Av**up() ' *z*2*ii* ++ 1 å**A**up() *z*å**v**'2 1 (9) *ji* èøèø == 00 *j j i j*

These two terms can be used to calculate the cumulative absorption profile:

*Abs*() *z* =+− *Abs*dn() *z Abs*up(0) *Abs*up() *z* (10)

### Acknowledgments

The research leading to these results has received funding from the German Federal Ministry for the Environment, Nature Conservation and Nuclear Safety under contract number 0325292 “ForTeS”. N. Tucher gratefully acknowledges the scholarship support from the Cusanuswerk, Bischöfliche Studienförderung. J. Eisenlohr gratefully acknowledges the scholarship support from the Deutsche Bundesstiftung Umwelt DBU.

|#250422|Received 23 Sep 2015; revised 26 Oct 2015; accepted 27 Oct 2015; published 25 Nov 2015||||
|---|---|---|---|---|
|© 2015|30|2015 | Vol.|No.|24 | DOI:10.1364/OE.23.0A1720|
