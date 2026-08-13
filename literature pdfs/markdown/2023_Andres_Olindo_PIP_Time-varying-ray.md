Received: 2 December 2021 Revised: 18 June 2022 Accepted: 20 July 2022 DOI: 10.1002/pip.3614

### <u>RESEARCH ARTICLE</u>

# Time-varying, ray tracing irradiance simulation approach for photovoltaic systems in complex scenarios with decoupled

# geometry, optical properties and illumination conditions

|1|1|1|
|---|---|---|
|1|1|1|

Calcabrini Andres | Cardose Ruben | Gribnau David | Babal Pavel | Manganiello Patrizio | Zeman Miro | Isabella Olindo

1 Department of Electrical Sustainable Energy, Delft University of Technology, Delft, The Abstract Netherlands The accurate computation of the irradiance incident on the surface of photovoltaic 2 Kipp & Zonen BV, Delft, The Netherlands modules is crucial for the simulation of the energy yield of a photovoltaic system. CorrespondenceDepending on the geometrical complexity of the surroundings, different approaches Manganiello, Patrizio, Department of Electrical Sustainable Energy, Delft University of are commonly employed to calculate the irradiance on the photovoltaic system. In Technology, Delft, The Netherlands. this article, we introduce a backward ray tracing simulation approach to calculate the Email: p.manganiello@tudelft.nl irradiance on photovoltaic systems in geometrically complex scenarios. We explain how the repetition of time-consuming simulation steps can be avoided with the pro- posed approach by storing a selection of the results from the most computationally expensive parts of the problem, and we show that the irradiance calculated with the proposed approach is in good agreement with the results of Radiance, a well- established irradiance simulation tool. Furthermore, we present an experimental vali- dation carried out using a pyranometer and a reference cell over a period of 6 months in a complex scenario, which shows errors lower than 5% in the calculation of the daily irradiation. Finally, we compare high-resolution spectral simulations with mea- surements taken with a spectroradiometer under different sky conditions. The pro- posed approach is particularly well-suited for the simulation of bifacial and tandem photovoltaic modules in complex urban environments, for it enables the efficient sim- ulation of high-resolution spectral irradiance in scenarios with time-varying reflec- tance properties.

KEYWORDS bifacial PV, irradiance modelling, ray tracing, spectral irradiance, tandem PV, urban PV

1 | INTRODUCTION where PV modules are often subject to partial shading. Moreover, partially shaded PV systems will become increasingly common since The developments in the photovoltaic (PV) field over the last the integration of PV in the urban environment will be of utmost decades have fostered the deployment of PV modules from utility-importance for the development of net-zero-energy districts and the scale power plants to buildings 1,2 to vehicles. 3,4 As a result, many achievement of the UN Sustainable Development Goals. 5 In these PV systems are installed in landscapes with complex geometries scenarios, sophisticated simulation models are required to calculate

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes. © 2022 The Authors. Progress in Photovoltaics: Research and Applications published by John Wiley & Sons Ltd.

wileyonlinelibrary.com/journal/pip Prog Photovolt Res Appl. 2023;31:134–148.

