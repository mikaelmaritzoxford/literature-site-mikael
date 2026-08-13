Renewable Energy 231 (2024) 120922

Contents lists available at ScienceDirect

# Renewable Energy

journal homepage: www.elsevier.com/locate/renene

# Experimentally validated thermal modeling for temperature prediction of photovoltaic modules under variable environmental conditions

a, b, * a, c d, e f, g Abdelhak Keddouda, Razika Ihaddadene, Ali Boukhari, Abdelmalek Atia, h, i d, f a, c Müslüm Arıcı, Nacer Lebbihiat, Nabila Ihaddadene a*University of M’Sila, Faculty of Technology, Department of Mechanical Engineering, PO Box 166, Ichebilia, 28000, M’Sila, Algeria* b*Laboratory of Materials and Mechanics of Structures (L.M.M.S), University of M’Sila, Algeria* c*Water, Environment and Renewable Energies Laboratory, University of M’Sila, M’Sila, Algeria* d*University of El Oued, Faculty of Technology, Department of Mechanical Engineering, 39000, El Oued, Algeria* e*Research and Development of Renewable Energies in Arid Zones, El Oued, 39000, Algeria* f*LEVRES Laboratory, Faculty of Technology, University of El Oued, 39000, El Oued, Algeria* g*UDERZA Unit, Faculty of Technology, University of El Oued, 39000, El Oued, Algeria* h*Kocaeli University, Faculty of Engineering, Department of Mechanical Engineering, 41001, Kocaeli, Turkey* i*International Joint Laboratory on Low-Carbon and New-Energy Nexus Research and Development, Kocaeli University, 41001, Kocaeli, Turkey*

ARTICLE INFO ABSTRACT

*Keywords:* In this work, a detailed analysis and thermal modeling for temperature prediction of a stand-alone photovoltaic PV module temperature module is performed. The study aims to present precise estimation of module temperature, since it is an Thermal modeling important parameter for power output calculation. Hence, the required data were collected via experiments. Prediction Accounting for all heat transfer mechanisms, and following model validation, a proposed algorithm was Ambient conditions implemented to investigate heat transfer from the module to its surrounding and predict different layers’ tem Heat loss coefficient perature. Results indicate that accurate energy distribution and temperature prediction was achieved by the adopted thermal model, only about 16% of the received energy is converted to electrical power while the rest is released by heat. Moreover, the proposed simulation algorithm provided one of the best results in comparison to literature models, achieving an *R*2of 0*.*963 and a *MAE* of 1*.*883, which is very close to the best overall model by King at *R²* = 0*.*973 and *MAE* = 1*.*663. Additionally, two new models for module temperature prediction were proposed. After testing on new data, the explicit model provided a reasonable first approximation attaining an adjusted *R*2of 0*.*97 and a *MSE* of 3*.*505, and an accurate implicit model, achieving a *MSE* of only 1*.*268.

**1. Introduction** and back sides of the module. In literature, various approaches have
been considered to calculate the temperature of photovoltaic modules, One of the key parameters in the performance of photovoltaic involving the dynamic energy balance method [9–11], data-driven modules, is the operating cell temperature, which plays a critical role in modeling [12–17], numerical methods [18–20], and thermal modeling the efficiency of solar-to-electrical energy conversion process [1–3], as well [21–24]. The following provides an overview of recent studies Therefore, it holds substantial amount of interest in literature [4]. that have considered these approaches. Considering that a significant portion of incident solar radiation is An early model for photovoltaic cell temperature was presented by transferred to the environment as heat, and that module temperature is Ross [25], a simply linear expression for cell temperature, stating that influenced by several environmental conditions, which can significantly the temperature difference between *Tcell*and *Ta*linearly depends on affect it, such as ambient temperature, wind speed, and solar radiation solar radiation (*G*) via a proportionality coefficient *k* in the range of 0*.*02 [5–8], different heat transfer mechanisms should be considered while to 0*.*04, later the range was extended upwards [26]. Another widely carrying out the energy balance for a photovoltaic module, aiming to used approach for *Tcell*calculation is the nominal operating cell tem calculate its temperature. Often, those mechanisms are present on top perature (NOCT) developed by Stultz [27] where solar radiation and

