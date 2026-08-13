Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

### 1Enhanced Performance of Two-

## Maryam Tufail

Department of Electrical Engineering, School of Science and Engineering,**and Three-Terminal Perovskite/** Lahore University of Management Sciences, Lahore 54792, Pakistan

# Silicon Tandem Solar Panels

e-mail: maryam.tufail098@gmail.com

## Hassan Imran Through Optimized Orientation

Department of Electrical Engineering, School of Engineering and Applied Sciences, GIFT University,

# and Tracking

Gujranwala 52250, Pakistan e-mail: hassan.imran.ee@gmail.com *The worldwide requirement for the most efficient and sustainable solar energy solutions* *has driven the development of bifacial and tandem photovoltaic (PV) technologies. The*

## Syed Usama Bin Afzaladoption of bifacial perovskite–silicon (PVK–Si) tandem solar cells has provided a new

College of Engineering and Physical Science, *way to improve solar energy conversion efficiency. This work provides a comprehensive* Khalifa University of Science and Technology, *analysis of the energy yield potential of east–west (E/W) and north–south (N/S) oriented* Abu Dhabi 12778, UAE *bifacial perovskite–silicon tandem solar panels in both single-axis tracking and fixed-tilt* e-mail: 100064462@ku.ac.ae *configurations. We focus on heterojunction with intrinsic thin layer (HIT), two-terminal* *tandem (2TT), and three-terminal tandem (3TT) configurations to evaluate their perfor*

## Suleman Sami Qazimance under varying ground albedo conditions. A simulation model based on MATLAB com

Department of Electrical Engineering, *putes the annual and seasonal energy yields for these configurations. The results show that* University of Engineering and Technology, *tracking panels consistently outperform their fixed-tilt counterparts. Seasonal analysis also* Lahore 54890, Pakistan *demonstrates that E/W-oriented tracking panels perform exceptionally well in summer,* e-mail: suleman.qazi@uet.edu.pk *whereas N/S-oriented tracking panels maintain a relatively stable output in both* *summer and fall. The optimized panel orientation significantly mitigates the skewed*

## Nauman Zafar Butt

*power output peaks observed in conventional configurations by strategically adjusting* Department of Electrical Engineering, *subcell exposure to incident sunlight. This approach results in a more balanced energy dis* School of Science and Engineering, *tribution throughout the day. These findings highlight the advantages of tracking bifacial* Lahore University of Management Sciences, *tandem photovoltaic systems over conventional fixed-tilt installations, particularly for sites* Lahore 54792, Pakistan *that require consistent power output and higher energy yields.* [DOI: 10.1115/1.4071046] e-mail: nauman.butt@lums.edu.pk *Keywords: albedo, perovskite–silicon (PVK–Si) solar cells, photovoltaics (PV),* *simulation, tandem solar cells, efficiency, renewable, simulation, solar*

## 1 Introduction

new utility-scale PV systems of around 70% since 2015 [3]. Loca

In order to meet the energy requirement of the expected global tion specified benefits of combining solar tracking with bifacial

population of approximately 10B by 2050, renewable energy solar cells highlighting the potential for achieving higher

resources such as photovoltaics (PVs) will be much needed as efficiency have already quantified, as a result of which tracking

they provide a very cost-effective and environment-friendly bifacial solar farms are likely to be extensively deployed glob

energy solution that is flexible to various land scales [1]. A remark ally [4]. To further minimize the LCOE, PV industry is developing

able reduction in the levelized cost of energy (LCOE) is made next-generation solar cell technologies based on monofacial and

through the rapid progression in the developed technologies of bifacial perovskite–perovskite (PVK–PVK), perovskite–silicon

solar cells and modules, consequently making PV is ever more (PVK–Si), and perovskite/organic (PVK/BHJ) tandem solar cells.

worthwhile. Next-generation solar technologies, for instance, bifa Arguably, among all these, PVK–Si tandem cell is the finest

cial solar cells, are projected to reach up to 40% of the market share choice because of potentially cheap integration of solution-

by 2028 [2]. Moreover, solar tracking has also been integrated into processed perovskite (PVK) along with already commercially developed Silicon (Si) solar cell technologies. These efforts are motivated by the potential efficiency gain of tandem solar cells and the optimal bandgap alignment of perovskite with silicon- 1 Corresponding author. heterojunction (SHJ) cells [5,6]. The commercialization of two- Contributed by the Solar Energy Division of ASME for publication in theterminal (2T) tandem solar cells has compelled studies on their

|J|S E|E|W E|
|---|---|---|---|
|E C received January 22, 2026; published online February 24, 2026. Assoc. Editor: Shima Hajimirza.|. Manuscript received September 24, 2025; final manuscript|||

JOURNAL OF SOLAR ENERGY ENGINEERING: INCLUDING WIND ENERGY AND BUILDING outdoor performance, concentrating on energy yield potential for NERGY ONSERVATION particularly bifacial modules in fixed-tilt and tracking systems. Theoretical study by Dupre et al. [7] has stated a significant gain

**Journal of Solar Energy Engineering Copyright © 2026 by ASME** JUNE 2026, Vol. 148 **/ 031005-1**

