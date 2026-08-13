Vol. 27, No. 8 | 15 Apr 2019 | OPTICS EXPRESS A507

# Methodology of energy yield modelling of perovskite-based multi-junction photovoltaics

## RAPHAEL SCHMAGER,

**1,3**

## MALTE LANGENHORST,

**1,3**

## JONATHAN LEHR,

**2**

## ULI LEMMER,

**1,2**

## BRYCE S. RICHARDS,

**1,2** **AND**

## ULRICH W. PAETZOLD

**1,2,***

*1* *Institute of Microstructure Technology, Karlsruhe Institute of Technology, 76344* *Eggenstein-Leopoldshafen, Germany* *2* *Light Technology Institute, Karlsruhe Institute of Technology, 76131 Karlsruhe, Germany* *3* *These authors have contributed equally to this work.* *** *ulrich.paetzold@kit.edu*

**Abstract:** Energy yield (EY) modelling is an indispensable tool to minimize payback time of emerging perovskite-based multi-junction photovoltaics (PV) but it relies on many assumptions about device architecture and environmental conditions. Here, we propose a comprehensive framework that enables rapid simulation of complex architectures of perovskite-based multi- junction PV and detailed calculation of their power output under realistic irradiation conditions in various climatic zones. Applying the framework to perovskite/silicon multi-junction solar modules, we showcase the impact of tracking on energy losses arising from spectral variations. Moreover, we demonstrate the strong dependency of the EY of bifacial multi-junction solar modules on the albedo.

© 2019 Optical Society of America under the terms of the OSA Open Access Publishing Agreement

### 1. Introduction

In order to lower the levelized cost of electricity (LCoE) of photovoltaics (PV) substantially [1], the power output of PV modules needs to increase further. In this regard, perovskite-based tandem PV is currently the focus of attention by researchers and industries world-wide, since the technology promises power conversion efficiencies (PCE) vastly exceeding the limits of the market-dominating single-junction silicon (Si) PV [2]. Companies, such as OxfordPV, are working intensively on a commercial launch of perovskite/Si tandem solar modules having reached an outstanding PCE of 28% on 1 cm² devices [3]. To minimize both the economic and energy payback time at an early phase of development and to predict the performance of PV systems under realistic irradiation conditions, an assessment of the annual energy yield (EY) of the technology in the targetted location is of highest importance. EY modelling has already widely been used for single-junction PV [4–10], concentrator PV [11–16] and III-V/Si multi-junction PV [17–20]. In particular for multi-junction PV, the absorber thicknesses can differ significantly by up to 30% when optimizing the architecture for annual EY rather than PCE under standard test conditions (STC) [21,22]. Consequently, numerous studies have been published discussing various correlations between environment and optimum device parameters of perovskite/CIGS [21], perovskite/Si [22–27] and perovskite/perovskite tandem PV [28]. The level of detail of each EY simulation framework used in the above-mentioned studies varies. Most studies, for instance, employ planar or abstracted device architectures to make more generalized statements about the prediction of realistic performance limitations of perovskite- based tandem solar modules [23–26,29]. Others, however, focus on specific aspects, such as precise modelling of the electrical behavior of multi-junction solar modules [25,26] or light-management foils [27], but then only consider clear sky conditions and disregard cloud cover (CC). The need for an elaborate model of CC has been highlighted by Liu *et al.* [18] reporting on comparative EY studies between measured irradiance spectra and calculated irradiance spectra

#359729 [https://doi.org/10.1364/OE.27.00A507](https://doi.org/10.1364/OE.27.00A507) Journal © Received Feb 2019; revised Mar 2019; accepted Mar 2019; published Apr

Vol. 27, No. | Apr | OPTICS EXPRESS A508

using radiative transfer models, in particular the widely-used ’simple model of atmospheric radiativetransferofsunshine’(SMARTS)[30]. Moreover, veryfewstudiestodateinvestigatedthe crucial question for perovskite/Si multi-junction PV, whether and how much texturing is required to maximize the output of the tandem architecture under realistic irradiation conditions [22]. The different emphases of these studies clearly undermine their comparability and thus highlight the need to establish and communicate a common and comprehensive framework for future EY studies. In particular, the optical modelling of the complex architecture of textured perovskite-basedmulti-junctionsolarmodulesandthemodellingofrealisticirradiationconditions requires methodology with a common framework. Therefore, in this paper, we outline all relevant aspects of the methodology of EY modelling of perovskite-based multi-junction PV. Our framework offers the possibility to simulate complex-textured or planar, monofacial or bifacial-architectures of single- and multi-junction PV, including all perovskite-based tech- nologies (e.g. perovskite/Si, perovskite/CIGS, perovskite/perovskite), other tandem technologies employing III-V or CdTe absorbers, as well as any other absorber material. The circumvention of time-consuming ray-tracing or wave-optical methods allows for rapid and accurate optical simulations without using high performance computing hardware. Our EY framework further provides hourly resolved realistic direct and diffuse irradiation conditions as well as CC in different climatic regions. Moreover, it includes robust modelling of all relevant electrical interconnection schemes of multi-junction PV, such as two-terminal (2T), three-terminal (3T) and four-terminal (4T). In addition, our EY framework also considers both various solar tracking methods as well as bifacial PV modules that can benefit from albedo-the model for the latter is based on the basis of the ECOSTRESS spectral library [31,32].

### 2. Energy Yield Modelling

Under realistic outdoor operation, the most important figure-of-merit to evaluate and compare multi-junction solar modules is the EY. Here, the EY is defined as the total energy generated by the solar module over the course of one (representative) year. The proposed methodology of EY modelling is based on four independent modules (see Fig. 1) providing realistic spectral irradiation covering a broad range of locations in the USA and the optical and electrical response of multi-junction solar modules. This modular EY framework can easily identify trends for specific architectures via the analysis of light-trapping concepts or the evaluation of the electric interconnection schemes, thus providing design rules for device properties (e.g. layer thicknesses) or optimal tilt for various locations.

Fig. 1. Schematic flow of the modular EY modelling. The irradiance module computes the

spectral irradiance *I*, the optics module the absorptance *A*, and the energy yield module calculates the short-circuit current density *J*SCand EY with the help of the electrics module.

