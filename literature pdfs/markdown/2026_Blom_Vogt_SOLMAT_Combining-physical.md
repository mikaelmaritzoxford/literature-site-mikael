Solar Energy Materials & Solar Cells 299 (2026) 114169

Contents lists available at ScienceDirect

## Solar Energy Materials and Solar Cells

journal homepage: www.elsevier.com/locate/solmat

# Combining physical- and scenario-based modeling to identify tolerable degradation rates of perovskite in monolithic two-terminal

# perovskite/silicon tandem modules

∗ ∗, Malte Ruben Vogt Youri Blom, Rudi Santbergen, Olindo Isabella *Delft University of Technology, Mekelweg 4, Delft, 2628CD, The Netherlands*

## ARTICLE INFO ABSTRACT

### Keywords: As crystalline silicon (c-Si) solar cells approach their theoretical efficiency limit, the perovskite/silicon (PerSi)

Degradation modeling tandem technology offers a promising solution for further improving the efficiency of photovoltaic (PV) Perovskite/silicon modules modules. However, as perovskite cells are facing stability issues, it is unclear whether PerSi modules will have a Lifetime energy yield larger lifetime energy yield (LEY) than c-Si modules. In this work, we present a novel methodology to simulate Environmental impact the LEY of PerSi tandem devices, accounting for environmental stress factor-dependent degradation across Reliability four different climates. Our approach combines a physics-based analytical degradation model for components shared with c-Si modules and a scenario-based degradation model for the perovskite top cell. This method enables us to identify the tolerable degradation rate (*𝑘𝑡𝑜𝑙*) of the perovskite cell under different scenarios and climatic conditions. We find that *𝑘𝑡𝑜𝑙*is lowest when degradation occurs in the short-circuit current, reaching a minimum value of 1.2% per year in Delft (the Netherlands). Additionally, we demonstrate that *𝑘𝑡𝑜𝑙*inversely depends on the module lifetime, reaching values up 7.6% per year in Lagos (Nigeria). Moreover, we show that module efficiency (*𝜂𝑚𝑜𝑑*) significantly impacts *𝑘𝑡𝑜𝑙*. For instance, increasing *𝜂𝑚𝑜𝑑*from 28.0% to 32.9% raises *𝑘𝑡𝑜𝑙*by approximately 50%. Additionally, we propose a simplified model that can predict *𝑘𝑡𝑜𝑙*without the computationally intensive simulations, which has a root-mean-square error of 0.34% per year. Lastly, environmental impact assessments reveal that PerSi modules are more sustainable in all impact categories when the degradation rate is 80% of

## 1. Introduction

To surpass the theoretical efficiency limit of 29.5% [1,2] for con- ventional crystalline silicon (c-Si) solar cells, the perovskite/silicon (PerSi) tandem technology offers a promising solution. This technol- ogy has practical and theoretical efficiency limits of 39.5% [3] and 42% [4,5], respectively, with a record efficiency of 34.6% [6] already demonstrated. However, perovskite-based solar cells face stability issues [7,8], which would affect the lifetime of PerSi modules. Since both efficiency and lifetime are crucial for total electricity generation [9], both factors must be considered when comparing c-Si and PerSi systems. A key determinant of a photovoltaic (PV) system’s lifetime is its degradation rate (*𝑘*), which quantifies the irreversible power loss com- pared to its initial power [10]. *𝑘* can be predicted using data-driven or physics-based models [11], both of which require calibration with outdoor data. Unfortunately, current reported outdoor experiments

*𝑘* *𝑡𝑜𝑙*for LEY.

involving PerSi technology are mostly limited to small-scale cells op- erating for a maximum of one year [12–15], making conventional approaches unsuitable. An alternative approach involves modeling energy yield under dif- ferent degradation scenarios to identify tolerable degradation rates. Qian et al. [16] introduced a method that separates the degradation rates of perovskite (*𝑘𝑝𝑒𝑟*) and silicon (*𝑘𝑠𝑖𝑙*). In Qian’s approach both *𝑘𝑝𝑒𝑟* and *𝑘𝑠𝑖𝑙*are assumed scenario based losses in output power without specifying the underlying degradation mechanisms. They found that *𝑘* *𝑝𝑒𝑟*values between 0.5% and 0.9% per year are acceptable for two- terminal PerSi cells to outperform c-Si cells. Moreover, they observed that a 2% absolute increase in tandem efficiency extends the tolerable *𝑘* *𝑝𝑒𝑟*by 1%. Similarly, Orooj and Paetzold [17] adjusted parameters in the equiv- alent circuit of a PerSi tandem cell to study their effects on standard test conditions (STC) and energy yield (EY). They found that degradation in the short-circuit current density of the perovskite subcell had the

∗ Corresponding authors. *E-mail addresses:* Y.Blom@tudelft.nl (Y. Blom), M.R.Vogt@tudelft.nl (M.R. Vogt).

