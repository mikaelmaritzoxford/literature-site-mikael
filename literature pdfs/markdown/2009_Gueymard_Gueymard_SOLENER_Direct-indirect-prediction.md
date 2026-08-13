Available online at www.sciencedirect.com

Solar Energy 83 (2009) 432–444 www.elsevier.com/locate/solener

# Direct and indirect uncertainties in the prediction of tilted irradiance for solar engineering applications

## Christian A. Gueymard

*

Solar Consulting Services, P.O. Box 392, Colebrook, NH 03576, USA

Received 22 March 2008; received in revised form 17 September 2008; accepted 13 November 2008 Available online 4 December 2008

Communicated by: Associate Editor David Renne

Abstract

Global radiation measured on fixed-tilt, south-facing planes (40 and vertical) and a 2-axis tracker at NREL’s Solar Radiation Research Lab. in Golden, CO is compared to predictions from ten transposition models, in combination with either optimal or subop- timal input data of horizontal irradiance. Suboptimal inputs are typically used in everyday engineering calculations, for which the nec- essary data are usually unavailable for the site under scrutiny, and must be estimated in some way. The performance of the transposition models is first evaluated for ideal conditions when optimal data are used. In this specific case, it is found that the Gueymard and Perez models provide the best estimates of global tilted irradiance under clear skies in particular. The performance of four direct/diffuse separation models is also evaluated. Their predictions of direct and diffuse radiation appear biased in most cases, with a model-dependent magnitude. Finally, the performance of the resulting combinations of separation and trans- position models is analyzed in a variety of situations. When only global irradiance is known, the accuracy of the tilted irradiance pre- dictions degrades significantly, and is mainly conditioned by the local performance of the direct/diffuse separation method. For the south-facing vertical surface, inaccuracies in the ground reflection calculations becomes another key factor and significantly increase the prediction error. The Reindl transposition algorithm appears to perform best in this case. When using suboptimal input data for the prediction of plane-of-array irradiance on a moderately tilted plane (40 S) or a 2-axis tracking plane, the Hay, Reindl and Skartveit models are less penalized than others and tend to perform better. It is concluded that further research should be conducted to improve the overall process of predicting irradiance on tilted planes in realistic situations where no local high-quality irradiance or albedo mea- surements are available. 2008 Elsevier Ltd. All rights reserved.

Keywords: Solar radiation; Irradiance; Direct and diffuse radiation; Tilted irradiance; Ground albedo; Reflectance

1. Introduction
ety of tilt angles in atria. Prediction of the irradiance inci- dent on such tilted surfaces is key to the evaluation of the Accurate solar radiation resource data are necessary at effective solar resource and of the performance of all these various steps of the design, simulation, and performance systems. Because of the usual lack of measured data at the evaluation of any project involving solar energy. Solar project’s site, the solar resource needs to be modeled in energy systems are installed on either fixed tilted planes most cases. Various models can be used, depending on or tracking receivers. Similarly, glazed envelopes are the time resolution (e.g., hourly or monthly mean) and installed vertically on the facades of buildings or at a vari-on the type of available input data (e.g., meteorological information or global irradiance on the horizontal). A typology of such models has been proposed recently (Gue- * Tel.: +1 603 2378550; fax: +1 603 237 5314.ymard and Myers, 2008a). Monthly and hourly datasets of E-mail address: Chris@SolarConsultingServices.com global radiation on the horizontal can now be found from

0038-092X/$ - see front matter 2008 Elsevier Ltd. All rights reserved. doi:10.1016/j.solener.2008.11.004

C.A. Gueymard / Solar Energy 83 (2009) 432–444
various sources, such as NASA’s SSE (Stackhouse et al.,

2006), NREL’s NSRDB (NREL, 1995) and SWERA (Ren- ne´ et al., 2005). These and other sources of measured or modeled data are described elsewhere (Gueymard and Myers, 2008b). Before the prediction of tilted (or ‘‘plane-of-array”) irra- diance can be attempted in practice, a first series of models is generally needed to predict the global irradiance on the horizontal and the direct irradiance on a plane perpendic- ular to the sun rays, or direct normal irradiance (DNI). If DNI predictions are accurate, no further calculation is needed for applications involving double-axis tracking con- centrators with small acceptance angles. More generally, modeling the direct irradiance incident on a tilted surface is trivial if DNI is known, since only a geometric relation- ship is involved. Assessing the prediction performance of global irradiance or DNI with the various types of models currently available is beyond the scope of this contribution, although their accuracy indeed conditions that of the tilted irradiance. This issue is actually central to the discussion about the effect of using ‘‘suboptimal” inputs that is offered in Sections 5 and 6. For most other applications involving flat-plate collec- tors or buildings, another difficulty is to estimate the dif- fuse irradiance that emanates from the sky and foreground reflections. All models reviewed here ideally assume that this foreground is horizontal and extends infinitely in front of the receiver with no interfering mask or shading surfaces. Realistic installations usually involve more geometrical and solar radiation calculation com- plexity, but such an analysis is beyond the scope of this contribution. Up to now, most solar power projects were ‘‘small scale” and were not hurt much by solar resource miscalculations, thanks to error cancelations through the various calcula- tion steps or engineering tolerances. Due to the extremely rapid expansion of the solar power plant industry, things are different now, and long-term errors as low as ±5% may jeopardize the profitability of large-scale projects, which is of serious concern since they require considerable investments. Various radiation datasets or calculation methods exist but they often disagree substantially (Myers, 2007; Suri et al., 2008). This is highly confusing and detri- mental to the whole community. Furthermore, the current trend in the energy production field (particularly when using photovoltaic technologies) is to use realistic energy simulations of a solar power plant that are based on radi- ation data measured at high frequency, with time steps of one minute or less. Most transposition models have been developed, and so far tested, using hourly data. One of the objectives of the present study is to evaluate whether

|The|sum of direct|and diffuse|irradiance|is usually|referred to as|
|---|---|---|---|---|---|
|‘‘global irradiance”. The alternate term ‘‘total irradiance” is not used here||||||
|because of its ambiguity (it is also frequently considered as synonymous of||||||
|‘‘broadband irradiance”, as opposed to ‘‘spectral irradiance”). Another||||||
|alternative standardization institutions (see, e.g., ASTM, 2003), but it is rarely used in the literature.|is ‘‘hemispherical|irradiance”,||as recommended|by some|
 such models can be used reliably for 1-minute predictions. Many solar power plants now use flat photovoltaic panels. To maximize energy production, these flat-panels are fre- quently mounted on 2-axis trackers. Hence the emphasis added on the results obtained for such a configuration, which has been rarely studied in the literature.
A previous study (Gueymard and Myers, 2009) showed that the accuracy of the predicted global tilted irradiance was a function of the experimental error in the global hor- izontal irradiance and of other factors, including ground albedo and frequency distribution of the diffuse/global ratio. The goal of the present contribution is to generalize these results by considering more variables, and to obtain results that can be related to the everyday practice of solar energy engineering. In this study, the overall performance of the radiation transposition between the horizontal and tilted planes is assessed in various ways. The literature is rich in investigations of this kind (e.g. Hay and McKay, 1986; Kambezidis et al., 1994; Loutzenhiser et al., 2007; Psiloglou et al., 1996). These contributions, however, focus on the performance of models that evaluate the tilted dif- fuse irradiance under ideal conditions only, i.e., when both the direct and diffuse horizontal components are measured at first-class experimental sites, as well as other important ancillary data, such as ground albedo. These studies there- fore fail to address the additional uncertainties introduced by the models used to separate the direct and diffuse hori- zontal components of global irradiance, or (a fortiori) those used to evaluate the global irradiance from meteorological inputs (such as cloud cover, aerosol turbidity, and water vapor). In this respect, the present contribution offers some important improvements over the conventional validation and performance assessment methodologies that have been used in the literature up to now. These improvements include the use of:

One-minute radiation data for enhanced time resolu- tion, of importance for fast-responding (e.g., PV) energy systems. Measured (each minute) vs estimated (using a fixed value, e.g., 0.2) ground albedo, for snow-free vs snow- covered ground conditions. Accurate 1-minute cloud cover information.

These improvements provide the necessary elements to evaluate the uncertainty in the resulting global tilted irradi- ance¹ under various conditions, from ideal or ‘‘optimal” (when the input direct and diffuse irradiances, and the ground albedo, are known very accurately) to most usual or ‘‘suboptimal” (when only the global horizontal irradi- ance is available). It is emphasized that the main purpose of this study is not to compare the performance of various transposition algorithms at a single site (which would be

essentially of local interest), but to provide better under- standing of what drives the modeling errors in general, and what experimental difficulties are involved in model validation, all of which is of universal interest. Here, the main difference with the existing literature is that a broader perspective is adopted to evaluate the prediction accuracies of global tilted irradiance over a more complete chain of calculations, thus closing part of the gap between scientific abstraction and practical engineering situations.

2. Transposition and separation models The global irradiance, Es, on a tilted plane, whose tilt is s degrees from the horizontal, can be evaluated from the classic equation:
### Es¼ Ebncos h þ EdRdþ qERrð1Þ

where Ebnis DNI, Edis the diffuse horizontal irradiance, E is the global horizontal irradiance, h is the angle of inci- dence of the sun rays on the tilted plane, Rdis the diffuse transposition factor, q is the foreground’s albedo, and Rr is the transposition factor for ground reflection. The irradi- ance components that appear on the right-hand-side of Eq.

(1) are inter-related by the fundamental closure equation
### E¼Ebncos Z þ Edð2Þ

where Z is the sun’s zenith angle at any instant. The calculation of the tilted direct component, Ebncosh, is purely geometric, and therefore straightforward and identical in all cases considered in what follows. The evaluation of the ground-reflected diffuse irradiance is dependent on the factor Rr. Most studies consider that the ground reflection process is ideally isotropic, in which specific case Rrcan be simplified into

### Rr¼ð1 cos sÞ=2: ð3Þ

The foreground albedo can be estimated in different ways: a priori (as in the general case), experimentally mea- sured on-site (as in this study), or modeled (Gueymard, 1987; Loutzenhiser et al., 2007). The uncertainties associ- ated with both the use of approximate values of q and the isotropic approximation for Rrare discussed in Section

4.2. The main unknown in Eq. (1) is normally Rd. If the dif- fuse radiance were ideally constant over the whole sky hemisphere, Rdwould be easily obtained from the simple isotropic approximation
### Rd¼ð1 þ cos sÞ=2: ð4Þ

In reality, a plane of tilt s facing the sun receives more diffuse radiation than a plane of same tilt in the opposite direction. Elaborate transposition models have been devel- oped to estimate this anisotropic effect and calculate a refined value of Rd. The transposition models selected here are those that are commonly used in solar energy engineering practice, for applications such as PV design (Carr, 2005) or building

energy simulation (Loutzenhiser et al., 2007). Besides the conventional isotropic approximation of Eq. (4), various anisotropic diffuse models have been proposed in the liter- ature since the pioneering work of Threlkeld (1962). Threl- keld’s model was derived (in graphical form only) from clear-sky radiation data measured on vertical planes exclu- sively. It is not considered here because of these limitations. However, a numerical fit to Threlkeld’s data was provided by Stephenson (1965). This was later adopted by the Amer- ican Society of Heating, Refrigerating and Air-Condition- ing Engineers (ASHRAE), which generalized the model by simply specifying the isotropic formula for all tilts differ- ent from vertical (ASHRAE, 2005). This composite ASH- RAE model is important in practice since it is used routinely by building engineers for solar heat gain and cooling load calculations. In ascending chronological order, the other models considered here have been pro- posed by Temps and Coulson (1977), Klucher (1979), Hay (1979), Skartveit and Olseth (1986), Gueymard (1987), Perez et al. (1990), Reindl et al. (1990), and Muneer (2004). Note that the Reindl model is also referred to as ‘‘HDKR” (Duffie and Beckman, 1991). These models are well described in their original publication, and in the abundant literature on this topic as well, so that no further details are provided for conciseness. To use Eq. (1), the radiative input must be in the form of separate measurements of the three components Ebn,Ed and E, or of only two of them through the additional use of Eq. (2). At many experimental sites, only one irradiance component (usually E) is measured. In the majority of cases in practice the solar resource must be predicted at a non-instrumented site, so that E needs to be interpolated from other sites, or evaluated first through appropriate modeling and meteorological data. The accuracy of this predetermination of E conditions the accuracy of E. Sinces there is a large number of ways to estimate E at any site, the propagation of errors from E to Escan be extremely difficult to evaluate. Such a specific error analysis has been left out of the scope of this study. Therefore, it is assumed here that at least E is known from on-site measurement. If only E is known, Ebnand Edmust be estimated. To separate the direct and diffuse components from E, many empirical relationships have been proposed in the litera- ture. Most such correlations are univariate (e.g., Erbs et al. 1982; Orgill and Hollands, 1977), i.e., they use global irradiance as the only independent variable. Among the various versions of the Reindl model, the most detailed approach is multivariate: the direct/diffuse separation is made dependent on Z, ambient temperature, and relative humidity. Between these univariate and multi- variate approaches, a bivariate model (Maxwell, 1987) sep- arates DNI and diffuse radiation using a suite of functions of global irradiance and Z. The Erbs, Orgill, Reindl and Maxwell correlations are widely used and considered as rel- atively ‘‘universal”. They are representative of the many empirical functions that have been proposed in the abun- dant literature on this topic, albeit with three perceptibly

different levels of sophistication. They will be used concur- rently in what follows to derive Ebnand Edfrom E.