1. The **Irradiation Module** calculates the spectral and angular-resolved irradiance over the course of one year with a temporal resolution of one hour by applying SMARTS to typical meteorological year (TMY3) data of locations in various climatic zones. A simple model is employed to account for CC such that realistic direct and diffuse irradiance are derived.
2. The **Optics Module** rapidly calculates the spectrally and angular-resolved absorptance of the non-simplified architecture of multi-junction solar modules. It is able to handle a strong entanglement of multiple planar and textured interfaces with coherent and incoherent light propagation by combining transfer matrix method (TMM) and geometrical ray-tracing.
3. The **Electrical Module** determines the temperature-dependent current density-voltage (*J*-*V*) characteristics accounting for series and shunt resistances for a given short-circuit current density (*J*SC) of the sub-cells forming the multi-junction in either a 2T-, 3T- or 4T-configuration. Furthermore, the maximum power point is determined to calculate the power output of the multi-junction solar module.
4. The **Energy Yield Core Module** calculates the EY over the course of one year of the sub-cells depending on their orientation (rotation and/or tilt of the module) and location. The EY is computed by combining the spectral and angular resolved solar irradiation (with or without albedo), the absorptance of the multi-junction solar module and the electrical properties (see Fig. 2).
Fig. 2. Schematic of energy yield modelling for multi-junction solar modules. The power
 generation of the tilted multi-junction solar module varies with the sun’s specular and diffuse irradiance, which is linked to the location, time, orientation of the solar module and the cloud coverage. For different architectures (monofacial or bifacial) and module installations (albedo), additional contributions of incident light to the generated current need to be considered.

### 3. Realistic irradiation conditions

To determine the annual EY of a specific multi-junction configuration, realistic irradiation data are essential. To assess different climatic regions, the TMY3 data sets, available from the National Renewable Energy Laboratory (NREL), are used [33]. They contain statistically representative hourly resolved meteorological and irradiation data of many locations spread over the USA, representing all relevant climatic zones. Furthermore, for each location, atmospheric properties like the dry-bulb temperature, pressure, precipitable water, aerosol optical depth and albedo are provided. Based on the irradiance, the atmospheric conditions and the position of the sun [34], the spectrally resolved (280 nm - 4000 nm) clear sky irradiance is calculated with SMARTS [30]. Therefore, the Shettle and Fenn’s urban aerosol model and the US standard reference atmosphere are used [35]. Furthermore, the irradiance spectra are enhanced by a simple cloud model with the CC, the value of which is available in the hourly TMY3 data set. Our simple cloud model assumes no spectral change for the direct irradiation. In this case, the direct irradiation *I*clouds,diris determined by the spectral resolved clear sky irradiance *I*clear,dir, which is calculated by the SMARTS code, scaled to the TMY3 measured absolute irradiance *I*meas,dirfor every hour of the year:

<u>I</u> <u>clear,dir„ ”</u> *I* clouds,dir„ ” = fl *I*meas,dir: (1) *I* clear,dir„ ”*d*

The diffuse irradiance is given by the direct and diffuse clear sky irradiance weighted by the CC. The normalized spectral data is again scaled to the measured diffuse irradiance *I*meas,diffof the TMY3 data:

<u>I</u> <u>clear,diff„ ”„1 CC” + Iclear,dir„ ” CC</u> *I* clouds,diff„ ” = fl *I*meas,diff: (2) »*I*clear,diff„ ”„1 CC” + *I*clear,dir„ ” CC…*d*

The direct and diffuse spectrum (average) obtained by this simple cloud model are displayed in Fig. 3(a) for Phoenix (Arizona, USA) for two months of a representative year. For June and December, the direct irradiance exceeds the diffuse irradiance. The large difference in maximum irradiance between summer and winter is a natural consequence of the meteorological conditions of the northern hemisphere. Owing to the strong wavelength dependence of Rayleigh scattering ( 4 ), the diffuse fraction exhibits a strong blue-shift. This blue-shift of the average photon energy (APE) compared to the global standard spectrum (AM1.5g) in Fig. 3(b) is also visible in the morning and evening when the total irradiance is dominated by diffuse irradiance [21,36]. The variation of the incident irradiation mimics realistic operating conditions due to the continuously changing angle of incidence and CC (fluctuating irradiance levels and spectral variations). While the proposed model for CC is rudimentary, it yet provides a possibility to account for the impact of clouds on clear sky diffuse irradiation calculated via SMARTS. The approach of assuming more blue-rich spectral irradiance with decreasing CC is in accordance with the previous study by Bartlett *et al.* [37]. Furthermore, it must be acknowledged that the radiative transfer in clouds is a complex subject [37,38] and yet there is no unified, comprehensive radiative transfer model [39] since the optical properties strongly depend on their size and shape as well as their composition [40].

### 4. Optical modelling

The architecture of state-of-the-art single-junction and multi-junction solar modules demands certain capabilities of the simulation framework to determine its spectral response. Therefore, the optics module needs to accurately handle three distinct features (Fig. 4(a)):

Fig. 3. (a) Monthly average spectral irradiance of Phoenix (Arizona, USA) during June

and December broken down into direct and diffuse portions. (b) Hourly resolved overall intensity of direct and diffuse irradiance and the average photon energy (APE) in November 19th in Phoenix (Arizona, USA).

*1. Multi-layer thin-film stacks*: Thin-film PV technologies-like III-V, copper indium gallium
diselenide (CIGS) and perovskite PV-require a coherent treatment of light propagation in thin-film multi-layer stacks. A proficient and fast method to account for interference of coherent light is TMM. The coherent calculation of the absorptance *A*cohvia TMM has already been discussed extensively in a previous publication [41] and will thus not be discussed further in this work.

*2. "Optically-thick" layers*: In "optically-thick" layers-such as module encapsulation materials
and 200 m-thick Si absorbers-interference does not play an important role and a simple calculation of the absorption in a dielectric via the Beer-Lambert law according to Eqn. (3) is sufficient: 2„ ” d cos13 6 *e* 0 7 6 7 6 ::: 7 *A*incoh„ ”=6 7; (3) 6 7 6 „ ” d cos 7 6 0 *e*n 7 4 5 where, „ ” is the absorption coefficient, *d* the thickness of the incoherent layer, andnthe angle of light propagating in the incoherent layer.

*3. Non-planar interfaces*: The third feature encompasses non-planar interfaces for light
management. In single-junction Si PV, this mostly involves alkaline-etched pyramidally-textured Si wafers or replica of these textures transferred into the module encapsulation. These textures can be handled using geometrical ray-tracing as described by Baker-Finch and McIntosh [42]. This elegant approach allows fast and accurate calculation of the impact of pyramidal textures on the reflectance *R* and transmittance *T* of an interface for all angles of incidence. If the textures are covered with a thin-film multi-layer stack (see Fig. 4(a)), even the impact of the texture on the absorptance of this ’effective interface’, defined from one thick layer to the next one, can be determined. Following the approach of Baker-Finch and McIntosh [42], light can pass through a texture only in a limited set of paths with characteristic intersection anglesintersectat the facets of the pyramids (Fig. 4(b)). The total absorption *A*path;iof a pyramidal texture covered with a

