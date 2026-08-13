## Solar RRL

## RESEARCH ARTICLE

# Simulation-Based Analysis of Silicon Solar Cell Performance with Laser Enhanced Contacts: Impact of Bulk Defect

# Density and Resistivity

Zhongshu Yang¹ | Marco Ernst¹ | Di Kang¹ | Rabin Basnet¹ | Kean Fong¹ | Peiting Zheng² | Jie Yang² | Anyao Liu¹ | Daniel Macdonald¹

1 2 School of Engineering, The Australian National University, Canberra, Australia | Jinko Solar, Haining Jiaxing, China

Correspondence: Zhongshu Yang (zhongshu.yang@anu.edu.au)

Received: 17 June 2025 | Revised: 21 July 2025 | Accepted: 28 July 2025

Funding: Australian Renewable Energy Agency

Keywords: bulk defects | laser-enhanced contacts | low illumination response | simulation analysis | TOPCon solar cells

ABSTRACT Laser-enhanced metal contact technology has recently emerged as an effective approach to reducing contact recombination in silicon solar cells, particularly in tunneling oxide passivating contacts cells with a front boron-doped emitter and rear phosphorus- doped polysilicon based passivating contact. This technique enables superior front-side surface passivation and open-circuit vol- tages comparable to those of silicon heterojunction counterparts. In this study, we conducted a comprehensive simulation-based analysis comparing the devices with laser-enhanced contacts (LASER) to conventional devices with selective emitters, using experimentally extracted bulk defect parameters across a range of bulk resistivities. Additionally, we evaluated the low-light illumination response of the devices and conducted energy yield simulations under various solar conditions. High-resistivity wafers consistently enhance efficiency when bulk defect levels are low but may degrade performance when defect densities are high, especially in devices with laser-enhanced contacts. Under low-light conditions, the benefits of high-resistivity wafers are further diminished in the presence of significant bulk defects, resulting in reduced energy yields in regions with poor or variable solar resources, despite gains in areas with abundant sunlight. The findings provide valuable insights into the impacts of bulk resistivity, bulk defect density, and illumination intensity on the device performance as well as energy yield.

1 | Introduction contacts between metal and silicon is eliminated, thereby simpli- fying the fabrication process. The laser-enhanced process creates In recent years, laser-enhanced metal contact technology has a large quantity of microscale contacts [6], forming excellent emerged as a promising approach to reducing metal/silicon con-metal/silicon contacts and significantly mitigating the overall tact recombination in silicon (Si) solar cells [1–7], which was metal/silicon contact recombination by reducing the fraction early applied to passivating emitter rear contact (PERC) solar of direct-contact interface area. Moreover, this technology allows cells and then employed to tunneling oxide passivating contacts for the use of p-type emitters with a much higher sheet resis- (TOPCon) solar cells as a crucial strategy. This technology tance, which in turn significantly enhances the front surface pas- involves applying highly intense local laser illumination near sivation by reducing Auger recombination in the heavily doped the metal contacts close to the p–n junction of the device under regions. As a result, laser-enhanced contact technology improves reverse bias conditions [1, 2]. By utilizing laser-enhanced con-open-circuit voltage and overall cell efficiency, elevating the tacts (LASER), the need for selective emitters (SE) to ensure good silicon solar cell performance. Meanwhile, the LASER exhibit

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made. © 2025 The Author(s). Solar RRL published by Wiley-VCH GmbH.

