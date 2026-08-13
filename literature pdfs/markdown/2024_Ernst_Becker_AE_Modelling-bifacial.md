Applied Energy 369 (2024) 123574

Contents lists available at ScienceDirect

# Applied Energy

journal homepage: www.elsevier.com/locate/apenergy

# Modelling bifacial irradiance – Step-by-step comparison and validation of view factor and ray tracing models

Marco Ernst a, *, Charles-Alexis Asselineau a, b, Peter Tillmann c, d, Klaus Jager ¨ c, d, Christiane Becker c

a *The Australian National University, School of Engineering, Canberra, ACT 2600, Australia* b *IMDEA Energy, Av. Ramon* ´ *de La Sagra, 3, 28935 M*´*ostoles, Madrid, Spain* c *Helmholtz-Zentrum Berlin für Materialien und Energie, Albert-Einstein-Straße 16, 12489 Berlin, Germany* d *Zuse Institute Berlin, Takustraße 7, 14195 Berlin, Germany*

HIGHLIGHTS

- Comparative analysis of View Factor (VF) & Ray Tracing (RT) models for bifacial PV.
- Both models perform similarly for front illumination, RT performs better for rear.
- VF overestimates module rear irradiance by 6.7% due to frame & structure shading. ARTICLE INFO ABSTRACT *Keywords:* This study presents a comprehensive comparative analysis of View-Factor (VF) and Ray Tracing (RT) models to Bifacial photovoltaic systems
evaluate their effectiveness in predicting bifacial irradiance in bifacial photovoltaic (PV) systems. The com Ray tracing parison was conducted using an experimental dataset from NREL (CO, USA), which included front and rear View-factor model plane-of-array (POA) irradiance values measured by silicon solar cell pyranometers. This initial step established a Irradiance predictions baseline understanding of each model's predictive capabilities in a real-world context. The comparison with POA Energy yield Structural components measurements indicates that for front illumination, both models are closely aligned with relative Root Mean Square Error (rRMSE) of 7.2% (VF) and 7.6% (RT). For rear illumination, the rRMSE increases to 20.9% and

22.9% for the VF and RT models, respectively. Additionally, both models show a similar relative Mean Bias Error (rMBE) for front illumination of 1.8% and 2.0% for the VF and RT methodologies, respectively. However, for rear illumination, the RT model predicts with only 0.1% bias, while the VF model *underestimates POA* irradiance by 8.4%. The study then focuses on directly comparing the VF and RT models in their simulation of cell-level irradiance. Starting from a VF-compatible problem, the research systematically introduces additional features and compo nents in RT simulations to assess the impact of increased complexity on irradiance predictions. In contrast to underestimating of the rear POA sensor values, the VF model *overestimates* rear *module* irradiance by 6.7% due to rear module shading by the frame and structure, which do not equally affect the POA sensors. These findings emphasize the importance of detailed geometric modelling in achieving accurate predictions. The overestimation of the module rear illumination translates to a 0.8% overestimation of energy yield by the VF model, considering cell-level irradiance values. Conclusively, the study highlights the significance of accurately incorporating structural elements when modelling bifacial PV systems.
**1. Introduction**
technology for increasing the yield of PV systems. Unlike their mono facial counterparts, bifacial systems harness sunlight from both the front Bifacial photovoltaic (PV) systems have become a fundamental and rear sides of solar modules, resulting in a significant increase in