of 20 with fixed-tilt standalone bifacial systems as compared to axis tracking systems, intelligent/algorithmic control strategies, bifacial single-junction cells, while Schmager et al. [8] deployed structural designs, and performance metrics. The study highlighted monofacial 2T tandem (2TT) and predicted a 21% and 32% gain how advanced tracking can improve irradiance capture, efficiency, in energy yield potential using single and dual-axis tracking and energy yield across climates, while also discussing emerging systems, respectively, as compared to fixed-tilt configuration. trends such as sensor-less control, artifical intelligence (AI) Field study conducted by Babics et al. [9] using a standalone bifa based optimization, and adaptive algorithms for diffuse-light con Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

cial 2T tandem with a single-axis tracking system reported a 55% ditions [21]. The study on the performance of PV tracking systems gain in daily energy yield relative to a fixed-tilt configuration in by Rodríguez-Gallegos et al. compared traditional sun-tracking desert conditions around the summer solstice. with the best-orientation tracking, showing that orienting panels A global simulation reported by Jahangir et al. [10] demon toward the direction of maximum instantaneous irradiance can strated that at an average albedo of 30%, three-terminal (3T) and improve energy yield, especially under diffuse or rapidly changing four-terminal (4T) tandem solar cells offer approximately 5% sky conditions [22]. However, their work focused on monofacial and 23% gain in annual energy production in comparison to the single-junction systems and did not investigate how such orienta 2T tandem and single-junction SHJ solar cells, respectively. The tion strategies could influence bifacial or tandem (2T/3T) architec first bifacial 4T tandem solar introduced by Kim et al. [11] in the tures, where rear-side irradiance, albedo, and multiterminal current lab gained 30.5% efficiency under 1 sun with 0.2 sun rear irradi extraction can introduce additional performance dynamics. ance, while bifacial minimodules of the same cell under 20–40% This work is the continuation of our previous work on design albedo condition at outdoor tests yield 20% higher output potential considerations of farm-level bifacial PVs. We have herein analyzed as compared to monofacial ones. Manshanden et al. [12] recently how vertical bifacial 2T/3T tandem solar farms perform under conducted an outdoor experiment revealing up to 26% efficiency varying the irradiance and albedo condition. Along with this, it gain at 10% albedo with 100 cm² bifacial 4TT minimodules over has also addressed how vertical bifacial 3T tandem configuration monofacial counterparts. Monolithic 4TT configuration experi attenuates issues like current-matching in 2T with overall improve ences optical losses, contact shading, lateral transport losses, and ment in system performance. However, most performance analysis parasitic absorption because of additional contacts [13]. Contrarily, in the literature have only focused on monofacial tandem cells, and the 3T configuration with optimal tailoring of the energy band gap the energy yield potential of bifacial farms is largely unexplored of bifacial interdigitated back contact (IBC) bottom subcell gives under realistic conditions. advantages by integrating an extra back contact for carrier extrac In this article, we extensively address the abovementioned gap tion, mitigating recombination losses from series-connected by performing the annual energy yield potential analysis for track current-matching limitations which further enhance the output ing bifacial 2T and 3T tandem solar farm under realistic tempera energy yield [14]. Gota et al. demonstrated that in different loca ture varying condition. Additionally, toward this goal, we also tions in the USA, monofacial 3T based on perovskite–silicon developed a detailed simulation model to validate the influence tandems can deliver up to 3–9% more output energy yield than of the orientation of panels (e.g., east–west or north–south) along monofacial 2T. Their studies also depict that a 4T tandem regard with their impact on the energy yield of tracking bifacial 2T and less of its relaxed design limitations in the context of perovskite 3T tandems and their constituent single-junction Si/SHJ cells. thickness and energy bandgap fails to outperform the energy yield of optimized 2T due to parasitic optical losses [15]. Tockhorn et al. experimentally showed 17.1% efficiency with monofacial 3T perovskite/silicon tandem cell featuring IBC, while their simula **2 Modeling Framework** tion result showed a potential efficiency of 27%. Furthermore, Bifacial tandem solar farm comprising both vertical E/W and studies also highlight the design capability of 3T tandems (3TTs) fixed-tilt N/S-oriented solar modules, with heterojunction with to enhance the energy yield by minimizing recombination losses intrinsic thin layer (HIT), 2TT, and 3TT configuration subtypes by facilitating the current extraction [16]. Ross Rucker and Birnie investigated the effects of array design parameters such as module height, inter-row spacing, and racking strategies on the annual energy yield of vertical bifacial solar installations. However, these analyses focus on conventional bifacial systems without considering advanced tandem architectures or dynamic tracking and orientation optimization, as explored in this study [17]. The study by Venu Gopal et al. numerically investigated the optical performance of V trough solar concentrators using bifacial and trifacial absorbers with various bottom reflector geom etries, showing that absorber type and reflector design significantly influence irradiance capture and optical efficiency. Their work pro vides valuable insights for designing concentrator PV systems, which can be further leveraged to evaluate farm-scale energy yield under realistic operating conditions in bifacial tandem solar farms [18]. Wei et al. demonstrated that image-based sun tracking can considerably improve the irradiance collection by specifically aligning PV panels with the solar trajectory. Their work empha sized the importance of dynamic orientation control in maximizing PV output [19]. Recent optimization studies by Lu and Hajimirza highlighted the importance of intelligently controlling panel orien tation to maximize annual energy yield. A particle-based dust deposition model was used to show that the dust accumulation can substantially shift the optimal tracking angle of PV panels. This highlighted that the real environmental effects can reduce the efficiency of the conventional sun-tracking approaches, and model-based angle adjustment can maximize the irradiance collection [20]. Kazem et al. provided a comprehensive review **Fig. 1 Schematic diagrams of modeled PV farms: (*a*) tilted** of modern PV tracking technologies, including single and dual-**bi−N***/***S and (*b*) vertical bi−E***/***W**