1099159x, 2023, 2, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/pip.3614](https://onlinelibrary.wiley.com/doi/10.1002/pip.3614) by Oxford University, Wiley Online Library on [18/02/2026]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License ANDRES ET AL.

the irradiance incident on the solar cells and, subsequently, the elec- trical yield of a PV system. The selection of an adequate irradiance simulation model for a specific application depends mainly on the size of the PV system and the complexity of the landscape surrounding the installation. Since the accuracy of the models increases proportionally to the required computing power and computation time, there is not a single model that is adequate for every application. The most common irradiance simulation models for PV applications can be classified in three main groups: transposition models, view factor models and ray tracing models. Transposition models determine the irradiance incident on a PV module by adding the contributions of the beam, diffuse and ground reflected sunlight components on the plane of array (PoA). The diffuse component can be determined using one of several sky diffuse models that make different levels of approximations to describe the radiance distribution over the sky dome. 6–8 Transpositions models are the sim- plest and fastest approach to calculate the PoA irradiance. For exam- ple, the irradiance impinging on each cell of a 72-cell PV module can be simulated with 1-min resolution for an entire year using the simpli- fied Perez diffuse sky model⁷ in a few seconds with a modern per- sonal computer. The main limitation of transposition models is the low accuracy in the calculation of the diffuse and reflected irradiance com- ponents. In a simple landscape, the expected simulation error is typi- cally below 10%. 9 However, errors can increase to about 15% when the PV module is not optimally oriented. 10,11 Further limitations of these models are the underlying assumptions that the ground is uni- formly illuminated and its reflectivity is constant. 12 As a result, trans- position models are mostly used to simulate the irradiance on monofacial PV modules in relatively open landscapes such as large PV power plants or on rooftop PV systems in areas with low building density. View factor models calculate the ground reflected irradiance com- ponent by computing the view factors from the PV module to the shaded and unshaded areas on the ground. This refinement makes view factor models suitable for simulating the irradiance on the rear side of modules in bifacial PV power plants. In addition, view factor models can be classified in two main types. The first type, usually referred to as 2D view factor models, assumes that rows of modules are infinitely long to simplify the calculation of view factors. 13 Two- dimensional view factor models have been implemented in commer- cial software packages¹⁴ and errors lower than 16% have been reported in the calculation of the rear side irradiance. 15 The second type of view factor models, usually referred to as 3D view factor models, 16–19 considers that rows of PV modules are finite in length, which allows to include edge effects in the simulations. Experimental studies have reported errors that range from 5% to 15% in the rear side irradiance calculation. 20,21 Three-dimensional view factor models are also quite fast because the view factors are computed with closed-form formulas. However, these formulas are not directly applicable in geometrically complex scenarios with non-horizontal sur- faces, such as urban environments. In these cases, the estimation of view factors can be achieved by means of ray casting methods.

Ray tracing (RT) models are the most general irradiance simulation approach and enable the simulation of surfaces with arbitrary orienta- tions and bidirectional scattering distribution functions (BSDF). 24 RT algorithms are classified in two main types, forward and backward RT. Forward RT (FRT) algorithms calculate the irradiance on the PV module by tracing rays from the light sources (i.e., the sun and the sky dome) to the PV module and its surroundings. 25 FRT is often ineffec- tive because most of the traced rays do not contribute to the compu- tation of the irradiance on the PV module. In comparison, backward RT (BRT) algorithms calculate the irradiance on the PV module by fol- lowing the path of rays from the PV module to the light sources, which significantly reduces the number of rays needed to compute the incident irradiance. In practice, BRT is mainly employed to solve the irradiance incident on the front (or back) surface of a PV module and FRT is typically used in combination with wave optics to solve the reflection and absorption in the internal layers of the PV module and the solar cells. 26–28 Radiance²⁹ is the most widely adopted backward ray tracer in the field of photovoltaics. 30–34 In order to alleviate the computational time, RT models are usu- ally employed to calculate daylight coefficients, 35 which are defined as the ratio between the irradiance incident on a target surface to the radiance emitted by a specific sky sector. Daylight coefficients are cal- culated to decouple the illumination conditions from the ray tracing solution of a specific geometry. 36 RT models provide a practical method to calculate daylight coefficients and to generate sensitivity maps²⁵ or daylight coefficient matrices. 32 These maps or matrices can then be multiplied by the sky radiance to calculate the irradiance on the solar cells under different sky conditions without repeating the ray tracing simulations. Two main desirable features for irradiance models, which are not readily available in current ray tracing models, are the ability to per- form spectrally-resolved simulations and to simulate surfaces with time-varying optical properties. Spectrally resolved irradiance simula- tions are important for bifacial PV systems 37–39 and will be essential in the near future to simulate the yield of tandem PV modules. 40,41 Meanwhile, the ability to simulate time-varying optical properties can be useful to model the effects of rain and snow on the surface reflec- tivity⁴² and improve the calculation of the bifacial energy gain in large PV power plants. 43 Whereas the implementation of these features in transposition and view factor models is rather simple, adding these simulation capabilities to existing RT implies a heavy computational burden. Considering that daylight coefficients depend on the wavelength-specific optical properties of the surfaces composing the scene, ray tracing simulations should be repeated to calculate daylight coefficients at every wavelength and for every possible combination of optical properties. In this article, we propose a backward ray tracing model to com- pute the irradiance on PV modules in scenarios with arbitrarily ori- ented diffuse and specular surfaces. The main novelty in this approach, is that the ray tracing calculations, the illumination condi- tions and the optical properties of the materials are decoupled. As a consequence, it is possible to avoid the repetition of the highly time- consuming ray tracing calculations when considering surfaces with

|radiance L|incident from direction r over the visible part of the||||
|---|---|---|---|---|
|sky Ω :|ð||ð||
||G ¼ L|ðrÞðr n Þ dΩ ¼ π|L ðrÞ dF|ð3Þ|

FIGURE 1 Irradiance components incident on a differential area

of a solar cell dAc. The beam component originates in the Sun, the diffuse component emanates from the sky dome and the reflected component comes from surfaces around the solar cell

time-varying optical properties and performing spectrally resolved irradiance simulations. This article is organised in the following way. In Section 2, rele- vant radiometry concepts are presented. The proposed approach is described in detail in Section 3. In Section 4, the model is validated with measurements taken with different sensors at the PVMD moni- toring station in Delft, the Netherlands. Finally, conclusions are pre- sented in Section 5.

### 2 | BASIC RADIOMETRIC CONCEPTS

The irradiance G on a differential area element of a solar cell dAcis defined as the total incident radiant flux dΦ per unit area. G can be divided into three components depicted in Figure 1: (1) The beam irra- diance (Gbeam) due to the radiant flux coming from the sun disk; (2) the diffuse irradiance (Gdiff) due to the radiant flux coming directly from the sky dome; and (3) the reflected irradiance (Grefl) due to the radiant flux that bounces on the surface of objects in the scene before reach- ing the solar cell * :

<u>dΦ</u> Gtot¼ ¼ Gbeamþ Gdiffþ Greflð1Þ dAc

Assuming that the Sun is a point source, the beam irradiance can be calculated using Equation (2) from the direct normal irradiance (DNI), and the scalar product of the normal vector to the solar cell nc and the vector that points from the centre of the solar cell to the cen- tre of the solar disk b:

Gbeam¼ DNI ðb nc2Þ

The diffuse irradiance can be determined by integrating the sky radiance Lskyincident from direction r over the visible part of the V

diff sky c sky c!s Ω V ΩV

where dΩ is the solid angle of a differential sky sector (i.e., sky patch). The second integral in Equation (3) is expressed in terms of the view factor from the differential area of the solar cell to a differential area element of the sky, which is defined as:

<u>1</u> dFc!s¼ π ðr ncÞ dΩ ð4Þ

Likewise, the reflected irradiance can be calculated by integrating the reflected radiance Lrincident from direction r over the part of the sphere around the solar cell that is blocked by surrounding reflective surfaces ΩB:

ð Grefl¼ LrðrÞðr ncÞ dΩ ð5Þ Ω B

The reflected radiance Lris determined by the radiance incident on the reflector and its optical properties described by the Bidirectional Reflectance Distribution Function (BRDF). The BRDF of an opaque reflective surface with normal nr, is defined as the ratio between the outgoing radiance dLrin direction r to the radiance incident Lifrom direction r:

ð ð L ðrÞ¼ rdL ðrÞ¼rBRDFðr, rÞ L ðrÞðrin Þ dΩrð6Þ Ω H ΩH

where ΩHis the hemisphere in front of the reflective surface. It must be noted that the incident radiance on each reflector L i depends on higher order reflections. Since the radiance incident on the reflector (Li) must be the emitted or reflected radiance at a point on another surface, Lris defined in terms of itself. 44 Therefore, practical methods, such as ray tracing, are needed to limit the recur- sivity of the problem and approximate the reflected irradiance on a solar cell.

*All the vectors in the equations of this article are unitary vectors.

3 | THE PROPOSED SIMULATION APPROACH

The irradiance simulation approach described in this section is based on a deterministic backward ray tracer limited to two ray bounces, which allows to simulate Lambertian and specular reflectors. The nov- elty of the approach lies in the order in which calculations are per- formed and the selection of results that are saved to reduce the computation time.

Þð

3.1 | Ray tracing A second independent hemispherical sampling is performed with
a higher angular resolution from the centre of the solar cell to gener- When surfaces in the scene have arbitrary shapes and orientations, it ate a shadow map. A shadow map is a binary representation of the is not possible to calculate view factors using closed-form formulas as sky visibility from a given point in the scene, and it will be used to cal- in 3D view factor models and the scene must be sampled by casting culate the beam irradiance component. To generate shadow maps rays. In this section, the scene in Figure 2A is used to illustrate the only rays that point forward from the solar cell and to the sky need to steps of the ray tracing algorithm in the proposed approach. be traced. An example of a shadow map is shown in Figure 3, where First, a deterministic hemispherical sampling is performed by dis- cretising an imaginary sphere centred at the solar cell as shown in

Figure 2B. In Figure 2B, an equiangular discretisation is applied, yet it

is important to note that the method is not limited to this specific dis- cretisation. With the sky discretisation, the view factors from the solar cell to each sky patch (dFc!s) are determined by the position (s) and the solid angle of the sky patch (dΩ) as expressed in Equation (4). Next, primary rays are cast from the centre of the solar cell to the centroids of the sky patches in front of the cell (Figure 2C). Intersec- tions between the scene and the rays can be solved combining an appropriate data structure (e.g., octrees and kD-trees) with efficient ray-surface intersection algorithms (e.g., Möller-Trumbore⁴⁵). Rays that do not intersect with surfaces in the scene correspond to sky patches that are visible from the solar cell (“visible sky patch” in

Figure 2D). For rays that intersect with surfaces in the scene, the pro-

jections of the corresponding sky patches at the intersection points are considered (“projection of blocked patch” in Figure 2D). It should be noted that the view factor from the solar cell to each blocked sky patch (in Figure 2E) is equal to the view factor from the solar cell to

FIGURE 3 Shadow map. This shadow map corresponds to the

the corresponding projected patches. A list with all the blocked rays solar cell in Figure 2A, which is facing North and tilted 30. The and the indices of the corresponding intersected surfaces is stored in angular resolution of this map was chosen for illustrative purposes. memory after the primary ray tracing. The typical resolution of a shadow maps is 1 or better

FIGURE 2 Graphical representation of the proposed ray tracing approach. (A) Example of a solar cell surrounded by two obstacles.

(B) Spherical discretisation. (C) Hemispherical sampling. (D) Visible and blocked sky patches. (E) Projection of the blocked patches on the surfaces intersected by the primary rays. (F) Primary and secondary rays

ET AL

|||||ANDRES|.|
|---|---|---|---|---|---|
|The discrete form of Equation (3) is used to calculate the diffuse component of the irradiance incident on the solar cell using the view factors from the cell to the unobstructed sky patches. In this work,|SFðtÞ¼|1 if the sun is visible, 0 if the sun is blocked,|||ð7Þ|
|the diffuse sky radiance (L sky radiance distribution model.||) in Equation (3) is calculated using Perez||||
|The|irradiance contribution|of specular|reflectors|is calculated||
|considering|that the|BRDF is a Dirac|delta function.|Then,|the|
|irradiance contribution of an ideal specular patch with normal n|||||and|
|solid angle given by|dΩ intersected dG|by a primary ¼ L ðpÞF ðp, n ¼ π L ðpÞF ðp, n|ray with Þðr₁ n ÞdΩ ÞdF|direction|r₁ is ð8Þ|
|where p is the specular reflection of r₁ about n factor which also depends on the refractive indices of the specular|||, and F|is the Fresnel||
|material (n) and the air (n||).||||
|In the case of Lambertian reflectors with normal n||||and solid angle||
|dΩ, the calculated as|contribution dG|to the irradiance ¼ π G ρ|on ðr₁ n ÞdΩ|the solar|cell is|
|||¼ ρ₁ G|dF||ð9Þ|
|where ρ₁ and G||are the reflectivity and the irradiance of the||||
|primary|Lambertian reflector|intersected|by r₁,|respectively.|The|
|irradiance irradiance; (2) the diffuse irradiance; and (3) the reflected irradiance by secondary reflectors (i.e., surfaces intercepted by secondary rays). The first two components can be determined using Equation (2) and Equation (3) from the position of the primary reflector instead of the|G consists|of three|components:|(1) the|beam|
|position|of the solar|cell. The third|component|is calculated||
|recursively|using Equation|(9) from|the position|of the|primary|
|reflector.|To limit the|recursivity of|the problem,|the irradiance||
|incident on secondary reflectors (G|||) is calculated considering|||
|only the Equation (10). where n₂ is the normal vector to the secondary reflector and Pz is the|sky beam G|and sky diffuse ¼ DNI ðb n₂Þ SF þ Pz DHI|irradiance ðÞ, SVF|according|to ð 10Þ|
|simplified|Perez diffuse|irradiance|model according|to|which|
|the diffuse|irradiance is|calculated|as the sum of|the circumsolar,||
|horizon|band and|isotropic background|contributions.||For|
|each secondary|reflector,|the shading|factor|(SF) and the|sky|
|view factor memory. It should be noted that an intrinsic bias arises in this approach since it is limited to two ray reflections. This means that, even for an|(SVF) are|calculated from|the shadow|maps stored|in|
|ideal simulation|where|the number|of rays tends|to infinity,|the|

the zeros correspond to sky patches blocked by the objects on the scene and ones to visible sky patches. The resulting shadow map is stored in memory. Shadow maps are binary arrays and require very limited storage space despite the high angular resolution. Approxi- mately, 1000 shadow maps with an angular resolution of 1 occupy only 3 MB. Then, for each intersection point between a primary ray and thesky scene (i.e., for every primary intersection point), the simulation 46 develops differently depending on the type of intersected surface. If the intersected surface is an ideal specular reflector, a single second- ary ray is cast from the primary intersection point. The direction ofr the secondary ray is given by the specular reflection of the primaryr ray on the intersected surface. If the secondary ray does not intersect with the scene, the index of the pointed sky patch is associated with the specular reflector patch and stored in memory, otherwise it is refl sky R r c r1 neglected. Otherwise, if the surface intersected by the primary ray is asky R r c!r1 Lambertian reflector, a secondary hemispherical sampling is per- formed from the primary intersection point (e.g., P₁ in Figure 2F).r R Again, some of the rays cast during the secondary hemispherical sam- pling will reach the sky and some will intersect with surfaces in theair scene at secondary intersection points (e.g., P₂ in Figure 2F). Ther results of each of the secondary hemispherical samplings are stored inr1 memory, same as in the case of the primary sampling. A shadow map is also generated and stored at every primary intersection point on a refl <u>1</u> hemiðr1Þ c r1 Lambertian reflector. Finally, at each secondary intersection point (e.g., P₂ in Figure 2F), hemiðr1Þ c!r1 the proposed approach only calculates the beam and diffuse irradi- ance contributions. For this purpose, a tertiary hemispherical samplinghemiðr1Þ is performed to generate shadow maps at every secondary inter- section point. The shadow map, the secondary intersection point andhemiðr1Þ the normal to the intersected surface are also stored in memory. To reduce the number of hemispherical samplings, new shadow maps are only calculated when a new intersection point is further than a spe- cific user-defined distance from all previously calculated and stored intersection points. † The described ray tracer only distinguishes between specular and diffuse reflectors. Therefore, the results of the hemispherical sam- plings and the shadow maps stored in memory are independent fromhemiðr2Þ the sky radiance and the reflectivity of the surfaces in the 3D model. Once the ray tracing calculations are completed, the irradiance is cal- culated as explained in the following section. hemiðr2Þ

3.2 | Irradiance calculation The beam irradiance incident on the solar cell is calculated by multi- plying Equation (2) by the shading factor (SF), a time-dependent binary
7 function defined in Equation (7). The shading factor indicates when the sun is blocked by the surroundings and it can be easily determined using shadow maps as look-up tables.

† In this work this parameter was set to 0.2 m

simulated irradiance on a specific sensor might differ from the actual irradiance received by the sensor. Assuming a perfect description of the optical properties of the materials in the scene and a perfect description of the sky radiance distribution, the proposed approach should result in an underestimation of the irradiance incident on the sensor. It is also worth noting, that this bias is even larger in view fac- tor models (both 2D and 3D) because most methods described in the literature are equivalent to a ray tracing model limited to a single ray bounce. To compensate this bias in view factor models, the most com- mon practice consists in overestimating the irradiance incident on the ground by considering that unshaded sectors receive the global hori- zontal irradiance (GHI) and shaded sectors receive only the diffuse horizontal irradiance (DHI). 16,18–20 The overestimation of irradiance approximately compensates the bias introduced by the limitations of the view factor models. It is possible to apply a similar workaround to the proposed approach by adding a third term to Equation (10)to approximate the reflected light on secondary reflectors considering the local albedo α:

Ghemiðr2Þ¼ DNI ðb n₂Þ SFþ Pz DHI ðÞþ, SVF ð11Þ α GHI ð1 SVFÞ

Using the ray tracing results, the irradiance incident on the solar cell can be quickly recalculated if the reflectivity of a surface changes. This allows to efficiently simulate surfaces with time-varying reflectivity values by considering ρðtÞ in Equation (9). Furthermore, all the presented equations can be expressed as a function of a specific wavelength and later integrated over the relevant spectral range to quickly perform spectrally resolved irradi- ance simulations. To demonstrate the ability of the proposed approach to perform spectral simulations, in this work the solar spec- trum is modelled combining DNI and DHI spectra generated with the SMARTS model 47–49 and the SBDART model. 50 The DNI and DHI spectra were originally generated for solar azimuth angles ranging from 0 to 89 in steps of 1, and then interpolated to calculate the spectral distribution of the beam and diffuse components for different solar altitude values. SBDART was used to generate spectra for 3 dif- ferent sky conditions (clear, cloudy and overcast) and a DNI-based sky classifier was used to identify the sky condition at each time as explained in Appendix D. By contrast, SMARTS can only generate spectra for clear sky conditions, thus it is expected to differ signifi- cantly from the actual spectra under partially cloudy and overcast skies. It is worth to note that several studies propose spectral sky models, 51–56 yet more research is needed to develop a generalised model that can accurately describe the spectral sky radiance in the presence of clouds. Another relevant characteristic of the proposed approach is that it allows to directly simulate the effect of the incidence angle modifier (IAM) and the transmissivity of the PV module front layer. Since the direction of all the irradiance contributions is known, the angular effects can be easily included by adding a multiplicative factor in Equations (2), (3) and (5).

### | EXPERIMENTAL VALIDATION

4.1 | Measurement setup The irradiance model described in Section 3, was implemented and validated using measurements taken at the PVMD monitoring station shown in Figure 4A located in Delft, the Netherlands. At the monitor- ing station, a Kipp & Zonen SOLYS2 sun tracker equipped with a SMP 21 pyranometer and a SHP1 pyrheliometer was used to measure the diffuse horizontal irradiance (DHI) and the direct normal irradiance (DNI), respectively. The three irradiance sensors indicated in Figure 4B were used to validate the model: a monocrystalline ISET sensor (IKS Photovoltaik) facing South and tilted 30 (S1); a SMP10 thermopile pyranometer (Kipp & Zonen) facing 65 East from North and tilted 90 (S2); and a MS-700 spectroradiometer (EKO Instruments) mounted horizontally (S3). The 3D model of the monitoring station shown in Figure 4B was generated to simulate the irradiance at the position of sensors S1, S2 and S3. The 3D model was created combining information from floor plans, Lidar data and in-situ measurements with a laser distance meter. The accuracy of the 3D model was further evaluated by com- paring photographs taken with an Horicatcher device at 10 positions with raster images generated from the 3D model. The relative differ- ence in the sky view factor between the photographs and the raster images is below 2% for all the positions evaluated. Rasterised images generated with the implemented ray tracer from the perspective of the three sensors are presented in Appendix A.
FIGURE 4 PVMD monitoring station. (A) Photograph. (B) Ray
 tracing-based rendering generated with the CAD model

||FIGURE 6|Effect of the ambient bounces (ab) parameter on the|
|---|---|---|
|||simulated irradiance on sensor S2 with Radiance. The simulation with ab ¼ 0 only calculates the beam irradiance incident on the sensor|
|Spectral reflectivity of the surfaces in the scene. The weighted average reflectivity of each material considering the AM1.5G solar spectrum is indicated in the legend in between All the surfaces in the scene are either ideal specular or Lamber- tian reflectors. Samples of most surfaces in the scene were taken and characterised using a LAMBDA 1050 spectrophotometer. The spec- tral reflectance of the surrounding vegetation and the concrete was 58,59 retrieved from the ECOSTRESS Spectral Library. The spectral and average reflectivity of all the materials in the scene is presented in | Simulation parameters The irradiance calculated with the proposed approach was compared to measurements and to simulations performed with Radiance (using the program rtrace), a well-established lighting simulation software described in Appendix B. The selection of the input parameters for rtrace is crucial to obtain accurate results and reasonable computation times. Considering the size and the level of detail of the scene the fol- values were chosen: ad ¼ 1024, as ¼ 64, ab ¼ 2, aa ¼ 0:1, The effect of the ambient bounces (ab) in the simulated irradiance on sensor S2 is shown in Figure 6 using DNI and DHI minutely mea- sured during 21 August 2020, as inputs to calculate the sky radiance distribution. As already explained, higher ab improves the accuracy of the simulation; however, doubling the value of ab approximately dou- bles the computation time. Due to the highly reflective white wall (ρ ¼ 0:74) in front of the sensor, it is clear that more than one ambient ‡ bounce is required to obtain reasonable results. The normalised mean errors (nMBE) and root square errors (nRMSE) are given Table 1. As expected, results converge when the number of ambient|theless, most 4.3 | and in|bounces is increased. In this scenario, the most accurate simulation (ab ¼ 4) overestimates the daily irradiation by 2% as indicated by the nMBE value in Table 1. Results also indicate that using more than three ambient bounces offers no improvement in the simulation accu- racy, yet it significantly increases the total computation time. Never- for the simulation presented in the following section ambient bounces were limited to 2, since this ab value offered the reasonable compromise between accuracy computation time. To make a fair comparison between the proposed approach and Radiance, the number of rays in both models must be similar. The sim- ulation results of the proposed approach presented in the following sections were obtained using an equiangular discretisation (Figure 2B) with 60 azimuthal and 30 polar divisions. Hence, when hemispherical sampling is performed, 900 rays are cast with the proposed approach compared to the ad value of 1024 typically employed in Radiance. When using the proposed approach, the results of the ray tracing calculations for each of the simulated sensors were stored in memory to accelerate the irradiance calculations. Ray tracing results include the indices of the primary and secondary rays that intersect with the scene, the normal vectors and the optical properties of the intersected surfaces, and the shadow maps. The simulations results with 900 pri- mary rays occupied only 5gb in average per each evaluated test point. Consequently, the ray tracing results of a 72-cell PV module with 4 test points per cell in a complex scenario would occupy less than 1.5 GB of storage space. Irradiation simulations The irradiance incident on sensors S1 and S2 was simulated using minutely DNI and DHI measurements taken between August 2020 and February 2021. A comparison between the proposed approach Radiance was carried out considering the average reflectivity values for the surfaces listed in Figure 5. The incidence angle modifier (IAM) of reference cell S1 was mod-|

FIGURE 5

parentheses

the

and

Figure 5.

4.2
lowing ar ¼ 1024.

bias

‡ Errors are normalised by the mean irradiance value. elled according to the physical model presented in De Soto et al⁶⁰

since manufacturer data were not available. In the proposed approach, (21 August 2020), when the sun is behind the sensor and the white the calculation of the IAM for the radiance incident on the solar cell wall is directly illuminated. from each direction is straightforward, as explained in Section 3.2.On The proposed approach is compared to Radiance and the mea- the other hand, rtrace does not inform the angular distribution of the surements in Figure 8, where it is possible to see that both models incident radiance. Hence, to improve the simulation of the IAM effect, the diffuse and reflected components were separated from the beam component by performing simulations with 0 and 2 ambient bounces. Then, the angle of incidence of the beam component was calculated as in Equation (2), and the effective angle of incidence of the reflected and diffuse components (56.8 ) was calculated according to Gilman 61 et al. In Figure 7, the irradiance simulated with the proposed approach is compared to the measurements of sensors S1 and S2 in clear sky and overcast conditions. The simulated global irradiance was decom- posed into its three components. The reflected irradiance component on sensor S1 is almost negligible due to the low tilt of the sensor. Contrarily, the reflected component has a significant contribution on the global irradiance received by sensor S2, which is oriented verti- cally and in close proximity to a highly reflective white wall. This

|cally and in close proximity to||a highly reflective white wall.||This||
|---|---|---|---|---|---|
|effect|is more evident|the afternoon|of the clear|sky day||

during

TABLE 1 Normalised mean bias error, mean absolute error and

root mean square error corresponding to Figure 6

ab 0123 4 nMBE (%) 58.0 12.3 0.3 2.0 2.1

|nMBE (%)|58.0|12.3|0.3|2.0|2.1||
|---|---|---|---|---|---|---|
|nMAE (%)|58.0|12.4|4.1|3.9|4.0||
|nRMSE (%) negative nMBE values indicate that the simulation overestimates the irradiance.|65.1|14.5|5.6|6.3|6.3|weekly irradiation on reference cell S1 (A) and pyranometer S2 (B)|

Note: Values are normalised by the mean of the measured data and FIGURE 8

Comparison between the measured and simulated

FIGURE 7 Simulated irradiance components on sensors S1 and S2 with the proposed approach. (A) Measured and simulated irradiance on

sensor S1 during a clear sky day. (B) Measured and simulated irradiance on sensor S1 during an overcast day. (C) Measured and simulated irradiance on sensor S2 during a clear sky day. (D) Measured and simulated irradiance on sensor S2 during an overcast day

|S2 between 19 August 2020 and 5 February 2021|can accurately simulate the weekly irradiation throughout the entire period. The irradiation was calculated by integrating the minutely irra- diance over an entire week after filtering out the outliers (0.2% of the data points). The relative mean absolute error in the daily irradiation simulated with the proposed approach is 3.5% and 4.3% for sensors S1 and S2, respectively. The normalised errors calculated based on the minutely measurements are presented in Table 2. The simulated root mean square error of the simulated irradiance on sensors S1 and Proposed approach|Normalised mean bias error, mean absolute error and|Radiance|present because reflected|62 response of silicon, lower nMAE compared the proposed irradiance on|irradiance on sensor S1 is more accurate with the proposed approach than with Radiance mainly due to the approximation of the effective angle of incidence of the diffuse irradiance component. Despite the fact that reference cells tend to underestimate the measured irradi- ance in cloudy skies and low solar altitudes as a result of the spectral to because sensor S1 receives much less reflected irradiance than sensor S2. It can also be noticed, especially in Figure 8B, that the proposed approach tends to yield higher values than Radiance. In part, this is approach secondary Equation (11). If this contribution is neglected and Equation (10)is|the simulated irradiances on reference cell S1 pyranometer considers the reflectors|S2. The contribution expressed|
|---|---|---|---|---|---|---|---|---|
|S1 0.1 7.7 21.1|S2 12.7 Note: Values are normalised by the mean of the measured data and negative nMBE values indicate that the simulation overestimates the|-0.1 8.1|S1 S2 1.4 3.4 7.2 7.6 21.5 12.9|used|instead, the nMBE ence cell S1 (τ 95% DNI and DHI (τ 95% time leads to an increased RMSE.|of the increases to 0.5%. On the other hand, the high nRMSE of sensor S1 is explained by the large response time difference between the refer- illumination conditions are varying quickly, the difference in response|proposed < 100ms) and the thermopile sensors that measure <2s). Especially during partially cloudy day when|approach at|

reason is

TABLE 2

of the in

Sensor sensor S2 nMBE (%) nMAE (%) nRMSE (%)

irradiance.

FIGURE 9 Spectral irradiance simulations with the proposed approach. (A) Integrated measured and simulated spectral irradiance on sensor

S3. The green arrows indicate the time instants at which the spectra are compared. The yellow dashed line indicates which SBDART spectra was chosen at each time according to the simple sky classifier in Appendix D.(B–D) Spectra and sky images at 8:00 a.m. 1:00 p.m., 3:30 p.m. and 6:00

p.m., respectively

4.4 | Spectral simulations noticed, that this wavelength range concentrates approximately
77.5% of the power in the AM1.5G spectrum and covers the most sig-
To demonstrate the ability of the proposed approach to perform spec-nificant part of the spectral responsivity of any PV module on the trally resolved simulations, the measured and simulated irradiance at market. The sky camera pictures in Figure 9 show that during the the position of spectroradiometer S3 are compared in Figure 9 during morning it was rainy and the sky was overcast. Towards the after- an entire day. The irradiance was simulated with 5nm resolution noon, the clouds were dispersed and the sky became clear. Overall,

|an entire|day. The|irradiance|was simulated|with 5nm|resolution|
|---|---|---|---|---|---|
|between 300 and 2500 nm, using DNI and DHI measurements to scale||||||
|the spectra generated with SMARTS and SBDART(refer to Tables 3||||||
|and 4). The time resolution for the spectral simulations was 30 s.||||||
|Using the precalculated ray tracing solution at the position of S3, it||||||
|took approximately 3 min to evaluate the spectral irradiance for an||||||
|entire day.||||||
|The 1050 nm, which is the valid measurement range of S3. It should be|irradiance|in Figure|9A is integrated|between|350 and|
|TABLE 3|SMARTS parameters|||||

the simulated integral irradiance is in good agreement with the mea- surements. The largest deviations from the measurements occur when the sun is covered by clouds. In particular, the comparison between the measurements and the simulations using SMARTS spectra as input (Figure 9B) shows a signif- icant spectral mismatch in the morning. This mismatch was expected since clouds cause a red-shift in the spectrum⁵¹ and SMARTS can only be used to generate spectra for clear sky days. It can also be noted that, as clouds disappear in Figure 9D,E, the spectral match improves for exactly the same reasons.

|Parameter||Value||
|---|---|---|---|
|Surf. Pressure (mb)||1013.25||
|Altitude (km)||0||
|Atmosphere|||U.S. Std Atm 1976|
|Water vapoUr|||From ref. atm. and alt.|
|Ozone||Def. ref. atm.||
|CO2 (ppvm)||370||
|Ext. Spectrum|||Gueymard 2002|
|Aerosol model||Urban S&F||
|Turbidity at 500 nm||0.084||
|Albedo||Light soil||
|Spectral range (nm)||280–4000||
|Circumsolar|||Radiometer aperture 2.9|
|TABLE 4|SBDART parameters|||
|Parameter|Clear|Cloudy|Overcast|
|NF|1|1|1|
|ISAT|0|0|0|
|WLINF|0.28|0.28|0.28|
|WLSUP|4|4|4|
|WLINC|0.001|0.001|0.001|
|SZA|0:89.5|0:89.5|0:89.5|
|ISALB|6|6|6|
|IDATM|6|6|6|
|UW|1.42|1.42|1.42|
|UO3|0.324|0.324|0.324|
|IAER|1|1|1|
|TBAER|0.084|0.084|0.084|
|ZCLOUD|n/a|2.0|2.0 6.0|
|TCLOUD|n/a|1.0|60.0 60.0|
|NRE|n/a|10.0|20.0 20.0|
|ZOUT|0,1|0,1|0,1|

As expected, in the presence of clouds, the results of the simula- tions using SBDART spectra are in better agreement with the mea- surements compared to SMARTS. However, the spectral mismatch at 8 a.m. illustrates the challenge of generalising cloudy and overcast spectra. Spectral matching in the presence of clouds could be improved by defining new sky types and using additional inputs to the sky classifier algorithm to identify each sky type. These results show that the proposed approach is able to perform simulations with high spectral and temporal resolution. Nevertheless, it is also evident the importance of using a proper sky model to describe the effect of clouds.

### 5 | CONCLUSIONS

A model for simulating the irradiance incident on PV systems in geo- metrically complex scenes has been presented. The model is a back- ward ray tracer limited to two ray bounces, which only considers ideally diffuse and specular reflectors to simplify the calculation of interreflections. The main advantage of the presented simulation approach is that it allows to fully decouple the solution of the ray tracing problem from both the optical properties (i.e., reflectivity) of the surfaces in the scene and the illumination conditions. The decoupling of the irradi- ance simulation problem into three parts allows to significantly reduce computation times in comparison to conventional ray tracing simula- tion approaches. The highly time consuming ray tracing simulations only need to be solved once and the results are stored in memory to quickly evaluate the irradiance profile on the module. Moreover, with the presented approach, it is possible to solve problems that could otherwise imply a very long computation time, e.g., solving the irradi- ance incident on a PV module with high spectral resolution (over 100 spectral bands) at every minute during an entire year. A validation study was carried out using measurements of differ- ent types of irradiance sensors installed at the PVMD monitoring sta- tion, in the Netherlands. A detailed 3D description of the monitoring IOUT station was created to simulate the irradiance incident on the sensors.

It was determined that the mean absolute error of the daily irradiation simulated with the proposed approach over a period of 6 months is lower than 5% using both a pyranometer and a reference cell. A com- parison with Radiance limited to two ambient bounces, suggests that the optical performance of the proposed approach is slightly better and the computation time can be reduced by three orders of magni- tude when performing annual irradiance simulations with minutely resolution. Finally, spectral simulations were performed using the diffuse and beam spectra generated with SMARTS and SBDART as inputs to the irradiance model, and compared to measurements taken with a spec- troradiometer. Results indicate that even though the proposed approach is capable of quickly computing the incident irradiance with high spectral and temporal resolution, the simulated spectrum can sig- nificantly differ from the measurements. While under clear sky condi- tions there is a good agreement between measurements and simulations, in the presence of clouds there is a larger mismatch due to the a red-shift in the spectrum in comparison to clear sky condi- tions. The presented results put in evidence the need for a more sophisticated spectral sky model to reproduce the atmospheric condi- tions and account for the effect of clouds. The ability of the proposed irradiance simulation approach to dis- tinguish between different types of reflectors instead of using a single albedo value allows to improve the accuracy of the estimation of the irradiance impinging on PV modules that receive a large portion of reflected irradiance. Moreover, in comparison to traditional ray tracers, the presented approach offers a practical way to simulate sur- faces with time varying optical properties and compute the spectral irradiance incident on a PV module. These features are particularly valuable for the simulation of bifacial and tandem PV systems.

ACKNOWLEDGEMENT The data that support the findings of this study are available from the corresponding author upon reasonable request.

ORCID Calcabrini Andres [https://orcid.org/0000-0002-1940-4705](https://orcid.org/0000-0002-1940-4705) Manganiello Patrizio [https://orcid.org/0000-0002-4752-0068](https://orcid.org/0000-0002-4752-0068)

REFERENCES

1. Ballif C, Perret-Aebi L-E, Lufkin S, Rey E. Integrated thinking for pho- tovoltaics in buildings. Nat Energy. 2018;3(6):438-442.
2. Ortiz Lizcano JC, Haghighi Z, Wapperom S, Infante Ferreira C, Isabella O, vd Dobbelsteen A, Zeman M. Photovoltaic chimney: ther- mal modeling and concept demonstration for integration in buildings. Prog Photovolt: Res Appli. 2020;28(6):465-482.
3. Brito MC, Santos T, Moura F, Pera D, Rocha J. Urban solar potential for vehicle integrated photovoltaics. Trans Res Part D: Transp Environ. 2021;94:102810.
4. Kutter C, Basler F, Alanis LE, Markert J, Heinrich M, Neuhaus DH. Integrated lightweight, glass-free pv module technology for box bod- ies of commercial trucks. In: 37th European PV Solar Energy Confer- ence and Exhibition (EUPVSEC); 2020:1711-1718.
5. United Nations. Sustainable development goals. [https://www.un.org/](https://www.un.org/) sustainabledevelopment/energy/; 2016.
6. Liu BenjaminYH, Jordan RC. The long-term average performance of flat-plate solar-energy collectors: with design data for the us, its out- lying possessions and canada. Sol Energy. 1963;7(2):53-74.
7. Perez R, Seals R, Ineichen P, Stewart R, Menicucci D. A new simplified version of the Perez diffuse irradiance model for tilted surfaces. Sol Energy. 1987;39(3):221-231.
8. Reindl DT, Beckman WA, Duffie JA. Evaluation of hourly tilted sur- face radiation models. Sol Energy. 1990;45(1):9-17.
9. Freeman J, Freestate D, Hobbs W, Riley C. Using measured plane-of- array data directly in photovoltaic modeling: methodology and valida- tion. In: 2016 IEEE 43rd Photovoltaic Specialists Conference (PVSC) IEEE; 2016:2653-2656.
10. Khalil SA, Shaffie AM. Evaluation of transposition models of solar irra- diance over egypt. Renew Sustain Energy Rev. 2016;66:105-119.
11. Mubarak R, Hofmann M, Riechelmann S, Seckmeyer G. Comparison of modelled and measured tilted solar irradiance for photovoltaic applications. Energies. 2017;10(11):1688.
12. Ineichen P, Guisan O, Perez R. Ground-reflected radiation and albedo. Sol Energy. 1990;44(4):207-214.
13. Jäger K, Tillmann P, Becker C. Detailed illumination model for bifacial solar cells. Opt Express. 2020;28(4):4751-4762.
14. Mermoud A, Wittmer B. Bifacial shed simulation with PVSyst. In: Bifacial workshop; 2017:25-26.
15. Marion B, MacAlpine S, Deline C, et al. A practical irradiance model for bifacial PV modules. In: 2017 IEEE 44th Photovoltaic Specialist Conference (PVSC) IEEE; 2017:1537-1542.
16. Chudinzow D, Haas J, Díaz-Ferrán G, Moreno-Leiva S, Eltrop L. Simu- lating the energy yield of a bifacial photovoltaic power plant. Solar Energy. 2019;183:812-822.
17. Hansen CW, Gooding R, Guay N, et al. A detailed model of rear-side irradiance for bifacial pv modules. In: 2017 IEEE 44th Photovoltaic Specialist Conference (PVSC) IEEE; 2017:1543-1548.
18. Shoukry I, Libal J, Kopecek R, Wefringhaus E, Werner J. Modelling of bifacial gain for stand-alone and in-field installed bifacial PV modules. Energy Procedia. 2016;92:600-608.
19. Yusufoglu UA, Pletzer TM, Koduvelikulathu LJ, Comparotto C, Kopecek R, Kurz H. Analysis of the annual performance of bifacial modules and optimization methods. IEEE J Photovoltaics. 2014;5(1): 320-328.
20. Berrian D, Libal J. A comparison of ray tracing and view factor simula- tions of locally resolved rear irradiance with the experimental values. Prog Photovolt Res Appl. 2020;28(6):609-620.
21. Nussbaumer H, Janssen G, Berrian D, et al. Accuracy of simulated data for bifacial systems with varying tilt angles and share of diffuse radiation. Solar Energy. 2020;197:6-21.
22. Gross U, Spindler K, Hahne E. Shapefactor-equations for radiation heat transfer between plane rectangular surfaces of arbitrary position and size with parallel boundaries. Lett Heat Mass Transf. 1981;8(3): 219-227.
23. Sönmez FF, Ziar H, Isabella O, Zeman M. Fast and accurate ray-cast- ing-based view factor estimation method for complex geometries. Sol Energy Mater Sol Cells. 2019;200:109934.
24. Bartell F, Dereniak E, Wolfe W. The theory and measurement of bidi- rectional reflectance distribution function (BRDF) and bidirectional transmittance distribution function (BTDF). In: Radiation scattering in optical systems, Vol. 257 International Society for Optics and Photon- ics; 1981:154-160.
25. Santbergen R, Muthukumar VA, Valckenborg RME, van de Wall WJA, Smets AHM, Zeman M. Calculation of irradiance distribution on PV modules by combining sky and sensitivity maps. Sol Energy. 2017; 150:49-54.
26. Holst H, Winter M, Vogt MR, Bothe K, Köntges M, Brendel R, Altermatt PP. Application of a new ray tracing framework to the anal- ysis of extended regions in SI solar cell modules. Energy Procedia. 2013;38:86-93. [https://www.daidalos-cloud.de](https://www.daidalos-cloud.de)

27. PV Lighthouse. Sunsolve. [https://www.pvlighthouse.com.au/](https://www.pvlighthouse.com.au/) sunsolve; 2021.
28. Santbergen R, Meguro T, Suezaki T, Koizumi G, Yamamoto K, Zeman M. Genpro4 optical model for solar cell simulation and its application to multijunction solar cells. IEEE J Photovoltaics. 2017;7(3): 919-926. [https://asa.ewi.tudelft.nl/](https://asa.ewi.tudelft.nl/)
29. Ward GJ. The radiance lighting simulation and rendering system. In: Proceedings of the 21st Annual Conference On Computer Graphics and Interactive Techniques; 1994:459-472.
30. Deline C, Ayala S. Bifacial_Radiance. computer software. USDOE Office of Energy Efficiency and Renewable Energy (EERE), Solar Energy Technologies Office (EE-4S) 10.11578/dc.20180530. 16. [Online]. Available: [https://github.com/NREL/bifacial_radiance](https://github.com/NREL/bifacial_radiance); 2021.
31. Hansen CW, Stein JS, Deline C, MacAlpine S, Marion B, Asgharzadeh A, Toor F. Analysis of irradiance models for bifacial PV modules. In: IEEE 43rd Photovoltaic Specialists Conference (PVSC) IEEE; 2016:138-0143.
32. Horvath I, Manganiello P, Goverde H, et al. Towards efficient and accurate energy yield modelling of bifacial PV systems. In: 35th European pv Solar Energy Conference and Exhibition (EUPVSEC);
2018.
33. Pelaez SA, Deline C, Greenberg P, Stein JS, Kostuk RK. Model and validation of single-axis tracking with bifacial PV. IEEE J Photovoltaics. 2019;9(3):715-721.
34. Pelaez SA, Deline C, MacAlpine SM, Marion B, Stein JS, Kostuk RK. Comparison of bifacial solar irradiance model predictions with field validation. IEEE J Photovoltaics. 2018;9(1):82-88.
35. Tregenza PR, Waters IM. Daylight coefficients. Light Res Technol. 1983;15(2):65-71.
36. Reinhart CF, Walkenhorst O. Validation of dynamic radiance-based daylight simulations for a test office with external blinds. Energy Build. 2001;33(7):683-697.
37. Brennan MP, Abramase AL, Andrews RW, Pearce JM. Effects of spec- tral albedo on solar photovoltaic devices. Sol Energy Mater Sol Cells. 2014;124:111-116.
38. Monokroussos C, Gao Q, Zhang X, et al. Rear-side spectral irradiance at 1 sun and application to bifacial module power rating. Prog Photo- volt Res Appl. 2020;28(8):755-766.
39. Ziar H, Sönmez FF, Isabella O, Zeman M. A comprehensive albedo model for solar energy applications: geometric spectral albedo. Appl Energy. 2019;255:113867.
40. Hörantner MT, Snaith HJ. Predicting and optimising the energy yield of perovskite-on-silicon tandem solar cells under real world condi- tions. Energy Environ Sci. 2017;10(9):1983-1993.
41. Lindsay N, Libois Q, Badosa J, Migan-Dubois A, Bourdin V. Errors in pv power modelling due to the lack of spectral and angular details of solar irradiance inputs. Sol Energy. 2020;197:266-278.
42. Gul M, Kotak Y, Muneer T, Ivanova S. Enhancement of albedo for solar energy gain with particular emphasis on overcast skies. Energies. 2018;11(11):2881.
43. Riedel-Lyngskær N, Ribaconka M, Po M, Thorsteinsson S, Thorseth A, ~ Dam-Hansen C, Jakobsen ML. Spectral albedo in bifacial photovoltaic modeling: what can be learned from onsite measurements?. In: 2021 48th IEEE Photovoltaic Specialists Conference (PVSC) IEEE; 2021: 1335-1338.
44. Ward G, Shakespeare R. Rendering with radiance: the art and science of lighting visualization. Calculation Methods. 3rd ed.; 1998:491-562.
45. Möller T, Trumbore B. Fast, minimum storage ray-triangle intersec- tion. J Graph Tools. 1997;2(1):21-28.
46. Perez R, Seals R, Michalsky J. All-weather model for sky luminance distribution–preliminary configuration and validation. Solar Energy. 1993;50(3):235-245.
47. Gueymard C. Smarts2, a simple model of the atmospheric radiative transfer of sunshine: algorithms and performance assessment. FSEC- PF-270-95, Florida Solar Energy Center Cocoa, FL; 1995.
48. Gueymard CA. Parameterized transmittance model for direct beam and circumsolar spectral irradiance. Solar Energy. 2001;71(5): 325-346.
49. Gueymard CA, Myers D, Emery K. Proposed reference irradiance spectra for solar energy systems testing. Solar Energy. 2002;73(6): 443-467.
50. Ricchiazzi P, Yang S, Gautier C, Sowle D. Sbdart: a research and teaching software tool for plane-parallel radiative transfer in the Earth's atmosphere. Bull Am Meteorol Soc. 1998;79(10):2101-2114.
51. Bartlett JS, Ciotti AM, Davis RF, Cullen JJ. The spectral effects of clouds on solar irradiance. J Geophys Res Oceans. 1998;103(C13): 31017-31031.
52. Bird RE, Riordan C. Simple solar spectral model for direct and diffuse irradiance on horizontal and tilted planes at the Earth's sur- face for cloudless atmospheres. J Appl Meteorol Climatol. 1986; 25(1):87-97.
53. Ernst M, Holst H, Winter M, Altermatt PP. Suncalculator: a program to calculate the angular and spectral distribution of direct and diffuse solar radiation. Sol Energy Mater Sol Cells. 2016;157:913-922.
54. Hosek L, Wilkie A. An analytic model for full spectral sky-dome radi- ance. ACM Trans Graph (TOG). 2012;31(4):1-9.
55. Kider Jr JT, Knowlton D, Newlin J, Li YK, Greenberg DP. A framework for the experimental comparison of solar and skydome illumination. ACM Trans Graph (TOG). 2014;33(6):1-12.
56. Winter M, Holst H, Vogt MR, Altermatt PP. Impact of realistic illumi- nation on optical losses in SI solar cell modules compared to standard testing conditions. In: 31st European PV Solar Energy Conference and Exhibition (EUPVSEC); 2015:1869-1874.
57. Boppana S, Passow K, Sorensen J, King BH, Robinson C. Impact of uncertainty in IAM measurement on energy predictions. In: 2018 IEEE 7th World Conference on Photovoltaic Energy Conversion (WCPEC)(a Joint Conference of 45th IEEE PVSC, 28th PVSEC & 34th eu pvsec) IEEE; 2018:2276-2281.
58. Baldridge AM, Hook SJ, Grove CI, Rivera G. The aster spectral library version 2.0. Remote Sens Environ. 2009;113(4):711-715.
59. Meerdink SK, Hook SJ, Roberts DA, Abbott EA. The ecostress spec- tral library version 1.0. Remote Sens Environ. 2019;230:111196.
60. De Soto W, Klein SA, Beckman WA. Improvement and validation of a model for photovoltaic array performance. Sol Energy. 2006;80(1): 78-88.
61. Gilman P, Dobos A, DiOrio N, Freeman J, Janzou S, Ryberg D. Sam photovoltaic model technical reference update. NREL/TP- 6A20-67399, Golden, CO, USA, NREL; 2018.
62. Karki S, Ziar H, Korevaar M, Bergmans T, Mes J, Isabella O. Perfor- mance evaluation of silicon-based irradiance sensors versus thermo- pile pyranometer. IEEE J Photovoltaics. 2020;11(1):144-149.
63. Cook RL. Stochastic sampling in computer graphics. ACM Trans Graph (TOG). 1986;5(1):51-72.
64. Subramaniam S. Daylighting simulations with radiance using matrix- based methods. Lawrence Berkeley National Laboratory; 2017.
65. Ward GJ, Rubinstein FM, Clear RD. A ray tracing solution for diffuse interreflection. In: Proceedings of the 15th Annual Conference on Computer Graphics and Interactive Techniques; 1988:85-92. How to cite this article: Andres C, Ruben C, David G, et al. Time-varying, ray tracing irradiance simulation approach for photovoltaic systems in complex scenarios with decoupled geometry, optical properties and illumination conditions. Prog Photovolt Res Appl. 2023;31(2):134‐148. doi:10.1002/pip.

|APP E NDIX A: VIEW FROM ANALYSED SENSORS|Radiance⁴⁴|AP PE NDIX B: IRRADIANCE SIMULATIONS WITH RADIANCE is a highly flexible and optimised lighting simulation tool|
|---|---|---|
|FIGURE A1 Raster images generated with our ray tracer|approach. 44 arately. ing artefacts|that has been continuously improved and validated over the last three decades. There are several programs that form part of this software suite. The program rtrace is used to trace the rays through the scene and calculate the irradiance on the solar cells. It is relevant to highlight the similarities and differences between Radiance and the proposed In order to perform a ray tracing simulation with rtrace, the illumi- nation conditions (i.e., DNI, DHI and the solar position) must be speci- fied to generate a description of the light sources with the program gendaylit.InRadiance, direct and diffuse light sources are sampled sep- The sun is considered a directional point light source and it is sampled with a single deterministic ray. The sky dome is considered 46 an extended diffuse light source described by Perez model, and it is sampled stochastically. The stochastic sampling approach, in opposi- tion to the proposed deterministic sampling, allows to eliminate alias- 63 in image rendering. Furthermore, Radiance can simulate surfaces with arbitrary BSDF functions, not only ideally dif- fuse and specular reflectors as in the proposed approach. The density of sampling rays can be adapted according to the illumination condi- tions to refine the sampling in in regions with larger irradiance gradi- ents. Hence, when the program rtrace is used to calculate irradiance, the ray tracing simulations must be repeated for every time step and|

depicting the field view from the perspective of the irradiance sensors. The black regions in the rasters correspond to the hemisphere behind the plane of array of the sensors. (A) View from reference cell S1 tilted 31 and facing South. (B) View from FIGURE B1 Relative computation time of year-long simulations pyranometer S2 tilted 90 and facing 65 East from North of a 72-cell PV module considering 2 ambient bounces with different (approximately North-Northeast). (C) View from spectroradiometer S3 temporal resolutions. It is assumed that the computation time is installed horizontally proportional to the number of traced rays according to Appendix B

simulations must be repeated to evaluate the spectral irradiance with more bands.

AP PE NDIX C: COMPUTATION COMPLEXITY COMPARISON

sky condition. Alternatively, the program rfluxmtx in Radiance, can be used to calculate daylight coefficients, 64 but this program was not used for this study. The calculation of diffuse interreflections in Radiance is not lim- ited to two ray bounces as in the proposed approach. A user-defined parameter is used to set the maximum number of ray bounces. More- over, ray tracing calculation are accelerated using the irradiance cach- ing algorithm, 65 which significantly reduces the number of points where higher order hemispherical sampling is performed. Irradiance caching is based on the assumption that diffuse illumination varies slowly over the scene, and hence it is not always necessary to initiate a new hemispherical sampling at each intersection point between a sampling ray and the scene. Under certain conditions, the irradiance at the new sampling point can be interpolated from cached values using irradiance gradients. The user can control the radius of validity of the gradient-based interpolation with different input parameters. The most relevant rtrace parameters for PV simulations are:

- Ambient divisions (ad): It indicates the number of primary rays used for hemispherical sampling.
- Ambient super-samples (as): It indicates the number of additional sample rays used in ambient divisions that present high variance.
- Ambient bounces (ab): It limits the maximum number of ray bounces allowed in the calculation of interreflections.
- Ambient accuracy (aa): There is an associated error that is esti- mated for each point where the irradiance is interpolated using irradiance gradients. If the interpolation error is larger than the ambient accuracy parameter, interpolation cannot be used and a new hemispherical sampling is initiated.
- Ambient resolution (ar): it determines the minimum distance between ambient sampling points. When the distance between two sampling points is smaller than the maximum scene dimension multiplied by aa and divided by ar, the new ambient value is inter- polated from the irradiance gradient independently of the error associated with the interpolation. One major difference between using rtrace and the proposed approach is the computation time. The program rtrace must be exe- cuted one time per simulated time instant; hence, the total computa- tion time increases linearly with the number of simulated time instants. On the contrary, the total computation time with the pro- posed approach is almost independent of the number of simulated instants. A comparison considering year-long simulations of a 72-cell PV module with different temporal resolutions is presented in Figure B1. The proposed approach is about 45 times faster than Radi- ance at calculating the hourly irradiance, and about 2700 times faster at performing year-long simulations with minutely resolution. Another important aspect is that the proposed approach can eas- ily handle dozens of spectral bands. However, Radiance is limited to only three independent channels (denominated R, G, and B) to calcu- late spectral irradiance. These channels can be used to perform spec- tral simulations using three arbitrary spectral bands, not necessarily in the visible spectrum. As a result, when using Radiance, ray tracing
The total computation time of ray tracing irradiance models is mainly determined by the total number of cast rays. In Radiance, the irradiance caching algorithm limits the geometric growth of the number of samplings required to solve diffuse interre- flections. Assuming that in average, the irradiance caching algorithm allows to reduce the number of sampling required at each higher level by 50%, 44 the total number of rays that are traced in one execution of the program rtrace when ab ¼ 2 is approximately:

R ¼ r þ <u>r²</u> þ <u>r³</u> ðC1Þ 1 2 8

where r is the original number of sampling rays (i.e., primary rays). The irradiance caching algorithm is particularly effective to evaluate the irradiance on multiple test points, thus R₁ is assumed to be indepen- dent of the number of evaluated test points. Nevertheless, since rtrace must be executed once per simulated time instant, the total number of traced rays and thus the total computation, time increase linearly with the number of simulated time steps. By contrast, the total number of rays that are traced with the pro- posed approach is independent of the number of simulated time steps, and it equals to the sum of the primary rays, secondary rays and the rays needed to generate the shadow maps. Therefore, the total number of rays needed to evaluate p test points with the proposed approach is:

R₂ ¼ p ðr þ r² þ rmþ rr²mÞþmrmðC2Þ

FIGURE C1 Required number of rays for a typical simulation of a 72-cell PV module. The number of required rays is approximated using Equations (C1) and (C2) where r ¼ 900, rm¼ 32400, p ¼ 288 and m ¼ 10000

where r is the number of rays cast in each primary and secondary samplings, rmis the number of rays cast to create each shadow map, and m is the number of shadow maps to solve the irradiance at sec- ondary intersection points. For shadow maps with an angular resolu- tion of 1, rm¼ 360 90. Since shadow maps at secondary intersection points are cached, typically less than 10000 shadow maps are enough to calculate the irradiance on all secondary intersection points. Figure C1 shows a comparison between the total number of rays required by Radiance (using the program rtrace) and the proposed approach for simulating a PV module with 72 solar cells and 4 test points per cell. The figure shows that the ray tracing calculations with the proposed approach take about the same time as 100 rtrace execu- tions. In other words, the proposed approach is faster than using rtrace when simulating more than 100 time steps. It should be noted that, when performing irradiance simulations in scenes with invariant optical properties, the daylight coefficient method is relatively faster compared to the proposed approach. As daylight coefficients can be calculated applying a stochastic and adap- tive hemispherical sampling method, less rays need to be traced com- pared to the deterministic hemispherical sampling in the proposed approach. On the other hand, when performing spectrally resolved irradiance simulations, the computation time of the daylight coeffi- cient method increases linearly with the number of spectral bands and is significantly higher than that of the proposed approach.

FIGURE D1 Simple DNI-based sky classifier algorithm. The function dipCnt determines the number of dips in a time series. APP E NDIX D : SPECTRAL MODELS DNITðtÞ indicates an interval of the DNI time series with length T and centred at instant t

SBDART allows to model the effect of clouds on the sunlight spec- trum. Beam and diffuse spectra for three generic sky conditions (clear, cloudy and overcast) have been generated using SBDART for the one of the three sky conditions at each time instant. As a first step, results presented in Section 4.4. These spectra were then used as an the dominant sky condition during the day is identified. Then the DNI input to the proposed irradiance simulation approach. time series is further evaluated by applying a 40 min moving window The sky classifier algorithm in Figure D1 is proposed to distin-to account for variations in cloud cover throughout the day. guish the sky condition at each simulated time instant. A two-step The values of the parameters used to generate the spectra with approach is used to count dips in the daily DNI time series and select SMARTS and SBDART are listed in Tables 3 and 4, respectively.