Fig. 4. (a) Illustration of the abstraction levels of the complex architecture of multi-junction

solar modules used for the optical simulation of their spectral response in dependence of the wavelength and the angle of incidencein. A perovskite/Si multi-junction solar module commonly exhibits three distinct features: optically-thick layers, multi-layer thin-film stacks and textures. (b) Textures are simulated using geometrical ray-tracing. The geometry of pyramidally textures only allows a specific set of characteristic light paths.

multi-layer thin-film stack along a path *i* is then defined as:

j maxj 1

|A „;|” = A|;|+|R|;|; A|
|---|---|---|---|---|---|---|
|path;i|in|coh intersect;1||coh j=2 k=1|intersect,k|coh|
|||tex/coh|tex/coh in|coh path;i|in path;i|in|
|||||i|||
|path;i|||||||

path;i in coh intersect;1 coh intersect,k coh intersect, j: (4)

Here, *i* is the index of an individual light path, *R* the reflectance of the thin-film stack obtained fromTMMcalculations, and *j* theindexoffacetshitbylightalongthepath. Thetotalabsorptance of this thin-film covered texture *A* is then determined by summation over all characteristic paths: *A* „; ” = *P* „ ” *A* „; ”; (5)

where, *P* is the probability for light to propagate along path *i*. Thus, the interaction of light with an effective interface that may be textured and/or covered with a multi-layer thin film stack

is described by Eqns. (6) and (7),

2 3 6 *R*; *T*„;1!1” ::: *R*; *T*„;n!1”7 6 7 6 : :: ::: : :: 7 *R*; *T* „ ”=6 7 (6) 6 7 6 7 6 *R*; *T*„;1!n” ::: *R*; *T*„;n!n”7 4 5

||R„;|! ” +|T „; !|” + A|„;|” = 1;|(7)|
|---|---|---|---|---|---|---|---|
|in|backward|in ref|in ref tex/coh i|trans|tex/coh incoh i|in|trans forward|
|in|forward|in backward|in i=0|forward,i|in i=1|backward,i|in|
||in||||in|max||

ref trans where is the angle of the incident light, the angle of back-reflected light, and the angle of transmitted light (see inset Fig. 4). With *R*, *A*, *T* and *A* all necessary information is given to pursue an iterative summation of absorption of all light passes in forward *A* and backward *A* direction through any material as described by Eisenlohr *et al.* [43] and indicated in Fig. 4(b).

max max *A*„; ” = *A* „; ” + *A* „; ” = *A* „; ” + *A* „; ” : (8)

This summation is performed up to a maximum number of iterations *i* at which the power of light passing through the slab of material is vanishing. The obtained total absorptance for each layer *A*„; ” is then a function of the angle of incidence and the wavelength and corresponds to the spectral response of the entire system. To account for the differing spectral response for front and rear illumination of bifacial multi-junction solar modules, the optical modelling has to be performed for each side individually. The outlined combination of geometrical ray-tracing and TMM circumvents the computing- intensive use of rigorous ray-tracing or wave-optical finite-element methods. Thus, it does not rely on high performance computing hardware for rapid simulations (i5-8250u processor: <2 min). However, geometrical ray-tracing restricts the applicable textures to *regular upright*, *random upright* and *inverted* pyramids. The optical response (*R*, *T* and *A*) of other non-pyramidal textures (or effective interfaces) must be calculated specifically by ray-tracing. Since the iterative summation of absorption follows a generic principle, more exotic or even artificial textures can be implemented with ease, though.

### 5. Electrical performance

To derive the power output of the the multi-junction solar module, the electrics module determines the *J*-*V* characteristics for a given short-circuit current density *J*SCwith the one-diode model based on the Shockley diode equation including series *R*sand shunt resistances *R*sh: V +J Rs<u>V + J R</u> <u>s</u> *J*„*V*” = *J*SC*J₀ e*nkTmodule1 (9) *R*sh

with the input parameters: *J₀* dark saturation current density, *n* ideality factor, *k* Boltzmann constant, *T*modulemodule temperature. It should be noted that the collection efficiency of generated charge carriers is considered in the calculation of the *J*SC. Since *T*modulehighly depends on a wide range of parameters, thermal modelling of the absorbers in photovoltaics is a complex matter [44]. For temperature-dependent EY modelling, two important aspects have to be kept in mind. Firstly, empirical modelling of *T*modulebased on the nominal operating cell temperature (NOCT) takes into account that the insolation *S* heats up the module above the ambient temperature *T*ambientaccording to [45,46]:

<u>NOCT 20 C</u> *T*module= *T*ambient+ *S*: (10) 800W/m

The NOCT is defined as *T*moduleat an insolation of 800 W/m², a wind speed of 1 m/s and a ambient temperature 20 C. Secondly, the influence of *T*moduleon the electrical performance is modeled using temperature coefficients *t*VOCJSCOC SC, which are normalized at

||and t|for V|and J|
|---|---|---|---|
|1|V|J|OC|
|||V||
|OC|OC,0|6||
|||J||
|SC|SC,0|6||

*T₀*=25 C and expressed in ppm K [47].

<u>tOC</u> *V* = *V* „1 + „*T T₀*”” (11) 10 <u>tSC</u> *J* = *J* „1 + „*T T₀*”” (12) 10 The use of the Lambert *W* function [48,49] enables the derivation of a closed-form solution for the open-circuit voltage at *T₀* from the transcendental Eqn. (9):

<u>J₀Rsh„JSC+ J₀”Rsh</u> *V*OC,0= „*J*SC+ *J₀*” *R*sh*nV*th*W* exp (13)

||nV|nV||
|---|---|---|---|
|th|th|th||

th th

where the thermal voltage is *V* = *kT*. The voltage *V* of the solar cell at a given temperature *T* is then given by:

<u>J₀Rsh„JSC+ J₀ J”Rsh</u> RT *V*„*J*” =s SC*J*”*R*sh*nV*th*W*

|J R + „J + J₀|exp||V + V|
|---|---|---|---|
|s SC|th|th|OC OC|

OC OC : (14) *nV*th*nV*th

Dependent on the different electrical interconnection schemes (see Fig. 5), the power output of the multi-junction solar module is calculated. For a 2T electrical interconnection, the individual sub-cells are connected in series for which the total current is given by the limiting sub-cell. The total voltage is calculated by the sum of both sub-cells (see Eqn. 14) subtracting losses due to the series resistance of the multi-junction.

Fig. 5. Electrical interconnection of the multi-junction solar module: (a) In the 2T