[https://doi.org/10.1016/j.solmat.2026.114169](https://doi.org/10.1016/j.solmat.2026.114169)

Available online 28 January 2026 Received 7 July 2025; Received in revised form 11 November 2025; Accepted 7 January 2026

0927-0248/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

*Y. Blom et al.* greatest impact on tandem performance. Additionally, they identified the tolerable degradation rates for the different degradation scenarios. Lastly, Aydin et al. [18] conducted a simplified Levelized Cost of Electricity analysis to determine acceptable degradation rates for PerSi tandems. They concluded that if the tandem degradation rate is 2% per year and there are no additional costs compared to c-Si modules, the module efficiency must exceed 32% to remain competitive. While these studies offer valuable insights into tolerable *𝑘𝑝𝑒𝑟*values, none accounts for climate dependency in degradation rates. Given that *𝑘* *𝑠𝑖𝑙*varies across different climates [19], it is likely that *𝑘𝑝𝑒𝑟*tolerances also vary by location. Moreover, in two-terminal PerSi tandem cells, where the voltages of both subcells are combined, a single degradation rate is insufficient to describe performance loss, as shown in Appendix
A. In this work, we propose a new approach to determine tolerable *𝑘* *𝑝𝑒𝑟*values. We develop an analytical model for the silicon bottom cell, fitting and validating it with experimental data. A scenario-based approach is then used to model degradation in the perovskite cell. By simulating EY for various *𝑘𝑝𝑒𝑟*values, we identify tolerable rates across different locations. Additionally, a simplified model is developed that can predict the tolerable degradation rates without performing the computationally intensive simulations. Finally, we examine how tolerable *𝑘𝑝𝑒𝑟*values change with higher cell efficiencies and assess the environmental impact of PerSi and c-Si modules. It is important to note that this study only covers the analysis for monotlithic two-terminal (2T) PerSi modules, as these devices are most similar to the single junction reference modules. Future work can be done to explore how the tolerable degradation rate changes for different terminal configurations.
## 2. Methodology

To identify tolerable values for *𝑘𝑝𝑒𝑟*, we extend the PVMD Tool- box [20] by developing a methodology to simulate degradation. The PVMD Toolbox is a modeling framework designed to predict the EY of various PV systems by simulating key aspects of their performance. The simulation process begins by calculating the optical response of each subcell for the relevant wavelength range (300–1200 nm), which helps determine the incoming irradiance. This irradiance data is then used to calculate the temperature of each cell throughout the year. Finally, the electrical performance is simulated to obtain the EY of the PV module and the system afterwards. Full details and validation of the PVMD Toolbox have been documented in previous studies [20–23]. To predict the lifetime energy yield (LEY) of a PV system, we extend the annual PVMD simulation by adjusting input parameters to account for degradation. Fig. 1a illustrates the degradation modeling methodology. We use an analytical model to simulate degradation in the silicon bottom cell, encapsulation, and contact resistance. Since these com- ponents are similar to those in single-junction c-Si modules, available outdoor data can be used to calibrate the model effectively. For the perovskite top cell, a different approach is required. Due to the lack of large-scale outdoor data for perovskite modules, we adopt a scenario-based approach. The simulation of the top cell is adjusted based on three different scenarios to explore tolerable degradation rates. The performance of the top and bottom cell is modeled using a one-diode equivalent circuit model with two resistors [24–27]. The behavior of this model can be described with 5 parameters, namely the photo-generated current (*𝐼𝑝ℎ*), the diode saturation current (*𝐼₀*), the diode ideality factor (*𝑛*), the shunt resistance (*𝑅𝑠ℎ𝑢𝑛𝑡*), and the series resistance (*𝑅𝑠*). To simulate a tandem cell, both circuits are connected in series with an additional resistor to represent the interconnection (*𝑅𝑐𝑜𝑛*).

*Solar Energy Materials and Solar Cells 299 (2026) 114169*

### 2.1. Analytical modeling

In literature, various analytical models have been developed to pre- dict performance loss in c-Si modules [28,29]. However, these models typically produce only a single value for *𝑘* without distinguishing be- tween losses in voltage or current. For this reason, they are unsuitable for tandem devices. To address this limitation, we develop a new analytical model that not only provides *𝑘* but also simulates losses in the absorption profile and the current–voltage (IV) curve. This model accounts for different degradation types and stress factors, simulating their impact on module performance through analytical equations. The degrada- tion mechanisms included in this model are discoloration, moisture- induced degradation (MID), thermal cycling-induced degradation (TC), and light-induced degradation (LID), as these mechanisms are most severe or occurring most frequently [30,31]. Certain effects, such as hotspots, potential-induced degradation, and soiling, are excluded from this study as they are not compatible with the modeling approach. Hotspots are due to current inhomogeneity within the cells, which can result from partial shading or wafer im- purities [32]. However, since the PVMD Toolbox assumes all cells are identical and, in this study, considers an unobstructed horizon, hotspot effects cannot be incorporated into the model. Similarly, PID occurs due to a potential difference between the module frame and the active circuit, which can reach up to 1500 V when multiple modules are connected in series [33]. This phenomenon cannot be captured in the simulations, as the model considers only the direct current (DC) performance of a single module, where such high potential differences are not present. Finally, the effect of soiling [34] has also been excluded from this model, as rainfall is not included as input parameter of the PVMD Toolbox, and cleaning strategies would need to be considered, making it a complex degradation mechanisms to model. It would be interesting for future work, however, to study how soiling impacts the current matching in tandem devices, as soiling effects are not the same across all wavelengths [35]. Nevertheless, the exclusion of these mechanisms does not lead to an underestimation of degradation, as the final calibration is based on real-world outdoor PV system data. Moreover, similar analytical models in the literature [28,29] also do not account for these more complex degradation mechanisms. Each degradation mechanism is characterized by its stress factors, time profile, and impact on the module. Fig. 1b provides an overview of the degradation mechanisms considered in this study. The stress factors considered in the model are ultraviolet (UV) irradiance, the temperature of the module (*𝑇*), the relative moisture content (RMC), and the photo-generated current (*𝐽𝑝ℎ*). Another important characteristic is the time profile of a degradation mode. Degradation rates are not nec- essarily constant over time; they may increase or decrease throughout the module’s lifespan [36], as will be shown later in Fig. 7. Finally, the degradation modes are characterized by which part of the module they affect. For each mechanism, a separate degradation rate *𝑘𝑖*is calculated. To obtain the power loss (*𝑃𝑙𝑜𝑠𝑠,𝑖*) solely due to a mechanism *𝑖*, we use *𝑡* *𝑃* *𝑙𝑜𝑠𝑠,𝑖*(*𝑡*) = ∫ *𝑘𝑖*(*𝜏*)*𝑑𝜏.* (1) 0

It should be realized that all mechanisms affect the performance differently at the same time. This means that the total *𝑃𝑙𝑜𝑠𝑠*does not necessarily equal the sum of the individual power losses.

#### 2.1.1. Discoloration

The encapsulant in PV modules, typically made of ethylene vinyl ac- etate (EVA) or polyolefin (POE) [37], undergoes color changes over its lifetime. Exposure to UV radiation can alter the encapsulant’s chemical composition, impacting the optical performance of the device [38].

**Fig. 1.** (a) An overview of the methodology, where a scenario-based approach is used for degradation in the top cell, and an analytical approach is used for

the bottom cell, encapsulant, and contact resistance. (b) An overview of the degradation mechanisms considered for the analytical model, including their stress

factors, time profile, and effect on the module. MID, TC, LID, and RMC stand for moisture-induced degradation, thermal cycling, light-induced degradation, and

relative moisture content.

**Fig. 2.** The change in *𝑁*(*𝜆*) and its effect on the absorption profile for different values of *𝑃𝑙𝑜𝑠𝑠*, solely due to discoloration.

To predict the performance loss due to discoloration, we use the modified Arrhenius equation from Sinha et al. [39], which calculates the discoloration degradation rate (*𝑘𝑑𝑖𝑠*) as: <u>−𝐸𝑎,𝑑𝑖𝑠</u> *𝑛𝑑𝑖𝑠* *𝑘* *𝑑𝑖𝑠*= *𝐴𝑑𝑖𝑠*⋅ *𝑒 𝑘*⋅*𝑇* ⋅ (UV)*,* (2)

where *𝐴𝑑𝑖𝑠*, *𝐸𝑎,𝑑𝑖𝑠*, and *𝑛𝑑𝑖𝑠*are the pre-exponential factor, the activation energy, and the exponent related to the discoloration, respectively, and *𝑘* is the Boltzmann constant. Based on the findings in literature, we assume *𝑛𝑑𝑖𝑠*to be 1 [40] and *𝐸𝑎,𝑑𝑖𝑠*to be 0.39 eV [39]. The value of *𝐴𝑑𝑖𝑠*is determined through calibration later in this section. The amount of UV is defined as all in-plane irradiance with a wavelength smaller than 400 nm [41]. Although the UV and *𝑇* have seasonal fluctuations, they are approximately similar for all years. Therefore *𝑘𝑑𝑖𝑠* is constant throughout the lifetime of the PV module, being consistent with literature [36]. Since discoloration affects the encapsulant’s optical properties, we model performance loss by adjusting the refractive index (*𝑁*(*𝜆*) = *𝑛*(*𝜆*) + *𝑖* ⋅ *𝑘*(*𝜆*)) of the encapsulant in the EY simulations. The PVMD Toolbox uses *𝑁*(*𝜆*) for each material to calculate the device’s optical response [20]. To model changes in the refractive index due to discoloration, we use data from Meena et al. [42], who measured variations in internal quantum efficiency and reflection spectra of discolored modules. The full details of the procedure for calculating *𝑁*(*𝜆*) are provided in Ap- pendix B. Fig. 2 illustrates different *𝑁*(*𝜆*) for different values of *𝑃𝑙𝑜𝑠𝑠*and the corresponding the optical response. This change in optical response will then also have an impact on the thermal and electrical simulation step of the PVMD Toolbox.

#### 2.1.2. Moisture induced degradation

Moisture ingress in PV modules can trigger various degradation modes, such as delamination and corrosion [43,44]. While these mech- anisms are distinct, it is challenging to separate them due to their same stress factor. Therefore, their effects are combined in our analysis. To quantify the amount of degradation due to MID (*𝑘𝑀𝐼𝐷*), the Peck model is used [11,28,29,45]: <u>𝐸𝑎,𝑀𝐼𝐷</u> *𝑘* = *𝐴* ⋅ *𝑒* −*𝑘*⋅*𝑇* ⋅ (RMC) *𝑛𝑀𝐼𝐷* *,* (3) *𝑀𝐼𝐷 𝑀𝐼𝐷* where *𝐴*, *𝐸*, and *𝑛* are the pre-exponential factor, the acti- *𝑀𝐼𝐷 𝑎,𝑀𝐼𝐷 𝑀𝐼𝐷* vation energy, and the exponent related to MID, respectively. The RMC is the relative moisture content that describes the amount of moisture that has entered the module compared to the saturation concentration of the encapsulant. In previous work, a model has been developed to simulate and predict the RMC over time for different climates [45]. The values for *𝐸𝑎,𝑀𝐼𝐷*and *𝑛𝑀𝐼𝐷*are assumed to be 0.809 eV and 1.87 based on previous work [45], and *𝐴𝑀𝐼𝐷*will be used for calibration. Since moisture ingress is a gradual process, RMC increases over time. As a result, the degradation rate *𝑘𝑀𝐼𝐷*also increases throughout the module’s lifetime, consistent with literature findings [36]. As MID affects both the electrical and optical properties of PV mod- ules, its impact is simulated by adjusting the diode model parameters of the c-Si bottom cell. Zhu et al. [46] conducted damp heat tests to measure the effects of moisture ingress on IV curves. They also identi- fied how the parameters of the equivalent circuit model change due to moisture exposure. These trends are used to adjust the simulation of c- Si performance, incorporating the associated performance loss. Fig. 3a illustrates the changes in the IV curve for different values of *𝑃𝑙𝑜𝑠𝑠*caused by MID. More information on the calculation of circuit parameters is provided in Appendix C.

**Fig. 3.** The effect on the IV curve of different values of *𝑃𝑙𝑜𝑠𝑠*, solely due to MID (a), TC (b), and LID (c).

**Table 1**

An overview of the datasets that are used for the calibration and validation of

the analytical model, and the calibrated values for the remaining parameters

for each parameter set.

Location Years Source *𝐴* *𝑑𝑖𝑠𝐴* *𝑀𝐼𝐷𝐴* *𝑇 𝐶𝐴* *𝐿𝐼𝐷* −2] [%/y] [%/y] [%/y] [C m 8 −5 7 Alice Springs 16 DKA [57] 0.0556 1*.*03 × 10 4*.*65 × 10 1*.*23 × 10 (Australia) 8 −5 7 Pfaffstäten 6 Lindig [58] 1.084 3*.*72 × 10 9*.*71 × 10 1*.*70 × 10 (Austria) Cocoa 6 NREL [59] 0.0677 6*.*10 × 1071*.*23 × 10−48*.*19 × 105 (USA) Grimstad 20 Segbefia [60] 0.2645 9*.*61 × 1072*.*11 × 10−57*.*53 × 106 (Norway) Borlänge 30 Psimopoulos [61] 0.1198 1*.*92 × 1084*.*96 × 10−51*.*12 × 106 (Sweden)

#### 2.1.3. Thermal cycling

In addition to the absolute temperature influencing Arrhenius pro- cesses in discoloration and MID, temperature fluctuations over time introduce additional degradation mechanisms. High-temperature vari- ations, combined with mismatches in the thermal expansion coeffi- cients of different materials, cause layers to expand at different rates, leading to thermomechanical stress on the interconnections [47,48]. Bosco et al. [49] proposed an analytical equation that can describe the damage due to TC (*𝐷𝑇 𝐶*), written as

*𝑛𝑇 𝐶 𝑏* − <u>𝐸𝑎,𝑇 𝐶</u> *𝐷𝑇 𝐶*= *𝐴𝑇 𝐶*⋅ (*𝛥𝑇*) ⋅ *𝑅* ⋅ *𝑒 𝑘*⋅*𝑇,* (4)

where *𝐴𝑇 𝐶*, *𝐸𝑎,𝑇 𝐶*, and *𝑛𝑇 𝐶*are the pre-exponential factor, the activa- tion energy, and the exponent related to TC, respectively, *𝛥𝑇* is the average daily temperature fluctuation, *𝑅* is the number of times the temperature has fluctuated, and *𝑏* is an exponent to *𝑅*. The values for *𝐸𝑎,𝑇 𝐶*, *𝑛𝑇 𝐶*, and *𝑏* are assumed to be 0.12 eV, 1.9, and 0.33 as calibrated by N. Bosco et al. [49], and *𝐴𝑇 𝐶*will be used for final calibration. As Eq. (4) outputs the total amount of damage instead of a degra- dation rate, the degradation rate due to TC (*𝑘𝑇 𝐶*) can be obtained iteratively with ∑*𝑡*−1 <u>𝐷𝑇 𝐶(𝑡) −𝜏=1𝑘𝑇 𝐶(𝜏) ⋅ 𝛥𝑡</u> *𝑘* *𝑇 𝐶*(*𝑡*) =*,* (5) *𝛥𝑡* where *𝛥𝑡* is the time step. Given that *𝑏* is equal to 0.33 and *𝑅* will constantly increase over time, *𝐷𝑇 𝐶*will keep rising but at a slower pace, causing *𝑘𝑇 𝐶*to decrease over time. The time profile of both the damage and *𝑘𝑇 𝐶*and the definition of *𝛥𝑇* are shown in Appendix D. It should be noted that Eq. (5) applies only for *𝑡 >* 0. *𝑘𝑇 𝐶*(0) is defined to be 0%/year. Since TC degradation primarily affects the contacts [47–49], we adjust the value of *𝑅𝑐𝑜𝑛*to simulate the required *𝑃𝑙𝑜𝑠𝑠*. Fig. 3b illustrates the impact of TC degradation on the IV curve.

#### 2.1.4. Light induced degradation

The final degradation mechanism considered is light-induced degra- dation (LID), where the efficiency of the solar cell decreases due to prolonged exposure to light. According to literature, this is attributed to an increase in the minority carrier lifetime (*𝜏𝑚𝑖𝑛*) within the solar cell [50–52], with the *𝐽𝑝ℎ*acting as the stress factor [53,54]. Experimental studies have demonstrated that *𝜏𝑚𝑖𝑛*decays exponen- tially with exposure to *𝐽𝑝ℎ*and eventually saturates at a constant value [54,55]. This time-dependent behavior of *𝜏𝑚𝑖𝑛*(*𝑡*) can be modeled as: <u>− ∫0</u>*𝑡* <u>𝐽𝑝ℎ(𝜏)𝑑𝜏</u> *𝜏* *𝑚𝑖𝑛*(*𝑡*) = *𝜏𝑚𝑖𝑛,*∞+ (*𝜏𝑚𝑖𝑛,*− *𝜏𝑚𝑖𝑛,*∞) ⋅ *𝑒* *𝐴𝐿𝐼𝐷,* (6)

where *𝜏𝑚𝑖𝑛,*and *𝜏𝑚𝑖𝑛,*∞are the minority carrier lifetime initially and after saturation, and *𝐴𝐿𝐼𝐷*is the decay constant for LID.

Since *𝜏𝑚𝑖𝑛*and *𝐼₀* are inversely proportional [56], the value of *𝐼₀* can be adjusted using <u>𝐼</u> *𝐼₀*(*𝑡*) = <u>0,𝑖𝑛𝑖𝑡</u> *,* (7) *𝐶𝜏*(*𝑡*) where *𝐼₀,𝑖𝑛𝑖𝑡*is the initial value of *𝐼₀* and *𝐶𝜏*(*𝑡*) is the ratio of *𝜏𝑚𝑖𝑛*(*𝑡*) over *𝜏* *𝑚𝑖𝑛,*0, written as <u>− ∫</u> *𝑡* <u>𝐽 (𝜏)𝑑𝜏</u> *𝐶* (*𝑡*) = <u>𝜏</u> <u>𝑚𝑖𝑛(𝑡)</u> = *𝐶* + (1 − *𝐶*) ⋅ *𝑒* <u>0</u> *𝐴𝐿𝐼𝐷* <u>𝑝ℎ</u> *,* (8) *𝜏* *𝜏* *𝑚𝑖𝑛,*0 *𝜏,*∞ *𝜏,*∞

where *𝐶* is <u>𝜏𝑚𝑖𝑛,∞</u>. Based on measurements in literature [55], *𝐶* is *𝜏,*∞ *𝜏𝑚𝑖𝑛,* 0 *𝜏,*∞ assumed to be 0.5, and *𝐴𝐿𝐼𝐷*is used for calibration. The effect of LID on the IV curve is shown in Fig. 3c. In contrast to the other degradation mechanisms, there is no direct analytical equation for the degradation rate due to LID (*𝑘𝐿𝐼𝐷*(*𝑡*)). Instead, it can be derived from the change in power output as

1 − <u>𝑃 (</u> <u>𝑃𝑡</u> <u>+</u> <u>(𝑡𝛥𝑡) )</u> *𝑘* *𝐿𝐼𝐷*(*𝑡*) = *𝛥𝑡* *,* (9)

where *𝑃* (*𝑡*) is the output power at time *𝑡*, excluding the other losses.

#### 2.1.5. Calibration and validation

Each degradation mechanism considered has one parameter that can be used to calibrate the models based on outdoor measurements. For this calibration process, we rely on measured outdoor data from various PV systems reported in the literature. Table provides an overview of the datasets selected for this calibration. For each dataset, the data was filtered and normalized to obtain the normalized power (*𝑃𝑛𝑜𝑟𝑚*(*𝑡*)) for each operating year. Full details of the filtering and normalization process are provided in Appendix

**Fig. 4.** (a) The calibration and validation of the analytical model for the different datasets. (b) A validation of the analytical model on the effect of degradation

on the IV curve.

E. Calibration was performed separately for each dataset, resulting in different values for *𝐴𝑑𝑖𝑠*, *𝐴𝑀𝐼𝐷*, *𝐴𝑇 𝐶*, and *𝐴𝐿𝐼𝐷*. This variation can be attributed to differences in module characteristics, as the degradation parameters are not identical across systems. Fig. 4a shows the calibra- tion results for all datasets, demonstrating that the analytical model accurately captures the temporal trends of *𝑃𝑛𝑜𝑟𝑚*for each site. To further validate the methodology, we assessed its ability to predict changes in the IV curve. Two studies have been found that reported the change in IV curve after 20 or 30 years of operation. Fig. 4b compares the predicted and measured IV curves of both studies, showing that the analytical model successfully captures the loss in IV performance. The results presented in this work are obtained by using the pa- rameters calibrated with the PV system in Alice Springs. The reason for selecting this dataset is that it has continuously reported the output power of the PV module for the longest time period. To see how using different parameters affect the results, Appendix F shows a sensitivity analysis. This sensitivity analysis contains the result of Fig. 9, obtained with different sets of parameters. It can be seen that the choice of parameter set can significantly change the values of *𝑘𝑡𝑜𝑙*, but the same trends and relative differences are present for all sets.
### 2.2. Scenario modeling

Degradation in the top cell is simulated using a scenario-based approach. Specifically, we introduce performance loss in the perovskite cell by adjusting parameters in the electrical model, following methods similar to those used by Qian et al. [16] and Orooj et al. [17]. To examine the effect on different degradation trends, three scenarios are considered where there is a loss in short circuit current (*𝐼𝑠𝑐*), open circuit voltage (*𝑉𝑜𝑐*), and fill factor (FF). These scenarios are simulated by adjusting *𝐼𝑝ℎ*(for *𝐼𝑠𝑐*degradation), *𝐼₀* (for *𝑉𝑜𝑐*degradation), and both *𝑅𝑠ℎ*as well as *𝑅𝑠*(for FF degradation). It is important to realize that the degradation of a perovskite cell in practice is not a loss in a single component, but rather a combination of multiple losses due to different mechanisms. The reason for analyzing these extreme cases is to establish a range of tolerable degradation rates that encompasses all possible degradation scenarios. If a real- world scenario involves a combination of the tested cases, its tolerable degradation rate will fall somewhere between the values derived in this study.

Fig. 5 illustrates the impact of these scenarios on the IV curve

for various values of *𝑃𝑙𝑜𝑠𝑠*. To simulate lifetime degradation, different constant values for *𝑘𝑝𝑒𝑟*are applied. To indicate a specific degradation scenario, the notation *𝑘𝑝𝑒𝑟,𝑋*, where *𝑋* can be *𝐼𝑠𝑐*, *𝑉𝑜𝑐*or *𝐹 𝐹*, is used. The corresponding *𝑃𝑙𝑜𝑠𝑠*for the top cell is calculated using Eq. (1), enabling the necessary adjustments to the IV curve. It should be noted that this scenario based approach only considers fixed degradation rates over the lifetime of the PV module. This means that non-linear trend in the degradation of the perovskite cell are not captured by this method.

### 2.3. Calculating the relative environmental impact

The methodology considered so-far only allows to make compar- isons between single junction and tandem devices in terms of energy yield. However, to develop truly sustainable PV modules, it is essential to also consider the environmental impact of both technologies. To include the environmental impact of both technologies, we use the results from Roffeis et al. [62] who reported the absolute envi- ronmental impacts of single-junction c-Si and PerSi tandem modules, covering 13 impact categories listed in Table 2. It should be noted that both modules have the same module area, but a different output power. Interestingly, the PerSi module has a lower environmental impact for the impact category human toxicity and marine ecotoxicity. This is because 37% less silver is used for the metallization process of the PerSi module, as explained by Roffeis et al. The silver reduction is enabled by the fact that tandem modules have about 50% lower currents as compared to Si single junction modules [62]. While these absolute environmental impact values (*𝐸𝐼𝑎𝑏𝑠*) are infor- mative, it is more meaningful to compare their relative environmental impacts (*𝐸𝐼𝑟𝑒𝑙*) by accounting for differences in energy production. We compute *𝐸𝐼𝑟𝑒𝑙*using the formula <u>𝐸𝐼𝑎𝑏𝑠</u> *𝐸𝐼𝑟𝑒𝑙*=*,* (10) LEY where LEY is calculated with the methodology described above. The values for *𝐸𝐼𝑟𝑒𝑙*can be used to assess for which degradation rates tandem modules have a lower environmental impact than single junction devices.

The effect on the IV curve of the perovskite subcell due to different degradation scenarios.

**Fig. 5.**

**Table 2**

The absolute environmental impact per module in different categories for the

c-Si and PerSi tandem module.

*Source:* These values are obtained from literature [62].

|Impact category|Unit|c-Si|PerSi|
|---|---|---|---|
|Climate change, default|kg CO2 eq.|411|434|
|Particulate matter formc|g PM2.5 eq.|644|684|
|Fossil depletion|kg oil eq.|157|164|
|Freshwater consumption|m³|14|14|
|Freshwater ecotoxicity|kg 1,4 DB eq.|4|4|
|Freshwater eutrophication|g P eq.|209|210|
|Human toxicity, non-cancer|kg 1,4 DB eq.|440|421|
|Ionizing radiation|kBq Co-60 eq.d|70|71|
|Marine ecotoxicity|kg 1,4 DB eq.|6|5|
|Marine eutrophication|g N eq.|29|31|
|Metal depletion|g Cu eq.|1900|2034|
|Terrestrial acidification|g SO2 eq.|1510|1577|

## 3. Case studies

The proposed methodology can be used to determine tolerable values for *𝑘𝑝𝑒𝑟*of a tandem PV module at different locations using a c-Si PV module as reference. This section outlines the module speci- fications and the selected geographical locations. For this study only monolithic 2T PerSi modules are considered. The reason for excluding other terminal configurations, such as three- or four-terminal devices, is that there cell and module design is significantly different than the reference c-Si module.

### 3.1. PV module

The PV module comprises 144 half-cut PerSi tandem cells with a G12 wafer size, connected in butterfly topology with three bypass diodes. The cell design is based on the 32.5% efficient 2T PerSi cell developed by S. Mariotti et al. [63], which has been integrated and validated in the PVMD Toolbox in previous studies [21,22]. Similar to those previous studies, a layer of encapsulant and glass is included to simulate realistic modules. Fig. 6 illustrates the optical structure, absorption profile, and module IV curve for both the reference c-Si as the PerSi module. The module has an output power of 948 W and a total area of 3.38 m², meaning the module has a module efficiency of

28.0%. The reference c-Si module is derived from the bottom cell of the PerSi device shown in Fig. 6. It also consists of 144 half-cut cells with a G12 wafer size, utilizing the same bottom-cell design as the PerSi device. Both modules consists of monofacial cells, and have a polyethylene terephthalate (PET) backsheet, being similar to modules in previous work [45]. Also, there is an anti-reflection coating (ARC) and an
amorphous fluoropolymer (AF) layer on top of the glass to further improve the optical performance.

### 3.2. Operating conditions

Different geographical locations are selected for which the accept- able values of *𝑘𝑝𝑒𝑟*are found. These distinct locations represent different climates according to the Koppen-Geiger-Photovoltaics *̈* (KGPV) classifi- cation [64,65] and a machine learning based PV climate classification (ML-PV) [66]. Table 3 shows the annual Global Horizontal Irradiance (GHI), weighted average ambient temperature (*𝑇𝑎*), average relative humidity (RH), KGPV classification, and the module tilt.

## 4. Results

We apply the outlined methodology to calculate the Lifetime Energy Yield (LEY) of different modules across four different locations. First, we simulate the performance of the c-Si modules with the analytical model to calculate the modules’ lifetime for all locations and their LEY. Next, we calculate the LEY of PerSi modules for all nine scenarios and different values of *𝑘𝑝𝑒𝑟*, identifying the maximum tolerable degradation rate. We also factor in the environmental impact of both c-Si and PerSi modules. By considering both energy yield and environmental impact, we determine the values of *𝑘𝑝𝑒𝑟*that make PerSi modules more sustainable compared to their c-Si counterparts. Finally, we propose a simplified model that can predict the maximum tolerable degradation rate.

### 4.1. Reference lifetime energy yield of c-Si modules

To determine the module lifetimes for different locations, we use the analytical model to calculate the degradation rates for all mecha- nisms. As illustrated in Fig. 7, Lagos exhibits the highest degradation rates due to its high temperatures and humid climate, as indicated in

Table 3. Conversely, the modules in Delft demonstrate the longest life-

times, thanks to the area’s lower ambient temperatures. The obtained time profiles of each degradation mechanism align well with the time profiles from literature presented in Fig. 1b. Based on the simulated degradation rates and the applied method- ology, we compute the normalized power (*𝑃*) over time, as depicted *𝑛𝑜𝑟𝑚* in Fig. 7. The module lifetime, defined as the time it takes to reach 80% of the original power output (*𝑇₈₀*), is also shown on top of the figure. Due to the elevated degradation rates, Lagos has the shortest module lifetime at 13 years. Shanghai and Lisbon follow with similar lifetimes of 26 and 30 years, respectively. Delft, benefitting from its favorable environmental conditions, achieves the longest lifetime of 48 years. It should be noted that similar differences in module lifetime across climates were also found in other studies [28]. The LEY of the modules is calculated by integrating the annual energy yield over time till the module lifetime *𝑇₈₀*.

**Fig. 6.** The optical structure (a), the absorption profile (b), and the IV curve (c) of the simulated PV module.

**Table 3**

The characteristics of the selected locations. The ambient temperature is weighted with the global horizontal

irradiance [21]. This metric is chosen as it, in our opinion, better represents the operating conditions of the PV

modules than the normal average of the ambient temperature. The selected module tilts are chosen such that

they maximize the annual front-side irradiation for each location. For acronyms in KGPV and ML-PV climates,

we refer to [65,66].

|Location|Annual global horizontal|Weighted average ambient|KGPV|ML-PV|Optimal module|
|---|---|---|---|---|---|
||irradiation [kW h m|−2] temperature [ ◦ C]|||tilt [ ◦]|
|Delft|1018|16.2|DL|Tem1|31|
|Lagos|1642|29.4|AH|Tro2|5|
|Lisbon|1758|20.6|DH|Tem5|28|
|Shanghai|1271|21.7|DM|Tro1|17|

**Fig. 7.** The degradation rates of the different degradation mechanisms in all locations. Also, the normalized power is plotted such that *𝑇₈₀* can be determined.

### 4.2. Tolerable degradation rates

To determine the tolerable value for *𝑘𝑝𝑒𝑟*, we employ both the ana- lytical and scenario-based models to calculate the LEY of PerSi modules. For a fair comparison, we use the same module lifetime as calculated for c-Si modules to determine the LEY. As an example, Fig. 8a illustrates the annual EY of the PerSi module in Delft under *𝐼𝑠𝑐*degradation for different values of *𝑘𝑝𝑒𝑟*. As *𝑘𝑝𝑒𝑟*increases, the EY declines more rapidly over the module’s lifetime due to faster performance degradation.

Fig. 8b integrates the energy production over the module’s lifetime

to determine the LEY, with the dashed line representing the LEY of c-Si modules. The LEY of PerSi modules decreases as *𝑘𝑝𝑒𝑟*increases, indicating a specific threshold value, denoted as *𝑘𝑡𝑜𝑙*. Similar to *𝑘𝑝𝑒𝑟,𝑋*, *𝑘* *𝑡𝑜𝑙,𝑋*is used to indicate a specific degradation scenario. This value represents the maximum allowable *𝑘𝑝𝑒𝑟*for PerSi devices in order to outperform c-Si modules. This process is repeated for each location and degradation scenario to calculate *𝑘𝑡𝑜𝑙*under various conditions. Fig. 9 presents the LEY for different values of *𝑘𝑝𝑒𝑟*for all PerSi modules, along with the corre- sponding *𝑘𝑡𝑜𝑙*values. It should be noted that LEY is simulated only for integer values of *𝑘𝑝𝑒𝑟*and the intermediate values are found via linear interpolation.

Across all locations, degradation in *𝐼𝑠𝑐*yields the lowest *𝑘𝑡𝑜𝑙*(1.2% per year for Delft) as two-terminal modules require current matching between subcells. As a result, current losses are more harmful than voltage losses. This also explains why *𝑘𝑡𝑜𝑙*values for *𝐹 𝐹* degradation are lower than those for *𝑉𝑜𝑐*degradation, as fill factor losses affect both current and voltage. Another key observation is that *𝑘𝑡𝑜𝑙*is inversely linked to *𝑇₈₀*. In Delft, where there is a high module lifetime, the perovskite top cell needs to be very stable as a degradation rate of only 1.9% can be tolerated. On the other hand, in Lagos, where the module lifetime is short, a larger perovskite degradation rate of 7.6% can be tolerated. This occurs because the total degradation in the perovskite cell (*𝑘𝑡𝑜𝑙*⋅ *𝑇₈₀*) remains approximately constant across locations. Consequently, locations with lower *𝑇₈₀* have larger *𝑘𝑡𝑜𝑙*values, as the modules last shorter at that location anyway, meaning perovskite degradation is less of an issue.

### 4.3. Effect of higher efficiency

The PV module used in the simulations is based on a 32.5% efficient PerSi tandem cell, resulting in a module efficiency (*𝜂𝑚𝑜𝑑*) of 28.0%.

**Fig. 8.** An example for identifying the tolerable degradation rate *𝑘𝑡𝑜𝑙,𝐼𝑠𝑐*for the modules in Delft. (a) shows the annual EY of the c-Si and PerSi modules for

different values of *𝑘𝑝𝑒𝑟,𝐼𝑠𝑐*. (b) shows the integrated LEY, such that *𝑘𝑡𝑜𝑙,𝐼𝑠𝑐*can be determined for the case of Delft.

**Fig. 9.** The LEY for different values of *𝑘𝑝𝑒𝑟*and the corresponding *𝑘𝑡𝑜𝑙*for each location and degradation mechanism.

However, (*𝜂𝑚𝑜𝑑*) could be higher, as the practical efficiency limit of PerSi technology is 39.5% [3]. An increase in efficiency would enhance the energy yield (EY) for tandem modules, which could in turn impact *𝑘* *𝑡𝑜𝑙*. To explore this effect, we repeat the previously described procedure using modules with higher efficiencies. The performance of the per- ovskite cell is artificially improved, as illustrated in Fig. 10, achieving a module efficiency of up to 32.9%. Details of these performance enhancements are provided in Appendix G. The higher-efficiency modules are labeled according to their respec- tive efficiencies. Fig. 11 presents the corresponding *𝑘𝑡𝑜𝑙*values for all modules across different locations and efficiency levels, showing a clear influence of *𝜂𝑚𝑜𝑑*on the tolerable degradation rate. For instance, in Delft, the *𝑘𝑡𝑜𝑙*for *𝐼𝑠𝑐*degradation increases from

1.2% to 1.9% per year, representing a relative increase of nearly 50%. This same approximate increase is observed in other locations and degradation scenarios. The highest *𝑘𝑡𝑜𝑙*is found in Lagos for *𝑉𝑜𝑐*
degradation, primarily because lower module lifetimes lead to higher *𝑘* *𝑡𝑜𝑙*, and voltage degradation is less harmful than current degradation. Overall, these simulations quantify by how much the tolerable degradation rate under expands with improving module efficiency. This illustrates that higher efficiency not only boosts energy production but can also loosen the stability requirements of the perovskite cell. As mentioned in Section 2.2, practical degradation scenarios will most likely not be a loss solely in *𝐼𝑠𝑐*, *𝑉𝑜𝑐*, or *𝐹 𝐹*, but a combination of them. The presented results can be used to create a window of tolerable degradation rates for the perovskite cell at different module efficiencies, as shown in Fig. 12. As mentioned before, degradation in current is most harmful for 2T tandem cells and degradation in voltage is least harmful, meaning these scenarios function as two extreme scenarios. Therefore, the tolerable degradation rate for any possible scenario is in between *𝑘𝑡𝑜𝑙,𝐼𝑠𝑐*and *𝑘𝑡𝑜𝑙,𝑉 𝑜𝑐*, indicated with the gray area in Fig. 12. This figure shows what is the minimum and maximum value for *𝑘𝑡𝑜𝑙*at different locations and module efficiencies.

**Fig. 10.** (a) The cell performance of perovskite subcells with increasing quality. The separate perovskite subcells can reach an efficiency of 24.1%. (b) The module

performance with increasing perovskite efficiencies.

**Fig. 11.** The effect of the module efficiency on *𝑘𝑡𝑜𝑙*. It can be seen that higher efficient modules have a larger tolerable degradation rate.

**Table 4**

The calibrated values for *𝑐𝑠𝑖𝑚*and *𝐸𝑎,𝑠𝑖𝑚*that are used in the simplified

model.

In practice, it is more practical to measure the degradation rate of a PerSi module rather than focusing specifically on the top cell. To identify a single tolerable degradation rate for the entire PerSi module,

|𝑐|[y|−1]|𝑐|[y|−1]|𝑐|[y|−1]|𝐸|[eV]|
|---|---|---|---|---|---|---|---|---|---|---|
|𝑠𝑖𝑚,𝐼|𝑠𝑐||𝑠𝑖𝑚,𝐹 𝐹|||𝑠𝑖𝑚,𝑉|𝑜𝑐||𝑎,𝑠𝑖𝑚||
|4. 71 × 10||11|5. 19 × 10||11|6. 85 × 10||11|0.743||

one can use the value of *𝑘𝑡𝑜𝑙,𝐼𝑠𝑐*as an approximation. Since the module consists of two-terminal cells, meaning its current is limited by the lowest subcell, any value of *𝑘𝑝𝑒𝑟,𝐼𝑠𝑐*will also translate into a similar module degradation rate.

### 4.4. Simplified model

The current methodology requires significant computational effort since energy yield must be calculated for each year and for various values of *𝑘𝑝𝑒𝑟*. To avoid these computationally-intensive simulations, a more streamlined approach is desirable. Therefore, we explore the potential of developing a simplified model to predict *𝑘𝑡𝑜𝑙*. Our proposed simplified model is an Arrhenius-based equation writ- ten as <u>−𝐸𝑎,𝑠𝑖𝑚⋅𝑞</u> *𝑘* *𝑡𝑜𝑙*= *𝑐𝑠𝑖𝑚*⋅ *𝜂𝑚𝑜𝑑*⋅ *𝑒* *𝑘*⋅*𝑇𝑎,* (11)

where *𝑐𝑠𝑖𝑚*is a pre-exponential constant that depends on the degrada- tion type, *𝐸𝑎,𝑠𝑖𝑚*is the activation energy of the simplified model, and *𝑇* *𝑎*is the weighted ambient temperature from Table 3. Although the physical degradation model accounts for multiple stress factors, the simplified model considers only temperature. This decision avoids the need for additional parameters that would require calibration. Given the limited dataset, including multiple factors could lead to overfitting, making a single-factor model more practical. The parameters *𝑐𝑠𝑖𝑚*and *𝐸𝑎,𝑠𝑖𝑚*are calibrated using the results from

Fig. 11, with the final values shown in Table 4.

**Fig. 12.** The window of tolerable degradation rates for the perovskite cell at different module efficiencies.

**Fig. 13.** The comparison between the predicted values for *𝑘𝑡𝑜𝑙*with the

simplified model and the simulated values with the detailed methodology.

To assess the accuracy of this approach, we apply the simplified model to predict *𝑘𝑡𝑜𝑙*values for the simulated scenarios. Fig. 13 com- pares these predicted values with the simulation results. The model performs well, achieving a root mean square error of 0.34% per year. This demonstrates that the simplified model provides accurate predic- tions for *𝑘𝑡𝑜𝑙*across all degradation scenarios and module efficiencies, making it a reliable tool for predicting *𝑘𝑡𝑜𝑙*under different climate conditions without detailed simulations.

### 4.5. Including the environmental impact

The values presented for *𝑘𝑡𝑜𝑙*indicate the maximum degradation rate at which PerSi devices achieve a larger LEY than c-Si modules. However, as mentioned before, it is essential to also consider the environmental impact of both technologies to make a good comparison. We use the approach outlined in Section 2 to identify the perovskite degradation rate at which the relative environmental impact of PerSi modules is lower than that of c-Si modules, denoted with *𝑘𝑡𝑜𝑙,𝐸𝐼*. Fig.

14 illustrates *𝑘𝑡𝑜𝑙,𝐸𝐼*across all impact categories and locations for PerSi modules with a 28% efficiency. The first row provides a reference value for *𝑘𝑡𝑜𝑙*when only considering LEY. In general, *𝑘𝑡𝑜𝑙,𝐸𝐼*values are lower than *𝑘𝑡𝑜𝑙*. This can be attributed to the more complex structure of PerSi cells, which require additional materials and production steps, thereby increasing their environmental footprint. Fig. 14 reflects this, showing a higher absolute environmental impact for PerSi modules despite their higher energy yield. Conse- quently, when PerSi devices achieve equal LEY to c-Si modules, their environmental impact relative to LEY is higher. Therefore, the tolerable degradation rates for environmental impact are generally lower than the one for LEY (*𝑘𝑡𝑜𝑙,𝐸𝐼< 𝑘𝑡𝑜𝑙,𝐸𝑌*) However, there are exceptions. In the categories Human Marine Ecotoxicity, PerSi devices exhibit lower absolute environmental impacts, resulting in higher *𝑘𝑡𝑜𝑙,𝐸𝐼*values compared to those based solely on LEY. Overall, the lowest *𝑘𝑡𝑜𝑙,𝐸𝐼*values are approximately 15% to 20% lower than when considering only LEY. This suggests that PerSi mod- ules with degradation rates below these minimum *𝑘𝑡𝑜𝑙,𝐸𝐼*values are more sustainable than c-Si devices across all considered environmental aspects.

## 5. Conclusion

In this work, we introduced a novel approach for simulating degra- dation in PerSi tandem modules by combining an analytical model for the bottom cell with a scenario-based model for the top cell. The analyt- ical model was validated using reported performance data from various outdoor PV modules. This methodology enabled us to determine the operational lifetime of c-Si PV modules across four different locations. We then identified the tolerable degradation rates for the perovskite cell, ensuring that the PerSi module continues to outperform the c-Si module. Various degradation scenarios were analyzed, with degrada- tion in *𝐼𝑠𝑐*found to be the most critical, resulting in the lowest *𝑘𝑡𝑜𝑙*. Notably, *𝑘𝑡𝑜𝑙*is inversely related to the module’s lifetime. In temperate climates where high module lifetimes can be achieved (Delft), the perovskite top cell needs to be very stable as a degradation rate of

**Fig. 14.** The values of *𝑘𝑡𝑜𝑙*when considering all environmental impact categories. The first row indicates the original calculate value for *𝑘𝑡𝑜𝑙*when only considering

). All results are obtained by using the original PerSi module with an efficiency of 28%.