* Corresponding author. *E-mail address:* marco.ernst@anu.edu.au (M. Ernst).
[https://doi.org/10.1016/j.apenergy.2024.123574](https://doi.org/10.1016/j.apenergy.2024.123574) Received 11 December 2023; Received in revised form 9 May 2024; Accepted 25 May 2024 Available online 31 May 2024 0306-2619/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)).

*M. Ernst et al. $SSOLHG Energy 369 (2024) 123574* energy production. Contrary to earlier projections, real-world applica tions often achieve performance gains of less than 10%, which is closer to the lower end of the projected range of 5% to 30% [1–5]. This per formance advantage has nonetheless made bifacial systems the domi nant choice for utility-scale PV installations in many countries, reflecting their proven value in maximising energy yield. Setting real istic expectations for bifacial gain is important, as factors such as the level and uniformity of rear illumination can impact performance. It is important to clarify that past overestimation of bifacial technology's benefits should be rectified to prevent further confusion within the industry. To optimize the design and accurately assess the economic viability of bifacial PV installations, it is necessary to model rear-side irradiance on photovoltaic modules precisely. However, the unique characteristics of bifacial systems pose several challenges in this regard. Critical limi tations include the need to account for factors such as elevation, ground albedo, shading conditions, and other rear-side-related variables. Ac curate models that encompass these complexities are essential for pre cisely calculating the energy yield and optimizing the system performance. A substantial body of research has been dedicated to addressing the complexities of bifacial irradiance modelling. These investigations aim to unravel the many optical effects influencing bifacial PV system per formance. Two predominant methods have evolved for modelling the illumination of PV modules: View-Factor (VF) methods [1,6–14] and Ray Tracing (RT) [2,3,5,15–18]. VF methods are integral components of well-established solar-energy yield modelling software such as PVSyst [19]. VF methods are usually very fast, initially capturing a limited scope of optical effects inherent in PV systems. However, to improve simulation accuracy while maintain ing computational efficiency, VF methods can incorporate correction factors for complex optical effects, such as structure shading, trans mission of light between and through modules, and losses due to elec trical mismatch. This integration of correction factors, particularly when determined through RT methods [18,20–23], significantly improves the accuracy of energy yield simulations. In contrast, RT is a more compu tationally expensive tool to model the complex optical and geometric properties of photovoltaic systems. This can include for example the detailed system mounting components, non-isotropic reflection and transmission, and spectral effects in utility-scale PV systems [3,5,16,18] and complex rooftop scenarios [24]. This paper references VF model outcomes based on a standard VF model without applying correction factors, enabling a clear comparison with a full RT model. Previous research has analysed the comparative features of VF models and RT models, as well as experimental irradiance on bifacial systems [4,11,17,20–22,25–32]. Grommes et al. compared RT and VF models for bifacial irradiance and energy yield calculations [17]. Their work emphasized the impor tance of considering a multitude of influencing factors, including the elevation angle, ground albedo, and shading conditions between PV rows. Critically, however, they note that their study does not consider shading effects from mounting system or module frames, or the gap between cells or modules. They compared the performance of front and rear irradiance calculations of a VF and a RT model against data from actual plants in Golden, Colorado, USA (single-axis tracked) and Lower Saxony, Germany (fixed-tilt), and concluded that a combination of RT modelling for rear irradiance and VF modelling for front irradiance appears valid for longer simulation periods with several months. They noted a slight overestimation in the RT-only simulations, which they explain with the omission of shading effects in their study. They conclude that RT simulations provide a more accurate representation of the actual irradiance measurements and closely align with real-world data. Zhao et al. developed models using Rhino (a 3D rendering software) and DIVA (a 3D rendering ray-tracing model), allowing for system-level ray-tracing simulations that included nearby shade obstructions from
photovoltaic racking structures, but excluded module frames [18]. Their simulated irradiance profiles were coupled with cell-level current- voltage curve modelling to provide insights into mismatch losses from non-uniform illumination for different racking configurations. Their work focused on horizontal single-axis trackers (HSAT) and fixed rack ing bifacial systems, including common module portrait and landscape configurations. They also analysed the effect of distance of the module above the torque tube, providing essential guidance for optimizing such mounting systems and accurate parameters required in PVsyst modelling. Berrian et al. emphasized the importance of modelling the backside irradiance of bifacial PV systems with high accuracy for reliable energy- yield predictions [26]. They compared the accuracy of two optical models: the VF concept and RT. They equipped a monocrystalline silicon solar panel with sensors to measure rear irradiance performance along the rows of the PV module during sunny and cloudy days. They found that both hourly RT and VF approaches could model long-term cumu lative irradiance received by solar cells with high accuracy, ranging from ±0.5% to ±2%. Additionally, Kang et al. highlighted discrepancies in yield pre dictions between view factor and ray tracing methods [27]. Despite these advancements, challenges persist, particularly in accurately esti mating the rear irradiance directly with VF models. In practice, VF correction factors are often determined using RT models [18,20–23] to overcome these limitations. Previous research has identified limitations in VF modelling, espe cially regarding the accurate modelling of rear irradiance. However, a notable gap in the literature is the lack of comprehensive comparisons that consider a wide range of optical factors within the RT model; as well as an estimation of the energy yield difference obtained when including electrical modelling considerations. This study addresses this gap and identifies the specific factor(s) that significantly contribute to the limitations observed in VF modelling. Thereby we improve the accuracy of modelling bifacial PV systems. For this purpose, validated VF and RT models by Jager ¨ et al. [13] and Ernst et al. [5], respectively, are used. The VF model was validated against measured short-circuit current for mono- and bifacial solar modules at one partly cloudy and two sunny days [33]. The RT model was validated against measured front and rear plane-of-array (POA) irradiance values from the National Renewable Energy Laboratory (NREL) Bifacial Experimental Single-Axis Tracking dataset [34], consisting of a total of 5326 datapoints after filtering, spanning a period of 14 months from October 2019 to December 2020 and measured albedo values ranging from 0.13 to 1.0. Both models are evaluated against the NREL dataset in this work. The methodology systematically introduces additional components and features into the RT simulations to evaluate their influence on prediction accuracy, consequently providing a nuanced understanding of the intricate relationship between system complexity and modelling precision. This approach facilitates the identification of critical factors affecting VF model limitations of real systems and furthers our comprehension of the interplay between structural components and bifacial PV system performance. Finally, we propose an answer the key question: How is the energy yield affected by the choice of optical model in the context of utility-scale PV systems?

**2. Model development and evaluation**
*2.1. Model complexity variation* The VF and RT models are described in the Methods section. Fig. 1a illustrates the VF model and Figs. 1b-d show the RT model at different levels of complexity. In this section, we delve into the systematic exploration of RT model complexity for bifacial solar irradiance modelling. The aim of this investigation is to compare RT results against the VF approach. Starting

**Fig. 1.** (a) Schematic illustration of the illumination with the VF model, which reach the module on the front and back sides at point P of a central module. (b)-(d)

Illustrations of RT scenes depicting increasing modelling complexity: (b) Step 1 – Single module unit cell, (c) Step 7 – Optical properties, module frame and torque tube added, (d) Step 9 – Six-module unit with mounting components. The grey walls represent the unit-boundary conditions.

with near-identical models utilizing both techniques, the RT model is progressively altered with additional features and components to assess their impact on the irradiance predictions. Table 1 outlines the 9 sequential steps of the RT modelling approach, progressively increasing in complexity as additional factors are incorporated into the simulation, including front and rear reflections, module frame, torque tube, spacing between modules, and mounting posts. Fig. 2 illustrates the key geo metric parameters of two adjacent solar modules, and Table 2 lists the key geometric parameters of the solar modules.

*2.2. Model evaluation* This section serves to evaluate the detailed RT and VF models in this work against irradiance measurements from the NREL Bifacial Experi mental Single-Axis Tracking dataset [34]. The NREL dataset is meticu lously filtered following the BSRN Global Network's recommended guidelines, version 2.0, resulting in a dataset comprising 5326 data points, spanning a period of 14 months from October 2019 to December
2020. The NREL system, shown in Fig. 4, is equipped with five plane-of- array (POA) silicon solar cell pyranometers, including one front-facing and four rear-facing sensors, located between two solar modules within a large solar array. Additionally, the dataset includes measure ments of ground albedo data captured at the solar PV site, as well as direct normal irradiance (DNI) and global horizontal irradiance (GHI) measurements taken from a solar irradiance station located approxi mately 100 m away from the solar array. To model the irradiance measurements, we replicate the irradiance sensors for the RT model Step 9 as illustrated in Fig. 5. Due to their position along the length of the module, we anticipate minimal impact on the rear sensors by the torque tube. The VF model does not distin guish between module and sensor irradiance. Instead, we evaluate the sensor irradiance directly from the simulation results for cell rows 1, 4, 9, 12 which are equivalent to the approximate sensor positions along the module length.
Figs. S1 and S2 in the Supplementary Materials compare the measured and modelled front and rear irradiance for both the VF and RT models. Table 3 presents the resulting error metrics (see Method Section

5.3) comparing the RT and VF models to the measured front and rear irradiance values. The rear irradiance values represent the average of all four rear-facing measurements and their corresponding simulated values. In the context of estimating bifacial irradiance, the relative Root Mean Square Error (rRMSE) for front irradiance is found to be closely aligned between the VF or RT methodologies, with values approximately 7–8%. Specifically, the RT model shows an rRMSE of 7.6%, while the VF model exhibits an rRMSE of 7.2%. For rear irradiance, the difference remains minimal, with the RT method recording an rRMSE of 22.9%, compared to the VF method at 20.9%. The relative Mean Bias Error (rMBE) for front illumination also aligns between the two methodolo gies, with values of 1.8% and 2.0% for the VF and RT methodologies, respectively. In contrast, rear irradiance shows a rMBE of 0.1% when estimated by RT and an 8.4% underestimation when determined by the VF model. It is important to note that the irradiance received at the rear of the module is approximately 11% of that at the front. Therefore, any dis crepancies between simulated and experimental energy yield would be primarily due to inaccuracies in the front irradiance estimation. One plausible explanation for the observed rRMSE and rMBE values could be the spatial separation between the solar irradiance station, which sup plies the DNI and GHI inputs to model POA irradiance values, and the PV site providing the measured POA values, as well as experimental error in GHI, DNI and POA values. Additional error could stem from spectral and nonlinear effects not considered in the model.
**3. Comparative analysis of VF and RT solar irradiance models**
*3.1. Performance evaluation across tracker scenarios* This section compares the average front and rear module irradiance

transmission curves with without Incident Angle of incidence angle. The and incidence angle is measured ◦at normal incidence and 90◦for relatively to the module surface and is 0

Geometric and optical parameters of the simulated modules and system.

**Table 1**

RT Simulation steps and associated model complexities. Each step represents an increase in model complexity, with additional components or conditions intro duced to refine the simulation. Step Description Details The initial RT model replicates a single-module Single-module unit cell unit frames cell or without mounting structural structures. components Both front like and model rear reflections omitted. This minimalistic RT 1 model serves as are a baseline for comparison against Near identical to the VF the VF method, which also disregards structural model components and front/rear reflections. The simulation scene is illustrated in Fig. 1a. A 2.4% *isotropic* front reflection is introduced to Incorporating front the RT model, allowing assessment of the effect of 2 reflection module front reflection on irradiance. This simple modification gauges the significance of front surface reflectivity. After introducing front reflection, a 10% *isotropic* 3 Adding rear reflection rear enables reflection analysis is added of the to role the of RT rear model. irradiance This step in bifacial systems. Front reflection is assumed *specular* following the Incident Angle Modifier (IAM) in this step, as 4 Specular reflection front with IAM illustrated more accurate in Fig. representation

3. This modification of how incident
provides a

angles impact the reflection of light from the module's front surface. Similarly, the rear reflection is adjusted to follow 5 Specular with IAM rear reflection the realistic *specular* assessment IAM. This of addition how rear enables irradiance a more is influenced by incident angles. A module frame is introduced to the RT model, Introduction of module representing a more complex structural 6 frame configuration. This step helps understand the impact of framing on both front and rear irradiance. The introduction of a torque tube enhances RT Incorporating torque model complexity, accounting for shading and 7 tube irradiance alterations caused by the tracking system. The simulation scene is illustrated in

Fig. 1b.

The model is scaled up to a six-module unit cell Scaling to multiple configuration, maintaining the complexity 8 modules introduced in Step 7. An additional gap is added between the modules at the centre of the array to allow for introduction mounting posts in step 9. Mounting posts are introduced in the centre Including mounting between the array, addressing the influence of 9 posts additional structural components on irradiance distribution. The simulation scene is illustrated in

Fig. 1c.

**Fig.** Modifier

**3.** Module (IAM) as glass function
incidence parallel to the surface.

**Table 2**

Parameter Cell length and width Number cell columns Number cell rows Cell-to-cell gap Perimeter left/right Perimeter top/bottom Frame height Frame width Front-side frame lip Bracket width left/right Bracket width top/bottom Frame/Bracket optical properties Torque tube

Value 156 mm 6 12 2 mm 7 mm 14 mm 30 mm 5 mm 2 mm 25 mm 10 mm Reflectivity *R* = 0.7 Specularity = 0.5 Circular, diameter 12 cm Distance to panel rear: 8 cm Elevation (center of tube): 1.5 m Reflectivity *R* = 0.7 Specularity = 0.0 Square, edge length 9 cm Reflectivity *R* = 0.7 Specularity = 0.0 Located in the center of the 6-module unit-system 3 cm At post: 20 cm

**Fig. 2.** Illustration of geometric parameters of two adjacent modules. The

nomenclature and design of this illustration were inspired by SunSolve [35].

of the VF and RT models. The average irradiance values are computed from 72 cell-level values in the RT model and 12 row-level values in the VF model. To comprehensively evaluate the performance of the RT model in comparison to the VF method, a series of simulations were conducted across six distinct tracker scenarios. Each scenario involved an assumed

Mounting posts

Spacing between modules

**Fig. 4.**

the North.

A satellite image illustrating the layout of the NREL single-axis tracking system. This system comprises ten tracker rows of 20 solar modules each. The sensor array, consisting of five Si solar cell pyranometers, is positioned in the third row from West, nestled between the fourth and fifth solar modules from

**Fig. 5.** Schematic representation of the sensor placement in the RT model Step 9. The sensor locations, both front and rear-facing, are positioned to mimic real-world

conditions. Their arrangement along the length of the module ensures minimal interference from shading effects caused by the module frame, aligning closely with the physical setup observed in the actual system.

**Table 3**

Error values of front/rear POA irradiance for RT and VF models against 5326 measured data points over the period October 2019 to December 2020. *O* is the mean of the measured values. Front POA irradiance Rear POA irradiance RT VF RT VF *R* 20.96 0.97 0.88 0.90 rMBE 1.8% 2.0% 0.1% 8.4% rRMSE 7.6% 7.2% 22.9% 20.9% *O* 657.1 W/m 272.2 W/m2

incident irradiance of 1000 W/m 2, both for separate direct and diffuse irradiance simulations. The six scenarios cover tracking angle configurations ranging from 58◦to 54◦and assume a constant ground albedo of 26%, which is the yearly average from three albedometers on the site [34]. Details on the parameters for the six scenarios are given in Table 4. The single-module unit cell RT model (Step 1, Fig. 1a), configured to represent a unit cell, was meticulously designed to replicate the VF model, albeit with the capacity to account for multiple reflections. However, it is important to note that due to the absence of reflective surfaces other than the ground, these additional reflections did not lead to any increase in front or rear irradiance.

Fig. 6 shows the comparison of the front and rear irradiance of the RT

unit cell simulation (Step 1) versus the VF model, for both direct and diffuse irradiance components for all six scenarios. Excellent agreement between the simple RT simulation and the VF model is observed to the point that the respective data points are hardly distinguishable. This meets the expected outcomes as both models considered the same op tical effects and provides a reliable baseline for the remaining analysis.

*3.2. Impact of model complexity on module irradiance* To compare the increasing complexity of the RT model with the VF model, the average front and rear irradiance values over the entire module surface and across the six tracking scenarios are normalized to the results of the RT unit cell simulation (Step 1). This normalization
**Table 4**
 Description of six tracking scenarios for comparative analysis of VF and RT models. The VF and RT models are described in the Methods section. Scenario Tracking angle (◦) Zenith (◦) Azimuth (◦)
58.4 70.1 216.0
37.1 65.6 200.0
3.9 30.8 186.6
0.0 28.9 180.0
22.2 49.3 159.5
54.1 54.3 96.2
establishes a reference point by defining the irradiance values obtained from Step 1 of the RT model as the benchmark.

Fig. 7 compares the nine RT simulations against the VF model results.

A small increase of average rear irradiance is observed with the addition of diffuse module reflectivity. However, when considering a more realistic scenario with specular glass reflection and IAM, the rear irra diance increase due to module front reflection vanishes for direct light (blue line). The reason for this is that the modules are installed in a single-axis tracking system, which means that direct light that is spec ularly reflected off the front of the module is less likely to reach the rear of an adjacent row of modules. In contrast, increasing the module number, and thus allowing additional light to pass to the ground in the gaps between the modules, yields the highest positive impact on rear irradiance. The incorporation of structural components leads to a significant reduction in rear irradiance. Among the structural components consid ered, the module frames and torque tubes have the most significant impact on rear irradiance. Both effects combined reduce the rear irra diance by over 10% with respect to the reference simulation, which is only partly offset by the increased rear illumination from the added module spacing. Furthermore, these structural elements cause local shading patterns on the module rear and thus cause cell current mismatch issues, a phenomenon that has been detailed in Refs. [16, 36–40]. The results show a significant overestimation of the average module rear irradiance of the VF model (dashed lines) compared to the detailed RT model (“+ Post”, Step 9) results (solid lines). The overestimation from the average of the six scenarios is 6.9% for direct light, and 11.8% for diffuse light. As expected, the average front irradiance is relatively independent of model complexity for both the RT and VF models. We note a small in crease of 0.24% in diffuse front irradiance for the RT model, due to the introduction of additional reflective surfaces, namely the torque tube, additional modules, and mounting posts. The results in Fig. 7 consider the average irradiance across all 72- cells of the module. However, as noted above, module irradiance is not uniform, which can cause current mismatch between cells and thus reduce module power [16,36–40].

Fig. 8 provides a comparative analysis of the distribution of rear

irradiance received by the individual cells for scenario 3 (see Table 4) under direct irradiance. The VF results are shown on the far left, fol lowed by the results obtained from the RT model at various stages of complexity (Step 1, 7, and 9) from left to right. This arrangement allows for a clear examination of the influence of the model sophistication on irradiance distribution. It is worth noting that the VF model utilized in this study operates within the constraints of 2D simulations, thus omitting consideration of cell columns in the *x*-direction. However, it should be noted that this limitation is not inherent to VF models at large. More complex VF models, as demonstrated in studies such as [11,41],

**Fig. 6.** Comparison of front (left) and rear (right) irradiance, modelled by VF (dashed blue lines) and RT unit cell simulations (solid red lines) across six scenarios.

2 of direct normal or diffuse horizontal Direct irradiance is represented by triangles, while diffuse irradiance is indicated by circles. All scenarios assume 1000 W/m irradiance. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

**Fig. 7.** Normalized average front (left) and rear (right) module irradiance for VF (dashed lines) and RT simulations (solid lines), considering both direct (blue) and

diffuse (red) irradiance components. Averages are calculated over the entire module surface and across six tracking scenarios. Dashed lines facilitate comparison of the VF model with RT at increasing levels of complexity. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

are capable of determining cell-level irradiance. In the studied illumination scenario, a reduction in irradiance toward the centre of the module is evident. With the introduction of module frames and torque tubes in RT Step 7, we can observe a further decrease in irradiance. The shading effects caused by the module frames are strongly affecting the left and right cell columns. Additionally, the central four cell rows experience additional shading stemming from the torque tube of the modules mounted in portrait orientation. These findings are supported and complemented by similar irradiance maps created in other studies, for example, those documented in references [16, 29].

Fig. 9 compares the rear direct and diffuse irradiance of each row of

cells of the VF model against different RT model complexity at the same time step as Fig. 8. We find a very good agreement between the VF and RT unit cell (Step 1), with small deviations observed for direct irradi ance. This difference likely stems from differences in the segmentation of the module. While the VF module uses equally sized segments along the whole module lengths, the RT model considers spacing to the module edges and between cells. We observe a strong impact on irradiance inhomogeneity when

introducing module frame and other structural components in the RT model. The module frame causes shading of the outer cells, while the torque tube causes shading at the centre of the module.

Fig. 10 shows the rear irradiance of the six columns of cells along the

width of the module. As the VF model does not consider this dimension, it is constant along this axis. This behaviour can be replicated with the simplest RT model. However, when introducing module frame, the rear irradiance of the edge cells is reduced noticeably.

*3.3. Comparison of module irradiance on a larger dataset* The previous sections have analysed the impact of modelling complexity on the module rear irradiance in six selected tracking sce narios. This section compares the module irradiance over a larger dataset, the NREL dataset introduced in Section 2.2 with 5326 data points, spanning a period of 14 months from October 2019 to December
2020. The impact of module frame and structural components on cell-level module rear irradiance and its average value is significant, as shown in Figs. 7, 8, and 9. Figs. 9 and 10 demonstrate that the VF model

**Fig. 8.** Comparison of relative rear irradiance distribution among individual solar cells within a nearly horizontal module (tracker angle: 4◦). The figure presents

results from VF simulations on the far left, followed by RT simulations at Step 1, 7, and 9, progressing from left to right, showcasing the influence of model complexity on irradiance distribution.

**Fig. 9.** Rear irradiance distribution for 12 cell rows averaged across cell columns for scenario 3 for direct and diffuse irradiance simulations. The figure shows results

from VF simulations (green circles) and RT simulations at Step 1, 7, and 9, (orange triangles, blue squares, and purple diamonds). The impact of module frame and torque tube on rear irradiance is clearly visible. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

**Fig. 10.** Rear irradiance distribution for six cell columns averaged across cell rows for scenario 3 for direct and diffuse irradiance simulations. VF simulations (green

circles) and RT simulations at Step 1, 7, and 9 (orange triangles, blue squares, and purple diamonds) illustrate the impact of model complexity and the impact of module frames on the outer cell columns are clearly visible. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

consistently overestimates irradiance values for the module rear. Correction factors are necessary to adjust for effect such as shading from module frames and mounting components. In practice, VF models use correction factors determined by RT to mitigate these discrepancies [18,20–23].

Fig. 11 presents the difference between the VF model results and the

RT model Step 9 results for the average module rear irradiance. It is clear that the VF model overestimates the rear irradiance at the module, and this overestimation increases as the albedo increases.

Fig. 12 compares the average module irradiance integrated over the

entire dataset. The values are normalized against the results obtained from the most intricate unit-system of the RT model (Step 9), which considers six modules and includes module frames and mounting com ponents. A positive value on this chart indicates higher total irradiance compared to the rear irradiance of the reference model. For example, the purple bar for the VF rear is a sum of all *y*-values (VF) of the data shown in Fig. 11 divided by the sum of all *x*-values (RT 9). As expected, the simulated front irradiance closely matches the measured sensor irradiance, with only a 2% deviation. The modelling results for the front irradiance are consistent across different RT model complexities and the VF model, as the front irradiance is minimally impacted by component shading effects. In contrast, for the rear side, both the simple RT (RT 1) and VF models significantly overestimate the average irradiance at the module rear side by nearly 7% when compared against the most detailed RT model (RT 9). This overestimation is due to the fact that shading effects caused by module frames and structural components are not taken into account. Furthermore, we compare the measured and modelled POA sensor values. The average irradiance received by the four rear POA sensors is more than 16% higher than the average irradiance at the module rear. It is worth noting that the sensor values can be accurately replicated with the RT model, as explained in Section 2.2. The difference between POA sensor and module rear irradiance can be mainly attributed to the fact that the sensor irradiance is not significantly influenced by shading ef fects from the torque tube or the module frame. Therefore, such sensor measurements may not be an ideal indicator of bifacial gain from the rear side.

*3.4. Implications of modelling detail on energy yield* Previous sections of this paper have explored the influence of
**Fig. 12.** Relative module irradiance across various model complexities, illus

trating the impact of model intricacy on total irradiance outcomes. Higher values indicate increased total irradiance compared to the reference model at Step 9.

modelling detail on the average irradiance of bifacial solar modules. This section evaluates the direct effect of modelling detail on energy yield by incorporating the impact of cell-level irradiance non-uniformity due to structural components. The energy yield modelling as previously detailed in Ref. [42], en compasses four essential steps, as illustrated in Fig. 13: *Step 1: Optical Modelling* In the first step, optical modelling is performed using both the VF model and the comprehensive RT model (Step 9) applied to the filtered NREL irradiance and weather dataset. Separate energy yield simulations are conducted for front illumination and the combined front and rear illumination scenarios. *Step 2: Thermal modelling* Subsequently, the results obtained from the optical model are inte grated into thermal and electrical models. The estimation of cell tem perature *TC*is achieved by applying an adapted Faiman model [43] for modelling the temperature of bifacial modules, as specified by Eq. (1): () *α* front× *E*front× (1 *η*cell) + *α*rear× *E*rear× 1 *η*cell*f*bifacial *T* *C*= *Ta*+ *U* + *U* × *WS* *c v*

(1)
In this equation, *Ta*represents the ambient temperature (◦C), *E*front and *E*rearstand for the front and rear plane-of-array irradiance (W/m 2 ), *α* frontand *α*rearare the front and rear absorption coefficients, *η*celldenotes the cell efficiency, *f*bifacialis the bifacial factor of the module efficiency, *WS* represents wind speed (m/s), *Uc*is the combined heat loss coefficient () *W/m*2, and *Uv*is the combined heat loss factor influenced by wind *K* () *W/m*2. *K* (*m/s*) *Step 3: Electrical Modelling* In the third step of our analysis, we compute the electrical power output of the PV system for each discrete time step. This computation is crucial as it integrates cell-level irradiance and module-level tempera ture inputs, utilizing the capabilities of the PVMismatch model [44], which is a sophisticated IV curve calculator developed in Python. PVMismatch uses a two-diode cell model to predict the IV behaviour of modules and systems. It accounts for variations in irradiance and tem perature, as well as the effects of shade and electrical mismatch, and the implications of module layout on performance. The methodology builds upon the RT model to simulate the electrical output for a unit system comprising six solar modules. The RT model

**Fig. 11.** Difference of modelled module rear irradiance between VF and RT

Step 9 models, highlighting VF's tendency for overestimation increasing with ground albedo.

Flow-chart of the four key steps involved in the energy yield model.

**Fig. 13.**

considers the cell-level irradiance for each of these six solar modules. Given that the electrical model operates at the granularity of individual cells, we adopt an assumption when using the VF model. The VF model, which provides values along the length of the module (i.e., 12 module rows), assumes identical irradiance values across all six cell columns. Furthermore, the VF model does not differentiate between individual modules, so we assume uniform illumination for all modules in the VF case simulations. The characteristics of the PV module used for yield estimation are outlined in Table 2, which includes optical and geometric specifications, and Table 5, which lists the electrical inputs for the diode cell model employed by PVMismatch. The module's bifaciality factor is determined solely by the optical model, as we assume that the cells have unity collection efficiency on both sides. Table 6 presents the electrical char acteristics of the bifacial module under standard test conditions (STC), using inputs from the RT 9 model and considering cell-level irradiance values for PVMismatch. The electrical model takes the irradiance on each individual cell as an input. The irradiance values of the individual cells are adjusted to consider the increased total irradiance due to the irradiation on the back of the module. In addition to this, energy yield simulations are per formed using average cell irradiance values at each time step. This approach allows us to isolate and analyse the effects of non-uniform illumination. *Step 4: Integration* Finally, the electrical power output of the system is integrated over the entire 14-month period of the dataset, spanning from October 2019 to December 2020. In contrast to the analytic approach of the VF model, RT is a statis tical approach and as such is affected by random statistical errors, as described in the Methods section. Therefore, we vary the random simulation error, *CI*(*IN*), with a 95% confidence level as defined in Eq.

(2) in the range from 0.1% to 30%, observing the maximum *CI*(*IN*) for all individual solar cells in the system.
Fig. 14 presents the outcomes of energy yield simulations as function
 of the RT simulation error for the most detailed RT model (Step 9) for the full NREL dataset (5326 timesteps). Analysing the energy yield results at the cell level, we observe that the energy yield attains a saturation point when the RT simulation error is below 3%. We note a difference in
**Table 6**

Resulting front and rear module characteristics modelled under STC conditions with RT 9. Parameter Front Rear *P* mpp406.3 W 316.4 W *V* mpp42.6 V 44.4 V *IV* mpp9.5

49.6 A V 7.1
49.2 A V
OC *I* SC10.0 A 8.5 A *η* 21.7% 16.9% *f* bifacial77.9%

energy yield comparing cell-level yield simulations with those employ ing module-level average irradiance values. The cell-level yield results are approximate 0.2% lower than the module-level yield results in the context of front illumination – both for VF and RT model results. This difference is due to the impact of non-uniform illumination effects in the electrical cell interconnection, which remains unaccounted for in the averaged results. The VF model yields results similar to the RT model when consid ering front illumination only. For bifacial irradiance, we observe a 0.8% overestimation of the energy yield when considering cell irradiance values for 12 cell rows. These discrepancies, specifically the 0.2% (RT) and 0.8% (VF) losses, are attributed to electrical mismatch. This is consistent with findings reported in other works [16,36–40].

Table 7 offers a comparison of integrated irradiance values averaged

over all individual solar cells in the system, providing insights into the contributions of the VF and RT models to the bifacial PV panel system. Notably, the total rear irradiance contribution is approximately 10% when assessed using both modelling approaches. However, what stands out is that the VF model yields a 5.8% higher average rear module irradiance compared to the RT model, which is mainly due to neglecting detailed shading effects from components as we have identified in the previous sections.

Fig. 15 and Table 8 compare the integrated energy yield estimates of

the VF and RT models by using cell-level and module-average irradiance data. The RT simulations are performed at 1% simulation error. For the cell-level results, it is observed that the VF model generates bifacial energy yield 0.8% higher than that obtained by using the RT model. The discrepancy arises mainly due to the difference in rear contribution, whereas almost identical yield is obtained under front illumination. The yield analysis reveals that the overestimation at the rear side is 10.8%, which is nearly two times greater than expected from analysing the overestimation in module irradiance averages alone (refer to Table 7). Alternatively, it is significantly higher than the results observed at the module level energy yield (refer to Table 8). These results highlight the necessity of carrying out thorough

**Table 5**

Diode cell modelling model parameters inputs to PVMismatch in the electrical of bifacial used solar as modules. Parameter Value Series resistance *R*s0.34 Ω cm Shunt resistance *R*sh20 kΩ cm Recombination parameter *J* fA cm Ideality factor *n* 1.04

**Fig. 14.** Energy yield as function of RT simulation error considering individual cell irradiance values (red) and module average irradiance values (blue), for bifacial

and front illumination. The results for the VF model are included as dashed line and are not subject to statistical simulation error. The computation times and number of rays required are detailed in Figs. S3 and S4 from the supplementary information. (For interpretation of the references to colour in this figure legend, the reader is

**4. Conclusions** In this study, we conducted a comprehensive comparative analysis of View-Factor and Ray Tracing models, both in purely numerical experi ments and applied to an instrumented single axis tracking PV installa tion based at NREL in Colorado (USA). This comparison was conducted to assess the performance of both modelling strategies in predicting rear irradiance in bifacial photovoltaic systems. Our investigation yielded
referred to the web version of this article.)

**Table 7**

Integrated irradiance for the module averaged over all cells. Model Front (kWh/m²) Rear (kWh/m²) Total (kWh/m²) Bifacial gain RT 9 856.2 82.5 938.8 9.6% VF 857.9 88.1 945.9 10.3% rMBE 0.2% 6.7% 0.8% rRMSE 1.2% 10.4% 1.5%

evaluations of energy output, emphasising that slight disparities in model precision can result in considerable variances. Therefore, it is crucial to employ accurate modelling methods when assessing energy yield in utility-scale PV systems. It is also essential to note that a rMBE of 0.8% in energy yield be tween the RT and VF models should not be dismissed as inconsequential, given its potential impact on utility-scale PV systems. The estimation of energy yield plays a crucial role in determining the economic feasibility and performance of utility-scale PV systems. Over- or underestimation can cause financial miscalculations, leading to excessive investments in hardware, land, and infrastructure. Moreover, this can result in overly optimistic revenue forecasts and ultimately impact the return on in vestment and project profitability.

**Table 8**

Energy yield computed using cell-level and module-level irradiance values for RT and VF models, and corresponding rMBE and rRMSE. Detail Model Front Rear contribution Total Bifacial (kWh) (Total – Front) (kWh) (kWh) gain Cell-level RT 9 8268.1 701.9 8970.0 7.8% VF 8262.1 777.4 9039.5 8.6% rMBE rRMSE 0.3%

0.1% 10.8%
18.1%
0.8%
1.4%
Module-RT 9 8277.7 725.6 9003.6 8.1% level VF 8268.4 784.2 9052.6 8.7% rMBE 0.1% 8.1% 0.5% rRMSE 0.3% 12.7% 1.0%

web version of this article.)

