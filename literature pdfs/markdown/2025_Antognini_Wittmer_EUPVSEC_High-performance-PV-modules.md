##### 42nd European Photovoltaic Solar Energy Conference and Exhibi;on

##### A GENERAL APPROACH TO MODEL HIGH-PERFORMANCE PV MODULES FOR ACCURATE ENERGY

##### YIELD SIMULATIONS

Luca Antognini, Michele Oliosi, Auriane Canesse, Robin Vincent, André Mermoud, Bruno Wittmer PVsyst SA Route de la Maison-Carrée 30, CH 1242 Satigny-Switzerland

ABSTRACT: One of the challenges in PV module performance modeling is to obtain a good description of the I-V curves at various temperatures and illuminations, based solely on limited available data. Currently in PVsyst, this is done by calculating the parameters for the one-diode model (1DM) from datasheet information and common assumptions on low-light performance. However, this fails to reproduce high fill factors (FF), typically compromising 𝑉 𝑜𝑐accuracy. To address this, we use an evolutionary algorithm (EA) which improves parameter determination for the 1DM, extends to more sophisticated models and can use measurement variability as input. This method necessitates solely datasheet information and common low-light assumptions to reproduce IEC 61853-1 measurements. We demonstrate its benefits on both measured PERC modules and synthetic high-FF scenarios. On measured data from a low-FF module, the EA lowers the mean efficiency error in reproducing IEC 61853-1 data compared to the current method. To test the EA on high-FF devices, we generate synthetic data from a reference recombination model informed by solar-cell literature. In this case too, the EA reduces power error and greatly improves 𝑉𝑜𝑐reproduction, which is further enhanced when switching from 1DM to the reference model itself. Keywords: PV Module Modeling, PVsyst

1 INTRODUCTION Then, we describe the current calculation procedure of PVsyst and the EA optimization approach. Accurate modelling of PV module I–V curves is essential for reliable energy yield simulations. The one-2.1 Current PVsyst I-V Parametrization diode model (1DM), as implemented in PVsyst, remains We describe here the parametrization of the 1DM as it an industry standard due to its simplicity and accuracy to is implemented in the current version of PVsyst (8.0). As represent PERC PV modules. PVsyst uses an analytical in any 1DM parametrization, the external current 𝐼 is a method to determine the model parameters based solely on balance between the photogenerated current and the the information available in datasheet, completed by current losses in the first diode and shunt resistor, observed technological trends for low-light performance.<u>𝑠</u>

||𝑞(𝑉+𝐼𝑅)|𝑠|
|---|---|---|
|𝑝ℎ|𝛾𝑘 𝑇|𝑠ℎ|
|𝑖𝑛𝑡 𝑠|𝑠 𝑝ℎ||

<u>𝑉 + 𝐼𝑅</u> However, for modern high-performance devices with 𝐼=𝐼 − 𝐼₀ (𝑒 𝐵 − 1) − elevated fill factors (FF), this approach often compromises 𝑅

open-circuit voltage accuracy, limiting its predictive where the term 𝑉 = 𝑉 + 𝐼𝑅 is the internal voltage of power. Moreover, the origin of those high FF within the solar cells prior to the voltage drop across the series crystalline silicon (c-Si) technology is well understood resistance 𝑅.The equivalent circuit of this equation can be through more sophisticated models incorporating several seen in Figure 1 (a). recombination mechanisms impacting in parallel the I–V The photogenerated current 𝐼 is assumed to depend behaviour. These developments call for parameter linearly on the temperature and irradiance evaluation methods that go beyond fixed assumptions and <u>𝐺</u>

|𝐼 (𝐺, 𝑇) =|𝐼|[1 + 𝜇 (𝑇 − 𝑇|)]|
|---|---|---|---|
|𝑝ℎ 𝑝ℎ,𝑟𝑒𝑓|𝑝ℎ,𝑟𝑒𝑓 𝑟𝑒𝑓|𝐼|𝑐,𝑟𝑒𝑓 𝑐,𝑟𝑒𝑓|
||𝑅𝑒𝑓|𝐼𝑠𝑐||
||𝑇 0,𝑟𝑒𝑓 𝑇|0 𝑞𝐸 1 𝛾𝑘 𝑇|1 𝑇|
||||𝑔|

