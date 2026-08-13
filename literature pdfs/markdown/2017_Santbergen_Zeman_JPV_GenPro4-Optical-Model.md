IEEE JOURNAL OF PHOTOVOLTAICS, VOL. 7, NO. 3, MAY 2017

## GENPRO4 Optical Model for Solar Cell Simulation and Its Application to Multijunction Solar Cells

Rudi Santbergen, Tomomi Meguro, Takashi Suezaki, Gensuke Koizumi, Kenji Yamamoto, and Miro Zeman

***Abstract*—We present a new version of our optical model for solar cell simulation: GENPRO4. Its working principles are briefly**

**explained. The model is suitable for quickly and accurately simulat-** **ing a wide range of wafer-based and thin-film solar cells. Especially adjusting layer thicknesses to match the currents in multijunction**

**devices can be done with a minimum of computational cost. To illus-** **trate this, a triple junction thin-film silicon solar cell is simulated.** **The simulation results show very good agreement with external quantum efficiency measurements. The application of an MgF₂**

**antireflective coating or an antireflective foil with pyramid texture is considered. Their effects on the implied photocurrents of top,**

**middle, and bottom cells are investigated in detail.**

***Index Terms*—Geometrical optics, modeling, thin film PV device properties and modeling.**

I. INTRODUCTION
OLAR cells are complex optical devices, employing ad-

# Svanced light incoupling and trapping strategies. Optical

simulations are an important tool for solar cell design and pro- vide detailed insight in reflection and parasitic absorption losses. These simulations require an optical model that, for a given so- lar cell structure, calculates the reflectance, absorptance, and transmittance as a function of wavelength, taking into account scattering of light at the interfaces and trapping of light inside of the solar cell. In case the optical model is coupled to an*electrical* model for calculation of the solar cell’s current–voltage char- acteristics, the optical model also needs to provide the photon absorption profile along the depth of the absorber layer [1]–[5]. Most of the existing optical models are either based on wave optics or ray optics. Wave optics models take the full electromag- netic wave nature of light into account by rigorously solving the Maxwell equations. Due to the high computational cost, these Maxwell solvers are limited to small simulation domains, so only periodic thin-film solar cells can be simulated within rea- sonable computation time [6]. Ray optics on the other hand ap- proximates light as rays. Ray-tracing techniques are commonly

Manuscript received November 3, 2016; revised December 21, 2016; accepted February 8, 2017. Date of publication March 2, 2017; date of current version April 19, 2017.

R. Santbergen and M. Zeman are with the Delft University of Technology,
Delft 2628CD, The Netherlands (e-mail: r.santbergen@tudelft.nl; m.zeman@ tudelft.nl).