configuration the two sub-cells are connected in series; (b) in the 3T configuration the the current excess in one of the sub-cells can be extracted; (c) in the 4T configuration both sub-cells are operated at their maximum power point.

The 3T interconnection is substantially more complex. It typically refers to the scenario of a 2T interconnection with an additional contact of the bottom cell that harvests the surplus of current generation in the bottom cell at the photovoltage of the bottom cell. A rudimentary treatment of this scenario neglects changes in the fill factor, which implies that the power conversion efficiency can be calculated in the same way as the 4T interconnection (see also [50]). This 3T model remains oversimplified and is subject to further advances of our framework. In a 4T interconnection the individual sub-cells are connected separately, which eliminates the constraints of current mismatch. In the optics module, an optical coupling layer (air or some refractive index matched insulator) is considered between the bottom electrode of the top solar cell and the top electrode of the bottom solar cell (see Section 4). The total power output is derived by the sum of the individual sub-cells operated at their distinct maximum power point. It should be noted that the device interconnection also induces system-related adaptations such as the number of inverters. For the simplest 2T interconnection of the sub-cells only a single

set of inverters is required. The additional contacts in the 3T and 4T interconnections, however, require a separate extraction of the power of both sub-cells and thus an additional set of inverters. In this way, both sub-cells are electrically decoupled by either contacting the recombination junction of a monolithic architecture [50] or employing advanced architectures based on Si solar cells with interdigitated back contacts [51]. On the other hand, a parallel connection of the top and bottom solar cells results in voltage-matched devices, which require only a single set of inverters [52]. However, this approach requires substantially more complex internal or external interconnections in the case of the 3T and 4T architecture, respectively. All electrical characteristics discussed here rely on the one-diode model. However, in reality, the recombination in the *pn*-junction dominates at lower voltages. Thus, the ideality factor varies as a function of irradiation intensity. Consequently, a more complex two-diode or multi-diode model would be more accurate [53]. Nevertheless, a two-diode model increases complexity in the computation and requires fitting of the additional electrical properties of the second diode [54]. In addition to that, the proposed one-diode model is sufficiently accurate as it differs by less than 1% compared to experimental data [55]. So far system-related aspects, such as ohmic losses, inverter losses, and energy storage losses [9], are disregarded. In general, thorough studies will have to include an in-depth uncertainty analysis of the investigated parameters.

### 6. Calculation of annual EY

The annual EY of the multi-junction solar module is derived by the interplay between the above described modules that calculate: the realistic irradiance data, the spectral and the electrical response of the multi-junction solar modules. The EY core module manages these inputs (see Fig.

1) and offers various additional features: (i) static tilt of the solar module; (ii) 1- and 2-axis sun tracking; (iii) albedo; (iv) mono- or bifacial solar modules; and (v) 2T, 3T and 4T interconnection schemes. The EY is calculated with a temporal resolution of one hour, which equates to the same resolution of the irradiance data. This is indispensable when considering tracking and targeting realistic modelling of outdoor performances of multi-junction solar modules [17,18].
*6.1. Short-circuit current density monofacial* The short-circuit current *J*SCis calculated for the direct and diffuse irradiation separately. For a rotated and titled solar module, the incident polar anglesunand azimuth angle ’sunof the sun are expressed in the local coordinate system of the solar module as follows:
! 0 (15) sun sun

’sun! ’sun 0 : (16)

The rotated sun coordinates **S⁰** are obtained by a quaternion **q** rotation about the corresponding

|Euler angle|about the Euler axis, given by:|||||||
|---|---|---|---|---|---|---|---|
||0|1||e x|y|e z||
||||dir|||||
||||SC|||||
||dir|||||||
|0||0|0|0||||
|sun||sun|sun|sun||||
|SC dir||sun 0|sun 0||sun 0|sun 0 sun 0||
||0 0|||||||

e

**S** = **qSq** with **q** = cos + „*S* **x** + *S* **y** + *S* **z**” sin : (17) 2 2

The direct short-circuit current density *J* is then derived via integration over the wavelength of the product of the collection efficiency, the absorptance *A* of the corresponding sub-cell, the direct irradiation *I* and the cosine of angle between the sun and the normal of the solar module cos„ ” for all angles < 90 and for „;’ ” = 1: „ <u>q</u> *J* = „ ”*A*„;”*I*dir„ ” cos„ ”*d*; < 90; „;’ ” = 1 : (18) *hc*

The function „;’ ” herein defines the allowed angles of incidence in the local coordinate system of the solar module, which corresponds to the the upper hemisphere in the non-rotated

coordinate system. is one for angles from where light can reach the solar module, and zero for any other angle. Furthermore, the elementary charge, the Planck constant and the speed of light are denoted by *q*, *h* and *c*. For the diffuse irradiation a Lambertian distribution of the light over the upper hemisphere is assumed. The diffuse short-circuit current density *J* SC diff is therefore obtained by the additional integration over the polar and azimuthal angles: » <u>q</u>

|diff|0|0 0|0|0 0 0|
|---|---|---|---|---|
|SC|diff||||

*J* = „ ”*A*„;”*I* „ ” „;’ ” sin„ ” cos„ ”*d*’ *d d* (19) *hc*

*6.2. Albedo for monofacial solar modules* Tilting a monofacial single- or multi-junction solar module leads to a decreased angular region of direct and diffuse irradiation originated from the upper hemisphere which is described by. However, an additional diffuse reflection of the solar irradiation from the ground (lower hemisphere) to the front side of the multi-junction solar module can be considered. Depending on the ground surface, different reflectivities of the ground are extracted from the ECOSTRESS spectral library, which contain over 3400 spectra of natural and man-made materials [31,32]. A Lambertian distribution of the ground-reflected light is assumed and the albedo is scaled by the level of direct and diffuse irradiance. The additional current by charge carriers generated by the albedo are added to the total short-circuit current density of the top and bottom solar cells. The contribution of albedo to *J*
SC tot is non-zero for tilted modules only, and is given by:

||tot|dir|diff|diff,albedo-front|
|---|---|---|---|---|
||SC|SC|SC|SC|

*J* = *J* + *J* + *J* : (20)

*6.3. Bifacial solar modules* For bifacial single- and multi-junction solar modules, an additional simulation for the absorption properties for backside illumination is performed by the optics module. It should be noted that may differ for illumination from the front and rear side, but in the following showcases we assumed to be unity for both sides. Now, three additional contributions to the total short-circuit current density are present (see Fig. 2). Firstly, the albedo impinging on the back side of the bifacial multi-junction solar module, secondly, the direct sunlight and thirdly the diffuse sunlight reaching the back side of the bifacial multi-junction solar module. Those three contributions become only relevant for tilted modules.