* Corresponding author. *E-mail address:* abdelhak.keddouda@univ-msila.dz (A. Keddouda).
[https://doi.org/10.1016/j.renene.2024.120922](https://doi.org/10.1016/j.renene.2024.120922) Received 28 February 2024; Received in revised form 19 June 2024; Accepted 3 July 2024 Available online 4 July 2024 0960-1481/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

*A. Keddouda et al. 5HQHZDEOH Energy 231 (2024) 120922* ambient temperature are used for estimating *Tcell*. Similar to Ross model, several models have been proposed in literature [28–32], basically expressing (*TcellTa*) as a function of *G*. Servant [33] presented a regression equation incorporating wind speed effects, and assuming a linear dependence on environmental parameters, which was found to agree with data from the experiments. Similarly, Lasnier [34] also established a model using regression analysis to approximate module temperature, considering it as function of solar irradiation and ambient temperature. King [35] established an experimental equation for mod ule temperature calculation, considering it to be correlated with ambient temperature, solar radiation, and also wind speed. Further more, TamizhMani et al. [36] investigated five and three-inputs models for the temperature of photovoltaic modules, with the latter accounts for basic environmental variables, while the former includes wind direction as well as relative humidity as inputs. Their findings showed that, solar radiation explains the raise in module temperature, ambient tempera ture sets its value, and wind speed tends to helps reduce it. Moreover, in another study, King et al. [37] suggested an analogous model that ac counts for build materials’ properties, and considers cell temperature to be related to module’s back-side temperature, in their study, they pro vided empirical coefficients for calculation. Besides that, King et al. [38] and Kurtz [39] proposed an additional correlation for cells temperature, analogous to their former model, this model considered the aforemen tioned parameters, and also takes module type and mounting configu ration into consideration. Mondol et al. [30] presented a correlation similar to Ross’s equation for module temperature estimation, associ ating the latter with ambient air temperature and irradiation. According to their findings, the proposed model yielded less predictive error in comparison to the NOCT analogy. Furthermore, Skoplaki et al. [40] offered a model equation for the temperature of photovoltaic modules, relating it to basic environmental variables. Their findings indicated that, while ignoring natural convection effects, the model error was within 3%, which could be further decreased by 1*.*4% with solar radi ation values of 600 – 1100 *W/m*2and wind speeds in the range of 1*.*2 to 4 *m/s*. Koehl et al. [41] considered the evaluation of photovoltaic module temperature using analytical and statistical models. They pro posed a realistic nominal module temperature (ROMT) rather than NOCT approach, finding that the proposed model tend to better corre late with the data from experimental measurements. Additionally, Almaktar et al. [42] specified that the temperature of photovoltaic modules can be correlated to ambient temperature directly, and pre sented regression-based correlations to evaluate it based on environ mental parameters, such as ambient temperature, solar radiation, and wind speed. Their findings indicated that their module temperature equations predicted the module temperature of different types with an acceptable error values, which tend to well agree with experimental data. Muzathik [14] presented a simple model equation based on a regression analysis for module temperature estimation, taking as inputs, ambient temperature, solar radiation, and wind speed. Findings revealed that the proposed model yielded a predictive error of about
2*.*85% in terms of root mean squared error (RMSE). Bailek et al. [12], suggested a model equation for back-side temperature of photovoltaic modules after testing several models. Their model considered ambient temperature and irradiation as inputs and was found to predict module temperature with a correlation coefficient of 0*.*955, and an error of 10%. Kaplanis et al. [43] studied the prediction of photovoltaic modules performance and temperature. accounting for several parameters, and after establishing a theoretical analysis, the authors presented an experimentally validated model for several mounting conditions. In comparison with comparable models, findings indicated that their model presented superior performance and lower error. Ceylan et al. [44] employed Artificial Neural Networks (ANNs) to predict module temperature, efficiency and power output, they used experimentally contained ambient temperature and irradiation to train the neural network. Cos¸ kun et al. [45] implemented Artificial Neural
Networks (ANNs) to predict the module’s surface temperature using ambient temperature, solar radiation, as well as wind speed. Following the evaluation of numerous training algorithms, the authors found that ANNs can precisely estimate photovoltaic modules temperature. More over, Sohani and Sayyaadi [46] carried out a study to determine the function shape and form via genetic programming, for module temper ature estimation. Considering standard climatic variables and relative humidity as inputs, they claimed that the proposed function had significantly better performance compared to models from literature such as the NOCT approach. Dong et al. [13] suggested a hybrid modeling technique aided by a radial basis function neural network for predicting photovoltaic module temperature. To enhance generaliz ability, they introduced a rectification factor based on the network output. According to their results, the proposed method significantly improved the accuracy of cell temperature predictions. Additionally, Dong et al. [47] suggested radial basis function neural network-based hybrid model for the prediction of photovoltaic module temperature. Based on an optimization model using *l*1norm penalty, the suggested model showed promising results and accurate predictions. Shiravi et al. [48] conducted an experimental study to investigate the effects of wind velocity and solar radiation intensity on photovoltaic modules perfor mance. By deriving equations for module temperature, power output and efficiency, they demonstrated that these factors can significantly influence the performance of photovoltaic modules. Another approach that was considered in the literature, for investigations into photovoltaic module temperature, power output, efficiency, and mounting conditions [49–52], as well as PV/thermal systems [53,54] is computational fluid dynamics (CFD) simulations. Lu and Zhao [51] considered investigating the effect of dust on photovoltaic modules performance using CFD simulation. According to their findings, module efficiency was reduced by dust deposition, where that effect depends on dust particles sizes. Similarly, the effect of wind on PV modules was also considered [55,56], where findings showed that wind speed influences both the pressure distribution on the PV module surface and the module’s cooling process. Hove [57] suggested that the temperature of the module can be approximated by conducting an energy balance for the photovoltaic module, where based on experimental data, the dissipated heat from the module can be computed. Additionally, Mattei et al. [58] also suggested a similar method using the energy balance approach to assess the photovoltaic module temperature. Their method incorporated an absorbance-transmittance coefficient (*τα*) of 0*.*81 and a loss coefficient derived from experimental measurements. The findings demonstrated that the model’s mean squared error (MSE) was 2.24◦C. Also, Tiwari and Sodha [59,60] used the energy balance approach to calculate the temperature of the modules (cells) in a photovoltaic-thermal (PVT) system. Their results indicated that a good agreement with experimental data was obtained for the system results. Moreover, Migliorini et al. [61] introduced a thermo-electrical model, which incorporates the dynamical behavior of photovoltaic modules. The model calculates module tem perature, which is then used to forecast its power output. The study results demonstrated a notable reduction in predictive error by ac counting for these crucial module dynamics. Furthermore, Akhsassi et al. [62] conducted an investigation using thermal modeling of photovoltaic modules, where they presented two different models, differentiated by whether a model accounts for the effect of wind or not. Their results revealed that the proposed models provided an enhanced performance compared to analogous models in literature. Besides that, Bevilacqua et al. [63] conducted a study using the finite difference method and the energy balance approach, with spray cooling, to examine the photovoltaic modules’ temperature. Their model was designed to present a thermal profile within the photovoltaic module. They found that spray cooling could reduce module temperature by

28.2 % and increase electric power output by up to 7.8 %. The literature survey presented above reveal that numerous studies about thermal-electrical modeling of photovoltaic modules can be found in literature [64–66]. However, it was found that, based on the carried

*5HQHZDEOH Energy 231 (2024) 120922*

survey of previous studies, module temperature calculation was mainly established via data-driven modeling. Additionally, the majority of other approaches were concentrating on a particular parameter, including wind speed and direction [67–69], and investigating building-integrated PV modules [70–72]. Moreover, in the literature, thermal radiation heat transfer and free convection, in many cases, were often neglected, which may be important at high temperatures or min imal wind speeds. Therefore, this work proposes a novel thermal model for module temperature prediction, seeking to bridge the gap and cover those deficiencies, and perform a detailed thermal modeling of free-standing photovoltaic modules based on adequate heat transfer principles and the energy balance method, with the objective of pre dicting photovoltaic module’s temperature at different layers, under time-varying ambient conditions. Several key advantages are presented in this work, such as considering the dynamical behavior of photovoltaic modules. Also, in this work, unlike many other studies, the heat dissi pation from the module to the surrounding involves free, forced, and mixed convection, in addition to radiative heat transfer. Additionally, the wind heat transfer coefficient in this work can take several function forms, where the best one will be selected for more accurate prediction of the wind heat transfer coefficient. Furthermore, this work aims to provide a comprehensive analysis of the heat loss from the module to its surrounding and quantify it for each mechanism. Beyond that, present study offers a simple but yet an effective and accurate modeling approach with the possibility of integrating the algorithm with effi ciency and power output calculation to evaluate the performance of photovoltaic modules Also, for engineering applications, this work aims to offer novel, reliable and exportable module temperature models. Besides, the work is also the first in south Algeria, in an arid climatic condition.

**2. Materials and methods**
*2.1. Experimental setup* With the focus on performing simulations to estimate photovoltaic module’s back-side (*Tback*) and cells temperature (*Tcell*), experimental measurements and in-situ ambient variables are needed. Thus, two identical polycrystalline silicon photovoltaic modules of

several parameters, such as solar radiation, ambient temperature, and wind speed. Thus, the standard heat transfer mechanisms should be considered while conducting the energy balance for the photovoltaic module to calculate its temperature. These mechanisms, normally, involve heat conduction, convection, and radiation, and take place on both sides of the module, i.e. front and back sides. The typical equation for an energy balance is as follows:

(*τα*)*G* = *ηpvG* + *Utop*(*TcellTa*) + *Uback*(*TcellTa*) (6)

It is worth noting that in Eq. (6), heat losses are stated with respect to *T* *a*for convenience. However, in fact, different heat exchanges between a photovoltaic module and its surrounding are as described in Fig. 2, where radiative heat transfer occurring on module’s top and back sides are considered with respect to *Tsky*and *Tgr*, respectively, which is the case considered in this work. In the first term of the right-hand side of Eq. (6), which stands for the module’s delivered power output, *ηpv*is the module efficiency, and it is given by Eq. (7):

())
*η* *PV*= *ηref*1 *μrefTcellTref*(7)

where *ηref*is the efficiency of the module at Standard Test Conditions, *T* *ref*is the temperature of the module at the reference state, *μref*is the temperature coefficient, this coefficient is taken to be constant in this work for simplicity. Details of the determination of *Utop*and *Uback*, as well as the heat conduction within the different layers of the module are presented in the following section.

**3. Thermal modeling** In this work, thermal modeling for photovoltaic modules is consid ered. The main objective is to determine convective and radiative heat losses from the module to its surrounding and model the heat transfer within the different layers of a photovoltaic module. Besides, the study investigates and predicts temperature profiles of module cells, top and back surfaces. This can eventually lead to estimating module tempera ture, its power output, and efficiency. Therefore, a thermal resistance model such as the one shown in Fig. 3 is proposed for investigation. The considered photovoltaic module comprises five distinct layers, namely, glass, Ethylene Vinyl Acetate (EVA), photovoltaic cells, EVA, and a back-
**Fig. 3.** Equivalent thermal resistances model.

sheet of Tedlar Polyester Tedlar (TPT), where the thickness and thermal conductivity of each layer are presented in Table 2.

*3.1. Convective heat losses* Convection heat transfers from the module to its surroundings is of primary importance when predicting *Tcell*. It is characterized by a heat transfer coefficient *hconv*on both sides of the module. Thus, it can be expressed generally by Newton’s law of cooling, which is given per unit area in Eq. (8). ʹʹ
) *q* = *hconvTsTf*(8)

where *Ts*and *Tf*are the solid and fluid temperature, respectively. The rate of convective heat transfer depends on ambient conditions, in this case, specifically the wind speed on the top and back sides of the photovoltaic module, where forced convection is expected for high *Ws* values.

*3.1.1. Forced convection* Over the photovoltaic module surface, *hconv*can be calculated using empirical correlations. Depending on flow conditions, the flow is considered fully laminar as the Reynolds number (*Re*) is in the range of 1 × 105, fully turbulent if *Re* number is greater than 3 × 106, and tran sitional flow in between [73]. Empirical correlations for *Nuave*for different flow conditions are as stated below [74], where *Nuave*number is given by:
**Table 2**
 Thickness and thermal conductivity for each module layer.