T. Meguro, T. Suezaki, G. Koizumi, and K. Yamamoto are with Kaneka
Corporation, Osaka 566-0072, Japan (e-mail: Tomomi.Meguro@kaneka. co.jp; Takashi.Suezaki@kaneka.co.jp; Gensuke.Koizumi@kaneka.co.jp; kenji. yamamoto@kaneka.co.jp). Color versions of one or more of the figures in this paper are available online at [http://ieeexplore.ieee.org](http://ieeexplore.ieee.org). Digital Object Identifier 10.1109/JPHOTOV.2017.2669640

used to simulate textured c-Si solar cells [7], [8]. However, be- cause wave effects such as diffraction are ignored, ray optics is not suitable for simulating light scattering by subwavelength features. In most commercially available Maxwell solvers or ray trac- ing software, it is possible to create a 3-D model of a complete solar cell. However, in many cases the solar cell can, to a good approximation, be represented as a 1-D multilayer structure. This allows the use of simpler and faster multilayer methods. In case all interfaces are optically flat, straightforward transfer- matrix or net-radiation methods can be used [9], [10]. In case the interfaces have a texture that scatters light, extended multilayer methods can be used [11]–[16]. We previously introduced the extended net-radiation method [17], [18] and similar methods have been proposed since [19], [20]. The extended net-radiation method takes the angular intensity distribution of scattered light for every interface as input. A simple intensity distribution (e.g., Lambertian) can be assumed or a more realistic distribution can be calculated taking into account the dependence on wavelength and the angle of incidence by using dedicated interface mod- els. In our previous implementation a Phong distribution [21] was assumed for subwavelength textured interfaces and a two- dimensional ray tracing model was used for interfaces with larger textures. In this paper, we introduce a new, much improved version of our optical model for solar cell simulation: GENPRO4. The nov- elty is not so much the use of the extended net-radiation method, which we [17], [18] and others [19], [20] have presented before, but the addition of fast and flexible interface models for light scattering at textured interfaces. Interfaces with subwavelength random texture are simulated using the scalar scattering model developed by Jager ¨ *et al.* [22], [23]. Interfaces with larger tex- ture are simulated using ray tracing. Both interface models are fully 3D and can take an atomic force microscopy (AFM) scan of the surface morphology as input. Angular intensity distributions calculated by commercially available Maxwell solvers, as done by Li *et al.* [19], can be given as input as well. In addition, we include new algorithms for detailed analysis of reflection losses and for current matching in multijunction solar cells. GENPRO4 has been validated for a wide range of wafer-based and thin-film solar cells [24]–[26] and is now commercially available to the solar cell community [27]. In Section II, the working principles of GENPRO4areex- plained. Then, in Section III, we illustrate its new features by considering a triple junction thin-film silicon solar cell. We ana- lyze the effects of an MgF2antireflection coating and an antire- flective foil with pyramid texture on the implied photocurrents

2156-3381 © 2017 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [http://www.ieee.org/publications](http://www.ieee.org/publications) standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Bodleian Libraries of the University of Oxford. Downloaded on June 30,2026 at 13:09:48 UTC from IEEE Xplore. Restrictions apply.

by a set of linear equations [10]:

|i a i|i−1 d||
|---|---|---|
|i b i|i a|i i c|
|ic i + 1|ib + 1||
|id i|ia|i ic|

|⎧ ⎪ ⎪q = τ|· q||
|---|---|---|
|⎪ ⎨ q =|r · q + t|· q|
|⎪ ⎪q ⎪ = τ|· q||
|⎩ q = t|· q + r|· q|

*.* (1)
Fig. 1. Schematic representation of a multilayer structure showing the num-

bering convention for layers and interfaces. (a) Various optical paths contributing to *R*, *T,* and *Ai*. (b) Net-radiation fluxes.

|to R, T, and A|. (b) Net-radiation fluxes.||||i|
|---|---|---|---|---|---|
||||b|||
|||i|Id d i−1|c i−1|b a i i|
|||i||||

of top, middle, and bottom cells. Finally, in Section IV, the conclusions are presented.

### II. MODEL DESCRIPTION

This section explains the extended net-radiation method on which GENPRO4 is based. More details can be found in the GENPRO4 user manual [28]. The method is completely general and can be applied to both wafer-based and thin-film solar cells.

*A. Flat Interfaces* In the simplest case where all interfaces are flat, the conven- tional net-radiation method can be used [10]. In the net-radiation method, the solar cell is represented as a multilayer structure as shown in Fig. 1. We number the layers and interfaces from top to bottom. The subscript *i* will be used to indicate layer and in- terface numbers. The goal of the simulation is to determine the overall reflectance *R*, the transmittance *T*, and the absorptance of each layer *Ai*. Each layer is characterized by thickness *di* and complex refractive index *Ni*(*λ*), where *λ* is the wavelength. Because *Ni*is wavelength dependent, *R*, *T,* and *Ai*are wave- length dependent as well. Below it is explained how *R*, *T,* and *Ai*are calculated for a single wavelength. This calculation is then repeated for every wavelength in the relevant wavelength range. When all interfaces are optically flat, the interface reflectances *r* *i*can be calculated from the Fresnel equation and the corre- sponding interface transmittances are given by *ti*= 1 *− ri*. The*layer* transmittances*τi*can be calculated from the Lambert– Beer law. Note that the values of *ri*, *ti*, and *τi*depend on the angle of incidence. An incident photon can bounce between the interfaces multiple times and travel a complicated path [see
Fig. 1(a)]. Therefore, to calculate*R*,*T,* and*Ai*from*ri*, *ti*, and*τi*,
 all possible reflections have to be taken into account. There are different mathematically equivalent methods to do this. The net- radiation method is illustrated in Fig. 1(b). At every interface four fluxes are defined: *qix*. Here, subscript*i*is the interface num- ber and the superscript *x* ( = *a*, *b*, *c,* or *d*) indicates whether the light is approaching/leaving the interface from the top/bottom, as defined in Fig. 1(b). Each flux represents the net-radiation (in W/m²) due to all possible photon paths. All fluxes are related
In total there are four*·I* equations, where *I* is the total number of interfaces. It is convenient to normalize all fluxes to the incident power, such that they can be written in nondimensional form. The assumption that all light is incident from the top and none from the bottom then implies that *q₁* *a* = 1 and *qIc*= 0. Equation (1) represents a set of linear equations that can be solved using standard numerical techniques to obtain the values of every flux. From this, the desired *R*, *T,* and *Ai*are obtained

*R* = *q₁* (2)

*T* = *q* (3)

*A* = *q − q* + *q − q.* (4)

Note that *A* is simply the sum of fluxes entering minus the fluxes leaving layer *i*.

*B. Interference* The fluxes *q* introduced in Section II-A represent the light intensities in W/m². In (1) and (4), these fluxes are simply being added without taking into account interference effects. This approach is only accurate for so-called incoherent layers that are thick compared to the coherence length of the incident sunlight (*≈* 1 *μ*m). For thin (coherent) layers, interference does play a role and GENPRO4 uses a different calculation method in which the fluxes represent the complex amplitudes of electro- magnetic waves [11]. GENPRO4 can combine these two distinct approaches by treating the thin (coherent) layers as a “coating,” which is part of the interface between two thick (incoherent) “layers.” In GENPRO4, “layers” are treated incoherently and do not give rise to interference while “coatings” are treated co- herently and do give rise to interference. Note that GENPRO4 calculates the photon absorption profile of both the coherent and incoherent layers using the method described in [11].
*C. Surface Texture* Most interfaces in the solar cell have a surface texture to reduce reflection losses and to scatter incident light into the absorber layer. In that case, instead of having one discrete prop- agation direction, the reflected and transmitted light is charac- terized by an angular intensity *distribution* over the available propagation directions. Each propagation direction can be visu- alized as a point on a hemisphere, characterized by zenith angle *θ* and azimuth angle *ϕ*. The net-radiation method described in Section II-A can then be extended by subdividing this hemi- sphere into angular intervals each with a corresponding subflux. In this case, we use a discretization scheme that divides the hemisphere into cones, such that each of the angular intervals is bounded by an upper and lower zenith angle *θ*, as indicated in Fig. 2(a). The zenith angle is measured relative to the surface normal direction and ranges from 0° (perpendicular to the in- terface) to 90° (parallel to the interface). Typically the number

SANTBERGEN *et al.*:GENPRO4 OPTICAL MODEL FOR SOLAR CELL SIMULATION AND ITS APPLICATION TO MULTIJUNCTION SOLAR CELLS

Fig. 2. (a) Division of every hemispherical direction into angular intervals.

(b) Net-radiation subfluxes at interface 1. (For clarity the figure shows six intervals. GENPRO4 typically uses 30 intervals for higher accuracy.) of angular intervals is set to 30, resulting in an angular width of the intervals of 3°. Each flux is then divided into 30 subfluxes as indicated in Fig. 2(b). All relations between these subfluxes can still be written as a set of linear equations. Note that this set now contains four*·I·V* equations, where *I* and *V* are the number of interfaces and the number of angular intervals, respectively. Typically this results in a large set of hundreds of equations. However, using standard numerical techniques, a computer can solve such a set of linear equations within a fraction of a second. It is convenient to indicate each subflux in the following way: *q* *ix*(*v*), where *x* and *i* have the same meaning as explained in Section II-A, and *v* is the interval number. For example *q₂* *a*
(5) is the flux approaching interface 2 from above in the
fifth angular interval (i.e., the interval ranging from 12° to 15°). The fluxes can then be grouped into vectors ***q*** *x* *i*= [*qix*(1)*,qix*(*v*)*,...,qix*(*V*)], where the bold font indicates a vec- tor. *V* is the number of intervals, which typically is 30. This vector notation allows the large set of equations to be written in a compact way using matrix multiplication

⎧

|a i i|d i − 1||
|---|---|---|
|b +|a −|c|
|i i|i i|i|
|ci i + 1|bi + 1||
|d +|a −|ci|
|i i i|i i i i|i|

⎪ ⎪ ***q*** = ***τ** · **q*** ⎪ ⎨ ***q*** = ***r** · **q*** + ***t** · **q***

*.* (5)
⎪ ⎪***q*** = ***τ** · **q*** ⎪ ⎩ ***q*** = ***t** · **q*** + ***r** · **q***

Note that the coefficients ***r***, ***t***, and ***τ*** are now also in bold to indicate that these are now matrices of size *V × V*.The matrices ***r**i*and ***t***, to which we will refer as scattering matrices, contain the angular intensity distribution of scattered light for every angle of incidence (also known as the bidirectional scatter distribution function). The ***r**i*and ***t**i*matrices for light incident on interface *i* from the top and bottom are different and the superscripts “+” and “–” are used to distinguish them. The scattering matrices are calculated from the surface morphology of the interface using either the ray optics model or the wave optics model, as will be illustrated in Section II-D. Once the matrices are calculated, they can be substituted into (5) and the set of equations can be solved. The vector *q₁* *b* contains all fluxes leaving the top of the first interface [see Fig. 2(b)] and therefore contains the information regarding the angular intensity distribution of light reflected by the multilayer structure. The total reflectance *R* is simply ∑ sum of the intensity of all the elements of this vector ***q*** *b* = *q₁* *b*

(1)+ *q₁* *b*
(2)+*···*+ *q₁*
*b*

(*V*). Similar to (2)–(4), *R*, *T,* and *Ai*
are given by ∑ *R* = ***q*** *b* 1(6) ∑ *T* = ***q*** *d* *I*(7) ∑ ∑ ∑ ∑ *Ai*= ***q*** *d* *i−*1*− **q*** *ci−* 1+ ***q*** *bi* *− **q*** *a* *i*

*.* (8)
*D. Calculation of Scattering Matrices* As explained above, every interface *i* is characterized by four scattering matrices (***r***
+ *, **t*** + *, **r*** *−* *, **t*** *−* ). Matrix element (*u,v*) *i i i i* indicates the probability that a photon, incident from angular interval *v,* after reflection or transmission ends up in interval *u*. For visualization purposes, we place these scattering matrices in a2*×* 2 array to form one single matrix as shown in Fig. 3. The horizontal axis of the matrix represents the incident angle and the vertical axis represents the outgoing angle. As also indicated in Fig. 2(b), these angles go from +0 *◦* (normal incidence from above the interface) to *±*90 *◦* (parallel to the interface) and back to *−*0 *◦* (normal incidence from below the interface). Plus and minus signs are used to indicate whether an angle is measured from the surface normal above or below the interface. The color indicates the corresponding probability which ranges from 0% (black) to 100% (white). Each quadrant of the matrices shown in

Fig. 3 consists of one scattering matrix with 90 *×* 90 elements,

corresponding to a small angular interval of 1 *◦*. The number of intervals can be increased to improve accuracy at the cost of increased simulation time. Intervals of 3 *◦*, resulting in scatter matrices of 30 *×* 30 elements, usually provide a good trade-off between accuracy and simulation time. Note that conservation of energy dictates that the sum of every column adds up to 100%. The reciprocity theorem [29] dictates that if light can go from interval *u* to *v*, the reverse path *v* to *u* should also be allowed, which implies that the matrix should be symmetrical.

*1) Model for Flat Interfaces:* A basic ray-optics model
based on the Fresnel equations for reflectance and Snell’s law for refraction angles is used for flat interfaces. Here, we con- sider a flat air/glass interface of which the resulting scattering matrices are shown in Fig. 3(a). The line on the main diago- nal represents the specular reflection component, because for specular reflection a photon incident in interval *u* is reflected back into the same interval *u*. The other lines (near the counter diagonal) represent the transmission component. As a result of refraction, these lines are curved and terminate at the critical angle. The sum of each column adds up to 100% indicating that energy is conserved. Also, the matrix is symmetrical, which is in agreement with the reciprocity theorem.

*2) Model for Interfaces With Small Texture:* For surface tex-
tures with features smaller than the wavelength, wave effects such as interference and diffraction need to be taken into ac- count. For this, the scalar scattering model developed by Jager ¨ *et al.* [22], [23] was implemented in GENPRO4. Input for this model is a height map of the surface morphology. The interface is then approximated by an array of point sources, each emitting spherical scalar waves at a phase calculated from the local height of the morphology and the angle of incidence. The scattering in- tensity for a particular direction depends on whether these waves interfere constructively or destructively in the far field. Math- ematically, this is equivalent to taking the Fourier transform