3. Experimental data The datasets used here are from NREL’s Solar Radia- tion Research Laboratory in Golden, Colorado (latitude
39.74 N, longitude 105.18 W, elevation 1829 m). This site is located on a mesa that overlooks the western side of the agglomeration of Denver. This is a sunny site, with an annual daily-average DNI of about 5.65 kWh/m². Such a resource can be classified as ‘‘relatively favorable” for solar applications. [This average DNI is close to the critical threshold of 6.0 kWh/m², above which the resource is gen- erally considered favorable to the construction of solar power plants (Gueymard et al., 2002).] The datasets have been obtained from SRRL’s down- load tool, [http://www.nrel.gov/midc/srrl_bms](http://www.nrel.gov/midc/srrl_bms). The 1-min irradiance data used here are from the following thermo- pile instruments: a Kipp & Zonen (KZ) CH1 pyrheliometer to measure DNI, a KZ CM22 to measure diffuse horizontal irradiance (both ventilated and with a tracking shade). The combination of the CH1 and CM22 instruments provides the ‘‘optimal” measurement dataset for direct and diffuse radiation. The optimal global irradiance is obtained by summation of these components per Eq. (2), following the current best practice (see, e.g., Gueymard and Myers, 2008b, 2009). This, and all the other steps taken to improve the measurement quality, should guarantee expanded uncertainties in the reference Ebn, Edand E better than
2.0%, 5.0% and 5.4%, respectively. An Eppley PSP with shadowband, combined with the CH1, defines a suboptimal way to obtain global irradiance. An unshaded PSP measures global horizontal radiation and provides another source of suboptimal data. A KZ CM21 measures Eson a 2-axis tracking plane always nor- mal to the sun’s direction, and five tilted PSPs measure Es
(i) on a south-facing tilt of 40 [nearly equal to latitude], and (ii) on vertical planes that face the four cardinal direc- tions. The uncertainty in the tilted data is ≈3% for 2-axis global and ≈5% for the fixed tilts. Ancillary data, also measured at 1-min intervals, include: temperature, relative humidity, total cloud cover, opaque cloud cover, ground albedo, and net thermal infra- red irradiance at the radiometers. The latter data is used to optimize the diffuse irradiance measurements per the cor- rection method recently proposed (Gueymard and Myers, 2009; Michalsky et al., 2007). The cloud cover information is obtained from a Yankee TSI instrument with a spatial resolution of 1% sky cover. The ground albedo is obtained as the ratio of the upwelling and downwelling global irra- diance measured by two PSPs at a height of 1.6 m. The ver- tical, 40 and 2-axis tracking instruments are all installed on a tower, with platforms at 2.4, 3.4, and 4 m above ground, respectively. This tower is about 52 m away from the setup measuring the horizontal irradiance and DNI components.
The experimental datasets cover the 12-month period September 2006 to August 2007. Their quality has been thoroughly controlled, adding to the normal QC tests rou- tinely performed by NREL. For instance, all data points with missing data from any sensor, with negative short- wave irradiance, with significant differences in redundant measurements, or with albedo values beyond some accept- able limits (0.05–1.0), have been rejected. A particularly insidious problem arises whenever the tilted radiometers sense direct radiation during a longer portion of the 1- min period than the horizontal ones, or vice versa. Error bounds have been used to eliminate these undesirable data points. It is stressed that the simultaneity of data collected by different instruments that are not exactly collocated is the more an issue that the measurement frequency increases. In contrast, conventional hourly data would not be affected as much, if at all. A total of 116,942 data points met all these criteria, and served as the main data- base for further analysis. In addition to this ‘‘Reference” case, five alternate sub- optimal input datasets have been devised:

(1) global horizontal calculated from Eq. (2) as before, but where diffuse irradiance is measured with a PSP/shadowband combination (case noted ‘‘Shadowband”);
(2) global horizontal measured with a PSP, and used with the Erbs et al. separation method (case noted ‘‘Erbs”);
(3) global horizontal measured with a PSP, and used with the Orgill & Hollands separation method (case noted ‘‘Orgill”);
(4) global horizontal measured with a PSP, and used with the Maxwell separation method (case noted ‘‘Maxwell”);
(5) global horizontal measured with a PSP, and used with the Reindl et al. separation method (case noted ‘‘Reindl”). These five alternate cases try to reproduce what would
be typical in the practice of solar engineering calculations,

i.e., use of suboptimal data. To better evaluate how the results obtained here can be representative of other climatic conditions, the accuracy of the prediction of Eshas also been analyzed as a function of season (summer vs winter, conducive to high vs low sun), sky clarity (clear-sky vs all-sky conditions), snow-free ground (low albedo) vs snow on ground (high albedo), and ground albedo estimated at a constant value of 0.2.
4. Transposition models performance In this section, the intrinsic performance of the ten trans- position models is evaluated by considering only the refer- ence case where optimal input data are used. Each 1-min prediction of Esvia Eq. (1) is compared to its measured counterpart. This defines the individual difference between

prediction and measurement, or apparent error of the pre- diction. It must be stressed that this is only an apparent error since each measured data point also carries some sys- tematic and random error in it. To conform to common usage, the term ‘‘error” will be used in what follows, even though the term ‘‘difference” would have been more appropriate. The dataset is analyzed first as a whole, then for various subsets. The usual summary statistics (mean bias error, MBE, and root mean square error, RMSE) are obtained for each of the ten transposition models and various tilted planes. More performance indices do exist, and are detailed elsewhere (Gueymard and Myers, 2008a). However, the latter reference showed that these indices behave differ- ently, so that, with present knowledge, any ‘‘objective” model ranking attempt is in fact index-dependent. The assessment described below is therefore not aimed at rank- ing the ten models, but, more modestly, at evaluating how their prediction uncertainty compares to that of the mea- surement, and is affected by atmospheric or environmental conditions. Considering that a bias in the tilted pyranome- ters’ calibration of about ±1% may exist, more weight is given to the random errors in the following discussion.

4.1. Overall statistical results The summary statistics for all models and three tilt geometries (40 S, 90 S, and fully 2-axis tracking) appear in Table 1. These results are separated into two important
Table 1
 Plane
groups, depending on cloud cover: (i) all-sky conditions (any cloud cover); and (ii) clear-sky conditions only (defined here as cloud amount 610% and DNI P120 W/ m²). The latter case constitutes as much as 50% of all cases, owing to the predominantly clear atmosphere at SRRL. The results in Table 1 clearly indicate that the isotropic approximation underestimates systematically and is the poorest performer in all cases, which could be expected, considering the overwhelming evidence provided by the lit- erature. The ASHRAE model is therefore affected by the same problem, except for the vertical tilt (since it uses an anisotropic algorithm in that specific case). The clear-sky conditions (bottom of Table 1) are obvi- ously associated with higher irradiances than those for all-sky conditions, but only 19–22% more on average because of the predominantly clear atmosphere. The RMS errors are lowest under clear-sky conditions, for all models and tilts. This could be expected because (i) the sky diffuse irradiance is low under clear skies, particularly at this clean, high-elevation site, compared to the high direct irradiance (considered ‘‘errorless” in the present con- text); (ii) clear-sky irradiances only change slowly and smoothly over one-minute intervals; and (iii) the sky radi- ance is spatially much more homogeneous than under partly-cloudy conditions, for instance. The latter two rea- sons suggest that these 1-minute RMS errors should be rep- resentative of the corresponding hourly RMS values, therefore easing the process of comparing the present results to others of the literature. The MBEs are below

|Plane|40 S9||0 S||Tracking||
|---|---|---|---|---|---|---|
|Model All-sky, N = 116,927|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|
|Mean E|643.2||432.3||835.9||
|ASHRAE|5.1|7.8|6.5|13.4|8.1|9.6|
|Gueymard|0.8|4.3|5.2|10.6|0.9|4.2|
|Hay|2.1|5.5|2.7|8.2|1.9|6.1|
|Isotropic|5.1|7.8|5.8|11.6|8.1|9.6|
|Klucher|1.4|4.6|0.3|8.5|6.0|7.5|
|Muneer|0.4|5.2|2.5|9.4|5.4|7.0|
|Perez|2.7|6.7|4.7|12.0|2.3|5.8|
|Reindl|1.8|5.3|0.4|7.7|1.5|5.9|
|Skartveit|2.4|5.7|4.3|9.3|2.2|6.4|
|Temps Clear sky, N = 58,871|1.3|6.0|4.8|11.3|4.5|6.6|
|Mean E|763.0||523.5||1019.6||
|ASHRAE|3.6|4.9|0.1|4.5|5.5|6.2|
|Gueymard|1.1|2.7|0.2|3.8|1.2|2.1|
|Hay|1.0|3.2|2.2|5.2|0.3|2.7|
|Isotropic|3.6|4.9|4.9|8.1|5.5|6.2|
|Klucher|1.0|2.8|0.5|5.1|4.1|4.8|
|Muneer|0.4|2.8|2.0|5.1|3.3|4.0|
|Perez|-0.7|2.6|0.4|3.9|1.0|2.1|
|Reindl|0.9|3.1|1.2|4.7|0.1|2.7|
|Skartveit|1.0|3.2|2.2|5.2|0.3|2.7|
|Temps|0.9|2.7|0.3|5.0|4.0|4.7|

s (W/m²)

s (W/m²)

0 S Tracking

Performance of ten transposition models (in alphabetical order) when using reference input data and the whole 12-month dataset. Percent results refer to the mean plane-of-array irradiance Esfor each plane. Top pane: results for all-sky conditions; bottom pane: results for clear-sky conditions only. 40 S9

±5% in all cases (except with the isotropic assumption), and would be conserved if hourly periods were rather con- sidered. The relatively low bias and random errors obtained with all anisotropic models suggest that their clear-sky predictions are of comparable accuracy to that of the actual measurements. Under such ideal conditions, the Gueymard and Perez models exhibit quite consistently lower bias and random differences, and therefore appear to perform better (particularly in the tracking plane case). When considering both clear and cloudy conditions (top of Table 1), all models suffer of a noticeable performance drop, indicated by larger MBE and RMSE. The RMS results show that only two models (Gueymard and Klu- cher) are below the 5% level for the 40 S plane, and only one (Gueymard) for the tracking plane. RMS errors are far larger—and substantially beyond the experimental uncertainty—for the south-facing vertical plane. The Reindl model performs best in the latter case. Since cloudy sky conditions are rapidly changing, it is likely that hourly RMS values would not be as high as the reported 1-minute values. Conversely, random errors would likely be much larger at cloudier sites. Interestingly, some models appear to be affected more than others by the presence of clouds. This translates into variable model-to-model changes in MBE and RMSE between the clear-sky and all-sky cases. This might explain, at least in part, why the relative perfor- mance of anisotropic models is location-specific, as the lit- erature reveals. Some models simply happen to be better tuned to very clear conditions, others to mid-range cloud- iness, and others to heavy cloudiness. This is also apparent in previous results (Gueymard and Myers, 2009), where the performance structure of various transposition models was found to be dependent on the frequency distribution of the Ed/E ratio, which is a strong function of cloudiness. The significantly lower performance of all transposition models for the vertical plane can be related to a drastic change in the relative importance of the different compo- nents in Es, per Eq. (1). From Eq. (2), Rris 0.5 for a ver- tical tilt, but only 0.117 for s =40. This means that the prediction of Esfor a vertical plane becomes very sensitive to any inaccuracies in the evaluation of the effective fore- ground reflectance, including its anisotropic features. Moreover, the mean vertical Esis also less rich in direct radiation (which is considered ‘‘errorless” here)—about 33% less overall than what is incident on the 40 tilt, on average. Another important aspect of these results is how they may apply to the design of solar systems. In Golden or sim- ilar sunny sites, 2-axis tracking flat-panel solar systems receive on average ≈30% more radiation than a flat-plate collector tilted at latitude. Under clear skies, this difference increases to ≈34%, and the mean annual global normal irradiance reaches, and even exceeds, the ‘‘one sun” level commonly referred to by energy ratings, i.e., 1000 W/m². Under such highly favorable conditions, the Gueymard and Perez models perform consistently better than the oth- ers, under either clear-sky or all-sky conditions.

The anisotropic reflectance issues mentioned earlier (and discussed further in the next section) appear even more obvious when considering the irradiance on vertical tilts of other cardinal directions, also measured at NREL. Although cardinal directions other than South (for the northern hemisphere) are of minor interest in solar energy applications (and are therefore not discussed in detail here), they are still important for the calculation of solar heat gains through windows, for instance. The all-sky per- formance of all models appears to degrade considerably when the vertical surface’s azimuth changes from S to E, W and N. The concomitant spread in mean annual RMS values changes from 7.7–13.4% (Table 1) to 10.5–20.0%,

13.3–26.9%, and 14.0–54.0%, respectively. It is highly likely that a significant part of these increasingly large apparent errors is in fact due to the presence of experimental arti- facts (from shading, parasitic reflections and inhomoge- neous conditions) coupled with oversimplified modeling of ground reflection, and with completely ignored obstruc- tion shading in current transposition models. The large error increase in the case of vertical surfaces is consistent with previous results from the literature. Since no known experimental setup can exactly replicate the ideal condi- tions assumed by transposition models, it is argued that selecting or ranking models according to their apparent performance relative to vertical surfaces should not be attempted unless the sky diffuse and ground-reflected dif- fuse irradiances can be precisely separated, which is not the case here.
4.2. Season and albedo effects The 12-month dataset has been split into two ideal sea- sons, covering the periods April–August (dubbed ‘‘Sum- mer”), and September–March (dubbed ‘‘Winter”). The ‘‘Winter” period was further split into ‘‘no snow” and ‘‘snow on ground” subsets, using a threshold albedo value of 0.5. No occurrence of snow-covered ground was found in ‘‘Summer”. Finally, a fourth dataset was created with all data points of any season by using a fixed albedo of
0.2 rather than the measured albedo. This is the usual sim- plification whenever the local albedo is not measured, i.e., in the vast majority of cases in an engineering practice. The interpretation of the summary statistics in Table 2 is difficult because the effects of season (and therefore solar geometry) and ground albedo are not the same for all mod- els or tilts. Interestingly, however, all predictions for the vertical tilt appear more accurate in winter with snow-cov- ered ground, i.e., when both the ground-reflected irradi- ance and Esare at their maximum. The ground albedo varies during the day for various reasons, including departure from Lambert’s Law of isot- ropy, and changes in ground properties (such as soil’s water content or snow cover). The diurnal variation of the measured albedo is shown in Fig. for two clear summer days and one clear winter day. The latter case shows a rapid decrease in albedo caused by melting

Table 2

Performance of ten transposition models (in alphabetical order) when using subsets of reference data, showing season and albedo effects. Plane 40 S9 0 S Tracking

|Plane|40 S9||0 S||Tracking||
|---|---|---|---|---|---|---|
|Model Summer, no snow, N = 61,669|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|
|Mean E|614.8||285.7||857.7||
|ASHRAE|3.2|6.1|11.2|18.9|7.3|8.7|
|Gueymard|1.0|4.1|8.4|16.1|2.0|3.9|
|Hay|2.7|4.9|4.7|9.2|2.7|5.0|
|Isotropic|3.2|6.1|0.1|7.2|7.3|8.7|
|Klucher|0.8|4.7|7.7|11.6|5.4|6.8|
|Muneer|0.6|4.0|3.9|10.8|5.0|6.4|
|Perez|3.5|7.4|8.7|19.4|3.0|5.6|
|Reindl|2.4|4.6|1.0|8.8|2.4|4.8|
|Skartveit|3.0|5.0|7.0|9.8|2.9|5.2|
|Temps Winter, no snow, N = 36,454|0.6|5.3|12.2|17.8|4.3|6.1|
|Mean E|645.9||487.4||748.5||
|ASHRAE|8.4|10.2|6.8|12.7|10.6|12.3|
|Gueymard|1.7|4.4|4.7|8.8|0.6|4.6|
|Hay|3.5|6.2|3.5|8.4|3.1|7.8|
|Isotropic|8.4|10.2|10.1|13.5|10.6|12.3|
|Klucher|3.0|5.0|3.8|7.9|7.8|9.6|
|Muneer|2.0|5.8|1.0|9.5|7.2|9.2|
|Perez|3.5|6.5|4.1|9.9|2.7|6.8|
|Reindl|3.2|5.9|1.3|7.5|2.4|7.4|
|Skartveit|3.8|6.5|5.2|10.2|3.5|8.3|
|Temps Winter, with snow, N = 18,808|1.8|6.3|2.3|8.7|5.4|7.9|
|Mean E|731.6||806.1||934.1||
|ASHRAE|5.0|6.9|0.7|7.6|6.7|8.0|
|Gueymard|1.6|4.4|1.9|6.3|1.6|4.2|
|Hay|1.9|5.5|0.5|5.9|2.2|6.2|
|Isotropic|5.0|6.9|7.6|9.5|6.7|8.0|
|Klucher|0.6|3.7|3.6|5.6|5.2|6.4|
|Muneer|2.9|6.2|2.5|6.9|3.9|5.4|
|Perez|0.7|4.8|0.9|5.9|0.4|4.7|
|Reindl|2.0|5.5|1.1|5.9|2.5|6.3|
|Skartveit|1.7|5.6|0.2|6.4|1.8|6.4|
|Temps Albedo = 0.2, N = 116,927|2.5|7.0|0.8|6.8|4.1|6.0|
|Mean E|643.2||432.3||835.9||
|ASHRAE|5.6|8.3|3.8|18.3|9.2|11.0|
|Gueymard|1.2|4.3|2.4|15.6|2.0|4.9|
|Hay|2.5|5.3|5.5|13.3|3.0|6.2|
|Isotropic|5.6|8.3|8.5|19.5|9.2|11.0|
|Klucher|1.9|4.9|2.4|16.3|7.1|9.0|
|Muneer|0.8|4.9|0.2|13.6|6.5|8.3|
|Perez|3.2|6.7|7.4|16.8|3.4|6.6|
|Reindl|2.2|5.1|3.2|12.9|2.6|6.0|
|Skartveit|2.8|5.5|7.1|14.1|3.3|6.6|
|Temps|0.9|6.0|2.1|17.3|5.6|8.1|

s(W/m²)

s(W/m²)

s(W/m²)

s(W/m²)

snow. Even the albedo of dry ground varies during the 0.375±0.277. Similarly, for summer, the minimum and day in summer, with a minimum around noon. The maximum are 0.05 and 0.552, with a mean of morning and afternoon albedos are not symmetrical, 0.184±0.033. The annual average albedo is 0.274, i.e., due to azimuthal inhomogeneities in ground cover and somewhat larger than the conventional value of 0.2. As possible partial shading. Moreover, the early morning could be expected, errors increase noticeably when and late evening albedos are often close to either or assuming a fixed albedo of 0.2 rather than using its mea- 1, mostly due to artifacts, such as shading or instrumen-sured value (compare the bottom part of Table 2 to the tal cosine error. Over the whole dataset, the winter top part of Table 1). As could be expected also, this albedo varies between 0.05 and 1.0 (because of the qual-error increase is far more important for a vertical surface ity-control constraints mentioned earlier), with a mean of than for more moderate tilts.

0.95 **Ground Albedo**
**Clear Days at SRRL, Golden, CO**

0.85
0.75
0.65
0.55
25 Jan 2007 Albedo

0.45
0.35
21 Aug 2007

0.25
0.15
18 Jun 2007

0.05 5:00 6:00 7:00 8:00 9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00
Standard Time

Fig. 1. Diurnal variation of 1-minute ground albedo measured during two

summer clear days and a winter day (with snow on ground) at SRRL. The dashed line indicates the conventional constant value of 0.2.

The uncertainty in ground reflection modeling, and of the compensation of errors that results (for some models more than others), is another factor that can explain (at least in part) why models perform differently depending on tilt geometry, or why they also perform differently from one specific site to the other, as the literature reveals. The present results confirm the concerns previously expressed about the importance of correctly measuring or estimating the ground-reflected irradiance (Gueymard, 1987; Ineichen et al., 1987, 1990; Loutzenhiser et al., 2007).

5. Suboptimal data uncertainty In most practical cases of an engineering practice, the inputs to the transposition models reviewed above are not optimal, either because of the experimental inadequa- cies summarized in a previous study (Gueymard and Myers, 2009), or because of the uncertainties introduced by the intermediate calculations needed to obtain E, Ebn and Edwhenever these irradiances are not measured locally (which is the most frequent case). In the Shadowband case (where global is obtained as the sum of shadowband diffuse and direct horizontal, as described in Section 3), only the diffuse measurement is suboptimal, resulting in an average RMS error of 7.5% in measured diffuse horizontal and 2.4% in derived global horizontal (Table 3). The reference DNI is used in this case, with therefore no error in what constitutes 68% of the aver- age global horizontal irradiance. The main input of the direct/diffuse separation methods is the global horizontal irradiance, obtained here from an unventilated and thermally uncorrected Eppley PSP pyra- nometer. This instrument has a large installed base over the world, so that this setup can be considered typical. The PSP-measured global irradiance yields an RMS error of ≈5%, indicating a less optimal setup than the Shadow- band just mentioned, particularly under clear skies. This might seem contrary to conventional knowledge, but there
are specific reasons for this, which have been discussed pre- viously (see, e.g., Gueymard and Myers, 2009). As the summary statistics in Table 3 also reveal, all the separation methods add significant random errors in the process, with typical RMS errors in DNI of ≈15% under all-sky conditions and 5–9% under clear-sky conditions. The performance of the Erbs method is similar in the all- sky and clear-sky cases. The Orgill method produces results very similar to those of the Erbs method. The Reindl method is less consistent, having the lowest RMS in the former case and the largest in the latter case. Conversely, the Maxwell correlation has the largest biases under all- sky conditions, but becomes the best performer to predict the direct and diffuse components under clear-sky condi- tions. All methods, except Maxwell’s, significantly underes- timate DNI and overestimate diffuse under clear-sky conditions, with an opposite trend under all-sky condi- tions. As discussed elsewhere (Gueymard, 2005), a possible reason for this is the low aerosol turbidity, which is prevail- ing at this site but not taken into consideration by any such separation method. These findings confirm previous results that have been obtained for other low-turbidity locations of the Southern Hemisphere (Spencer, 1982). The large RMS errors obtained here are consistent with the results from the many studies of the literature, which used hourly data most generally. Most troubling, however, is that the two more elaborate separation methods (Maxwell and, even more so, Reindl) do not perform better than the sim- pler ones (Erbs and Orgill). To the contrary, there are con- ditions (season or sky clarity) for which the latter ones yield lower bias or random errors than Maxwell or Reindl. This can be explained by the fact that, while all separation meth- ods are empirical in nature and may not apply as well to all possible climates, the multivariate methods may still ignore the physically most important variables (such as cloud properties and aerosol turbidity).

6. Suboptimal tilted irradiance prediction The effect on the predicted tilted radiation of combining suboptimal input data and suboptimal direct/diffuse sepa- ration is now analyzed. As can be expected, the more their input data deviate from optimal quality, the more predic- tion errors increase. This is shown in Fig. 2 for the 40 S tilt, for instance. In this case, the incident tilted irradiance is only marginally affected by any modeling error in fore- ground reflectance (since Rris small), and the largest step in error increase results from using an empirical direct/dif- fuse separation instead of measured data. The concomitant error increase is not uniform from one transposition model to the other. It is relatively larger for the Gueymard, Klu- cher, Muneer and Temps models than for the Hay, Perez, Reindl and Skartveit models when using the Erbs separa- tion method (which overestimates the direct/diffuse ratio), for instance. Similar results are obtained with the Orgill separation method. Conversely, different compensations of errors appear to occur when using either the Maxwell

Mean annual errors in horizontal irradiance due to using suboptimal measurement and estimation techniques.

Table 3

Component Global Model MBE (%) RMSE (%) All-sky, N = 116,927 Reference (W/m²) 543.5 Ref. DNI + Shadowband Diff. 0.1 2.4 Meas. Global + Orgill 0.4 4.5 Meas. Global + Erbs 0.4 4.5 Meas. Global + Maxwell 0.4 4.5 Meas. Global + Reindl 0.4 4.5 Clear sky, N = 58,871 Reference (W/m²) 620.5 Ref. DNI + Shadowband Diff. 0.3 1.7 Meas. Global + Orgill 0.9 4.7 Meas. Global + Erbs 0.9 4.7 Meas. Global + Maxwell 0.9 4.7 Meas. Global + Reindl 0.9 4.7

**40° South** Optimal inputs **Annual Results** Shadowband diffuse + DNI 15 Erbs, meas. albedo Reindl, albedo = 0.2

RMS Error (%) 5

0 Hay Perez Reindl Temps ASHRAE Gueymard Isotropic Transposition Model Klucher Muneer Skartveit

Fig. 2. Apparent RMS error for ten transposition models for 40 tilt

facing south at SRRL. Four input data quatites are compared: (i) Reference (optimal) measurements of direct and diffuse irradiance and of albedo; (ii) Reference direct irradiance measurement, suboptimal diffuse irradiance measurement with shadowband, and measured albedo; (iii) Measured global irradiance with direct/diffuse separation using the Erbs correlation, and measured albedo; and (iv) Measured global irradiance with direct/diffuse separation using the Reindl correlation, and fixed albedo value of 0.2.

separation method (which overestimates the direct/diffuse ratio even more) or the Reindl separation method (which is relatively neutral for all-sky conditions on a yearly basis). A better understanding of these error compensations is desirable so that some generalization can be eventually obtained and ‘‘universal” recommendations can be pro- posed. A thorough investigation comparing the frequency distributions between model errors and direct/diffuse or diffuse/global ratio at various sites is suggested to that effect, but is beyond the scope of this contribution. For conciseness, only a subset of annual results from all possible combinations is compiled in Table 4. Moreover, the results for the Orgill case are omitted because very sim- ilar to those for Erbs. For all cases, a comparison between Tables 1 and 4 clearly confirms the results shown in Fig. 2: the random error in the predicted Esincreases sharply when replacing optimal input data by suboptimal data.

Diffuse Direct MBE (%) RMSE (%) MBE (%) RMSE (%)

173.8 598.2
0.2 7.5 0.0 0.0
8.2 46.9 2.1 14.9
10.6 47.4 2.8 15.1
24.2 48.2 6.7 14.9
1.1 46.6 0.6 14.2
90.7 855.1
2.0 11.5 0.0 0.0
39.6 55.4 4.9 7.1
32.3 49.5 4.1 6.7
8.6 39.6 0.2 5.2
57.8 82.7 6.8 9.1
For all tilts, most separation and transposition model com- binations tend to underestimate Es. This is particularly evi- dent in the case of the vertical plane (90 S) when a fixed albedo of 0.2 is used. In that case, the RMS error also becomes large (Fig. 3). This could be expected since a ver- tical plane receives a relatively large fraction of ground- reflected radiation, and a fixed value of 0.2 grossly under- estimates the albedo in the presence of snow. From an engi- neering standpoint, such an underestimation may be a good thing (to some extent), since it is on the safe or con- servative side. The problem is that, a priori, it is difficult to know whether an underestimation or an overestimation will occur at any specific site and/or for any specific period. More generally, it is nearly impossible to make recom- mendations about the best model combination because of the number of variables involved, the various possibilities of error cancelation, and the relative importance of bias (MBE) vs random errors (RMSE) in the decision process. The main finding of this study, which needs to be empha- sized, is that in most cases, the intrinsic uncertainty of a transposition model becomes secondary when combined with suboptimal global radiation data, a direct/diffuse sep- aration model, and a rough estimate of the ground albedo.

Fig. 4 compares the performance results (expressed as

percent RMS errors) of the ten transposition models for different seasons/conditions, the 2-axis tracking plane, and the ideal case where all inputs are optimally measured. These results can be directly compared to those of Fig. 5, rather obtained for the pragmatic case where the Erbs cor- relation does the direct/diffuse separation in the input data. The degradation in performance between Figs. 4 and 5 is obvious and significant. Moreover, the model performance ranking that can be attempted from the results in Fig. 4 does not translate necessarily well to the results in Fig. 5. The only possible exception is the isotropic transposition model, which consistently appears as the worst performer. The selection of the most appropriate combination of models and albedo value ultimately conditions the perfor- mance of the whole chain of calculations. Therefore, it

Table 4

Performance of ten transposition models when using suboptimal data obtained from three empirical direct/diffuse separation techniques. <u>Plane 40</u> S9 <u>0 S Tracking</u>

|Plane|40 S9||0 S||Tracking||
|---|---|---|---|---|---|---|
|Model|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|MBE (%)|RMSE (%)|
|Mean E All-sky, Erbs correlation, N = 116,927|643.2||432.3||835.9||
|ASHRAE|4.8|11.9|4.3|20.1|8.5|16.4|
|Gueymard|0.8|9.3|3.2|17.5|1.6|12.1|
|Hay|2.0|8.7|3.6|14.9|2.3|11.3|
|Isotropic|4.8|11.9|6.5|20.3|8.5|16.4|
|Klucher|1.0|10.4|0.1|18.8|6.3|15.5|
|Muneer|0.1|10.4|1.6|18.3|5.8|15.3|
|Perez|1.2|10.1|2.2|17.8|1.7|13.3|
|Reindl|1.6|8.7|1.2|14.8|1.9|11.2|
|Skartveit|2.2|8.7|5.0|15.0|2.6|11.3|
|Temps All-sky, Maxwell correlation, N = 116,927|0.8|10.7|2.9|19.3|5.3|15.2|
|ASHRAE|3.7|10.2|4.3|19.1|4.4|12.4|
|Gueymard|0.4|8.8|3.2|16.9|0.8|10.7|
|Hay|1.3|8.2|2.5|14.1|0.2|9.9|
|Isotropic|3.7|10.2|5.0|17.6|4.4|12.4|
|Klucher|0.2|9.4|0.7|16.8|2.5|11.8|
|Muneer|0.5|9.5|2.3|17.1|2.1|11.7|
|Perez|0.5|9.8|1.2|17.7|1.3|11.9|
|Reindl|1.0|8.2|0.2|14.4|0.7|10.0|
|Skartveit|1.5|8.2|3.8|14.1|0.0|9.8|
|Temps All-sky, Reindl correlation, N = 116,927|1.1|10.0|2.9|17.9|1.8|11.8|
|ASHRAE|5.8|12.1|5.2|20.6|8.7|15.5|
|Gueymard|1.2|9.1|3.6|17.5|1.5|11.3|
|Hay|2.3|8.4|3.7|14.2|2.0|10.2|
|Isotropic|5.8|12.1|7.0|20.7|8.7|15.5|
|Klucher|1.3|10.0|0.5|18.9|6.2|14.2|
|Muneer|0.1|9.9|3.1|18.3|5.5|13.8|
|Perez|2.2|9.9|3.5|17.4|1.9|12.3|
|Reindl|1.9|8.3|1.0|14.2|1.5|10.2|
|Skartveit|2.5|8.4|5.0|14.3|2.2|10.2|
|Temps All-sky, Erbs correlation, Albedo = 0.2, N = 116,927|0.5|10.4|3.5|19.7|5.2|14.0|
|ASHRAE|5.2|12.5|1.8|24.9|9.5|17.6|
|Gueymard|1.2|9.7|0.7|22.2|2.6|12.9|
|Hay|2.4|9.0|6.0|19.6|3.3|11.9|
|Isotropic|5.2|12.5|8.9|26.5|9.5|17.6|
|Klucher|1.4|10.8|2.5|24.4|7.3|16.6|
|Muneer|0.5|10.6|0.9|22.2|6.8|16.3|
|Perez|1.6|10.4|4.6|22.3|2.7|14.0|
|Reindl|2.0|9.0|3.6|19.5|2.9|11.8|
|Skartveit|2.6|9.1|7.4|19.8|3.6|12.0|
|Temps|0.4|11.0|0.5|24.5|6.3|16.6|

s(W/m²)

seems that, from a practical engineering standpoint, the power plants. The bias errors reported here can be current literature does not provide all the answers needed. directly compared to previous results based on hourly This is because, in practice, models cannot be used in the data because bias is not sensitive to the aggregation time ideal way they have been developed. step. Hourly random errors would normally be lower than the 1-minute results obtained here. Under stable

7. Conclusion conditions, however, the difference between 1-minute
and hourly random errors should be small. Although To the difference of most previous studies on this the transposition models reviewed here were generally topic, which have focused on hourly data, 1-minute data developed from hourly data, they appear to be equally have been used here throughout. Usage of these higher-applicable to 1-minute data. This also means that the frequency data reflects the current needs from sophisti-main findings presented here should remain valid when cated simulations of energy production by large-size solar considering hourly time steps.

||MBE optimal|
|---|---|
||MBE Erbs, albedo = 0.2 RMS optimal RMS Erbs, albedo = 0.2|
|Muneer using|Perez Reindl Temps Skartveit optimal experimental|

40 **Vertical South** **Annual Results** 30

MBE and RMSE (%) 0

-10 Hay Isotropic Klucher ASHRAE Gueymard Transposition Model

Fig. 3. Apparent Mean Bias and RMS errors for ten transposition models

for south vertical tilt at SRRL. Inputs to the models are either reference measured direct and diffuse irradiances techniques, or measured global irradiance with fixed albedo value and direct/diffuse separation using the Erbs correlation.

15 Summer **Global normal (tracking)** Winter (no snow) **Input data:** Winter (snow) **Optimal meas. direct & diffuse** 10Clear sky

5 RMS Error (%)

0 Hay ASHRAE Gueymard Isotropic Klucher Muneer Skartveit Perez Reindl Temps Transposition Model

Fig. 4. Dependence of the RMS error for ten transposition models on

season and sky clarity for 2-axis tracking plane. Inputs to the models are reference measured direct and diffuse irradiances using optimal experi- mental techniques.

30 Summer**Global normal (tracking)** **Input data:** 25Winter (no snow)**Meas. global (PSP) + Reindl correl.** Winter (snow) 20 Clear sky

RMS Error (%) 10

0 Hay ASHRAE Isotropic Klucher Muneer Perez Reindl Skartveit Temps Gueymard Transposition Model

Fig. 5. Dependence of the RMS error for ten transposition models on

season and sky clarity for 2-axis tracking plane. Inputs to the models are measured global horizontal irradiance and estimated direct and diffuse irradiances estimated from the Reindl correlation.

It is found that the isotropic transposition method always performs poorly at the low-turbidity SRRL site, confirming previous results of the literature for other sites in widely different climatic areas. In sharp contrast, the per-

formance of all the anisotropic transposition models reviewed here is within, or close to, the instrumental uncer- tainty limits (≈3% for a 2-axis tracking plane and ≈5% for fixed-tilt planes) if optimal input data of measured irradi- ance (direct + diffuse) and ground albedo are used, and only clear skies are considered. Under such ideal condi- tions, the Gueymard and Perez models provide estimates of 1-minute global tilted irradiance with low bias and the lowest random differences, compared to global irradiance measured on a 40 S, 90 S and tracking plane. Under all- sky (clear and cloudy) conditions and still ideal input con- ditions, the performance of all models degrades somewhat, as could be expected. This performance degradation man- ifests as an increase in both bias and random errors. This is most particularly important for the vertical plane facing south (for which case the Reindl algorithm performs best), and even more pronounced for vertical planes facing the three other cardinal directions. The proposed explanation is that the existing obstacles and inhomogeneous ground conditions in the experimental setup interfere with the ide- ally perfect environment assumed by all transposition models. When using suboptimal inputs, i.e., when only global horizontal irradiance is measured locally and the direct and diffuse components need to be estimated, it is found that the performance of all transposition models degrades significantly. Their bias and random error summary statis- tics vary as a function of receiver geometry, atmospheric conditions, season, ground albedo, and accuracy of the direct/diffuse separation. The four direct/diffuse separation methods that are investigated here behave differently, with noticeable bias and random errors in most cases. The mul- tivariate separation methods (Maxwell and Reindl) do not perform better than the simpler univariate methods (Erbs and Orgill). The transposition models that perform best under these suboptimal conditions are not those that per- form best under the optimal conditions mentioned above, due to intricate model-to-model variance in accumulation or compensation of errors. For the site under scrutiny and the various suboptimal input datasets considered, the models performing best are generally those of Hay, Reindl and Skartveit. The results in this study also show, beyond any doubt, that the major part of the uncertainty in the predicted tilted irradiance at a sunny site is generally caused by the direct/ diffuse separation obtained by empirical models whenever these components are not measured locally. For vertical planes and other situations where the ground-reflected radiation is a significant part of the total tilted irradiance, the accuracy of the estimated ground-reflected irradiance becomes another key factor. Consequently, performance assessment results based on first-class experimental mea- surements and published in the abundant literature on this topic may not apply to the majority of engineering applica- tions in practice, since then the irradiance components and other environmental factors are normally not measured on- site and must be estimated beforehand.

The results presented here are limited to a sunny site where diffuse radiation is lower than average, particularly under clear skies, due to the high altitude and overall clar- ity of the atmosphere, but should be representative of many other sunny sites with high potential for solar energy appli- cations. Under such circumstances, the inherent inadequa- cies of the transposition models translate into only limited inaccuracies in the predicted tilted irradiance. What actu- ally limits their performance most is the quality of their inputs, such as the direct and diffuse irradiances or the ground albedo. It is highly likely that a far larger spread in the performance of these models would be found at cloudier sites, in which case the site-specific selection of the most appropriate transposition model might become a more critical issue than here. Finally, it is recommended that research be now ori- ented toward the improvement of the complete procedure to predict tilted irradiances in practice, considering the suite of necessary models as a whole, with particular emphasis on reducing the current uncertainties in estimat- ing global, direct and diffuse horizontal irradiances. Better characterization of the ground reflectance processes, including realistic shading of the horizon, is also recom- mended to improve the prediction of the incident irradi- ance on steep or vertical surfaces.

Acknowledgements

The NREL SRRL operations and maintenance staff is thanked for their enduring hard work dedicated to provid- ing the community with high-quality measurements. Daryl Myers kindly reviewed the manuscript and offered worth- while comments.

References

ASHRAE, 2005. Handbook of Fundamentals, SI Edition. American Society of Heating, Refrigerating and Air-Conditioning Engineers, Atlanta, GA. ASTM, 2003. Standard Tables for Reference Solar Spectral Irradiances: Direct Normal and Hemispherical on 37 Tilted Surface. Standard G173, American Society for Testing an Materials, West Conshohoc- ken, PA (Available from: <[http://www.astm.org/Standards/](http://www.astm.org/Standards/) G173.htm>). Carr, A.J., 2005. A detailed performance comparison of PV modules of different technologies and the implications for PV system design methods. Ph.D. Thesis, Murdoch Univ., Australia. Available from <[http://wwwlib.murdoch.edu.au/adt/browse/view/adt-](http://wwwlib.murdoch.edu.au/adt/browse/view/adt-) U20050830.94641>. Duffie, J.A., Beckman, W.A., 1991. Solar Engineering of Thermal Processes, third ed. Wiley, New York. Erbs, D.G. et al., 1982. Estimation of the diffuse radiation fraction for hourly, daily and monthly-average global radiation. Solar Energy 28, 293–302. Gueymard, C.A., 1987. An anisotropic solar irradiance model for tilted surfaces and its comparison with selected engineering algorithms. Solar Energy 38, 367–386, Erratum, Solar Energy 40, 175 (1988). Gueymard, C.A., 2005. Importance of atmospheric turbidity and associ- ated uncertainties in solar radiation and luminous efficacy modelling. Energy 30, 1603–1621.

Gueymard, C.A., Myers, D.R., 2008a. Validation and ranking method- ologies for solar radiation models. In: Badescu, V. (Ed.), Modeling Solar Radiation at the Earth’s Surface. Springer. Gueymard, C.A., Myers, D.R., 2008b. Solar Radiation Measurement: Progress in Radiometry for Improved Modeling. In: Badescu, V. (Ed.), Modeling Solar Radiation at the Earth’s Surface. Springer. Gueymard, C.A., Myers, D.R., 2009. Evaluation of conventional and high-performance routine solar radiation measurements for improved solar resource, climatological trends, and radiative modeling. Solar Energy 83, 171–185. Gueymard, C.A. et al., 2002. Proposed reference irradiance spectra for solar energy systems testing. Solar Energy 73, 443–467. Hay, J.E., 1979. Calculation of monthly mean solar radiation or horizontal and inclined surfaces. Solar Energy 23, 301–307. Hay, J.E., McKay, D.C., 1986. Calculation of solar irradiances for inclined surfaces: verification of models which use hourly and daily data. Report to International Energy Agency, SHCP Task IX, Atmospheric Environment Service, Canada. Ineichen, P. et al., 1987. The importance of correct albedo determination for adequately modeling energy received by tilted surfaces. Solar Energy 39, 301–305. Ineichen, P. et al., 1990. Ground-reflected radiation and albedo. Solar Energy 44, 207–214. Kambezidis, H.D. et al., 1994. Measurements and models for total solar irradiance on inclined surface in Athens, Greece. Solar Energy 53, 177–185. Klucher, T.M., 1979. Evaluation of models to predict insolation on tilted surfaces. Solar Energy 23, 111–114. Loutzenhiser, P.G. et al., 2007. Empirical validation of models to compute solar irradiance on inclined surfaces for building energy simulation. Solar Energy 81, 254–267. Maxwell, E.L., 1987. Quasi-physical model for converting hourly global horizontal to direct normal insolation. Proc. Solar ‘87 Conf., J. Hayes and D.A. Andrejko eds., Portland OR, American Solar Energy Society, pp. 35–46. Available from: <[http://www.nrel.gov/docs/leg-](http://www.nrel.gov/docs/leg-) osti/old/3087.pdf>. Michalsky, J.J. et al., 2007. A proposed working standard for the measurement of diffuse horizontal shortwave irradiance. J. Geophys. Res. 112D, 10.1029/2007JD008651. Muneer, T. (Ed.), 2004. Solar radiation and daylight models, second ed., Elsevier. Myers D.R., 2007. Relative performance of multiple solar radiation resource assessment data sources. Proc. Solar 2007 Conf., Cleveland, OH, American Solar Energy Society. NREL, 1995. National Solar Radiation Data Base User’s Manual. Report and data Available from: <[http://rredc.nrel.gov/solar/old_data/](http://rredc.nrel.gov/solar/old_data/) nsrdb/>. Orgill, J.F., Hollands, K.G.T., 1977. Correlation equation for hourly diffuse radiation on a horizontal surface. Solar Energy 19, 357–359. Perez, R. et al., 1990. Modeling daylight availability and irradiance components from direct and global irradiance. Solar Energy 44, 271–289. Psiloglou, B.E. et al., 1996. Evaluation of different radiation and albedo models for the prediction of solar radiation incident on tilted surfaces, for four European locations. Trans. ASME J. Solar Eng. 118, 183–189. Reindl, D.T. et al., 1990. Evaluation of hourly tilted surface radiation models. Solar Energy 45, 9–17. Renne´, D. et al., 2005. Results of solar resource assessments in the UNEP/ SWERA project. Proc. Solar World Congress, Orlando, FL, Interna- tional Solar Energy Society. Skartveit, A., Olseth, J.A., 1986. Modelling slope irradiance at high latitudes. Solar Energy 36, 333–344. Suri, M. et al., 2008. First steps in the cross-comparison of solar resource spatial products in Europe. Proc. Eurosun Conf., Lisbon, Portugal. Spencer, J.W., 1982. A comparison of methods for estimating hourly diffuse solar radiation from global solar radiation. Solar Energy 29, 19–32.

Stackhouse, P. et al., 2006. New renewable energy prototype data sets Temps, R.C., Coulson, K.L., 1977. Solar radiation incident upon slopes of from NASA satellites and research. Proc. Solar ‘06, Denver, CO, different orientations. Solar Energy 19, 179–184. American Solar Energy Society. Available from: <[http://eos-Threlkeld](http://eos-Threlkeld), J.L., 1962. Solar irradiation of surfaces on clear days. web.larc.nasa.gov/sse/>. ASHRAE J. 4, 43–54. Stephenson, D.G., 1965. Equations for solar heat gain through windows. Solar Energy 9, 81–86.