||Material|k W.m .K)|t (mm)|
|---|---|---|---|
||Glass|0.98|3.2|
||EVA|0.31|0.4|
|Fig. 2. Schematic representation of different heat exchanges between the|Cells|150|0|
|photovoltaic module and its surrounding.|TPT|0.23|0..4 35|
||4|||
 Material *k W.m.K*
) *t* (*mm*)

*h* *convL* *Nuave*= (9) *k* *f* For laminar flow:

*Nuave*= 0*.*664*Re¹* */*2 *Pr¹* */*3 (10)

For turbulent flow:

*Nuave*= 0*.*037*Re⁴* */*5 *Pr¹* */*3 (11)

For mixed boundary layers: 4*/*5 ) 1*/*3 *Nuave*= 0*.*037*Re A Pr* (12)

where *A* = 0*.*037*Re⁴c /* 5

0*.*664*Re⁰c.* 5, and *Rec*=5× 105. It is important
) to note that fluid (air) properties are calculated at *Tfilm*= *Ts*+ *Tf/* 2. Alternatively, different models are available in the literature (Table 3), which can be used to estimate *hconv*. Sparrow et al. [75,76] presented model equations for *hconv*of the form *j* = *aRbe*; where *j* = ) 2*/*3 *h* *conv/ρCpWsPr*. While Test et al. [77], Kumar et al. [78], and Jayamaha et al. [79] stated that wind heat transfer coefficient can be estimated using a simple linear equation, such as: *hconv*= *aWs*+ *b*. Additionally, Sartori [80] proposed that, based on Nusselt number correlations, *hconv*can be calculated using equations of the form *hconv*= *aWsLb*. Furthermore, details on calculation of *hconv*and its estimating equations can be found in Ref. [81].

*3.1.2. Free convection* For the back side of the module, a well-known correlation for *Nuave*is used to determine *hconv*for the entire range of *Ra* number, given in Eq. (30) considering that g is replaced by *gcos θ* and 0 *< θ <* 60◦, (*θ* is calculated from the vertical) [87,88]. (
1*/*6

)2
0*.*387(*RaLcos θ*)
*Nuave*= 0*.*825 + () 8*/*27 (30) 1 + (0*.*479*/Pr*) 9*/*16

) 3 where *RaL*= *GrPr* = *gβ TsTfL /να*, and *β* = 1*/Tfilm*. Additionally, Fujii and Imura [89,90] proposed that *Nuave*at the back surface of an

**Table 3**

Illustrative equations for the wind heat convection coefficient available in literature. No. Author(s) *hconv* equation *Ws* limit Eq. Ref. 1 Nusselt–Jurges *hconv* = 3*.*95*Ws* + 5*.*8 *Wss* ≤ 5 *m/s* (13) [81] 2 McAdams *hconv* = 3*.*8*Ws* +5*.*7 *W* ≤ 5 *m/s* (14) [82] 3 Sparrow et al. *j* = 0*.*86*R¹e /*2; )*j* = (15) [76] *h* *conv /ρCp Ws Pr²* */*3 4 Watmuff *hconv* = *Ws* + 2+*.*8 *Ws* ≤ *m* (16) [[83 5 Test et al. et al. *hconv* = 32*.*56*Ws Ws* ≤ 55 *m//s s* (17) 77]]

8*.*55
6 Kumar et al. *hconv* = 4*.*687*Ws* + *Ws* ≤ 5 *m/s* (18) [78]

10*.*03
7 Sharples and *hconv* = 2*.*2*Ws* + 8*.*3 *Ws* ≤ 6 *m/s* (19) [84] Charlesworth *hconv* = 3*.*3*Ws* + 6*.*5 (20) 8 Sartori *hconv* = 3*.*83*Ws L*0*..*5Lam. flow (21) [80] *h* *conv* = 5*.*74*Ws L* 02Turb. (22) *h* *conv* 5*.*74*Ws L*

0*.*2 Mixed flow flow (23)
16*.*46=*L*1
9 Kumar and *hconv* = 3*.*87*Ws* + 6*.*9 *Ws* ≤ 1*.*12 *m/s* (24) [85] Mullick *hconv* = 6*.L*63+ (25)

3*.*87*W⁰s.*8 0*.*2
10 Schott *hconv* = 5*.*79*W⁰s s.*8*L*0*.*2*Ws* ≥ 0*.*3 *m/s* (26) [31] 11 Jayamaha et al. *hconv* = 1*.*444*W* + *Ws* ≤ 4 *m/s* (27) [79] *.* Shakerin *j* = 1*. Re /*; *j* = (28) [86]

) (29)
*h* *conv /ρCp Ws Pr* *j* = 0*. Re* */*; ) *j* = *h* *conv /ρC W p s Pr*

inclined plate can be determined using Eq. (31) which holds for *RaLcos θ* ◦ values within 10 to 10 and for inclination angles above 2, whereas, Kaplani and Kaplanis [68] indicated that it can be used for about 30◦, while beyond that, Eq. (30) is recommended. 1*/*4 *Nuave*= 0*.*56(*RaLcos θ*) (31)

For the top side of the module, and because the PV module is typi cally at higher temperature than its surroundings, the boundary layers breaks, forming plumes on the module’s top side. Thus, the rate of heat transfer increases relatively to a vertically orientated plate [91]. Therefore, Fujii and Imura [89] indicated that Nusselt number for the top face of a hot inclined plate can be calculated using the following correlation:

*Nuave*= 0*.*13 *GrPr¹* */*3 *GrcPr¹* */*3

)+0
*.*56(*GrcPr cos θ*)
1*/*4 (32)

where *Grc*is the *Gr* number at which, the flow starts transitioning from laminar to turbulent behavior. Values for *Grc*that corresponds to different values of *θ* can be found in Refs. [68,90,92].

*3.1.3. Mixed convection* Convection is considered mixed when the effects of forced and free convection are comparable and neither of them can be neglected. Con vection is considered free when *Ri*≫1, forced when *Ri***≪**1, and mixed
2 if *Ri* number is in between those limits (*Ri* ∼ 1), where *Ri* = *Gr/Re*. The *Nuave*for mixed convection is given by Ref. [74]: ( *n n* ) 1*/n* *Nuave*= *Nuave,forced*+ *Nuave,free*(33)

The value of the exponent *n* is in the range of 3 to 4, and best results are obtained for *n* = 3, although values of 3*.*5 and 4 may be better suited for transverse flows involving horizontal plates and cylinders (or spheres), respectively [74].

*3.2. Radiative heat losses* In this work, in order to account for radiation heat transfer between the photovoltaic module and its surrounding, Eq. (34) is used to express radiative heat flux per unit area. ʹʹ = 4 4
) *q σϵ TsTsurr*(34)

Here, *σ* and *ϵ* are the Stefan-Boltzmann constant and material emissivity, respectively, while *Ts*represents the module’s top or back side temperature. *Tsky*was calculated using Eq. (35) [68], and *Tgr*was estimated using Eq. (36) [93], both represented by *Tsurr*in Eq. (34).

1*.*5
*T* *Sky*= 0*.*0552 *Ta*(35)

*T* = 17*.*898 + 0*.*951*T* (36) *gr a* It is worth noting that *Ta*, *Ts*, and *Tsurr*should be in Kelvin (*K*). Additionally, and since radiative heat transfer is a surface phenomenon and depends on the orientation of the surfaces, the concept of view factor was introduced to determine the fraction of the radiation leaving one surface that is intercepted by another surface. The view factor *F* must be taken into account, since they are relevant and critical in modeling the thermal behavior of photovoltaic modules, which can be calculated using Eqs. (37)–(40) [68,94]:

*F* = (1 + cos (*α*))*/* 2 (37) *f sky*

*F* *f gr*= (1 cos (*α*))*/* 2 (38)

*F* *b sky*= (1 + cos (*π α*))*/* (39)

*F* *b gr*= (1 cos (*π α*))*/* (40) Then, in this work heat transfer by radiation from the photovoltaic

module can be written alternatively in terms of a heat transfer coeffi cient *hrad*as follows: ʹʹ = *q hrad*(*TsTsurr*) (41)

where *hrad*is the radiative heat transfer coefficient, and takes the form of Eq. (42): 2 2 ) *h* *rad*=*Fσϵ Ts*+ *Tsur*(*Ts*+ *Tsur*) (42)