Fig. 3. Scattering matrices calculated by GENPRO4 for (a) a flat air/glass interface. (b) An interface with Asahi U-type texture (calculated for *λ* = 600 nm).

(c) An air/glass interface with an inverted pyramid texture with a steepness of 55°. of the pupil function. This scalar scattering model has been experimentally validated for a wide range of surface morpholo- gies and was shown to be most accurate for morphologies with feature sizes on the order of 100 nm or less [22], [23]. Amorphous silicon (a-Si:H) solar cells are commonly de- posited onto an Asahi U-type glass/SnO:F substrate. This has a surface texture with a root mean square roughness of about 50 nm. Its morphology was measured using AFM and used as input for the scalar scattering model. Fig. 3(b) shows the cor- responding scattering matrices calculated for an SnO:F/a-Si:H interface with this texture. The diffusely reflected and transmit- ted light is scattered over a broad angular range, distributing the probabilities over a wide range of intervals. The *specular* reflection and transmission components are visible as the thin lines. The sum of each column again adds up to 100% indicating that energy is conserved. However, Fig. 3(b) reveals that the ma- trix is not symmetrical, which means that the scalar scattering model developed by Jager ¨ *et al*. is not reciprocal. This limita- tion, which we have exposed by displaying the scatter matrices in this way, means that care should be taken when using this model. In Section III we will, however, show by means of ex- perimental validation that the model is accurate for the thin-film silicon solar cell considered.
*3) Model for Interfaces With Large Texture:* For surface tex-
tures with a feature size that is large compared to the wavelength, wave effects can be ignored and ray optics applies. For this, GEN- PRO4 uses a built-in ray tracing model. To calculate column *u* of the interface matrix, incident rays are emitted onto the textured interface from interval*u*and the angular intensity distribution of rays reflected and transmitted by the interface is recorded. This is then repeated for every incident angular interval. Fig. 3(c) shows the resulting scattering matrices of an air/glass interface with an inverted pyramid texture with a steepness of 55°.This figure shows that for a given angle of incidence, a ray can be re- flected or transmitted in various directions. This is because each pyramid has four facets, each with a different orientation that can be hit by the ray one or multiple times. The sum of each col- umn adds up to 100% indicating that energy is conserved. Also the matrix is symmetrical, from which it can be concluded that the ray tracing model does not violate the reciprocity theorem.