**031005-2 /** Vol. 148, JUNE **Transactions of the ASME**

Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

**Fig. 2 Bifacial tandem solar farm with its subtypes of solar modules under each orientation**

of solar modules for each orientation, is shown in Figs. 1 and 2, respectively. For the simulation of the bifacial tandem solar farm, we have used a modeling framework that has been explained previously in Ref. [23]. Solar radiation composed of a bifacial tandem solar **Fig. 3 Structure of (*a*) 2TT PVK/HIT and (*b*) 3TT PVK/HIT(IBC)** farm with respect to any location on the planet earth is computed using an irradiance model. For the calculation of the daily sun path elucidated by the sun’s azimuth and zenith angles, the PVLIB toolbox from Sandia National Library is used for any par distribution of incident sunlight over the surface of modules and ticular location [24]. Thereafter, a Haurwitz clear sky model [25] is ground. A Two-dimensional-view factor approach that is explained used for the computation of global horizontal irradiance (GHI), in detail in our previous work [28] is applied for the calculation of after which it is scaled with the monthly average data from the output energy generated by albedo and diffused irradiance. A set of NASA surface meteorology and solar energy database [26]. By all these calculations is carried out at an interval of one minute per Orgill and Hollands Perez’s model [27], beforehand computed day. Moreover, to get maximum output power, we are considering GHI is decomposed into its two subcomponents, i.e., diffuse hori the horizontal single-axis tracking system with both east–west and zontal and direct normal irradiance. north–south orientations shown in Fig. 1. The module tilt angle (*β*) Sun’s azimuth angle (*γM*) relative to north, ground albedo (RA), about the fixed horizontal axis is updated at each time-step for the module tilt angle (*β*) from the ground, panel’s height (*h*) of 1 m, extraction of maximized output power. Silvaco ATLAS tool simu row-to-row spacing or pitch (*p*) of 2 m, and the elevation (*E*) of lates individual subcells for tandem PVK/Si solar cells, which are 1 m are used for defining PV array configuration in the farm. then combined at the module level with a VM (voltage matching) With these design attributes, the model calculates the spatial string ratio of 3/2 and cell area of 15*.*6 cm × 15*.*6 cm, and these

**Fig. 4 Daily energy yield of vertical bi−E***/***W 3TT, 2TT, and HIT for various months for**

***p**/**h* = 2, RA = 30**%**, and *E* = 1 m**

**Journal of Solar Energy Engineering** JUNE 2026, Vol. 148 **/ 031005-3**

third contact on the back is meant for the collection of electrons from both subcells, and the subcells are connected with the same n-type doping at their common interface as shown in Fig. 3, respec tively, with this nomenclature explained in detail [6] which actually shortens the descriptors of 2TT and 3TT cell configurations. The 3TT configuration ensures the maximum charge carriers collection, Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