*3.3. Overall heat transfer coefficient* It can be noted that, from Eq. (6), a model equation for *Tcell*can be written in the form of Ross model [25], as it is shown in Eq. (43), where *T* *cellTa*is directly proportional to the incident solar radiation, and this proportional constant is known as *k*. *T* *cell*= *Ta*+ *kG* (43)
) Here, *k* is given by *τα ηpvG/Uloss*, and *Uloss*= *Utop*+ *Uback*. These two quantities are calculated from Eqs. (44) and (45), respectively.

[] *Utop*= + *Rcond.f*(44) *h* *conv.f*+ *hrad.f* []1 1 *Uback*= *h* + *h* + *Rcond.b*(45) *conv.b rad.b* However, determining the value of *Utop*and *Uback*for either sides of the module, implicitly necessitates finding the surface temperature. For example, for the top side, the heat loss per unite area from the photo voltaic cells at an average temperature of *Tcell*to the glass surface at the average temperature of *Ttop*is given by Eq. (46). From the glass to the surrounding at *Ta*and *Tsky*, respectively, it is given by Eq. (47):

*q* ʹʹ = 1 *T* *cellTtop* ) (46) *top* *Rcond.f*

*q* ʹʹ = *hconv.fTtopTa* ) + *h* *rad.fTtopTsky* ) (47) *top* Therefore, *Ttop*and *Tback*have to be found using an iterative or nu merical solution of Eqs. (46) and (47) for *hrad*and *Ttop*, and similarly for the back-side. The solution to all of these equations has to finally satisfy

**Fig. 4.**

Overall simulation algorithm procedure.

the energy balance equation (Eq. (43)), which is solved for *Tcell*. It is worth noting that *hrad*may be linearized to *Ta*for convenience [40,95].

*3.4. Proposed simulation algorithm* A predictive simulation algorithm for module temperature is pro posed in this work, as well as to investigate the heat transfer from the module to its surrounding, and the different heat transfer coefficients. To accomplish that, Fig. 4 illustrates the general workflow for the simulation, firstly, *Ta*, *Ws*and *G* are loaded, then the algorithm initiates the temperature at different layers of the module, namely *Ttop*, *Tback*, and *T* *cell*and finds *Tfilm*at both sides of the module. Then air properties are determined, and *Re*, *Gr*, *Ri*, and *Ra* are calculated, based on those quantities, the flow conditions are concluded. Afterwards, the algorithm calculates *hconv*and *hrad*based on initial *Ttop*and *Tback*. Once determined, it solves Eqs. (46) and (47) to correct the initial guess of *Ttop*and *Tback*, and then solves for *Tcell*using Eq. (43). Once the convergence criterion (1% error) is satisfied for each temperature value, the solution is considered as converged for that time step and moves on to the next one. If it is not the case, it updates the initial temperature values and goes through the loop again.
*3.5. Model validation* To validate thermal model in this work and assess its accuracy, simulations for the experiments conducted by Aly et al. [18] are carried out using experimental data from their study. Considering the same ambient temperature, solar irradiation, and wind speed conditions as of June 25, 2014, which are the model inputs. While the expected output is *T* *back*, and by employing the algorithm from this study to predict module temperature, it was observed that the present thermal model accurately estimates *Tback*with a high level of precision as it is shown in Fig. 5. Additionally, the results obtained by the simulation algorithm for the validation day was assessed in several ways. Firstly, it was found that the coefficient of determination (R
2 ) was at 0.986 with an adjusted R 2 of

0.984, indicating that the model successfully fits the predicted values with experimental data using the considered inputs. Secondly, using several error metrics, where it was found that predicted module tem perature was at 1.322, 1.556, and 2.420 in terms of MAE, RMSE, and MSE, respectively. Whereas the MAPE was at 3.56 % and the standard error was only of 1.624. Furthermore, the residuals of predicted module temperature shown in Fig. 5 reveals that, while only 12.5 % of predic tion error exceeds the 2.5◦C limit, only 2.08 % of that error is beyond the 3◦C. Moreover, the maximum relative error presented by the algo rithm simulation was only 0.947 %, which is less than its designed convergence criterion (1 %). These findings give credit for the suitability and reliability of the thermal model for the current investigation.
**4. Results and discussion** In this study, the prediction of photovoltaic module temperature is investigated using a simulation algorithm based on heat transfer prin ciples. Experimental dataset is utilized for the simulation, where *Ta*, *Ws*, *G*, as well as *Tback*were recorded from March 15, to 19, 2023. Fig. 6 shows the recorded data during that period, showcasing a typical trend where ambient conditions exhibit an increase in *Ta*and *G* from morning to noon time, followed by a decline towards evening time. While in contrast, *Ws*values, exhibits a stochastic behavior.
*4.1. Heat transfer analysis* To quantify the amount of energy loss from the module to the sur rounding, the heat flux leaving different surfaces of the module is determined in this work. Therefore, energy distribution is shown in
Fig. 7, revealing that a substantial portion of the energy received by the

**Fig. 5.** Validation of present thermal model against data of the study performed

by Aly et al. (a) experimental versus predicted values, and (b) residuals’ scatter plot [18].

module is released as heat. Mainly, as a significant radiative heat loss from the top side of the module at *Ttop*to the sky at *Tsky*. A similar amount of heat transfer occurs by the convection on both sides of the module, which is comparable to the radiative heat exchange (during sunny days) between the back side and ground at *Tback*and *Tgr*, respec tively. On an average, about 16 % of the total absorbed energy is con verted to electrical power by the module, while approximately 34 % of that energy is released to the surrounding through convection, specif ically, 15.8 % from the top side and 18.2 % by the module’s back side. The remaining 50 % is lost as radiative heat exchanges, with 35 % from the module’s top surface and about 15 % from the back surface, which reveals that most of the energy received is released in the form of heat, emphasizing the potential for applications like PV/thermal systems.

*4.2. Wind heat transfer coefficient* Due to its importance in predicting *Tback*, wind heat transfer coeffi

**Fig. 6.** Weather data recorded during March 15 to 19, 2023: (a) ambient temperature, (b) wind speed, (c) solar radiation and (d) module temperature.

**Fig. 7.** Energy distribution in the form of electrical power output and heat loss.

cient (*hconv*) is also investigated. Results of the simulation using experi with *hconv*estimated using Eq. (48) as well as that calculated by several mental data, and based on the aforementioned *Nuave*correlations, along models from literature, are shown in Fig. 8. As it can be seen from the figure, firstly, Eq. (48) aligns well with simulation results, and secondly, literature models deviate significantly from the current study’s results. However, the results obtained in this work perfectly cover the gap in literature models, since as it can be noted, the algorithm results and Eq. (48) are falling between values obtained by Sartori models for laminar and turbulent conditions, using Eq. (21) and (22), respectively. It is essential to note that in Eq. (48), omits the effect of radiation, and considers only one side of the module, accounting solely for convective heat transfer on that side.

1*.*048
*hconv*= 1*.*945*Ws*(48)

*4.3. Temperature prediction and model accuracy* The simulation results for the prediction of *Tback*using the algorithm developed in this study are compared with experimental values in Fig. 9. The results clearly demonstrate that simulation algorithm accurately predicts *Tback*, where the predicted temperature is in excellent agree ment with experimental data. This alignment indicates the algorithm’s proficiency in estimating module temperature under various climatic conditions. The algorithm, grounded on fluid flow and heat transfer principles, considers factors such as free convective and radiative heat transfer, as well as mixed convection and different boundary layer conditions (laminar, turbulent, and mixed). This comprehensive
**Fig. 8.** Comparison of wind heat transfer coefficient from present study with approach contributes to improved prediction accuracy, yielding well-

other from literature. estimated results of *Tback*. Additionally, the model’s ability to capture

**Fig. 9.** Comparison of experimental module temperature with the algorithm’s

predicted *Tpv*during March 15 to 19, 2023.

the intricacies of heat transfer mechanisms under diverse conditions is evident in its successful alignment with experimental observations. On the other hand, a slight deviation of the predicted module temperature from the experimental values was observed for the day of March 19,