|tot|dir|diff|diff,albedo-front|diff,albedo-back|dir,back|diff,back|
|---|---|---|---|---|---|---|
|SC|SC|SC|SC|SC|SC|SC|
 *J* = *J* + *J* + *J* + *J* + *J* + *J* : (21) In PV module installations, the reduction of the contribution of albedo to the short-circuit current density by self-shading effects must be considered as well. The self-shading mainly scales with the module installation height and is implemented according to the light-collection model introduced by Sun *et al.* [56]. Due to the complexity of self-shading of bifacial solar modules, this issue is disregarded in the following demonstration.
*6.4. Short-circuit current density for tracking* The EY of the multi-junction solar modules can either be analyzed for a static tilt or a dynamic tracking. Tracking the sun with the solar module and therefore steadily optimizing the harvested solar irradiation will increase the EY [57]. To model the impact on EY, single-axis (1-axis) and dual-axis (2-axis) tracking are implemented. General predictions with average or integrated spectral data on realistic outdoor performance are very complicated [9,18,58]. The high temporal resolution and precise spectral information enables an in-depth analysis of different 1-axis and 2-axis tracking.

### 7. Demonstration of the EY framework: perovskite/Si multi-junction PV

Todemonstratetheversatilityofthepresentedframework, weshowcasedifferenttrackingmethods for a 2T perovskite/Si multi-junction solar module in the following (see Fig. 6). Here, we provide an investigation on how tracking affects the relative energy loss due to current mismatch caused by spectral variations. Furthermore, the EY of perovskite/Si tandem solar module with different electrical interconnections (2T, 3T and 4T) are compared for various locations. Finally, the EY in a 4T monofacial and bifacial architecture is validated on the impact of different albedos (see Fig.

7). For the calculation of the module temperature according to Eqn. (10), we assume a typical NOCT of 48 C [46]. For 1-axis tracking, we consider a solar module, which is able to rotate around a fixed axis. We restrict ourselves to two configurations. On the one hand, a rotation around the zenith, where the tilted solar module describes a movement from east to west, and, on the other hand, a fictitious tilted axis from south to north, around which the solar module is rotated dependent on the sun’s position from east to west (see Fig. 6(a)). In both cases, the normal of the solar module follows the azimuth angle ’sunof the sun. For 2-axis tracking, we consider the solar module to follow the exact sun’s position. The different tracking methods are evaluated for a 2T perovskite/Si multi-junction solar module and are compared to a fixed optimal tilt and to the module lying horizontally on the ground. The layer stack is adapted from our previous study (see Lehr *et* *al.* [22]) and the EY modelling is conducted for Phoenix (Arizona, USA). To assess the potential of different tracking methods, the layer thicknesses are kept constant. It should be noted, that minor enhancements are expected by further optimizing the layers for each tracking. Compared to an optimized, fixed tilt angle, a 1-axis tracking and a permanent tracking of the sun’s position (2-axis, sun follow) are superior and show an improvement in annual EY of 23% and 32%, respectively. Especially about noon, the optimal tilt clearly exhibits a higher EY compared to the horizontal module, since the tilt allows absorption of more intense direct sunlight at angles closer to the normal (see Fig. 6(c)). As apparent in Fig. 6(d), the sun’s position always changes (sun,sun). Thus, a 1-axis tracking of the sun by the solar module is more advantageous than a fixed tilt. Consequently, the EY is further enhanced by an additional rotation of the solar module around the zenith compared to a fixed, optimally tilted solar module (see
Fig. 6(a),(c)). A rotation around a tilted axis from south to north (meaning an east-west tilt),
 enhances the power generation particularly in the morning and in the evening, where the sun is rising and setting. Overall, the difference between the two 1-axis tracking methods (’zenith rotation’ and ’east-west tilt’) sums up to 2%, highlighting that a small but significant gain in EY is achievable by an appropriate choice of module installation. To highlight the importance of tracking in the context of perovskite/Si multi-junction PV, we showcase that tracking not only changes the total irradiance on the solar module, but also the spectrum of incident irradiation, which is described by the average utilizable photon energy (AUPE). This AUPE – a key parameter for the performance of tandem PV – is defined as the APE of photons with energies above the bandgap of the Si absorber and that are incident on the front side of the tandem solar module. As illustrated for a chosen day (June 14th) in Fig. 6(e), tracking significantly reduces the AUPE in the early morning (6:00) and in the late afternoon (19:00). This effect arises from the increased share of direct irradiation (low APE), when tracking the sun’s position, since the majority of diffuse irradiation with a high APE is lost on the rear side of a monofacial tandem solar module in the morning and evening hours. Contrary, for optimal tilt, diffuse irradiation (high APE) dominates the incident irradiation at these hours of the day leading to an increase in AUPE. Comparing the *J*SCof both sub-cells of a 2T perovskite/Si tandem solar module for the chosen day (see Fig. 6(f)), it is apparent that the current generation at optimal tilt (green) is higher in the top sub-cell at all times. Contrary to that, when operating this tandem solar module with 2-axis tracking (red), this persistent trend reverses when the AUPE gets closer to the bandgap of

Fig. 6. EY of a perovskite/Si multi-junction solar module for different tracking methods for a
 single day and the complete year in Phoenix (Arizona, USA). (a) Schematic of two different 1-axis tracking methods; (b) the angular EY; (c) the EY for a chosen day (November 19th);
(d) the sun’s polarsunand azimuth angle ’sun as well as the direct and diffuse irradiance for the same day; (e) the average usable photon energy (AUPE) for a chosen day (June 14th) and (f) *J*SCof the top and bottom solar cell for optimal tilt (green) and 2-axis tracking (red) for the same chosen day (June 14th).
the perovskite top absorber (see circles in Fig. 6 (e) and (f)). In total, the annual energy loss due to current mismatch amounts to 44.0 kWhm 2 a 1 and 51.2 kWhm 2 a 1, for optimal tilt and 2-axis tracking, respectively. This correlates to a reduction in current mismatch loss from 7.5% to 6.7%, with regard to the actual annual EY by employing 2-axis tracking. In conclusion, these observations reveal that tracking methods lower the relative energy loss due to current mismatch