resulting in the implication of high efficiency for 3TT by evading current mismatching. In a 3TT tandem solar cell, the bottom IBC subcell incurs an inherent loss associated with albedo photocurrent due to the extra back contact shading as it blocks more reflected light in comparison to the conventional bottom HIT subcell in the 2TT cell which has only one back contact. However, this extra third back contact avoided the current mismatching con straints that are inherently present in the 2TT solar cell. To reduce voltage mismatch in parallel and series interlacing of 3TT cells, connections with the help of VM strings are assumed, although this technique results in end losses of two out of 72 cells. Contrarily, there is no need for voltage matching in the case of 2TT modules, and therefore, they incur no end losses. The ideal VM ratio for 3TT comes out to be 1.579 based on VMPP of each subcell, but in order to keep the design practical

**Fig. 5 Seasonal energy yield of vertical bi−E***/***W 3TT, 2TT, and** and minimize end losses, a VM ratio of 1.5 provides a close

**HIT panels for *p**/**h* = 2, RA = 30**% **and *E* = 1 m** match, though a VM ratio of 5/3 would even be a better match, but it turns out to incur double the end losses consequently making 3/2 more efficient overall. results are further processed to model the performance of bifacial Finally, we have also incorporated the effect of location-based PV arrays at the farm level [29]. temperature variation by self-consistently calculating the cell tem At an individual level, the configuration of each subcell of perature *T*cellbased on hourly average ambient temperature data of single-junction HIT and tandem solar cell including both 2TT the past 5 years obtained from NASA Power and temperature- and 3TT has already been previously described in detail; here, dependent efficiency *η*(*T*cell). For the calculation of the effective we are summarizing its key points. The cell configuration of 2TT temperature coefficient TC* of a 3/2 VM ratio PVK/Si tandem, is PVK/s/HIT, and it is a series-connected configuration in which the temperature coefficient of PVK and HIT was taken to be positive charge carriers (holes) extraction is carried out via a top −0*.*379%/K and −0*.*213%/K, respectively [30]. After that, with contact, on the other hand, negative charge carriers (electrons) this computed TC*, *T*amb, and total incident light, we calculated extraction is carried out via a back contact, while 3TT is PVK/r/ the temperature corrected efficiency *η*(*T*cell). After applying tem nuIBC which is a reverse-connected configuration in which the perature corrections, the electrical model adjusts for partial

**Fig. 6 Daily energy yield of fixed-tilt bi−N***/***S 3TT, 2TT, and HIT for various months for**

**031005-4 /** Vol. 148, JUNE **Transactions of the ASME**

output profile of 2TT and 3TT as in our previous work [31]. Since the top PVK subcell for both 2TT and 3TT was facing east, it leads to a prominent peak in the morning and a slightly lower peak in the afternoon. We modified the panel orientation by positioning half of the panels with their top PVK subcell facing east and the other half with their bottom HIT subcell Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

facing east, to achieve the balanced peaks, ensuring uniform power output in both morning and afternoon. A similar trend of skewed morning and afternoon peaks in the daily energy output profile of HIT was observed too due to the bifa cility factor. However, by modifying the orientation in such that half of the HIT panels face their front side toward the east, and the other half have their back side facing east, the adjustment allows the panels to receive direct sunlight on the front side of HIT in the afternoon when the sun shifts westward, leading to balanced power output in both the morning and afternoon. To obtain more realistic results, we incorporated the effect of location-specified temperature variations by self-consistently calculating the cell temperature and then temperature-dependent efficiency to assess the energy output as discussed in the modeling framework. It is observed that there is a slight decrement in yearly

**Fig. 7 Seasonal energy yield of fixed-tilt bi−N***/***S 3TT, 2TT, and** energy output of 3TT, 2TT, and HIT than in our previous findings.

**HIT panels for *p**/**h* = 2, RA = 30**%**, and *E* = 1 m** Meanwhile, our results support the same trend regarding the perfor mance shown in Fig. 5, and the seasonal output is uppermost in shading losses calculated in our previous work [31] and calculates spring, then tailed by summer and autumn, and lowermost in the solar farm’s power output at each step. winter. Seasonal output energy shows that 3TT overtakes around 16% and 27% than HIT and 2TT, respectively. Overall yearly energy output yield of 3TT, 2TT, and HIT is 193*.*4 kW h*/*m²,

140*.*6 kW h*/*m², and 162*.*5 kW h*/*m² respectively.
## 3 Results and Discussions

### 3.1 Energy Yield of E/W-Oriented Vertical Bifacial 3TT,