2023. This is due to the stochastic and sudden changes in the climatic conditions, specifically in solar radiation for that particular day (Fig. 6). However, even under those conditions, the model provided reasonable approximation of *Tback*. Furthermore, the average deviation of the pre dicted module temperature for the day of March 19, 2023 was only
2.490◦C, which is within an acceptable margin of error. Statistical evaluation of the predicted *Tback*is performed to assess the performance of simulation algorithm. Fig. 10, presents a scatter plot of predicted versus measured *Tback*, indicating a clustered distribution around the perfect regression line of 45◦. The linear best fit, with an *R*2 of 0*.*963, suggests accurate predictions. Furthermore, the adjusted *R*2is also high at 0*.*957, signifying strong performance given the input vari ables. Additionally, in terms of error metrics, the predicted *Tback*was at
2.344, 1.883, and 5.495 in terms of RMSE, MAE, and MSE, respectively. Moreover, the standard error of predicted module temperature was at
2.345, while the MAPE was only 6.614 %, which is well below 10 % and indicates that current algorithm provides very accurate results. It was also found that over 96 % of predicted module temperature error was less than the threshold value of 5◦C, which is a widely accepted value that would produce less than 3 % error in photovoltaic power output prediction [35,38].
The simulation algorithm was designed to also allow for prediction of heat conduction within the photovoltaic module. Considering the March 17th, 2023 as a typical day, where temperature profiles at the photo voltaic module’s different layers are shown in Fig. 11, as it is expected, at the cells layer, higher temperature values are observed, while the module’s back-side has lower values, whereas the top-side exhibits the lowest temperature values. This is owing to the fact that, while neglecting material properties, heat must travel longer distances through modules layer of EVA, and glass compared to the thickness of EVA and back-sheet for the back side. Additionally, as it was revealed earlier, the heat loss by convection is almost similar on both sides of the module. However, radiative heat loss from the top side is much larger than that from the back-side. The maximum temperature difference ) (*TcellTback*) was found to be nearly 0*.*7◦*C*, while the *TcellTtop*dif ference was about 1*.*4◦*C*, these values fall in the intervals shown in the literature [52,94]. In addition, it can be seen from Fig. 11 that those differences correlate with *G* values, where typically larger values of *G* would produce larger temperature differences, and vice versa.

*4.4. Comparison with literature models* The performance of the simulation algorithm is compared with some temperature models from literature, including NOCT model, PVSyst’s model [96–98], and the model by Mattei [58]. Comparison of results in
Fig. 12 reveals that the presented algorithm is in good agreement with
 experimental data, as well as with literature models. However, as it can be noticed that generally, more accurate results are obtained using simulation algorithm from this study, as it presents one of the best overall performance in comparison to experimental data, outperforming almost all other models. Even under the condition of a cloudy day, where sudden changes in solar radiation are present, the algorithm still provides good and reasonable results. In more details, the NOCT model seems to significantly overestimate the module temperature under all conditions, while in contrast, PVSyst model provides good results under sunny day conditions, while significant error is observed by the latter under cloudy day situation. As per Mattei’s models, the predicted module temperature by this model is quite good during a cloudy day such as that of March 19, 2023. However, during other days where no clouds are present, the models is significantly underestimating the module temperature. On the other hand, the proposed simulation al gorithm, provided the good alignment with experimental under the conditions of sunny, and cloudy days as well. This is thanks to the fact that present thermal model considers the dynamical nature of the module behavior as well as the nature of its surrounding. In terms of statistical metrics, Table 4 shows an evaluation of simulation results and additional models from literature. The simulation algorithm exhibits a high *R*2of 0*.*963 and a high adjusted *R*2as well. Also, predictive error of simulation results was almost less than that of all considered models. Notably, the MAE of *Tback*resulted in from the current simulation was only 1.883. For other considered models, the lowest MAE was at 1.663 for King model while the highest was at 3.454 by Bailek et al. model. In terms of MSE, it was found that simulation
**Fig. 10.** Scatter plot of predicted versus experimentally measured module

temperature.

**Fig. 11.** Predicted temperature profiles at module top and back side and cells

layer during March 17, 2023.

**Fig. 12.** Comparison of simulation algorithm of present work with experimental data and other temperature models.

**Table 4**

Assessment for the performance of different models versus experimental. Model *R*2*adj R*2RMSE MAE MSE MAPE (%) Present **0.963 0.957 2.344 1.883 5.495 6.614** NOCT [18,27] 0.957 0.937 2.839 1.993 8.057 6.588 PVSyst [96,98] **0.962 0.960 2.245 1.757 5.039 6.007** TamizhMani 0.880 0.866 4.136 3.238 17.103 12.686 Mattei [58] [36] 0.968 0.921 3.172 2.468 10.062 7.703 Skoplaki et al. [40] 0.914 0.897 3.633 2.665 13.201 8.359 Bailek et al. [12] 0.963 0.853 4.334 3.454 18.781 10.855 King et al. [38] **0.973 0.966 2.068 1.663 4.277 5.843**

results yielded a MSE of 5.495, which is very close to 5.039 attained by PVSyst as the second-best result, while the largest MSE was resulted by Bailek et al. model at 18.781. More details about the statistical evalua tion of those models are presented in Table 4.

*4.5. Proposed models* Based on simulation results and the analysis performed in this study, in addition to the experimental data in hand, an exportable, explicit, and a quick-to-implement model to predict *Tcell*, which is similar to Eq. (43), is proposed. The model takes as inputs, *G* and *Ta*, where *k* takes the value of 0.023, which is about the daily-average value predicted by simulation and consistent with the values reported in literature. Thus, the proposed model takes the form of Eq. (49): *T* *cell*= *Ta*+ 0*.*023*G* (49) Although the model in Eq. (49) accounts implicitly for convection (wind effects) and radiation, taking *k* a constant value is not always the best solution. Therefore, an alternative form of such model is proposed to better account for the dynamics and changes in ambient conditions of *T* *a*, *Ws*.and *Tcell*. The suggested model may potentially take the form of Eq. (50): (
()))
*τα ηref*1 *μrefTcellTref* *T* *cell*= *Ta*+ *G* (50)

4*.*132*Ws*+ 0*.*088*Tcell*7*.*215
Here, *τα* takes the value of 0.81, *ηref*and *μref*represent the module efficiency and temperature coefficient at reference state, respectively, with *Tref*denoting the reference temperature (298*.*15 *K*). Since *Tcell*ap pears on both sides of Eq. (50), iterative solution must be implemented to calculate it. It should be pointed out that temperature values in Eq. (50) are in Kelvin and if it is used for *Tback*, values reported in literature and in this work for *Tcell*– *Tback*must be considered as well. To assess the performance of both models, different experimental data from

November 29, 2022 are utilized. The results yielded by Eqs. (49) and (50) are shown in Fig. 13, where it is evident that the implicit model excels in capturing the dynamics of *T* as a function of ambient con *cell* ditions, and efficiency.

Fig. 14 shows a Taylor diagram for evaluating the considered model

on the new dataset, indicating that the proposed models and algorithm are among the best approaches. The statistics of these models, reveal a similar *R*2of 0.99, and an adjusted *R*2of 0.989 and 0.970 for the implicit and explicit models, respectively. Furthermore, it was found that the MAE was 0.802 and 1.325, while the MSE was 1.268 and 3.505 for the same models, respectively. Moreover, the MAPE was at 3.036 % and

4.438 %, with a standard error of 1.127 and 1.874, for the implicit and explicit models, respectively. This indicates that Eq. (49) can be used for a rough approximation of *Tcell*or as a first guess for the implicit model. However, if more accurate results are desired, Eq. (50) is then recom mended. Generally, several advantages are presented in this work and the proposed models, compared to literature model, in particular, the simulation algorithm and the implicit model. First, and unlike PVSyst’s model, the present thermal model considers a variable photovoltaic module efficiency, which is more representative of a real module behavior, and similarly for the wind heat transfer coefficient, where it is considered either a linear function in wind speed at best, whereas, the default values in PVSyst assume no dependence on wind speed. On the other hand, the study by Sartori shows that it may take some power law function, while this work provides the possibility for the wind heat transfer coefficient to take any form based on a selected correlation and to evaluate the best form possible. Additionally, many other works appear to neglect radiation effects on module temperature, while it was considered in the proposed simulation algorithm and the implicit model as well. Furthermore, this work and its proposed simulation algorithm provides an energy balance analysis over the module and estimates energy losses within the system. Beyond that, the algorithm provides
**Fig. 13.** Comparison of proposed explicit and implicit models with experi
 mental data on new data.

**Fig. 14.** Taylor diagram for performance evaluation of simulation algorithm,

proposed and literature models on new dataset.

estimation of temperature of different surfaces of the PV module, namely top, cells, and back-side temperature.