LEY (*𝑘𝑡𝑜𝑙,𝐸𝑌*

only 1.9% can be tolerated. On the other hand, in humid/tropical climates (Lagos), where module lifetime anyway is short, a larger perovskite degradation rate of 7.6% can be tolerated. Additionally, we demonstrated that improving module efficiency can relatively increase *𝑘* *𝑡𝑜𝑙*by nearly 50%. To avoid the computationally intensive simulations, we introduced a simplified model that can predict the tolerable degradation rate. This Arrhenius-based model considers only module efficiency and ambient temperature. With a root mean square error of 0.34% per year, the model effectively and accurately predicts *𝑘𝑡𝑜𝑙*for different locations, offering a practical alternative for future analyses. Beyond considering only electricity production, we also factored in the environmental impact. *𝑘𝑡𝑜𝑙,𝐸𝐼*was calculated for different environ- mental categories, showing that using approximately 80% of the cal- culated *𝑘𝑡𝑜𝑙*from LEY ensures that PerSi modules are more sustainable across all aspects.

## CRediT authorship contribution statement

**Youri Blom:** Writing – original draft, Methodology, Investigation. **Rudi Santbergen:** Writing – review & editing, Supervision. **Olindo** **Isabella:** Writing – review & editing, Supervision. **Malte Ruben Vogt:** Writing – review & editing, Supervision, Methodology, Investigation.

**Declaration of Generative AI and AI-assisted technologies in the writing process**

During the preparation of this work the author used Copilot in order to paraphrase sentences and improve the language and readabil- ity. After using this tool/service, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication.

## Funding

This research did not receive any specific grant from funding agen- cies in the public, commercial, or not-for-profit sectors.

## Declaration of competing interest

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Appendix A. Limitation of single degradation value in a tandem device

As mentioned in the main text, the type of degradation (current or voltage loss) in a subcell influences the overall power loss (*𝑃𝑙𝑜𝑠𝑠*) differently. Fig. A.1 illustrates that a 10% current loss in the perovskite subcell results in an 8.7% power loss, while a 10% voltage loss leads to a 6.2% power loss. This shows that the degradation in both the perovskite and silicon subcell is relevant, and a single value for *𝑘* is not sufficient.

## Appendix B. Calculating changes in 𝑵(𝝀) due to discoloration

To model the effect of discoloration, we adjust the refractive index (*𝑛*(*𝜆*) + *𝑖* ⋅ *𝑘*(*𝜆*)) of the encapsulant layer via *𝑛* *𝑛𝑒𝑤*(*𝜆*) = *𝑛𝑜𝑟𝑖𝑔*(*𝜆*) + *𝛥𝑛*(*𝜆*) (B.1) *𝑘* *𝑛𝑒𝑤*(*𝜆*) = *𝑘𝑜𝑟𝑖𝑔*(*𝜆*) + *𝛥𝑘*(*𝜆*)*,* where *𝛥𝑛*(*𝜆*) and *𝛥𝑘*(*𝜆*) are the changes in refractive index. In order to calculate *𝛥𝑛*(*𝜆*) and *𝛥𝑘*(*𝜆*), we use the work of Meena et al. [42], who reported external quantum efficiency (*𝐸𝑄𝐸*) and the reflection of field aged modules, as shown in Fig. B.1. We begin by computing the change in parasitic absorption across all wavelengths. The spectral parasitic absorption (*𝐴𝑝𝑎𝑟*(*𝜆*)) accounts for photons absorbed without contributing to current generation and is defined as *𝐴𝑝𝑎𝑟*(*𝜆*) = 1 −*𝑅*(*𝜆*) − *𝐸𝑄𝐸*(*𝜆*). *𝐴𝑝𝑎𝑟*(*𝜆*) is calculated for both reference and field-aged modules, allowing us to obtain the difference in parasitic absorption (*𝛥𝐴𝑝𝑎𝑟*(*𝜆*)). To control the degradation level, we introduce a parameter *𝑐𝑑𝑖𝑠*, which scales *𝛥𝐴𝑝𝑎𝑟*(*𝜆*). We make the assumption that this additional parasitic absorption is only absorbed in the encapsulant. By using the Lambert–Beer law, we find the difference in absorption coefficient *𝛥𝛼*(*𝜆*) via −*𝛥𝛼*(*𝜆*)⋅*𝑑𝐸𝑉 𝐴* () (1 − *𝑅*(*𝜆*)) ⋅ *𝑒* = 1 − *𝑅*(*𝜆*) − *𝑐𝑑𝑖𝑠*⋅ *𝛥𝐴𝑝𝑎𝑟*(*𝜆*)*,* (B.2)

where *𝑑𝐸𝑉 𝐴*is the thickness of the EVA encapsulant. Rearranging Eq. (B.2) provides an explicit function for *𝛥𝛼*(*𝜆*), written as ( <u>1 − 𝑅(𝜆) − 𝑐 ⋅ 𝛥𝐴 (𝜆)</u> ) *𝛥𝛼*(*𝜆*) = − ln <u>𝑑𝑖𝑠 𝑝𝑎𝑟</u> ∕*𝑑* (B.3) 1 − *𝑅*(*𝜆*) *𝐸𝑉 𝐴*

We can obtain *𝛥𝑘*(*𝜆*) via <u>𝛥𝛼(𝜆) ⋅ 𝜆</u> *𝛥𝑘*(*𝜆*) = (B.4) 4*𝜋*

To determine *𝑛𝑛𝑒𝑤*(*𝜆*), we assume *𝛥𝑛*(*𝜆*) is approximately equal to *𝑐* *𝑑𝑖𝑠*, such that only one changing variable is needed. This assumption is justified by the fact that *𝑛* and *𝑘* are connected via the Kramers–Kronig (KK) relationship [67]. Numerical KK integration [68] of *𝛥𝑘*(*𝜆*) confirms that *𝛥𝑛*(*𝜆*) is nearly constant.

**Fig. A.1.** The effect of a 10% current (left) or voltage (right) loss in the perovskite subcell (blue) on the loss on 2 terminal tandem IV curve (green). The solid

and dashed lines represent the original and degradated IV curves, respectively. It can be seen that a loss in voltage has a lower impact than a loss in current.

**Fig. B.1.** The change in EQE and reflection due to discoloration.

*Source:* The data is obtained from literature [42].

To connect *𝑐𝑑𝑖𝑠*to *𝑃𝑙𝑜𝑠𝑠*due to discoloration, we simulate the optical absorption for different values of *𝑐𝑑𝑖𝑠*and calculate the loss in current.

Fig. B.2a illustrates the effect of *𝑐𝑑𝑖𝑠*on the absorption profile of the

solar cell. It can be seen that there is a similar trend compared to the original measurements in Fig. B.1. Fig. B.2b demonstrates how *𝑐𝑑𝑖𝑠* affects the current loss, providing a basis for selecting appropriate *𝑐𝑑𝑖𝑠* values for specific degradation levels.

## Appendix C. Calculating changes in circuit parameters due to MID

To model the impact of moisture ingress on the IV curve of a silicon solar cell, we base our approach on the work of Zhu et al. [46], who provided circuit parameter values under varying stress levels quantified in a procedure-defined unit (p.d.u.) [46]. First, we extracted the trends for each circuit parameter from the experimental data and applied these trends to our c-Si cell. Fig. C.1a illustrates the variation of circuit parameters with different stress doses, while Fig. C.1b shows the corresponding power loss. To model the power loss caused by moisture ingress, we use Eq.

(3) to predict the required power loss and identify the associated dose value. This dose value enabled us to determine the degraded circuit parameter values.
## Appendix D. Time profile of thermal cycling

The effect of thermal cycling is modeled by using the equation from Bosco et al. [49]. This equation describes the amount of damage expe- rienced by the PV module as a function of temperature fluctuation *𝛥𝑇*. For this work, we define *𝛥𝑇* to be the average of the daily temperature fluctuation, written as ∑*𝑁𝑑𝑎𝑦𝑠*() <u>𝑖=1</u> <u>max(𝑇𝑖− min(𝑇𝑖))</u> *𝛥𝑇* =*,* (D.1) *𝑁 𝑑𝑎𝑦𝑠* where *𝑁𝑑𝑎𝑦𝑠*is the number of days in the year, and *𝑇𝑖*is the temperature at day *𝑖*. The damage due to thermal cycling is then translated into a degradation rate *𝑘𝑇 𝐶*via Eq. (5). Fig. D.1 shows the time profile of the damage and degradation rate over time for the c-Si module in Delft.

## Appendix E. Filtering and normalization datasets

The datasets summarized in Table 1 provide performance measure- ments of PV systems over several years. To obtain *𝑃𝑛𝑜𝑟𝑚*, we have preformed the following steps. First, a data filtering process was conducted. Data points with GHI values below 200 W m−2or above 1200 W m−2were excluded. Additionally, only measurements recorded at 12:00 were selected to ensure consistent solar positioning across all data points. The power output was then normalized to standard test conditions (STC) using an equation from literature [11,69]

*𝑃* = *𝑃* ⋅ <u>𝐺𝑆𝑇 𝐶</u> ⋅ ( <u>1</u> )*,* (E.1) *𝑛𝑜𝑟𝑚 𝑎𝑐* *𝐺𝐻𝐼* 1 + *𝛾* ⋅ *𝑇* − *𝑇* *𝑆𝑇 𝐶* where *𝑃𝑎𝑐*is the provided output power, *𝐺𝑆𝑇 𝐶*and *𝑇𝑆𝑇 𝐶*are the irradiance-level and temperature at STC (i.e. 1000 W m−2and 25◦C, respectively), and *𝛾* is the temperature coefficient. Following normalization, outliers were removed by excluding data points with deviations exceeding twice the standard deviation. Finally, the data were averaged over 100 samples to smooth variations and enhance the visibility of trends.

## Appendix F. Sensitivity analysis for parameters in physical model

As mentioned in the main text, the parameters for the physical model are based on the calibration performed for the PV system in Alice Springs. To see how different parameters would change the results, we repeat the calculations for the tolerable degradation rates with different parameter sets. Table 1 contains the parameters for PV modules from all five datasets that can be used for a sensitivity analysis.

on the absorption and reflection profiles (a) and the loss in current (b).

**Fig. B.2.** The effect of *𝑐𝑑𝑖𝑠*

The effect of moisture ingress dosage on the circuit parameters (a) and the power loss (b).

**Fig. C.1.**

**Fig. D.1.** The time profile of the damage and the degradation rate due to

thermal cycling.

The parameter set for Pfaffstäten has been excluded, as a normalized power of 0.8 was already reached after 5 years, being much smaller than typical module lifetimes. It is important to note that the differences between the datasets are not only due to varying locations but also to differences in PV modules and their respective systems. Since each module uses a distinct bill of materials and manufacturing process, their degradation rates can vary, explaining the differences observed in parameter values.

Fig. F.1 shows how the tolerable degradation rate changes when

different parameter sets are used. It can be seen that the parameters can have a significant impact on the tolerable degradation rates. This is because the parameters impact the degradation rates of the physical model, which affect the value of *𝑇₈₀*. Since the product *𝑘𝑡𝑜𝑙*⋅ *𝑇₈₀*, stays

approximately constant, as mentioned in the main text, the tolerable degradation rates change accordingly. For all simulated locations, it can be seen that *𝑘𝑡𝑜𝑙*is the lowest when the parameters are calibrated for Cocoa PV module dataset, as the these calibrated values are, extend *𝐴𝑑𝑖𝑠*the lowest for all datasets (Table 1). This results in a larger module lifetime, leading to lower values for *𝑘𝑡𝑜𝑙*. Similarly, *𝑘𝑡𝑜𝑙*is the largest when the Boränge PV module dataset is used, as the parameters in this calibration are the largest. Overall, it can be seen that for each parameter set, the same trends and relative differences among locations and degradation scenarios are visible.

## Appendix G. Improving the perovskite quality

Fig. 10a illustrates the IV curves of perovskite subcells with en-

hanced efficiencies. To simulate these higher-quality subcells, new calibrated lumped element method (CLEM) models are made. The full details for how the CLEM model is constructed are explained in previous literature [20]. To make the new CLEM models, the electrical parameters are adjusted. Each parameter is interpolated between its original value and the corresponding value for an ideal solar cell, using a factor denoted as *𝑐𝑝𝑒𝑟*. This factor ranges from 0 to 1, where *𝑐𝑝𝑒𝑟*= 0 represents the original cell configuration, and *𝑐𝑝𝑒𝑟*= 1 corresponds to the ideal cell. Based on the value of *𝑐𝑝𝑒𝑟*, the value of the electrical circuit param- eters are determined by () *𝐼₀* = exp log(*𝐼₀,𝑜𝑟𝑖𝑔*) ⋅ (1 − *𝑐𝑝𝑒𝑟*) + log(*𝐼₀,𝑖𝑑𝑒𝑎𝑙*) ⋅ *𝑐𝑝𝑒𝑟* *𝑛* = *𝑛𝑜𝑟𝑖𝑔*⋅ (1 − *𝑐𝑝𝑒𝑟*) + *𝑛𝑖𝑑𝑒𝑎𝑙*⋅ *𝑐𝑝𝑒𝑟* *𝑅𝑠*= *𝑅𝑠,𝑜𝑟𝑖𝑔*⋅ (1 − *𝑐𝑝𝑒𝑟*) + *𝑅𝑠,𝑖𝑑𝑒𝑎𝑙*⋅ *𝑐𝑝𝑒𝑟*(G.1)

*𝑅𝑠ℎ* = *𝑅𝑠ℎ,𝑜𝑟𝑖𝑔* ⋅ (1 − *𝑐𝑝𝑒𝑟*) + *𝑅𝑠ℎ,𝑖𝑑𝑒𝑎𝑙* ⋅ *𝑐𝑝𝑒𝑟,*

**Fig. F.1.** A sensitivity analysis of the tolerable degradation rates. The different parameter sets used for the validation are utilized to plot the tolerable degradation

rates for the different parameters.

where *𝑛𝑖𝑑𝑒𝑎𝑙*= 1, and *𝑅𝑠,𝑖𝑑𝑒𝑎𝑙*and *𝑅𝑠ℎ,𝑖𝑑𝑒𝑎𝑙*are 1 ⋅ 10−6and 1 ⋅ 106, respectively, representing arbitrary small and large values. *𝐼₀,𝑖𝑑𝑒𝑎𝑙*is cal- culated by using the generalized equation for black body radiation [70]

*𝜆𝑔* <u>4𝜋 ⋅ 𝑐 1</u> *𝐼₀,𝑖𝑑𝑒𝑎𝑙*= *𝐴𝑐𝑒𝑙𝑙*⋅ ∫ 4 ⋅ <u>ℎ⋅𝑐</u> *𝑑𝜆,* (G.2) 0*𝜆* exp( *𝜆*⋅*𝑘* ⋅*𝑇*

) − 1
*𝑏* where *𝑐* and *ℎ* are the speed of light and planks constant, respectively, and *𝜆𝑔*is the wavelength corresponding to the perovskite bandgap energy. In the main text, the two extreme cases are considered, (i.e. *𝑐𝑝𝑒𝑟*= 0 and *𝑐𝑝𝑒𝑟*= 1). Additionally, an intermediate scenario is evaluated where *𝑐* *𝑝𝑒𝑟*represents a value such that the subcell efficiency lies halfway between the two extremes. This intermediate value of *𝑐𝑝𝑒𝑟*is different for the various IV curves that are needed as input for the CLEM model.

## Appendix H. Supplementary data

Supplementary material related to this article can be found online at [https://doi.org/10.1016/j.solmat.2026.114169](https://doi.org/10.1016/j.solmat.2026.114169).

## Data availability

Other underlying data will be made available on request.

## References

[1] A. Richter, M. Hermle, S.W. Glunz, Reassessment of the limiting efficiency for crystalline silicon solar cells, IEEE J. Photovol. (4) (2013) 1184–1191, [http://dx.doi.org/10.1109/JPHOTOV.2013.2270351](http://dx.doi.org/10.1109/JPHOTOV.2013.2270351). [2] S. Schafer, R. Brendel, Accurate calculation of the absorptance enhances ef- ficiency limit of crystalline silicon solar cells with lambertian light trapping, IEEE J. Photovol. 8 (4) (2018) 1156–1158, [http://dx.doi.org/10.1109/JPHOTOV](http://dx.doi.org/10.1109/JPHOTOV).

2018.2824024.
[3] O. Er-raji, C. Messmer, A.J. Bett, O. Fischer, S.K. Reichmuth, F. Schindler, M. Bivour, O. Schultz-Wittmann, J. Borchert, M. Hermle, J. Schön, F.D. Heinz, M.C. Schubert, silicon tandem

P.S.C.solar Schulze, cells:S.W. Characterization
Glunz, Loss analysis methods ofand fully-textured simulation toward perovskite the practical efficiency potential, Sol. RRL 7 (24) (2023) [http://dx.doi.org/10.1002/](http://dx.doi.org/10.1002/) solr.202300659. [4] A.D. Vos, Detailed balance limit of the efficiency of tandem solar cells, J. Phys. D: Appl. Phys. 13 (5) (1980) 839–846, [http://dx.doi.org/10.1088/0022-](http://dx.doi.org/10.1088/0022-) 3727/13/5/018. [5] Y. Blom, M.R. Vogt, C.M. Ruiz Tobon, R. Santbergen, M. Zeman, O. Isabella, Energy loss analysis of two-terminal tandem PV systems under realistic operating conditions—Revealing 2200579, [http://dx.doi.org/10.1002/solr.202200579](http://dx.doi.org/10.1002/solr.202200579) the importance of fill factor gains,. Sol. RRL 7 (8) (2023)

[6] 34.6%! record-breaker LONGi once again sets a new world efficiency for silicon- perovskite tandem solar cells, 2024, URL [https://www.longi.com/en/news/2024-](https://www.longi.com/en/news/2024-) snec-silicon-perovskite-tandem-solar-cells-new-world-efficiency/. [7] H. Zhu, S. Teale, M.N. Lintangpradipto, S. Mahesh, B. Chen, M.D. McGehee, E.H. Sargent, O.M. Bakr, Long-term operating stability in perovskite photovoltaics, Nat. Rev. Mater. 8 (9) (2023) 569–586, [http://dx.doi.org/10.1038/s41578-023-](http://dx.doi.org/10.1038/s41578-023-) 00582-w. [8] L. Duan, D. Walter, N. Chang, J. Bullock, D. Kang, S.P. Phang, K. Weber,

T. White, D. Macdonald, K. Catchpole, H. Shen, Stability challenges for the commercialization of perovskite–silicon tandem solar cells, Nat. Rev. Mater. 8
(4) (2023) 261–281, [http://dx.doi.org/10.1038/s41578-022-00521-1](http://dx.doi.org/10.1038/s41578-022-00521-1).
[9] J. andPeng, greenhouse

L. Lu, H. gasYang, emission
Review of solar on lifephotovoltaic cycle assessment systems, of Renew. energy payback Sustain. Energy Rev. 19 (2013) 255–274, [http://dx.doi.org/10.1016/j.rser.2012.11.035](http://dx.doi.org/10.1016/j.rser.2012.11.035), URL [https://www.sciencedirect.com/science/article/pii/S1364032112006478](https://www.sciencedirect.com/science/article/pii/S1364032112006478). [10] I. Kaaya, J. Ascencio-Vásquez, K.-A. Weiss, M. Topič, Assessment of uncertainties and variations in PV modules degradation rates and lifetime predictions using physical models, Sol. Energy 218 (2021) 354–367, [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/)

j.solener.2021.01.071, URL [https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/) S0038092X21000979.
[11] S. andLindig, analytical

I. Kaaya, degradation
K.-A. Weiss, models D.forMoser, photovoltaic
M. Topic, modules Review andofsystems
statistical as well as related improvements, IEEE J. Photovol. 8 (6) (2018) 1773–1786, [http://dx.doi.org/10.1109/JPHOTOV.2018.2870532](http://dx.doi.org/10.1109/JPHOTOV.2018.2870532). [12] M. Babics, M. De Bastiani, E. Ugur, L. Xu, H. Bristow, F. Toniolo, W. Raja, A.S. Subbiah, J. Liu, L.V. Torres Merino, E. Aydin, S. Sarwade, T.G. Allen, A. Razzaq,

N. Wehbe, M.F. Salvador, S. De Wolf, One-year outdoor operation of monolithic perovskite/silicon tandem solar cells, Cell Rep. Phys. Sci. 4 (2) (2023) 101280, [http://dx.doi.org/10.1016/j.xcrp.2023.101280](http://dx.doi.org/10.1016/j.xcrp.2023.101280), URL [https://www.sciencedirect](https://www.sciencedirect). com/science/article/pii/S2666386423000395.

[13] M. Remec, Š. Tomšič, M. Khenkin, Q. Emery, J. Li, F. Scheler, B. Glažar, M. Jankovec, M. Jošt, E. Unger, S. Albrecht, R. Schlatmann, B. Lipovšek, C. Ulbrich,

M. Topič, From sunrise to sunset: Unraveling metastability in perovskite solar cells by coupled outdoor testing and energy yield modelling, Adv. Energy Mater. 14 (29) (2024) 2304452, [http://dx.doi.org/10.1002/aenm.202304452](http://dx.doi.org/10.1002/aenm.202304452).
[14] M. De Bastiani, E. Van Kerschaver, Q. Jeangros, A. Ur Rehman, E. Aydin, F.H. Isikgor, A.J. Mirabelli, M. Babics, J. Liu, S. Zhumagali, E. Ugur, G.T. Harrison,

T.G. Allen, B. Chen, Y. Hou, S. Shikin, E.H. Sargent, C. Ballif, M. Salvador, S. De Wolf, Toward stable monolithic perovskite/silicon tandem photovoltaics: A six-month outdoor performance study in a hot and humid climate, ACS Energy Lett. 6 (8) (2021) 2944–2951, [http://dx.doi.org/10.1021/acsenergylett.1c01018](http://dx.doi.org/10.1021/acsenergylett.1c01018), arXiv:[https://doi.org/10.1021/acsenergylett.1c01018](https://doi.org/10.1021/acsenergylett.1c01018).
[15] J. Liu, E. Aydin, J. Yin, M. De Bastiani, F.H. Isikgor, A.U. Rehman, E. Yengel,

E. Ugur, G.T. Harrison, M. Wang, Y. Gao, J.I. Khan, M. Babics, T.G. Allen,
A.S. Subbiah, K. Zhu, X. Zheng, W. Yan, F. Xu, M.F. Salvador, O.M. Bakr,
T.D. Anthopoulos, M. Lanza, O.F. Mohammed, F. Laquai, S. De Wolf, 28.2%- Efficient, outdoor-stable perovskite/silicon tandem solar cell, Joule 5 (12) (2021) 3169–3186, [http://dx.doi.org/10.1016/j.joule.2021.11.003](http://dx.doi.org/10.1016/j.joule.2021.11.003).
[16] J. Qian, M. Ernst, N. Wu, A. Blakers, Impact of perovskite solar cell degradation on the lifetime energy yield and economic viability of perovskite/silicon tandem modules, Sustain. Energy & Fuels 3 (6) (2019) 1439–1447, [http://dx.doi.org/10](http://dx.doi.org/10). 1039/C9SE00143C. [17] S. Orooji, U.W. Paetzold, Energy yield modeling of perovskite–silicon tandem photovoltaics: Degradation and total lifetime energy yield, Energy Technol. 12 (11) (2024) 2400998, [http://dx.doi.org/10.1002/ente.202400998](http://dx.doi.org/10.1002/ente.202400998), arXiv: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/ente.202400998](https://onlinelibrary.wiley.com/doi/pdf/10.1002/ente.202400998). URL https:// onlinelibrary.wiley.com/doi/abs/10.1002/ente.202400998. [18] E. Aydin, T.G. Allen, M.D. Bastiani, A. Razzaq, L. Xu, E. Ugur, J. Liu, S.D. Wolf, Pathways toward commercial perovskite/silicon tandem photovoltaics, Science 383 (6679) (2024) eadh3849, [http://dx.doi.org/10.1126/science.adh3849](http://dx.doi.org/10.1126/science.adh3849), URL [https://www.science.org/doi/abs/10.1126/science.adh3849](https://www.science.org/doi/abs/10.1126/science.adh3849). [19] D.C. Jordan, S.R. Kurtz, K. VanSant, J. Newmiller, Compendium of photovoltaic degradation rates, Prog. Photovolt., Res. Appl. 24 (7) (2016) 978–989, http: //dx.doi.org/10.1002/pip.2744. [20] M. Vogt, C.R. Tobon, A. Alcañiz, P. Procel, Y. Blom, A.N. El Din, T. Stark,

Z. Wang, E.G. Goma, J. Etxebarria, H. Ziar, M. Zeman, R. Santbergen, O. Isabella, Introducing a comprehensive physics-based modelling framework for tandem and other PV systems, Sol. Energy Mater. Sol. Cells 247 (2022) 111944, [http://dx.doi.org/10.1016/j.solmat.2022.111944](http://dx.doi.org/10.1016/j.solmat.2022.111944).
[21] Y. Blom, M.R. Vogt, O. Isabella, R. Santbergen, Optimization of the per- ovskite cell in a bifacial two-terminal perovskite/silicon tandem module, Sol. Energy Mater. Sol. Cells 282 (2025) 113431, [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/)

j.solmat.2025.113431, URL [https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/) S0927024825000327.
[22] Y. Blom, M. Ruben Vogt, H. Uzu, G. Koizumi, K. Yamamoto, O. Isabella,

R. Santbergen, Exploring the potential of perovskite/perovskite/silicon triple- junction pv modules in two-and four-terminal configuration, Sol. RRL 9 (2025).
[23] Y. Blom, W. Suprayogi, M. Ruben Vogt, O. Isabella, R. Santbergen, Comparison on module performance and degradation robustness of two-, three-, and four- terminal perovskite silicon configurations under realistic operating conditions, n/a, 2025, [24] T. Ma, Z. Guo, L. Shen, X. Liu, Z. Chen, Y. Zhou, X. Zhang, Performance modelling of photovoltaic modules under actual operating conditions considering loss mechanism and energy distribution, Appl. Energy 298 (2021) 117205, http: //dx.doi.org/10.1016/j.apenergy.2021.117205, URL [https://www.sciencedirect](https://www.sciencedirect). com/science/article/pii/S0306261921006292. [25] T. Ma, H. Yang, L. Lu, Development of a model to simulate the performance characteristics of crystalline silicon photovoltaic modules/strings/arrays, Sol. Energy 100 (2014) 31–41, [http://dx.doi.org/10.1016/j.solener.2013.12.003](http://dx.doi.org/10.1016/j.solener.2013.12.003), URL [https://www.sciencedirect.com/science/article/pii/S0038092X13005203](https://www.sciencedirect.com/science/article/pii/S0038092X13005203). [26] A. Chouder, S. Silvestre, B. Taghezouit, E. Karatepe, Monitoring, modelling and simulation of PV systems using LabVIEW, Sol. Energy 91 (2013) 337–349, http:// dx.doi.org/10.1016/j.solener.2012.09.016, URL [https://www.sciencedirect.com/](https://www.sciencedirect.com/) science/article/pii/S0038092X12003416. [27] K. Ramalingam, C. Indulkar, Solar energy and photovoltaic technology, Distrib. Gener. Syst. (2017) 69–147. [28] I. Kaaya, M. Koehl, A.P. Mehilli, S. de Cardona Mariano, K.A. Weiss, Modeling outdoor service lifetime prediction of PV modules: Effects of combined climatic stressors on PV module power degradation, IEEE J. Photovol. 9 (4) (2019) 1105–1112, [http://dx.doi.org/10.1109/JPHOTOV.2019.2916197](http://dx.doi.org/10.1109/JPHOTOV.2019.2916197). [29] A. Bala Subramaniyan, R. Pan, J. Kuitche, G. TamizhMani, Quantification of environmental effects on PV module degradation: A physics-based data-driven modeling method, IEEE J. Photovol. 8 (5) (2018) 1289–1296, [http://dx.doi.org/](http://dx.doi.org/)

10.1109/JPHOTOV.2018.2850527.
[30] D.C. Jordan, T.J. Silverman, J.H. Wohlgemuth, S.R. Kurtz, K.T. VanSant, Photo- voltaic failure and degradation modes, Prog. Photovolt., Res. Appl. 25 (4) (2017) 318–326, [http://dx.doi.org/10.1002/pip.2866](http://dx.doi.org/10.1002/pip.2866), arXiv:[https://onlinelibrary.wiley](https://onlinelibrary.wiley). com/doi/pdf/10.1002/pip.2866. URL [https://onlinelibrary.wiley.com/doi/abs/](https://onlinelibrary.wiley.com/doi/abs/)

10.1002/pip.2866.
[31] M. Köntges, S. Kurtz, C. Packard, U. Jahn, K.A. Berger, K. Kato, T. Friesen, H. Liu, M. Van Iseghem, Review of Failures of Photovoltaic Modules, Tech. rep., INTERNATIONAL ENERGY AGENCY, 2014. [32] M. Simon, E.L. Meyer, Detection and analysis of hot-spot formation in solar cells, Sol. Energy Mater. Sol. Cells 94 (2) (2010) 106–113, [http://dx.doi.org/10](http://dx.doi.org/10). 1016/j.solmat.2009.09.016, URL [https://www.sciencedirect.com/science/article/](https://www.sciencedirect.com/science/article/) pii/S0927024809003420. [33] W. Luo, Y.S. Khoo, P. Hacke, V. Naumann, D. Lausch, S.P. Harvey, J.P. Singh,

J. Chai, Y. Wang, A.G. Aberle, S. Ramakrishna, Potential-induced degradation in photovoltaic modules: A critical review, Energy Env. Sci. 10 (2017) 43–68, [http://dx.doi.org/10.1039/C6EE02271E](http://dx.doi.org/10.1039/C6EE02271E).
[34] P. Borah, L. Micheli, N. Sarmah, Analysis of soiling loss in photovoltaic modules: A review of the impact of atmospheric parameters, soil properties, and mitigation approaches, Sustainability 15 (24) (2023) [http://dx.doi.org/10.3390/](http://dx.doi.org/10.3390/) su152416669, URL [https://www.mdpi.com/2071-1050/15/24/16669](https://www.mdpi.com/2071-1050/15/24/16669). [35] J.J. John, V. Rajasekar, S. Boppana, S. Chattopadhyay, A. Kottantharayil, G. TamizhMani, Quantification and modeling of spectral and angular losses of naturally soiled PV modules, IEEE J. Photovol. 5 (6) (2015) 1727–1734, http: //dx.doi.org/10.1109/JPHOTOV.2015.2463745. [36] D.C. Jordan, T.J. Silverman, B. Sekulic, S.R. Kurtz, PV degradation curves: Non-linearities and failure modes, Prog. Photovolt., Res. Appl. 25 (7) (2017) 583–591, [http://dx.doi.org/10.1002/pip.2835](http://dx.doi.org/10.1002/pip.2835), arXiv:[https://onlinelibrary.wiley](https://onlinelibrary.wiley). com/doi/pdf/10.1002/pip.2835. URL [https://onlinelibrary.wiley.com/doi/abs/](https://onlinelibrary.wiley.com/doi/abs/)

10.1002/pip.2835.
[37] VDMA, International technology roadmap for photovoltaics (ITRPV), 2024. [38] C. Peike, L. Purschke, K.-A. Weiss, M. Köhl, M. Kempe, Towards the origin of photochemical EVA discoloration, in: 2013 IEEE 39th Photovoltaic Specialists Conference, PVSC, 2013, pp. 1579–1584, [http://dx.doi.org/10.1109/PVSC.2013](http://dx.doi.org/10.1109/PVSC.2013). 6744447. [39] A. Sinha, H. Gopalakrishna, A. Bala Subramaniyan, D. Jain, J. Oh, D. Jordan,

G. TamizhMani, Prediction of climate-specific degradation rate for photovoltaic encapsulant discoloration, IEEE J. Photovol. 10 (4) (2020) 1093–1101, http:
[40] //dx.doi.org/10.1109/JPHOTOV.2020.2989182

Y. Lyu, J.H. Kim, X. Gu, Developing methodology
. for service life prediction of PV materials: Quantitative effects of light intensity and wavelength on discol- oration of a glass/EVA/PPE laminate, Sol. Energy 174 (2018) 515–526, http:// dx.doi.org/10.1016/j.solener.2018.08.067, URL [https://www.sciencedirect.com/](https://www.sciencedirect.com/) science/article/pii/S0038092X18308375. [41] Iarc working group on the evaluation of carcinogenic risks to humans, in: Radiation, Lyon, 2012, Chapter 1. URL [https://www.ncbi.nlm.nih.gov/books/](https://www.ncbi.nlm.nih.gov/books/) NBK304366/. [42] R. Meena, S. Kumar, R. Gupta, Comparative investigation and analysis of delaminated and discolored encapsulant degradation in crystalline silicon photo- voltaic modules, Sol. Energy 203 (2020) 114–122, [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/)

j.solener.2020.04.041, URL [https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/) S0038092X20304163.
[43] O.K. Segbefia, A.G. Imenes, T.O.S. tre, Moisture ingress in photovoltaic mod- ules: A review, Sol. Energy 224 (2021) 889–906, [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/)

j.solener.2021.06.055, URL [https://www.sciencedirect.com/science/article/pii/](https://www.sciencedirect.com/science/article/pii/) S0038092X21005375.
[44] A.A.Q. Hasan, A. Ahmed Alkahtani, S.A. Shahahmadi, M. Nur E. Alam, M.A. Islam, N. Amin, Delamination-and electromigration-related failures in solar panels—A review, Sustainability 13 (12) (2021) [http://dx.doi.org/10.3390/](http://dx.doi.org/10.3390/) su13126882, URL [https://www.mdpi.com/2071-1050/13/12/6882](https://www.mdpi.com/2071-1050/13/12/6882). [45] Y. Blom, D. Jimenez Pelarda, T. Minett, I. Kaaya, N. Kyranaki, R. Santbergen, O. Isabella, M. Ruben Vogt, Modelling moisture ingress in PV modules with different encapsulant and backsheet materials, Renew. Energy (2025) Submitted to. [46] J. Zhu, M. Koehl, S. Hoffmann, K.A. Berger, S. Zamini, I. Bennett, E. Gerritsen, P. Malbranche, P. Pugliatti, A. Di Stefano, F. Aleo, D. Bertani, F. Paletta, F. Roca,

G. Graditi, M. Pellegrino, O. Zubillaga, F.J.C. Iranzo, A. Pozza, T. Sample, R. Gottschalg, Changes of solar cell parameters during damp-heat exposure, Prog. Photovolt., Res. Appl. 24 (10) (2016) 1346–1358, [http://dx.doi.org/10.1002/](http://dx.doi.org/10.1002/) pip.2793, arXiv:[https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.2793](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.2793). URL [https://onlinelibrary.wiley.com/doi/abs/10.1002/pip.2793](https://onlinelibrary.wiley.com/doi/abs/10.1002/pip.2793).
[47] O.O. Ogbomo, E.H. Amalu, N. Ekere, P. Olagbegi, Effect of operating temperature on degradation of solder joints in crystalline silicon photovoltaic modules for improved reliability in hot climates, Sol. Energy 170 (2018) 682–693, http:// dx.doi.org/10.1016/j.solener.2018.06.007, URL [https://www.sciencedirect.com/](https://www.sciencedirect.com/) science/article/pii/S0038092X18305462. [48] H. Gopalakrishna, A. Sinha, J. Carpenter, S. Niverty, N. Chawla, D. Jordan, G. Tamizhmani, Activation energy for end-of-life solder bond degradation: Thermal cycling of field-aged PV modules, IEEE J. Photovol. 10 (6) (2020) 1762–1771, [http://dx.doi.org/10.1109/JPHOTOV.2020.3025726](http://dx.doi.org/10.1109/JPHOTOV.2020.3025726). [49] N. Bosco, T.J. Silverman, S. Kurtz, Climate specific thermomechanical fatigue of flat plate photovoltaic module solder joints, Microelectron. Reliab. 62 (2016) 124–129, [http://dx.doi.org/10.1016/j.microrel.2016.03.024](http://dx.doi.org/10.1016/j.microrel.2016.03.024), URL [https://www](https://www). sciencedirect.com/science/article/pii/S0026271416300609. [50] J. Schmidt, A.G. Aberle, R. Hezel, Investigation of carrier lifetime instabilities in cz-grown silicon, in: Conference Record of the Twenty Sixth IEEE Photovoltaic Specialists Conference - 1997, 1997, pp. 13–18, [http://dx.doi.org/10.1109/PVSC](http://dx.doi.org/10.1109/PVSC).

1997.653914.

[51] J. Lindroos, H. Savin, Review of light-induced degradation in crystalline silicon solar cells, Sol. Energy Mater. Sol. Cells (2016) 115–126, [http://dx.doi](http://dx.doi). org/10.1016/j.solmat.2015.11.047, URL [https://www.sciencedirect.com/science/](https://www.sciencedirect.com/science/) article/pii/S0927024815006406. [52] A. Herguth, Application of the concept of lifetime-equivalent defect density in defect systems comprising a multitude of defect species, Phys. Status Solidi

(A) 216 (17) (2019) 1900322, [http://dx.doi.org/10.1002/pssa.201900322](http://dx.doi.org/10.1002/pssa.201900322), arXiv: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pssa.201900322](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pssa.201900322). URL https:// onlinelibrary.wiley.com/doi/abs/10.1002/pssa.201900322.
[53] A. Herguth, On the meaning(fullness) of the intensity unit ‘suns’ in light induced degradation experiments, Energy Procedia 124 (2017) 53–59, [http://dx](http://dx). doi.org/10.1016/j.egypro.2017.09.339, 7th International Conference on Silicon Photovoltaics, SiliconPV 2017, 3-5 April 2017, Freiburg, Germany. URL https: //www.sciencedirect.com/science/article/pii/S1876610217343102. [54] H. Hashigami, Y. Itakura, T. Saitoh, Effect of illumination conditions on czochralski-grown silicon solar cell degradation, J. Appl. Phys. 93 (7) (2003) 4240–4245, [http://dx.doi.org/10.1063/1.1559430](http://dx.doi.org/10.1063/1.1559430), arXiv:[https://pubs.aip.org/](https://pubs.aip.org/) aip/jap/article-pdf/93/7/4240/19247263/4240_1_online.pdf. [55] B. Sopori, P. Basnyat, S. Devayajanam, S. Shet, V. Mehta, J. Binns, J. Appel, Understanding light-induced degradation of c-si solar cells, in: 2012 38th IEEE Photovoltaic Specialists Conference, 2012, pp. 001115–001120, [http://dx.doi](http://dx.doi). org/10.1109/PVSC.2012.6317798. [56] D.A. Neamen, Semiconductor Physics and Devices, fourth ed., McGrawHill, 2011,

p. 301.
[57] Desert Knowledge Australia Solar Centre, Trina, 5.3kw, mono-si, fixed, 2009, 2024, URL [https://dkasolarcentre.com.au/source/alice-springs/dka-m6-b-phase](https://dkasolarcentre.com.au/source/alice-springs/dka-m6-b-phase). (Accessed 18 January 2024). [58] S. Lindig, A. Curran, K. Rath, A. Khalilnejad, D. Moser, R.H. French, R. Wieser, IEA PVPS task 13-ST2.5: PLR determination benchmark study, 2024, [http://dx](http://dx). doi.org/10.17605/OSF.IO/VTR2S, URL [https://osf.io/vtr2s/](https://osf.io/vtr2s/). [59] NREL, PV data acquisition, 2024, URL [https://developer.nrel.gov/docs/solar/](https://developer.nrel.gov/docs/solar/) pvdaq-v3/. (Accessed 18 January 2024). [60] O.K. Segbefia, N. Akhtar, T.O. Sætre, Moisture induced degradation in field- aged multicrystalline silicon photovoltaic modules, Sol. Energy Mater. Sol. Cells 258 (2023) 112407, [http://dx.doi.org/10.1016/j.solmat.2023.112407](http://dx.doi.org/10.1016/j.solmat.2023.112407), URL https: //www.sciencedirect.com/science/article/pii/S0927024823002283. [61] E. Psimopoulos, J. Plautz, F. Fiedler, A. Augusto, Performance of a PV system operating for 30-years in scandinavia, in: 2024 IEEE 52nd Photovoltaic Specialist Conference, PVSC, 2024, pp. 0353–0355, [http://dx.doi.org/10.1109/PVSC57443](http://dx.doi.org/10.1109/PVSC57443).

2024.10748925.
[62] M. Roffeis, S. Kirner, J.-C. Goldschmidt, B. Stannowski, L.M. Perez, C. Case, M. Finkbeiner, New insights into the environmental performance of perovskite-on- silicon tandem solar cells – a life cycle assessment of industrially manufactured modules, Sustain. Energy Fuels 6 (2022) 2924–2940, [http://dx.doi.org/10.1039/](http://dx.doi.org/10.1039/) D2SE00096B. [63] S. Mariotti, E. Köhnen, F. Scheler, K. Sveinbjörnsson, L. Zimmermann, M. Piot, F. Yang, B. Li, J. Warby, A. Musiienko, D. Menzel, F. Lang, S. Keßler, I. Levine, D. Mantione, A. Al-Ashouri, M.S. Härtel, K. Xu, A. Cruz, J. Kurpiers, P. Wagner, H. Köbler, J. Li, A. Magomedov, D. Mecerreyes, E. Unger, A. Abate, M. Stolterfoht,

B. Stannowski, R. Schlatmann, L. Korte, S. Albrecht, Interface engineering for high-performance, triple-halide perovskite–silicon tandem solar cells, Science 381 (6653) (2023) 63–69, [http://dx.doi.org/10.1126/science.adf5872](http://dx.doi.org/10.1126/science.adf5872).
[64] M. Kottek, J. Grieser, C. Beck, B. Rudolf, F. Rubel, World map of the Köppen-Geiger climate classification updated, Meteorol. Zeitschrif 15 (3) (2006) 259–263. [65] J. Ascencio-Vásquez, K. Brecl, M. Topič, Methodology of Köppen-Geiger- photovoltaic climate classification and implications to worldwide mapping of PV system performance, Sol. Energy 191 (2019) 672–685, [http://dx.doi.org/10](http://dx.doi.org/10). 1016/j.solener.2019.08.072. [66] F.J. Triana de las Heras, O. Isabella, M.R. Vogt, A machine learning approach to pv-climate classification, 2024, [http://dx.doi.org/10.2139/ssrn.4905242](http://dx.doi.org/10.2139/ssrn.4905242). [67] T. Dethe, H. Gill, D. Green, A. Greensweight, L. Gutierrez, M. He, T. Tajima, K. Yang, Causality and dispersion relations, Am. J. Phys. 87 (4) (2019) 279–290, [http://dx.doi.org/10.1119/1.5092679](http://dx.doi.org/10.1119/1.5092679). [68] K. Ohta, H. Ishida, Comparison among several numerical integration methods for Kramers-Kronig transformation, Appl. Spectrosc. 42 (6) (1988) 952–957, URL [https://opg.optica.org/as/abstract.cfm?URI=as-42-6-952](https://opg.optica.org/as/abstract.cfm?URI=as-42-6-952). [69] G. Belluardo, P. Ingenhoven, W. Sparber, J. Wagner, P. Weihs, D. Moser, Novel method for the improvement in the evaluation of outdoor performance loss rate in different PV technologies and comparison with two other methods, Sol. Energy 117 (2015) 139–152, [http://dx.doi.org/10.1016/j.solener.2015.04.030](http://dx.doi.org/10.1016/j.solener.2015.04.030), URL [https://www.sciencedirect.com/science/article/pii/S0038092X15002182](https://www.sciencedirect.com/science/article/pii/S0038092X15002182). [70] L.C. Hirst, N.J. Ekins-Daukes, Fundamental losses in solar cells, Prog. Photo- volt., Res. Appl. 19 (3) (2011) 286–293, [http://dx.doi.org/10.1002/pip.1024](http://dx.doi.org/10.1002/pip.1024), arXiv:[https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.1024](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.1024). URL https:// onlinelibrary.wiley.com/doi/abs/10.1002/pip.1024.