can flexibly adapt to new device characteristics.𝑠𝑐 To overcome the limitations arising at high FFs, we 𝐺

explore two approaches: 1) Change the determination�where 𝐼 is the photogenerated current under the method

### _for the model parameters evaluation from

standard test conditions (STC) temperature 𝑇 = 25 °𝐶 datasheet information. 2) Investigate the potential benefit and irradiance 𝐺 = 1000 𝑊/𝑚². 𝜇 is the short- of a different_I–V-parametrization that is established in circuit current temperature coefficient. Similarly, the literature and known to be able to describe high FF. saturation current of the diode 𝐼 depends on the In particular, we propose an evolutionary algorithm temperature as (EA) framework that can adapt to both the conventional 3 1DM and recombination-based models. This method 𝐼₀(𝑇) = 𝐼 () exp( <u>𝑔</u> ( −)), necessitates solely datasheet data and common low-light𝑟𝑒𝑓 𝐵 𝑟𝑒𝑓 assumptions to reproduce IEC 61853-1 measurements. We where for crystalline silicon (c-Si) the bandgap 𝐸 is set demonstrate its benefits on both measured PERC modules to a fixed value of 1.12 eV. and synthetic high-FF scenarios. Next, based on experimental observations [2], PVsyst assumes an exponential behaviour of the shunt resistance with irradiance 2 METHOD 𝑅𝑠ℎ(𝐺) = 𝑅𝑠ℎ,𝐵𝑎𝑠𝑒+ [𝑅𝑠ℎ(0) − 𝑅𝑠ℎ,𝐵𝑎𝑠𝑒] <u>𝐺</u> ' We first summarize the current PVsyst I-V × exp(−𝑅 𝑠ℎ,𝑒𝑥𝑝()). s parameterization and a reference recombination-based 𝐺𝑟𝑒𝑓 model from the solar cell literature state-of-the-art. This with model is commonly accepted to describe the origin of high fluskun

||(STC) − 𝑅|(0) exp(−𝑅||
|---|---|---|---|
|𝑠ℎ,𝐵𝑎𝑠𝑒|𝑠ℎ|𝑠ℎ 𝑠ℎ,𝑒𝑥𝑝|𝑠ℎ,𝑒𝑥𝑝|

FF in record efficiency device [1] and we will therefore 𝑅 = <u>𝑅)</u>

use it to generate synthetic data in the next sections. 1 − exp(−𝑅)

10.4229/EUPVSEC2025/3AV.3.32 020196-001