**5. Conclusion** In this study, a simulation algorithm has been proposed to predict photovoltaic modules temperature utilizing experimental data collected during March 15 to 19, 2023. Following model validation, the module temperature was determined using the proposed algorithm, and comprehensive heat and energy transfer analyses were performed. In additions to comparison with models from the literature, statistical in dicators were implemented to assess the results. Based on the findings, the following concluding points are drawn:
- Grounded on fluid flow and heat transfer principles, the proposed algorithm yielded an accurate prediction of *Tback*, as well as *hconv*and *h* *rad*. Moreover, quantifying heat losses showed that only 16 % of energy in converted to electrical power, while the rest is lost by ra diation and convection at 50 and 34 %, respectively.
- In comparison to counterpart models and experimental data, the simulation-based *Tback*exhibited an excellent agreement with experimental data, positioning it as one of the most accurate modeling approaches.
- Statistically, simulation-based *Tback*yielded an *R*2of 0.963, an adjusted *R*2of 0.957, and a MAE of 1.883. In comparison, the best model from literature (King’s model), which achieved values of
0.973, 0.966 in terms of *R*2and adjusted *R²*, with MAE of 1.663.
- Based on the detailed analysis, two types of exportable models were proposed, an explicit model relating *Tcell*to *Ta*and *G* using coefficient *k* of 0.023 analogous to Ross model, and an implicit model that takes into account the dynamics of the phenomena, proving to provide very reasonable performance.
- The proposed implicit model, provided very reasonably accurate results, presenting an *R*2value of 0.99 and a similar adjusted *R²*, with a MAE of 0.802, when tested on new dataset. In conclusion, this work has conducted a detailed analysis and thermal modeling of photovoltaic modules resulting in highly accurate temperature predictions. Additionally, new and accurate temperature models have been proposed for engineering applications.
## CRediT authorship contribution statement

**Abdelhak Keddouda:** Writing – original draft, Validation, Software, Methodology, Investigation, Formal analysis, Conceptualization. **Razika Ihaddadene:** Writing – review & editing, Supervision, Project administration, Methodology, Investigation, Formal analysis, Concep tualization. **Ali Boukhari:** Writing – review & editing, Software, Methodology, Formal analysis, Conceptualization. **Abdelmalek Atia:** Writing – review & editing, Conceptualization. **Müslüm Arıcı:** Writing – review & editing, Methodology, Formal analysis. **Nacer Lebbihiat:** Writing – original draft, Investigation. **Nabila Ihaddadene:** Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

The first author thankfully acknowledges the support of Directorate- General for Scientific Research and Technological Development (Min istry of Higher Education and Scientific Research) for PhD scholarship and facilitating this research work.

**Nomenclature**

|||(|)|
|---|---|---|---|
|C|Specific heat capacity|J.kg|.K|
|F|View factor (|))||
|G|Solar radiation W.m||)|
|g|Gravitational acceleration m.s||)|
|h|Heat transfer coefficient W.m||.K)|
|k|Thermal conductivity W.m||.K|
|L|Module length (m)|||
|n|Number of attributes (|)|)|
|qʹʹ|Heat loss per unit area W.m|||
|T|Temperature (|C)||
|t|Thickness (mm)||)|
|U|Heat loss coefficient W.m||.K|

p 1 1

2 2 2 1 1 1

2 ◦

) WsWind speed m*.*s

|W|Wind speed m.s|||
|---|---|---|---|
|η|Module efficiency (|))||
|α|Thermal diffusivity m².s||)|
|β|Thermal expansion coefficient K|||
|ϵ|Surface emissivity (|)||
|η|Module efficiency (|)||
|μ|Temperature coefficient|( (% /K)|)|
|ν|Specific heat capacity|J.kg|.K|
|||)||
|ρ|Density kg.m||)|
|σ|Stefan-Boltzmann constant W.m||.K|
|τα Subscripts|Absorbance-transmittance coefficient (||)|
|a|Ambient|||
|ave|Average|||
|b/back|Back|||
|c|Cell/Critical|||
|conv|Convection|||
|exp|Experimental|||
|f|Front/Fluid|||
|film|Film|||
|gr|Ground|||
|pred|Predicted|||
|rad|Radiation|||
|ref|Reference state|||
|s|Speed/Solid|||
|sky|Sky|||
|surr|Surrounding|||
|t/top Abbreviations|Top|||
|ANN|Artificial Neural Network|||
|Gr|Grashof number|||
|MAE|Mean Absolute Error|||
|MAPE|Mean Absolute Percentage Error|||
|MSE|Mean Squared Error|||
|NOCT|Nominal operating cell temperature|||
|Pr|Prandtl number|||
|PV|Photovoltaic|||
|Ra|Rayleigh number|||
|Re|Reynolds number|||
|Ri|Richardson number|||
|RMSE|Root Mean Squared Error|||
|STC|Standard Test Conditions|||

1 1

1 1 3 2 4

**References**

[1] Y. Gong, Z. Wang, Z. Lai, M. Jiang, TVACPSO-assisted analysis of the effects of temperature and irradiance on the PV module performances, Energy 227 (2021) 120390. [2] D. Govindasamy, F. Daniel, A. Kumar, Performance enhancement of photovoltaic system using composite phase change materials, Energy 288 (2024) 129871. [3] A. Keddouda, R. Ihaddadene, A. Boukhari, A. Atia, M. Arıcı, N. Lebbihiat,

N. Ihaddadene, Solar photovoltaic power prediction using artificial neural network and multiple regression considering ambient and operating conditions, Energy Convers. Manag. 288 (2023) 117186.
[4] E. Skoplaki, J.A. Palyvos, Operating temperature of photovoltaic modules: a survey of pertinent correlations, Renew. Energy 34 (1) (2009) 23–29. [5] K. Hasan, S.B. Yousuf, M.S.H.K. Tushar, B.K. Das, P. Das, M.S. Islam, Effects of different environmental and operational factors on the PV performance: a comprehensive review, Energy Sci. Eng. 10 (2) (2022) 656–675. [6] R. Korab, M. Połomski, T. Naczynski, ´ T. Kandzia, A dynamic thermal model for a photovoltaic module under varying atmospheric conditions, Energy Convers. Manag. 280 (2023) 116773. [7] E. Skoplaki, J.A. Palyvos, On the temperature dependence of photovoltaic module electrical performance: a review of efficiency/power correlations, Sol. Energy 83

(5) (2009) 614–624.
[8] K. Vidyanandan, An overview of factors affecting the performance of solar PV systems, Energy Scan 27 (28) (2017) 216. [9] S. PV Kaplanis, temperatures

E. Kaplani, taking A into new account
dynamic the model environmental to predict conditions, transient and Energies steady 12 state

(1)
(2018) 2. [10] D.T. Lobera, S. Valkealahti, Dynamic thermal model of solar PV systems under varying climatic conditions, Sol. Energy 93 (2013) 183–194. [11] G. Osma-Pinto, G. Ordo´nez-Plata, ˜ Dynamic thermal modelling for the prediction of the operating temperature of a PV panel with an integrated cooling system, Renew. Energy 152 (2020) 1041–1054. [12] N. Bailek, K. Bouchouicha, M.A. Hassan, A. Slimani, B. Jamil, Implicit regression- based correlations to predict the back temperature of PV modules in the arid region of south Algeria, Renew. Energy 156 (2020) 57–67. [13] X.-J. Dong, J.-N. Shen, G.-X. He, Z.-F. Ma, Y.-J. He, A general radial basis function neural network assisted hybrid modeling method for photovoltaic cell operating temperature prediction, Energy 234 (2021) 121212. [14] A. Muzathik, Photovoltaic modules operating temperature estimation using a simple correlation, Int. J. Energy Eng. 4 (4) (2014) 151. [15] D.P.N. Nguyen, K. Neyts, J. Lauwaert, Proposed models to improve predicting the operating temperature of different photovoltaic module technologies under various climatic conditions, Appl. Sci. 11 (15) (2021) 7064. [16] A. Ziane, R. Dabou, A. Necaibia, N. Sahouane, M. Mostefaoui, A. Bouraiou,

S. Khelifi, A. Rouabhia, M. Blal, Tree-based ensemble methods for predicting the

module temperature of a grid-tied photovoltaic system in the desert, Int. J. Green Energy 18 (13) (2021) 1430–1440. [17] A. Keddouda, R. Ihaddadene, A. Boukhari, A. Atia, M. Arıcı, N. Lebbihiat,