**Fig. 15.** Energy yield as function of RT modelling detail for cell-level irradiance values (red) and module average irradiance values (blue), for bifacial and front

illumination. The results for the VF model are shown as dashed lines. (For interpretation of the references to colour in this figure legend, the reader is referred to the

several key findings:

- Both VF and RT models show a similar correlation to measure front POA irradiance. The rRMSE and rMBE are approximately 7–8% and 2%, respectively, regardless of whether the VF or RT methodolo gies are used.
- In contrast, rear irradiance shows a rMBE of 0.1% when estimated by RT and an 8.4% underestimation when determined by the VF model. Through detailed comparative analysis, we identified unac counted optical reflections at module surfaces and light passing through gaps between modules as the primary reasons for the un derestimation of sensor rear irradiance by our VF model.
- The modelling shows significant differences between the simulated sensor results and the rear irradiance results of the module. These differences are due to the additional impact of shading caused by the module frame and structure. This leads to the VF model over estimating module rear irradiance by 6.7%. This finding bears po tential implications for models utilizing measured rear illumination values.
- Discrepancies in irradiance modelling approaches translate into a notable overestimation of the energy yield when employing the VF model. Specifically, the VF model yields an estimate that exceeds that of the RT model by 0.8%. The discernible difference between module and sensor rear irradi
ance and resulting energy yield difference underscores the critical sig nificance of incorporating structural elements into the modelling of bifacial PV systems. This study has identified module frames and mounting components as the key elements affecting the module rear irradiance, and thus leading cause for discrepancies in the VF model. In conclusion, our comparative analysis provides insights into the capabilities and limitations of VF and RT models in simulating bifacial PV systems performance. While both models offer reasonable correla tions and RMSE values, the tendency of the VF model to overestimate module rear irradiance and energy yield highlights the need for caution when utilizing this approach, especially in systems with complex structural configurations.

**5. Methods**
*5.1. View Factor (VF) model* The view-factor model used in this study utilizes 2D calculations for very fast evaluation of front and backside illumination for large PV ar rays. This is implemented by assuming an infinitely large PV array such that edge effects can be neglected. No mounting structures are consid ered, and the modules are assumed to be perfectly flat and are perfect light absorbers on the front and back side. The sunlight in this study is assumed as AM1.5 g spectrum for both direct and diffuse light, and additional the diffuse component is considered to be isotropically distributed over the hemisphere while direct sunlight is modelled as a point source. The ground is treated as a Lambertian reflector. The irra diance on the module consists of four components: direct sunlight, diffuse skylight, diffuse light reflected from the ground originating from direct sunlight and diffuse light reflected from the ground originating from diffuse skylight. The details of the models are described in Ref. [13].
*5.2. Monte Carlo Ray Tracing (RT) model* In this research, an energy partitioning forward RT approach is uti lized to conduct optical simulations for bifacial irradiance modelling. Within this RT framework, rays are initiated from the aperture plane of the scene and meticulously tracked until they exit the system. At each interaction point, the model records the absorbed energy. A compre hensive description of the RT model, including the time-resolved
simulation methodology, can be found in Ref. [5]. The RT model employed in this study distinguishes between direct and diffuse light components, processing them independently. The re sults are subsequently combined, taking into account the measured direct and diffuse irradiance values at each time step. The representation of the diffuse sky employs an isotropic distribution. Objects within the simulation scene are defined by geometric prim itives, and an optical manager is responsible for calculating locally absorbed energy as well as randomly generating reflection and trans mission directions. The object-oriented RT modelling framework used in this research is versatile allowing for considering different components and optical effects. To account for increased complexity in the simulations, additional elements are progressively incorporated into the scene. At the core of this approach is a dedicated PV module model, which comprehensively considers light interactions at all module layers, including module frames. The modular approach also provides the flexibility to modify individual components and their optical properties, such as front and rear reflection properties. Within the RT framework, this PV module model is seamlessly in tegrated into a single-axis tracking system model, encompassing not only PV modules but also components such as the rotating torque tube and mounting posts. Representation of individual solar cells adopts a simplified bi-dimensional rectangular sheet, incorporating specific masking functions to address inter-cell gaps. To capture the unique optical behaviours associated with photovoltaic cells, custom optical managers are employed, accounting for factors like texturing and other cell engineering-related optical effects. This approach efficiently sim plifies the ray-tracing problem by avoiding the need for a multitude of surfaces to represent each module. Similar to the VF model used in this research, the RT simulations assume AM1.5 g spectra for both direct and diffuse light. This enables a more direct comparison with the VF model. It is important to note that the RT model also accommodates spectral resolution of optical proper ties and irradiance if required. Within the RT model, detailed records are maintained of the absorbed irradiance on both the front and rear sides of each individual solar cell within every solar module in the system, providing comprehensive insights into energy absorption and losses at the microscale level. RT serves as a stochastic simulation technique wherein intricate in teractions are approximated through the generation and propagation of randomly distributed light rays. As is customary with stochastic meth odologies, RT inherently yields outputs with statistical variance. Expanding the number of samples (i.e., the quantity of rays) diminishes the range of this stochastic uncertainty. In our investigation, the irra diance detected at each sensor or solar cell exhibits such stochastic fluctuations. The RT model quantifies this random simulation error, *CI*(*IN*), with a 95% confidence level as defined in Eq. (2). *σ* N *CI*(*IN*) = *t* * (*N* 1) √̅̅̅̅̅̅̅̅̅̅̅̅ (2) *N* 1 Where *IN*represents the mean value, defined by Eq. (3), and *σ*Nsig nifies the standard deviation defined by Eq. (4). ∑ *N* *I* *N*= 1 *Ii*(3) *N* *i*=1 √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ √ √*N* *σ* N= √1 ∑(*I* *iIN*) (4) *N* *i*=1

*t* * (*N* 1) corresponds to the two-tail t-distribution critical value for a 95% significance level, with *t**(∞) = 1*.*96, as referenced in [45]. It is important to note that the number of simulations, *N*, must exceed 1. Here, *IN*refers to a sequence of *N* independent simulations.

*5.3. Error metrics* Three error metrics are used to assess model performance compared to the measured irradiance values: relative Root Mean Square Error (rRMSE), relative Mean Bias Error (rMBE), and the Coefficient of Determination (*R²*): √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
*n* 1 1 ∑2 rRMSE = (*PiOi*) (5) *O ni*=1

1 ∑ *n* rMBE = (*PiOi*) (6) *nOi*=1

∑ *n* 2 (*OiPi*) *R²* = 1 *i* ∑ = *n* 1

(7)
(*OiO*) 2 *i*=1 In these equations, *Pi*is the simulated value at time step *i*, *Oi*is the measured value at time step *i*, *n* is the total number of simulations, and *O* is the mean of all measurements. rRMSE, presented as a percentage, quantifies accuracy with larger errors having a more significant impact when scaled by *O*. rMBE calculates the average error, considering bias. *R*2assesses both error magnitude and model quality. An *R*2of 1.0 in dicates a perfect match, while negative values imply no correlation between the model and observations.

*5.4. Computational demand comparison* This section compares the computational demand of the VF and RT modelling approaches for a full yield simulation of 5326 timesteps. The VF model distinguishes itself as an analytic approach, offering rapid computations suitable for assessing irradiance in large PV arrays. Its computational demands are modest, with a runtime of approximately 15 min when executed on a single CPU (12th Gen Intel Core i7-1270P). When deployed on a virtual server with a shared CPU (single core), the VF model completes its calculations in approximately 43 min, which is nearly factor three slower. The VF model performance can be improved by clustering of similar sun positions and tracking angles.
In contrast, the stochastic RT modelling approach introduces vari ability in its simulations. The computational demand of RT depends on the complexity of the system. As the model incorporates more optical effects and elements, the computational time increases proportionally. Notably, RT allows for flexibility in managing computational resources through the optimization of parameters. Our RT model utilizes an error target strategy instead of a fixed number of rays, enhancing accuracy while minimising the required number of rays for a given simulation. We further only simulate relative irradiance values and apply clustering of similar sun positions, tracking angles and ground albedo to reduce the number of ray tracing simula tions from 5326 timesteps to 1629 simulation steps, an approach we described in Ref. [5]. Clock time in RT is directly influenced by the number of parallel CPUs engaged. In this study, 256 CPUs were employed on the same compute infrastructure, utilizing virtual CPUs. The simplest RT model achieved convergence in 20 min, while the most complex scenario required 730 min. The capacity to decrease clock time by increasing the number of CPUs is a noteworthy advantage, and the use of dedicated servers is anticipated to enhance performance potentially by factor three.

Fig. 16 illustrates the increase in computational demand for the RT

energy yield simulations, for the NREL dataset used in this work. A steep increase in the clock time is observed at simulation errors below 3%. Notably, the level of model detail has a significant impact on simulation time, with an order of magnitude increase from the simplest to the most detailed model. Figs. S3 and S4 from the supplementary information provide a detailed overview of the computation times. Fig. S3 shows that the distributions of calculation times of individual simulations vary widely to achieve a constant simulation error and typically spread over one order of magnitude. Fig. S4 illustrates how a constant simulation error necessitates an increase in number of rays with increased model detail. It is essential to recognize that RT, with its stochastic foundation, offers opportunities for optimisation. Code optimisation, for example through implementing kd-trees, have the potential to yield substantial improvements, potentially achieving over an order of magnitude in performance enhancement. Notably, for systems of moderate complexity with a moderate number of CPUs, the clock times of RT are

**Fig. 16.** Total simulation time (clock time) for modelling energy yield with 256 parallel virtual CPU cores as function of RT simulation error for the nine levels of RT

modelling detail. Computation time increases with decreasing simulation error and increasing modelling detail.

comparable to those of the VF model, presenting a balanced choice between precision and computational efficiency.

**CRediT authorship contribution statement**

**Marco Ernst:** Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization. **Charles-Alexis** **Asselineau:** Writing – review & editing, Software. **Peter Tillmann:** Writing – review & editing, Software. **Klaus Jager:** ¨ Writing – review & editing. **Christiane Becker:** Writing – review & editing.

**Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Data availability**

Data will be made available on request.

**Acknowledgements**

This Project received funding from the Australian Renewable Energy Agency (ARENA) as part of ARENA's TRAC Program through project 2022/TRAC004. The views expressed herein are not necessarily the views of the Australian Government, and the Australian Government does not accept responsibility for any information or advice contained herein. This research was supported by use of the Nectar Research Cloud, a collaborative Australian research platform supported by the NCRIS- funded Australian Research Data Commons (ARDC), and the National Computational Infrastructure, which is supported by the Australian Government.

**Appendix A. Supplementary data**

Supplementary data to this article can be found online at [https://doi](https://doi). org/10.1016/j.apenergy.2024.123574.

**References**

[1] Yusufoglu UA, Lee TH, Pletzer TM, Halm A, Koduvelikulathu LJ, Comparotto C, et al. Simulation of energy production by bifacial modules with revision of ground reflection. Energy Procedia 2014;55:389–95. [https://doi.org/10.1016/j](https://doi.org/10.1016/j). egypro.2014.08.111. [2] Reise C, Schmid A. Realistic YIELD expectations for bifacial PV systems – an assessment of announced, predicted and observed benefits. 5 pages. In: 31st European photovoltaic solar energy conference and exhibition; 2015. p. 1775–9. [3] Pelaez SA, Deline C, Greenberg P, Stein JS, Kostuk RK. Model and validation of single-axis tracking with bifacial PV. IEEE J Photovolt 2019;9(3):715–21. https:// doi.org/10.1109/JPHOTOV.2019.2892872. [4] Pelaez SA, Deline C, MacAlpine SM, Marion B, Stein JS, Kostuk RK. Comparison of bifacial solar irradiance model predictions with field validation. IEEE J Photovolt 2019;9(1):82–8. [https://doi.org/10.1109/JPHOTOV.2018.2877000](https://doi.org/10.1109/JPHOTOV.2018.2877000). [5] Ernst M, Conechado GE, Asselineau C-A. Accelerating the simulation of annual bifacial illumination of real photovoltaic systems with ray tracing. iScience 2021: 103698. [https://doi.org/10.1016/j.isci.2021.103698](https://doi.org/10.1016/j.isci.2021.103698). [6] Egido MA, Lorenzo E. Bifacial photovoltaic panels with sun tracking. Int J Solar Energy 1986;4(2):97–107. [https://doi.org/10.1080/01425918608909842](https://doi.org/10.1080/01425918608909842). [7] P´erez Oria J, Sala G. A good combination: tracking of the sun in polar axis and bifacial photovoltaic modules. Sol Wind Technol 1988;5(6):629–36. [https://doi](https://doi). org/10.1016/0741-983X(88)90060-4. [8] Lindsay A, Chiodetti M, Dupeyrat P, Binesti D, Lutun E, Radouane K. Key elements in the design of bifacial PV power plants. 6 pages. In: 31st European photovoltaic solar energy conference and exhibition; 2015. p. 1764–9. [9] Shoukry I, Libal J, Kopecek R, Wefringhaus E, Werner J. Modelling of bifacial gain for stand-alone and in-field installed bifacial PV modules. Energy Procedia 2016; 92:600–8. [https://doi.org/10.1016/j.egypro.2016.07.025](https://doi.org/10.1016/j.egypro.2016.07.025).

[10] Chiodetti M, Lindsay A, Dupeyrat P, Binesti D, Lutun E, Radouane K, et al. PV bifacial photovoltaic yield solar simulation energy with conference a variable and Albedo exhibition; model.

2016. 7 pages.
p. 1449 In: 32nd –55. European
[11] Hansen CW, Gooding R, Guay N, Riley DM, Kallickal J, Ellibee D, et al. A detailed model of rear-side irradiance for bifacial PV modules. In: In: 44th IEEE photovoltaic specialist conference (PVSC). IEEE; 2017. p. 1543–8. [12] Janssen G, Gali R, de Groot K, Carr AJ, van Aken BB, Romijn IG. Impact of inhomogeneous irradiance at the rear of bifacial panels on modelled energy yield. 6 pages. In: 33rd European photovoltaic solar energy conference and exhibition;

[13]

2017. J¨ager K,
p. Tillmann 1618–23. P, Becker C. Detailed illumination model for bifacial solar cells.
Opt Express 2020;28(4):4751–62. [https://doi.org/10.1364/OE.383570](https://doi.org/10.1364/OE.383570). [14] Vogt MR, Pilis G, Zeman M, Santbergen R, Isabella O. Developing an energy rating for pip.3678 bifacial. photovoltaic modules. Prog Photovolt 2023. [https://doi.org/10.1002/](https://doi.org/10.1002/)

[15] Lo CK, Lim YS, Rahman FA. New integrated simulation tool for the optimum design of bifacial solar panel with reflectors on a specific site. Renew Energy 2015;81: 293–307. [https://doi.org/10.1016/j.renene.2015.03.047](https://doi.org/10.1016/j.renene.2015.03.047). [16] McIntosh modules due KR, to Abbott nonuniform MD, Sudbury illumination BA, Meydbray in 1-D tracking

J. Mismatch systems. loss IEEE in J bifacial
Photovolt 2019;9(6):1504–12. [https://doi.org/10.1109/JPHOTOV.2019.2937217](https://doi.org/10.1109/JPHOTOV.2019.2937217). [17] Grommes E-M, Schemann F, Klag F, Nows S, Blieske U. Simulation of the irradiance and ray tracing yield calculation and view of factor bifacial model. PV systems EPJ Photovolt in the USA 2023;14:11. and Germany [https://doi.org/](https://doi.org/) by combining

10.1051/epjpv/2023003.
[18] Zhao C, Xiao J, Yu Y, Jaubert J-N. Accurate shading factor and mismatch loss analysis of bifacial HSAT systems through ray-tracing modeling. Solar Energy Adv 2021;1:100004. [https://doi.org/10.1016/j.seja.2021.100004](https://doi.org/10.1016/j.seja.2021.100004). [19] PVSyst (7.4). PVSyst SA. 2023. [20] Beardsworth G, Shishavan Amir Asgharzadeh, Meydbray Jenya. Quantifying your bifacial gains: Using calibrated PVsyst model input parameters to accurately predict in-field performance. 2020. [21] Crimmins J, McIntosh K, Creasy L, Lee K. Field testing meets modeling: Validated data on bifacial solar performance. 2020. [22] McIntosh depend on K, conditions. Abbott M, In: Sudbury Virtual

B. BifiPV How the Workshop; PVSyst inputs
2020. for bifacial systems
[23] Lighthouse PV. Step-by-step guide to determine PVSyst bifacial inputs with SunSolveTM: Version 5.2. 2023. [24] Ernst the bifacial M, Liu gain X, Asselineau potential of C-A, rooftop Chen D, Solar Huang photovoltaic C, Lennon systems.

A. Accurate Submitted. modelling
2023 of. [25] Cumber PS. View factors-when is ray tracing a good idea? Int J Heat Mass Transf 2022;189:122698. [https://doi.org/10.1016/j.ijheatmasstransfer.2022.122698](https://doi.org/10.1016/j.ijheatmasstransfer.2022.122698). [26] Berrian D, Libal J. A comparison of ray tracing and view factor simulations of locally 28(6):609 resolved –20. [https://doi.org/10.1002/pip.3261](https://doi.org/10.1002/pip.3261) rear irradiance with the experimental. values. Prog Photovolt 2020;

[27] Kang J, Jang J, Reise C, Lee K. Practical comparison between view factor method and ray-tracing method for bifacial PV system yield prediction. 6 pages. In: 36th

[28] European Deline C, Pelaez photovoltaic SA, Marion solar energy B, Sekulic conference B, Stein and J. Understanding exhibition; 2019. bifacial

p. 1474–9.
photovoltaics potential: field performance. Taiyang News Webinar 2019. [29] Pelaez tube parameters SA, Deline on C, rear-irradiance Stein JS, Marion and B, rear-shading Anderson K, loss Muller for M. bifacial Effect PV of torque-

performance on single-axis tracking systems. In: 46th IEEE photovoltaic specialists conference 2019; 2019. p. 3525–30. [30] Riedel-Lyngskaer N, Petit M, Berrian D, Poulsen PB, Libal J, Jakobsen ML. A spatial irradiance map measured on the rear side of a utility-scale horizontal single axis tracker with validation using open source tools. In: 2020 47th IEEE photovoltaic specialists conference (PVSC). IEEE; 2020. p. 1026–32. [31] Russell ACJ, Valdivia CE, Bohemier C, Haysom JE, Hinzer K. DUET: a novel energy yield 2022:1 model –10. [https://doi.org/10.1109/JPHOTOV.2022.3185546](https://doi.org/10.1109/JPHOTOV.2022.3185546) with 3-D shading for bifacial photovoltaic systems.. IEEE J Photovolt [32] Berrian D. Accuracy of ray tracing and view factor optical models for energy yield prediction of fixed tilt and tracked bifacial PV systems. 2020. [33] Tillmann P, J¨ager K, Karsenti A, Kreinin L, Becker C. Model-chain validation for estimating the energy yield of bifacial perovskite/silicon tandem solar cells. Solar RRL 2022;6(9). [https://doi.org/10.1002/solr.202200079](https://doi.org/10.1002/solr.202200079). [34] Ayala Pelaez S, Deline C, Marion B, Sekulic B, McDanold B, Parker J, et al. NREL bifacial experimental single-axis tracking dataset. In: EMN-DURMAT (EMN- DuraMAT). Golden, CO (United States): National Renewable Energy Laboratory (NREL); 2020. [35] SunSolve (6.20.9). PV Lighthouse; 2023. [36] Bishop JW. Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits. Solar Cells 1988;25(1):73–89. https:// doi.org/10.1016/0379-6787(88)90059-2. [37] Deline C, Ayala Pelaez S, MacAlpine S, Olalla C. Estimating and parameterizing mismatch power loss in bifacial photovoltaic systems. Prog Photovolt Res Appl 2020;28(7):691–703. [https://doi.org/10.1002/pip.3259](https://doi.org/10.1002/pip.3259). [38] Deline C, Ayala Pelaez S, MacAlpine S, Olalla C. Bifacial PV system mismatch loss estimation and parameterization. 5 pages. In: 36th European photovoltaic solar energy conference and exhibition; 2019. p. 1449–53. [39] Raina G, Sinha S. A comprehensive assessment of electrical performance and mismatch losses in bifacial PV module under different front and rear side shading scenarios. Energ Conver Manage 2022;261:115668. [https://doi.org/10.1016/j](https://doi.org/10.1016/j). enconman.2022.115668. [40] Qian J, Thomson A, Blakers AW, Tokusato E, Ernst M, Haedrich I. A PV module current mismatch simulation model and application to bifacial modules. In:

Egan R, Passey R, editors. Proceedings of the Asia Pacific solar research conference [43] Faiman D. Assessing the outdoor operating temperature of photovoltaic modules.

2016. Australian PV Institute; 2016. Prog Photovolt Res Appl 2008;16(4):307–15. [https://doi.org/10.1002/pip.813](https://doi.org/10.1002/pip.813).
[41] Cardose R. Irradiance simulation of PV system in urban environments: 3D view [44] Mikofski M, Meyers B, Chaudhari C. PVMismatch project. Richmond, CA: factor model validation and comparison with ray-tracing methods [Master]. Delft SunPower Corporation; 2018. University of Technology: Delft University of Technology; 2020. [45] Beyer WH. Handbook of tables for probability and statistics. CRC Press; 2017. [42] Ernst M, Liu X, Asselineau C-A, Chen D, Huang C, Lennon A. Accurate modelling of the bifacial gain potential of rooftop solar photovoltaic systems. Energ Conver Manage 2024;300:117947. [https://doi.org/10.1016/j.enconman.2023.117947](https://doi.org/10.1016/j.enconman.2023.117947).
