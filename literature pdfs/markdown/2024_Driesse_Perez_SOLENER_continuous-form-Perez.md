Solar Energy 267 (2024) 112093

Contents lists available atScienceDirect

# Solar Energy

journal homepage:www.elsevier.com/locate/solener

# A continuous form of the Perez diffuse sky model for forward and reverse transposition

a b,∗ c Anton Driesse, Adam R. Jensen, Richard Perez a *PV Performance Labs, Freiburg, Germany* b *Department of Civil and Mechanical Engineering, Technical University of Denmark, Kgs. Lyngby, Denmark* c *Atmospheric Sciences Research Center, University at Albany, State University of New York, Albany, NY, USA*

A R T I C L E I N F O A B S T R A C T

*Keywords:* The Perez 1990 transposition model has emerged as the preferred choice for estimating global tilted irradiance, Solar energy also known as plane-of-array irradiance. One notable drawback is the Perez model’s reliance on empirical Transposition coefficients assigned to discrete bins of the sky clearness parameter, resulting in discontinuities in the calculated Photovoltaic (PV) tilted irradiance. In this study, we present a novel method to eliminate the discontinuities of the Perez model Performance modeling by replacing the empirical look-up table with a set of six quadratic splines. This is facilitated by transforming Irradiance the unbounded sky clearness parameter (epsilon) to an equivalent bounded parameter (zeta). Transposition using the original Perez model and continuous Perez–Driesse model are compared for multiple orientations at two locations. The two models produce very similar deviation statistics, meaning the continuous version can be used as a plug-in replacement for the original. Reverse transposition is demonstrated using the Perez–Driesse model together with a new continuous version of the Erbs diffuse fraction model and a simple bisection solution search. This combination achieves a substantially higher success rate than the GTI-DIRINT algorithm in our tests.