|∞ So varianc onyway|real additional 𝑅 𝑠ℎ 、 Finaly, where 𝜇 𝐼 𝑝ℎ,𝑟𝑒𝑓, We 4 𝑅 𝑠ℎ|(0)/𝑅 𝑠ℎ 2 at 1000 W/m, 𝑅 PVsyst 𝛾 𝜇, 𝐼₀ 𝐼 𝑠𝑐 additionally (𝑆𝑇𝐶) unknown parameters to 7. 𝐼=𝐼|degrees 𝑠ℎ assumes temperature of the diode ideality factor 𝛾 𝛾(𝑇) = 𝛾, 𝛾, 𝜇, 𝑅 𝛾 assume 𝑅 for c-Si, − 𝐼 𝑝ℎ|Based on the measurement campaign led in [2], the two of a given PV technology, leaving only the shunt resistance a + 𝜇 𝑟𝑒𝑓 𝛾 is an additional unknown parameter. In summary, PVsyst 1DM has 9 parameters:, 𝑅 𝑠 𝑠ℎ 𝑠ℎ,𝑒𝑥𝑝 2.2 Reference recombination model for high-FF We explicitate here the reference parametrization of the I-V curve informed by solar cell literature on electron/hole recombination mechanisms. As for the 1DM, the model is still described as a current balance equation − 𝐼 𝑎𝑢𝑔 𝑟𝑎𝑑|freedom (𝑆𝑇𝐶) ratio takes remarkably fixed values for (𝑆𝑇𝐶), as unknown parameter. linear (𝑇 − 𝑇 (𝑆𝑇𝐶), 𝑅 = 5.5 − 𝐼 𝑆𝑅𝐻|𝑅 𝑠ℎ,𝑒𝑥𝑝 dependence), 𝑟𝑒𝑓, and 𝑅 𝑠ℎ,𝑒𝑥𝑝 and 𝑅 which reduces the number of − 𝐼, 𝑠ℎ|𝑠ℎ (0) = 𝑠ℎ|42nd European Photovoltaic Solar Energy Conference and Exhibi;on and on (0).|depend thickness of 𝑉|approximation 𝑛₀ the internal voltage by 2 𝑛 exp (𝑘 𝑖. 𝑖𝑛𝑡|explicitly on 𝑊. Those equilibrium concentration 𝑛₀ 𝑛 = 𝑛 0 intrinsic carrier concentration 𝑛 = [4] for the value of the coefficients 𝐶 𝑞𝑉 𝑖𝑛𝑡 𝑏|the + Δ𝑛 and 𝑝 = excitation (voltage and illumination), 𝑛₀ 𝑝₀ 𝑁 (and 𝑝₀ remaining terms are defined in the same publication. Within the description of [3] [4], 𝑛|electron concentration 𝑛 and 𝑝, respectively, and the c-Si wafer quantities and 𝑝₀ where Δ𝑛 is the excess charge concentration created by the by 𝑖 = 𝑛. 𝑖2 Finaly, in the case of n-type wafer, we have the = 𝑁 is the base doping concentration of the wafer. We follow Note that the carrier concentrations are directly related to 2 𝑛 𝑖 𝑇)= 𝑝𝑛 ≈ (𝑁 + Δ𝑛)(𝑁 + Δ𝑛). Therefore, an increase in Δ𝑛 results directly in an increase|and are by 𝑝 + Δ𝑛 0, 𝐶 𝑝0 𝑛0 𝑖|hole related related 𝑁 for p-type), where, 𝐵 𝑙𝑜𝑤|to and the depends both on|carrier the to the|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||where the different terms are defined below and the equivalent circuit diagram is shown in Figure 2 (a). For the description of the intrinsic recombination, we|||||𝑛 𝑖|(𝑇, 𝑛, 𝑝) =|accepted parametrization is [5] [6] 9.653 × 10|temperature and carrier concentrations. 9|||A|commonly different from Hamer?||
|matches Hamer|Figure 1:|𝐼 𝑎𝑢𝑔 𝐼 𝑟𝑎𝑑|= 𝑞𝑊(𝑔 + 𝑔 and the radiative recombination current = 𝑞𝑊(1 − 𝑓 derived from the slope of the top black curve.|follow the latest parametrization proposed in [3] [4]. In this formalism the Auger recombination current 𝐶 𝑒ℎℎ 𝑝0 𝐶 𝑒𝑒ℎ 𝑛0)𝐵 𝑃𝑅 𝑙𝑜𝑤 model. (b) Breakdown of current losses for typical model parameters on logarithmic scale and local ideality factor|2 (𝑝 𝑛 − 𝑝₀ 2 (𝑝𝑛 − 𝑝 𝐵 𝑟𝑒𝑙 (a) Equivalent circuit diagram of the one diode|2) 𝑛₀ 2 𝑛)) 0 (𝑛𝑝 − 𝑛₀ 𝑝₀|V ")|10.4229/EUPVSEC2025/3AV.3.32 020196-002|bandgap Figure|where the function 𝐸 temperature dependance. 2:|narrowing (a) from the slope of the top black curve.|𝑇[°𝐾] × (300 𝐺 effect Equivalent|1.706) at concentration. Note the resemblance with the 1DM’s 𝐼₀ circuit recombination model. (b) Current losses breakdown for typical model parameters and local ideality factor derived|exp (− (𝑇, 𝑛, 𝑝) represents the effect of the|𝐺 increased diagram|𝐸 (𝑇, 𝑛, 𝑝) 2𝑘 𝑇 𝐵 of|) carrier the|

For the description of the extrinsic recombination, we replace the single diode term with the Shockley-Read-Hall equation which uses the same formalism as presented in this section and, in the assumption of single defect level close to mid-gap [1], can be approximated as

##### valid is this

<u>𝑝𝑛 − 𝑛𝑖</u> 2 how 𝐼𝑆𝑅𝐻= 𝑞 𝑊 # 𝜏𝑆𝑅𝐻 (𝑛 + 𝑝) assumptionwhere 𝜏 𝑆𝑅𝐻is the effective lifetime of the excess charge Does explicit created by the excitation (voltage and illumination) and 𝑊 being # the thickness of c-Si wafer. improvefig The shunt current is still given by inconstrained param) <u>𝑉 + 𝐼𝑅𝑠</u> (without 𝐼𝑠ℎ= 𝑅𝑠ℎ and we keep the same assumptions for the irradiance and

|temperature dependance of 𝑅||and 𝐼|. This also sums up||
|---|---|---|---|---|
|||𝑠ℎ|𝑝ℎ||
|𝑝ℎ,𝑟𝑒𝑓 𝑠ℎ|𝐼 𝑆𝑅𝐻|𝑠 𝑠ℎ|𝑠ℎ,𝑒𝑥𝑝|𝑠ℎ 𝑠ℎ,𝑒𝑥𝑝|

##### to 9 unknown parameters

𝐼, 𝜇 𝑠𝑐, 𝜏, 𝑊, 𝑁, 𝑅, 𝑅 (𝑆𝑇𝐶), 𝑅, and 𝑅 (0)

where the same assumptions can be made on 𝑅 and 𝑅 (0), which reduces the number of unknown parameters to 7 again. The motivation to use this model is now described. It is a well-known fact that the STC efficiency of an ideal c- Si solar cell (i.e. with no extrinsic recombination nor shunt or series resistance) is limited by radiative and Auger recombination to a value of 29.4% while the FF is limited to 89.26%. Note that those numbers remained unchanged up to the second digit in the last decades [7] [8] [4]. The FF limit is explained by the strong increase of the Auger 2 recombination at higher carrier concentrations (𝑝 𝑛 and 2 𝑝𝑛 terms), and therefore at higher voltages, increasing gradually the intrinsic recombination current from the maximal power point (MPP) until the open-circuit conditions (OC). This is shown in Figure 2 (b). Another way to understand this, is that if one were to approximate by an effective single diode model representing the intrinsic recombination mechanisms, it would be required to introduce a voltage dependent diode ideality factor which decreases towards a value of 2/3 as the voltage increases, making the I-V curve’s shape more squared and increase the FF. radiative parametes thijustifiesAura

2.3 Current PVsyst Parameter Calculation In the current PVsyst implementation (8.0), the direct calculation method of the 1DM parameters requires at least 9 independent input data to be well defined. The 6 first are (almost always) specified in the PV module datasheet. First, I-V curve is constrained to pass by three points defined by the STC values: (𝑉𝑚𝑝𝑝, 𝐼𝑚𝑝𝑝), (𝑉𝑜𝑐, 0), and (0, 𝐼𝑠𝑐). Note that it is not specified that the first point is the maximum power point, and therefore the 𝑃𝑚𝑝𝑝value obtained by the model can be slightly different than the one of the input data. Second, 𝜇𝐼𝑠𝑐is used directly as input parameter and the power temperature coefficient 𝜇𝑃𝑚𝑝𝑝needs to be reproduced (mainly by adjusting the parameter 𝜇𝛾). Note that the temperature coefficient of the open circuit voltage 𝜇 𝑉𝑜𝑐is not used in this calculation (its usage is restricted to compute in a separate way the 𝑉𝑜𝑐at low temperature for system sizing and norm safety purpose). Third, as mentioned above, two additional constraints can be set by fixing 𝑅𝑠ℎ,𝑒𝑥𝑝= 5.5 and 𝑅𝑠ℎ(0) = 4 𝑅𝑠ℎ(𝑆𝑇𝐶), validated for c-Si technology. The final constraint is the relative efficiency loss under
low-in behavior ? Rs fit impacts greatly

low-light conditions (200 W/m², 25 °C) compared to STC

#### (Rel. eff. = 1 − 𝜂𝑙𝑜𝑤/𝜂𝑆𝑇𝐶.

This strongly helps to determine 2 𝑅𝑠since the power loss goes as 𝑃𝑙𝑜𝑠𝑠~ 𝐼 𝑅𝑠. Unfortunately, this information is almost never present in product datasheets and PVsyst assumes by default a value of −3% when no information is available based on previous experimental campaigns [2]. Since then, with the constant reduction in series resistance in PV manufacturing, driven by improvements in contact layer resistance, metallic grid conductivity and increased number of busbars, this relative efficiency has been decreasing consistently on average to values below −5% [9]. A lower bound of about −6.8% for this value can be estimated based on the measured series resistance of some best state-of-the-art c-Si solar cell [1]. Therefore, in the present study, recognizing the relative low light efficiency value of −3% as optimistic with currently available PV modules, we use a value of −4.5% when no other information can be assumed. The first set of constraints defines 1DM parameters with a degree of freedom, leaving the series resistance free up to a maximum value 𝑅. The additional constraint 𝑠,𝑚𝑎𝑥 imposed by the relative low-light efficiency fixes this value. However, in the case of high FF, not all values of relative low-light efficiency can be achieved while k respecting the other constraints [10]. In these cases, PVsyst will artificially increase the 𝑉𝑜𝑐value until it is possible to respect all the constraints, such as the MPP which is the first relevant information to preserve for accurate energy yield simulations. Such an example is presented in Figure 3, where we choose the extreme example of the above-mentioned certified record solar cell [1], leading to an inaccurate reproduction of the 𝑉. In comparison, fitting those data using either the reference 𝑜𝑐

recombination model of section 2.2 or a two-diode model allows an accurate reproduction of the 𝑉𝑜𝑐. This will be discussed further in the next sections.

tina

**Figure 3:** High FF solar cell certified data from *[1]* and

corresponding I-V curve estimation from PVsyst 8.0 1DM, a two-diode model and the intrinsic recombination model (“New Param”).

2.4 Alternative Parameter Evaluation To circumvent the limitations of the current 1DM parameters calculation of PVsyst, we propose a fitting method based on an Evolutionary Algorithm (EA). EA are popular to handle non-linear optimization problems and
020196-003

synthetically generated from the reference recombination model of section 2.2. This emulates a PV module with very high FF (85.7%) and very low relative low-light efficiency (−6.8%), which represents closely the best performance we could expect one day from c-Si PV module and serves as an extreme case to test the presented methods.

3.1 Evolutionary Algorithm Fit for One Diode Model and Standard Fill Factor
Figure 4 shows how the 1DM EA fit reproduces the
 measured data of the PERC device at all temperatures and

|irradiances available in its IEC 61853-1 report.||The|
|---|---|---|
|efficiency and the 𝑉 small discrepancy at low-light level can be seen. This is explained by the fact that the real measured relative low|are well fitted at 1000 W/m², but a||
|light efficiency assumed unavailable and the default value of −4.5% ±|for this device|was|
|2% was used instead according to our hypothesis||on|

𝑜𝑐

##### (−6.2% ± 1.2%)

|𝑃|||
|---|---|---|
|𝑚𝑝𝑝|𝑚𝑝𝑝,𝑓𝑖𝑡|𝑚𝑝𝑝|
|𝑉|||
|𝑜𝑐|𝑜𝑐,𝑓𝑖𝑡 𝑜𝑐||
|𝑉|||
|𝑠𝑐|𝑠𝑐,𝑓𝑖𝑡 𝑠𝑐||
|𝐼|||
|𝑃|𝑃 ,𝑓𝑖𝑡|𝑃|
|μ|||
|𝐼|𝐼 ,𝑓𝑖𝑡 𝐼||
|μ|||
|𝑉|𝑉 ,𝑓𝑖𝑡|𝑉|
|μ|||
||fit||

##### commonly available data.

용 sia

easily adaptable to various problem formulations. They are notably used by some PV module characterization centers in order to produce .PAN files reproducing as closely as possible IEC 61853-1 measured data. In this work, we use a penalty-based differential evolution algorithm which was shown to beat other evolutionary algorithms in reproducing the original two-diode model parameters of synthetically generated data [11]. Our EA fit works by optimizing the set of model parameters of the 1DM. Note that it can also be adapted to find the parameters of the recombination model of section

2.2. Based on the typical available information in product datasheet and low-light performance assumption to reproduce, we write a fitting objective function that needs to be minimized by an optimal set of parameters. This function is written as
1 𝐹 𝑜𝑏𝑗(𝑃𝑎𝑟𝑎𝑚𝑠) = (𝑃𝑚𝑝𝑝− 𝑃𝑚𝑝𝑝,𝑓𝑖𝑡)/𝑃𝑚𝑝𝑝 σ𝑃 𝑚𝑝𝑝 1 + (𝑉 − 𝑉)/𝑉 σ 𝑚𝑝𝑝 1 + (𝑉 − 𝑉)/𝑉 σ 𝑜𝑐 1 + (𝐼 − 𝐼)/𝐼 σ 𝑠𝑐 1 + (μ 𝑚𝑝𝑝 − μ 𝑚𝑝𝑝 ) /μ 𝑚𝑝𝑝 σ 𝑃𝑚𝑝𝑝 1 + (μ 𝑠𝑐 − μ 𝑠𝑐 )/μ 𝑠𝑐 σ 𝐼𝑠𝑐 1 + (μ 𝑜𝑐 − μ 𝑜𝑐 )/μ 𝑜𝑐 σ 𝑉𝑜𝑐 1 + (Rel. eff − Rel. eff)/Rel. eff σRel.eff where the subscript “fit” indicate the respective values computed by the chosen I-V model for a given set of parameters, the elements without subscripts are the measured values and the σ’s represent their respective standard deviation. The latter is of importance because some input data have much stronger experimental variations. For example, in the case of data obtained from IEC 61853-1 reports, three similar modules are measured. By analyzing reports from several test centers, we observed that while the STC values variation is well below 1% among the three modules, the variation in 𝜇𝐼 𝑠𝑐 is of the order of 10%. Likewise, when the low-light efficiency is unknown, we can more generally assume a value of −4.5% ± 2%, covering widely all the observable values reported in the literature [9]. Another advantage of this method is that it allows for the use of the 𝜇𝑉 𝑜𝑐 information. Note that any other available information that can be computed from an I-V model could be used in this objective function and it could therefore be adapted to reproduce all the measured elements of an IEC 61853-1 report.

**Figure 4**: Reproduction of measured IEC 61853-1 data

from the EA fit for a conventional FF (78.4%, PERC) based only on limited input (𝑃𝑚𝑝𝑝, 𝑉𝑚𝑝𝑝, 𝑉𝑜𝑐, 𝐼𝑠𝑐, 𝜇𝐼𝑠𝑐, 𝜇𝑉𝑜𝑐, 𝜇𝑃𝑚𝑝𝑝) and conventional assumption on low light efficiency (-4.5% +/- 2%) [9]*.*

Figure 5 shows how the measured parameters are

reproduced by (a) the current PVsyst method and (b) the EA fit with the 1DM. Both methods are in good agreement and reproduce the IEC MPP data within 2.5%. The EA fit reduces the error further, close to the tolerated standard deviation of each PV module characteristic. It provides better reproduction of the MPP and 𝑉𝑜𝑐data, their

##### 3 TEST SCENARIOS

In this section, two case studies are used to compare the parameter evaluation method of the current PVsyst model and the EA fit. In the first case, we focus on reproducing IEC 61853-1 certified data from a real PERC PV module, with a conventional FF value of 78.4%, based solely on the above-cited available information. In the second case, we repeat the operation with data

020196-004

temperature coefficients, and reduces error across all reduce this error below 0.5%, allowing a very good temperature and irradiance conditions. This is due to the reproduction of both 𝑃𝑚𝑝𝑝and 𝑉𝑜𝑐while keeping the same advantages of the EA fit, which leverages 𝜇𝑉 1DM parametrization as PVsyst. Using the same model 𝑜𝑐 parametrization as the reference one used for generating information, variations in 𝜇𝐼𝑠𝑐, and (often unknown) low- data yields even lower error on the 𝑉𝑜𝑐. However, the error light efficiency, whereas PVsyst discards the first and on the 𝑃𝑚𝑝𝑝becomes larger. We explained this by the fact assumes a fixed value for the others. that this parametrization is less flexible and cannot allow a relative low light efficiency too far from the requested −4.5% without creating discrepancies on the other parameters. Therefore, in the case of unknown low light efficiency, the 1DM parametrization seems the most adapted to reproduce well high FF PV module behavior over all conditions of interest.

**Figure 5:** Error from (a) the PVsyst calculated model

and (b) the EA fit model in reproducing the IEC 61853- 1 data. Pmpp, Vmpp, Voc and Isc refer to the STC conditions, MuPmpp, MuVoc and MuIsc to the temperature coefficients calculated at 1000 W/m² from the data at the different temperatures, VmppMatrix, VocMatrix, IscMatrix and EffMatrix to the corresponding average error in reproducing the data over all the temperatures and illumination, and RelEff_lowLight is the ratio of the efficiency at 1000 W/m² and 200 W/m² (at 25 °C)*.*

3.2 Fitting Synthetic Data for Hypothetical High Fill Factor Synthetic data for STC values, temperature coefficients and relative low-light efficiency were generated using the recombination model of section 2.2, using input parameters reproducing closely the certified measured data of [1]. Random errors on the temperature and irradiance were added to emulate measurement errors. This scenario raises a caveat, since we are attempting to fit data with a relative low-light efficiency of −6.8% while assuming 4.5% for a modern PV module.
Figure 6 shows the relative error in reproducing 𝑃𝑚𝑝𝑝
 and 𝑉𝑜𝑐at temperatures and irradiances relevant to PV system simulations for three approaches. The errors in reproducing 𝑃𝑚𝑝𝑝are small for each approach and mainly driven by the low light assumptions. The EA Fit improves even further the results as it does not impose a strict value for the low light efficiency. As expected for this test scenario, the error on 𝑉𝑜𝑐by the PVsyst calculation is large, up to 4%. Very interestingly, the EA fit manages to
##### 4 SUMMARY AND OUTLOOK

Accurately modelling PV module I–V curves across operating conditions remains a key challenge for yield simulations, especially for high-performance devices with high fill factors. The current PVsyst approach, based on direct parameter calculation for the one-diode model, provides reliable estimates but compromises open-circuit voltage reproduction when faced with high-FF technologies. In this work, we introduced an evolutionary algorithm to improve parameter evaluation for the one-diode model. On measured data from a standard PERC module, the EA fit reduced errors in maximum power point, open-circuit voltage, and temperature coefficients compared to the current method, while robustly handling measurement variability and unavailable low-light performance. For a synthetic high-FF case, the EA successfully lowered 𝑉𝑜𝑐 reproduction errors from several percent to below 0.5%, demonstrating its ability to capture the voltage-dependent recombination mechanisms characteristic of state-of-the- art c-Si devices. The results show that evolutionary algorithm provides a flexible framework that can estimate accurately PV performance at all relevant temperature and irradiance conditions based solely on available datasheet information and common low-light assumptions. It does so with greater accuracy than the current PVsyst deterministic calculation especially when low-light efficiency is unknown (leveraging *μVoc* and typical low-light trends). Importantly, even though the EA method already increases significantly the accuracy of the 1DM evaluation, it enables a straightforward extension to more advanced parametrizations. This general framework lays the groundwork for more accurate PVsyst .PAN files, ensuring robust energy yield simulations for the next generation of PV technologies. Future work will focus on validating the approach with high-FF commercial modules. The possible exploitation of the full IEC matrix also offers promising prospects. The sensitivity to missing or inconsistent data (e.g. product datasheet v.s. certified IEC report) should be studied in more details. Finally, this case study focused exclusively on PV modules of a single power class. Other power classes could not be evaluated due to the lack of certified measurements; however, it would be valuable to investigate them once manufacturers provide standardized data.

020196-005

**Figure 6**: Relative error on Voc and Pmpp in reproducing the synthetic data for relevant temperatures and irradiances, either

using the current PVsyt calculation with the 1DM, the EA fit with the 1DM, or the EA fit with the reference model parametrization (same as the one used for generating the synthetic data, denoted as “alternative parametrization”). The black dots references represent the mandatory measurement conditions within the IEC 61853-1 norm and the STC are marked by a red square.

##### 5 ACKNOWLEDGEMENTS

We acknowledge Sandia National laboratories, KIWA PVEL, Groundwork Renewables, Supsi PVLAB, and EPFL PV-LAB, for fruitful discussion and guidance on the topic.

REFERENCES

[1] H. Lin, G. Wang, Q. Su, C. Han, C. Xue, S. Yin, L. Fang, X. Xu and P. Gao, "Unveiling the mechanism of attaining high fill factor in silicon solar cells," *Progress in Photovoltaics: Research and* *Applications,* vol. 32, p. 359–371, June 2024. [2] A. Mermoud and T. Lejeune, "Performance assessment of a simulation model for PV modules of any available technology," 2010. [3] L. E. Black e D. H. Macdonald, «On the quantification of Auger recombination in crystalline silicon,» *Solar Energy Materials and Solar Cells,* vol. 234, p. 111428, January 2022. [4] T. Niewelt, B. Steinhauser, A. Richter, B. Veith- Wolf, A. Fell, B. Hammann, N. E. Grant, L. Black,

J. Tan, A. Youssef, J. D. Murphy, J. Schmidt, M. C. Schubert and S. W. Glunz, "Reassessment of the intrinsic bulk recombination in crystalline silicon," *Solar Energy Materials and Solar Cells,* vol. 235, p. 111467, January 2022.
[5] P. P. Altermatt, "Models for numerical device simulations of crystalline silicon solar cells—a review," *Journal of Computational Electronics,* vol. 10, p. 314–330, September 2011. [6] A. Schenk, "Finite-temperature full random-phase approximation model of band gap narrowing for silicon device simulation," *Journal of Applied* *Physics,* vol. 84, p. 3684–3695, October 1998.

[7] A. Richter, M. Hermle e S. W. Glunz, «Reassessment of the Limiting Efficiency for Crystalline Silicon Solar Cells,» *IEEE Journal of* *Photovoltaics,* vol. 3, p. 1184–1191, October 2013. [8] S. Schafer and R. Brendel, "Accurate Calculation of the Absorptance Enhances Efficiency Limit of Crystalline Silicon Solar Cells With Lambertian Light Trapping," *IEEE Journal of Photovoltaics,* vol. 8, p. 1156–1158, July 2018. [9] U. Kräling, P. Gebhardt, M. Kaiser and D. Philipp, "PV module performance measurements – statistical analysis of technological trends," 2022. [10] A. Bridel-Bertomeu, M. Oliosi, A. Mermoud and B. Wittmer, "Limits of the single diode model in view of its application to the latest PV cell technologies,"⑤

2023.
[11] K. Ishaque, Z. Salam, H. Taheri and A. Shamsudin, "A critical evaluation of EA computational methods for Photovoltaic cell parameter extraction based on two diode model," *Solar Energy,* vol. 85, p. 1768– 1779, September 2011.

020196-006