N. Ihaddadene, Photovoltaic module temperature prediction using various machine learning algorithms: performance evaluation, Appl. Energy 363 (2024) 123064.
[18] S.P. Aly, S. Ahzi, N. Barth, A. Abdallah, Using energy balance method to study the thermal behavior of PV panels under time-varying field conditions, Energy Convers. Manag. 175 (2018) 246–262. [19] M. Prilliman, J.S. Stein, D. Riley, G. Tamizhmani, Transient weighted moving- average model of photovoltaic module back-surface temperature, IEEE J. Photovoltaics 10 (4) (2020) 1053–1060. [20] J. Zhou, Q. Yi, Y. Wang, Z. Ye, Temperature distribution of photovoltaic module based on finite element simulation, Sol. Energy 111 (2015) 97–103. [21] M. Abdolzadeh, T. Zarei, Optical and thermal modeling of a photovoltaic module and experimental evaluation of the modeling performance, Environ. Prog. Sustain. Energy 36 (1) (2017) 277–293. [22] A. Gholami, M. Ameri, M. Zandi, R.G. Ghoachani, Electrical, thermal and optical modeling of photovoltaic systems: step-by-step guide and comparative review study, Sustain. Energy Technol. Assessments 49 (2022) 101711. [23] W. Gu, X. Wang, X. Bai, Coupled optical-electrical-thermal loss modelling and energy distributions of a photovoltaic module, Energy Convers. Manag. 276 (2023) 116476. [24] A. Hassan, S. Abbas, S. Yousuf, F. Abbas, N. Amin, S. Ali, M.S. Mastoi, An experimental and numerical study on the impact of various parameters in improving the heat transfer performance characteristics of a water based photovoltaic thermal system, Renew. Energy 202 (2023) 499–512. [25] R. Ross Jr., Interface design considerations for terrestrial solar cell modules, in: 12th Photovoltaic Specialists Conference, 1976, pp. 801–806. [26] T. Nordmann, L. Clavadetscher, Understanding temperature effects on PV system performance, in: 3rd World Conference onPhotovoltaic Energy Conversion, 2003, Proceedings of, IEEE, 2003, pp. 2243–2246. [27] J.W. Stultz, Thermal and other tests of photovoltaic modules performed in natural sunlight, J. Energy 3 (6) (1979) 363–372. [28] J.D. Mondol, Y. Yohanis, M. Smyth, B. Norton, Long-term validated simulation of a building integrated photovoltaic system, Sol. Energy 78 (2) (2005) 163–176. [29] J.D. Mondol, Y.G. Yohanis, B. Norton, The effect of low insolation conditions and inverter oversizing on the long-term performance of a grid-connected photovoltaic system, Prog. Photovoltaics Res. Appl. 15 (4) (2007) 353–368. [30] J.D. Mondol, Y.G. Yohanis, B. Norton, Comparison of measured and predicted long term performance of grid a connected photovoltaic system, Energy Convers. Manag. 48 (4) (2007) 1065–1080. [31] T. Schott, Operation temperatures of pv modules: a theoretical and experimental approach, EC Photovoltaic solar energy conference 6 (1985) 392–396. [32] W. Durisch, B. Bitnar, J.-C. Mayor, H. Kiess, K.-h. Lam, J. Close, Efficiency model for photovoltaic modules and demonstration of its application to energy yield estimation, Sol. Energy Mater. Sol. Cell. 91 (1) (2007) 79–84. [33] J.-M. Servant, Calculation of the cell temperature for photovoltaic modules from climatic data, in: Intersol Eighty Five, Elsevier, 1986, pp. 1640–1643. [34] F. Lasnier, in: Photovoltaic Engineering Handbook, CRC Press, 1990. [35] D.L. King, Photovoltaic module and array performance characterization methods for all system operating conditions, in: AIP Conference Proceedings, American Institute of Physics, 1997, pp. 347–368. [36] G. TamizhMani, L. Ji, Y. Tang, L. Petacci, C. Osterwald, Photovoltaic module thermal/wind performance: long-term monitoring and model development for energy rating, in: NCPV and Solar Program Review Meeting Proceedings, 24-26 March 2003, National Renewable Energy Lab., Denver, Colorado (CD-ROM), 2003. Golden, CO.(US). [37] D.L. King, J.A. Kratochvil, W.E. Boyson, Field Experience with a New Performance Characterization Procedure for Photovoltaic Arrays, Sandia National Lab.(SNL- NM), Albuquerque, NM (United States), 1997. [38] D.L. King, J.A. Kratochvil, W.E. Boyson, Photovoltaic Array Performance Model,

2004. Citeseer.
[39] S. Kurtz, K. Whitfield, D. Miller, J. Joyce, J. Wohlgemuth, M. Kempe, N. Dhere,

N. Bosco, T. Zgonena, Evaluation of high-temperature exposure of rack-mounted photovoltaic modules, in: 2009 34th IEEE Photovoltaic Specialists Conference (PVSC), IEEE, 2009, 002399-002404.
[40] E. Skoplaki, A. Boudouvis, J. Palyvos, A simple correlation for the operating temperature of photovoltaic modules of arbitrary mounting, Sol. Energy Mater. Sol. Cell. 92 (11) (2008) 1393–1402. [41] M. Koehl, M. Heck, S. Wiesmeier, J. Wirth, Modeling of the nominal operating cell temperature based on outdoor weathering, Sol. Energy Mater. Sol. Cell. 95 (7) (2011) 1638–1646. [42] M. Almaktar, H.A. Rahman, M.Y. Hassan, S. Rahman, Climate-based empirical model for PV module temperature estimation in tropical environment, Appl. Sol. Energy 49 (2013) 192–201. [43] S. Kaplanis, E. Kaplani, J. Kaldellis, PV temperature and performance prediction in free-standing, BIPV and BAPV incorporating the effect of temperature and inclination on the heat transfer coefficients and the impact of wind, efficiency and ageing, Renew. Energy 181 (2022) 235–249. [44] I. ˙ Ceylan, O. Erkaymaz, E. Gedik, A.E. Gürel, The prediction of photovoltaic module temperature with artificial neural networks, Case Stud. Therm. Eng. 3 (2014) 11–20. [45] C. Coskun, N. Koçyigit, ˘ Z. Oktay, Estimation of pv module surface temperature using artificial neural networks, Mugla Journal of Science and Technology 2 (2) (2016) 15–18.

[46] A. Sohani, H. Sayyaadi, Employing genetic programming to find the best correlation to predict temperature of solar photovoltaic panels, Energy Convers. Manag. 224 (2020) 113291. [47] X.-J. Dong, J.-N. Shen, Z.-F. Ma, Y.-J. He, Simultaneous operating temperature and output power prediction method for photovoltaic modules, Energy 260 (2022) 124909. [48] A.H. Shiravi, M. Firoozzadeh, M. Lotfi, Experimental study on the effects of air blowing and irradiance intensity on the performance of photovoltaic modules, using central composite design, Energy 238 (2022) 121633. [49] N. Dabaghzadeh, M. Eslami, Temperature distribution in a photovoltaic module at various mounting and wind conditions: a complete CFD modeling, J. Renew. Sustain. Energy 11 (5) (2019). [50] M. Jaszczur, J. Teneta, Q. Hassan, E. Majewska, R. Hanus, An experimental and numerical investigation of photovoltaic module temperature under varying environmental conditions, Heat Tran. Eng. 42 (3–4) (2021) 354–367. [51] H. Lu, W. Zhao, CFD prediction of dust pollution and impact on an isolated ground- mounted solar photovoltaic system, Renew. Energy 131 (2019) 829–840. [52] A. Keddouda, R. Ihaddadene, A. Boukhari, A. Atia, M. Arıcı, N. Lebbihiat,