*4) External Models:* The three interface models mentioned
above are included in GENPRO4. With these models most types of c-Si and thin-film solar cells can be simulated accurately. However, some effects, such as plasmonic effects and refractive index grading, are not included. These effects can nonetheless

be simulated for a single interface using external models such as a Maxwell solver or an effective medium model. As long as the external model can predict the angular intensity distribution of reflected and transmitted light as a function of the angle of incidence, this information can be imported by GENPRO4inthe form of a scattering matrix and included in the simulation. In this way, different simulation techniques, each optimized for a particular interface, can be combined in a computationally efficient way. By displaying the generated scattering matrices as shown in Fig. 3, one can quickly check whether conservation of energy and reciprocity are obeyed.

*E. Features of the Model* The extended net-radiation method is very fast and efficient and a typical simulation takes only a few minutes. In GENPRO4, most of the computation time is spent on calculating the scat- tering matrices ***r**i*and ***t**i*for every wavelength. When repeating the simulation with a different layer thickness, the correspond- ing layer transmittance matrix ***τ**i*changes, but the scattering matrices ***r**i*and ***t**i*stay the same. In that case, the previously calculated scattering matrices can be reused without recalcu- lation to save computation time. This is especially useful for matching the currents between subcells of a multijunction solar cell by varying absorber layer thicknesses, as will be illustrated in the next section. In the next section, we simulate multijunction solar cells under normally incident light. In that case, the incident flux is in the first angular interval of ***q***
*a* 1. However, it is also possible to have this flux incident in any other angular interval of***q*** *a* 1and simulate the cell under a different angle of incidence. One could even distribute the incident flux over several intervals to mimic the angular distribution of diffuse light coming from different parts of the sky. Simplifying assumptions that make the GENPRO4 model fast, also give rise to some limitations that have to be considered. First, the model represents the solar cell as a multilayer sys- tem. Three-dimensional structures that deviate from this, such as metal contact fingers, cannot be included in the simulation. Also the calculated photon absorption profile along the depth of the absorber layer is a 1-D cross-section. Three-dimensional nonuniformities are not resolved. Second, for this work, we have not discretized the angular intervals with respect to the azimuth angle [see Fig. 2(a)]. This is convenient for flat interfaces or ran- dom textures with rotation symmetry around the surface normal,