### 2TT, and HIT Solar Farms. The simulation results of daily 3.2 Energy Yield of N/S-Oriented Fixed Tilt Bifacial 3TT,

energy output for HIT, 2TT, and 3TT are shown in Fig. 4 for dif **2TT, and HIT Solar Farms.** Figure 6 shows the simulated ferent months. To elucidate the impact of the panel orientation, the results of daily energy output for HIT, 2TT, and 3TT for various issue of skewed morning and afternoon peaks in the daily energy months. Unlike E/W orientation, their daily energy output profile

**Fig. 8 Daily energy yield of tracking bi−E***/***W 3TT, 2TT, and HIT for various months for**

**Journal of Solar Energy Engineering** JUNE 2026, Vol. 148 **/ 031005-5**

**Fig. 9 Seasonal energy yield of tracking bi−E***/***W 3TT, 2TT, and**

**HIT panels for *p**/**h* = 2, RA = 30**%**, and *E* = 1 m**

holds only one midday peak, and it is observed that the perfor mance pattern follows a consistent trend of increasing energy output from HIT to 2TT and then 3TT. N/S orientation, 2TT configuration is uniformly receiving both direct and diffuse solar irradiance throughout the day thereby reducing the current mis matching factor that could limit its efficiency, and thus improve its performance as compared to HIT. The seasonal variation in the performance of 3TT, 2TT, and HIT shown in Fig. 7 highlights the impact of sun trajectory and seasonal variations of solar angle. Seasonal energy output is highest in spring, followed by autumn

and summer, and lowest in winter. In comparison to E/W orienta tion, the seasonal output of autumn surpasses summer because in autumn sun is usually lower in the sky and hence follows a more southern arc which results in N/S-oriented tilted solar panels to receive more direct sunlight, making them more effective in this season than E/W-oriented vertical bifacial solar panels. The Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

overall yearly energy output yield of HIT, 2TT, and 3TT is

212*.*4 kW h*/*m², 255*.*3 kW h*/*m², and 278*.*2 kW h*/*m², respectively.
### 3.3 Energy Yield of Tracking E/W-Oriented Bifacial 3TT, 2TT, and HIT Solar Panels. The significance of tracking solar

panels in E/W-oriented bifacial configurations comes from the fact that these panels can change their orientation with respect to the sun’s position throughout the day, thereby enabling them to capture solar energy all day long. This dynamic adjustment sup ports the system by making it possible to harvest greater energy than the fixed-tilt systems as they are only capable of capturing the sunlight at a static angle. Daily energy output yield of tracking E/W-oriented bifacial 3TT, 2TT, and HIT solar panels for various months is shown in Fig. 8. A slight drop in the intensity of energy output is observed during midday which is due to the effect of albedo. Other than that, tracking configuration also follows the same pattern regarding performance, i.e., 3TT outperforms 2TT while HIT underperforms both 2TT and 3TT. Seasonal output energy yield of tracking E/W vertical bifacial 3TT, 2TT, and HIT solar panels is shown in Fig. 9 which goes from highest to lowest in spring, summer, autumn, and winter, respectively, and it is quite visible that 3TT surpasses approximately 8% and 25% 2TT and HIT, respectively. The effect of tracking is more pro nounced in 2TT and 3TT in comparison to fixed-mounted solar panel configurations. Yearly energy output yield of HIT, 2TT, and 3TT is 239*.*3kW h*/*m², 292*.*7 kW h*/*m², and 316*.*7 kW h*/*m², respectively.

**Fig. 10 Daily energy yield of tracking bi−N**

### 031005-6 / Vol. 148, JUNE

*/***S 3TT, 2TT, and HIT for various months for**

### Transactions of the ASME

**Fig. 11 Seasonal energy yield of tracking bi−N***/***S 3TT, 2TT, and**

**HIT panels for *p**/**h* = 2, RA = 30**%**, and *E* = 1 m**

### 3.4 Energy Yield of Tracking N/S-Oriented Bifacial 3TT, 2TT, and HIT Solar Panels. The simulated results for the daily

energy output yield of tracking N/S-oriented HIT, 2TT, and 3TT for various months are shown in Fig. 10. Unlike tracking the E/W-oriented configuration, the performance of tracking N/ S-oriented configurations does not possess a significant advantage compared to its counterpart fixed-tilt configuration because N/S tracking panels are optimized for capturing sunlight primarily when the sun is directly overhead, thus limiting their efficiency during morning and evening hours. On the other hand, the perfor mance trend of N/S tracking 3TT, 2TT, and HIT follows the same pattern as N/S fixed-tilt configuration such that 3TT outperforms 2TT and HIT underperforms both 3TT and 2TT. Seasonal output energy yield of N/S tracking bifacial 3TT, 2TT, and HIT solar panels is shown in Fig. 11, which shows the highest yield in spring and the lowest in winter, while nearly consistent in summer and autumn in comparison to N/S fixed-tilt configurations because of their tracking mechanism which always ensures the panels align for capturing maximum sunlight. However, 3TT performs 24% better than HIT and 8% more than 2TT. The yearly energy output yield of N/S tracking HIT, 2TT, and 3TT is 222*.*7 kW h*/*m², 266*.*7 kW h*/*m², and 313*.*9 kW h*/*m², respectively.