caused by spectral variations. Besides tracking methods, the electrical connection scheme affects the annual EY of the 2T, 3T and 4T architecture of perovskite/Si solar modules differently. Therefore, we compare the 2T double-side textured perovskite/Si solar module described above under optimal tilt (as already reported in Lehr *et al.* [22]) to the same monolithic architecture with a 3T interconnection and mechanically stacked 4T architectures. In the 4T architecture, the required intermediate insulation and the front electrode of the bottom Si sub-cell increases parasitic reflection and absorption losses (see Fig. 7(a) and (b)). Overall, the annual EY of perovskite/Si solar modules is highly dependent on the location (see Fig. 7(c)). In the northern (temperate and boreal) regions the annual EY is lower, compared to the southern more tropical or arid locations. Employing 3T or 4T electrical interconnection avoids the current mismatch characteristic for 2T, and thus leads to an average increase in EY by 7% and 4% for all considered locations for the 3T and 4T architecture, respectively. However, it should be noted that these values only consider the optical performance and more the sophisticated grid connection for both the 3T and 4T architecture is not considered. This will possibly results in the 2T architecture realizing a lower LCoE. These small-but-significant differences in power output reveal that there is still room for improvement by enhancing the transmission of the transparent electrodes and insulating layers as well as further light management to reduce reflection losses of multi-junction solar modules.

Fig. 7. Absorptance of the individual layers in the (a) 2T and the (b) 4T multi-junction solar

modules. (c) Annual EY for four locations with different climatic conditions: temperate (Portland, Oregon), tropical (Miami, Florida), boreal (Chicago, Illinois), and arid (Phoenix, Arizona) for a 2T, 3T and 4T monofacial perovskite/Si solar module. (d) Annual EY for a monofacial and bificial 4T perovskite/Si solar module with three different ground surfaces (sandstone, grass and concrete) leading to different albedos.

Another topic of interest are bifacial perovskite/Si multi-junction solar modules. Compared to a monofacial 4T perovskite/Si multi-junction solar module in Phoenix (Arizona), the annual EY is increased by 3% for the bifacial architecture, since additional direct and diffuse irradiation directly incident on the rear side of the solar module can now be absorbed (see Fig. 7(d) ’no albedo’). While the impact of additional albedo for the monofacial solar module is negligible (EY increases by 1%), the strong impact of albedo on the EY is apparent in the case of a bifacial solar module. Additionally, the origin of albedo (sandstone, grass, concrete, etc.) plays an important role for the annual EY of bifacial solar modules. In particular, grass-covered ground contributes another 20% to the annual EY, while sandstone (6%) and concrete (18%) exhibit lower contributions due to overall lower reflectance. These results highlight the strong impact of environmental conditions on the annual EY of bifacial multi-junction solar modules.

### 8. Conclusion

Since STC are not suitable for credible predictions on LCoE of advanced multi-junction solar modules under realistic outdoor operations, sophisticated and detailed EY modelling is required. In this work, we present the methodology of EY modelling for PV with a strong focus on perovskite-based multi-junction solar modules. We further construct a common framework for future studies to model realistic outdoor performances of multi-junction solar modules. The outlined framework subdivides and encompasses an irradiance, an optics and an electrics module. The modular subdivision enables fast and versatile calculations and predictions as well as rapid implementation of experimental data. The key features of the introduced irradiance model are the high temporal (hourly resolved) and spectral (280 nm - 4000 nm) resolution of the irradiance data for various locations in the USA (1020 locations), which cover all relevant climatic zones. The optics module stands out by fast calculations of angular and spectral absorptance of non-simplified complex single- and multi-junction solar modules, combining coherent and incoherent light propagation as well as planar and textured interfaces, which is crucial for 2T perovskite/Si PV. The electrical module enables the rapid calculation of temperature-dependent multi-junction solar modules employing various interconnection schemes accounting for series and shunt resistances. The interaction of the three modules is handled by the EY core module, which is calculating the annual EY for the given input parameters for static rotations or tilts, dynamic 1-axis or 2-axis tracking methods accounting for albedo and current generation in monofacial as well as bifacial multi-junction solar modules. Furthermore, the ability of the presented EY modelling is demonstrated at the example of different tracking methods, for which distinct trends are recognizable. In contrast to a horizontal perovskite/Si multi-junction solar module, an optimal tilt enhances the EY by 10%. Compared to an optimally tilted perovskite/Si multi-junction solar module, a 1-axis tracking and 2-axis tracking of the sun increases the annual EY by 23% and 32%, respectively. This improvement mainly originates from improved light harvesting in the morning and late afternoon for 1-axis tracking, and improved EY throughout the whole day for 2-axis tracking. The difference between various 1-axis tracking methods is small (2%) but not negligible, though. Beyond the basic application of tracking methods, we showcase the outstanding capabilities of our framework by investigating the impact of tracking methods on energy loss for 2T perovskite/Si tandem solar modules arising from spectral variations for a chosen day. We demonstrate the reductionoftherelativeannualenergylossduetocurrentmismatchfrom7.5%to6.7%originating from a change in AUPE by 2-axis tracking. Moreover, the investigation of 2T, 3T and 4T perovskite/Si multi-junction solar modules reveals potential for further optimization of the electrical interconnection of multi-junction PV. Bifacial solar modules also are an option to improve the power output of perovskite/Si multi-junction PV but the relative gain in EY of this technology strongly depends on the origin of albedo

(sandstone, grass, concrete). Overall, the identification of these trends in EY highlights the value of a comprehensive EY modelling framework.

### Funding

Helmholtz Association, "Science and Technology of Nanosystems" (STN), HYIG of U.W. Paetzold (FKZ VH-NG-1148), PEROSEED (FKZ ZT-0024), German Federal Ministry for Education and Research (BMBF), PRINTPERO (FKZ 03SF0557A), Karlsruhe School of Optics & Photonics (KSOP).

### References