Fig. 4. (a) Schematic cross-section of triple junction thin-film silicon solar

cell. (b) Measured EQE (circles) and simulated absorptance in i-layer (lines) of top, middle, and bottom cells.

but it is less accurate for periodic textures that do not have this rotation symmetry, such as gratings or grooves.

### III. RESULTS

In this section, we consider the triple junction thin-film silicon solar cell design by Kaneka Corporation, indicated in Fig. 4(a). The top, middle, and bottom cells are a-Si:H, amorphous sili- con/germanium alloy, and nanocrystalline silicon. The bandgaps of these respective materials are 1.8, 1.5, and 1.1 eV. Each cell consists of an intrinsic absorber layer with 10–20 nm thin p- and n-type regions at the front and rear, respectively. Two low- index intermediate reflector layers separate the top and middle cells and the middle and bottom cells, respectively [29]. The whole layer stack was deposited onto a glass/SnO₂:F super- strate (Asahi U-type). The SnO₂:F is approximately 700 nm thick and serves as transparent front contact. In addition, it has a surface texture with an rms roughness of about 50 nm, to scat- ter the incident light. At the rear side there is a back reflector consisting of 100 nm of ZnO:Al and 300 nm of silver. In this initial design, the thicknesses of top, middle, and bot- tom intrinsic layers (i-layers) are 100.0, 112.5, and 2300 nm, re-

spectively. This triple junction device was fabricated by Kaneka Corporation. The external quantum efficiencies (EQEs) of top, middle, and bottom cells were measured and the result is shown in Fig. 4(b) (symbols). This shows that the top, middle, and bottom cells each absorb a different part of the spectrum. The corresponding short-circuit current densities, obtained by inte- grating the EQE curves over the AM1.5g spectrum, are indicated as well. This shows that the bottom cell generates the lowest cur- rent density of 7.70 mA/cm² and therefore limits the current of the total device. GENPRO4 was used to simulate the layer structure of Fig. 4(a) in the wavelength range 300–1200 nm in steps of 10 nm. The layer thicknesses mentioned above were used and the refractive index and extinction coefficient of each layer were measured in- house using spectral ellipsometry and/or reflection/transmission measurements. In principle, such thin i-layers could give rise to interference fringes in the EQE curves. However, the mea- sured EQE curves shown in Fig. 4(b) do not show such fringes. Most likely these interference fringes are suppressed by the strong light scattering due to the surface textures. For this reason, we simulate the i-layers incoherently. The first two in- terfaces (air/glass and glass/SnO₂:F) are flat. The SnO₂:F su- perstrate has a nanotexture designed for light scattering and its surface morphology was measured using AFM over an area of 20*μ*m *×* 20 *μ*m. All subsequent interfaces have a nanotexture as well. The most accurate simulation results are obtained when the measured morphology of every interface is used as input [22], [23]. However, here we use the simplifying assumption that deposition is perfectly conformal, such that all subsequent interfaces have the same texture. To make sure that this assump- tion does not introduce a significant error, experimental valida- tion will be presented below. The angular intensity distribution of light scattered by the textured interfaces was simulated using the scalar scattering model with the AFM scan of the surface morphology as input [22], [23]. GENPRO4 gives the reflectance, absorptance of each layer and the transmittance as a function of wavelength. The absorptances of the top, middle, and bottom i-layers, calculated for normal incidence, are shown in Fig. 4(b) (lines) and compared with the measured EQE (circles). For state-of-the-art devices, it is accurate to assume that every photon absorbed in the i-layer generates one electron–hole pair and recombination losses can be ignored. In that case, the absorptance of the i-layer should be identical to the cell’s EQE. Fig. 4(b) shows that there is very good agreement between measurement and simulation. This simulation result shows that GENPRO4 is a valid tool for simulating this type of solar cell. In addition, it shows that for this type of solar cell a purely optical simulation can be used to predict EQE curves and the corresponding short-circuit current densities. Note that if losses due to recombination of photogenerated charge carriers play a more important role, an electrical model that takes these effects into account would have to be needed to accurately predict the EQE. Next, the simulation is repeated for different top and middle i-layer thicknesses while keeping the thickness of the bottom cell fixed at 2300 nm. In all simulations, normal incidence is assumed and the current densities are obtained by integrating over the AM1.5g spectrum. The goal is to determine the thick- ness combination that results in perfectly matched cell currents.

Fig. 5. (a) Device current density (in mA/cm²) as a function of top and middle

i-layer thicknesses. Blue, green, and red areas indicate where, respectively, top, middle, or bottom cell are current limiting. The maximum current is obtained where all currents are matched (indicated by yellow circle). (b) Absorptance of every layer and reflectance for the current matched triple junction cell.

Because the scattering matrices calculated in the first simulation can be reused, each simulation finishes within a few seconds. This means that it is feasible to simulate many thickness combi- nations. We vary both top and middle i-layer thicknesses from 50 to 150 nm in steps of 5 nm. The result of more than 400 simu- lations is shown in Fig. 5(a). It shows the *device* current density as a function of top and middle cell thicknesses for a fixed bot- tom cell thickness of 2300 nm. Note that this device current density is the *limiting* current, i.e., the lowest current generated by the top, middle, or bottom cell. When the top cell is thin (region indicated in blue), it limits the device current. When the middle cell is thin (region indicated in green), this cell limits the device current. When both top and middle cells are thick (region indicated in red), the bottom cell limits the device current. The highest device current is obtained when all currents are perfectly matched. The simulation shows that this is the case when the top cell is 94.0 nm thick (instead of 100.0 nm) and the middle cell is 99.5 nm thick (instead of 112.5 nm). At this point, the de- vice current density is 7.98 mA/cm². Therefore, relative to the initial device considered in Fig. 4(b), *decreasing* the thickness of top and middle i-layers *increases* the device current by 3.6%.