## 4 Conclusion

In this study, we have compared the performance of bifacial tandem perovskite/silicon solar PV farms in the vertical east/west faced and north/south faced fixed-tilted orientations with the single- axis tracking system in 2T and 3T IBC configurations. We modeled time-varying irradiance interception by the modules including direct, diffuse, and albedo components and the effect of location- based temperature to achieve high consistency. For 3T tandem IBC modules, we incorporated practical cell to module losses including shading of the extra back contact, voltage mismatch of the parallel strings, and end loss for the voltage-matched string. The following are the main conclusions of this article:

The performance of bifacial 2T tandem cells strongly depends on the time-varying solar spectrum and albedo, thus requir ing careful optimization according to the use conditions to minimize current mismatch and the associated heating and reliability challenges. 3T IBC bifacial tandem configuration offers a flexible design as it avoids the current mismatch under various time-varying spectrum and albedo conditions.

Annual energy production of east/west-facing 3TT PVK/IBC vertical bifacial farm is 37.5% higher than the 2TT PVK/ HIT vertical bifacial farm and 18% higher than single- junction HIT vertical bifacial farm. Annual energy production of east/west-facing 3TT PVK/IBC tracking bifacial farm is 8.2% higher than the 2TT PVK/ Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026

HIT tracking bifacial farm and 32.4% higher than single- junction HIT tracking bifacial farm. East/west bifacial tracking farms outperform vertical bifacial farms by 63% (3TT), 108% (2TT), and 47% (HIT). Annual energy production of north/south 3TT PVK/IBC fixed- tilt bifacial farm is 8.9% higher than the 2TT PVK/HIT fixed-tilt bifacial farm and 30.9% higher than single- junction HIT fixed-tilt bifacial farm. Annual energy production of N/S 3TT PVK/IBC tracking bifa cial farm is 9.4% higher than 2TT PVK/HIT tracking bifa cial farm and 31.1% higher than single-junction HIT tracking bifacial farm. N/S bifacial tracking farms outperform fixed-tilt farms by 5% (3TT), 4.5% (2TT), and 4.8% (HIT).

The results predict that the east/west-facing 3TT PVK/IBC tracking bifacial farm is the best configuration due to its signifi cantly higher annual energy production compared to all other con figurations as it outperforms 2TT and HIT tracking farms and provides substantial gains over vertical and fixed-tilt setups. The tracking capability and optimal east/west orientation maximize sunlight capture, making it the most efficient option, particularly for Lahore, Pakistan (latitude: 31*.*5 ◦ N, longitude: 74*.*3 ◦

E).
## Conflict of Interest

### There are no conflicts of interest.

## Data Availability Statement

The datasets generated and supporting the findings of this article are obtainable from the corresponding author upon reasonable request.

## Nomenclature

### Latin Symbols

