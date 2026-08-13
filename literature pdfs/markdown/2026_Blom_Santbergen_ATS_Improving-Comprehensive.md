## Advanced Theory and Simulations

**www.advtheorysimul.com**

### RESEARCH ARTICLE

# Improving the Comprehensive Modeling Framework for Energy Yield Simulations of Various Novel Photovoltaic

# Systems

Youri Blom Malte Ruben Vogt Olindo Isabella Rudi Santbergen

Delft University of Technology, Photovoltaic Materials and Devices group, Delft, The Netherlands

**Correspondence:** Youri Blom (Y.Blom@tudelft.nl) Rudi Santbergen (R.Santbergen@tudelft.nl)

**Received:** 17 September 2025 **Revised:** 9 April 2026 **Accepted:** 21 April 2026

**Keywords:** electrical modeling | multi-junction devices | optical modeling | PV systems | shade-resilient PV modules

### ABSTRACT

Advanced and emerging photovoltaic (PV) technologies play a crucial role in meeting the increasing global energy demand sustainably. Simulations are essential for predicting system behavior and improving our understanding of complex PV architectures. This work extends an existing modeling framework designed for novel PV systems, offering a modular and flexible workflow suitable for diverse research applications. The framework computes PV performance from first-principles physics, removing the need for module datasheets. It comprises two pre-processing steps and six simulation steps. The first steps determine the optical behavior of the modules, followed by irradiance modeling and temperature calculations. The final steps evaluate the electrical characteristics and the conversion to alternating current at the full-system level. The framework incorporates detailed energy loss analysis and includes advanced features such as partial shading, reverse-bias effects, and photon recycling. Two applications demonstrate its capabilities: comparing module configurations in urban settings and optimizing multi-junction PV system design. Results show that Smart modules enhance shade resilience, delivering approximately 10% higher energy yields. Additionally, the optimal perovskite bandgap for perovskite/silicon tandem devices is found to be 1.60–1.62 eV. These outcomes highlight the framework’s value for future PV system research and development. The developed software can be found at: [https://github.com/YBlom1999/PVMD_Toolbox](https://github.com/YBlom1999/PVMD_Toolbox).

## 1 Introduction

are promising candidates, already demonstrating efficiencies of

34.6% [6], with practical and theoretical limits of 39.5% [7] and
Photovoltaic (PV) energy is a key technology for reducing green-42% [8, 9], respectively. house gas emissions while meeting future global energy demands. A total installed capacity of 75 TW by 2050 is projected [1], which Next to improving the conversion efficiency, the total PV installed can be achieved through both increased conversion efficiency and capacity can also be improved by installing PV systems at expanded deployment. more locations, such as urban areas [10]. This also contributes to different aspects of urban sustainability [11]. However, as Currently, crystalline silicon (c-Si) dominates the PV market with PV systems in urban environments can experience significant a 97% share [2], achieving a record efficiency of 27.81% [3], close shadings, it is crucial to develop shade-resilient PV modules. to its theoretical limit of 29.5% [4, 5]. To surpass this limit, new Different approaches for these shade-resilient modules have been technologies are required. Perovskite/silicon (PS) tandem devices described by Ziar et al. [12].

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License,whichpermitsuse,distributionandreproduction in any medium, provided the original work is properly cited and is not used for commercial purposes. ©2026The Author(s). *Advanced Theory and Simulations* published by Wiley-VCH GmbH

*Advanced Theory and Simulations*, 2026; 9:e01793 1of15 [https://doi.org/10.1002/adts.202501793](https://doi.org/10.1002/adts.202501793)

25130390, 2026, 5, Downloaded from [https://advanced.onlinelibrary.wiley.com/doi/10.1002/adts.202501793](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adts.202501793) by Oxford University, Wiley Online Library on [19/05/2026]. See the Terms and Conditions ([https://onlinelibrary.wiley.com/terms-and-conditions](https://onlinelibrary.wiley.com/terms-and-conditions)) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

To better understand the potential of these novel PV modules, numerical modeling can play a key role. Simulations fulfill different purposes, ranging from making predictions to con- tributing to the understanding of complex systems [13]. Also, in the field of PV systems, different simulation studies have been presented that contributed to our understanding of emerging outdoors PV systems. Multiple studies have developed models and simulation tools to predict the energy yield of multi-junction or perovskite PV devices [14–19], enabling comparisons with c-Si and guiding optimal PS devices design. Similarly, various studies have demonstrated the potential of shade-resilient PV modules [20–26], showing how power electronics can improve the performance of PV modules under partial shading. Further- more, much work has been spent on simulating the performance of PV systems in different environments, such as floating PV or agriphotovoltiac systems [27–30], revealing the potential of PV systems in less conventional areas. However, the simula- tion framework in these studies is mostly tailor-made for their specific research goal. This makes it difficult to use modeling progress obtained in one domain for other types of PV systems. A single modeling framework for various PV systems would simplify the exchange of modeling progress between various subfields.

In this contribution, we continue on previous work [31], where a comprehensive and fundamental modeling framework for photovoltaic systems was introduced, referred to as the “PVMD Toolbox”. The PVMD toolbox divides simulations into distinct steps, offering flexibility across applications. It has been used to perform tandem device optimization [32–35], model photo- voltaic thermal systems [36, 37], study wave effects in floating PV [38], and assess current matching in tandem modules by accounting for location-dependent spectral irradiance [39]. This flexible and multi-purpose approach allows for a fast translation from progress made in one application to another. Moreover, the PVMD Toolbox is mostly based on fundamental material properties and requires minimal empirical input, making it suitable for novel and emerging PV technologies. Since the first publication on the PVMD Toolbox by Vogt et al. [31] the PVMD Toolbox has undergone significant enhancements [32– 34], expanding its capabilities. This work aims to highlight the newly added contributions and demonstrate how the PVMD Toolbox can be applied for various studies. These novelties include reverse bias behavior, photon recycling, extending the spectral irradiance model, accounting for thermal mass, allowing for more module interconnections, and incorporating a detailed loss analysis. These have further strengthened the capabilities of the PVMD Toolbox as a comprehensive framework for sim- ulating a wide range of novel PV systems and have improved the accuracy of energy yield calculations. Furthermore, differ- ent types of validation have been performed that demonstrate the accuracy of the PVMD Toolbox. Section 2 outlines the methodology and the various simulation steps. In Section 3, the different case studies are reported that are used to demonstrate the operation of the PVMD Toolbox. These demonstrations are shown in Section 4, where the wide functionalities of the PVMD Toolbox are illustrated. Finally, Section 5 concludes this work.

**FIGURE 1** The overview of the PVMD Toolbox. In total the Toolbox

consists of six simulation steps, two pre-processing steps, and a loss

analysis.

### 2 Methodology

The overview of the different simulation steps of the PMVD Toolbox is presented in Figure 1. The framework consists of six main simulation steps, along with two pre-processing steps that precede Steps 3 and 5. Additionally, a loss analysis can be executed after the energy yield simulation to obtain a quantitative performance analysis in each step. This structure follows the methodology introduced in our earlier work [31].

Each step requires different types of inputs, as shown in the left of Figure 1. These inputs range from simulation settings, such as the number of cells in the module or system orientation, to material parameter or weather data. These latter inputs can be obtained via direct measurements, literature, or other simulation software. To validate the usage of these input parameters, as well as the developed models, different types of validation have been performed.

Among the six steps, two are classified as static models, mean- ing their outputs remain constant over time. In contrast, the remaining steps are time-resolved models, where outputs vary as a function of time. The remainder of this section provides a detailed explanation of each simulation step and discusses the relevant inputs.

Throughout the PVMD toolbox, two key distinctions are made: between module and sub-module, and between cell and sub-cell. A module refers to the smallest repeating unit in a PV system, typically composed of interconnected strings of solar cells. In the case of four-terminal modules, which contain two electrically independent strings, the module consists of two sub-modules. These sub-modules are encapsulated within the same physical device but are electrically isolated. While sub-modules may differ in cell layout and dimensions, they must share identical overall length and width to fit within the same module frame.

2of15 *Advanced Theory and Simulations*,2026

A cell is defined as the smallest repeating unit within a string. For multi-junction devices, each cell comprises multiple sub- cells, where each sub-cell corresponds to a distinct P-N or P-i-N junction.

The proposed workflow in Figure 1 differs from existing multi- physics PV simulation tools in various ways. In comparison to general multi-physics simulation software, such as COMSOL [40] or Ansys [41], the workflow is computationally much more effi- cient. As this software typically employs finite element method (FEM) techniques, the computation becomes very intensive when simulating on a system level while accounting for effects at the atomistic level. In the proposed workflow, the domain scale can be different for different steps, creating an optimal balance between accuracy and computational effort.

In comparison to more specialized multi-physics PV simulation tools, the difference in workflow varies for different studies in the literature. The Supporting Information contains a detailed com- parison between the presented workflow and different studies.

### 2.1 Optical Absorptance Model

The first step in simulating the energy yield of a PV system involves calculating the absorptance profile of the absorber layers within the device. This step requires a detailed description of the layer stack, including the thickness and complex refractive index of each layer. Additionally, the presence of surface texturing at various interfaces must be specified. Another essential input is the identification of absorber layers within each sub-cell, as well as the assignment of each sub-cell to its corresponding sub- module. Figure 2 illustrates three example layer stacks used as input, along with their resulting absorptance profiles.

The absorptance profile is computed using GenPro4 [42], which is integrated into the PVMD Toolbox. GenPro4 combines the net radiation method [43] with ray-tracing techniques to account for surface texturing. Besides pyramid texturing that is common for wafer-based modules, various nano-textures can also be simulated, such as Asahi U-type texturing [44] that is used in the top part of the 4T module.

While Figure 2 presents the spectral absorptance for normally incident light, the simulation also evaluates absorptance across a range of incidence angles. These angle-resolved profiles, pro- vided in the Supporting Information, are crucial for accurately modeling the optical response of the device under real-world illu- mination conditions. Additionally, bifacial modules also require an absorptance profile for light entering from the rear side. This information serves as a foundation for the subsequent simulation steps.

segments, as illustrated in Figure 3a. A sensitivity value 𝑆𝑖,𝑗,𝑘(𝜆) is generated for each sky segment 𝑖, each cell 𝑗 in the module, and each sub-cell 𝑘 and is wavelength dependent. 𝑆𝑖,𝑗,𝑘(𝜆) is defined as the fraction of the incident light from the sky segment that is absorbed in the absorber layer [45], written as

<u>𝐼 (𝜆)</u> <u>𝑎𝑏𝑠,𝑖,𝑗,𝑘</u> 𝑆 𝑖,𝑗,𝑘(𝜆) =, (1) 𝐼 𝑠𝑘𝑦,𝑖(𝜆)

where 𝐼𝑎𝑏𝑠,𝑖,𝑗,𝑘(𝜆) is the absorbed irradiance and 𝐼𝑠𝑘𝑦,𝑖(𝜆) is the inci- dent irradiance from sky segment 𝑖. This sensitivity is inherently wavelength-dependent due to the spectral characteristics of both the absorptance profile and the ground’s albedo reflectance.

The calculation of the sensitivity map considers two levels of detail. At a fine level, nearby objects are considered that have different impacts on different cells in the system. A critical input for this level is the geometric configuration of the PV modules and their surroundings. This includes the dimensions and spectral reflectance of nearby objects, as well as the albedo of the ground. Previous work [32] has shown that ground material properties significantly influence the performance of bifacial tandem devices. Figure 3b presents two examples of sensitivity maps for a c-Si single-junction module, showing the fraction of light, compared to the incident light from the sky elements, absorbed in the bottom-left cell at a wavelength of 600 nm. It should be noted that these maps only represent a cross-section of the full sensitivity dataset, which spans all cells and wavelengths.

The PVMD Toolbox offers two methods for generating sensitivity maps, differing in complexity and computational cost. The most detailed approach uses the forward ray-tracing software LUX [45], which employs a Monte Carlo method and is well-suited for periodic scenarios, such as field-deployed PV modules. How- ever, LUX can become computationally intensive for complex geometries or high ray counts.

As a faster alternative, the Toolbox includes a backward ray- tracing method developed by Calcabrini et al. [46]. This method combines view factor calculations with single-generation ray- tracing, offering a balance between accuracy and efficiency. A comparison of both methods is provided in the Supporting Infor- mation.

Importantly, both approaches support the simulation of bifa- cial modules. Sensitivity maps can be generated for both the front and rear sides, enabling accurate modeling of rear-side irradiance contributions.

Besides the effects captured by the ray-tracing models, skyline effects can also be considered at a coarser level. This includes all objects at a distance far enough that they impact all cells in the system equally. The skyline is described by a function that expresses the height of the skyline for each azimuth, as shown in Figure 3c. Irradiance coming from sky elements below the skyline cannot be absorbed by the cells, so the sensitivity values for these sky elements are manually set to 0. These objects are not included in the ray-tracer, as the increased amount of data needed to describe the environment will drastically increase the computational time of the ray-tracing algorithm. Given that these

### 2.2 Optical Module Mounting Model

The optical response calculated in the first simulation step is used to generate the so-called sensitivity map [45] of the PV modules. This map quantifies how sensitive each cell in the module is to light originating from different regions of the sky. To construct the sensitivity map, the sky is discretized into multiple angular

**FIGURE 2** Three examples of the input and output of the first simulation step. The input contains the layer stack with the thickness and complex

refractive index of all layers. Also, the absorber layers of the sub-cells are indicated with “Absorber”, and its corresponding submodule is indicated

in curly brackets. The output contains the spectral absorptance profile of the absorber layers. The reflection and parasitic absorption from supporting

layers are indicated in light blue and light grey, respectively. Our framework can handle bifacial modules too, for which also transmission losses can be

spectrally quantified.

effects appear at a far distance, they will impact all cells equally, pre-processing block in Figure 1. For each timestep, the irradiance justifying this fast approach. values from the sky map are multiplied by the correct normalized spectrum (depending on whether the sun is within a given sky segment) to obtain the full spectral irradiance across the sky.

### 2.3 Irradiance Model

A key distinction between the two spectral models is that The first time-resolved step in the PVMD Toolbox involves SMARTS assumes clear-sky conditions, while SBDART accounts calculating the absorbed irradiance and the resulting photo-for cloud cover. To incorporate cloud effects, SBDART generates current density for each cell in the PV module. As illustrated in separate look-up tables for three sky conditions: clear, partly

Figure 4, this is achieved by combining the previously computed cloudy, and overcast. The appropriate table is selected based on

sensitivity map with a time-dependent sky map. the sky clearness index provided by the Perez model [47]. The complete look-up tables for both models are provided in the The sky map describes the angular distribution of irradiance Supporting Information. across the sky dome for each simulation timestep [31, 45]. It is generated using the Perez model [47], which requires as input

|the solar position, direct normal irradiance (DNI), and diffuse|2.4|Temperature Model|||||
|---|---|---|---|---|---|---|
|horizontal irradiance (DHI). These meteorological inputs are|||||||
|obtained via Meteonorm [48]. The Perez model provides the total irradiance per sky segment but|Following Toolbox Initially, the Toolbox employed only the Fuentes fluid dynamic|the calculation simulates|the cell|of absorbed temperature|irradiance, throughout|the PVMD the year.|
|does not include spectral information. As the spectral decomposi-|model|[51]. In its|current|version,|the framework|has been|
|tion is critical for accurately modeling multi-junction devices, the|extended|to include|additional|thermal|models,|such as the|
|PVMD Toolbox integrates two spectral models: SMARTS [49] and|Duffie-Beckman model [52], the Sandia Module Temperature||||||
|SBDART [50]. These models are used to generate look-up tables|model [53], and the Faiman model [54]. This allows users to select||||||
|of normalized spectral distributions for both direct and diffuse|the most appropriate model for their specific application. Notably,||||||
|components as a function of air mass, corresponding to the first|the Fuentes model remains particularly suitable for emerging||||||

4of15 *Advanced Theory and Simulations*,2026

**FIGURE 3** (a) It shows visualization of the sensitivity map. The sky is discretized into different sky segments for which its sensitivity is calculated.

(b) It shows two examples of a sensitivity map of two scenarios. It can be seen that the object has a significant impact on the sensitivity map. The two

maps are calculated for single junction c-Si modules and the cross-section of the bottom left cell at a wavelength of 600 nm is shown. The sensitivity

maps are generated with the backward ray-tracer by Calcabrini et al. [46].

**FIGURE** An example of the calculation of the absorbed irradiance for a PV module in Delft on the 1st of June at 16:00. The sensitivity map and

the sky map are combined to calculate the absorption for each cell at each hour.

*Advanced Theory and Simulations*,2026 5of15

PV systems, as it does not rely on empirical parameters [31]. A comparative analysis of these models is provided in the Supporting Information.

A limitation of earlier implementations was the assumption of steady-state conditions for cell temperature. However, due to the thermal mass of PV modules, temperature changes occur gradually and must be modeled accordingly, especially at high temporal resolutions [55]. To account for this, the cell temperature at time 𝑡, denoted 𝑇𝑐𝑒𝑙𝑙(𝑡), is calculated using

− <u>𝑡𝑖𝑛𝑡</u> () 𝑇𝑐𝑒𝑙𝑙(𝑡) = 𝑇𝑐𝑒𝑙𝑙,𝑠𝑠+ 𝑒𝜏𝑇𝑐𝑒𝑙𝑙(𝑡 − 𝑡𝑖𝑛𝑡)−𝑇𝑐𝑒𝑙𝑙,𝑠𝑠, (2)

where 𝑇𝑐𝑒𝑙𝑙,𝑠𝑠is the steady-state temperature from the thermal model, 𝑡𝑖𝑛𝑡is the simulation time step, and 𝜏 is the ther- mal response time, assumed to be seven minutes [55]. This equation takes a weighted average between the steady-state temperature under current conditions and the temperature of the previous time step. The weight given to the previous time step decreases exponentially with the duration of the timestep.

Another enhancement addresses the effect of reverse bias on cell temperature. In the fluid dynamic model, one of the heat flow terms is the electrical power generated by the cell, 𝑃𝑔𝑒𝑛, which is subtracted from the total absorbed power as it does not contribute to heating. Previously, 𝑃𝑔𝑒𝑛was estimated to be

𝑃𝑔𝑒𝑛= 𝐼𝑎𝑏𝑠⋅𝜂𝑆𝑇𝐶, (3)

where 𝐼𝑎𝑏𝑠is the absorbed irradiance and 𝜂𝑆𝑇𝐶is the effi- ciency under standard test conditions (STC). However, cells almost never operate at STC during outdoor operation. Fur- thermore, due mismatches in irradiances within the mod- ule and current matching requirements, cells can operate at non-ideal conditions and even reach reverse biases. The lat- ter would mean that a cell is dissipating heat instead of removing heat. These aspects make Equation (3) not always accurate.

To address this, an iterative approach is implemented. The elec- trical operating point of each cell is determined in the electrical simulation step, and the thermal and electrical calculations are repeated until both 𝑇𝑐𝑒𝑙𝑙and 𝑃𝑔𝑒𝑛converge [56], as illustrated in

Figure 1. In the first iteration, 𝑃𝑔𝑒𝑛is estimated using Equation (3),

and in subsequent iterations, it is updated using the output from the electrical simulation. The Supporting Information shows the maximum temperature and module power at different iterations for a test case with partial shading. Typically, convergence is achieved within three iterations.

#### 2.5.1 Sub-Cell I–V Curves

The electrical behavior of each sub-cell is modeled separately for the forward bias (𝑉𝑐𝑒𝑙𝑙*>* 0) and reverse bias (𝑉𝑐𝑒𝑙𝑙*<* 0) regimes. In forward bias, the one-diode equivalent circuit model is employed. This model consists of a current source, a diode, and two resistive elements. The cell current 𝐼𝑐𝑒𝑙𝑙as a function of voltage 𝑉𝑐𝑒𝑙𝑙is implicitly defined by

( <u>𝑉𝑐𝑒𝑙𝑙 +𝐼𝑐𝑒𝑙𝑙 ⋅𝑅𝑠</u> ) <u>𝑉𝑐𝑒𝑙𝑙+ 𝐼𝑐𝑒𝑙𝑙⋅𝑅𝑠</u> 𝐼 𝑐𝑒𝑙𝑙(𝑉𝑐𝑒𝑙𝑙)=𝐼𝑝ℎ− 𝐼₀ ⋅ 𝑒 𝑛⋅𝑉𝑡− 1 −, (4) 𝑅𝑠ℎ

where 𝐼𝑝ℎis the photo-generated current, 𝐼₀ and 𝑛 are the diode’s saturation current and ideality factor, and 𝑅𝑠ℎand 𝑅𝑠are the shunt and series resistances, respectively.

To determine these parameters, the PVMD Toolbox uses the Calibrated Lumped Element Method (CLEM) as a second pre- processing step to significantly reduce computational complex- ity [31]. This CLEM model requires as input either measured or simulated*I*–*V*curves of the (sub-)cell under varying temperatures and irradiance levels, such that it can derive the dependencies of the parameter value on the cell temperature and absorbed photo- current. These dependencies are used to obtain a function for each parameter that depends on cell temperature and absorbed current. A more detailed explanation on how the CLEM model makes these functions is provided in the Supporting Information. It should be noted that the level of detail considered in the electrical simulation, and whether certain effects or transport mechanisms are included, depend on how the input *I*–*V* curves are obtained. These input *I*–*V* curves can be obtained in various ways, ranging from detailed semiconductor simulations in TCAD Sentaurus [57] to measured solar cells.

The PVMD Toolbox uses the pre-processed functions from the CLEM model and inputs the 𝑇𝑐𝑒𝑙𝑙and 𝐽𝑎𝑏𝑠from step 3 and 4, respectively, to reconstruct the *I*–*V* curves of the sub-cells at different operating conditions. In case *I*–*V* curves at varying conditions are unavailable, the CLEM model also allows for datasheet values as input. The details for the translation of datasheet values into parameter dependencies are also provided in the Supporting Information.

At reverse bias conditions, we utilize the model from Alonso- Garcia et al [58], which expresses 𝐼𝑐𝑒𝑙𝑙as

2 𝐼 (𝑉) = <u>𝐼</u> <u>𝑝ℎ−</u> ( <u>𝑅𝑠ℎ</u> ( <u>⋅𝑉𝑐𝑒𝑙𝑙</u> √ <u>+ 𝑐 ⋅𝑉</u> <u>𝑐𝑒𝑙𝑙</u> )), (5) 𝑐𝑒𝑙𝑙 𝑐𝑒𝑙𝑙 <u>𝜙𝑇 −𝑉𝑏</u> 1 − exp 𝐵𝑒1 − 𝜙𝑇 −𝑉𝑐𝑒𝑙𝑙

where 𝑐 is a coefficient to characterize the parabolic behavior of the current, 𝐵𝑒is a quasi-constant parameter, 𝜙𝑇is the built-in junction voltage, and 𝑉𝑏is the breakdown voltage.

In multi-junction devices, it is possible for electron-hole pairs that recombine radiatively in a high bandgap sub-cell to be absorbed in lower-bandgap sub-cells, known as photon recycling [59–62]. This is implemented using the method by Jäger et al. [18], as previously described in Ref. [33]. The *I*–*V* curve of lower-bandgap sub-cell is adjusted by updating the photo-generated current of sub-cell 𝑘

### 2.5 Electrical Model

The electrical simulation in the PVMD Toolbox is structured in two levels. First, the current–voltage (*I*–*V*) characteris- tics of all cells or sub-cells within the module are mod- eled individually. These cell-level *I*–*V* curves are then com- bined to construct the overall IV curve of the complete PV module.

(𝐼𝑝ℎ,𝑘) with

𝑘−1 ∑ () 𝐼 𝑝ℎ,𝑘= 𝐼𝑝ℎ0,𝑘+ 𝜂𝐿𝐶,𝑛→𝑘⋅ 𝐼𝑝ℎ,𝑛− 𝐼𝑐𝑒𝑙𝑙,𝑛(𝑉𝑐𝑒𝑙𝑙,𝑛), (6) 𝑛=1

where 𝐼𝑝ℎ0,𝑘is the initial photo-generated current of sub-cell 𝑘 as outputted by the CLEM, 𝜂𝐿𝐶,𝑛→𝑘is the luminescence efficiency from sub-cell 𝑛 to sub-cell 𝑘 [33], and 𝐼𝑐𝑒𝑙𝑙,𝑛(𝑉𝑐𝑒𝑙𝑙,𝑛) is the current of sub-cell 𝑛 at its operating voltage.

Finally, the model accounts for meta-stability effects, which are particularly relevant for perovskite sub-cells. These effects manifest as reversible efficiency changes during light and dark cycles [63, 64]. The implementation follows the model by Remec et al. [64], which introduces an initial voltage loss 𝑉𝑙𝑜𝑠𝑠 that recovers under illumination. 𝑉𝑙𝑜𝑠𝑠is calculated with

<u>𝐻𝑐𝑢𝑚1</u> −<u>𝐸𝑎,𝑀𝑆</u> − 𝑉𝑙𝑜𝑠𝑠= 𝐴𝑀𝑆⋅𝑒𝜏; = 𝐵𝑀𝑆⋅𝑒𝑘𝑏 ⋅𝑇𝑐𝑒𝑙𝑙, (7) 𝜏

where 𝐴𝑀𝑆, 𝐵𝑀𝑆, and 𝐸𝑎,𝑀𝑆are calibration constants, 𝐻𝑐𝑢𝑚is the cumulative daily irradiance, and 𝑘𝑏is the Boltzmann constant. The Supporting Information contains a quantification of how the inclusion of meta-stability improves the modeling accuracy, which has already been demonstrated in earlier work [34].

### 2.6 Conversion Model

#### 2.5.2 Module I–V Curve

Once the *I*–*V* characteristics of all individual cells and sub-cells are determined, they are combined to construct the overall *I*–*V* curve of the PV module. The specific method for combining these curves depends on the module’s interconnection scheme. Funda- mentally, this involves summing voltages for series connections and summing currents for parallel connections.

For a series connection, the total voltage as a function of current can be written as

∑ 𝑉𝑡𝑜𝑡𝑎𝑙(𝐼) = 𝑉𝑖(𝐼), (8) 𝑖

where 𝑉𝑖(𝐼) represents the voltage of segment 𝑖 as a function of current.

Conversely, for a parallel connection, the total current as a function of voltage is expressed as

∑ 𝐼 𝑡𝑜𝑡𝑎𝑙(𝑉) = 𝐼𝑖(𝑉), (9) 𝑖

where 𝐼𝑖(𝑉) is the current of segment 𝑖 as a function of voltage.

Figure 5 illustrates several interconnection schemes supported by

the PVMD Toolbox, highlighting its flexibility. For single-junction devices, various layouts are possible (Figure 5a), each offering different levels of shade tolerance. The standard configuration consists of a series connection of cells with bypass diodes. The

effect of these diodes is modeled by modifying Equation (8) as

()

𝑉𝑡𝑜𝑡𝑎𝑙= max 𝑉 (𝐼), −𝑉𝑖 𝑑𝑖𝑜𝑑𝑒, (10) ∑

𝑖

where 𝑉𝑑𝑖𝑜𝑑𝑒is the forward voltage of the bypass diode.

To enhance shade tolerance, a butterfly layout can be used. This design employs half-cut cells arranged into two substrings connected in parallel with one bypass diode. For even greater resilience, bypass diodes can be replaced with buck converters, forming so-called smart modules, as proposed by Mirbagheri Golroodbari et al. [65]. These bypass diodes allow each substring to work at its own maximum power point, allowing for a greater electricity production in shaded conditions. The implementation of these converters is detailed in the Supporting Information.

Multi-junction devices can come in different terminal config- urations [66–69], significantly influencing the module inter- connection scheme. In previous work [34], we compared the performance of two-terminal, three-terminal, and four-terminal PV modules under outdoor conditions. The PVMD Toolbox also supports simulations of triple-junction devices, as demonstrated in Ref. [33].

The final step in simulating the energy yield of a PV system involves modeling the conversion of direct current (DC) to alternating current (AC). The PVMD Toolbox supports various inverter topologies, including central, string, and micro-inverters, allowing for flexible system configurations. For each topol- ogy, the AC output power (𝑃𝐴𝐶) is calculated with the SNL model [70] This model expresses 𝑃𝐴𝐶as a function of the DC input power, DC input voltage, and inverter-specific parameters, capturing the efficiency and operational characteristics of the inverter.

The required DC input power and voltage are obtained from the module *I*–*V* curves computed in the previous simulation step. Depending on the selected inverter topology, the module voltages and currents are aggregated using the series and parallel connection rules defined in Equations (8) and (9), respectively.

### 2.7 Loss Analysis

To enable a more detailed evaluation of PV system performance, an energy loss analysis has been developed and integrated into the Toolbox. This analysis quantifies the contribution of various loss mechanisms, as thoroughly described in previous work [9].

A total of 17 loss mechanisms is included, grouped into four categories: fundamental, optical, electrical, and system losses. Together, these losses, along with the system efficiency, sum to 100%, allowing for a comprehensive and balanced comparison between different PV systems. This structured approach provides deeper insights into system behavior and helps identify key areas for performance improvement.

Some examples of the different module layouts that can be simulated in the PVMD Toolbox. (a) shows different interconnection

**FIGURE 5**

schemes for single-junction cells, and (b) illustrates the different topologies for multi-junction devices [33].

### 2.8 Validation

To ensure the accuracy and reliability of the PVMD Toolbox, multiple validation studies have been conducted under both STC and real-world outdoor environments.

First, we validate the irradiance simulation of the PVMD Toolbox, by comparing the spectral irradiance generated by the PVMD Toolbox with year-long measurements reported by Driesse et al. [71]. Their dataset includes spectral irradiance on a horizontal surface in Albuquerque, New Mexico. Figure 6 shows the comparison between measured and simulated spectral irradi- ance over the course of a year. Both the SMARTS and SBDART models demonstrate good agreement with the measurements, with similar deviations in total received irradiance.

To validate the performance of double- and triple-junction tan- dem devices under STC, their optical and electrical performance was simulated and compared with experimental measurements, as shown in Figure 7a. The reference devices include a 32.5%- efficient perovskite/silicon (PS) tandem cell reported by Mari- otti et al. [72], and a 27.1%-efficient perovskite/perovskite/silicon triple-junction cell from Liu et al. [73]. Full details of the STC validation are provided in our earlier work [33].

In addition to STC validation, the PVMD Toolbox has been tested for PS device under outdoor conditions [34]. Figure 7b shows

the comparison of maximum power point (MPP) power, current density, and voltage for a 24.2%-efficient PS tandem cell operating in Berlin, as reported by Remec et al. [64]. A comprehensive description of the outdoor validation methodology and results is available in Ref. [34].

## 3 Case Studies

To demonstrate the versatility of the PVMD Toolbox, we present two case studies simulating the performance of different PV system configurations. These examples illustrate how the Toolbox can be applied to a variety of research scenarios. The first case considers a PV system in an urban environment, while the second focuses on a PV field installation, as shown in

Figure 8. While the PVMD Toolbox allows for extensive parameter

variation and optimization, this work focuses on a limited set of parameters to highlight the core functionalities of the framework.

Both case studies are evaluated at four geographically diverse locations, selected based on the Köppen-Geiger-Photovoltaics (KGPV) classification [74, 75] and the machine learning-based PV climate classification (ML-PV) [76]. An overview of the different locations is provided in Table 1. Hourly weather data for a typical meteorological year is sourced from Meteonorm [48]. For thermal modeling, the fluid dynamic model is used in both case studies.

**FIGURE 6** The comparison between the measured and reconstructed spectral irradiance. It can be seen that both the SBDART and SMARTS

model are in good agreement with the measurement. Additionally, the received irradiance (Rec. Irr) and Root Mean Square Error (RMSE) are calculated

for the measurements and both simulations, showing a similar deviation for both models.

**FIGURE 7** (a) The optical and electrical validation of a double and triple junction tandem cell at STC, as demonstrated in Ref. [33]. (b) The

validation of a double junction tandem cell under outdoor conditions, as demonstrated in Ref. [34].

### 3.1 Urban Environment

ior is modeled using Equation (5), fitted to measurements from Clement et al. [78]. The urban case study (Figure 8a) features four PV mod- ules installed on a rooftop with a dormer. To assess the Different module layouts (Figure 5a) are compared to evaluate impact of the dormer, sensitivity maps of each module can their performance under partial shading. In all cases, the four be analyzed. The sensitivity values of all lower left cells at modules are connected in series to a string inverter. The inverter 600 nm are shown in Figure 8a. The maps reveal signifi-efficiency curve and building geometry details are provided in the cant shading effects on the two modules adjacent to the Supporting Information. dormer.

Each module consists of single-junction crystalline silicon (c-**3.2 PV Field** Si) cells with M12 wafer size, using the layer stack shown in the top-left of Figure 2. The electrical behavior is illustrated in The second case study considers a PV module operating in a

Figure 8c. Forward-bias behavior is modeled using the CLEM field environment (Figure 8b). The module consists of 144 half-

approach, calibrated with datasheet values from a 23.6%-efficient cut tandem cells (M12 wafer size), based on the 32.5% efficient PS interdigitated back contact (IBC) device [77]. Reverse-bias behav-device from HZB [72], also used in Figure 2 and the validation in

*Advanced Theory and Simulations*,2026 9of15

**FIGURE 8** The case studies are used to demonstrate the functionality of the PVMD Toolbox. An urban environment (a), where four modules are

placed on a roof (1 to 4 from left to right), and a PV field (b) are considered. For the urban environment, single junction modules are used, for which the

electrical behavior at forward and reverse bias (c) is shown. In the field, modules consisting of perovskite/silicon tandem solar cells are simulated, for

which the electrical behavior is shown in (d) with a perovskite bandgap energy of 1.68 eV.

**TABLE 1** The main climate characteristics of the locations. The ambient temperature is weighted with the global horizontal irradiance, as it better

represents the operating conditions of the PV modules than the simple time average of the ambient temperature.

**Annual Global** **Horizontal Irradiation Weighted average** **Location [kW h** 𝐦 **−**𝟐 **] ambient temperature [** ◦ 𝐂**] KGPV ML-PV**

|Location|[kW h 𝐦|ambient temperature [||KGPV|ML-PV|
|---|---|---|---|---|---|
|Delft|1018||16.2|DL|Temperate 1|
|Lagos|1642||29.4|AH|Tropical 2|
|Lisbon|1758||20.6|DH|Temperate 5|
|Shanghai|1271||21.7|DM|Tropical 1|

Figure 7a. The sub-cell *I*–*V* curves of the encapsulated device are **4 Results**

shown in Figure 8d. The PVMD Toolbox is used to simulate the performance of For each location, the annual energy yield is calculated while the case studies described in Section 3. The primary metric varying module tilt and the perovskite sub-cell bandgap (1.50– for comparison is the annual energy yield. However, additional

1.70 eV) to optimize performance. These bandgap variations metrics such as received irradiance are also considered to provide follow the methodology outlined in [33, 34, 79]. The refractive further insight into system behavior. index and *I*–*V* curves for each simulated bandgap are provided in the Supporting Information.
### 4.1 Urban Environment

Although the scenario represents a PV field, only a single module is simulated under the assumption of periodic boundary condi-We begin by analyzing the performance of PV systems in the tions. This simplification is sufficient to evaluate system-level per-urban environment. Figure 9 illustrates the difference in opera- formance and identify optimal design parameters. The distance tion between the different topologies, by showing the *I*–*V* curve between two module rows is assumed to be 8 meters, and modules of the module 2 in Delft for three consecutive hours. At 11:00, a in a row are separated by 2 cm. Additionally, a free horizon is significant part of the module is shaded, leading to the activation considered. of some bypass diodes. It can be seen that butterfly modules

10of15 *Advanced Theory and Simulations*,2026

**FIGURE 9** The *I*–*V* curve of module 2 at three consecutive hours with different module layouts. It can be seen that smart module has the highest

shade resilience followed by the butterfly module.

**FIGURE 10** The energy yield of the PV systems with different module topologies across all locations. It can be seen that the smart modules have

the largest electricity production, followed by the module with butterfly topology. The crosses in the figure indicate the mismatch losses in each location

for each module layout.

can achieve higher voltages around 7 A due to the different cell The *I*–*V* curves shown in Figure 9 are generated for each interconnections. The smart module can obtain higher powers, hour of the year and for all modules, allowing for an annual as each substring can operate on its own optimal power point. comparison for different topologies. Figure 10 presents the annual For the following hours, the partial shading becomes less, making yield of the different module layouts across all locations. The the module*I*–*V*curves more similar. It can be noted that the smart Supporting Information includes the received irradiance data modules have a slightly lower 𝑉𝑜𝑐compared to the other modules. for each module, confirming that the dormer causes significant This is due to the maximum duty cycle of the buck-converters, shading on adjacent modules. To better quantify the shade which is set at 0.98 (as discussed in the Supporting Information), resilience of the different module layout, also the mismatch losses preventing the module from reaching identical values of 𝑉𝑜𝑐. It are presented in Figure 10. The mismatch losses are defined as should be realized, however, that this does not cause any loss, as the difference between the ideal energy yield (when all cells can the buck converter allows the module to have the same power at operate independently) and the actual energy yield, compared to a lower voltage. the total received irradiance [9].

*Advanced Theory and Simulations*,2026 11 of 15

(a) The received annual irradiation of the modules for different tilts at the different locations. The maximum irradiation is indicated

**FIGURE 11**

with an ’x’. (b) The annual conversion efficiency of the PV module for varying perovskite bandgap energy at the optimal tilt, where the maximum

efficiency is also indicated with an ’x’.

junction module for different bandgap energies. The optimal bandgap energy is found to be between 1.60 and 1.62 eV across all locations. The optimal values can mostly be attributed to these values providing a current matching between the top and bottom cells, minimizing the mismatch losses. As demonstrated in previous work [32, 34], the optimal bandgap energy in a two- terminal tandem device is mostly determined by the mismatch losses due to current-matching constraints.

These parameter sweeps demonstrate the optimization capabili- ties of the PVMD Toolbox and highlight its utility in guiding PV module design for diverse environmental conditions.

Among the configurations, the smart modules exhibit the highest energy yield and the lowest mismatch losses. Additionally, it can be seen that there is only a marginal gain of butterfly modules compared to standard modules. Although different studies have found that butterfly layouts have an improved shade tolerance compared to standard ones [21, 80], this marginal gain can be explained by the fact that all four modules are connected in series. Since the two outer modules do not experience heavy partial shading, the optimal string current is often at high current levels. As the butterfly topology mostly improves the performance at lower current levels (Figure 9), there is only a small boost in performance.

On the contrary, the replacement of the bypass diodes with buck converters does improve the performance on the system level, as it allows the various substrings to operate at various current levels.

It should be realized that more design choices can be made than only the module topology. Other parameters, such as the diode forward voltage or the cell reverse bias voltage, can also impact the results. Calcabrini et al. [20] demonstrated that a breakdown voltage of 0.3 V can improve the energy yield by relatively 20% under shaded conditions. Further stud- ies are recommended to identify the most shade-resilient modules.

### 4.2 PV Field

Next, we evaluate the DC energy yield of a tandem PV module operating in a field environment. As a first step, we analyze the received irradiance for different module tilt angles. Figure 11a shows the annual received irradiation as a function of tilt for each location, with the optimal tilt indicated. As expected, the optimal tilt varies by location due to differences in latitude. In addition to the total received irradiation, the change in spectral irradiance with increasing tilt for all locations is discussed in the Supporting Information.

After optimizing the module tilt and maximizing the received irradiance, we vary the bandgap energy of the perovskite sub-cell.

Figure 11b presents the resulting efficiency of a single double-

## 5 Conclusion

In this work, we have demonstrated the functionality and work- flow of the new version of our PVMD Toolbox, a comprehensive modeling framework for simulating the performance of emerging PV systems. The Toolbox divides the simulation process into six sequential steps, supported by two preprocessing stages, where each step builds upon the output of the previous one. Besides the six modeling steps, an energy loss analysis can be performed to quantitatively evaluate the performance of the PV system.

For each modeling step, the methodology and underlying phys- ical principles have been described in detail. The simulation begins with optical modeling at both the cell and module levels, accounting for spectral absorptance and environmental shading. This is followed by weather-dependent simulations that compute absorbed irradiance and cell temperature over time. Finally, the Toolbox calculates the DC and AC electricity output, incorporating advanced effects such as reverse bias behavior, photon recycling, and meta-stability, while supporting a variety of module configurations.

This modular and physics-based approach enables the PVMD Toolbox to be applied flexibly across a wide range of research scenarios. To illustrate its capabilities, two case studies were pre- sented.

The first case study examined a PV system in a shaded urban environment using c-Si modules. Different module layouts were compared, revealing that smart modules, featuring buck convert- ers, significantly improve shade resilience. Additionally, it was shown that the reverse breakdown voltage of the cells plays a critical role in determining performance under shading.

The second case study focused on optimizing the performance of a perovskite/silicon tandem module in a PV field. By varying the module tilt and the perovskite bandgap energy, the study identified the optimal values of those parameters for maximizing annual energy yield.

Together, these case studies highlight the versatility and potential of the PVMD Toolbox as a powerful tool for the design, analysis, and optimization of next-generation PV systems. The software of the PVMD Toolbox can be found at: https://github.com/ YBlom1999/PVMD_Toolbox.

## Acknowledgements

TU Delft’s Climate Action Program Flagship project “Materials for circular renewable energy technologies”supported this work.

## Conflicts of Interest

The authors declare no conflicts of interest.

### Data Availability Statement

The data that support the findings of this study are available in the supplementary material of this article.

## References

1. N. M. Haegel, P. Verlinden, and M. Victoria, “Photovoltaics at Multi- Terawatt Scale: Waiting Is Not an Option,” *Science* 380, no. 6640 (2023): 39–42, https://www.science.org/doi/abs/10.1126/science.adf6957.
2. Verband Deutscher Maschinen- und Anlagenbau (VDMA), “Interna- tional Technology Roadmap for Photovoltaics (ITRPV),”(2024).
3. “27.81%! LONGi Refreshes the World Record for the Efficiency of Monocrystalline Silicon Cells Again,” accessed May 2025, https://www.longi.com/us/news/longi-world-record-efficiency-of- monocrystalline-silicon-cells/.
4. A. Richter, M. Hermle, and S. W. Glunz, “Reassessment of the Limiting Efficiency for Crystalline Silicon Solar Cells,” *IEEE Journal of* *Photovoltaics* 3, no. 3 (October 2013): 1184–1191.
5. S. Schafer and R. Brendel, “Accurate Calculation of the Absorptance Enhances Efficiency Limit of Crystalline Silicon Solar Cells With Lam- bertian Light Trapping,” *IEEE Journal of Photovoltaics* 8, no. 8 (July 2018): 1156–1158.
6. “34.6%! Record-Breaker LONGi Once Again Sets a New World Efficiency for Silicon-Perovskite Tandem Solar Cells,” accessed June 2024, https://www.longi.com/en/news/2024-snec-silicon-perovskite- tandem-solar-cells-new-world-efficiency/.
7. O. Er-raji, C. Messmer, A. J. Bett, et al., “Loss Analysis of Fully-Textured Perovskite Silicon Tandem Solar Cells: Characterization Methods and Simulation toward the Practical Efficiency Potential,” *Solar RRL* 7, no. 24 (2023): 2300659, https://doi.org/10.1002/solr.202300659.
8. A. D. Vos, “Detailed Balance Limit of the Efficiency of Tandem Solar Cells,” *Journal of Physics D: Applied Physics* 13, no. 13 (May 1980): 839–846.
9. Y. Blom, M. R. Vogt, C. M. Ruiz Tobon, R. Santbergen, M. Zeman, and
O. Isabella, “Energy Loss Analysis of Two-Terminal Tandem PV Systems under Realistic Operating Conditions–Revealing the Importance of Fill Factor Gains,” *Solar RRL* 7, no. 7 (February 2023): 2200579.
10. A. Vulkan, I. Kloog, M. Dorman, and E. Erell, “Modeling the Potential for PV Installation in Residential Buildings in Dense Urban Areas,” *Energy and Buildings* 169 (2018): 97–109, https://www.sciencedirect.com/ science/article/pii/S0378778817339877.
11. D. M. Kammen and D. A. Sunter, “City-Integrated Renewable Energy for Urban Sustainability,” *Science* 352, no. 6288 (2016): 922–928, https:// www.science.org/doi/abs/10.1126/science.aad9302.
12. H. Ziar, P. Manganiello, O. Isabella, and M. Zeman, “Photovoltatron- ics: Intelligent PV-Based Devices for Energy and Information Applica- tions,” *Energy & Environmental Science* 14 (2021): 106–126, https://doi.org/
10.1039/D0EE02491K.
13. E. Winsberg, “Computer Simulations in Science,” in *The Stanford* *Encyclopedia of Philosophy*, Winter 2022 ed., E. N. Zalta and U. Nodelman, Eds. (Metaphysics Research Lab, Stanford University, 2022).
14. Š. Tomšič, M. Jošt, K. Brecl, M. Topič, and B. Lipovšek, “Energy Yield Modeling for Optimization and Analysis of Perovskite-Silicon Tandem Solar Cells under Realistic Outdoor Conditions,” *Advanced Theory and* *Simulations* 6, no. 4 (2023): 2200931, https://advanced.onlinelibrary.wiley. com/doi/abs/10.1002/adts.202200931.
15. M. H. Futscher and B. Ehrler, “Modeling the Performance Limitations and Prospects of Perovskite/Si Tandem Solar Cells under Realistic Operating Conditions,” *ACS Energy Letters* 2, no. 2 (2017): 2089–2095.
16. R. Schmager, M. Langenhorst, J. Lehr, U. Lemmer, B. S. Richards, and
U. W. Paetzold, “Methodology of Energy Yield Modelling of Perovskite- Based Multi-Junction Photovoltaics,” *Optics Express* 27, no. 27 (Apr 2019): A507–A523, https://opg.optica.org/oe/abstract.cfm?URI=oe-27-8-A507.
17. A. Onno, N. Rodkey, A. Asgharzadeh, et al., “Predicted Power Output of Silicon-Based Bifacial Tandem Photovoltaic Systems,” *Joule* 4, no. 3 (2020): 580–596, https://www.sciencedirect.com/science/article/pii/ S2542435119306324.
18. K. Jäger, P. Tillmann, E. A. Katz, and C. Becker, “Perovskite/Silicon Tandem Solar Cells: Effect of Luminescent Coupling and Bifaciality,” *Solar RRL* 5, no. 5 (2021): 2000628.
19. A. Chatzipanagi, N. Taylor, I. M. Suarez, A. M. Martinez, T. S. Lyubenova, and E. D. Dunlop, “An Updated Simplified Energy Yield Model for Recent Photovoltaic Module Technologies,” *Progress in Pho-* *tovoltaics: Research and Applications* 33, no. 8 (2025): 905–917, https:// onlinelibrary.wiley.com/doi/abs/10.1002/pip.3926.
20. A. Calcabrini, P. Procel Moya, B. Huang, et al., “Low-Breakdown- Voltage Solar Cells for Shading-Tolerant Photovoltaic Modules,” *Cell* *Reports Physical Science* 3, no. 3 (December 2022): 101155.
21. A. Calcabrini, R. Weegink, P. Manganiello, M. Zeman, and O. Isabella, “Simulation Study of the Electrical Yield of Various PV Module Topolo- gies in Partially Shaded Urban Scenarios,” *Solar Energy* 225 (September
2021): 726–733.
22. S. Z. Mirbagheri Golroodbari, A. C. De Waal, and W. G. J. H. M. Van Sark, “Improvement of Shade Resilience in Photovoltaic Modules Using Buck Converters in a Smart Module Architecture,” *Energies* 11, no. 11 (January 2018): 250.
23. B. B. Pannebakker, A. C. de Waal, and W. G. van Sark, “Photovoltaics in the Shade: One Bypass Diode per Solar Cell Revisited,” *Progress in* *Photovoltaics: Research and Applications* 25, no. 10 (2017): 836–849, https:// onlinelibrary.wiley.com/doi/abs/10.1002/pip.2898.
24. M. Baka, P. Manganiello, D. Soudris, and F. Catthoor, “A Cost- Benefit Analysis for Reconfigurable PV Modules under Shading,” *Solar* *Energy* 178 (2019): 69–78, https://www.sciencedirect.com/science/article/ pii/S0038092X18311708.
25. S. Ali, L. El Iysaouy, M. Lahbabi, et al., “A MATLAB-Based Modelling to Study and Enhance the Performance of Photovoltaic Panel Configura-

tions during Partial Shading Conditions,” *Frontiers in Energy Research* (2023): 1169172, https://doi.org/10.3389/fenrg.2023.1169172.

26. A. M. Badea, D. Manaila-Maximean, L. Fara, and D. Craciunescu, “Maximizing Solar Photovoltaic Energy Efficiency: MPPT Techniques Investigation Based on Shading Effects,” *Solar Energy* 285 (2025): 113082, https://www.sciencedirect.com/science/article/pii/S0038092X24007771.
27. V. S. Nysted, L. E. S. Stieng, M. Kumar, et al., “Modelling Wave- Induced Losses for Floating Photovoltaics: Impact of Design Parameters and Environmental Conditions,” *Solar Energy* 293 (2025): 113439, https:// www.sciencedirect.com/science/article/pii/S0038092X25002026.
28. K. Polychronakis, D. Korres, C. Sammoutos, E. Vidalis, and C. Tzivanidis, “Frequency Domain Model of Wave-Induced Mismatch in a Moored Floating Solar Platform with Thermal Effects,” *Solar Energy* 304 (2026): 114180, https://www.sciencedirect.com/science/article/pii/ S0038092X25009430.
29. S. Z. Golroodbari and W. van Sark, “Simulation of Performance Differences Between Offshore and Land-Based Photovoltaic Systems,” *Progress in Photovoltaics: Research and Applications* 28, no. 9 (2020): 873–886, https://onlinelibrary.wiley.com/doi/abs/10.1002/pip.3276.
30. S. Zainali, S. M. Lu, Á. Fernández-Solas, et al., “Modelling, Sim- ulation, and Optimisation of Agrivoltaic Systems: A Comprehensive Review,” *Applied Energy* 386 (2025): 125558, https://www.sciencedirect. com/science/article/pii/S0306261925002880.
31. M. Vogt, C. R. Tobon, A. Alcañiz, et al., “Introducing a Comprehensive Physics-Based Modelling Framework for Tandem and Other PV Systems,” *Solar Energy Materials and Solar Cells* 247 (October 2022): 111944.
32. Y. Blom, M. R. Vogt, O. Isabella, and R. Santbergen, “Optimization of the Perovskite Cell in a Bifacial Two-Terminal Perovskite/Silicon Tandem Module,” *Solar Energy Materials and Solar Cells* 282 (2025): 113431, https:// www.sciencedirect.com/science/article/pii/S0927024825000327.
33. Y. Blom, M. R. Vogt, H. Uzu, et al., “Exploring the Potential of Perovskite/Perovskite/Silicon Triple-Junction PV Modules in Two- and Four-Terminal Configuration,” *Solar RRL* 9, no. 5 (2025): 2400613, https:// onlinelibrary.wiley.com/doi/abs/10.1002/solr.202400613.
34. Y. Blom, W. Suprayogi, M. Ruben Vogt, O. Isabella, and R. Santbergen, “Comparison on Module Performance and Degradation Robustness of Two-, Three-, and Four-Terminal Perovskite Silicon Configurations under Realistic Operating Conditions,” Progress in Photovoltaics: Research and Applications (2026): 1-14, https://onlinelibrary.wiley.com/doi/abs/10. 1002/pip.70066.
35. M. Singh, J. Finazzo, Y. Blom, et al., “On the Annual Energy Yield of Perovskite/Silicon Tandem Modules with Different Bottom Cell Technologies and Optimized Top Cell Properties for Different Locations,” *EPJ Photovolt* 16 (2025): 21, https://doi.org/10.1051/epjpv/2025009.
36. Z. Ul-Abdin, M. Zeman, O. Isabella, and R. Santbergen, “Investigating the Annual Performance of Air-Based Collectors and Novel Bi-Fluid Based PV-Thermal System,” *Solar Energy* 276 (2024): 112687, https://www. sciencedirect.com/science/article/pii/S0038092X24003827.
37. H. Bruckner, S. Alyokhina, S. Schneider, et al., “Lessons Learned from Four Real-Life Case Studies: Energy Balance Calculations for Implementing Positive Energy Districts” *Energies* 18, no. 18 (2025), https:// www.mdpi.com/1996-1073/18/3/560.
38. A. Alcañiz, N. Monaco, O. Isabella, and H. Ziar, “Offshore Floating PV- DC and AC Yield Analysis Considering Wave Effects,” *Energy Conversion* *and Management* 300 (2024): 117897, https://www.sciencedirect.com/ science/article/pii/S0196890423012438.
39. P. Procel, Y. Zhou, M. Verkou, et al., “PV Multiscale Modelling of Per- ovskite / Silicon Two-Terminal Devices: From Accurate Cell Performance Simulation to Energy Yield Prediction,” *Solar Energy Materials and Solar* *Cells* 293 (2025): 113864, https://www.sciencedirect.com/science/article/ pii/S0927024825004659.
40. I. COMSOL, “COMSOL Multiphysics Reference Manual, Version 6.2,” accessed 2 April 2026, www.comsol.com.
41. I. ANSYS, “Ansys Academic Research Mechanical,” accessed 2 April 2026 https://www.ansys.com/.
42. R. Santbergen, T. Meguro, T. Suezaki, G. Koizumi, K. Yamamoto, and
M. Zeman, “GenPro4 Optical Model for Solar Cell Simulation and Its Application to Multijunction Solar Cells,” *IEEE Journal of Photovoltaics* 7, no. 7 (2017): 919–926.
43. R. Siegel, “Net Radiation Method for Transmission through Partially Transparent Plates,” *Solar Energy* 15, no. 3 (1973): 273–276.
44. K. Sato, Y. Goto, Y. Wakayama, Y. Hayashi, K. Adachi, and H. Nishimura, “Highly Textured SnO2:F TCO Films for a-Si Solar Cells,” *Asahi Garasue Kenkyu Hokoku* 42 (1993): 129–137.
45. R. Santbergen, V. Muthukumar, R. Valckenborg, W. van de Wall, A. Smets, and M. Zeman, “Calculation of Irradiance Distribution on PV Modules by Combining Sky and Sensitivity Maps,” *Solar Energy* 150 (July
2017): 49–54.
46. A. Calcabrini, R. Cardose, D. Gribnau, et al., “Time-Varying, Ray Trac- ing Irradiance Simulation Approach for Photovoltaic Systems in Complex Scenarios with Decoupled Geometry, Optical Properties and Illumination Conditions,” *Progress in Photovoltaics: Research and Applications* 31, no. 31 (February 2023): 134–148.
47. R. Perez, R. Seals, and J. Michalsky, “All-Weather Model for Sky Lumi- nance Distribution–Preliminary Configuration and Validation,” *Solar* *Energy* 50, no. 50 (March 1993): 235–245.
48. J. Remund, S. Müller, M. Schmutz, and P. Graf, “Meteonorm Version 8,” Meteonorm (2020), https://mn8.meteonorm.com/en/meteonorm- documents.
49. C. A. Gueymard, “The SMARTS Spectral Irradiance Model after 25 Years: New Developments and Validation of Reference Spectra,” *Solar Energy* 187 (2019): 233–253, https://www.sciencedirect.com/science/ article/pii/S0038092X19305110.
50. P. Ricchiazzi, S. Yang, C. Gautier, and D. Sowle, “SBDART: A Research and Teaching Software Tool for Plane-Parallel Radiative Transfer in the Earth’s Atmosphere,” *Bulletin of the American Meteorological Society* 79, no. 79 (October 1998): 2101–2114.
51. M. K. Fuentes, “A Simplified Thermal Model for Flat-Plate Photo- voltaic Arrays,” Sandia National Labs., Albuquerque, NM (USA), Tech. Rep. (May 1987), https://www.osti.gov/biblio/6802914.
52. J. A. Duffie and W. A. Beckman, *Solar Engineering of Thermal* *Processes*, 4th ed. (Wiley, 2013).
53. D. L. King, J. A. Kratochvil, and W. E. Boyson, *Photovoltaic Array* *Performance Model*, vol. 8 (Citeseer, 2004).
54. D. Faiman, “Assessing the Outdoor Operating Temperature of Photo- voltaic Modules,” *Progress in Photovoltaics: Research and Applications* 16, no. 4 (2008): 307–315.
55. A. Jones and C. Underwood, “A Thermal Model for Photovoltaic Sys- tems,” *Solar Energy* 70, no. 4 (2001): 349–359, https://www.sciencedirect. com/science/article/pii/S0038092X00001493.
56. W. Gu, T. Ma, L. Shen, M. Li, Y. Zhang, and W. Zhang, “Coupled Electrical-Thermal Modelling of Photovoltaic Modules under Dynamic Conditions,” *Energy* 188 (2019): 116043, https://www.sciencedirect.com/ science/article/pii/S0360544219317384.
57. S. D. U. Guide, “Sentaurus Device User Guide,” (Mountain View,
2013).
58. M. Alonso-García and J. Ruíz, “Analysis and Modelling the Reverse Characteristic of Photovoltaic Cells,” *Solar Energy Materials and Solar* *Cells* 90, no. 7 (2006): 1105–1120, https://www.sciencedirect.com/science/ article/pii/S0927024805002199.
59. A. W. Walker, O. Höhn, D. N. Micha, et al., “Impact of Photon Recycling and Luminescence Coupling on III-V Single and Dual Junction Photovoltaic Devices,” *Journal of Photonics for Energy* 5, no. 5 (September
2015): 053087.

60. M. A. Steiner and J. F. Geisz, “Non-Linear Luminescent Coupling in Series-Connected Multijunction Solar Cells,” *Applied Physics Letters* 100, no. 25 (2012): 251106, https://doi.org/10.1063/1.4729827.
61. M. Z. Shvarts, M. A. Mintairov, V. M. Emelyanov, V. V. Evstropov, V.
M. Lantratov, and N. K. Timoshina, “Method for Direct Measurements of Luminescent Coupling Efficiency in Concentrator MJ SCs,” (2013): 147–
151.
62. N. L. A. Chan, T. Thomas, M. Fuhrer, and N. J. Ekins-Daukes, “Practical Limits of Multijunction Solar Cell Performance Enhancement From Radiative Coupling Considering Realistic Spectral Conditions,” *IEEE Journal of Photovoltaics* 4, no. 4 (2014): 1306–1313.
63. M. V. Khenkin, A. K. M., I. Visoly-Fisher, et al., “Reconsidering Figures of Merit for Performance and Stability of Perovskite Photo- voltaics,” *Energy & Environmental Science* 11 (2018): 739–743.
64. M. Remec, Š. Tomšič, M. Khenkin, et al., “From Sunrise to Sunset: Unraveling Metastability in Perovskite Solar Cells by Coupled Outdoor Testing and Energy Yield Modelling,” *Advanced Energy Materials* 14, no. 29 (2024): 2304452.
65. S. Z. Mirbagheri Golroodbari, A. C. De Waal, and W. G. J. H. M. Van Sark, “Improvement of Shade Resilience in Photovoltaic Modules Using Buck Converters in a Smart Module Architecture,” *Energies* 11, no. 11 (2018): 250, https://www.mdpi.com/1996-1073/11/1/250.
66. K. Alberi, J. J. Berry, J. J. Cordell, et al., “A Roadmap for Tandem Photovoltaics,” *Joule* 8,no.3(2024):658–692.
67. S. Akhil, S. Akash, A. Pasha, et al., “Review on Perovskite Silicon Tandem Solar Cells: Status and Prospects 2T, 3T and 4T for Real World Conditions,” *Materials & Design* 211 (2021): 110138.
68. Y. Shi, J. J. Berry, and F. Zhang, “Perovskite/Silicon Tandem Solar Cells: Insights and Outlooks,” *ACS Energy Letters* 9, no. 3 (2024): 1305–1330.
69. E. Raza and Z. Ahmad, “Review on Two-Terminal and Four-Terminal Crystalline-Silicon/Perovskite Tandem Solar Cells; Progress, Challenges, and Future Perspectives,” *Energy Reports* 8 (2022): 5820–5851.
70. W. E. Boyson, G. M. Galbraith, D. L. King, and S. Gonzalez, “Per- formance Model for Grid-Connected Photovoltaic Inverters,” Sandia National Laboratories (SNL), Albuquerque, NM, and Livermore, CA (United States), Tech. Rep. (September 2007), https://www.osti.gov/ biblio/920449.
71. A. Driesse, M. Theristis, and J. Stein, “Global Horizontal Spectral Irra- diance and Module Spectral Response Measurements: An Open Dataset for PV Research,”Sandia National Laboratories (SNL), Albuquerque, NM, and Livermore, CA, Tech. Rep. (2023).
72. S. Mariotti, E. Köhnen, F. Scheler, et al., “Interface Engineering for High-Performance, Triple-Halide Perovskite-Silicon Tandem Solar Cells,” *Science* 381, no. 381 (July 2023): 63–69.
73. S. Liu, Y. Lu, C. Yu, et al., “Triple-Junction Solar Cells with Cyanate in Ultrawide-Bandgap Perovskites,” *Nature* 628, no. 628 (April 2024): 306–
312.
74. M. Kottek, J. Grieser, C. Beck, B. Rudolf, and F. Rubel, “World Map of the Köppen-Geiger Climate Classification Updated,” *Meteorologische* *Zeitschrif* 15, no. 15 (June 2006): 259–263.
75. J. Ascencio-Vásquez, K. Brecl, and M. Topič, “Methodology of Köppen- Geiger-Photovoltaic Climate Classification and Implications to World- wide Mapping of PV System Performance,” *Solar Energy* 191 (October
2019): 672–685.
76. F. J. T. de las Heras, O. Isabella, and M. R. Vogt, “A Machine Learning Approach to PV-Climate Classification,” *Renewable Energy* 256(2026): 123685, https://www.sciencedirect.com/science/article/pii/ S0960148125013473.
77. AIKO, “N-Type ABC Mono-Glass Module,” accessed 24 February https://static.groothandelsolar.com/downloads/2024/03/08/aiko- 65eae936eb475477071316.pdf, model = AIKO-A460-MAH54Mb.
78. C. E. Clement, J. P. Singh, E. Birgersson, Y. Wang, and Y. S. Khoo, “Illumination Dependence of Reverse Leakage Current in Silicon Solar Cells,” *IEEE Journal of Photovoltaics* 11, no. 5 (2021): 1285–1290.
79. Y. Blom, M. Ruben Vogt, O. Isabella, and R. Santbergen, “Method for Bandgap Interpolation of Perovskite–s Spectral Complex Refractive Index,” *Optics Express* 32,no.32(January2024):4365.
80. N. Klasen, F. Lux, J. Weber, T. Roessler, and A. Kraft, “A Compre- hensive Study of Module Layouts for Silicon Solar Cells under Partial Shading,” *IEEE Journal of Photovoltaics* 12, no. 2 (2022): 546–556.
## Supporting Information

Additional supporting information can be found online in the Supporting Information section. **Supporting File:** adts70401-sup-0001-SuppMat.pdf.