Note that in practice, it is difficult to deposit these films of this exact layer thickness with subnanometer accuracy uniformly and reproducibly over large areas. The mentioned thicknesses should, therefore, be interpreted as target thicknesses and the corresponding increase in device current as the theoretically maximum achievable current gain.

Fig. 5(b) shows the absorptance of each layer as a function

of wavelength in the current-matched device. The desired ab- sorption in the i-layers is indicated by the light brown area and the contributions from top, middle, and bottom i-layers are indicated by the blue, green, and red lines. Integrating these curves over the AM1.5 g spectrum confirms that top, middle, and bottom cells generate exactly the same current density of

7.98 mA/cm². Besides the desired absorption, there are signifi- cant parasitic absorption losses as well. The yellow and orange areas represent the absorption losses in SnO₂:F and the com- bined absorption losses in the p- and n-layers. The white area represents the reflectance loss. The reflectance loss is one of the largest optical losses and two approaches for reflection reduction are tried. First, the effect of an MgF₂ antireflective coating, with a refractive index of about
1.38, is investigated. A bare air/glass interface has a constant reflectance of 4%. An MgF₂ coating reduces this to less than 2%, but only in the wavelength range near a reflection minimum. The first-order reflection minimum occurs at a wavelength that is four times the coating’s optical thickness. Therefore, with increasing coating thickness the first-order reflection minimum red-shifts and consecutively overlaps the region where top, mid- dle, and bottom cells are most sensitive. By tuning the coating thickness it should, therefore, be possible to selectively enhance the current in top, middle, or bottom cell. GENPRO4 was used to simulate the triple junction cell with MgF₂ coating. Fig. 6(a) shows the simulated top, middle, and bottom cells current density as a function of coating thickness. This reveals that the optimum MgF₂ coating thicknesses for maximum currents from top, middle, and bottom cells are 88, 110, and 130 nm, respectively. Overall, the optimum coating thickness is 110 nm, as this increases the top, middle, and bot- tom cell currents by 1.7%, 2.0% and 1.7%, respectively. When starting from a perfectly current-matched device, as shown in Fig. 6(a), the MgF₂ coating will, therefore, increase the device current by 1.7%. Note, however, that when starting from a slightly mismatched device, the highest device current may be achieved by targeting the cell that is limiting the current. For example, when the device current is limited by the bottom cell [as for the initial configuration considered in Fig. 4(b)],a 130 nm coating would enhance the device current by 1.8% while a 110 nm coating would enhance this by only 1.7%.
Fig. 6(a) also shows a second set of maxima for coating thick-
 nesses of more than 200 nm. These maxima are caused by the *second*-order reflection minimum passing over the spectral re- gions where top, middle, and bottom cells are most sensitive. Interestingly, because the second-order reflection minimum is much narrower, the current of the individual cells can be en- hanced more selectively. For example, a 260 nm thick MgF₂ coating enhances the top cell current by 1.3%, without affecting the bottom cell current. A second approach for reducing reflectance loss is to apply a transparent polymer at the air/glass interface that has a texture with a feature size in the micron to millimeter range [31]. Here,

Fig. 6. Top, middle, and bottom cells implied photocurrent density. (a) As a

function of MgF₂ coating thickness. (b) As a function of texture foil pyramid steepness.

we will consider a square base pyramid texture. Such a foil will reduce reflectance loss when any light reflected off one pyramid hits a neighboring pyramid and enters the material. To which extent this occurs depends on the steepness of the pyramid (i.e., the angle the pyramid face makes with the horizontal). As long as the pyramids are larger than the wavelength of the incident light, ray optics applies and the antireflective properties do not depend on the exact size of the pyramid. Unlike the MgF₂ coat- ing, this antireflective foil will cause a *broadband* reflection reduction that affects the top, middle, and bottom cells in the same way. However, refraction of light by the texture changes the propagation direction of light inside the device. The light will be scattered in somewhat different directions at each of the nanotextured interfaces. Because every layer has a different, wavelength dependent, refractive index it is difficult to predict the overall effect in advance. Some layers might absorb more light, leaving less light for other layers thereby potentially cre- ating some current mismatch between top, middle, and bottom cells. GENPRO4 was used to investigate the effect of such a pyramid textured antireflective foil. For simplicity, it was assumed that the foil has the same optical properties as glass. Note that ray optics is used for the pyramid texture while wave optics was used for the nanotextured interfaces. The fact that ray and wave optics can be combined in this way shows the flexibility of GENPRO4. The pyramid steepness was varied between*−* *◦* and 60°, where

Fig. 7. (a) SEM image of antireflective texture foil showing the inverted

pyramid texture. (b) *IV*-curve, measured independently by AIST in Japan, of the triple junction thin-film silicon PV module with an area of 1.42 m *×* 1.10 m with antireflective texture foil.