**1. Introduction** Knowledge of the solar resource is important for a range of differ- ent fields, for example, within solar energy, agriculture, and climate modeling. For solar energy applications, the quantity of interest is typically the global tilted irradiance (GTI), i.e., the incident energy on a panel that can be used for energy conversion. For photovoltaic (PV) systems this quantity is also commonly referred to as plane-of-array irradiance (POA). The global tilted irradiance depends on the specific panel orientation and differs from the commonly available irradiance components (global horizontal, diffuse horizontal, and direct normal irradiance). Consequently, solar radiation models have been developed to pre- dict tilted irradiance from the commonly available irradiance com- ponents. These models are called transposition models and provide estimates of the incident irradiance for any arbitrarily oriented surface (see [1] for classification of radiation models). Transposition models typically require inputs of diffuse horizontal irradiance (DHI) and direct normal irradiance (DNI) in addition to geometrical parameters, including the solar zenith angle and orientation of the tilted surface. The most common approach is to model tilted irradiance as consist- ing of three separate components: direct irradiance, diffuse irradiance ∗ Corresponding author. *E-mail address:* arajen@dtu.dk(A.R. Jensen). [https://doi.org/10.1016/j.solener.2023.112093](https://doi.org/10.1016/j.solener.2023.112093) Available online 2 December 2023 ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)).
from the sky, and diffuse irradiance reflected from the ground. Deter- mining the incident direct radiation on a surface requires only sim- ple geometrical calculations when the direct irradiance is known [2]. Several methods exist for estimating the ground-reflected diffuse irra- diance with the majority of studies assuming this contribution to be isotropic [3]. Determining the incident sky diffuse irradiance, however, is significantly more complex, as the sky diffuse radiance is highly variable in both time and space. As pointed out by several studies, the sky diffuse irradiance cannot reasonably be assumed isotropic for the purpose of transposition (e.g., Hay and McKay [4]), but rather it is imperative that the main anisotropic effects are accounted for. Numerous anisotropic sky diffuse transposition models have been proposed during the past decades, with varying degrees of complexity and accuracy. The performance of these models has been investigated in several studies, with the majority finding the Perez et al. [5] model to perform best. For example, Yang [6] compared 26 transposition models using measurement data for four sites and concluded that the Perez1990model ranked best overall. David et al. [7] came to the same conclusion after evaluating four transposition models by com- parison to irradiance measurements on 14 tilted planes at Le Reunion Island. Ineichen [8] compared eight different transposition models

Received 31 August 2023; Received in revised form 24 September 2023; Accepted 7 October 2023

0038-092X/© 2023 The Authors. Published by Elsevier Ltd on behalf of International Solar Energy Society. This is an open access article under the CC BY license

*A. Driesse et al.* **Nomenclature** **Latin letters** *𝑎* Weighted solid angle (circumsolar) [–] *𝑏* Weighted solid angle (horizon) [–]
2 *𝐷𝑐*In-place sky diffuse irradiance [W/m] *𝐷𝑔*In-plane ground reflected irradiance [W/m2] *𝐷ℎ*Diffuse horizontal irradiance (DHI) [W/m2] *𝐹* Anisotropic coefficient [–] *𝐹* 1Circumsolar brightening coefficient [–] *𝐹* 2Horizon/zenith brightening coefficient [–] *𝐺𝑐*Global tilted irradiance (GTI), *𝐺𝑐*= *𝐼𝑐*+ *𝐷𝑐*+ *𝐷𝑔*[W/m2] *𝐺ℎ*Global horizontal irradiance (GHI), *𝐺ℎ*= *𝐷ℎ*+ *𝐼* cos*𝑍* [W/m2] 2 *𝐼* Direct normal irradiance (DNI) [W/m] 2 *𝐼* 0Extraterrestrial normal irradiance [W/m] *𝐼* *𝑐*In-plane direct irradiance [W/m 2] *𝑘* *𝑡*Clearness index [–] *𝑚* Relative airmass [–] *𝑁* Number of data points [–] *𝑅𝑑*Sky diffuse transposition factor [–] *𝑅𝑟*Ground reflection transposition factor [–] *𝑆* Slope of the tilted plane [◦] ◦ *𝑍* Solar zenith angle []

**Greek letters**

*𝛥* Sky brightness [–] *𝜖* Sky clearness (1986 & 1987) [–] *𝜖* 0Sky clearness, zenith independent (1988 &

1990) [–]
*𝜅* Sky clearness adjustment constant (1.041) [rad−3] *𝜌* Ground albedo [–] *𝜃* Incidence angle [◦]

**Subscripts**

*𝑐* in-plane of panel/collector *𝑑* sky-diffuse *ℎ* horizontal *𝑖𝑖*’th time step

*6RODU Energy 267 (2024) 112093*

However, the coefficients are discontinuous with respect to the sky clearness, stemming from the empirical coefficients being specified for discrete bins of the sky clearness. The discontinuous parameterization has the drawback that it results in step-like jumps in the predicted tilted irradiance when the sky conditions change *𝜖* bins. This is increasingly becoming an issue with the more frequent use of sub-hourly data and models. For example, this can pose an issue when employing tracker optimization algorithms and result in unfounded fluctuations in performance metrics. Continu- ous behavior of transposition models is also important for short-term forecast of power availability for curtailed PV plants, e.g., Gostein and Hobbs [9]. Additionally, the discrete nature of the Perez model intro- duces challenges when utilizing the model for reverse transposition,

i.e., deriving GHI from GTI. Faiman et al. [10] noted that using the Perez model for reverse transposition results in non-linear equations. More importantly, the authors pointed out that since the ‘‘sky clearness parameter is expressed in terms of discrete steps... the iterative... algorithm does not always converge’’. Similarly, Marion [11] noted that the Perez models are ‘‘not continuous functions, and this can be problematic for determining an iterative solution when using simple methods such as bisection algorithms and others that require a continuous function’’. For these reasons, several studies have avoided using the Perez model for reverse transposition and opted for simpler transposition models such as the Hay model, e.g., Tschopp et al. [12]. Reverse transposition is further discussed in Section2.6. By fixing the sky clearness bin calculated during the first iter- ation, Faiman et al. [10] partly overcame the challenges, although noting that ‘‘the construction of a continuous version of the Perez model appears attractive’’ for reverse transposition. To this end, Elsinga et al. [13] developed a continuous version of the Perez model by replacing the discrete coefficients with continuous spline functions, though regrettably and perhaps unknowingly using the outdated1987 version of the Perez model. Notably, during the original model devel- opment, Perez et al. [14] considered developing a fully analytical and continuous model using polynomials but rejected the idea at the time due to the increased computational requirement. However, due to the development in computational power during the past decades, this no longer poses an obstacle. In this paper, we present a continuous form of the Perez 1990 transposition model and demonstrate the associated benefits when used for reverse transposition. Specifically, the Perez model’s discontinuous parameterization of the sky clearness using discrete bins is replaced by continuous quadratic splines. The model is evaluated for forward transposition by comparison to the original model and experimental data to ensure that it can be used as a plug-in replacement for the original model. Additionally, the use of the continuous Perez model for enhanced reverse transposition is demonstrated, and the conditions for which reverse transposition is impossible are defined. The structure of this paper is as follows: A review of transposition models is presented in Section2followed by a description of the model development and formulation in Section3. The performance of the new continuous model is compared to measurement data and the original Perez model in Section4. The application of the continuous Perez model to reverse transposition is demonstrated and discussed in Section5. Finally, the conclusions of the study are presented in Section6.
**2. Background**
*2.1. Tilted irradiance* Global tilted irradiance, *𝐺𝑐*, is typically modeled as the sum of three separate components: in-plane direct irradiance, *𝐼𝑐*, sky diffuse irradiance, *𝐷𝑐*, and ground reflected irradiance, *𝐷𝑔*: *𝐺𝑐*= *𝐼𝑐*+ *𝐷𝑐*+ *𝐷𝑔*(1)
using measurement data from Geneva and Denver and also concluded that the Perez model gave the best results. For these reasons, the Perez 1990 model has become the industry standard, which has led most commercial PV modeling software to only offer the Perez1990 and the simpler Hay transposition models (e.g., PVsyst, SolarFarmer, PlantPredict, HelioScope). Additionally, Yang [6] noted that the Perez model was the most cited transposition model. The high accuracy of the Perez transposition model derives from its sophisticated parameterization of the sky conditions, which serves to capture the anisotropic effects. The sky conditions are parametrized using the solar zenith angle (*𝑍*), sky clearness (*𝜖*), and sky bright- ness (*𝛥*). The Perez model uses these parameters to determine the anisotropic contributions, i.e., irradiance contributions from circum- solar and horizon brightening/darkening. Specifically, the model cal- culates two anisotropic coefficients using empirically determined co- efficients stored in a look-up table. The anisotropic coefficients are continuous with respect to the zenith angle and the sky brightness.

The in-plane direct irradiance can be calculated as *𝐼𝑐*= *𝐼* cos*𝜃*, where *𝜃* is the incidence angle between the normal vector of the surface and the sun, and *𝐼* is the direct normal irradiance. The in-plane ground reflected irradiance can be formulated as a function of the global horizontal irradiance, *𝐺ℎ*:

*𝐷𝑔*= *𝜌𝐺ℎ𝑅𝑟*(2)

where *𝜌* is the ground albedo, and *𝑅𝑟*is the ground reflection trans- position factor. Under the common assumption of isotropic ground reflections, *𝑅𝑟*is equal to (1 − cos*𝑆*)∕2, where *𝑆* is the slope of the tilted plane. Similarly, the in-plane diffuse sky irradiance, *𝐷𝑐*, can be calculated as:

*𝐷𝑐*= *𝐷ℎ𝑅𝑑*(3)

where *𝐷ℎ*is the diffuse horizontal irradiance, and *𝑅𝑑*is the sky diffuse transposition factor. In the past decades, numerous different methods have been proposed for modeling the sky diffuse transposition factor, which are summarized in the following sections.

*2.2. Isotropic transposition models* The simplest approach to modeling the sky diffuse irradiance is to assume isotropic conditions, i.e., uniform distribution of the diffuse radiance from the sky hemisphere. An isotropic transposition model was first proposed by Moon and Spencer [15] and is provided in Eq.(4) (see [16] for a discussion of the isotropic model origin). Due to the assumption of uniform radiance, the isotropic sky diffuse transposition factor only depends on the slope of the tilted plane, *𝑆*. <u>1 + cos𝑆</u> *𝑅𝑑*= (4) 2 However, numerous comparison studies have shown that isotropic models are too inaccurate and that it is imperative to include the main anisotropic features in order to avoid significant short and long-term errors in the prediction of tilted irradiance [4].
*2.3. Anisotropic transposition models* The two main anisotropic effects are (1) enhanced irradiance from the sun region due to forward scattering (circumsolar) and (2) horizon- zenith gradients that include horizon brightening in clear conditions and zenith brightening in heavily overcast conditions [14]. The main attempts to develop models capable of capturing these anisotropic effects are discussed below. One of the earliest attempts to model the sky diffuse anisotropic effects was made by Bugler [17], who extended the isotropic model by adding a circumsolar brightening term corresponding to 5% of the DNI. In the same year, Temps and Coulson [18] developed a model that accounted for both horizon brightening and circumsolar effects, though only suitable for clear sky conditions. Later, Klucher [19] added a modulating term to the Temps and Coulson model to account for variations between clear and overcast sky conditions. Hay and Davies [20] developed what remains a very popular trans- position model, which varies the circumsolar contribution based on an anisotropic index. The anisotropic index describes the degree of anisotropy and is calculated based on the transmittance of direct ir- radiance through the atmosphere. Reindl et al. [21] extended the Hay model by adding a horizon brightening correction factor. It is worth noting that models utilizing a sky description based only on the amount of direct irradiance (e.g., Hay, Klucher, and Reindl) become isotropic in the absence of direct irradiance. Perez et al. [22] found that these types of models tend to miss certain anisotropic effects, particularly circumsolar enhancements for bright atmospheres with low or no direct irradiance.
*2.4. Perez transposition models* Consequently, Perez formulated a series of models that divide the sky hemisphere into three zones: a circumsolar region, a horizon region, and an isotropic background [22]. These models are based on novel pa- rameterization of the sky conditions, yet relying on commonly available data, i.e., solar zenith angle, DNI, DHI, and extraterrestrial irradiance. The anisotropic contributions were determined from three parameters and a table of empirical coefficients. The empirical coefficients were derived by fitting the models to experimental data and are suitable for all sky conditions. The variation of the specific anisotropic modeling and parameterization of the various Perez models are described below. The1986formulation of the Perez model treated the circumsolar irradiance as a uniform contribution from a circular region centered around the sun (15◦half-angle) and horizon brightening from a finite band at the horizon (angular thickness of 6.5◦) [22]. The sky conditions were discretized into 200 categories based on the zenith angle, diffuse horizontal irradiance (*𝐷*), and sky clearness (*𝜖*) defined in Eq.(5).
*ℎ* 0

*𝜖* 0= <u>𝐷ℎ+ 𝐼</u> (1986 *𝑎𝑛𝑑* 1987 *𝑚𝑜𝑑𝑒𝑙𝑠*) (5) *𝐷ℎ* The Perez1987model featured several improvements, including simplification of the governing equation and allowing negative horizon brightening coefficients (equivalent to brightening at the top of the sky dome) [14]. The new model formulation had the advantage of reducing the number of empirical coefficients from 480 to only 48. Additionally, the horizon brightening region was modified to be an infinitesimally thin region at 0-degree elevation, and the sky condition parameterization was adjusted by replacing *𝐷ℎ*with sky brightness (*𝛥*) as defined in Eq.(6).

*𝛥* = *𝐷ℎ*⋅ *𝑚*∕*𝐼𝑜*(6)

where *𝑚* is the relative airmass and *𝐼𝑜*is the extraterrestrial normal irradiance. Furthermore, the1988and1990versions featured several improve- ments and simplifications, including modeling circumsolar irradiance as a point source instead of an arbitrarily sized region around the sun disk [5,23]. This has the associated benefit that it is no longer necessary to solve non-linear equations when deriving coefficients for the new model formulation. The sky clearness was also modified to eliminate its dependence on the solar zenith angle. The zenith independent sky clearness (*𝜖*) is expressed as: <u>𝜖 + 𝜅 𝑍</u>3 *𝜖* = <u>0</u> 3 (*𝑧𝑒𝑛𝑖𝑡ℎ 𝑖𝑛𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑡,*1988 *𝑎𝑛𝑑* 1990 *𝑚𝑜𝑑𝑒𝑙𝑠*) (7) 1 + *𝜅 𝑍* where *𝜅* is a constant equal to 1.041 when the solar zenith angle *𝑍* is in radians. The Perez 1990 model remains the most widely used version of the Perez transposition models, and its mathematical formulation is introduced in detail in the following section. Note the Perez 1988 and 1990 model formulations are the same, only the coefficient sets differ.

*2.5. Perez 1990 model formulation* The mathematical formulation of the 1990 Perez et al. [5] sky diffuse transposition factor, *𝑅𝑑*, is provided in Eq.(8). *𝑅𝑑*= (1 − *𝐹*1) <u>1 + cos𝑆</u>
+ *𝐹*1 <u>𝑎</u> + *𝐹*2sin*𝑆* (8) 2 *𝑏* The terms *𝑎* and *𝑏* represent the cosine of circumsolar incidence angles on the considered tilted plane and the horizontal, respectively:

*𝑎* = max[0*,* cos*𝜃*] (9)

◦ *𝑏* = max[cos 85*,* cos*𝑍*] (10)

where *𝑍* is the solar zenith angle and *𝜃* is the incidence angle of the sun and the tilted surface.

**Table 1**

Perez model coefficients (all sites composite 1990) [5].

|𝜖 bin|𝐹₁₁|𝐹₁₂|𝐹₁₃|𝐹₂₁|𝐹₂₂|𝐹₂₃|
|---|---|---|---|---|---|---|
|[1.000–1.065)|−0.008|0.588|−0.062|−0.060|0.072|−0.022|
|[1.065–1.230)|0.130|0.683|−0.151|−0.019|0.066|−0.029|
|[1.230–1.500)|0.330|0.487|−0.221|0.055|−0.064|−0.026|
|[1.500–1.950)|0.568|0.187|−0.295|0.109|−0.152|−0.014|
|[1.950–2.800)|0.873|−0.392|−0.362|0.226|−0.462|0.001|
|[2.800–4.500)|1.132|−1.237|−0.412|0.288|−0.823|0.056|
|[4.500–6.200)|1.060|−1.600|−0.359|0.264|−1.127|0.131|
|[6.200–∞]|0.678|−0.327|−0.250|0.156|−1.377|0.251|

The anisotropic coefficients *𝐹*1and *𝐹*2are functions of the sky conditions and express the degree of circumsolar and horizon/zenith anisotropy, respectively.

*𝐹* 1= max[0*, 𝐹*11(*𝜖*) + *𝛥* ⋅ *𝐹*12(*𝜖*) + *𝑍* ⋅ *𝐹*13(*𝜖*)] (11)

*𝐹* 2= *𝐹*21(*𝜖*) + *𝛥* ⋅ *𝐹*22(*𝜖*) + *𝑍* ⋅ *𝐹*23(*𝜖*) (12) The most widely used set of anisotropic coefficients for Eqs.(11) and(12)is provided inTable1. This set of coefficients was derived based on measurement data from eight different locations with vastly different climatic conditions and will be used for the remainder of this paper. As can be seen from Eqs.(11)and(12), the anisotropic coefficients are continuous with respect to the solar zenith angle and the sky brightness. However, due to the binning of empirical coefficients (see Table1andFig.1), the model is not continuous with respect to the sky clearness (*𝜖*). As highlighted in the introduction, this discontinuity has several important implications.

*2.6. Reverse transposition* During the operation phase of a PV plant, it is customary to mea- sure the irradiance in the plane of the PV panels for performance monitoring. However, certain applications require GHI measurements,
e.g., irradiance remote sensing or operational tuning of forecasts and validations. Additionally, when using measured GTI for PV perfor- mance modeling, it is necessary to determine the split between direct and diffuse irradiance in order to model incidence angle losses and assess self-shading [12,24]. Therefore, methods for deriving GHI from GTI are of interest, which use transposition models in reverse [25]. When only GTI for a single orientation is available, it is necessary to also use a decomposition model to derive GHI. Whereas if GTI is measured for multiple ori- entations, GHI can be estimated without the use of a decomposition model. In addition to obtaining GHI, reverse transposition also allows for obtaining estimates of DNI and DHI. Steinmüller [26] developed a method for reverse transposition called the ‘‘two-solarimeter method’’, which derives DNI and DHI from measurements of GTI from two different orientations. Similarly, Faiman et al. [27] developed a multi-pyranometer instrument and demonstrated the derivation of GHI from multiple GTI measurements under the assumption of isotropic conditions. Yang et al. [28] presented a method for using the Perez transposition for reverse transposition. The method presented by Yang et al. requires knowledge of either horizontal diffuse irradiance or GTI from multiple different oriented sensors. Furthermore, Gostein et al. [29] measured GTI using five differently oriented reference cells and demonstrated deriving GHI, DNI, and DHI using the Perez 1990 model. Gostein demonstrated a higher prediction accuracy of GTI for alternative orientations compared to using high- quality measurements of DNI and DHI, although this was only done for one orientation. Lorenz et al. [30] deployed a network of stations with three differently oriented reference cells and one horizontal pyra- nometer. Lorenz used the DIRINT decomposition and the Perez 1990
transposition models to determine the azimuth of tilted reference cells for quality control purposes. However, GTI is commonly only measured for a single orientation, i.e., that of the PV panels. Hence methods requiring multiple measurements have limited usage in practice. To this end, Marion [11] developed the popular GTI-DIRINT method, which estimates DNI and DHI from a single GTI measurement. The GTI- DIRINT method estimates the irradiance components iteratively using the DIRINT decomposition model [31] and the Perez 1990 transposition model. Holmgren [32] noted that the performance of the GTI-DIRINT ◦ method is poor when the angle of incidence (AOI) is greater than 80. The aforementioned methods for reverse transposition are all nu- merical, i.e., they rely on some form of optimization, which has the drawback of longer computation times and potential conversion issues, which analytical solutions do not have. For these reasons, Halilovic et al. [33] developed an analytical method for reverse transposition. While the method seems promising, the main drawback is that it was developed and validated using data for a single region with a homogeneous climate. Thus, the model cannot be recommended for global usage before further validation is carried out. In contrast, the Perez transposition model was developed based on measurement data from eight different sites with vastly different climates and has been found to be practically universally applicable with good performance.

*2.7. Decomposition models* While transposition models require inputs of direct and diffuse irra- diance, these individual components are often not measured. Instead, it is customary to only measure GHI, primarily due to the high costs and requirement of a tracker for measuring DHI/DNI. Consequently, it is often necessary to employ methods for deriving DHI/DNI from GHI prior to the transposition step. Such models are known as decomposi- tion or separation models. Decomposition models range in complexity, with the simplest models consisting of piecewise equations relating the clearness index to the diffuse fraction, e.g., Erbs et al. [34]. A review of decomposition models is presented in [35]. As mentioned in the previous section, decomposition models are used for reverse transposition. Thus, similar to transposition models, it is also desirable for decomposition models to be continuous.
**3. Methods** This section first describes the main contribution, the transforma- tion of the forward transposition model. Next, reverse transposition is described in Section3.2, followed by a discussion on root-finding algorithms in Section3.3. Last, Section3.4describes a modification to the Erbs decomposition model in order for it to be continuous as needed for reverse transposition.
*3.1. Transposition* The Perez model uses lookup tables to map sky clearness values *𝜖* to a set of six empirical coefficients. Three of these factors are used to calculate the circumsolar brightening factor (F1) and the other three are used to calculate the horizon brightening factor (F2) (seeEqs.(11)and (12)). To eliminate discontinuities at the transitions between *𝜖*-bins, six continuous functions of *𝜖* are needed to calculate the six coefficients. The simplest type of continuous function would be a series of connected line segments, one for each of the eight bins. However, the continuous function must be also able to reproduce the original bin values; that is, the average value of the continuous function over the interval of each bin should equal the tabulated value for that bin. This goal cannot be achieved using connected straight-line segments. Connected curve segments can provide additional degrees of freedom, which leads us to a spline solution, and a spline that reproduces the bin values is known as a mean-preserving spline.

**Fig. 1.** Illustration of the F₁₁ coefficients (all sites composite 1990) and the quadratic

spline used to replace them in the continuous model.

In [13] we find an illustration of six (presumably cubic) splines passing through the midpoints of each *𝜖* bin. This type of fit provides continuity but fails to maintain the bin average values and, therefore, would lead to larger deviations from the original model. In fact, to meet the requirements, it is necessary to obtain only one additional degree of freedom per segment or bin, hence, a quadratic spline segmented at the bin boundaries is adequate. The quadratic variant also provides continuity in the first derivative, that is, it is *C1* continuous. A challenge with the *𝜖* parameter is that its domain is unbounded, ranging from 1 to ∞ (although in practice, most observations are below

20). The original empirical data points were unevenly distributed in this range, which led to very narrow bins at low *𝜖* values (e.g., 1.0 to 1.056) and much wider ones at high values (e.g., 5.98 to 10.08). For these reasons, Perez et al. [5] frequently uses a log scale in order to improve the clarity of graphics. In this work, we propose a simple transformation of *𝜖* that maps the original domain, 1 to ∞, to the bounded range, 0 to 1. The transformed clearness value is called zeta
(*𝜁*) and is defined as follows: *𝜁* = 1 − <u>1</u>
(13) *𝜖* The transformation to *𝜁* produces more uniform bin widths, which signals that the original data points are more evenly distributed on the

*𝜁* scale. Since the underlying distribution is continuous, the transfor- mation also improves the uniformity *within* each bin. This is important because the mean-preserving spline fit assumes uniform distributions within each bin. Another small problem is that the last bin would need to be limited to a finite *𝜖* value in order to calculate the average value of the spline over that *𝜖* interval (in the spline fitting process). The choice of cut-off strongly affects the spline that is produced, not only for the last bin but also for the adjacent ones, because of the continuity requirement. The new *𝜁*-space is bounded at 1.0 and eliminates the need for an arbitrary upper *𝜖* limit.Fig.1shows the bin values for F11on the *𝜁* scale along with the quadratic spline used to replace them. A recent paper by Ruiz-Arias [36] solves a system of linear equa- tions to calculate the three quadratic polynomial coefficients for each segment of a quadratic mean-preserving spline. For this work, we devel- oped the same method initially but subsequently adopted a numerical optimization that produces a set of overall spline coefficients rather than the individual polynomial coefficients per segment. This leads to a smaller total number of coefficients, maintains continuity even if coefficients are rounded off (e.g., for publication), and enables fast evaluation using efficient, established software routines in multiple programming languages, including Python, MATLAB, and Fortran. The first column inTable2lists the so-called knot values that delimit the quadratic spline segments. These are simply the *𝜁* bin boundaries with the first and last values repeated thrice. The coeffi- cients that we calculated for the six F functions are listed inTable2. A typical software function to evaluate a spline function requires the list of knots (*t*), one of the columns of coefficients (*c*), and the degree of the spline (*k*), which is 2. The circumsolar function *𝐹*1and horizon brightening function *𝐹*2 are each linear combinations of three spline functions; therefore, the first order derivative (C1 continuity) with respect to *𝜁* is maintained. Fig.2illustrates how the change from *𝜖* to *𝜁* affects the bin distribution,

i.e., the bin distribution (*𝜖*) in the left subplots varies greatly, whereas the bin distribution (*𝜁*) in the middle subplots are more uniform. While preparingFig.2we noticed that the value of *𝐹*1could exceed
◦

1.0 for zenith angles less than 30, which would be physically incoher- ent and produce a negative irradiance for the isotropic sky component. However, in our validation data sets, we observed only isolated cases with *𝐹*1over 0.7, and for one equatorial location (the BSRN station DWN) the natural limit was approximately 0.9. Consequently, there ap- pears to be a low likelihood of reaching 1.0. Nevertheless, to guarantee physically coherent transposition results, we recommend that a limit of
**Fig. 2.** Comparison of *𝐹₁* and *𝐹₂* anisotropic coefficients calculated using binned coefficients vs. splines. All plots are for a solar zenith angle of 45◦. (For interpretation of the

references to color in this figure legend, the reader is referred to the web version of this article.)

**Table 2**

<u>Quadratic spline knot and coefficient values (k=2) for the continuous Perez model.</u>

|t|𝑐₁₁|𝑐₁₂|𝑐₁₃|𝑐₂₁|𝑐₂₂|𝑐₂₃|
|---|---|---|---|---|---|---|
|0.000|−0.053|0.529|−0.028|−0.071|0.061|−0.019|
|0.000|−0.008|0.588|−0.062|−0.060|0.072|−0.022|
|0.000|0.131|0.770|−0.167|−0.026|0.106|−0.032|
|0.061|0.328|0.471|−0.216|0.069|−0.105|−0.028|
|0.187|0.557|0.241|−0.300|0.086|−0.085|−0.012|
|0.333|0.861|−0.323|−0.355|0.240|−0.467|−0.008|
|0.487|1.212|−1.239|−0.444|0.305|−0.797|0.047|
|0.643|1.099|−1.847|−0.365|0.275|−1.132|0.124|
|0.778|0.544|0.157|−0.213|0.118|−1.455|0.292|
|0.839|0.544|0.157|−0.213|0.118|−1.455|0.292|
|1.000|0.000|0.000|0.000|0.000|0.000|0.000|
|1.000|0.000|0.000|0.000|0.000|0.000|0.000|
|1.000|0.000|0.000|0.000|0.000|0.000|0.000|

**Fig. 3.** Example of the relationship between modeled GTI and GHI showing how the

Perez–Driesse model ensures there is a GHI value for every GTI value. The calculated GTI is based on *𝜌* = 0*.*25, *𝑆* = 40◦, surface azimuth=180◦, solar zenith = 75◦, and solar azimuth=82◦.

**Fig.**

**4.** Example of the relationship between modeled GTI and GHI at high angle of
incidence, where multiple GHI values can produce the same GTI value. The calculated GTI is based on *𝜌* = 0*.*25, *𝑆* = 40, surface azimuth = 180, solar zenith=75, and solar◦ ◦ ◦ ◦ azimuth = 76.

0.9 be imposed on *𝐹*1in implementations of both the original and the continuous models, as shown in Eq.(14). *𝐹* 1= min[0*.*9*,* max[0*, 𝐹*11(*𝜖*) + *𝛥* ⋅ *𝐹*12(*𝜖*) + *𝑍* ⋅ *𝐹*13(*𝜖*)]] (14) Note that the min and max operations technically introduce dis- continuities in the derivative of *𝐹*1, which may need to be taken into account in the root finding algorithm for reverse transposition (discussed below). In the remainder of this paper, we refer to the new continuous version of the Perez model as the Perez-Driesse model. Next, we explain how the Perez-Driesse model can be used for reverse transposition.
*3.2. Reverse transposition* In this section, we discuss the process of determining a value for GHI when given a value for GTI. Since it is not possible to invert the Perez model analytically, a numerical optimization method is needed to search for (and find) the value of GHI that, when transposed, produces the given target GTI value: *𝑓* *𝑡𝑟𝑎𝑛𝑠𝑝𝑜𝑠𝑒*(*𝐺𝐻𝐼*) → *𝐺𝑇𝐼𝑡𝑎𝑟𝑔𝑒𝑡*(15) Prior to transposition GHI must be split into beam (DNI) and diffuse (DHI) components using a decomposition function: *𝑓* *𝑑𝑒𝑐𝑜𝑚𝑝𝑜𝑠𝑒*(*𝐺𝐻𝐼*) → *𝐷𝑁𝐼,𝐷𝐻𝐼* (16) Therefore, the search needs both a decomposition and transposition step: *𝑓* *𝑡𝑟𝑎𝑛𝑠𝑝𝑜𝑠𝑒*(*𝑓𝑑𝑒𝑐𝑜𝑚𝑝𝑜𝑠𝑒*(*𝐺𝐻𝐼*)) → *𝐺𝑇𝐼𝑡𝑎𝑟𝑔𝑒𝑡*(17) Mathematically, reverse transposition is then accomplished by find- ing the root of the equation: *𝑓* *𝑡𝑟𝑎𝑛𝑠𝑝𝑜𝑠𝑒*(*𝑓𝑑𝑒𝑐𝑜𝑚𝑝𝑜𝑠𝑒*(*𝐺𝐻𝐼*)) − *𝐺𝑇𝐼𝑡𝑎𝑟𝑔𝑒𝑡*= 0 (18) The reverse transposition process can be visualized usingFig.3. Here we have taken a range of potential GHI values for a fictional moment in time and calculated the corresponding GTI values by de- composition and forward transposition (Eq.(17)). If, at this moment, we measure that *𝐺𝑇𝐼𝑡𝑎𝑟𝑔𝑒𝑡*= 200 W/m2, then it is easy to read from the graph that the corresponding value of GHI is approximately 370 W/m2. A numerical optimization algorithm using Eq.(18)would determine this value of GHI to the required level of precision. The magnified portion ofFig.3shows a part of the curve where the original Perez model produces discontinuities in the relationship between GTI and GHI, and as a result, there are some values of GTI, that simply do not have a corresponding GHI value. A numerical algorithm searching for such a GTI value would fail to find an exact solution because it does not exist and would at best provide the nearest solution. The Perez–Driesse model does not leave such gaps and hence has an exact solution for all values of GTI in this example, in other words,
the continuous transposition function for this case is a bijection, and therefore invertible. While not apparent here, some Perez model dis- continuities lead to downward jumps in the GTI vs. GHI graph, which means there could be two solutions rather than zero. The Perez–Driesse model eliminates this problem as well. However, even after all discontinuities are smoothed out, there are still situations where multiple solutions can occur, in other words, the transposition is a surjection. An example of this is shown inFig.4. As GHI increases the diffuse fraction (DF) decreases and where DF decreases fast enough, DHI actually decreases. When the tilted surface is oriented so that it receives little or no beam radiation GTI depends mostly on DHI, therefore, some increases in GHI lead to a decrease in GTI. As GHI increases further the diffuse fraction stabilizes and both DHI and GTI start to increase again. Elsinga et al. [13] also identified this problem, but assumed it could occur anytime. In fact, it only occurs when little or no beam radiation reaches the surface, which happens when the angle of incidence approaches 90◦or goes beyond.

*3.3. Root finding algorithms* Reverse transposition has now been formulated as finding the cor- rect root of a continuous function (Eq.(18)). Many root-finding al- gorithms exist and differentiate themselves most prominently by the number of iterations they need to find a root. For reverse transposition, however, speed is secondary to robustness. One feature that contributes to robustness is the ability to specify the upper and lower bounds for the solution. Since the solution is a

**Fig.**

**5.** Comparison of the
original the proposed C1 continuous Erbs–Driesse model. The Erbs insetsdecomposition show the twomodel small and discontinuities of the original Erbs model that can potentially disrupt numerical optimization algorithms.

GHI value it must be non-negative and its maximum can be estimated from clear-sky conditions plus some reasonable margin. The simplest bounded algorithm is bisection, and it is guaranteed to find a single root in a given interval—provided there is exactly one root. This last condition is the reason bisection cannot be used reliably together with the original Perez model. When multiple roots exist, the challenge is two-fold: finding the solutions, and selecting the most appropriate one, since in the real world, there is only one correct GHI value. This challenge invites the use of heuristics, which we will explore in future work. Similarly, if no numerical solution exists for the function, there is nevertheless a correct GHI value. This could occur when one of the models (decomposition or transposition) deviates too far from reality, but also when a GTI measurement is incorrect and does not represent reality. Thus, in addition to heuristics, a comprehensive reverse transposition process will require some level of validation of inputs and outputs. The GTI-DIRINT method should be mentioned in this context be- cause it contains a custom root-finding algorithm and integrates some heuristics, which include distinguishing between times when the sun is in front of (AOI *<* 90◦) vs. behind the plane (AOI *>* 90◦). The solution search is constrained to a range of plausible GHI values and does not fail expressly because of multiple possible solutions but might converge on any one or none of them. For times when the sun is behind the GTI plane, the GTI-DIRINT algorithm assumes that the clearness index is the same as for a preceding or subsequent period when the sun is in front of the GTI plane.

*3.4. Decomposition* As discussed in the background section, transposition algorithms require separate inputs of DNI and DHI. Thus, if only GHI is available, a decomposition model is needed to estimate the split between beam and diffuse irradiance. In algorithms for reverse transposition from GTI to GHI this decomposition step is also required, and the decomposition model should ideally also be a continuous function to ensure that the numerical methods employed can converge on a solution. A simple and well-known decomposition model is the Erbs model [34], which maps the clearness index (*𝑘𝑡*) to diffuse fraction (*𝐷𝐹*) using an empirical piece-wise polynomial function. Close inspection of this function at the two transition points reveals that it is not completely continuous.Fig.5shows the transitions at *𝑘𝑡*= 0*.*22 and *𝑘𝑡*= 0*.*80. Moving the transition points slightly and adjusting the polynomial coefficients allowed us to make the Erbs model C1 continuous while maintaining the prediction of *𝐷𝐹* within ±0*.*0005 of the original func- tion over the full range of *𝑘𝑡*. The level of continuity achieved in practice is limited by the precision of the calculations and hence, by the precision of the polynomial coefficients. We show all digits required for double-precision floating-point calculations here, not because they improve the model, but because they benefit numerical optimization algorithms. Incidentally, it is possible to express this same piece-wise polynomial as a degree 4 spline, however, that would require 16 coefficients. ⎧1 − 0*.*09 ⋅ *𝑘*
*𝑡*if *𝑘𝑡*≤ 0*.*216 ⎪ *𝐷𝐹* = ⎨0*.*165 if *𝑘𝑡>* 0*.*792 (19) ⎪ *𝑃* (*𝑘*) otherwise ⎩ *𝑡* 4 *𝑃* (*𝑘𝑡*) = 12*.*26911439571261000 ⋅ *𝑘𝑡* 3 − 16*.*47050842469730700 ⋅ *𝑘𝑡* + 4*.*24692671521831700 ⋅ *𝑘* 2 *𝑡*(20) −*.*11390583806313881 ⋅ *𝑘𝑡* +*.*94629663357100100 ⋅ *𝑘𝑡* Like the continuous version of the Perez transposition model, this is a drop-in replacement for the original Erbs model.

**4. Performance assessment of the Perez–Driesse model** The performance of the continuous Perez–Driesse model is inves- tigated in the following sections. First, the measurement data and metrics used for the validation are described in Section4.1. Second, equivalence between the original and the continuous Perez model for forward transposition is demonstrated in Section4.2. The main objective of this assessment is to demonstrate that the continuous model can be used as a plug-in replacement for the original model without negative consequences. Next, the elimination of discontinuities in predicted tilted irradiance is demonstrated in Section4.3. Last, the computational differences between the two models are quantified in Section4.4.
*4.1. Validation data* Two datasets of measured solar irradiance data were used to assess the performance of the Perez–Driesse model. The first dataset was obtained from NREL’s Solar Radiation Research Laboratory’s (SRRL) Baseline Measurement System (BMS) in Golden, Colorado
◦ [37]. The following three GTI configurations were used: (1) 40 tilt and south facing (2) one-axis tracking plane with a north–south tracking axis, and

(3) normal to the sun corresponding to two-axis tracking. The second dataset was obtained from the University of Oregon’s Solar Radiation Monitoring Laboratory (SRML)’s station in Eugene, Oregon. Data from the SRML can be accessed fromsolardata.uoregon. edu. Four different GTI measurements from Eugene were used, namely:
- ◦ ◦
(1) 30 tilt and south facing, (2) 90 tilt and south facing, (3) 90 tilt and north facing, and (4) normal to the sun corresponding to two-axis tracking. The pyranometers used for the three fixed tilt GTI configurations were shielded from the ground-reflected irradiance. Data was retrieved using the pvlib iotools [38]. Both datasets also included measurements of GHI, DNI, and DHI, as well as ancillary meteorological parameters with a frequency of 1-minute. All irradiance measurements were made using broadband thermopile radiometers which were regularly cleaned. Specifically, DNI was measured with Kipp & Zonen CHP1 pyrheliometers, and GHI was measured using Kipp & Zonen CMP22 pyranometers. At the Golden site, DHI and GTI were also measured using CMP22 pyranometers. At the Eugene site, DHI was measured using a Schenk Star pyranometer, and GTI was measured with Eppley PSP pyranometers. At the Golden site, the GHI used for the validation was calculated from DHI and DNI. Whereas due to the higher uncertainty of the Schenk Star pyranometer, DHI was calculated from GHI and DNI at the Eugene site. For both sites, data from 2022 was used.

*4.2. Equivalence of the Perez–Driesse and Perez models* As a first step, the predicted GTI from the Perez–Driesse and the Perez models are compared to the measured GTI and to each other. The comparison is presented inTable3in terms of MBD and RMSD. A positive MBD indicates that the Perez–Driesse model predicts higher irradiance values on average. As can be noted fromTable3, both models exhibit low MBD when compared to the validation measurements. Furthermore, the MBD and RMSDs of the model-to-model comparison are much lower than when compared to the measurements. This illustrates that while there are mi- nor differences between the models, these differences are significantly lower than the model accuracy; thus, the models can be considered equivalent.
**Fig. 6.** Example of global horizontal irradiance and predicted in-plane diffuse irradi-
 ance during a clear sky day. In the bottom subplot, the black line corresponds to the diffuse irradiance predicted using the original Perez 1990 model, and the green line corresponds to the predicted sky irradiance using the continuous Perez–Driesse model proposed in this study.
*4.3. Continuity demonstration* As noted, one of the shortcomings of the Perez model is the step changes in predicted sky irradiance occurring when the sky clearness change from one bin to another. The discontinuities in sky irradiance predicted by the Perez model are demonstrated inFig.6, which shows
Comparison of predicted GTI from the Perez and Perez–Driesse models against measurement data. A comparison of the Perez–Driesse against the Perez model is also shown. All

For the unshielded GTI pyranometers, it is necessary to account for ground-reflected irradiance. As shown in Eq.(2)this requires knowl- edge of the local albedo. For the Golden site, which features significant variation in albedo due to snow cover, measured albedo was used. However, the albedo was not measured at the Eugene site, and instead, a fixed value of 0.2 was used as in [39].

*4.1.1. Quality control* The measurement data from Golden was provided with quality control flags calculated by the SERI-QC software [40]. Only data points flagged 1, 2, or 3 were used, which corresponds to points for which no test failed. The data provider of the Eugene data used a different QC approach; for this dataset, only data flagged 11 or 12 were used. Additionally, for both datasets, the BSRN quality control tests were applied to the GHI, DHI, and DNI measurements; see [41] (extremely rare limits were used). For the GTI measurements, limit thresholds were imposed by comparison to GTI derived from a transposition model as proposed by Lorenz et al. [30]. Specifically, the threshold limit imposed was: |*𝛥𝐺𝑐,𝑖*| *<* 0*.*15 ⋅ *𝐺𝑐,𝑖*(*𝑃𝑒𝑟𝑒𝑧*) + 50 W∕m
2 (21) where *𝛥𝐺𝑐,𝑖*is the difference between the modeled (predicted) and measured (observed) GTI at the *𝑖*’th time step. The modeled GTI was calculated using the Perez 1990 model (no notable difference in metrics were found when using the Hay model). These limits have been defined sufficiently loose to only remove obvious erroneous data (e.g., snow- covered instruments). Thus, using the Perez model for quality control and later using the data for assessing the same model does not pose an issue. Finally, only data for which the solar elevation was greater than 10◦was used in order to eliminate measurement data with large uncertainties.

*4.1.2. Validation metrics* The model performances were evaluated using two metrics, namely the mean bias difference (MBD) and the root-mean-square deviation (RMSD) (see Gueymard [42] for an in-depth review of validation metrics). The mathematical expressions for the MBD and RMSD are provided in Eqs.(22)and(23). *𝑖* ∑ =*𝑁* <u>𝛥𝐺</u> *𝑀𝐵𝐷* =
<u>𝑐,𝑖</u> (22) *𝑖*=1 *𝑁* [ *𝑖*=*𝑁* 2]1∕2 ∑ <u>(𝛥𝐺𝑐,𝑖)</u> *𝑅𝑀𝑆𝐷* = (23) *𝑖*=1 *𝑁* where *𝑁* is the total number of data points. Both metrics have units of W/m2.

**Table 3**

metrics are expressed in W/m². Mean GTI is calculated from validation data. Location GTI Mean Resolution configuration GTI

Golden, CO 40◦, south 553 1-min 1-h Golden, CO One-axis tracking 630 1-min 1-h Golden, CO Two-axis tracking 735 1-min 1-h

Eugene, OR 30◦, south 433 1-min 1-h Eugene, OR 90◦, south 237 1-min 1-h Eugene, OR◦, north 1-min 1-h Eugene, OR Two-axis tracking 1-min 1-h

Mean of all configurations 1-min 1-h

Perez Perez–Driesse Perez–Driesse vs. Perez *MBD RMSD MBD RMSD MBD RMSD* −1.0 0.2

13.9
15.5 −1.1 0.3
14.0
15.4 −0.1 0.1
2.7
2.6
− −1.3 0.7

17.4
15.6 − −1.3 0.4
17.5
15.7
0.0
0.3
3.4
3.6
−1.4 0.3

19.2
21.9 −1.8 0.3
19.3
22.0 −0.4 0.1
4.7
4.6
3.2
3.6
19.0
16.6
2.6
3.2
19.0
16.5 − −0.5 0.4
2.5
2.4
18.4
19.8
30.5
31.0
17.7
19.3
30.7
31.3 − −0.7 0.5
3.4
3.4
− −0.9 0.6

14.4
13.6 − −0.9 0.6
14.5
13.5
0.0
0.1
1.3
1.2
18.9
20.3
33.0
26.3
17.9
19.6
33.1
26.5 − −1.1 0.7
5.0
4.9
5.4
6.4
21.7
19.5
5.1
6.3
21.7
19.5 − −0.1 0.1
3.3
3.3

**Fig. 7.** Frequency histogram of the change in sky diffuse irradiance between time steps.

the GHI and predicted in-plane sky diffuse irradiance for a fictional clear sky day. For comparison, the in-plane sky diffuse irradiance from the continuous Perez–Driesse model is also shown in the figure. Noticeably, the model predictions are generally in close agreement. On closer inspection, it can be seen that the Perez–Driesse model remains continuous and takes on an intermediary value at the switch between sky clearness bins. To investigate the magnitude of the step changes caused by the sky clearness binning, a frequency histogram of the absolute change in irradiance from one time step to the next of the sky diffuse irradiance is plotted inFig.7. The sky diffuse irradiance time series was calculated based on the 40◦south-facing sensor at Golden (see Section4.1). A noticeable difference in the frequency distribution can be seen inFig.7, demonstrating that the predicted sky diffuse irradiance from the Perez model exhibits significantly larger changes in irradiance from one time step to the next. In particular, the new continuous model only exhibits step changes up to about 25 W/m2, whereas the original Perez model featured larger step changes and more frequently so. The investigation was based on 1-min data, whereas the difference in the frequency histogram is expected to be less for lower-frequency data.

*4.4. Computational differences* The computational time of the pvlib python v0.9.5 [43,44] imple- mentation of the Perez model has been compared to the Perez–Driesse model. Both models were implemented in the Python programming language and showed no statistical difference in computation time. The computation time was calculated for a one-year simulation at a 1- minute resolution. For both models, the computation time was 0.18 s on an HP Pavillion laptop with 16 GB ram and an 11th Gen Intel i5 processor. The computation time was calculated as the average time based on 10 runs with 50 loops each.
**5. Application to reverse transposition** In this section, we demonstrate the operation of reverse transposi- tion using the new continuous versions of the Perez and Erbs models together with the simple bisection search, and we compare this to the GTI-DIRINT implementation in pvlib python. The algorithms have three possible outcomes: no solution is found, an incorrect solution is found, or the correct solution is found. Using measured GHI and measured GTI it is often difficult to distinguish between these three outcomes because, in the real world, the relationship between these two measurements may not fit any models. As a result, a successful reverse transposition search could produce a value of GHI that does not match the measured GHI, which in turn would give the erroneous impression that the search was not successful. To avoid this problem, we do not test the algorithms with measured GTI but rather with modeled GTI. For the reverse transposition using
Perez–Driesse, we calculate GTI from GHI using Erbs–Driesse decom- position and Perez–Driesse transposition, whereas for GTI-DIRINT we calculate GTI using DIRINT decomposition and the traditional Perez transposition. In this manner, each algorithm is tested with target values that it *should* be able to reach exactly—in other words, easy targets. The example we use is based on the 40◦tilt south-facing mea- surement at Golden described in Section4.1. For each of the two algorithms, we calculate the easy target GTI values, then run the algorithm to estimate the GHI, and finally re-transpose this GHI to check whether the target GTI was indeed attained. If the re-transposed GTI value is close to the target (±1 W/m2), then we consider that the algorithm succeeded in finding a solution. If the GHI that was found is also close to the value we started with (±1 W/m2), then we consider that the *correct* solution was found; otherwise, an *incorrect* solution was found. These thresholds are somewhat arbitrary, but in cases where the algorithms are converging successfully on the correct solution, both errors are usually at least an order of magnitude smaller. GTI-DIRINT uses a 1 W/m2threshold internally to decide on convergence; therefore, we applied the same threshold externally for consistency. InFig.8we visualize the performance of the two algorithms by plotting the errors in GTI and GHI as a function of sun position (azimuth and elevation). The color of each patch indicates the mean bias deviation (MBD) for all the data points where the sun is in that position (±1◦azimuth, ±0.5◦elevation) and the diagonal lines identify sun positions where AOI=90◦and AOI=80◦. While these graphs do not register every single error, they very clearly identify where the majority of errors occur. The top two frames depict the MBD of GTI, therefore, the non-green areas show where the algorithms failed to find solutions. While the Perez–Driesse-based method appears to always finds a solution, this is somewhat misleading because the failure to find a solution results in a not-a-number (NaN) value, which cannot be included in the MBD. GTI-DIRINT ◦ fails frequently at lower sun elevations and when AOI *>* 90. The bottom two frames depict the MBD of GHI, therefore, the green areas represent correct solutions, whereas the blue and red areas identify under- and over-estimations respectively. In the Perez–Driesse-based method there is a small but distinct region around the AOI=90 line where the incorrect solution is frequently identified. These occurrences fall in the region where multiple solutions can exist. GTI-DIRINT reports the incorrect solution for a much wider range of sun positions, which may be due in part to the nature of its search algorithm, and in part to the discontinuities of both the Perez and DIRINT models that lead to multiple solutions at other sun positions. Table4quantifies these observations by reporting the proportion of data points for which a solution was either not found, incorrect or correct. The Perez–Driesse-based method is able to find the correct solution for a substantially higher fraction of data points in all three AOI angle ranges, with a remarkable success rate of 100% for the range AOI*<* 80 which represents 85% of the data points and 97% of the solar energy (GHI) in this example. Table5provides several error metrics for the GHI reported by the two methods. Data points where one of the methods produced a NaN value (3%) were excluded from these calculations. What these numbers tell us about our two methods is less important than what they tell us about reverse transposition in general, and therefore also when using measured GTI. In the best case, a well-performing search method should not contribute at all to the GHI error, which should ideally be the same as the forward transposition error. However, if the search method is not successful, GHI errors may become very large. Thus, an important output of any reverse transposition algorithm is the ability to detect and report or suppress any output values that are suspect. Similarly, evaluation and comparison studies of different reverse transposition methods should go beyond overall aggregate error metrics and investigate when and why the errors arise.

*A. Driesse et al. 6RODU Energy 267 (2024) 112093*
**Fig. 8.** Mean bias deviation of GTI (upper diagrams) and GHI (lower diagrams) derived from reverse transposition using the 40◦south-facing orientation at Golden. The GTI
 targets values for reverse transposition were calculated from measured GHI using the same models as in the subsequent reverse transposition: Erbs–Driesse/Perez–Driesse on the left; DIRINT/Perez on the right. The MBD is coded by color and plotted as a function of solar position. The dashed and solid black lines denote an incidence angle of 80◦and 90◦, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
**Table 46. Conclusions**
 Convergence metrics for the example case of reverse transposition. AOI Description Perez–Driesse GTI-DIRINTIn this paper, we have shown how discontinuities in predicted irra-

|AOI|Description|Perez–Driesse|GTI-DIRINT|
|---|---|---|---|
||No solution|0%|3.6%|
|0–80|Incorrect solution Correct solution No solution|0% 100% 1.3%|2.4% 94.0% 33.8%|
|80–90|Incorrect solution Correct solution No solution|17.1% 81.6% 40.1%|8.3% 57.9% 67.0%|
|90–110|Incorrect solution Correct solution|7.2% 52.8%|14.9% 18.1%|

diance of the widely used Perez transposition model can be smoothed ◦ effectively by replacing the empirical look-up table with six quadratic splines. As part of this work, we have transformed the sky clearness ◦parameter *𝜖*, which varies from 1 to ∞, into an equivalent parameter *𝜁* that varies from 0 to 1. Empirical observations are more uniformly distributed on the new *𝜁* sky clearness scale, therefore, the transformed

- lookup table bin boundaries are more uniformly spaced as well. This,
in turn, benefits the spline fitting process. The original Perez and the new *C1* continuous Perez–Driesse trans- position models were compared against measurements for multiple orientations at two locations. The comparison showed very similar deviation statistics (MBD and RMSD) in all cases, and the annual MBD between the two models was found to be 1.1 W/m2or less—usually

**Table 5**

Error metrics for GHI values produced by the reverse transpositionmuch less. Thus, the continuous transposition model can be considered

|Error metrics|for GHI values|by the reverse|transposition|
|---|---|---|---|
|example. All values are in W/m².||||
|AOI|Description|Perez–Driesse|GTI-DIRINT|
||MBD|0.0|0.0|
|0–80|RMSD|0.0|6.4|
||MAD|0.0|0.9|
||MBD|0.6|34.8|
|80–90|RMSD|52.7|77.3|
||MAD MBD|19.9 −6.9|40.7 10.8|
|90–110|RMSD|48.4|49.0|
||MAD|15.9|20.2|

a drop-in replacement for the original. The application where functional continuity is most called for is reverse transposition (GTI→GHI), which employs a numerical optimiza- ◦tion or search algorithm. This process uses a decomposition model, which should also be a continuous function. To demonstrate reverse transposition, therefore, we adjusted the well-known Erbs decomposi- ◦ tion model to provide *C1* continuity. Like the Perez–Driesse transpo- sition model, the resulting Erbs–Driesse decomposition model can be considered a drop-in replacement for the original. ◦ Using the two new continuous models, we then demonstrated that reverse transposition can be done more reliably using the simple and robust bisection algorithm than the custom GTI-DIRINT algorithm. The latter failed to find a solution or reported the incorrect solution more

often, resulting in substantially higher errors for the reported GHI. Both algorithms had greater difficulty at angles of incidence approaching 90◦and also just beyond 90◦due to the demonstrated existence of multiple mathematical solutions. However, GTI-DIRINT appeared to fail frequently under other conditions as well. In future work on re- verse transposition, we aim to develop suitable heuristics to choose the best among multiple potential solutions, thereby making reverse transposition as reliable and easy-to-use as forward transposition.

**Software availability**

Implementations of the Perez–Driesse and Erbs–Driesse models are available as open-source software in pvlib python on GitHub.

**CRediT authorship contribution statement**

**Anton Driesse:** Conceptualization, Methodology, Software, Visual- ization, Writing – original draft. **Adam R. Jensen:** Validation, Data cu- ration, Visualization, Writing – original draft. **Richard Perez:** Writing – review & editing.

**Declaration of competing interest**

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Acknowledgments**

The authors would like to acknowledge Afshin Andreas (NREL) and Josh Peterson (University of Oregon), who provided guidance on the irradiance data used for the validation in this study. Adam R. Jensen was funded by the Danish Energy Agency under grant no.: 64020- 1082 and 134232-510237, and a NumFOCUS Small Development Grant supported the open-source implementation in pvlib python.

**References**

[1]C.A. Gueymard, D.R. Myers, Validation and ranking methodologies for solar radiation models, in: V. Badescu (Ed.), Modeling Solar Radiation at the Earth’s Surface: Recent Advances, Springer, Berlin, Heidelberg, 2008, pp. 479–510, http://dx.doi.org/10.1007/978-3-540-77455-6_20. [2]J. Appelbaum, J. Bany, Shadow effect of adjacent solar collectors in large scale systems, Sol. Energy 23 (6) (1979) 497–507,http://dx.doi.org/10.1016/0038- 092X(79)90073-2. [3]C.A. Gueymard, Direct and indirect uncertainties in the prediction of tilted irradiance for solar engineering applications, Sol. Energy 83 (3) (2009) 432–444, http://dx.doi.org/10.1016/j.solener.2008.11.004. [4]J.E. Hay, D.C. McKay, Estimating solar irradiance on inclined surfaces: A review and assessment of methodologies, Int. J. Sol. Energy 3 (4–5) (1985) 203–240, http://dx.doi.org/10.1080/01425918508914395. [5]R. Perez, P. Ineichen, R. Seals, J. Michalsky, R. Stewart, Modeling daylight avail- ability and irradiance components from direct and global irradiance, Sol. Energy 44 (5) (1990) 271–289,http://dx.doi.org/10.1016/0038-092X(90)90055-H. [6]D. Yang, Solar radiation on inclined surfaces: Corrections and benchmarks, Sol. Energy 136 (2016) 288–302,http://dx.doi.org/10.1016/j.solener.2016.06.062. [7]M. David, P. Lauret, J. Boland, Evaluating tilted plane models for solar radiation using comprehensive testing procedures, at a southern hemisphere location, Renew. Energy 51 (2013) 124–131,http://dx.doi.org/10.1016/j.renene.2012.08.

074.
[8]P. Ineichen, Global Irradiance on Tilted and Oriented Planes: Model Validations, Technical Report, University of Geneva, 2011, URL:https://archive-ouverte. unige.ch//unige:23519. [9]M. Gostein, W. Hobbs, Exploring distributed PV power measurements for real- time potential power estimation in utility-scale PV plants, in: 2023 IEEE Photovoltaic Specialist Conference, PVSC, 2023,http://dx.doi.org/10.36227/ techrxiv.23262056.v1. [10]D. Faiman, D. Feuermann, A. Zemel, Site-independent algorithm for obtaining the direct beam insolation from a multipyranometer instrument, Sol. Energy 50

(1) (1993) 53–57,http://dx.doi.org/10.1016/0038-092X(93)90007-B.
[11]B. Marion, A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance, Sol. Energy 122 (2015) 1037–1046, http://dx.doi.org/10.1016/j.solener.2015.10.024.

[12]D. Tschopp, A.R. Jensen, J. Dragsted, P. Ohnewein, S. Furbo, Measurement and modeling of diffuse irradiance masking on tilted planes for solar engineering applications, solener.2021.10.083 Sol. Energy. 231 (2022) 365–378,http://dx.doi.org/10.1016/j.

[13]B. Elsinga, W. van Sark, L. Ramaekers, Inverse photovoltaic yield model for global horizontal irradiance reconstruction, Energy Sci. Eng. 5 (4) (2017) 226–239,http://dx.doi.org/10.1002/ese3.162. [14]R. Perez, R. Seals, P. Ineichen, R. Stewart, D. Menicucci, A new simplified version of the perez diffuse irradiance model for tilted surfaces, Sol. Energy 39 (3) (1987) 221–231,http://dx.doi.org/10.1016/S0038-092X(87)80031-2. [15]P. Moon, D.E. Spencer, Illumination from a non-uniform sky, Illum. Eng. 37 (1942) 707–722. [16]N. Kamphuis, C. Gueymard, M. Holtzapple, A. Duggleby, K. Annamalai, Perspec- tives on the origin, derivation, meaning, and significance of the isotropic sky model, Sol. Energy 201 (2020) 8–12,http://dx.doi.org/10.1016/j.solener.2020.

02.067.
[17]J. Bugler, The determination of hourly insolation on an inclined plane using a diffuse irradiance model based on hourly measured global horizontal insolation, Sol. Energy 19 (5) (1977) 477–491,http://dx.doi.org/10.1016/0038-092X(77) 90103-7. [18]R.C. Temps, K. Coulson, Solar radiation incident upon slopes of different orientations, Sol. Energy 19 (2) (1977) 179–184,http://dx.doi.org/10.1016/

[19]T. Klucher, Evaluation of models to predict insolation on tilted surfaces, Sol. En- 0038-092X(77)90056-1.

ergy 23 (2) (1979) 111–114,http://dx.doi.org/10.1016/0038-092X(79)90110-

5.
[20]J.E. Hay, J. Davies, Calculation of the solar irradiance incident on an inclined surface, in: J. Hay, T. Won (Eds.), Proceedings: First Canadian Solar Radiation Data Workshop, April 17-19, 1978, Toronto, Ontario, Canada, 1980, pp. 59–72. [21]D. tion models, Sol. Energy 45 (1) (1990) 9–17, Reindl, W. Beckman, J. Duffie, Evaluation http://dx.doi.org/10.1016/0038- of hourly tilted surface radia-

092X(90)90061-G. [22]R. Perez, R. Stewart, C. Arbogast, R. Seals, J. Scott, An anisotropic hourly diffuse radiation model for sloping surfaces: Description, performance validation, site dependency evaluation, Sol. Energy 36 (6) (1986) 481–497,http://dx.doi.org/

[23]R.

10.1016/0038-092X(86)90013-7 Perez, R. Steward, R. Seals, .T. Guertin, The Development and Verification of the Perez Diffuse Radiation Model, Technical Report SAND88-7030, Sandia National Lab and State Univ. of New York, Albany, 1988,http://dx.doi.org/10. 2172/7024029.
[24]A.R. Jensen, I. Sifnaios, S. Furbo, J. Dragsted, Self-shading of two-axis tracking solar collectors: Impact of field layout, latitude, and aperture shape, Sol. Energy 236 (2022) 215–224,http://dx.doi.org/10.1016/j.solener.2022.02.023. [25]D. Yang, Z. Dong, A. Nobre, Y.S. Khoo, P. Jirutitijaroen, W.M. Walsh, Evaluation of transposition and decomposition models for converting global solar irradiance from tilted surface to horizontal in tropical regions, Sol. Energy 97 (2013) 369–387,http://dx.doi.org/10.1016/j.solener.2013.08.033. [26]B. Steinmüller, The two-solarimeter method for insolation on inclined surfaces, Sol. Energy 25 (5) (1980) 449–460,http://dx.doi.org/10.1016/0038-092X(80) 90453-3. [27]D. Faiman, D. Feuermann, P. Ibbetson, A. Zemel, A multipyranometer instrument for obtaining the solar beam and diffuse components, and the irradiance on inclined planes, Sol. Energy 48 (4) (1992) 253–259,http://dx.doi.org/10.1016/ 0038-092X(92)90099-V. [28]D. Yang, Z. Ye, A.M. Nobre, H. Du, W.M. Walsh, L.I. Lim, T. Reindl, Bidirectional irradiance transposition based on the Perez model, Sol. Energy 110 (2014) 768–780,http://dx.doi.org/10.1016/j.solener.2014.10.006. [29]M. Gostein, A. Hoffman, B.H. King, A. Marquis, Measuring global, direct, diffuse, and ground-reflected irradiance using a reference cell array, in: 2022 IEEE 49th Photovoltaics Specialists Conference, PVSC, 2022, pp. 0285–0290,http: //dx.doi.org/10.1109/PVSC48317.2022.9938489. [30]E. Lorenz, P. Guthke, A. Dittmann, N. Holland, W. Herzberg, S. Karalus, B. Müller, C. Braun, W. Heydenreich, Y.M. Saint-Drenan, High resolution mea- surement network of global horizontal and tilted solar irradiance in southern Germany with a new quality control scheme, Sol. Energy 231 (2022) 593–606, http://dx.doi.org/10.1016/j.solener.2021.11.023. [31]R. Perez, P. Ineichen, E. Maxwell, R. Seals, A. Zelenka, Dynamic global-to-direct irradiance conversion models, ASHRAE Trans.-Res. Ser. (1992) 354–369. [32]W.F. Holmgren, GTI DIRINT Examples, Zenodo, 2018,http://dx.doi.org/10. 5281/zenodo.7869556. [33]S. Halilovic, J.M. Bright, W. Herzberg, S. Killinger, An analytical approach for estimating the global horizontal from the global tilted irradiance, Sol. Energy 188 (2019) 1042–1053,http://dx.doi.org/10.1016/j.solener.2019.06.027. [34]D. Erbs, S. Klein, J. Duffie, Estimation of the diffuse radiation fraction for hourly, daily and monthly-average global radiation, Sol. Energy 28 (4) (1982) 293–302, http://dx.doi.org/10.1016/0038-092X(82)90302-4. [35]N. Engerer, Minute resolution estimates of the diffuse fraction of global ir- radiance for southeastern Australia, Sol. Energy (2015) 215–237,http: //dx.doi.org/10.1016/j.solener.2015.04.012.

[36]J.A. Ruiz-Arias, Mean-preserving interpolation with splines for solar radiation modeling, Sol. Energy 248 (2022) 121–127,http://dx.doi.org/10.1016/j.solener.

2022.10.038.
[37]A. Andreas, T. Stoffel, NREL Solar Radiation Research Laboratory (SRRL) Baseline Measurement System (BMS), Technical Report NREL Report No. DA-5500- 56488, National Renewable Energy Laboratory (NREL), 1981,http://dx.doi.org/

10.5439/1052221.
[38]A.R. Jensen, K.S. Anderson, W.F. Holmgren, M.A. Mikofski, C.W. Hansen, L.J. Boeman, R. Loonen, Pvlib iotools—open-source python functions for seamless access to solar irradiance data, Sol. Energy 266 (2023) 112092,http://dx.doi. org/10.1016/j.solener.2023.112092. [39]B. Marion, A. Anderberg, C. Deline, J. del Cueto, M. Muller, G. Perrin, J. Rodriguez, S. Rummel, T.J. Silverman, F. Vignola, R. Kessler, J. Peterson, S. Barkaszi, M. Jacobs, N. Riedel, L. Pratt, B. King, New data set for validating PV module performance models, in: 2014 IEEE 40th Photovoltaic Specialist Conference, PVSC, 2014, pp. 1362–1366,http://dx.doi.org/10.1109/PVSC.2014. 6925171.

[40]E. Maxwell, Users Manual for SERI QC Software Assessing the Quality of Solar Radiation Data, Technical Report NREL/TP-463-5608, NREL, 1993,http://dx. doi.org/10.2172/10125711. [41]C.N. Long, E.G. Dutton, BSRN Global Network recommended QC Tests, V2.0, Technical Report, 2002, URL:https://bsrn.awi.de/fileadmin/user_upload/bsrn. awi.de/Publications/BSRN_recommended_QC_tests_V2.pdf. [42]C.A. Gueymard, A review of validation methodologies and statistical performance indicators for modeled solar radiation data: Towards a better bankability of solar projects, Renew. Sustain. Energy Rev. 39 (2014) 1024–1034,http://dx.doi.org/

10.1016/j.rser.2014.07.117.
[43]W.F. Holmgren, C.W. Hansen, M.A. Mikofski, pvlib python: a python package for modeling solar energy systems, J. Open Source Softw. 3 (29) (2018) 884, http://dx.doi.org/10.21105/joss.00884. [44]W. Holmgren, K. Anderson, C. Hansen, Calama-Consulting, M. Mikofski, A. Lorenzo, U. Krien, bmu, A.R. Jensen, C. Stark, A. Driesse, DaCoEx, M.S. de León Peque, kt, N. Priyadarshi, mayudong, Heliolytics, E. Miller, M.A. Anoma,

V. Guo, L. Boeman, J. Stein, W. Vining, jforbess, T. Lunel, A. Morgan, J. Ranalli, S. Aneja, Carlosbogo, C. Leroy, pvlib/pvlib-python: v0.9.5, Zenodo, 2023, http://dx.doi.org/10.5281/zenodo.7748922.