*h* = panel height (m) *p* = pitch (row-to-row spacing) (m) *E* = panel elevation above ground (m) *T*amb= ambient temperature (K) *T* cell= solar cell temperature (K) *VM*= module voltage (V) *V*MPP= voltage at maximum power point (V) DHI = diffuse horizontal irradiance (W*/*m²) DNI irradiance (W*/* 2 )m GHI = = direct global normal horizontal irradiance (mW*/* 2 ) TC ∗ = effective temperature coefficient (% K −1 ) *η* = conversion efficiency (–)

### Greek Symbols

*β* = module tilt angle from ground (deg) *γ* = sun azimuth angle relative to north (deg) *M*

### Subscripts

*M* = module amb = ambient condition cell = solar cell MPP = maximum power point

### Abbreviations

2T = two-terminal 2TT = two-terminal tandem

JUNE 2026, Vol. 148 **/ 031005-7** **Journal of Solar Energy Engineering**

3T = three-terminal 3TT = three-terminal tandem 4T = four-terminal 4TT = four-terminal tandem HIT = heterojunction with intrinsic thin layer PV = photovoltaic PVK = perovskite RA = ground albedo Si = silicon

## References

[1] Razykov, T. M., Ferekides, C. S., Morel, D., Stefanakos, E., Ullal, H. S., and Upadhyaya, H. M., 2011, “Solar Photovoltaic Electricity: Current Status and Future Prospects,” Sol. Energy, **85**(8), pp. 1580–1608. [2] Fischer, M., Woodhouse, M., Herritsch, S., Trube, J., et al., 2021, “International Technology Roadmap for Photovoltaic (ITRPV),” VDMA EV, [https://itrpv](https://itrpv). vdma.org/en/ueber-uns [3] Fu, R., Feldman, D. J., and Margolis, R. M., 2018, “US Solar Photovoltaic System Cost Benchmark: Q1 2018,” National Renewable Energy Lab. (NREL), Golden, CO, Tech. Rep. [4] Patel, M. T., Ahmed, M. S., Imran, H., Butt, N. Z., Khan, M. R., and Alam, M. A., 2021, “Global Analysis of Next-Generation Utility-Scale PV: Tracking Bifacial Solar Farms,” Appl. Energy, **290**, p. 116478. [5] Alam, M. A., and Khan, M. R., 2019, “Shockley–Queisser Triangle Predicts the Thermodynamic Efficiency Limits of Arbitrarily Complex Multijunction Bifacial Solar Cells,” Proc. Natl. Acad. Sci. USA, **116**(48), pp. 23966–23971. [6] Ryyan Khan, M., and Alam, M. A., 2015, “Thermodynamic Limit of Bifacial Double-Junction Tandem Solar Cells,” Appl. Phys. Lett., **107**(22), p. 223502. [7] Dupre, O., Tuomiranta, A., Jeangros, Q., Boccard, M., Alet, P.-J., and Ballif, C., 2020, “Design Rules to Fully Benefit From Bifaciality in Two-Terminal Perovskite/Silicon Tandem Solar Cells,” IEEE J. Photovolt., **10**(3), pp. 714–721. [8] Schmager, R., Langenhorst, M., Lehr, J., Lemmer, U., Richards, B. S., and Paetzold, U. W., 2019, “Methodology of Energy Yield Modelling of Perovskite- Based Multi-junction Photovoltaics,” Opt. Express, **27**(8), pp. A507–A523. [9] Babics, M., De Bastiani, M., Balawi, A. H., Ugur, E., Aydin, E., Subbiah, A. S., Liu, J., et al., 2022, “Unleashing the Full Power of Perovskite/Silicon Tandem Modules With Solar Trackers,” ACS Energy Lett., **7**(5), pp. 1604–1610. [10] Jahangir, J. B., Patel, M. T., Asadpour, R., Khan, M. R., and Alam, M. A., 2024, “Planet-Scale Energy Yield Potential of Next-Generation Bifacial, Multiterminal, Perovskite-Silicon Tandem Solar Farms,” IEEE J. Photovolt., **14**(2), pp. 363–371. [11] Kim, S., Trinh, T. T., Park, J., Pham, D. P., Lee, S., Do, H. B., Dang, N. N., Dao,

V.-A., Kim, J., and Yi, J., 2021, “Over 30% Efficiency Bifacial 4-Terminal Perovskite-Heterojunction Silicon Tandem Solar Cells With Spectral Albedo,” Sci. Rep., **11**(1), p. 15524.
[12] Manshanden, P., Coletti, G., Rosca, V., Jansen, M. J., de Groot, K., de Graaff,

G. J., Creatore, M., et al., 2022, “Quantifying the Performance Gain of 100 Cm² Bifacial Four Terminal Perovskite-Si Tandem Modules,” EPJ Photovolt., **13**, p. 11.
[13] Qasim, U. B., Imran, H., Kamran, M., Faryad, M., and Butt, N. Z., 2020, “Computational Study of Stack/Terminal Topologies for Perovskite Based Bifacial Tandem Solar Cells,” Sol. Energy, **203**, pp. 1–9.

[14] Sun, Y., Zhou, Z., Asadpour, R., Alam, M. A., and Bermel, P., 2019, “Tailoring Interdigitated Appl. Phys. Lett. Back, Contacts (10), p. for 103901. High-Performance Bifacial Silicon Solar Cells,”

[15] Gota, F., Langenhorst, M., Schmager, R., Lehr, J., and Paetzold, U. W., 2020, “Energy Yield Advantages of Three-Terminal Perovskite-Silicon Tandem Photovoltaics,” Joule, **4**(11), pp. 2387–2403. [16] Tockhorn, and Korte, P., L., Wagner, 2020, “P., Three-Terminal Kegelmann, L., Perovskite/Silicon Stang, J.-C., Mews, Tandem

M., Albrecht, Solar Cells
S., Downloaded from [http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf](http://asmedigitalcollection.asme.org/solarenergyengineering/article-pdf/148/3/031005/7590315/sol-25-1313.pdf) by University of Oxford user on 31 March 2026
With Top and Interdigitated Rear Contacts,” ACS Appl. Energy Mater., **3**(2), pp. 1381–1392. [17] Ross Rucker, W., and Birnie, D. P. III, 2023, “Design Considerations for Vertical Bifacial Agrivoltaic Installations,” ASME J. Sol. Energy Eng., **145**(6), p. 061007. [18] Venu Gopal, P., Saravanan, A., and Elumalai, P., 2026, “Numerical Investigation of Trifacial Optical Absorbers Performance With in V-Trough Various Bottom Solar Concentrators Reflector Geometries, Using Bifacial ” ASME and

J. Sol. Energy Eng., **148**(2), p. 021002.
[19] Wei, C.-C., Song, Y.-C., Chang, C.-C., and Lin, C.-B., 2016, “Design of a Solar Tracking System Using the Brightest Region in the Sky Image Sensor,” Sensors, **16**(12), p. 1995. [20] Lu, J., and Hajimirza, S., 2017, “Optimizing Sun-Tracking Angle for Higher Irradiance Collection of PV Panels Using a Particle-Based Dust Accumulation Model With Gravity Effect,” Sol. Energy, **158**, pp. 71–82. [21] Kazem, H. A., Chaichan, M. T., Al-Waeli, A. H., and Sopian, K., 2024, “Recent Advancements in Solar Photovoltaic Tracking Systems: An In-Depth Review of Technologies, Performance Metrics, and Future Trends,” Sol. Energy, **282**,

p. 112946.
[22] Rodríguez-Gallegos, C. D., Gandhi, O., Panda, S., and Reindl, T., 2020, “On the PV Tracker Performance: Tracking the Sun Versus Tracking the Best Orientation,” IEEE J. Photovolt., **10**(5), pp. 1474–1480. [23] Riaz, M. H., Imran, H., Younas, R., and Butt, N. Z., 2021, “The Optimization of Vertical Bifacial Photovoltaic Farms for Efficient Agrivoltaic Systems,” Sol. Energy, **230**, pp. 1004–1012. [24] Holmgren, W. F., Hansen, C. W., and Mikofski, M. A., 2018, “pvlib Python: A Python Package for Modeling Solar Energy Systems,” J. Open Source Softw., **3**(29), p. 884. [25] Haurwitz, B., 1945, “Insolation in Relation to Cloudiness and Cloud Density,”

J. Atmos. Sci., **2**(3), pp. 154–166.
[26] Patel, M. T., Khan, M. R., Sun, X., and Alam, M. A., 2019, “A Worldwide Cost-Based Design and Optimization of Tilted Bifacial Solar Farms,” Appl. Energy, **247**, pp. 467–479. [27] Orgill, J., and Hollands, K., 1977, “Correlation Equation for Hourly Diffuse Radiation on a Horizontal Surface,” Sol. Energy, **19**(4), pp. 357–359. [28] Riaz, M. H., Imran, H., Younas, R., Alam, M. A., and Butt, N. Z., 2021, “Module Technology for Agrivoltaics: Vertical Bifacial Versus Tilted Monofacial Farms,” IEEE J. Photovolt., **11**(2), pp. 469–477. [29] Alam, M. A., and Khan, M. R., 2022, *Principles of Solar Cells: Connecting* *Perspectives on Device, System, Reliability, and Data Science*, World Scientific, Singapore. [30] McMahon, W. E., Schulte-Huxel, H., Buencuerpo, J., Geisz, J. F., Young, M. S., Klein, T. R., Tamboli, A. C., and Warren, E. L., 2021, “Homogenous Voltage- Matched Strings Using Three-Terminal Tandem Solar Cells: Fundamentals and End Losses,” IEEE J. Photovolt., **11**(4), pp. 1078–1086. [31] Afzal, S. U. B., Imran, H., Qazi, S. S., Alam, M. A., and Butt, N. Z., 2023, “Performance of Vertical Bifacial 2T and 3T Perovskite/Silicon Tandem Solar Farms,” IEEE 50th Photovoltaic Specialists Conference (PVSC), San Juan, PR, June 11–16, IEEE, pp. 1–3.

**031005-8 /** Vol. 148, JUNE **Transactions of the ASME**