a negative and positive steepnesses signify inverted and upright pyramids, respectively. Fig. 6(b) shows the top, middle, and bottom cell currents as a function of pyramid steepness. This shows that a shallow pyramid with a steepness less than 30° has little effect. This steepness is insufficient to induce a second bounce and reduce reflectance. However, increasing the pyramid steepness from 30° to 45° does reduce reflectance and enhances all cell currents by about 5%, both for inverted and upright pyramids. About 4% of this gain can be attributed to reduced reflection losses and the additional 1% is due to increased path length inside the absorber layers. No significant further increase is observed when pyramid steepness is increased beyond 45°. Small differences between the cells can be observed. Especially *◦* for a pyramid steepness of *±*45, where the bottom cell current exceeds the current of the top cell by 1.8%. Based on these simulation results, an antireflective texture foil was developed with inverted pyramids of 70 *μ*m wide and with a steepness of *−*55 *◦*, as shown in Fig. 7(a). This texture foil was then applied to a large area (1.42 m *×* 1.10 m) triple junction thin-film silicon PV module. As predicted by the model, the application of the foil increased the PV module’s current and power output. This resulted in a PV module power of 184 Wp, which corresponds to an initial conversion efficiency of 11.77%, as independently confirmed by measurement at the National Institute of Advanced Industrial Science and Technology (AIST) in Japan [showninFig.7(b)]. This is a very high efficiency for a thin-film silicon PV module of this size. The results presented in this section have shown that both an MgF₂ coating and texture foil can enhance the device current of the triple junction thin-film silicon solar cell, but can also introduce a slight current mismatch. In order to arrive at the maximum device current, the cell currents need to be perfectly matched. Therefore, the effects of MgF₂ coating or antireflec- tive foil need to be taken into account when determining the optimum top, middle, and bottom i-layer thicknesses. GENPRO4 was used to “rematch” the currents by varying top and mid- dle cell i-layer thicknesses. This was done for both the cases of the device with either MgF₂ coating or with antireflective foil. The results are shown in Table I and the case with bare glass is given as a reference. Note that it was not needed to sys- tematically go through all possible thickness combinations [as showninFig.5(a)]. Instead a simplex search algorithm was used to quickly find the top and middle cell thicknesses for perfect current matching.

TABLE I TOP,MIDDLE, AND BOTTOM CELL I-LAY E R THICKNESSES AND CORRESPONDING MAT C H E D CURRENT

2 Top [nm] Middle [nm] Bottom [nm] *J*sc[mA/cm]

Bare glass 94.0 99.5 2300 7.98 MgF₂ (110 nm) 94.3 99.2 2300 8.12 Foil (*−*55*◦*pyramid) 97.1 101.9 2300 8.45

### IV. CONCLUSION

GENPRO4 is a much improved version of our optical model for simulation of solar cells. It is based on the extended net-radiation method in which ray optics and wave optics are combined in a computationally efficient way. It can be used to gain insight in the optical losses of the solar cell and is especially suitable for quickly finding the absorber layer thicknesses needed for current matching in multijunction solar cells. The features of GENPRO4 are illustrated by simulation of a triple junction thin-film silicon solar cell. Very good agreement with EQE measurements is found. Simulations show that perfect current matching can be achieved by reducing the thicknesses of top and middle i-layers and thereby increasing the device current by 3.6%. A 110 nm thin MgF₂ antireflection coating on the front glass can increase the device current by an additional

1.7%. Alternatively, a foil with inverted or upright pyramid texture of at least 45° steepness can increase the device current up to 5%. Both the MgF₂ coating and the texture foil introduce a slight current mismatch which can be corrected by adjusting the i-layer thicknesses.
ACKNOWLEDGMENT

The authors would like to thank O. Isabella of the Delft University of Technology for providing useful feedback on the manuscript and K. Jager of Helmholtz-Zentrum Berlin for fruit-¨ ful discussions.

REFERENCES

[1] R. E. I. Schropp and M. Zeman, *Amorphous and Microcrystalline Silicon* *Solar Cells: Modeling, Materials and Device Technology*.NewYork,NY, USA: Springer, 1998. [2] M. Zeman and J. Krc, “Optical and electrical modeling of thin-film silicon ˇ solar cells,” *J. Mater. Res.*, vol. 23, no. 4, pp. 889–898, 2008. [3] D. A. Clugston and P. A. Basore, “PC1D version 5: 32-bit solar cell modeling on personal computers,” in *Proc. IEEE Photovolt. Spec. Conf.*, 1997, pp. 207–210. [4] J. Krc, F. Smole, and M. Topi ˇ c, “Analysis of light scattering in amorphous ˇ Si:H solar cells by a one-dimensional semi-coherent optical model,” *Prog.* *Photovolt.*, vol. 11, pp. 15–26, 2003. [5] M. Burgelman, P. Nollet, and S. Degrave, “Modelling polycrystalline semiconductor solar cells,” *Thin Solid Films*, vol. 361–362, pp. 527–532,

2000.
[6] K. Jager, D. N. P. Linssen, O. Isabella, and M. Zeman, “Ambiguities in ¨ optical simulations of nanotextured thin-film solar cells using the finite- element method,” *Opt. Express*, vol. 23, no. 19, pp. A1060–A1071, 2015. [7] P. Campbell and M. Green, “Light trapping properties of pyramidally textured surfaces,” *J. Appl. Phys.*, vol. 62, pp. 243–249, 1987. [8] K. R. McIntosh and S. C. Baker-Finch, “OPAL2: Rapid optical simula- tions of silicon solar cells,” in *Proc. IEEE Photovolt. Spec. Conf.*, 2012, pp. 265–271, [9] O. S. Heavens, *Optical Properties of Thin Films*. London, U.K.: Butter- worth, 1955.