Solar RRL, 2025; 9:e202500465 1of11 [https://doi.org/10.1002/solr.202500465](https://doi.org/10.1002/solr.202500465)

2367198x, 2025, 21, Downloaded from [https://onlinelibrary.wiley.com/doi/10.1002/solr.202500465](https://onlinelibrary.wiley.com/doi/10.1002/solr.202500465) by The Australian National University, Wiley Online Library on [16/11/2025]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

exploring their performance across a range of bulk resistivities. In addition, monthly and annual energy output of the two types of devices for representative locations in Australia were simu- lated using historical irradiance data with a 5-min resolution, providing a comprehensive evaluation of the impact of local solar resource variations on energy yield.

Overall, this work is to evaluate the performance of silicon solar cells with laser-enhanced contacts through comprehensive device simulation analysis, shedding light on the potential ben- efits and limitations of this advanced technology.

excellent stability [4, 5], making it a suitable process to be incor- porated in cell fabrication. Given its significance and relevance for fabricating high-efficiency solar cells, in this study we present a simulation-based analysis focused on quantifying the impact of a laser-enhanced contact approach on the performance of a typi- cal n-type TOPCon cell, with a front boron-doped emitter and rear phosphorus-doped polysilicon on ultrathin silicon oxide interlayer (poly-Si/SiOx) structure.

Concurrently, as surface passivation improves, the quality of industrial Czochralski (CZ) grown Si wafers becomes increas- ingly critical for achieving high-efficiency solar cells. Although the level of transition metal impurities has been significantly reduced during the ingot growth [8–10] of modern CZ-Si and can be further reduced through gettering in some solar cell fab- rication process [11–14], the bulk silicon materials may still pose a limit on the device efficiency. To assess the quality of industrial CZ-Si wafers and its impact on cell performance, we first employed injection dependent lifetime spectroscopy (IDLS) [15–18] to extract the electrical properties of the defects in such silicon wafers after gettering through polysilicon formation [12–14, 19], which represent the residual defects after cell proc- essing since some impurities can be gettered during the solar cell fabrication process. We then applied these apparent residual bulk defect parameters to the simulation of cell performance.

In addition, the optimal silicon bulk resistivity for cell perfor- mance remains a topic of ongoing discussion, and is affected by various factors, such as silicon material quality, processing conditions, and device architecture. A deeper understanding of these interactions is crucial for refining solar cell design and max- imizing overall efficiency. This study presents a simulation-based analysis of TOPCon devices with either SE or LASER on the front side and assessed the effects of bulk resistivity and bulk defect density on device performance.

It is also important to note that solar cell efficiency and the power ratings of photovoltaic (PV) modules are typically reported under standard test conditions (STC), which assume 1-sun illumination (1000 W/m²) at 25°C. However, in real-world applications, PV modules rarely experience continuous 1-sun illumination and may operate under various climate conditions, where the annual energy yield of PV systems may be strongly influenced by the low-illumination characteristics of the cells [20, 21]. To address this, we also compared the low-illumination response of the two types of devices (conventional SE and laser-enhanced contact),

## 2 | Methodology

The samples used in this study for wafer quality assessment were industrially sourced phosphorus-doped n-type and gallium-doped p-type silicon wafers with different resistivities: n-type 0.5 Ωcm, n-type 0.8 Ωcm, n-type 1.2 Ωcm, p-type 1.2 Ωcm, p-type 1.6 Ωcm, and p-type 2.0 Ωcm. After standard RCA cleaning, the samples were symmetrically passivated by n-type phosphorus-doped poly-Si/SiOxstructures and capped with aluminum oxide and sili- con nitride on both sides, resulting in a surface recombination current density (J₀) of around 1.5 fA/cm [2] per side. The injection- dependent lifetime measurements were performed using a Sinton WCT-120 instrument under the photoconductance decay method [22]. The intrinsic recombination was calculated with the recent radiative [23] and Auger recombination [24] models. After accounting for radiative, Auger and surface recombination components, IDLS analysis [15] was applied to extract the SRH parameters of the apparent bulk defect, assuming that it is a recombination active bulk defect with only one single energy level.

The two cell structures simulated in this study are high-efficiency n-type poly-Si/SiOxbased silicon solar cells with different front p+ emitters as shown in Figure 1: one is a selective emitter design with local heavily doped regions under front metal fingers (referred to as “SE”), and the other features a full area lightly doped p+ emitter with laser enhance contact technology (referred to as “LASER”). The simulations were performed with Quokka 3 [25], with the simulation inputs listed in Table S1. The electrical inputs were estimated from the literature [26–28], with details noted in Table S1. The optical model of the cells is based on a lumped front surface transmission extracted from SunSolve Power. To generalize the simulation-based comparison between SE and LASER technologies, device simulations were performed

FIGURE 1 | Schematic cross-section of the n-type poly-Si/SiOx

on the front side.

2of11 Solar RRL, 2025

based solar cells, with a structure of either SE (left) or laser enhanced contact (right)

on the same cell geometry (e.g., silicon substrate thickness, finger The impact of module temperature was considered in the module width, finger pitch, etc.), but with varying bulk resistivities and energy yield simulation, assuming a typical temperature coeffi- defect densities. Typical SE and LASER cells are known to have cient of −0.29%/°C for both types of devices. The monthly and slightly different processing conditions for the boron diffusion annual energy yield was examined at three representative loca- and firing steps, which may, in principle, lead to slightly different tions covering a range of annual irradiance distributions: Alice levels of ring defects and hydrogen-related defects. However, such Springs with consistent and high irradiance, Wagga Wagga with defects are not prevalently observed in completed solar cells, and varied and moderate irradiance, and Melbourne with the worst therefore their impact on the final bulk properties is considered and largely varying solar irradiance. small. We therefore assume the same bulk properties for the SE and LASER cells in some of the subsequent simulation scenarios. 3 | Results and Discussion The energy yield simulation of device output was performed by SunSolve Yield using the solar irradiance data with a temporal 3.1 | Experimental Assessment of the Wafer resolution of 5 min [29], with the assumption that a 144-half-cell Quality module performs under sunlight with single-axis tracking. Electrical input parameters were derived from Quokka 3 gener-Figure 2a–f presents the measured and simulated injection- ated IV curves for varying light intensities and bulk resistivities, dependent lifetime curves of the six sets of samples. The radia- with the inclusion of the apparent bulk defects (details below). tive, Auger, and surface recombination components of the

FIGURE 2 | (a–f ) Experimental and simulated injection-dependent lifetime curves for six sets of samples: n-type 0.5 Ωcm, n-type 0.8 Ωcm, n-type

1.2 Ωcm, p-type 1.2 Ωcm, p-type 1.6 Ωcm, and p-type 2.0 Ωcm. The simulated lifetimes include radiative [23], Auger [24], surface, and SRH components, with the SRH component being the only fitting component. (g) The generalized SRH parameters extracted from the IDLS for all six sets of the samples.
(h) A plot of capture cross-section ratio (k = σn/σp) versus defect energy level for the extracted SRH parameters (red star: solid and open, as the specific half of the bandgap cannot be determined) and the reported SRH parameters of common defects (black square) in silicon wafers [15, 30–39]. Solar RRL, 2025 3of11

as it represents the remaining residual bulk defects that directly affect the final cell performance.

The extracted SRH parameters were then used for device simulations. Note that they were extracted from a relatively

|narrow|bulk resistivity||range of|
|---|---|---|---|
|D|15|16|−3|
|A|15|16|−3|

0.5–1.2 Ωcm for n-type
(N = 4.1 × 10 –1.2 × 10 cm) and 1.2–2.0 Ωcm for p-type (N = 7.2 × 10 –1.2 × 10 cm), but the subsequent simulation considers a wider range of bulk resistivities from 0.3 to 50 Ωcm, for an n-type silicon substrate. However, since the defect is unlikely to be related to dopants (discussed above), in this study the simulation analysis assumed that the defects remain unaf- fected by the variations in bulk resistivity.

injection-dependent lifetimes were calculated based on known models and measured input parameters (detailed above), while the SRH lifetime was the only fitting component. The carrier life- times for all samples are shown to be limited by SRH recombi- nation at injection levels below the 10 15 –5 × 10 15 cm −3 range, except the n-type 0.5 Ωcm samples where Auger recombination dominates the effective carrier lifetime due to the heavy back- ground doping in the silicon wafer bulk. At higher injection lev- els, Auger recombination starts to play a more dominant role, manifesting the impact of bulk resistivity.

The detailed SRH parameters for each sample are listed in Table S2 with the least square errors, and as shown in

Figure 2a–f, the simulated lifetime curves show a good agreement

with the experiment data. The extracted capture cross-section ratio (k = σn/σp) was found to be greater than unity (k > 1), suggesting that the lifetime curves of the p-type samples are more sensitive to the bulk defects and exhibit a stronger injection-dependence compared to n-type samples, as can be seen in Figure 2a–f.

The generalized SRH parameters that fit for the majority of sam- ples with minor variation are listed in Figure 2g, which were fur- ther utilized for device simulation. As can be seen, the defect energy level was found to be 0.06 eV from the intrinsic Fermi level, Et-Ei= ±0.06 eV, since we are unable to determine which half of the bandgap from room-temperature IDLS. It is worth not- ing that the extracted SRH parameters are applicable to both n-type and p-type samples, indicating that the observed bulk defects exhibit similar densities and characteristics regardless of the background dopant type or doping level, therefore unlikely to be caused by dopant-related defects or complexes.

Figure 2h shows a comparison between the extracted SRH

parameters and the reported parameters of common defects in silicon [15, 30–39] by a plot of capture cross-section ratio (k = σn/σp) versus defect energy level with respect to the valence band edge (Et-Ev). The best-matched candidates are found to be copper precipitates and manganese. However, manganese is gen- erally not considered to be a main impurity in silicon devices [40] and there is little information about its presence or concentration in the silicon materials for PVs. On the other hand, copper pre- cipitates have been observed in the silicon materials for PVs (although reported in multicrystalline silicon) [32, 41–43], result- ing in significant carrier recombination [32, 44]. Nevertheless, as the samples were passivated by n-type phosphorus doped poly- Si/SiOxstructure, which provides excellent gettering effects for metal impurities [12, 13], most of the fast or moderately fast diffusing metal impurities are expected to be removed from the silicon wafer bulk, including copper precipitates as well [45]. Although the gettering of copper precipitates first requires a pre- cipitate dissolution step, given copper’s high solubility and diffu- sivity in silicon [40], the gettering process is unlikely to be limited by precipitate dissolution. It is therefore more likely that the extracted SRH parameters come from unknown defects or a com- bination of multiple defects, that are not sensitive to gettering.

Despite the difficulty in exclusively identifying the exact bulk defect, the extracted SRH parameters represent the properties of an apparent defect in the bulk of industrial CZ-Si wafers. Since the apparent defect parameters were extracted from the samples after gettering, it is highly relevant for cell simulation

3.2 | Impact of SRH Defect Density and Bulk Resistivity on Device Performance
Figure 3a–f compares the simulation results of TOPCon devices
 featuring either SE or LASER across a range of bulk resistivities, with or without the previously extracted SRH bulk defect param- eters. As can be seen, the LASER devices exhibit generally supe- rior performance to the SE devices, mainly resulting from an improved front surface passivation, as shown in the J₀ parame- ters in Table S1. There are two main reasons contributing to the reduced J₀ parameters: one is that the laser-enhanced contacts can significantly reduce Auger recombination on the front sur- face by lowering the required doping concentration, without sacrificing the contact resistance between metal and silicon [1, 2]; the other is that the laser process can also reduce recom- bination at the metal/silicon contact region, by applying a different metal paste of no/low aluminum fired at a lower temperature, forming localized microscale contacts under the metal fingers [5, 6]. Thus, as expected, the simulated LASER devices exhibit higher open-circuit voltage (Voc) and maximum- power-point voltage (Vmpp), due to an improved minority carrier lifetime in the silicon wafer bulk, while the short-circuit current ( Jsc) remains similar to the SE devices as the same optical model was used in this study. In addition, for both SE and LASER devices with or without SRH defects, the device performance (Voc, Jsc, Vmpp) improves with increasing bulk resistivity. This can be attributed to an improved minority carrier lifetime in high-resistivity silicon wafers, result- ing from the alleviation of Auger recombination constraints through the reduction of the majority carrier concentration in the silicon bulk. Consequently, the minority carrier density increases, leading to an improved power conversion efficiency (PCE), as shown in Figure 3d. Meanwhile, as the bulk resistivity increases, the difference between the samples with and without SRH defects becomes more pronounced, as high-resistivity sili- con wafers are more susceptible to SRH recombination. This was experimentally observed in Figure 2, where the effective car- rier lifetime becomes increasingly limited by SRH defect lifetime for the n-type silicon wafers of a higher bulk resistivity. In addi- tion, the difference in Vmppbetween samples with and without SRH defects is more evident than in Voc, as SRH defects have a greater influence at lower injection levels, as previously dis- cussed. This highlights the critical demand for silicon wafers of higher bulk quality, particularly if the PV industry is

Simulated cell parameters for SE (left) and LASER (right) devices of various bulk resistivities with or without SRH defects: (a) open-

FIGURE 3 |

circuit voltage, (b) short-circuit current, (c) fill factor, (d) PCE, (e) Vmpp

considering moving toward high-resistivity silicon wafers for their benefit of higher intrinsic lifetimes.

The simulation results for the fill factor (FF) reveal complex behaviors strongly influenced by SRH bulk defects, as shown in Figure 3c. In SE devices without SRH defects, FF increases with bulk resistivity due to enhanced carrier lifetime. However, in the presence of SRH defects, this trend reverses— FF decreases as bulk resistivity increases. In contrast, LASER devices show a consistent improvement in FF with increasing resistivity, regardless of SRH defect presence. Notably, a sharp FF drop is observed in LASER devices at resistivities of

1.0 Ωcm or lower, likely due to elevated series resistance losses (Figure 3f), which include both resistive (majority carrier) and diffusive (minority carrier) components [46]. The declining FF trend in SE devices with SRH defects aligns with previous reports [47, 48], attributed to enhanced SRH recombination. However, this behavior is not observed in LASER devices with SRH defects, suggesting that architectural differences—such as the absence of SE, the higher sheet resis- tance of the full-area p+ emitter, and improved front surface passivation—significantly affect FF behavior. To further explore this, simulations with modified SE parameters were performed (Figure S1).
, and (f ) series resistance loss.

The results from Figure S1b indicate that pseudo-FF (pFF) also decreases with increasing resistivity in the presence of SRH defects, supporting the observed FF trend in Figure 3c. Notably, changes to emitter sheet resistance—not contact recombination— were found to reverse this FF trend by mitigating series resistance losses (Figure S1c). The higher sheet resistance of the p+ emitter amplifies resistive losses, leading to overall higher series resis- tance across the resistivity range. As bulk resistivity decreases, reduced carrier lifetimes lower the minority carrier density, increasing diffusive losses and total series resistance.

These findings suggest that the reversed FF trend in SE devices arises from the interplay between SRH recombination and carrier transport limitations, while the relatively steady FF improvement in LASER devices is primarily constrained by increased resistive losses at low bulk resistivities.

Here, the impact of SRH defect density on the cell performance was analyzed using the previously extracted apparent SRH parameters. Additional details on the simulated impact of defect density are provided in Figure 4. As illustrated, both SE and LASER devices benefit from high-resistivity silicon wafers when the SRH defect density is low. However, as the defect density increases to the range of 10 –10 cm −3, the device performance deteriorates significantly due to SRH recombination. Notably,

Simulated cell parameters for SE (left) and LASER (right) devices of varying bulk resistivity and SRH defect density: (a) open-circuit, and (f ) series resistance loss.

FIGURE 4 |

voltage, (b) short-circuit current, (c) FF, (d) PCE, (e) Vmpp

under high SRH recombination, devices with higher bulk resis- tivities exhibit even lower efficiency compared to those with lower bulk resistivity. Furthermore, LASER devices are found to be more sensitive to SRH defects, resulting in even lower effi- ciencies than SE devices at higher SRH defect densities.

This observation underscores the importance of higher-quality wafers for high-efficiency silicon solar cells, particularly as the PV industry shifts toward high-resistivity silicon wafers. While high-resistivity wafers can improve minority carrier lifetime and PCE by mitigating Auger recombination, these benefits depend critically on maintaining low levels of SRH defects. In the cases where SRH recombination is significant, low-resistivity wafers may still provide advantages.

types of devices decline, and the devices of a higher bulk resis- tivity demonstrate slightly higher Vocvalues. Notably, the slope of Vocversus illumination intensity remains identical for both SE and LASER devices across different bulk resistivities. The Jscval- ues of both SE and LASER devices exhibit a good linear relation- ship with illumination intensity, which can be clearly observed when Figure 5b is presented with both axes plotted on a logarith- mic scale (not shown here).

The FF values exhibit a distinct trend, initially increasing and then decreasing significantly as illumination intensity decreases, and both types of devices display a noticeable hump in the FF trend. Devices with higher bulk resistivities experience a more pronounced drop in FF values under low illumination condi- tions. In contrast, devices with lower bulk resistivities exhibit bet- ter low-light illumination response and maintain relatively stable FF values under similar conditions. Notably, LASER devices exhibit more pronounced degradation under low illumination, with the FF values of high bulk resistivity devices dropping below those of their SE counterparts. Similarly, the Vmppresponse follows the distinct FF trend at low illumination intensity, as shown in Figure 5e.

As can be seen from Figure 5f, the series resistance loss was found to increase with decreasing illumination intensity. This

## 3.3 | Low-Light Illumination Response of the

## Device Performance

Figure 5a–f compares the simulation results for SE and LASER

devices with varying bulk resistivities under different illumina- tion intensities in the presence of SRH defects (parameter details listed in Figure 2g). As expected, the SE devices consistently exhibit inferior performance compared to LASER devices. With decreasing illumination intensity, the Vocvalues of both

Simulated cell parameters for SE (left) and LASER (right) devices of varying bulk resistivity under various illumination intensities with

FIGURE 5 |

SRH defects: (a) open-circuit voltage, (b) short-circuit current, (c) FF, (d) PCE, (e) V

can be attributed to the increased diffusive loss (related to minor- ity carriers) at low illumination intensities for both device types [46, 49], and the devices with a higher bulk resistivity exhibit more severe degradation in the series resistance loss. This increased series resistance loss can explain the drop of FF under low illumination intensity.

Another contributing factor is the presence of SRH defects, which intensify SRH recombination at low injection levels while Auger recombination dominates at high injection levels [16, 24], as shown in Figure 2. Notably, such a large FF drop is not observed in the simulated results without SRH defects (Figure S2). Under low illumination, while all devices experience increased series resistance loss, the loss is more pronounced in devices with SRH defects (Figure 5). Consequently, in the presence of SRH defects, devices with higher bulk resistivities experience a signif- icantly greater increase in series resistance loss compared to those with lower resistivities, resulting in lower FF values under low-light illumination conditions.

It was previously deduced in Section 3.2 that a higher bulk resistivity leads to a higher device PCE under the standard one-sun condition, either with or without SRH defects. However, the results of low light illumination response show that,ifthedeviceswithSRHdefectsperformatalow

mpp, and (f ) series resistance loss.

illumination intensity, the overall PCE of both types of devices with a higher bulk resistivity is inferior to the ones with a lower bulk resistivity (Figure 5d), while the devices without SRH defects benefit from high bulk resistivity across the whole light intensity range (Figure S2d). This distinguished difference highlights the complex nature of identifying a single optimum bulk resistivity for silicon solar cells, and the involvement of SRH defects in the degradation of device performance at vari- ous illumination intensities. Additionally, this raises questions regarding the overall performance of the devices under real- world sunlight conditions, which will be simulated and dis- cussed below.

## 3.4 | Energy Output for Three Representative

## Locations in Australia

Module performance was further simulated for three representa- tive locations in Australia (Alice Springs, Wagga Wagga, and Melbourne) to evaluate the energy output of both SE and LASER devices, with the inclusion of apparent SRH defect parameters and across different bulk resistivities. Figure 6a illus- trates the relative frequency of the suns intensity at these loca- tions. Alice Springs benefits from consistently abundant solar irradiance throughout the year, whereas Wagga Wagga

FIGURE 6 | (a) Relative frequency of the suns intensity at three representative locations in Australia: Alice Springs, Wagga Wagga, and Melbourne.

(b) Simulated normalized annual output forSE (left) and LASER (right) devices across different bulk resistivities, normalized to the results with a baseline resistivity of 2 Ωcm. (c–e) Simulated normalized monthly output for SE (left) and LASER (right) devices at (c) Alice Springs, (d) Wagga Wagga, and (e) Melbourne, normalized to the results with a baseline resistivity of 2 Ωcm. experiences moderate irradiance, and Melbourne endures the It is important to note that the simulation results in Figure 6 poorest conditions out of the three locations, with low illumina-and S3 also account for the impact of module temperature on tion prevailing. device performance, which is known to significantly impact
device performance [50, 51]. However, the temperature correc-

Figure 6b displays the simulated annual outputs, normalized to a tion has only a minor impact on the performance trends at a

baseline resistivity of 2 Ωcm. SE devices achieve the peak perfor-given location, as the same temperature coefficient was applied mance at 2 Ωcm, with their annual output declining as resistivity to both types of devices. This approach highlights the dominant increases, particularly under suboptimal solar conditions. In con-role of irradiance variations in this study. For additional context, trast, LASER devices benefit from a higher bulk resistivity, simulation results without temperature correction are provided although the performance gains diminish in locations with in Figure S4 for reference. poorer solar conditions. This trend aligns well with the device simulation results shown in Figure 3d, representing the device Figure 6c–e presents the normalized monthly energy output for performance under the standard one-sun condition. Notably, both SE and LASER devices across varying bulk resistivities, the variations in annual output due to bulk resistivity remain referenced to the 2 Ωcm baseline. In Alice Springs (Figure 6c), within 0.2%, which is slightly lower than the relative PCE where solar irradiance is consistently high, the impact of bulk improvements observed in Figure 3d. For additional insights, resistivity on SE device performance is minimal. In fact, a higher Figure S3 provides the absolute monthly energy yields for devices resistivity slightly reduces energy output compared to the base- with bulk resistivities of and 50 Ωcm, illustrating seasonal line, aligning with the findings in Figure 3d (simulation based on fluctuations. The reduced energy yield improvement for high-the standard one-sun condition), which identified 2 Ωcm as the resistivity devices is primarily attributed to low-light conditions, optimal bulk resistivity for SE devices with SRH defects. In con- particularly during the winter months (June to August in trast, LASER devices in Alice Springs demonstrate a steady Australia). increase in monthly output with rising bulk resistivity, following

## 8of11 Solar RRL, 2025

The results highlight the potential advantages of high-resistivity wafers in achieving high-efficiency silicon solar cells under STC, particularly when bulk defect densities are low. However, in the presence of significant bulk defect densities, high-resistivity wafers may lead to even lower efficiencies, especially in laser- enhanced contact devices, which are more susceptible to SRH recombination. This underscores the critical need for high- quality wafers with minimal SRH defect densities as the industry considers moving toward high-resistivity materials. Additionally, our energy yield analysis under low illumination conditions sug- gests that high bulk resistivity does not always confer a perfor- mance advantage, as its benefits are diminished in regions with poor or highly variable solar resources. Notably, while LASER devices demonstrated higher annual energy output compared to SE devices, they also exhibited larger seasonal variations, which may pose challenges for maintaining stable energy yields year-round. These findings provide valuable insights into the practical operation of TOPCon solar cells with laser-enhanced contacts, highlighting the importance of optimizing bulk resistiv- ity and defect control to fully realize the efficiency and energy yield benefits across diverse environmental conditions.

the same trend observed in Figure 3d. This suggests that LASER devices can leverage the benefits of higher resistivity more effec- tively under strong solar conditions.

In contrast, devices operating in Wagga Wagga and Melbourne exhibit significant fluctuations in monthly output due to seasonal variations in solar irradiance between summer and winter. As depicted in Figure 6d–e, SE devices with higher bulk resistivities experience reduced monthly output, particularly during the win- ter months (June to August in Australia), when solar irradiance is at its lowest. While SE devices with a lower resistivity of 1 Ωcm show relatively better performance in winter, their output remains below the 2 Ωcm baseline even during summer. As a result, the annual output of SE devices in Wagga Wagga and Melbourne confirms an optimal bulk resistivity of 2 Ωcm, as depicted in Figure 6b.

Conversely, LASER devices in Wagga Wagga and Melbourne exhibit enhanced monthly outputs with increasing bulk resistiv- ity during the Australian summer. However, during the winter, a pronounced decline in monthly output is observed, with perfor- mance falling below the 2 Ωcm baseline. This behavior is likely attributable to reduced efficiency under low-light conditions [20, 21], as illustrated in Figure 5d, which amplifies seasonal var- iations in energy output. Although this presents challenges for systems requiring a stable output profile, the overall annual per- formance of LASER devices still benefits from higher bulk resistivity—primarily due to improved PCE during summer months. However, the gains from higher bulk resistivities for LASER devices may be fully reversed if the solar conditions are even worse, as demonstrated in Figure S5 (a location with worse solar irradiance than Melbourne), where an optimal bulk resistivity was found to be 1 Ωcm for SE devices and 2 Ωcm for LASER devices, suggesting lower energy yields for both SE and LASER devices of high bulk resistivities.

Moreover, as shown in Figure S3c–d, the monthly energy yield comparison indicates that LASER devices achieve an improve- ment of over 2% relative to SE devices throughout the year, with even greater gains at a higher bulk resistivity of 50 Ωcm. This finding aligns with the trends presented in Figure 3d, under- scoring the advantages of employing laser-enhanced metal contacts in n-type TOPCon solar cells.

Acknowledgements This work has been supported by the Australian Renewable Energy Agency (ARENA) through the Australian Centre for Advanced Photovoltaics (ACAP).

Open access publishing facilitated by Australian National University, as part of the Wiley-Australian National University agreement via the Council of Australian University Librarians.

Conflicts of Interest The authors declare no conflicts of interest.

Data Availability Statement The data that support the findings of this study are available from the corresponding author upon reasonable request.

References

1. R. Mayberry, K. Myers, V. Chandrasekaran, A. Henning, H. Zhao, and
U. E. Hofmüller, “Laser Enhanced Contact Optimization (LECO) and LECO-Specific Pastes –A Novel Technology for Improved Cell Efficiency,” in 36th European Photovoltaic Solar Energy Conference and Exhibition, (EUPVSEC, 2019), 80.
2. E. Krassowski, S. Großer, M. Turek, and H. Hoffler, “Laser enhanced contact optimization-A novel technology for metal-semiconductor contact optimization for crystalline silicon solar cells,” in 37th European Photovoltaic Solar Energy Conference (EUPVSEC), (EUPVSEC, 2020), 1–25.
3. D. Ourinson, G. Emanuel, K. Rahmanpour, et al., “Laser-Powered Co-Firing Process for Highly Efficient Si Solar Cells,” IEEE Journal of Photovoltaics 11 (2021): 282–288.
4. E. Krassowski, S. Großer, M. Turek, A. Henning, and H. Zhao, “Investigation of monocrystalline p-type PERC cells featuring the laser enhanced contact optimization process and new LECO paste,” in AIP Conference Proceedings, (AIP, 2021).
5. T. Fellmeth, H. Höffler, S. Mack, et al., “Laser-Enhanced Contact Optimization on iTOPCon Solar Cells,” Progress in Photovoltaics: Research and Applications 30 (2022): 1393–1399.
## 4 | Conclusion

In this study, we first experimentally evaluated the quality of industrially sourced CZ-Si wafers and extracted the SRH parameters associated with the apparent bulk defects after get- tering, which represent the residual defects present in the final device. Subsequently, we conducted a comprehensive simula- tion analysis based on the extracted SRH defect parameters to compare the performance of n-type TOPCon devices (boron doped p + emitter on the front side and phosphorus doped poly-Si/SiOxpassivating contacts on the rear side) either with conventional SE or incorporating laser-enhanced contacts on the front. The analysis examined device performance with and without SRH defects across a range of bulk resistivities (0.3–50 Ωcm).

6. S. Groser, E. Krassowski, S. Swatek, H. Zhao, and C. Hagendorf, “Microscale Contact Formation by Laser Enhanced Contact Optimization,” IEEE Journal of Photovoltaics 12 (2022): 26–30.
7. E. Krassowski, T. Luka, V. Naumann, M. Turek, S. Großer, and
H. Zhao, “Degradation Stability of Solar Cells After Laser Enhanced Contact Optimization (LECO).”, in AIP Conference Proceedings, 2487, (AIP, 2022).
8. R. Basnet, C. Sun, T. Le, et al., “Investigating Wafer Quality in Industrial Czochralski-Grown Gallium-Doped p-Type Silicon Ingots with Melt Recharging,” Solar RRL 7 (2023): 1–7.
9. T. Le, Y. Cai, Z. Yang, R. Chen, D. Macdonald, and A. Liu, “Industrial Czochralski n-Type Silicon Wafers: Gettering Effectiveness and Possible Bulk Limiting Defects,” Solar RRL 8 (2024): 1–6.
10. A. Kashizadeh, R. Basnet, L. Black, et al., Auger-Limited Bulk Lifetimes in Industrial Czochralski-Grown n-Type Silicon Ingots with Melt Recharging, Solar Energy Materials and Solar Cells 277 (2024): 113143.
11. S. P. Phang and D. MacDonald, “Direct Comparison of Boron, Phosphorus, and Aluminum Gettering of Iron in Crystalline Silicon,” Journal of Applied Physics 109 (2011): 073521.
12. A. Y. Liu, D. Yan, S. P. Phang, A. Cuevas, and D. Macdonald, “Effective Impurity Gettering by Phosphorus-and Boron-Diffused Polysilicon Passivating Contacts for Silicon Solar Cells,” Solar Energy Materials and Solar Cells 179 (2018): 136–141.
13. A. Y. Liu, S. P. Phang, and D. Macdonald, “Gettering in Silicon Photovoltaics: A Review,” Solar Energy Materials and Solar Cells 234 (2022): 111447.
14. Z. Yang, J. Krügener, F. Feldmann, et al., “Comparing the Gettering Effect of Heavily Doped Polysilicon Films and Its Implications for Tunnel Oxide-Passivated Contact Solar Cells,” Solar RRL 7 (2023): 2200578.
15. S. Rein, Lifetime Spectroscopy: A Method of Defect Characterization in Silicon for Photovoltaic Applications, (Springer, 2005).
16. H. Bleichner, P. Jonsson, N. Keskitalo, and E. Nordlander, “Temperature and Injection Dependence of the Shockley-Read-Hall Lifetime in Electron Irradiated n-Type Silicon,” Journal of Applied Physics 79 (1996): 9142–9148.
17. C. Vargas, Y. Zhu, G. Coletti, et al., “Recombination Parameters of Lifetime-Limiting Carrier-Induced Defects in Multicrystalline Silicon for Solar Cells,” Applied Physics Letters 110 (2017): 092106.
18. Y. Zhu, C. Sun, T. Niewelt, G. Coletti, and Z. Hameiri, “Investigation of Two-Level Defects in Injection Dependent Lifetime Spectroscopy.,” Solar Energy Materials and Solar Cells 216 (2020): 110692.
19. Z. Yang, J. Krügener, F. Feldmann, et al., “Impurity Gettering in Polycrystalline-Silicon Based Passivating Contacts—the Role of Oxide Stoichiometry and Pinholes,” Advanced Energy Materials 12 (2022): 1–11.
20. N. H. Reich, W. G. J. H. M. van Sark, E. A. Alsema, et al., “Crystalline Silicon Cell Performance at Low Light Intensities,” Solar Energy Materials and Solar Cells 93 (2009): 1471–1481.
21. R. K. Sharma, A. D. Pakki, and J. Holovský, “Silicon Heterojunction Solar Cells: Excellent Candidate for Low Light Illuminations”, Solar Energy Materials and Solar Cells 274 (2024): 113001.
22. R. A. Sinton and A. Cuevas, “Contactless Determination of Current- Voltage Characteristics and Minority-Carrier Lifetimes in Semiconduc- tors from Quasi-Steady-State Photoconductance Data,” Applied Physics Letters 69 (1996): 2510–2512.
23. A. Fell, T. Niewelt, B. Steinhauser, F. D. Heinz, M. C. Schubert, and S. W. Glunz, “Radiative Recombination in Silicon Photo- voltaics: Modeling the Influence of Charge Carrier Densities and Photon Recycling,” Solar Energy Materials and Solar Cells 230 (2021): 111198.
24. L. E. Black and D. H. Macdonald, “On the Quantification of Auger Recombination in Crystalline Silicon,” Solar Energy Materials and Solar Cells 234 (2022): 111428.
25. A. Fell, J. Schön, M. C. Schubert, and S. W. Glunz, “The Concept of Skins for Silicon Solar Cell Modeling,” Solar Energy Materials and Solar Cells 173 (2017): 128–133.
26. R. Basnet, D. Yan, D. Kang, et al., “Current Status and Challenges for Hole-Selective Poly-Silicon Based Passivating Contacts,” Applied Physics Reviews 11 (2024):
27. PV Lighthouse, EDNA2 Emitter Calculator, accessed March 21, 2025, [https://www2.pvlighthouse.com.au/calculators/edna2/edna2.aspx](https://www2.pvlighthouse.com.au/calculators/edna2/edna2.aspx).
28. X. Wang, J. Yuan, X. Wu, et al., “Higher efficiencies TOPCon solar cells in mass production enabled by laser-assisted firing,” in Asia- Pacific Solar Research Conference, (Australian Photovoltaic Institute (APVI), 2024).
29. M. Ernst and J. Gooday, “Methodology for Generating High Time Resolution Typical Meteorological Year Data for Accurate Photovoltaic Energy Yield Modelling,” Solar Energy 189 (2019): 299–306.
30. A. C. Wang and C. T. Sah, “Complete Electrical Characterization of Recombination Properties of Titanium in Silicon,” Journal of Applied Physics 56 (1984): 1021–1031.
31. J. P. Kalejs, B. R. Bathey, J. T. Borenstein, and R. W. Stomont, “Effects of transition metal impurities on solar cell performance in polyscrystalline silicon,” in 23rd IEEE Photovoltaic Specialists Conference, (IEEE, 1993), 184–189.
32. D. Macdonald, W. Brendle, A. Cuevas, and A. A. Istratov, “Injection- Dependent Lifetime Studies of Copper Precipitates in Silicon,” in Proceedings of the Workshop on Crystalline Silicon Solar Cell Materials and Processes, (AIP, 2002), 201–204.
33. D. Macdonald and L. J. Geerligs, “Recombination Activity of Interstitial Iron and Other Transition Metal Point Defects in p- and n-Type Crystalline Silicon,” Applied Physics Letters 85 (2004): 4061–4063.
34. D. MacDonald, T. Roth, P. N. K. Deenapanray, T. Trupke, and
R. A. Bardos, “Doping Dependence of the Carrier Lifetime Crossover Point upon Dissociation of Iron-Boron Pairs in Crystalline Silicon,” Applied Physics Letters 89 (2006): 14–16.
35. T. Roth, P. Rosenits, S. Diez, et al., “Electronic Properties and Dopant Pairing Behavior of Manganese in Boron-Doped Silicon,” Journal of Applied Physics 102 (2007): 103716.
36. S. Diez, S. Rein, T. Roth, and S. W. Glunz, “Cobalt Related Defect Levels in Silicon Analyzed by Temperature-and Injection- Dependent Lifetime Spectroscopy,” Journal of Applied Physics 101 (2007): 033710.
37. C. Sun, F. E. Rougieux, and D. Macdonald, “Reassessment of the Recombination Parameters of Chromium in n- and p-Type Crystalline Silicon and Chromium-Boron Pairs in p-Type Crystalline Silicon,” Journal of Applied Physics 115 (2014): 214907.
38. J. Schon, T. Niewelt, D. Mu, et al., “Experimental and Theoretical Study of Oxygen Precipitation and the Resulting Limitation of Silicon Solar Cell Wafers,” IEEE Journal of Photovoltaics 11 (2021): 289–297.
39. T. T. Le, Z. Zhou, A. Chen, et al., “Reassessing Iron-Gallium Recombination Activity in Silicon,” Journal of Applied Physics 135 (2024): 0–12.
40. K. Graff, Metal Impurities in Silicon-Device Fabrication, (Springer,
2001).
41. A. A. Istratov, T. Buonassisi, R. J. McDonald, et al., “Metal Content of Multicrystalline Silicon for Solar Cells and Its Impact on Minority Carrier Diffusion Length,” Journal of Applied Physics 94 (2003): 6552–6559.
42. D. Macdonald, A. Cuevas, A. Kinomura, Y. Nakano, and L. J. Geerligs, “Transition-Metal Profiles in a Multicrystalline Silicon Ingot,” Journal of Applied Physics 97 (2005): 033523.

43. G. Stokkan, D. S. Marisa, R. Søndenå, et al., “Impurity Control in High (left) and laser-enhanced contacts (right) devices at Hamelin, across dif- Performance Multicrystalline Silicon,” Physica Status Solidi (A) ferent bulk resistivities, normalized to the results with a baseline resis- Applications and Materials Science 214 (2017): 1700319.
tivity of 2 Ωcm. Supporting Information Table S1: Input parameters

44. J. Lindroos and H. Savin, “Review of Light-Induced Degradation in
for the Quokka device simulations on n-type silicon solar cells with either selective emitters or laser-enhanced contacts on the front side and full- Crystalline Silicon Solar Cells,” Solar Energy Materials and Solar Cells 147 area phosphorus-doped n-type polysilicon passivating contact on the rear. (2016): 115–126, Preprint at [https://doi.org/10.1016/j.solmat.2015.11.047](https://doi.org/10.1016/j.solmat.2015.11.047). Supporting Information Table S2: The extracted SRH parameters from

45. A. Liu, C. Sun, H. C. Sio, X. Zhang, H. Jin, and D. Macdonald, the injection-dependent lifetime spectroscopy for each set of samples. “Gettering of Transition Metals in High-Performance Multicrystalline Silicon by Silicon Nitride Films and Phosphorus Diffusion,” Journal of Applied Physics 125 (2019): 043103.
46. R. Brendel, S. Dreissigacker, N. P. Harder, and P. P. Altermatt, “Theory of Analyzing Free Energy Losses in Solar Cells,” Applied Physics Letters 93 (2008): 173503.
47. A. Richter, J. Benick, F. Feldmann, A. Fell, M. Hermle, and
S. W. Glunz, “N-Type Si Solar Cells with Passivating Electron Contact: Identifying Sources for Efficiency Limitations by Wafer Thickness and Resistivity Variation,” Solar Energy Materials and Solar Cells 173 (2017): 96–105.
48. A. Richter, J. Benick, A. Fell, M. Hermle, and S. W. Glunz, “Impact of Bulk Impurity Contamination on the Performance of High-Efficiency n- Type Silicon Solar Cells,” Progress in Photovoltaics: Research and Applications 26 (2018): 342–350.
49. A. Quokka Fell, 3 Modelling Guide, accessed March 21, 2025, https:// www.quokka3.com/support/modelling-guide.html.
50. M. Nikolaeva-Dimitrova, R. P. Kenny, E. D. Dunlop, and
M. Pravettoni, “Seasonal Variations on Energy Yield of a-Si, Hybrid, and Crystalline Si PV Modules,” Progress in Photovoltaics: Research and Applications 18 (2010): 311–320.
51. M. Shravanth Vasisht, J. Srinivasan, and S. K. Ramasesha, “Performance of Solar Photovoltaic Installations: Effect of Seasonal Variations,” Solar Energy 131 (2016): 39–46. Supporting Information Additional supporting information can be found online in the Supporting Information Section. Supporting Information Figure S1: Simulated (a,d) fill factor, (b,e) pseudo fill factor and (c,f ) Rs loss for selective emitter devices of different bulk resistivities (a,b,c) with and (d,e,f ) without SRH defects. Baseline: fill factor of baseline condition (i.e., the same as
Figure 3); Front Rsheet: adjusting front full-area p+ emitter to a sheet
 resistance of 500 Ω/sq (200 Ω/sq in the baseline condition); SE Rsheet: adjusting front selective emitter with sheet resistance of 200 Ω/sq (80 Ω/sq in the baseline condition); Front+SE Rsheet: adjusting both front full-area p+ emitter and selective emitter both to a sheet resistance of 500 Ω/sq; J0,metal: adjusting front metal/silicon recombination J0, metal to 75 fA/cm² (250 fA/cm² in the baseline condition). Supporting Informtion Figure S2: Simulated cell parameters for selective emitter (left) and laser-enhanced contacts (right) devices of different bulk resis- tivities under various illumination intensities without SRH defects: (a) open-circuit voltage, (b) short-circuit current, (c) fill factor, (d) power con- version efficiency, (e) maximum-power-point voltage, and (f ) series resistance loss. Supporting Information Figure S3: (a,b) Simulated absolute monthly energy yield for selective emitter (left) and laser- enhanced contacts (right) devices of (a) 2 Ωcm and (b) 50 Ωcm at three representative locations in Australia with temperature correction. (c,d) Improvement in the simulated monthly energy output with temper- ature correction for the laser-enhanced contacts devices over selective emitter devices, with a bulk resistivity of (c) 2 Ωcm and (d) 50 Ωcm. Supporting Information Figure S4: (a,b) Simulated absolute monthly energy yield for selective emitter (left) and laser-enhanced contacts (right) devices of (a) 2 Ωcm and (b) 50 Ωcm at three representative locations in Australia without temperature correction. (c,d) Improvement in the simulated monthly energy output without temperature correction for the laser-enhanced contacts devices over selective emitter devices, with a bulk resistivity of (c) 2 Ωcm and (d) 50 Ωcm. Supporting Information Figure S5: Simulated normalized annual output for selective emitter Solar RRL, 2025 11 of 11