1. C. Kost, J. N. Mayer, J. Thomsen, N. Hartmann, C. Senkpiel, S. Philipps, S. Nold, S. Lude, N. Saad, and T. Schlegel, “Levelized cost of electricity: Renewable energy technologies,” Tech. Rep. March, Fraunhofer-Institut für Solare Energiesysteme ISE (2018).
2. K. Yoshikawa, W. Yoshida, T. Irie, H. Kawasaki, K. Konishi, H. Ishibashi, T. Asatani, D. Adachi, M. Kanematsu,
H. Uzu, and K. Yamamoto, “Exceeding conversion efficiency of 26% by heterojunction interdigitated back contact solar cell with thin film Si technology,” Sol. Energy Mater. Sol. Cells **173**, 37–42 (2017).
3. “Perovskite world record of 28% | Oxford PV,” [https://www.oxfordpv.com/news/oxford-pv-perovskite-solar-cell-](https://www.oxfordpv.com/news/oxford-pv-perovskite-solar-cell-) achieves-28-efficiency.
4. Y. Hirata and T. Tani, “Output variation of photovoltaic modules with environmental factors-I. The effect of spectral solar radiation on photovoltaic module output,” Sol. Energy **55**, 463–468 (1995).
5. R. Gottschalg, T. Betts, D. Infield, and M. Kearney, “The effect of spectral variations on the performance parameters of single and double junction amorphous silicon solar cells,” Sol. Energy Mater. Sol. Cells **85**, 415–428 (2005).
6. M. Alonso-Abella, F. Chenlo, G. Nofuentes, and M. Torres-Ramírez, “Analysis of spectral effects on the energy yield of different PV (photovoltaic) technologies: The case of four specific sites,” Energy **67**, 435–443 (2014).
7. G. S. Kinsey, “Spectrum Sensitivity, Energy Yield, and Revenue Prediction of PV Modules,” IEEE J. Photovoltaics **5**, 258–262 (2015).
8. S. Senthilarasu, E. F. Fernández, F. Almonacid, and T. K. Mallick, “Effects of spectral coupling on perovskite solar cells under diverse climatic conditions,” Sol. Energy Mater. Sol. Cells **133**, 92–98 (2015).
9. O. Isabella, R. Santbergen, H. Ziar, A. Calcabrini, J. C. O. Lizcano, E. G. Goma, P. Nepal, V. Schepel, and M. Zeman, “Advanced modelling of e/uipv systems from location to load,” in *2018 IEEE 7th World Conference on Photovoltaic* *Energy Conversion (WCPEC)(A Joint Conference of 45th IEEE PVSC, 28th PVSEC & 34th EU PVSEC),* (IEEE,
2018), pp. 2691–2696.
10. A. Calcabrini, H. Ziar, O. Isabella, and M. Zeman, “A simplified skyline-based method for estimating the annual solar energy potential in urban environments,” Nat. Energy p. 1 (2019).
11. K. Araki and M. Yamaguchi, “Influences of spectrum change to 3-junction concentrator cells,” Sol. Energy Mater. Sol. Cells **75**, 707–714 (2003).
12. G. S. Kinsey and K. M. Edmondson, “Spectral response and energy output of concentrator multijunction solar cells,” Prog. Photovoltaics: Res. Appl.**17**, 279–288 (2009).
13. S. Philipps, G. Peharz, R. Hoheisel, T. Hornung, N. Al-Abbadi, F. Dimroth, and A. Bett, “Energy harvesting efficiency of III-V triple-junction concentrator solar cells under realistic spectral conditions,” Sol. Energy Mater. Sol. Cells **94**, 869–877 (2010).
14. X. Wang and A. Barnett, “The Effect of Spectrum Variation on the Energy Production of Triple-Junction Solar Cells,” IEEE J. Photovoltaics **2**, 417–423 (2012).
15. N.L.A.Chan,T.B.Young,H.E.Brindley,N.J.Ekins-Daukes,K.Araki,Y.Kemmoku,andM.Yamaguchi,“Validation of energy prediction method for a concentrator photovoltaic module in Toyohashi Japan,” Prog. Photovoltaics: Res. Appl.**21**, 1598–1610 (2013).
16. E. F. Fernández, F. Almonacid, J. Ruiz-Arias, and A. Soria-Moya, “Analysis of the spectral variations on the performance of high concentrator photovoltaic modules operating under different real climate conditions,” Sol. Energy Mater. Sol. Cells **127**, 179–187 (2014).
17. H. Liu, Z. Ren, Z. Liu, A. G. Aberle, T. Buonassisi, and I. M. Peters, “The realistic energy yield potential of GaAs-on-Si tandem solar cells: a theoretical case study,” Opt. Express **23**, A382 (2015).
18. H. Liu, A. G. Aberle, T. Buonassisi, and I. M. Peters, “On the methodology of energy yield assessment for one-Sun tandem solar cells,” Sol. Energy **135**, 598–604 (2016).
19. H. Liu, Z. Ren, Z. Liu, A. G. Aberle, T. Buonassisi, and I. M. Peters, “Predicting the outdoor performance of flat-plate III-V/Si tandem solar cells,” Sol. Energy **149**, 77–84 (2017).
20. H. Schulte-Huxel, T. J. Silverman, M. G. Deceglie, D. J. Friedman, and A. C. Tamboli, “Energy Yield Analysis of Multiterminal Si-Based Tandem Solar Cells,” IEEE J. Photovoltaics **8**, 1376–1383 (2018).
21. M. Langenhorst, B. Sautter, R. Schmager, J. Lehr, E. Ahlswede, M. Powalla, U. Lemmer, B. S. Richards, and U. W. Paetzold, “Energy yield of all thin-film perovskite/CIGS tandem solar modules,” Prog. Photovoltaics: Res. Appl. (2018).

22. J. Lehr, M. Langenhorst, R. Schmager, S. Kirner, U. Lemmer, B. S. Richards, C. Case, and U. W. Paetzold, “Energy yield modelling of perovskite/silicon two-terminal tandem PV modules with flat and textured interfaces,” Sustain. Energy & Fuels **2** (2018).
23. M. H. Futscher and B. Ehrler, “Efficiency Limit of Perovskite/Si Tandem Solar Cells,” ACS Energy Lett.**1**, 863–868 (2016).
24. M. H. Futscher and B. Ehrler, “Modeling the Performance Limitations and Prospects of Perovskite/Si Tandem Solar Cells under Realistic Operating Conditions,” ACS Energy Lett.**2**, 2089–2095 (2017).
25. M. T. Hörantner and H. J. Snaith, “Predicting and optimising the energy yield of perovskite-on-silicon tandem solar cells under real world conditions,” Energy & Environ. Sci.**10**, 1983–1993 (2017).
26. O. Dupré, B. Niesen, S. De Wolf, and C. Ballif, “Field Performance versus Standard Test Condition Efficiency of Tandem Solar Cells and the Singular Case of Perovskites/Silicon Devices,” The J. Phys. Chem. Lett.**9**, 446–458 (2018).
27. M. Jošt, E. Köhnen, A. B. Morales-Vilches, B. Lipovšek, K. Jäger, B. Macco, A. Al-Ashouri, J. Krč, L. Korte, B. Rech,
R. Schlatmann, M. Topič, B. Stannowski, and S. Albrecht, “Textured interfaces in monolithic perovskite/silicon tandem solar cells: advanced light management for improved efficiency and energy yield,” Energy & Environ. Sci. (2018).
28. M. T. Hörantner, T. Leijtens, M. E. Ziffer, G. E. Eperon, M. G. Christoforo, M. D. McGehee, and H. J. Snaith, “The Potential of Multijunction Perovskite Solar Cells,” ACS Energy Lett.**2**, 2506–2513 (2017).
29. P. Faine, S. R. Kurtz, C. Riordan, and J. Olson, “The influence of spectral solar irradiance variations on the performance of selected single-junction and multijunction solar cells,” Sol. Cells **31**, 259–278 (1991).
30. C. A. Gueymard, “Parameterized transmittance model for direct beam and circumsolar spectral irradiance,” Sol. Energy **71**, 325–346 (2001).
31. A. Sucich, T. Snyder, R. S. Bittencourt, E. H. Cirilo, J. Madajian, Y. Wang, B. Miller, P. Srinivasan, P. Lubin, and G. B. Hughes, “Experimental design for remote laser evaporative molecular absorption spectroscopy sensor system concept,” in *CubeSats and NanoSats for Remote Sensing II,* vol. 10769 (International Society for Optics and Photonics, 2018), p. 107690O.
32. A. Baldridge, S. Hook, C. Grove, and G. Rivera, “The aster spectral library version 2.0,” Remote. Sens. Environ.**113**, 711–715 (2009).
33. S. Wilcox and W. Marion, *Users manual for TMY3 data sets* (National Renewable Energy Laboratory Golden, CO,
2008).
34. I. Reda and A. Andreas, “Solar position algorithm for solar radiation applications,” Sol. energy **76**, 577–589 (2004).
35. E. P. Shettle and R. W. Fenn, “Models for the aerosols of the lower atmosphere and the effects of humidity variations on their optical properties,” Tech. rep., Air Force Geophysics Lab Hanscom Afb Ma (1979).
36. O. Dupré, B. Niesen, S. De Wolf, and C. Ballif, “Field performance versus standard test condition efficiency of tandem solar cells and the singular case of perovskites/silicon devices,” The journal physical chemistry letters **9**, 446–458 (2018).
37. J. S. Bartlett, Á. M. Ciotti, R. F. Davis, and J. J. Cullen, “The spectral effects of clouds on solar irradiance,” J. Geophys. Res. Ocean.**103**, 31017–31031 (1998).
38. C. Osterwald, K. Emery, and M. Muller, “Photovoltaic module calibration value versus optical air mass: the air mass function,” Prog. Photovoltaics: Res. Appl.**22**, 560–573 (2014).
39. H. H. Aumann, X. Chen, E. Fishbein, A. Geer, S. Havemann, X. Huang, X. Liu, G. Liuzzi, S. DeSouza-Machado,
E. M. Manning *et al.*, “Evaluation of radiative transfer models with clouds,” J. Geophys. Res. Atmospheres **123**, 6142–6157 (2018).
40. X. Liu, Q. Yang, H. Li, Z. Jin, W. Wu, S. Kizer, D. K. Zhou, and P. Yang, “Development of a fast and accurate PCRTM radiative transfer model in the solar spectral region,” Appl. Opt.**55**, 8236 (2016).
41. S. J. Byrnes, “Multilayer optical calculations,” [http://arxiv.org/abs/1603.02720](http://arxiv.org/abs/1603.02720).
42. S. C. Baker-Finch and K. R. McIntosh, “Reflection of normally incident light from silicon solar cells with pyramidal texture,” Prog. Photovoltaics: Res. Appl.**19**, 406–416 (2011).
43. J. Eisenlohr, N. Tucher, O. Höhn, H. Hauser, M. Peters, P. Kiefel, J. C. Goldschmidt, and B. Bläsi, “Matrix formalism for light propagation and absorption in thick textured optical sheets,” Opt. Express **23**, A502 (2015).
44. M. K. Fuentes, “A simplified thermal model for flat-plate photovoltaic arrays,” Tech. rep., Sandia National Labs., Albuquerque, NM (USA) (1987).
45. R. G. Ross Jr, “Flat-plate photovoltaic array design optimization,” in *14th IEEE Photovoltaic Specialists Conference,* (San Diego, CA, 1980), pp. 1126–1132.
46. R. G. Ross Jr and M. I. Smokler, “Flat-Plate Solar Array Project: Final Report: Volume 6, Engineering Sciences and Reliability,” Tech. rep., Jet Propulsion Lab., Pasadena, CA (USA) (1986).
47. O. Dupré, R. Vaillon, and M. Green, “Physics of the temperature coefficients of solar cells,” Sol. Energy Mater. Sol. Cells **140**, 92–100 (2015).
48. A. Jain and A. Kapoor, “Exact analytical solutions of the parameters of real solar cells using lambert w-function,” Sol. Energy Mater. Sol. Cells **81**, 269–277 (2004).
49. X. Gao, Y. Cui, J. Hu, G. Xu, and Y. Yu, “Lambert w-function based exact representation for double diode model of solar cells: Comparison on fitness and parameter extraction,” Energy Convers. Manag.**127**, 443–460 (2016).
50. T. Tayagaki, K. Makita, R. Oshima, H. Mizuno, and T. Sugaya, “Analysis of luminescence coupling effect in

three-terminal tandem solar cells,” J. Photonics for Energy **8**, 1 (2018).

51. G. W. Adhyaksa, E. Johlin, and E. C. Garnett, “Nanoscale back contact perovskite solar cell design for improved tandem efficiency,” Nano letters **17**, 5206–5212 (2017).
52. T. Trupke and P. Würfel, “Improved spectral robustness of triple tandem solar cells by combined series/parallel interconnection,” J. applied physics **96**, 2347–2351 (2004).
53. A. M. Humada, M. Hojabri, S. Mekhilef, and H. M. Hamada, “Solar cell parameters extraction based on single and double-diode models: A review,” Renew. Sustain. Energy Rev.**56**, 494–509 (2016).
54. N. M. A. A. Shannan, N. Z. Yahaya, and B. Singh, “Single-diode model and two-diode model of pv modules: A comparison,” in *Control System, Computing and Engineering (ICCSCE), 2013 IEEE International Conference on,* (IEEE, 2013), pp. 210–214.
55. M. de Blas, J. Torres, E. Prieto, and A. GarcÄśÌĄa, “Selecting a suitable model for characterizing photovoltaic devices,” Renew. Energy **25**, 371–380 (2002).
56. X. Sun, M. R. Khan, C. Deline, and M. A. Alam, “Optimization and performance of bifacial solar modules: A global perspective,” Appl. Energy **212**, 1601–1610 (2018).
57. H. Mousazadeh, A. Keyhani, A. Javadi, H. Mobli, K. Abrinia, and A. Sharifi, “A review of principle and sun-tracking methods for maximizing solar systems output,” Renew. sustainable energy reviews **13**, 1800–1818 (2009).
58. M. Alonso-Abella, F. Chenlo, G. Nofuentes, and M. Torres-Ramírez, “Analysis of spectral effects on the energy yield of different pv (photovoltaic) technologies: The case of four specific sites,” Energy **67**, 435–443 (2014).