[10] R. Siegel, “Net radiation method for transmission through partially trans- parent plates,” *Sol. Energy*, vol. 15, no. 3, pp. 273–276, 1973. [11] R. Santbergen, A. H. M. Smets, and M. Zeman, “Optical model for mul- tilayer structures with coherent, partly coherent and incoherent layers,” *Opt. Express*, vol. 21, no. 102, pp. A262–A267, 2013. [12] B. E. Pieters, J. Krc, and M. Zeman, “Advanced numerical simulation tool ˇ

2006, pp. 1513–1516. for solar cells—ASA5,” in *Proc. IEEE Conf. Photovolt. Energy Convers.*,

[13] M. Zeman, O. Isabella, S. Solntsev, and K. Jager, “Modeling of thin-film ¨ silicon solar cells,” *Sol. Energy Mater. Sol. Cells*, vol. 119, pp. 94–111,

2013.
[14] J. Krc and M. Topi ˇ c,ˇ *Optical Modeling and Simulation of Thin-Film Pho-*

[15] *tovoltaic Devices*

B. Lipovsek, J. Kr ˇ
. Boca Raton, FL, USA: CRC Press, 2013. c, and M. Topi ˇ c, “Optical model for thin-film photo-ˇ voltaic devices with large surface textures at the front side,” *Informacije* *MIDEM*, vol. 41, no. 4, pp. 264–271, 2011. [16] M. Topic, M. Sever, B. Lipov ˇ sek, A. ˇ Campa, and J. Kr ˇ c, “Approaches and ˇ challenges in optical modeling and simulation of thin-film solar cells,” *Sol. Energy Mater. Sol. Cells*, vol. 135, pp. 57–66, 2015. [17] R. Santbergen and R. J. C. van Zolingen, “The absorption factor of crys- talline silicon PV cells: A numerical and experimental study,” *Sol. Energy* *Mater. Sol. Cells*, vol. 92, no. 4, pp. 432–444, 2008. [18] R. Santbergen, J. M. Goud, M. Zeman, J. A. M. van Roosmalen, and R. J.

C. van Zolingen, “The AM1.5 absorption factor or thin-film solar cells,”
[19] Y. Li, Y. Chen, Z. Ouyang, and A. Lennon, “Angular matrix framework *Sol. Energy Mater. Sol. Cells*, vol. 94, no. 5, pp. 715–723, 2010.

for light trapping analysis of solar cells,” *Opt. Express*, vol. 23, no. 24, pp. A1707–A1719, 2015. [20] N. Tucher *et al.*, “Optical simulation of photovoltaic modules with mul- tiple textured interfaces using the matrix-based formalism OPTOS,” *Opt.* *Express*, vol. 24, no. 14, pp. A1083–A1093, 2016. [21] B. T. Phong, “Illumination for computer generated pictures,”*Commun.* *ACM*, vol. 18, no. 6, pp. 311–317, 1975. [22] K. J scattering model for nano-textured interfaces and its application in opto- ager, M. Fischer, R. A. C. M. M. van Swaaij, and M. Zeman, “A ¨

electrical simulations of thin-film solar cells,” *J. Appl. Phys.*, vol. 111, 2012, Art.ID. 083108. [23] K. Jager, “On the scalar scattering theory for thin-film solar cells,” Ph.D. ¨ dissertation, Delft Univ. Technol., Delft, The Netherlands, 2012. doi:

10.4233/uuid:4220e3ee-bdcb-4a46-ade1-470d3c2ad6da.
[24] D. Zhang *et al.*, “Design and fabrication of SiOx/ITO double-layer anti- reflective coating for heterojunction silicon solar cells,” *Sol. Energy Mater.* *Sol. Cells*, vol. 117, pp. 132–138, 2013. [25] F. T. Si *et al.*, “Quadruple-junction thin-film silicon-based solar cells with high open-circuit voltage,” *Appl. Phys. Lett.*, vol. 105, 2014, Art. ID. 063902. [26] H. Tan *et al.*, “Highly efficient hybrid polymer amorphous silicon mul- tijunction solar cells with effective optical management,” *Adv. Mater.*, vol. 28, no. 11, pp. 2170–2177, 2016. [27] Photovoltaic materials and devices laboratory, Delft University of Tech- nology, Software platform. [Online]. Available: [http://www.ewi.tudelft](http://www.ewi.tudelft). nl/en/the-faculty/departments/electrical-sustainable-energy/photovoltaic- materials-and-devices/software-platform/ [28] R. Santbergen, “Manual for solar cell optical simulation software: Gen- Pro4.” [Online]. Available: [http://www.ewi.tudelft.nl/fileadmin/Faculteit/](http://www.ewi.tudelft.nl/fileadmin/Faculteit/) EWI/DocumentenAfdelingen/Electrical_Sustainable_Energy/PVMD/ GenPro4_manual.pdf [29] R. J. Potton, “Reciprocity in optics,” *Rep. Prog. Phys.*, vol. 67, pp. 717– 754, 2004. [30] T. Sasaki, Y. Koi, K. Yamamoto, M. Yoshimi, and M. Ichikawa, “Stacked photoelectric converter,” U.S. Patent 7 550 665 B2, Jun. 23, 2009. [31] C. Ulbrich, A. Gerber, K. Hermans, A. Lambertz, and U. Rau, “Analysis of short circuit current gains by an anti-reflective textured cover on silicon thin film solar cells,” *Prog. Photovolt.*, vol. 21, no. 8, pp. 1672–1681,

2013.
Authors’ photographs and biographies not available at the time of publication.