N. Ihaddadene, Experimental and numerical modeling of photovoltaic modules temperature under varying ambient conditions, Energy Convers. Manag. 312 (2024) 118563.
[53] M. Herrando, G. Fantoni, A. Cubero, R. Simon-Allu ´ ´e, I. Guedea, N. Fueyo, Numerical analysis of the fluid flow and heat transfer of a hybrid PV-thermal collector and performance assessment, Renew. Energy 209 (2023) 122–132. [54] M.A. Yildirim, A. Cebula, A numerical and experimental analysis of a novel highly- efficient water-based PV/T system, Energy 289 (2024) 129875. [55] A. Abiola-Ogedengbe, H. Hangan, K. Siddiqui, Experimental investigation of wind effects on a standalone photovoltaic (PV) module, Renew. Energy 78 (2015) 657–665. [56] M.G. Chowdhury, D. Goossens, H. Goverde, F. Catthoor, Experimentally validated CFD simulations predicting wind effects on photovoltaic modules mounted on inclined surfaces, Sustain. Energy Technol. Assessments 30 (2018) 201–208. [57] T. Hove, A method for predicting long-term average performance of photovoltaic systems, Renew. Energy 21 (2) (2000) 207–229. [58] M. Mattei, G. Notton, C. Cristofari, M. Muselli, P. Poggi, Calculation of the polycrystalline PV module temperature using a simple method of energy balance, Renew. Energy 31 (4) (2006) 553–567. [59] A. Tiwari, M. Sodha, Performance evaluation of solar PV/T system: an experimental validation, Sol. Energy 80 (7) (2006) 751–759. [60] A. Tiwari, M. Sodha, Performance evaluation of hybrid PV/thermal water/air heating system: a parametric study, Renew. Energy 31 (15) (2006) 2460–2474. [61] L. Migliorini, L. Molinaroli, R. Simonetti, G. Manzolini, Development and experimental validation of a comprehensive thermoelectric dynamic model of photovoltaic modules, Sol. Energy 144 (2017) 489–501. [62] M. Akhsassi, A. El Fathi, N. Erraissi, N. Aarich, A. Bennouna, M. Raoufi,

A. Outzourhit, Experimental investigation and modeling of the thermal behavior of a solar PV module, Sol. Energy Mater. Sol. Cell. 180 (2018) 271–279.
[63] P. Bevilacqua, R. Bruno, A. Rollo, V. Ferraro, A novel thermal model for PV panels with back surface spray cooling, Energy 255 (2022) 124401. [64] W. Gu, T. Ma, L. Shen, M. Li, Y. Zhang, W. Zhang, Coupled electrical-thermal modelling of photovoltaic modules under dynamic conditions, Energy 188 (2019) 116043. [65] T. Ma, Z. Guo, L. Shen, X. Liu, Z. Chen, Y. Zhou, X. Zhang, Performance modelling of photovoltaic modules under actual operating conditions considering loss mechanism and energy distribution, Appl. Energy 298 (2021) 117205. [66] X. Ma, M. Li, Y. Peng, L. Sun, C. Chen, Development of thermo–electrical loss model for photovoltaic module with inhomogeneous temperature, Energy 248 (2022) 123542. [67] H. Goverde, D. Goossens, J. Govaerts, V. Dubey, F. Catthoor, K. Baert,

J. Poortmans, J. Driesen, Spatial and temporal analysis of wind effects on PV module temperature and performance, Sustain. Energy Technol. Assessments 11 (2015) 36–41.
[68] E. Kaplani, S. Kaplanis, Thermal modelling and experimental assessment of the dependence of PV module temperature on wind velocity and direction, module orientation and inclination, Sol. Energy 107 (2014) 443–460. [69] C. Schwingshackl, M. Petitta, J.E. Wagner, G. Belluardo, D. Moser, M. Castelli,

M. Zebisch, A. Tetzlaff, Wind effect on PV module temperature: analysis of different techniques for an accurate estimation, Energy Proc. 40 (2013) 77–86.
[70] P.A. Mirzaei, R. Zhang, Validation of a climatic CFD model to predict the surface temperature of building integrated photovoltaics, Energy Proc. 78 (2015) 1865–1870. [71] D. Roeleveld, G. Hailu, A. Fung, D. Naylor, T. Yang, A. Athienitis, Validation of computational fluid dynamics (CFD) model of a building integrated photovoltaic/ thermal (BIPV/T) system, Energy Proc. 78 (2015) 1901–1906. [72] R. Zhang, P.A. Mirzaei, J. Carmeliet, Prediction of the surface temperature of building-integrated photovoltaics: development of a high accuracy correlation using computational fluid dynamics, Sol. Energy 147 (2017) 151–163. [73] Y.A. Çengel, J.M. Cimbala, in: Fluid Mechanics: Fundamentals and Applications, forth ed., McGraw-Hill Education, New York, 2018. [74] T.L. Bergman, Fundamentals of Heat and Mass Transfer, John Wiley & Sons, 2011. [75] E. Sparrow, K. Tien, Forced Convection Heat Transfer at an Inclined and Yawed Square Plate—Application to Solar Collectors, 1977. [76] E.M. Sparrow, J. Ramsey, E. Mass, Effect of Finite Width on Heat Transfer and Fluid Flow about an Inclined Rectangular Plate, 1979. [77] F. Test, R. Lessmann, A. Johary, Heat transfer during wind flow over rectangular bodies in the natural environment, J. Heat Tran. (1981) 262–267.

[78] S. Kumar, V. Sharma, T. Kandpal, S. Mullick, Wind induced heat losses from outer cover of solar collectors, Renew. Energy 10 (4) (1997) 613–616. [79] S. Jayamaha, N. Wijeysundera, S. Chou, Measurement of the heat transfer coefficient for walls, Build. Environ. 31 (5) (1996) 399–407. [80] E. Sartori, Convection coefficient equations for forced air flow over flat surfaces, Sol. Energy 80 (9) (2006) 1063–1071. [81] J. Palyvos, A survey of wind convection coefficient correlations for building envelope energy systems’ modeling, Appl. Therm. Eng. 28 (8–9) (2008) 801–808. [82] W.H. McAdams, in: Heat Transmission, third ed., McGraw-Hill, Tokyo, Japan,

1954.
[83] J. Dw, P. Wws C, Solar and wind induced external coefficients for solar collectors. Coop Mediterr Pour l’Energie Solaire, Rev Int d’Heliotechnique 2 (1977) 56. [84] S. Sharples, P. Charlesworth, Full-scale measurements of wind-induced convective heat transfer from a roof-mounted flat plate solar collector, Sol. Energy 62 (2) (1998) 69–77. [85] S. Kumar, S. Mullick, Wind heat transfer coefficient in solar collectors in outdoor conditions, Sol. Energy 84 (6) (2010) 956–963. [86] S. Shakerin, Wind-related Heat Transfer Coefficient for Flat-Plate Solar Collectors,

1987.
[87] Y.A. Çengel, A.J. Ghajar, in: Heat and Mass Transfer: Fundamentals and Applications, sixth ed., McGraw-Hill Education, 2020. [88] S.W. Churchill, H.H. Chu, Correlating equations for laminar and turbulent free convection from a vertical plate, Int. J. Heat Mass Tran. 18 (11) (1975) 1323–1329.

[89] T. Fujii, H. Imura, Natural-convection heat transfer from a plate with arbitrary inclination, Int. J. Heat Mass Tran. 15 (4) (1972) 755–767. [90] A. Bejan, A.D. Kraus, in: Heat Transfer Handbook, John Wiley & Sons, 2003. [91] Y. Cengel, J. Cimbala, R. Turner, in: Fundamentals of Thermal-Fluid Sciences, fifth ed. ed., McGraw Hill, 2017. [92] S. Armstrong, W. Hurley, A thermal model for photovoltaic panels under varying atmospheric conditions, Appl. Therm. Eng. 30 (11–12) (2010) 1488–1495. [93] M. Ouzzane, P. Eslami-Nejad, M. Badache, Z. Aidoun, New correlations for the prediction of the undisturbed ground temperature, Geothermics 53 (2015) 379–384. [94] E. Kaplani, S. Kaplanis, PV module temperature prediction at any environmental conditions and mounting configurations, in: Renewable Energy and Sustainable Buildings: Selected Papers from the World Renewable Energy Congress WREC 2018, Springer, 2020, pp. 921–933. [95] D.Y. Goswami, Principles of Solar Engineering, CRC press, 2022. [96] L. Deville, M. Theristis, B.H. King, T.L. Chambers, J.S. Stein, Open-source photovoltaic model pipeline validation against well-characterized system data, Prog. Photovoltaics Res. Appl. 32 (5) (2024) 291–303. [97] M. Dorenk ¨ amper, ¨ M.M. de Jong, J. Kroon, V.S. Nysted, J. Selj, T. Kjeldstad, Modeled and measured operating temperatures of floating PV modules: a comparison, Energies 16 (20) (2023) 7153. [98] A. Mermoud, B. Wittmer, PVSYST User’s Manual, Switzerland, January, 2014.
