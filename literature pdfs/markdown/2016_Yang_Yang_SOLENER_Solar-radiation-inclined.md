Solar Energy 136 (2016) 288–302

Contents lists available at ScienceDirect

## Solar Energy

journal homepage: www.elsevier.com/locate/solener

Review

### Solar radiation on inclined surfaces: Corrections and benchmarks

Dazhi Yang Singapore Institute of Manufacturing Technology (SIMTech), Agency for Science, Technology and Research (A⁄STAR), 71 Nanyang Drive, Singapore 638075, Singapore

article info abstract

Article history: Predicting solar radiation on inclined surfaces is a critical task for photovoltaic energy systems design, Received 8 February 2016 simulation and performance evaluation. Many transposition models have been proposed in the literature; Received in revised form 22 June 2016 and there are abundant evaluation studies. However, these models are sometimes used incorrectly. Accepted 24 June 2016 Moreover, these errors tend to propagate through the literature. This paper aims to identify and correct Available online 15 July 2016 some errors in the literature. It also provides a benchmark on transposition model accuracies. Twenty-six models are described using a consistent nomenclature. Model performance is ranked and pairwise accu- Keywords: racies are evaluated with one year of solar irradiance measurements from four locations. Although no Solar radiation universal model is found in this study, some are recommended. The paper comes with computer code Transposition models Diffuse irradiance modeling and a small portion of experimental data. Inclined surface 2016 Elsevier Ltd. All rights reserved.

Contents

1. Introduction ......................................................................................................... 289
1.1. A brief literature review of comparative and validation studies on transposition models................ ...................... 289
1.2. Objectives and paper organization...... ............................................................................ 290
2. Transposition models......... ......................................................................................... 291
2.1. LIU............................................................................................................ 291
2.2. BUGLER family of models............... ............................................................................ 291
2.3. TEMPS.......................................................................................................... 291
2.4. KLUCHER........................................................................................................ 291
2.5. STEVEN family of models............... ............................................................................ 291
2.6. HAY family of models................. ............................................................................ 292
2.7. WILLMOTT....................................................................................................... 292
2.8. KORONAKIS....................................................................................................... 292
2.9. PEREZ family of models................ ............................................................................ 292
2.10. SKARTVEIT...................................................................................................... 293
2.11. GUEYMARD...................................................................................................... 293
2.12. MUNEER family of models............. ............................................................................ 293
2.13. REINDL........................................................................................................ 293
2.14. OLMO family of models.............. ............................................................................ 293
2.15. TIAN.......................................................................................................... 294
2.16. BADESCU....................................................................................................... 294
3. Validation.. ......................................................................................................... 294
4. Concluding remarks.......... ......................................................................................... 296
Conflict of interest........... ......................................................................................... 297
Acknowledgments........... ......................................................................................... 298
Appendix A. Why are some earlier models considered by Hay and McKay (1988) not included in this study?.......... ................ 298
Appendix B. Notes on BUGLER model................ ...................................................................... 298
Appendix C. Notes on STEVEN model................ ...................................................................... 298

E-mail addresses: yangdazhi.nus@gmail.com, yangdz@simtech.a-star.edu.sg

[http://dx.doi.org/10.1016/j.solener.2016.06.062](http://dx.doi.org/10.1016/j.solener.2016.06.062) 0038-092X/ 2016 Elsevier Ltd. All rights reserved.

D. Yang / Solar Energy 136 (2016) 288–302
Nomenclature

a circumsolar half angle [rad] v c; vh; wc; whsome intermediate parameters in Perez model D sky’s brightness q foreground’s albedo h incidence angle [rad] e sky’s clearness, as Perez et al. (1990) e⁰ sky’s clearness, as Perez et al. (1987) a; c sky geometry parameters, in the simplified Perez model a⁰; b⁰; c⁰; d⁰ sky geometry parameters, in the original Perez model a₀; a₁; a₂ Muneer’s parameters for the background diffuse irra- diation A Ianisotropy index, AI¼ Ih=Ioh A 0I alternative definition for anisotropy index, A 0I ¼ I=Isc b parameter describing the radiance distribution of over- cast skies c ban approximation of Revfeim’s integration of the geom- etry associated with isotropic diffuse irradiance on a sloping surface Dcin-plane horizontal irradiance (DHI) [W/m²] Dgirradiance due to ground’s reflection (DHI) [W/m²] Dhdiffuse horizontal irradiance (DHI) [W/m²] f Klucher’s modulating factor, f ¼p1ffiffiffiffiffiffiffiffiffiffiffiffi ðDh=GhÞ² f⁰ Reindl’s modulating factor, f⁰ ¼ Ih=Gh 0c f modified Olmo’s multiplying factor for anisotropic reflections F₁; F₂ coefficients expressing the degree of circumsolar and horizon anisotropy, in the simplified Perez model

F⁰¹; F⁰² coefficients expressing the degree of circumsolar and horizon anisotropy, in the original Perez model f cOlmo’s multiplying factor for anisotropic reflections Gcin-plane global irradiance (global tilted irradiance, GTI) [W/m²] Ghglobal horizontal irradiance (GHI) [W/m²] h solar elevation [deg] I normal incident direct irradiance (direct normal irradi- ance, DNI) [W/m²] I cin-plane direct irradiance [W/m²] I hhorizontal direct irradiance (Ih¼ I cos z)[W/m 2] I oextraterrestrial normal incident irradiance (Isccor- rected for actual Sun–Earth distance) [W/m²] I ohextraterrestrial GHI [W/m²] I scsolar constant, 1362 W/m² k tclearness index, Gh=Ioh NptGueymard’s weighting factor between a clear and an overcast sky, or total cloud opacity r bfactor that accounts for direction of beam radiation, r b¼ cos h= cos z R ddiffuse transposition factor R rtransposition factor for ground reflection R d0diffuse transposition factor for clear condition R d1diffuse transposition factor for overcast condition S Steven’s anisotropy index s tilt angle of an inclined surface [rad] Z fraction of D that is due to collimated radiation from zenith h

z zenith of the Sun [rad]

1. Introduction Many types of solar radiation models have been developed to predict solar radiation when measurements are not available or are inappropriate. There was not any accepted typology, until Gueymard and Myers (2008) proposed to classify radiation models based on nine criteria. A transposition model (see criterion 8 in Gueymard and Myers, 2008) typically takes measured and/or mod- eled irradiance components on the horizontal surface as inputs. Together with several known geometrical parameters, such as solar zenith angle, surface inclination, and incidence angle, the model predicts irradiance components on an inclined surface. Transposition models are frequently used during photovoltaic (PV) energy systems design, simulation and performance evalua- tion. For example, transposition models are used to optimize the tilt and azimuth of flat-plane PV arrays (e.g., Khatib et al., 2015; Khoo et al., 2014; Lahjouji and Darhmaoui, 2013; Lave and Kleissl,
2011), so that their energy output can be maximized. Other emerg- ing applications, such as using PV systems as sensors for spatio- temporal irradiance forecasting (see discussions in Yang et al., 2015, 2014a; Lonij et al., 2013), also require transposition models, or more specifically, the inverse transposition models (Marion, 2015; Yang et al., 2014b; Yang et al., 2013; Faiman et al., 1987).
1.1. A brief literature review of comparative and validation studies on transposition models This work will not attempt reviewing the entire history of trans- position models, but a few studies are highlighted. The present work includes minimal theoretical explanations on various trans- position models; rather the focus is on the model formulations using a consistent nomenclature. In this section, a brief literature review of comparative and validation studies on transposition models is presented. The first transposition model appeared in the 1960s (Liu and Jordan, 1963, 1961; Kondratyev and Manolova, 1960). This model is isotropic, i.e., it assumes that the diffuse radiance is uniformly distributed over the sky hemisphere. However, the anisotropic nat- ure of sky radiance has long been demonstrated by Kondratyev and Manolova (1960) and others. Since then, a large number of increas- ingly sophisticated (physical and empirical) models have been pro- posed by treating the sky diffuse component as anisotropic (e.g., Yao et al., 2015; Muneer, 1990; Gueymard, 1987; Perez et al.,
1986). On the other hand, with the technological advancements in artificial intelligence, there is a trend in using tools such as arti- ficial neural networks to predict tilted irradiance (e.g., Ramli et al., 2015; Dahmani et al., 2014; Notton et al., 2012; Mehleri et al.,
Appendix D. Notes on GUEYMARD model. ................................................................................... 299
Appendix E. Other errors found in the references........... ................................................................ 299
Appendix F. Supplementary material.. ................................................................................... 299
References.... ...................................................................................................... 301

2010). Interested readers are referred to the recent review by Yadav and Chandel (2014). The scope of this paper is however lim- ited to physical and empirical models. Many attempts have been made to validate, compare, and review transposition models. Most early works compared the per- formance of slope irradiance models at daily and longer time inte- grals (e.g., Klein, 1977; Norris, 1966). Ma and Iqbal (1983) compared three models, with both their daily and hourly formula- tions, using measured data over a period of one year from Wood- bridge, Ontario. Two coincident review papers (Muneer and Saluja, 1985; Hay and McKay, 1985) jointly covered most of the available models at that time. In a report of IEA Task 9 by Hay and McKay (1988), 21 tilted irradiance models were compared. The study used 24 datasets, spanning the years from 1961 to 1984, from sites in diverse cli- matic regimes. It contained information about the different trans- position models then available. An effective validation methodology was introduced, in which sites with different exper- imental setups were used to prepare separate validation datasets. A popular transposition model, the PEREZ model, was recommended in the concluding remarks of that report, with GUEYMARD being the next best model. These two models, in terms of number of param- eters and granularity of modeling, are more elaborate than others; their complexity is justified by their superior performance as evi- dent in Hay and McKay (1988). Although the remaining models were shown to be suboptimal in most test cases, they occasionally outperformed on some specific datasets. For such reasons, several less sophisticated models are included in this paper. Empirical sup- port of the model choices is provided in Appendix A. Throughout the past decade, the validation and comparison of transposition models has intensified. From using a handful of sec- ond generation models, according to Muneer et al. (2004)’s classi- fication of transposition models, to 10–20 models from all three generations, many researchers have validated their models of choice with data collected at geographically dispersed locations, including Austria (Orehounig et al., 2014); Belgium (Demain et al., 2013); Brazil (Escobedo et al., 2014); Egypt (Khalil and Shaffie, 2013b); Hungary (Horváth and Csoknyai, 2015); India (Pandey and Katiyar, 2014); Israel (Evseev and Kudish, 2009b); Italy (Gracia and Huld, 2013); Northern Ireland (Mondol et al.,
2008); Poland (Chwieduk, 2009); Romania (Vasar et al., 2016); South Korea (Lee et al., 2013); Spain (Posadillo and López Luque,
2009) and Thailand (Wattan and Janjai, 2016). This list is far from being complete. Nevertheless, these references, together with some other references appeared in later parts of this paper, are plotted in Fig. 1 as a word cloud. The size of a word is proportional to the number of models considered in that reference. The growing body of recent literature on this topic, or more generally, in the areas of solar radiation and solar resource assess- ment, motivates the emergence of global, ‘‘all-inclusive” intercom- parisons to provide more definitive answers on model performance. On this point, several (associate) editors of Solar Energy (Gueymard et al., 2009) have thought it advisable to com- municate a short editorial regarding the journal’s performance and publication criteria, in which the intention of publishing only papers containing ‘‘universal” models and/or providing unique insights was announced. Comparing transposition models with datasets from a specific site is of local and limited interest. Further- more, in situations where only a few second generation models are compared, choosing the winning model for subsequent applica- tions, such as evaluating PV performance, introduces additional uncertainties, which could be reduced if a superior model is used. Uncertainty quantification is of practical importance and thus has been a topic in the literature. Loutzenhiser et al. (2007) com- pared 7 models using data from two 25 days periods measured in Duebendorf, Switzerland. The authors also conducted detailed
Wlodarczyk and Nowak,2009 Wattan and Janjai,2016 Muneer et al.,2004

# Souza and Escobedo,2013

Cucumo et al.,2007 Escobedo et al.,2014 Khatib et al.,2012 Lahjouji and Darhmaoui,2013 Yadav and Chandel,2013

Khatib et al.,2015 Araneo et al.,2014 Padovan and Del Col,2010 Yao et al.,2015 Orehounig et al.,2014 Vasar et al.,2016 Horvath and Csoknyai,2015 David et al.,2013 Benghanem,2011

Pandey and Katiyar,2014 Lave et al.,2015 Mehleri et al.,2010

Khalil and Shaffie,2013 Lee et al.,2013 Yoon et al.,2014Chwieduk,2009 Gulin et al.,2013 Kamali et al.,2006 Noorian et al.,2008 Mondol et al.,2008 Loutzenhiser et al.,2007 Diez−Mediavilla et al.,2005 Khalil and Shaffie,2013

#### Notton et al.,2006

Demian et al.,2013 Kambezidis et al.,1994 Posadillo and Lopez Luque,2009 Evseev and Kudish,2009 Evseev and Kudish,2009

#### Gracia and Huld,2013

Yang et al.,2013 Gueymard,2009

Fig. 1. Word cloud of studies that compare several transposition models. The size of

a word is proportional to the number of models considered in the study, ranging from 2 to 20 models.

sensitivity analyses using Monte Carlo and fitted effects for N-way factorial analyses to assess the effect of input uncertainties on the output. The sensitivity analyses were later recommended by Gueymard and Myers (2008) in their book chapter. Gueymard (2009) conducted a study on direct and indirect uncertainties involved in transposition modeling, using 1-min data from NREL, Golden, Colorado. One of the interesting features of the work is the evaluation of 10 models using data recorded by many types of co-located instruments with different measurement uncertain- ties. It was found that the models which perform well using subop- timal data are not necessarily those that perform well with optimal data, due to intricate model-to-model variance in accumulation or compensation of errors (Gueymard, 2009). The uncertainties asso- ciated with foreground’s albedo which enters ground reflected irradiance calculation have been investigated (e.g., Yoon et al., 2014; Demain et al., 2013; Katiyar and Panday, 2010; Gueymard,

2009).
1.2. Objectives and paper organization In this paper, the performance of 26 transposition models are compared. Various error metrics, linear ranking, and hypothesis testing are employed to quantify the model performance. Uncertainties are not considered in this paper, but further studies on transposition modeling uncertainties are encouraged. One contribution is that additional models compared to Hay and McKay (1988) are considered in this paper and a global bench- mark on modeling accuracy is provided. However, the comprehen- sive literature revealed suboptimal or even incorrect usage of several transposition models. Although a poorly implemented model usually results in high errors, these suspicious numbers still sometimes slip through proofreading and peer-review. Further- more, these errors tend to propagate through the literature. This paper therefore aims to identify some errors in the literature. The goal is not to defame the authors nor their works. Instead, it is simply to help readers to understand the origin and confusion stemming from these errors and avoid future works from repeating the mistakes. Similarly, the author welcomes comments or rebut- tals on the present paper and its interpretation of model errors. The computer programs of transposition models and quality controlled datasets were released by Hay and McKay (1988) on magnetic tape, including a user’s guide and reference manual. Unfortunately, in energy journals, releasing computer code

supplemental to publications is still not popular. As computer code can help avoid misinterpretations and promote the widespread uptake of the results by researchers globally, the R code used in this paper is provided as supplementary material (see Appendix F for details). While R is not the most popular programming lan- guage as of today (it was ranked 6th by IEEE Spectrum in 2015), it only takes a minimal effort to interface R with other popular pro- gramming languages such as Java, C, C++, Python and Matlab. The validation dataset is also provided to benchmark future implementations. The remaining part of the paper is organized as follows. A review on 26 transposition models is first performed in Section 2. The models are validated and ranked against irradiance data on tilted planes at 4 sites with 18 different tilt and azimuth angles in Section 3. Conclusions follow at the end.

2. Transposition models In general, a transposition model takes the form: Gc¼ Icþ Dcþ Dg; ð1Þ where the global tilted irradiance (GTI) received by a solar collector (Gc) is expressed as the sum of in-plane direct irradiance (Ic), in- plane diffuse irradiance (Dc) and irradiance due to ground reflection (Dg). Iccan be calculated via:
<u>cos h</u> I c¼ I cos h ¼ Ih; ð2Þ cos z

where I is direct normal irradiance (DNI), which is the direct irradi- ance received by a surface normal to the sun-ray; Ihis the direct irradiance on a horizontal surface; h is the incidence angle; and z is the solar zenith angle. While Icis deterministically calculated, Dcand Dgare modeled by defining transposition factors:

Dc¼ DhRd; ð3Þ Dg¼ qGhRr; ð4Þ

where q is the foreground’s albedo; Rdis diffuse transposition fac- tor; Dhis diffuse horizontal irradiance (DHI); Ghis global horizontal irradiance (GHI, Gh¼ Ihþ Dh); and Rris the transposition factor for ground reflection. Over the years, many authors have presented transposition models. While it is common to model Rrunder the isotropic assumption (Gueymard, 2009):

<u>1 cos s</u> R r¼; ð5Þ 2

where s is the tilt angle of the inclined surface, the formulations dif- fer by the modeling of Rd. The transposition models are arranged in chronological order. This paper follows the naming convention used by Gueymard and Ruiz-Arias (2016), namely, first author in SMALL CAPS, optionally followed by a number if more than one version of the model is available.

2.1. LIU LIU (Liu and Jordan, 1961): Ldiu1 þ cos s R ¼ : ð6Þ Although this classic isotropic model was reported by Kondratyev and Manolova (1960) at an earlier time, we follow its well- accepted name.
2.2. BUGLER family of models BUGLER1(Bugler, 1977): <u>1 þ cos s</u> I cos h R B dugler1¼ þ 0:05 : ð7Þ
2 Dh

Eq. (7) originates from the argument that the anisotropy in tilted diffuse irradiance should be accommodated through an additional component contributed by the circumsolar region (Bugler, 1977); Bugler assumes the addition component is 5% of DNI. However, Hay and McKay (1985) pointed out that the original formulation ignores the fact that a portion of the isotropic radiation is also con- tributed by the circumsolar region. Therefore, an adjusted formula- tion is given as: ~ B<u>Ih</u>1 þ cos s <u>I cos h</u> R dugler2¼ 1 0:05 þ 0:05; ð8Þ Dh2 Dh

which is referred to as BUGLER2 in this paper. For further information on BUGLER models, the readers are referred to Appendix B.

2.3. TEMPS TEMPS (Temps and Coulson, 1977):
hi R T demps¼ cos² <u>s</u> 1 þ sin³ <u>s</u> 1 þ cos² h sin³ z; ð9Þ 2 2

where the ½1 þ sin ðs=2Þ term accounts for the horizon brightening 3 3 effect and the ð1 þ cos² h sin zÞ term accounts for the brightening in the vicinity of the Sun (the circumsolar region).

2.4. KLUCHER KLUCHER (Klucher, 1979):
hi Klucher 2<u>s</u>3<u>s</u>2 3 R d¼ cos 1 þ f sin 1 þ f cos h sin z; ð10Þ 2 2

where f ¼ 1 ðDh=GhÞ² is a modulating function to modulate TEMPS as the sky varies from clear to overcast.

2.5. STEVEN family of models STEVEN1(Steven and Unsworth, 1979): R d Steven1 ¼ Srbþð1 SÞ
<u>s</u> 2b hi <u>s</u> cos² þ sin s s cos s p sin²; 2 pð3 þ 2bÞ 2 ð11Þ

where S ¼ 0:51 and b ¼0:87. Steven and Unsworth (1979) also fit- ted S and b for different zenith angle ranges:

S ¼ 0:65; b ¼1:04; for z ¼ 35; S ¼ 0:60; b ¼1:00; for z ¼ 45; S ¼ 0:53; b ¼0:90; for z ¼ 55; S ¼ 0:46; b ¼0:85; for z ¼ 65; ð12Þ

which leads to the model STEVEN2, which assigns S and b in Eq. (11) according to the closest z value. An important note on the above two STEVEN models is given in Appendix C. Steven and Unsworth (1980) reiterated their diffuse radiation model under overcast skies: Steven3 hi s s R d¼ 0:143 sin s s cos s p sin þ cos : ð13Þ

Eq. (13) is named STEVEN3. While the first two STEVEN models are derived for clear sky conditions, they can be used together with STEVEN3. In this paper, a model called STEVEN4 is included, which uses

band is assumed to be coming from an infinitesimally thin region, Eq. (18) can be written as:

<u>1 þ cos s</u> a⁰ Perez1 R ¼ð1 F Þ þ F þ F sin s; ð19Þ 1 2 d 1 2 c⁰

where

a⁰ ¼ 2ð1 cos aÞv ;c ð20Þ c⁰ ¼ 2ð1 cos aÞvh; ð21Þ 8 > w cos h; if h < p=2 a; < h vc¼ w wh csinðw aÞ;cif h 2½p=2 a; ð22Þ > : 0; otherwise; cos z; if z < p=2 a; ð23Þ vh¼ whsinðwhaÞ; otherwise; wc¼ðp=2 h þ aÞ=ð2aÞ; ð24Þ ðp=2 z þ aÞ=ð2aÞ; if z > p=2 a; ð25Þ wh¼ 1; otherwise; 0 0 0 F₁ ¼ maxð0; F₁₁ðe ÞþDF ð26Þ 12ðe ÞþzF 13ðe ÞÞ; ð27Þ F₂ ¼ F₂₁ðe⁰ÞþDF₂₂ðe⁰ÞþzF₂₃ðe⁰Þ; e⁰ ¼ðDhþ IÞ=Dh; ð28Þ <u>Dh</u> D¼I ð29Þ cos z; o and a is the circumsolar half angle, which is assumed to be 25 in Perez et al. (1987). This model is called PEREZ 1 in this paper; its coef- ficients are given as the first set of coefficients in Table 1. Perez et al. (1987, 1988) further assumed that all circumsolar energy originates from a point source. This simplification leads to PEREZ2: <u>1 þ cos s</u> a þ F₂ Perez2 R ¼ð1 F₁Þ þ F₁ sin s; ð30Þ d 2 c where

Perez model coefficients for irradiance as a function of the sky’s clearness. Note that

STEVEN2 for e > 1:1, STEVEN3 otherwise; parameter e is sky’s clearness (see PEREZ model below).

2.6. HAY family of models HAY1(Hay and Davies, 1980): H 2<u>s</u> R d ay1¼ð1 AIÞ cos þ AIrb; ð14Þ
2 where AI¼ Ih=Ioh¼ I=Iois the ‘‘anisotropy index” and r b¼ cos h= cos z. The expression for AIdescribes the degree of aniso- tropy: under a sky with complete cloud cover, H 2 A I ¼ 0; Rd ay1¼ cos ðs=2Þ is isotropic; under a scattering free atmo- H sphere, AI¼ 1; Rd ay1¼ rbis completely directional. It should be noted that in the latter case, Dc¼ rbDh¼ 0, since Dh¼ 0 for a scat- tering free atmosphere. Hay (1993) gave another formulation for anisotropy index, which leads to HAY2: H 0I 2<u>s</u>0I R d ay2¼ð1 A Þ cos þ A rb; ð15Þ 2 0I where A ¼ I=Isc.

2.7. WILLMOTT WILLMOTT (Willmott, 1982): R W d illmott¼ A 0I r
bþ cbð1 A 0I Þ; ð16Þ 0I where rbis given in HAY1, A is given in HAY2 and 2 c b¼ 1:0115 0:20293s 0:080823s; 0:5 6 cb6 1. cbis an approxi- mation of Revfeim (1978) integration of the geometry associated with isotropic diffuse irradiance on a sloping surface.

2.8. KORONAKIS KORONAKIS (Koronakis, 1986): K<u>2 þ cos s</u> R doronakis¼ : ð17Þ
3

2.9. PEREZ family of models PEREZ0(Perez et al., 1986):
0 0 0 P<u>0:5ð1 þ cos sÞþa⁰ðF₁ 1Þþb ðF₂ 1Þ</u> R derez0¼0 0 0 0: ð18Þ 1 þ c ðF₁ 1Þþd ðF₂ 1Þ

The PEREZ family of models (Perez et al., 1986, 1987, 1988, 1990) divides the sky hemisphere into three zones, namely, the circumso- lar disc, the horizon band and the isotropic background. In Eq. (18), a⁰ and b⁰ are solid angles occupied by the circumsolar region and horizon band, respectively, weighted by their average incidence on a slope; c⁰ and d⁰ are a⁰; b⁰ equivalents on a horizontal surface. 01 02 The coefficients F and F are non-dimensional multiplicative fac- tors that relate the radiance in the two anisotropic regions to that in the main portion of the sky dome. The transposition factor Rd Perez0 has nonlinear relationship with F⁰¹ and F⁰², which may lead to some difficulties during parameter fitting. In addition, PEREZ0 is more complex to use than other trans- position models; it had not been validated for diverse environ- ments (Perez et al., 1987). To that end, several modifications were made on PEREZ0. The right hand side of Eq. (18) was re- written as: 0:5ð1 þ cos sÞð1 F₁ F₂ÞþF₁ða =c ÞþF₂ðb =d Þ, where F₁ and F₂ are the modified multiplicative factors; they are related to F⁰¹ and F⁰² by some transformation (see Eqs. (6) and (7) in Perez et al., 1987). Furthermore, if the energy from the horizon

Table 1

and <u>e⁰</u> are calculated differently. <u>F₁₁ F₁₂ F₁₃ F₂₁</u> e⁰ (for PEREZ1) ½1; 1:056Þ 0.011 0.748 0.080 0.048 ½1:056; 1:253Þ 0.038 1.115 0.109 0.023 ½1:253; 1:586Þ 0.166 0.909 0.179 0.062 ½½1 2::586 134;; 23::134 23Þ Þ

0.419
0.710
0.646
0.025
0.262
0.290
0.140
0.243
½3:23; 5:98Þ 0.857 0.370 0.279 0.267 ½5:98; 10:08Þ 0.743 0.073 0.228 0.231 ½10:08; þ1Þ 0.421 0.661 0.097 0.119 e⁰ (for PEREZ2) ½1; 1:056Þ 0.041 0.621 0.105 0.040 ½1:056; 1:253Þ 0.054 0.966 0.166 0.016 ½1:253; 1:586Þ 0.227 0.866 0.250 0.069 ½1:586; 2:134Þ 0.486 0.670 0.373 0.148 ½2:134; 3:23Þ 0.819 0.106 0.465 0.268

½½5 3::98 23;; 10 5:98 :08 Þ Þ

1.009
1.020
0.708
0.260
0.433
0.514
0.287
0.306
½10:08; þ1Þ 0.936 1.121 0.352 0.226 e (for PEREZ3 and PEREZ4) ½1; 1:065Þ 0.008 0.588 0.062 0.060 ½1:065; 1:23Þ 0.130 0.683 0.151 0.019 ½1:23; 1:5Þ 0.330 0.487 0.221 0.055 ½1:5; 1:95Þ 0.568 0.187 0.295 0.109 ½1:95; 2:8Þ 0.873 0.392 0.362 0.226 ½2:8; 4:5Þ 1.133 1.237 0.412 0.288 ½4:5; 6:2Þ 1.060 1.600 0.359 0.264 ½6:2; þ1Þ 0.678 0.327 0.250 0.156

<u>F₂₂</u>

0.073
0.106
0.021
0.167
0.511
0.792
1.180
2.125
0.074
0.114
0.002
0.137
0.497
1.286
0.804
2.449
0.072
0.066
0.064
0.152
0.462
0.823
1.127
1.377
e

<u>F₂₃</u>

0.024
0.037
0.050
0.042
0.004
0.076
0.199
0.446
0.031
0.045
0.062
0.056
0.029
0.166
0.046
0.383
0.022
0.029
0.026
0.014
0.001
0.056
0.131
0.251

a ¼ maxð0; cos hÞ; ð31Þ2 2<u>s</u>

|R ¼ cos|s þ|2b hi sin s|s cos s|ð43Þ|
|---|---|---|---|---|
||2||||
|where partly cloudy sky conditions, it is proposed to use a linear function to represent b, namely, b ¼ 0:5 þ N ity, a weighting factor depending on cloud observations. If no cloud observation is available, N N ¼ max½minðY; 1Þ; 0; 8|b ¼ 1:5 is thought|appropriate can be approximated through:|(Gueymard,, where N|Under ð44Þ|
|> > < 6:6667 D||1:4167; if D|6 0:227;||
|Y ¼ > > : 1:2121 D|G|G 0:1758; otherwise:||ð45Þ|
||G||||
|For further information on G to Appendix D.|||model, the readers are referred||
|2.12. M|family of models||||
|M|1(Muneer, 1990): 8||||
||> > > > A r þð1 > > > > > hio > > > > > > sin s > > > > > > b ¼0:62; > > > > > > > > > cos > < hi|A Þ cos² s cos s for G s 2b 2 þ|s þ 2b 2 s 2; > D; h < 2; s||
|R|¼ > sin s > > > > > > > > > b ¼ 1:68; > > > > > > > > cos > > > > hi > > > > > sin s > > > > : b ¼ 5:73;|s cos s for G s þ 2b 2 s cos s for h P|; 2 ¼ D; h < 2; 2 s; 2;|ð46Þ|
|where A In Muneer (1990), the 2b= unshaded conditions is empirically modeled:|¼ I =I and r|¼ cos h= cos z.|||
|2b where a₀; this formulation M|¼ a₀ a A a₁ and a₂ are location-dependent parameters. We name|a A; 2. In the current work, the set of parameters||ð47Þ|
|that is a₀ ¼ 0:04; are other versions of M not be dramatically different from M 2.13. R R|fitted a₁ ¼ 0:82 and a₂ ¼ 2:026 (Muneer et al., 2004). There (Reindl et al., 1990):|for the globe models, but their accuracies should s hi|is considered, 1 and M s|namely,|
|R ¼ð1|A Þ cos|2 1 þ f|2 pffiffiffiffiffiffiffiffiffiffiffiffi þ A r;|ð48Þ|
|where A based on H|; r are given in H 1 by including a horizon brightening correction factor|1 and f⁰ ¼|I =G||
|similar to the one used in T||.|||
|2.14. O|family of models||||
|O|1(Olmo et al., 1999):||||
|G ¼ G|exp½k ðh|z Þf;||ð49Þ|

d1p sin; c ¼ maxðcos 85; cos zÞ: ð32Þpð3 þ 2bÞ 2

PEREZ2 is parameterized by the second set of coefficients in Table 1. 1987). The coefficients used in PEREZ1 and PEREZ2 are fitted using hourly measurements from Trappes and Carpentras, France. Althoughpt ptis total cloud opac- using locally-fitted coefficients can improve model performance for specific locations (e.g., Yang et al., 2014b; Gomez et al., 1992), pt these coefficients may not perform optimally for other locations. pt Therefore, Perez et al. (1990) fitted another set of coefficients using <u>h h</u> data from 10 American and 3 European sites. The model PEREZ3 fol- lows the formulation of PEREZ2, but uses the third set of coefficientsh h in Table 1. It should be noted that the partition of sky’s clearness<u>h</u> for PEREZ3 is different from that for PEREZ1 and PEREZ2. Instead ofh using Eq. (28),PEREZ3 uses:UEYMARD

<u>ðDhþ IÞ=Dhþ 1:041z³</u> e ¼ ð33Þ 1 þ 1:041z3 UNEER to eliminate dependence between e⁰ and z.PEREZ3 is most widely accepted version of PEREZ model. UNEER Utrillas and Martinez-Lozano (1994) performed a comprehen- sive review on various versions of PEREZ model. Using a datasetI b I pð3 þ 2bÞ from València, two important conclusions were drawn: (1) the 2 simplified circumsolar model (PEREZ1) performed noticeably better p sin than the original model (PEREZ0), and (2) the models were sensitive <u>p</u> to the set of coefficients used. In consideration of these, the results h h of PEREZ0 are not presented in this work. Instead, another model, 2 PEREZ4, is considered, which has the formulation of PEREZ1 but uses pð3 þ 2bÞ the e binning and coefficients of PEREZ3. Although the third set of Muneer1 2 coefficients in Table 1 could be considered as most ‘‘universal” d p sin owing to the many datasets it uses, a set of coefficients which <u>p</u> could provide an asymptotic level of optimization is desired in h h the future. 2 pð3 þ 2bÞ

2.10. SKARTVEIT
p sin² SKARTVEIT (Skartveit and Olseth, 1986):<u>p</u> S 2<u>s</u> Rdkartveit¼ð1 AIZÞ cos þ AIrbþ Z cos s; ð34Þ 2 I h oh b where AI; rbare given in HAY1 and Z ¼ maxð0; 0:3 2AIÞ. p=ð3 þ 2bÞ term for non-overcast and

2.11. GUEYMARD
2 1 I 2 I pð3 þ 2bÞ GUEYMARD (Gueymard, 1987): G Rd ueymard¼ð1 NptÞRd0þ NptRd1; ð35ÞUNEER

where > Rd0¼ exp ðXHÞ h þFðsÞGðhÞ; ð36Þ UNEER > UNEER UNEER2. h ¼ 1 cos h cos² h cos³ h; ð37Þ 0 02 03 04 > H ¼ 1 h h h h; ð38ÞEINDL 0 1 0:90 3:36 3:96 1:91 0:00 B C EINDL 4:45 12:96 34:60 48:78 27:51 C X¼BB C; ð39Þ @ 2:77 9:16 18:88 23:78 13:01 AReindl 2 0 3 d IsinI b 0:31 0:22 0:81 0:32 0:00 2 I b AY h h.REINDL is developed FðsÞ¼½1 0:2249 sin s þ 0:1231 sinð2sÞ AY 0:0342 sinð4sÞ=ð1 0:2249Þ; ð40Þ EMPS GðhÞ¼0:408 0:323h⁰ þ 0:384h⁰² 0:17h⁰³; ð41Þ h⁰ ¼ 0:01h ð42ÞLMO

and h is solar elevation in degrees. While Rd0describes transpositionLMO factor for clear sky conditions, Rd1describes the transposition factor Olmo1 for overcast conditions: c h t c

Table 2

Data summary. CM11, CM22, CMP11 pyranometers and CH1, CHP1 pyrheliometers are manufactured by Kipp & Zonen; PSP pyranometer and NIP pyrheliometer are manufactured by Eppley; Star pyranometer is manufactured by Schenk GmbH; SPN1 pyranometer is manufactured by Delta-T; and Si-420TC-K silicon sensor is manufactured by Ingenieurbüro.

|Location|Latitude Longitude Altitude Albedo meas.? DNI meas.? Tilted sensors (tilt: s, azimuth: b)|
|---|---|
|Eugene 44.05 Golden 39.74 Oldenburg 53.15 Singapore 1.30 GHI|127.07 150 Yes Yes (30, 180); (90, 180); (90, 0) 105.18 1829 Yes Yes (40, 180); (90, 0); (90, 90); (90, 180); (90, 270) 8.17 40 No Yes (45, 180); (45, 135) 103.77 40 No No (10, 64); (20, 64); (30, 64); (40, 64); (90, 0); (90, 90); (90, 180); (90, 270) DHI DNI GTI Period Data link|
|Eugene Calc. Golden Calc. Oldenburg Calc. Singapore|Star CHP1 PSP 2015 [http://solardat.uoregon.edu/SelectArchival.html](http://solardat.uoregon.edu/SelectArchival.html) CM22 CH1 PSP 2014 [https://www.nrel.gov/midc/apps/go2url.pl?site=BMS](https://www.nrel.gov/midc/apps/go2url.pl?site=BMS) CM11 NIP CM11 2014 [http://doi.pangaea.de/10.1594/PANGAEA.847830](http://doi.pangaea.de/10.1594/PANGAEA.847830) CMP11 SPN1 Calc. Si-420TC-K 2013 Proprietary dataset, see Yang et al. (2014b)|
|where k t that accounts f ¼ 1 þ q sin² ðh=2Þ.O c diffuse irradiance directly. To make a rewritten into: G h O R ¼ exp½k d lmo1 D h O LMO et al., 2002). An is partitioned based on sky conditions: 8 3 q cos > < 1 0c f ¼ 1 q sin ðÞ h=2; > : 1; O R ¼ exp½k ðh² t d lmo2 2.15. T IAN T IAN (Tian et al., 2001): s T : R ¼ 1 dian 180 The tilt angle in T ADESCU 2.16. B B ADESCU (Badescu, 2002): 3 þ cos 2s B|is clearness index (the ratio of G and I) and f is a factor nents; and one may assume the result at once. More specifically, h oh c the effect of anisotropic reflections, E NGERER 2(Engerer, 2015) is recommended as a ‘‘quasi-universal” 1-min separation model; under appropriate conditions (e.g., low- LMO 1 is different from the other transposition albedo), considering only E NGERER 2 will most likely suffice. Such models in terms of parameter of interest. Instead of modeling the conclusions are hard to come by and thus are desired. However, on the inclined surface, O LMO 1 models GTI, performing studies that lead to such results is hardly an individual consistent model representation, Eq. (49) is effort, especially when a suitable database is lacking. On this point, I would welcome any contribution of data and results that can help no s I r 2 h b 2 2 evolve the current work. For now, the remaining part of the paper ðh z Þf q sin : ð50Þ t c 2 D h attempts to perform a preliminary evaluation of transposition model accuracies with 4 datasets. 1 is often found to produce significant errors, even at small tilt The 4 datasets used in this work are summarized in Table 2.As angles (e.g., Muzathik et al., 2011; Evseev and Kudish, 2009a; Ruiz some irradiance components are measured by multiple devices, alternative model, O LMO 2, is thus proposed by 0c the measurements with best accuracy are identified through previ- that Evseev and Kudish (2009a), with a new multiplying factor f ous studies (Gueymard, 2009; Yang et al., 2014b) and personal communication with the respective data owners. It is believed that ðÞ h=2; if 0 6 k < 0:35; every attempt has been made to ensure the quality of raw data by t respective owners. ð51Þ if 0:35 6 k 6 0:65; t As there is no optimal quality control sequence for irradiance otherwise: data, I follow Gueymard and Ruiz-Arias (2016) and apply the first Furthermore, the revised model is applied to diffuse radiation only: set of filters: 0c z² Þf : ð52Þ (1) z < 85. (2) G > 0 and D > 0 and I > 0. h h (3) I < 1100 þ 0:03 Altitude.. (4) I < I o 1:2 (5) D < 0:95I cos z þ 50. o h 1:2 < 1:50I cos z þ 100. (6) G o h ð53Þ (7) j100ðI cos z þ D G Þ=G j < 5%. h h h (8) D =G < 1:05 for G > 50 and z < 75. h h h IAN is in degrees. (9) D =G < 1:10 for G > 50 and z > 75. h h h Filters (1)–(9) are set mainly for irradiance quality control at the horizontal surface. For tilted data, I consider the following filters: (10) G > 0. c (11) 0:95 > q > 0:05 for Eugene and Golden datasets.|

Rdadescu¼ : ð54Þ (12) Slope adjustments for Gcin Eugene and Singapore datasets. 4

Data points that do not satisfy the above lists are rejected. After

3. Validation the raw datasets (1 min resolution) are averaged into 15 min inter-
vals, they are fed through the filters. For each location, about half of Before validating the 26 transposition models, we digress to dis-the data points (night time data points) are rejected by the z < 85 cuss a recent review on separation models, which predict DHI, and filter. On top of that, the combined rejection rate by all other filters thus DNI, using GHI and other observable parameters (such as is ≈ 15%. Normalized mean bias errors (nMBE, in percentage) and cloud fraction and clear sky irradiance). Owing to the importance normalized root mean squares errors (nRMSE, in percentage) on of separation modeling, one could immediately realize the rich lit-the filtered datasets using the 26 transposition models are tabu- erature on it. However, knowing which model could provide the lated in Tables 3 and 4, respectively. A total of 18 case studies highest possible accuracy at any specific location requires thor-(18 different orientations/locations) are presented. ough works. In the valuable review paper by Gueymard and A linear ranking method (Alvo and Yu, 2014) is used to rank the Ruiz-Arias (2016), 140 separation models have been validated with models based on nMBE and nRMSE, respectively. The models are 1-min data collected at 54 research-class stations from 7 conti-first ranked based on their performance at each orientation, i.e.,

Table 3

Normalized mean bias errors (nMBE, in percentage) using 26 transposition models on various datasets. The performance of each model is ranked for each orientation. The overall ranking of a model is then computed by averaging all of its rankings. Model Eugene (44:05; 127:07 ) Oldenburg (53:15; 8:17 ) Singapore (1:30; 103:77 )

|Model|Eugene (44:05;|127:07 )||Oldenburg (53:15;||8:17 )|Singapore (1:30;|103:77 )|||
|---|---|---|---|---|---|---|---|---|---|---|
||(30, 180)|(90, 180)|(90, 0)|(45, 180)|(45, 135)||(10, 64)|(20, 64)|(30, 64)|(40, 64)|
|Liu|2.2|3.6|11.1|5.6||3.7|0.3|1.7|0.7|1.0|
|Temps|5.3|11.1|30.0|8.3||9.6|5.0|4.0|5.7|6.8|
|Bugler1|0.5|1.9|11.2|3.3||1.5|1.5|0.1|1.0|0.8|
|Bugler2|2.3|4.5|5.1|5.1||3.4|0.7|2.2|1.2|1.4|
|Klucher|1.1|3.1|21.2|0.7||2.3|2.3|1.1|2.5|2.9|
|Steven1|4.3|11.9|6.4|10.5||10.4|0.0|1.0|0.7|1.4|
|Steven2|4.6|12.2|7.8|10.8||10.5|0.0|1.0|0.7|1.2|
|Steven3|3.1|9.1|1.5|8.0||6.2|0.5|2.4|2.1|3.3|
|Steven4|1.3|3.3|5.4|4.3||4.2|0.0|1.0|0.3|0.5|
|Hay1|0.3|1.4|6.3|1.1||0.2|0.2|1.7|0.8|1.3|
|Hay2|0.2|1.3|7.0|1.0||0.1|0.2|1.7|0.8|1.3|
|Willmott|1.5|1.3|7.0|3.1||2.3|1.0|3.5|3.2|4.0|
|Koronakis|1.5|6.0|29.1|3.0||1.0|0.2|1.2|0.5|1.4|
|Perez1|2.0|5.0|2.6|2.9||3.1|0.1|1.0|0.1|0.1|
|Perez2|2.2|5.0|1.8|3.2||3.4|0.3|0.7|0.4|0.1|
|Perez3|1.4|2.9|3.9|1.9||2.3|0.1|1.1|0.2|0.7|
|Perez4|1.2|2.8|4.0|1.2||1.5|0.0|1.3|0.4|0.9|
|Skartveit|0.6|5.3|19.9|2.1||1.2|0.2|1.9|1.3|2.1|
|Gueymard|0.6|0.6|5.2|2.2||1.1|0.0|1.4|0.5|1.0|
|Muneer1|0.0|0.2|10.7|0.2||0.9|0.1|1.2|0.2|0.4|
|Muneer2|0.4|2.4|9.9|0.2||1.3|0.1|1.1|0.4|0.8|
|Reindl|0.1|1.8|3.1|0.4||0.6|0.2|1.6|0.5|0.5|
|Olmo1|7.4|17.4|44.2|10.2||10.4|1.9|0.4|1.3|1.1|
|Olmo2|4.6|13.7|6.4|7.5||6.8|4.5|5.8|4.6|4.5|
|Tian|5.9|3.6|11.1|11.4||9.7|3.0|6.6|7.0|7.9|
|Badescu|4.3|3.6|11.1|11.4||9.7|0.7|3.4|4.3|6.8|
|Model|Singapore (90, 90)|(90, 180)|(90, 270)|(90, 0)|Golden (39:74; (40, 180)|105:18 ) (90, 0)|(90, 90)|(90, 180)|(90, 270)|Rank|
|Liu|2.6|13.8|5.3|14.3|3.9|8.5|2.5|1.6|1.2|15|
|Temps|20.7|30.0|23.8|29.9|3.0|24.2|9.3|9.1|12.4|26|
|Bugler1|3.7|14.0|6.1|14.5|1.1|8.5|0.6|0.3|0.5|12|
|Bugler2|1.7|11.7|4.0|12.4|3.6|3.2|3.2|1.9|2.7|16|
|Klucher|12.0|22.3|14.7|22.5|0.2|17.8|4.3|4.3|6.6|19|
|Steven1|11.6|10.9|12.3|9.7|2.9|5.0|4.2|8.8|6.7|18|
|Steven2|10.9|10.1|11.6|8.6|3.2|6.3|3.8|9.0|6.3|20|
|Steven3|5.9|4.0|4.0|4.9|5.1|1.2|7.4|5.6|6.8|17|
|Steven4|6.6|7.3|5.7|7.6|0.9|4.8|0.8|5.0|3.4|11|
|Hay1|0.8|6.3|1.1|7.2|1.0|7.7|2.3|1.3|1.6|6|
|Hay2|0.8|6.0|1.0|7.0|0.9|8.3|2.3|1.4|1.6|5|
|Willmott|0.8|6.0|1.0|7.0|2.1|8.3|2.3|1.4|1.6|13|
|Koronakis|16.4|28.6|19.9|28.7|2.7|23.4|6.0|5.5|8.7|21|
|Perez1|3.1|5.9|2.2|5.7|1.2|1.8|1.2|5.5|2.9|8|
|Perez2|2.8|5.4|1.9|5.4|1.4|1.2|1.3|5.4|2.7|10|
|Perez3|0.9|3.4|0.0|3.8|0.5|3.0|0.1|3.8|1.4|2|
|Perez4|0.6|4.1|0.0|4.4|0.3|2.9|0.5|3.7|0.8|1|
|Skartveit|5.0|1.3|5.5|0.0|1.4|15.5|5.1|0.8|5.0|14|
|Gueymard|2.3|9.3|3.4|10.2|1.5|4.8|0.0|1.9|1.4|7|
|Muneer1|1.4|7.3|1.3|7.1|0.4|7.7|1.6|2.9|0.0|3|
|Muneer2|2.0|7.6|1.7|8.0|0.3|7.1|0.2|5.1|1.5|4|
|Reindl|7.0|13.9|8.0|14.6|0.7|0.3|0.9|3.8|2.1|9|
|Olmo1|13.2|22.8|16.4|20.4|7.4|32.6|9.4|10.0|15.5|25|
|Olmo2|10.2|10.8|9.3|9.8|3.0|2.4|5.1|9.9|7.3|24|
|Tian|2.6|13.8|5.3|14.3|7.4|8.5|2.5|1.6|1.2|23|
|Badescu|2.6|13.8|5.3|14.3|6.8|8.5|2.5|1.6|1.2|22|

rank the numbers in each column of Tables 3 and 4. The overall ranking is then computed by ordering the mean ranks of the mod- els; the mean rank Riof a model i is given by:

X m! Ri¼ njmjðiÞ=n; ð55Þ j¼1

where mj; j ¼ 1; 2;...; m! represents all possible rankings of the m Pm models; njis the observed frequency of ranking j; n ¼j¼1nj; and m j ðiÞ is the rank score given to object i in ranking j. It is found, with no surprise, that the rankings based on nMBE and nRMSE are differ- ent. Nevertheless, PEREZ4 performs the best in both rankings.

The above-mentioned ranking method have two deficiencies:

(1) it is difficult to visualize the performance of a model against all other models in all scenarios, (2) when the errors of two models are close, we are not certain if the observed difference is signifi- cant. For these reasons, Diebold–Mariano (DM) test (Diebold and Mariano, 1995) is performed to compare the prediction accuracy of the 18 case studies. I consider a squared loss function, i.e., geModel A¼ eModel A, where eModel Adenotes the prediction error t t t for Model A at time interval t. The null hypothesis of the DM test is that the mean of the loss differential: d ge Model A
ge Model B; ð56Þ t t

Table 4

Normalized root mean squares errors (nRMSE, in percentage) using 26 transposition models on various datasets. The performance of each model is ranked for each orientation. The overall ranking of a model is then computed by averaging all of its rankings. Model Eugene (44:05; 127:07 ) Oldenburg (53:15; 8:17 ) Singapore (1:30; 103:77 )

|Model|Eugene (44:05;|127:07 )||Oldenburg (53:15; 8:17 )|||Singapore (1:30; 103:77 )|
|---|---|---|---|---|---|---|---|
||(30, 180)|(90, 180)|(90, 0)|(45, 180)|(45, 135)||(10, 64)|
|Liu|5.5|14.1|31.3|11.9|13.2||4.3|
|Temps|8.1|17.0|46.0|12.4|13.6||7.3|
|Bugler1|4.7|12.3|31.1|9.7|11.2||4.9|
|Bugler2|4.9|13.1|30.6|11.0|11.9||3.9|
|Klucher|4.4|11.5|39.2|6.7|8.5||5.3|
|Steven1|7.6|20.3|23.9|15.1|15.6||3.7|
|Steven2|7.5|20.0|23.0|15.1|15.4||3.6|
|Steven3|6.0|17.2|27.1|13.8|14.5||4.3|
|Steven4|5.1|13.2|20.8|10.4|10.2||3.0|
|Hay1|4.0|9.1|29.1|6.8|7.2||3.0|
|Hay2|4.1|9.0|29.5|6.7|7.1||3.0|
|Willmott|4.8|9.0|29.5|7.8|7.9||3.3|
|Koronakis|5.0|15.4|45.4|10.5|12.4||4.3|
|Perez1|4.3|9.2|20.5|6.6|6.2||2.7|
|Perez2|4.3|9.3|19.2|6.7|6.4||2.9|
|Perez3|3.9|8.3|19.8|6.1|5.9||2.8|
|Perez4|3.8|8.4|20.1|6.3|6.1||2.8|
|Skartveit|4.2|11.4|32.3|7.1|7.3||3.0|
|Gueymard|4.2|10.7|26.1|7.4|8.0||3.3|
|Muneer1|4.0|10.0|25.6|6.3|7.1||3.0|
|Muneer2|4.4|12.2|24.5|7.2|7.8||3.1|
|Reindl|4.0|9.1|30.7|6.5|7.1||3.0|
|Olmo1|10.8|26.1|53.9|16.8|17.6||5.0|
|Olmo2|8.1|22.4|24.7|13.4|13.6||7.6|
|Tian|8.6|14.1|31.3|16.9|17.1||5.6|
|Badescu|7.1|14.1|31.3|16.9|17.1||4.3|
|Model|Singapore (90, 90)|(90, 180)|(90, 270)|(90, 0)|Golden (39:74; (40, 180)|105:18 ) (90, 0)|(90, 90)|
|Liu|25.0|24.2|24.6|23.8|7.6|24.5|14.1|
|Temps|30.1|39.0|33.1|38.5|6.9|38.7|16.4|
|Bugler1|23.2|24.3|23.3|23.8|5.8|24.4|12.2|
|Bugler2|23.1|22.3|22.9|22.2|6.9|26.7|13.1|
|Klucher|25.7|33.3|27.8|32.3|4.4|30.7|13.0|
|Steven1|24.1|22.8|25.4|18.9|7.4|19.7|15.0|
|Steven2|23.7|23.2|25.2|18.8|7.3|19.3|14.4|
|Steven3|25.8|18.7|24.1|17.6|8.5|19.2|15.5|
|Steven4|19.7|21.2|20.4|17.7|5.1|19.4|11.4|
|Hay1|16.1|18.5|17.0|18.2|5.3|31.3|11.8|
|Hay2|16.0|18.4|16.9|18.2|5.2|31.9|12.0|
|Willmott|16.0|18.4|16.9|18.2|6.0|31.9|12.0|
|Koronakis|31.0|38.0|33.3|37.7|6.8|38.0|17.0|
|Perez1|12.6|17.3|12.8|14.9|4.3|13.8|8.5|
|Perez2|12.9|16.8|12.5|14.8|4.2|13.7|8.5|
|Perez3|12.6|16.2|12.2|14.3|4.1|14.1|8.2|
|Perez4|12.6|16.7|12.5|14.6|4.0|13.8|8.2|
|Skartveit|16.6|17.9|17.1|15.8|5.4|29.4|12.7|
|Gueymard|17.1|21.1|17.3|19.4|5.1|18.4|9.8|
|Muneer1|16.0|22.4|17.1|19.1|4.8|19.2|10.4|
|Muneer2|17.2|24.2|18.3|20.6|5.2|19.0|11.7|
|Reindl|18.0|23.7|19.7|23.3|5.0|31.3|11.7|
|Olmo1|25.6|29.5|26.7|28.1|14.2|38.5|23.5|
|Olmo2|21.7|22.3|22.8|21.3|9.0|28.7|16.9|
|Tian|25.0|24.2|24.6|23.8|10.6|24.5|14.1|
|Badescu|25.0|24.2|24.6|23.8|10.1|24.5|14.1|

|(20, 64)|(30, 64)|(40, 64)|
|---|---|---|
|7.1|11.0|13.0|
|7.2|10.2|11.7|
|6.2|10.1|11.6|
|6.5|10.0|11.7|
|5.8|9.0|10.3|
|6.1|8.6|10.8|
|6.0|8.4|10.8|
|7.3|11.3|13.4|
|4.7|6.5|8.3|
|4.5|6.8|7.7|
|4.5|6.7|7.6|
|5.7|7.5|8.6|
|6.9|11.0|13.1|
|3.4|4.9|5.2|
|3.4|4.9|5.3|
|3.6|5.0|5.3|
|3.6|5.1|5.3|
|4.6|6.8|7.9|
|4.7|7.2|8.1|
|4.5|7.0|8.2|
|4.4|7.0|8.1|
|4.5|6.7|7.7|
|7.5|10.1|12.7|
|9.6|9.9|12.3|
|10.3|13.7|15.8|
|7.8|12.1|15.1|
|||Rank|
|(90, 180)|(90, 270)||
|9.8|14.8|19|
|13.2|20.0|25|
|9.0|13.1|15|
|9.0|14.3|14|
|9.5|14.7|16|
|14.9|19.2|18|
|14.7|18.5|17|
|11.6|15.6|20|
|11.3|15.7|13|
|8.7|14.7|7|
|8.9|15.0|6|
|8.9|15.0|12|
|12.0|19.9|24|
|9.0|9.2|3|
|8.8|9.1|4|
|7.7|8.8|2|
|7.6|7.9|1|
|9.8|14.6|10|
|8.5|9.7|8|
|9.6|12.6|5|
|11.9|13.9|11|
|9.2|15.0|9|
|20.9|29.7|26|
|17.6|24.1|21|
|9.8|14.8|23|
|9.8|14.8|22|

is 0, i.e., H₀ : EðdÞ¼0. As either Model A or Model B could be better, be found that the two models perform differently. Fig. 2 suggests a two-sided alternative is used, H₁ : EðdÞ – 0. For each pair of mod-that no universal model is found (a universal model in this case els, a total of 18 DM tests are performed; the results are depicted in would be a model that outperforms all other models in all case

Fig. 2. The entries denote ‘‘Model A better than Model B” scenarios, studies). However, it is evident that PEREZ family of models perform

i.e., well against other models. Model A

|EðdÞE ge||ge|< 0:|||ð57Þ||
|---|---|---|---|---|---|---|---|
||||||||4. Concluding remarks|
|For examples, the entry ‘‘1” in the first row (from top) first column||||||||
|denotes (Model B) in 1 out of 18 case studies; the entry ‘‘16” in the last|that B|(Model|A) performs|better|than W||A total of 26 transposition models are arranged, discussed and validated using 18 case studies from 4 sites. Model performance|
|row last out of 18 times; and for the remaining test case, no evidence can|column indicates|that|W|outperforms|B|16|comparison is conducted through two approaches, namely, linear ranking and pairwise hypothesis testing. According to the linear|
 t
Model B t

ADESCU ILLMOTT

ILLMOTT ADESCU

|1|3210|13 9|30|11 9|0216161818 8||15 2237||10 10|
|---|---|---|---|---|---|---|---|---|---|
|6 16|17 18|16 16|8|17 17|411|81718181817 15|10 10|14 15|86 016|
|12 18|18 18|18 18|18 15|15 18 18|61018 18|18 18 18 18|13 13|15 18|0 1218|
|2|5511|11 12|62|12 10|001718181810||12 0140||20 29|
|3 12|13 14|13 13|10 6 11|16 15|121818181813||16 6 7|0 14|3 313|
|9 10|11 15|16 16|9 6 10|16 15|051818181814||16 1 0|11 17|5 816|
|9 10|10 15|16 16|10 6 10|17 15|051818181814||16 0 14|11 18|5 816|
|0||11 11||21695|01|20141418180|10|2215|00 03|
|2||10 13||359118|04|10141518177|0|4456|20 29|
|0||||00000|000043800 00||0|0000|00 00|
|0||||00000|000054080 00||0|0000|00 00|
|0||||11220|44109013141 00||3|0000|00 02|
|0||||11220|33000613132 00||3|0000|00 02|
|8 11|12 17|16 16|12|11 18 17|20|91818181817 14|13 13|14 18|6 716|
|15 17|18 18|18 18|13 12|16 18 18|01618 18|18 18 18 18|18 18|16 18|11 1418|
|1|3210|13 12||13 0|01|401717181812 9||2337|10 17|
|0||||11503|7710161518178 00||5|1124|00 04|
|0 15|17 18|16 16|8|17 17|17|61718181817 15|8 8|6 15|02 016|
|17 10|16 18|18 18|17 0 12|18 17|681818181818||1812 12|11 16|2 18 10|
|9 10|10 16|16 16|0 1|16 13|461616181817||15 8 8|8 11|90 815|
|1||||22574|6010141418187 02||3|2233|10 19|
|1||||22484|01110141418187 02||7|2234|10 15|
|0||12 12||000135|01|201616181811|8|3346|00 07|
|1|9017|15 15|82|17 14|031717181813||16 77513||10 115|
|3|0918|15 15||17 15|04|811717181815 15||88613|30 213|
|0 15|18 17|16 16|8|17 17|29|81718181817 15|9 9|14 15|016 85|

Willmott Tian Temps Steven4 Steven3 Steven2 Steven1 Skartveit Reindl Perez4 Perez3 Perez2 Perez1 Olmo2 Model B Olmo1 Muneer2 Muneer1 Liu Koronakis Klucher Hay2 Hay1 Gueymard Bugler2 Bugler1 Badescu

Liu Hay1Hay2 Klucher Badescu Bugler1Bugler2 Koronakis Muneer1 Gueymard

Fig. 2. Pairwise Diebold–Mariano (DM) tests for comparing the predictive accuracy of various models. For each pair of models, we count the number of instances the DM test

statistics falls in the lower or upper 2.5% tail of a standard normal

ranking results on nRMSE, the top four (families of) models are PEREZ,MUNEER,HAY and GUEYMARD. This result agrees with the findings concluded by Hay and McKay (1988). Results of the pairwise Diebold–Mariano tests show that no universal model can be concluded. However, we are able to obtain some insights from a simple clustering analysis. Using the k-means via principal compo- nent analysis on the data matrix presented in Fig. 2, four clusters can be established: (1) PEREZ1, PEREZ2, PEREZ3, PEREZ4; (2) GUEYMARD, HAY1, HAY2, MUNEER1, MUNEER2, REINDL,SKARTVEIT,STEVEN4, WILLMOTT;

(3) BUGLER1, BUGLER2, LIU,KLUCHER,STEVEN1, STEVEN2, STEVEN3; and (4) BADESCU,KORONAKIS,OLMO1, OLMO2, TEMPS,TIAN. This clustering out- come can provide a guideline on which models to choose for future studies. Based on the results of this paper, including the models out of the first two clusters is expected to provide the most accurate results. Future work should address detailed uncertainty modeling and error analyses to further our understanding on the preferred mod- els. For example, Tables 3 and 4 reveal that most transposition models struggle to perform in cases with vertical surfaces. As the foreground’s albedo is a crucial modeling parameter in such cases, an experiment that varies the albedo could be useful to elucidate error sources. In addition, developing more advanced transposition models with universal applicability should be attempted. The diffuse irra- diance received by inclined surfaces can be calculated from angular sky radiance distribution. Most of the transposition models
Reindl Temps Tian Muneer2 Olmo1Olmo2Perez1Perez2Perez3Perez4 Skartveit Steven1Steven2Steven3Steven4 Willmott Model A

distribution. The entries denote ‘‘Model A better than Model B” scenarios, i.e.,

presented in this paper model the diffuse irradiance received by a sloped plane according to a two-part or three-part geometrical framework. However, the errors due to the approximations used in these simplified models are sometimes found to be significant (Matagne and Bachtiri, 2014; Torres et al., 2006). Therefore, calcu- lating the tilted diffuse irradiance by integrating the radiance dis- tribution is attractive and has great potential in moving towards a universal model. Furthermore, as mentioned by several authors (e.g., Perez et al., 1990; Gueymard, 1987), a good amount of high quality data from geographically and climatically dispersed sources is also essential for developing a universal model. Before a universal model can be established and accepted by the community, location-specific validation studies will continue to be carried out. Although, academically, these studies are of local and limited interest, they are important to their respective subsequent solar engineering applications. As suboptimal or incorrect model implementations may lead to high errors and thus false conclu- sions, one should be skeptical about any unusual error terms observed during a validation study. To facilitate future studies, the R code and a small test dataset for benchmarking purposes is provided in the supplementary materials.

Conflict of interest

The author declared that there is no conflict of interest.

EðdÞE geModel A tgeModel B t< 0. For example, out of the 18 case studies, BADESCU performs better than BUGLER1 in 3 case studies (the entry is at the bottom left corner).

Acknowledgments

I would like to thank Chris Gueymard, Jan Kleissl, Elke Lorenz, André Nobre, Dave Renné and Frank Vignola for providing valuable insights and facilitating the author to obtain the data. My special thanks goes to Thomas Schmidt who helped arrange the data for Oldenburg (Kalisch et al., 2015).

Appendix A. Why are some earlier models considered by Hay and McKay (1988) not included in this study?

The 21 models considered by Hay and McKay (1988) are listed in Table A.5. As indicated in the last column of the table, 10 out of 21 models are included in the present study. There are two main reasons for not including the remaining 11 models: (1) the original study shortlisted four models (Gueymard, Hay and two versions of Perez) after a preliminary validation, while the other models were consistently outperformed by the four models; (2) empirical evi- dence (see below) shows that some models are less popular than others due to various reasons. This appendix focuses on illustrating the latter point. Google Scholar citation is a reasonable indicator of popularity and impact of a publication. After searching the references listed in Table A.5 using Google Scholar, it is found that 9 out of 24 refer- ences, namely, Lawrence Berkeley Lab. (1982), Josefsson (Pers. Comm., 1985), Ineichen (1983), ASHRAE (1976), Van den Brink, ASHRAE (1971), Oegema (1971), Rogers et al. (1979) and Perez (Pers. Comm., 1985), are not tracked by Google Scholar. Despite that some of these 9 references can be found via a regular Google search, it is believed that their impacts are limited by problems such as non-English text, lengthy document and lack of digital ver- sion. They are thus not considered in the present study.

Table A.5 Hourly transposition models considered by Hay and McKay (1988). The model names follow the original publication. The third column of the table indicates whether a model is included in the present study. <u>Model Reference In this study?</u> Isotropic Kondratyev and Manolova (1960) Yes Liu and Jordan (1963) 50/50 Comb Hay (1979) No Bugler1 Bugler (1977) Yes Bugler2 Hay and McKay (1985) Yes Hay et al. (1986) C&Z Cohen and Zerpa (1982) No DOE2 Lawrence Berkeley Lab. (1982) No Gueymard Gueymard (1983) Yes Hay Hay (1979) Yes Hay and Davies (1980) Hay2 Josefsson (Pers. Comm., 1985) No Skartveit Skartveit and Olseth (1986) Yes Ineichen Ineichen (1983) No Klucher Klucher (1979) Yes Kusada ASHRAE (1976) No Van den Brink Van den Brink No Lokmanhekim ASHRAE (1971) No Oegema Oegema (1971) No Page Page (1979) No Rogers et al. (1979) Perez1 Perez et al. (1983) Yes Perez2 Perez (Pers. Comm. 1985) Yes Puri Puri et al. (1980) No T&C Temps and Coulson (1977) Yes

The Google Scholar citation data of the remaining references are plotted in Fig. 3. Note that among the remaining 15 references, two references, namely, Gueymard (1983) and Perez et al. (1983), have more well-known versions (Gueymard, 1987; Perez et al., 1990,

1987). These more recent versions are used for citation plotting. Furthermore, Hay et al. (1986) is the errata to Hay and McKay (1985); it is thus not plotted. It can be concluded that most of these references receive increasing attention over the years, while Cohen and Zerpa (1982), Puri et al. (1980), Page (1979) are less cited. Based on this empirical evidence, together with the findings in Hay and McKay (1988), this study investigates only the selected models. Appendix B. Notes on BUGLER model In Hay and McKay (1985), Eq. (8) was given incorrectly as: D#s¼ 0:5ðD#0:05I= cos zÞð1 þ cos aÞþ0:05I cos i; where D#sand D# are diffuse irradiance on inclined and horizontal surfaces, respectively; i and z are incidence and zenith angles; a is surface tilt and I is direct normal irradiance. The authors made a correction later and updated their results (Hay et al., 1986): D#s¼ 0:5ðD#0:05I cos zÞð1 þ cos aÞþ0:05I cos i: Nevertheless, an incorrect equation was displayed in Kambezidis et al. (1994) (in addition to the above typo, the authors also mixed up DNI with beam irradiance in their equation), and subsequently the exact form of incorrect expression is repeated in many other works (e.g., Wattan and Janjai, 2016; Demain et al., 2013; Gulin et al., 2013; Gracia and Huld, 2013; Souza and Escobedo, 2013; Włodarczyk and Nowak, 2009; Notton et al., 2006). On a separate note, the BUGLER models used in this paper are the interpretations of Hay et al. (1986) and Hay and McKay (1985).In the original publication, DNI and DHI were unknown; they were computed separately using the approaches described in Sections
2.1 and 2.2 of Bugler (1977). Such treatment implies a departure from the conventional closure equation (see Eq. (3.5) of Bugler,
1977). Consequently, the global tilted irradiance derived through this approach will most likely be different from that of BUGLER1. Though the model is still open to interpretation, on the account of our earlier model ranking results, further investigation seems unnecessary. Appendix C. Notes on STEVEN model STEVEN1 and STEVEN2 are not explicitly expressed in Steven and Unsworth (1979)’s original paper. This results in a large number of repetitive, incorrect interpretation of the models (such as Khatib et al., 2015; Khalil and Shaffie, 2013a; Khalil and Shaffie, 2013b; Lahjouji and Darhmaoui, 2013; Souza and Escobedo, 2013; Yadav and Chandel, 2013; Khatib et al., 2012; Benghanem, 2011; Noorian et al., 2008; Kamali et al., 2006). However, the method to deduce those empirical parameters is well documented. In this paper, I reproduce some results from Steven and Unsworth (1979) to demonstrate the correct use of STEVEN family of models. By integrating the standard distribution (see Steven, 1977)of clear sky radiance, the relative diffuse irradiance (ratio between tilted and horizontal diffuse irradiance components, i.e., Dc=Dh) can be obtained. These numbers are given in Tables 1–4 of Steven and Unsworth (1979), for a range of zenith, tilt and azimuth angles. In what follows, both Eq. (11) and a commonly used wrong model:

||Temps and Coulson, 1977 (275)||Puri et al., 1980 (22)||Perez et al., 1990 (1043)||
|---|---|---|---|---|---|---|
|25 20 15 10 5 0||4 3 2 1 0||120 100 80 60 40 20 0|||
||Perez et al., 1987 (478)||Page, 1979 (22)||Klucher, 1979 (477)||
|50 40 30 20 10 0||3 2 1 0||50 40 30 20 10 0|||
||Cohen and Zerpa, 1982 (4)||Skartveit and Olseth, 1986 (148)||Gueymard, 1987 (144)||
|1 No. of citations 0||15 10 5 0||15 10 5 0|||
||Hay, 1979 (112)||Hay and Davies, 1980 (236)||Hay and McKay, 1985 (233)||
|67 45 23 01||25 20 15 10 5 0||20 15 10 5 0|||
||Bugler, 1977 (164)||Liu and Jordan, 1963 (554)||Kondratyev and Manolova, 1960 (60)||
|10 8 6 4 2 0|1977 1987 1997 2007 2015 June are indicated in the parentheses beside the references. Source: Google Scholar, accessed on 2016 June 2.|40 30 20 10 0|1977 1987 1997 2007 2015 Year Fig. 3. Google Scholar citation data for transposition models considered by Hay and McKay (1988). Only citations after 1977 are plotted; total numbers of citations up to 2016|56 4 3 2 01|1977 1987 1997 2007 2015||

Table C.6 Parameters b and S for STEVEN diffuse radiation models at a range of solar zenith angles (cf. Steven and Unsworth, 1979). <u>Parameters all z 35 45 55 65</u> STEVEN b 0.87 1.04 1.00 0.90 0.85 S 0.51 0.63 0.60 0.53 0.46 Eq. (11) b 0.88 1.09 0.99 0.91 0.85 S 0.52 0.67 0.59 0.53 0.46 Eq. (C.1) b 7.87 3.87 5.40 6.76 7.58 S 0.30 0.19 0.26 0.31 0.35

2<u>s</u> R d¼ Srbþ cos 2 2b hi 2<u>s</u> þ sin s s cos s p sin ðC:1Þ pð3 þ 2bÞ 2

are fitted to the irradiance values in Tables 1–4 of Steven and Unsworth (1979); the fitted parameters are shown in Table C.6.It can be concluded that Eq. (11) corresponds to the original models (the fitted parameters are precise; the remaining deviation likely originates from the different non-linear least squares routines used). When the above wrong Eq. (C.1) is used, the predicted Gcis far from its actual value. The resultant high errors thus often lead to false conclusions (e.g., Noorian et al., 2008; Kamali et al., 2006).

Appendix D. Notes on GUEYMARD model

The original paper by Gueymard (1987) has two typographical errors. The subsequently published erratum (Gueymard, 1988) corrected the numerical values of those two coefficients. Ignoring the erratum will likely result in large prediction errors (such as

Diez-Mediavilla et al., 2005). While some of these erroneous imple- mentations have been pointed out and corrected (Diez-Mediavilla et al., 2006), others remain (e.g., Demain et al., 2013).

Appendix E. Other errors found in the references

Table E.7 shows some errors found in some references. The symbols used in the table follow their corresponding original doc- uments; they should not be mixed with symbols defined in the nomenclature. Some of these errors are typographical and thus do not affect the results; some errors lead to wrong implementa- tions, which can be deduced from the unusual error metrics reported. These errors may not be exhaustive.

Appendix F. Supplementary material

Supplementary data associated with this article can be found, in the online version, at [http://dx.doi.org/10.1016/j.solener.2016.06](http://dx.doi.org/10.1016/j.solener.2016.06).

062. The transposition models used in this work are implemented in R (R Core Team, 2015). The code is released in the form of an R pack- age. After unzipping the supplementary material, users should find three items, namely, a pdf document (SolMod-manual.pdf) which contains the package documentation, an R script (test.R) to gener- ate nRMSE based on the sample data, as well as a folder (SolMod) which contains all the necessary files to build and install the pack- age. Further information on building and installing R packages can be found at [http://kbroman.org/pkg_primer/pages/build.html](http://kbroman.org/pkg_primer/pages/build.html). In addition to the implementation of the transposition models, the package also performs solar positioning. The solar positioning function (solpos) is a wrapper over some functions in the ‘insol’ package (Corripio, 2014). The example dataset

Some errors found in the references. Errors pointed out earlier are not repeated here. Table E.7

<u>Author</u> Khatib et al. (2015)

Yoon et al. (2014)

David et al. (2013) Gracia and Huld (2013) Khalil and Shaffie (2013a) Khalil and Shaffie (2013b)

<u>Error</u> Eq. (9) Eqs. (12) and (14) Eq. (3) Eq. (4) Eq. (7) Eq. (8) Eq. (6) Eq. (37)

Section 4

Eq. (39)

Eq. (41) Eq. (43) Eq. (48)

Eq. (14)

Eq. (20) Eq. (28)

Eq. (30) Eq. (16)

Eq. (23) Eqs. (27c) and (27d) Eqs. (A.5), (A.12) and (A.13) Eq. (A.6) Eq. (A.7) Eq. (10) Eqs. (13), (15) and (16) Eq. (7)

Eq. (12)

Eq. (13)

Table 1

Table 1

Eq. (12)

Remark Should read: RD¼ð2 þ cos TLTÞ=3 Hay’s anisotropy index should be B=Iohinstead of B=G Should read I ¼ IDNcos i þ IdHfð1 KÞSVF þ K cos i= cos hzgþIGHqGVF Should read: I ¼ IDNcos i þ IdHfð1 KÞSVF SQRT½ðIGHIdHÞ=IGHsin³ðb=2ÞþK cos i= cos hzgþIGHqGVF Should read: I ¼ IDNcos i þ IdHfTð1 KÞþK cos i= cos hzgþIGHqGVF The term 2SVF should not appear hi Should read: ei¼ðIDþ IB;nÞ=ðIDÞþ5:535 10 6 Z³ =ð1 þ 5:535 10 6 Z³Þ Should read: f ¼ pffiffiffiffiffiffiffiffiffiffiffi Gb=G

Inconsistent use of symbols. Several other errors found in this section, reappeared verbatim in Khalil and Shaffie (2013b), are listed next Should read: Rd¼ð3 þ cos 2bÞ=4

Should read: Rd¼ð2 þ cos bÞ=3 Reindl’s modulating factor is expressed wrongly Should read: Gd;T¼ Gd;g <u>1þcos</u> 2 <u>b</u>1 þ F₁ sin 3 2<u>b</u> ð1 þ F₁ cos² h sin³ hzÞ. Furthermore, Klucher’s modulating factor should be: F₁ ¼ 1 ðGd;g=GgÞ² Should read: Rd¼ð2 þ cos bÞ=3

Should read: HT¼ðHg HdÞRbþ Hg q<u>1 cos</u> 2 <u>b</u>þ HdRd Should read: ID;b;a¼ ID½fðbÞð1 KbÞþKbcosl= sin cs. Furthermore, Eq. (28) should only apply to sunlit surface under non-overcast skies Should read: fðbÞ¼ cos²ðb=2Þþ2c=p=ð3 þ 2cÞ½sin b ðbp=180Þ cos b p sin²ðb=2Þ Should read: HhRb¼ HhDH½ð2 þ cos bÞ=3 Appears to be a wrong model that leads to skeptical errors terms Should read: Y ¼ 6:6667KhDH1:1467 if KhDH0:227 and Y ¼ 1:2121KhDH0:1758 otherwise, respectively I Difin those equations should read IGloIDif

F⁰ in the equation should be 1 ðIDif=IGloÞ² Should read: e ¼ hiIDifIþIDirþ jZ180p 3 hi 1 þ jZ180p 3 Dif Should read RD¼<u>2þcos</u>3 <u>TLT</u> Hay’s anisotropy index in those equations should read ðETEDÞ=Eextra

Should read: WM IðIgÞ¼kt rbþð1 ktÞ cos²ðb=2Þ

Eq. (12b) is used for a sunlit surface under a non-overcast sky. For a sunlit surface under a overcast sky and shaded surface, the b values should be 1.68 and 5.73 respectively The first term should read: ð1 þ cos bÞ=2

Hay model should read:G<u>Bh</u>rbþ 1G<u>Bh 1þcos</u> 2 <u>s</u> oh oh The last term in Temps and Coulson model should read ½1 þ cos²ðhÞ sin³ðZÞ Should read: F₂₁ þ DF₂₂ þ hzF₂₃

Lahjouji and Darhmaoui (2013)

Lee et al. (2013)

Souza and Escobedo (2013)

Yang et al. (2013)

Khatib et al. (2012)

Evseev and Kudish (2009b)

Włodarczyk and Nowak (2009) Noorian et al. (2008)

Diez-Mediavilla et al. (2005)

|provided by the package contains all necessary solar positioning|||
|---|---|---|
|parameters.|To use|the package,|
|running|for|a demonstration.|
|should look like:|||
|> rmse|(40, 180)|(90, 0)|
|Liu|5.7|25.2|
|Temps|6.6|40.2|
|Bugler1|4.7|25.1|
|Bugler2|5.7|24.8|
|Klucher|5.2|33.1|
|Steven1|5.0|17.9|
|Steven2|5.3|17.2|
|Steven3|6.7|17.8|
|Steven4|4.4|17.1|

||||Hay1|4.8|25.2|10.3|13.0|16.4|
|---|---|---|---|---|---|---|---|---|
|the|users could|start with|Hay2|4.8|25.5|10.4|13.1|16.6|
|The|output|from test.R|Willmott|5.9|25.5|10.4|13.1|16.6|
||||Koronakis|5.3|39.5|19.8|26.2|27.1|
||||Perez1|4.2|12.9|5.9|11.9|10.1|
||||Perez2|4.3|13.4|6.3|11.6|10.7|
|(90,|(90,|(90,|Perez3|4.1|13.1|6.4|10.8|10.3|
|16.5|13.1|19.7|Skartveit|4.9|21.6|11.4|12.5|15.0|
|18.6|27.2|27.1|Gueymard|4.6|18.5|9.9|12.6|12.0|
|14.0|13.4|18.0|Muneer1|4.3|15.2|8.8|16.8|12.7|
|14.7|12.1|18.7|Muneer2|4.3|14.6|9.5|18.9|13.7|
|15.4|21.0|20.8|Reindl|4.5|27.4|10.7|15.7|17.5|
|12.8|15.1|22.4|Olmo1|8.8|32.5|21.9|27.9|29.7|
|12.5|15.4|22.0|Olmo2|4.5|25.9|14.6|16.2|25.4|
|17.7|9.2|19.6|Tian|9.7|25.2|16.5|13.1|19.7|
|10.2|14.3|18.7|Badescu|8.9|25.2|16.5|13.1|19.7|

90) 180) 270) Perez4 4.1 12.6 6.4 11.4 9.1

test.R

References

Alvo, M., Yu, P.L.H., 2014. Exploratory analysis of ranking data. In: Statistical Methods for Ranking Data. Frontiers in Probability and the Statistical Sciences. Springer, New York, pp. 7–21. Badescu, V., 2002. 3D isotropic approximation for solar diffuse irradiance on tilted surfaces. Renew. Energy 26, 221–233. Benghanem, M., 2011. Optimization of tilt angle for solar panel: case study for Madinah, Saudi Arabia. Appl. Energy 88, 1427–1433. Bugler, J., 1977. The determination of hourly insolation on an inclined plane using a diffuse irradiance model based on hourly measured global horizontal insolation. Solar Energy 19, 477–491. Chwieduk, D.A., 2009. Recommendation on modelling of solar energy incident on a building envelope. Renew. Energy 34, 736–741. Cohen, B., Zerpa, N., 1982. Spatial transformations of insolation measurements- preliminary results. Solar Energy 28, 75–76. Corripio, J.G., 2014. Insol: Solar Radiation. r package version 1.1.1. <[http://CRAN.R-](http://CRAN.R-) project.org/package=insol>. Dahmani, K., Dizene, R., Notton, G., Paoli, C., Voyant, C., Nivet, M.L., 2014. Estimation of 5-min time-step data of tilted solar global irradiation using ANN (artificial neural network) model. Energy 70, 374–381. David, M., Lauret, P., Boland, J., 2013. Evaluating tilted plane models for solar radiation using comprehensive testing procedures, at a southern hemisphere location. Renew. Energy 51, 124–131. Demain, C., Journée, M., Bertrand, C., 2013. Evaluation of different models to estimate the global solar radiation on inclined surfaces. Renew. Energy 50, 710–

721.
Diebold, F.X., Mariano, R.S., 1995. Comparing predictive accuracy. J. Bus. Econ. Stat. 13, 253–263. [http://dx.doi.org/10.2307/1392185](http://dx.doi.org/10.2307/1392185). Diez-Mediavilla, M., Bilbao, J., de Miguel, A., 2006. Erratum to ‘‘Measurement and comparison of diffuse solar irradiance models on inclined surfaces in Valladolid (Spain)” [Energy Conversion and Management 46 (2005) 2075–2092]. Energy Convers. Manage. 47, 3504–3506. Diez-Mediavilla, M., de Miguel, A., Bilbao, J., 2005. Measurement and comparison of diffuse solar irradiance models on inclined surfaces in Valladolid (Spain). Energy Convers. Manage. 46, 2075–2092. Engerer, N., 2015. Minute resolution estimates of the diffuse fraction of global irradiance for southeastern Australia. Solar Energy 116, 215–237. Escobedo, J., Souza, A., Martins, D., 2014. An assessment of the diffuse radiation models for prediction on hourly global radiation in tilted surface. Nativa 2, 23–

31.
Evseev, E.G., Kudish, A.I., 2009a. An assessment of a revised Olmo et al. model to predict solar global radiation on a tilted surface at Beer Sheva, Israel. Renew. Energy 34, 112–119. Evseev, E.G., Kudish, A.I., 2009b. The assessment of different models to predict the global solar radiation on a surface tilted to the south. Solar Energy 83, 377–388. Faiman, D., Zemel, A., Zangvil, A., 1987. A method for monitoring insolation in remote regions. Solar Energy 38, 327–333. Gomez, V., Casanovas, A., Utrillas, M., Martinez-Lozano, J., 1992. Determination of Perez solar diffuse irradiance model coefficients for Valencia (Spain). In: Sayigh,

A. (Ed.), Renewable Energy, Technology and the Environment. Pergamon, pp. 2746–2750.
Gracia, A.M., Huld, T., 2013. Performance Comparison of Different Models for the Estimation of Global Irradiance on Inclined Surfaces. Technical Report EUR 26075 EN. European Commission, Joint Research Centre, Institute for Energy and Transport. Italy. Gueymard, C., 1983. Utilisation des données météorologiques horaires pour le calcul du rayonnement solaire sur des surfaces inclinées: application á la simulation thermique des bâtiments solaires passifs. Ph.D. thesis. École polytechnique (Montréal, Québec). Département de génie mécanique. Gueymard, C., 1987. An anisotropic solar irradiance model for tilted surfaces and its comparison with selected engineering algorithms. Solar Energy 38, 367–386. Gueymard, C., 1988. Erratum. Solar Energy 40, 175. Gueymard, C.A., 2009. Direct and indirect uncertainties in the prediction of tilted irradiance for solar engineering applications. Solar Energy 83, 432–444. Gueymard, C.A., Myers, D.R., 2008. Validation and ranking methodologies for solar radiation models. In: Badescu, V. (Ed.), Modeling Solar Radiation at the Earth’s Surface: Recent Advances. Springer, Berlin, Heidelberg, pp. 479–510. Gueymard, C.A., Renné, D., Vignola, F.E., 2009. Editorial: journal’s performance and publication criteria. Solar Energy 83, 1. Gueymard, C.A., Ruiz-Arias, J.A., 2016. Extensive worldwide validation and climate sensitivity analysis of direct irradiance predictions from 1-min global irradiance. Solar Energy 128, 1–30, Special issue: Progress in Solar Energy. Gulin, M., Vasak, M., Baotic, M., 2013. Estimation of the global solar irradiance on tilted surfaces. In: 17th International Conference on Electrical Drives and Power Electronics (EDPE 2013). Hay, J.E., 1979. A Study of Shortwave Radiation on Non-Horizontal Surfaces. Technical Report 0SB7800053. Atmospheric Environment Service. Downsview, Ontario. Hay, J.E., 1993. Calculating solar radiation for inclined surfaces: practical approaches. Renew. Energy 3, 373–380, Solar radiation, environment and climate change. Hay, J.E., Davies, J.A., 1980. Calculation of the solar irradiance incident on an inclined surface. In: Hay, J.E., Won, T.K. (Eds.), First Canadian Solar Radiation Data Workshop, Toronto, Ontario, Canada, pp. 59–72.

Hay, J.E., McKay, D.C., 1985. Estimating solar irradiance on inclined surfaces: a review and assessment of methodologies. Int. J. Solar Energy 3, 203–240. Hay, J.E., McKay, D.C., 1988. Final Report IEA Task IX-Calculation of Solar Irradiances for Inclined Surfaces: Verification of Models Which Use Hourly and Daily Data. Technical Report. International Energy Agency Solar Heating and Cooling Programme. Hay, J.E., Perez, R., McKay, D.C., 1986. Addendum and errata to the paper ‘‘estimating solar irradiance on inclined surfaces: a review and assessment of methodologies”. Int. J. Solar Energy 4, 321–324. Horváth, M., Csoknyai, T., 2015. Evaluation of solar energy calculation methods for 45 inclined, south facing surface. Energy Proc. 78, 465–470, 6th International Building Physics Conference, IBPC 2015. Kalisch, J., Schmidt, T., Heinemann, D., Lorenz, E., 2015. Continuous Meteorological Observations in High-Resolution (1 Hz) at University of Oldenburg in 2014. <[https://doi.pangaea.de/10.1594/PANGAEA.847830](https://doi.pangaea.de/10.1594/PANGAEA.847830)>. Kamali, A.G., Moradi, I., Khalili, A., 2006. Estimating solar radiation on tilted surfaces with various orientations: a study case in Karaj (Iran). Theor. Appl. Climatol. 84, 235–241. Kambezidis, H., Psiloglou, B., Gueymard, C., 1994. Measurements and models for total solar irradiance on inclined surface in Athens, Greece. Solar Energy 53, 177–185. Katiyar, A.K., Panday, C.K., 2010. Study of ground-reflected component and its contribution in diffuse solar radiation incident on inclined surfaces over India. Int. J. Energy Environ. 1, 547–554. Khalil, S.A., Shaffie, A., 2013a. A comparative study of total, direct and diffuse solar irradiance by using different models on horizontal and inclined surfaces for Cairo, Egypt. Renew. Sust. Energy Rev. 27, 853–863. Khalil, S.A., Shaffie, A.M., 2013b. Performance of statistical comparison models of solar energy on horizontal and inclined surface. Int. J. Energy Power 2, 8–25. Khatib, T., Mohamed, A., Mahmoud, M., Sopian, K., 2015. Optimization of the tilt angle of solar panels for Malaysia. Energy Sources, Part A: Recov. Utiliz. Environ. Effects 37, 606–613. Khatib, T., Mohamed, A., Sopian, K., 2012. A review of solar energy modeling techniques. Renew. Sust. Energy Rev. 16, 2864–2869. Khoo, Y.S., Nobre, A., Malhotra, R., Yang, D., Ruther, R., Reindl, T., Aberle, A.G., 2014. Optimal orientation and tilt angle for maximizing in-plane solar irradiation for PV applications in Singapore. IEEE J. Photovolt. 4, 647–653. Klein, S., 1977. Calculation of monthly average insolation on tilted surfaces. Solar Energy 19, 325–329. Klucher, T., 1979. Evaluation of models to predict insolation on tilted surfaces. Solar Energy 23, 111–114. Kondratyev, K., Manolova, M., 1960. The radiation balance of slopes. Solar Energy 4, 14–19. Koronakis, P.S., 1986. On the choice of the angle of tilt for south facing solar collectors in the Athens basin area. Solar Energy 36, 217–225. Lahjouji, D., Darhmaoui, H., 2013. Tilt angle optimization for maximum solar energy collection – case study for Ifrane, Morocco. In: 2013 International Renewable and Sustainable Energy Conference (IRSEC), pp. 96–101. [http://dx.doi.org/](http://dx.doi.org/)

10.1109/IRSEC.2013.6529731.
Lave, M., Kleissl, J., 2011. Optimum fixed orientations and benefits of tracking for capturing solar radiation in the continental United States. Renew. Energy 36, 1145–1152. Lee, K., Yoo, H., Levermore, G.J., 2013. Quality control and estimation hourly solar irradiation on inclined surfaces in South Korea. Renew. Energy 57, 190–199. Liu, B.Y., Jordan, R.C., 1963. The long-term average performance of flat-plate solar- energy collectors. Solar Energy 7, 53–74. Liu, B.Y.H., Jordan, R.C., 1961. Daily insolation on surfaces tilted towards the equator. ASHRAE Trans. 67, 526–541. Lonij, V.P., Brooks, A.E., Cronin, A.D., Leuthold, M., Koch, K., 2013. Intra-hour forecasts of solar power production using measurements from a network of irradiance sensors. Solar Energy 97, 58–66. Loutzenhiser, P., Manz, H., Felsmann, C., Strachan, P., Frank, T., Maxwell, G., 2007. Empirical validation of models to compute solar irradiance on inclined surfaces for building energy simulation. Solar Energy 81, 254–267. Ma, C., Iqbal, M., 1983. Statistical comparison of models for estimating solar radiation on inclined surfaces. Solar Energy 31, 313–317. Marion, B., 2015. A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance. Solar Energy 122, 1037–1046. Matagne, E., Bachtiri, R.E., 2014. Exact analytical expression of the hemispherical irradiance on a sloped plane from the Perez sky. Solar Energy 99, 267–271. Mehleri, E., Zervas, P., Sarimveis, H., Palyvos, J., Markatos, N., 2010. A new neural network model for evaluating the performance of various hourly slope irradiation models: implementation for the region of Athens. Renew. Energy 35, 1357–1362, Special Section: IST National Conference 2009. Mondol, J.D., Yohanis, Y.G., Norton, B., 2008. Solar radiation modelling for the simulation of photovoltaic systems. Renew. Energy 33, 1109–1120. Muneer, T., 1990. Solar radiation model for Europe. Build. Serv. Eng. Res. Technol. 11, 153–163. Muneer, T., Gueymard, C., Kambezidis, H., 2004. Hourly slope irradiation and illuminance. In: Solar Radiation and Daylight Models. Butterworth-Heinemann, Oxford, pp. 143–221. Muneer, T., Saluja, G., 1985. A brief review of models for computing solar radiation on inclined surfaces. Energy Convers. Manage. 25, 443–458. Muzathik, A., Ibrahim, M., Samo, K., Nik, W.W., 2011. Estimation of global solar irradiation on horizontal and inclined surfaces based on the horizontal measurements. Energy 36, 812–818.

Noorian, A.M., Moradi, I., Kamali, G.A., 2008. Evaluation of 12 models to estimate hourly diffuse irradiation on inclined surfaces. Renew. Energy 33, 1406–1412. Norris, D., 1966. Solar radiation on inclined surfaces. Solar Energy 10, 72–76. Notton, G., Cristofari, C., Poggi, P., 2006. Performance evaluation of various hourly slope irradiation models using Mediterranean experimental data of Ajaccio. Energy Convers. Manage. 47, 147–173. Notton, G., Paoli, C., Vasileva, S., Nivet, M.L., Canaletti, J.L., Cristofari, C., 2012. Estimation of hourly global solar irradiation on tilted planes from horizontal one using artificial neural networks. Energy 39, 166–179, Sustainable Energy and Environmental Protection 2010. Olmo, F., Vida, J., Foyo, I., Castro-Diez, Y., Alados-Arboledas, L., 1999. Prediction of global irradiance on inclined surfaces from horizontal global irradiance. Energy 24, 689–704. Orehounig, K., Dervishi, S., Mahdavi, A., 2014. Computational derivation of irradiance on building surfaces: an empirically-based model comparison. Renew. Energy 71, 185–192. Page, J.K., 1979. Methods for the estimation of solar energy on vertical and inclined surfaces. In: Dixon, A.E., Leslie, J.D. (Eds.), Solar Energy Conversion: An Introductory Course. Pergamon Press, pp. 37–99. Pandey, C., Katiyar, A., 2014. Hourly solar radiation on inclined surfaces. Sust. Energy Technol. Assess. 6, 86–92. Perez, R., Ineichen, P., Seals, R., Michalsky, J., Stewart, R., 1990. Modeling daylight availability and irradiance components from direct and global irradiance. Solar Energy 44, 271–289. Perez, R., Seals, R., Ineichen, P., Stewart, R., Menicucci, D., 1987. A new simplified version of the Perez diffuse irradiance model for tilted surfaces. Solar Energy 39, 221–231. Perez, R., Stewart, R., Arbogast, C., Seals, R., Scott, J., 1986. An anisotropic hourly diffuse radiation model for sloping surfaces: description, performance validation, site dependency evaluation. Solar Energy 36, 481–497. Perez, R., Stewart, R., Seals, R., Guertin, T., 1988. The Development and Verification of the Perez Diffuse Radiation Model. Technical Report SAND88-7030. Atmospheric Sciences Research Center, SUNY at Albany, Albany, NY. Posadillo, R., López Luque, R., 2009. Evaluation of the performance of three diffuse hourly irradiation models on tilted surfaces according to the utilizability concept. Energy Convers. Manage. 50, 2324–2330. Puri, V., Jimenez, R., Menzer, M., Costello, F., 1980. Total and non-isotropic diffuse insolution on tilted surfaces. Solar Energy 25, 85–90. R Core Team, 2015. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing. Vienna, Austria. <[https://www.R-project](https://www.R-project). org/>. Ramli, M.A., Twaha, S., Al-Turki, Y.A., 2015. Investigating the performance of support vector machine and artificial neural networks in predicting solar radiation on a tilted surface: Saudi Arabia case study. Energy Convers. Manage. 105, 442–452. Reindl, D., Beckman, W., Duffie, J., 1990. Evaluation of hourly tilted surface radiation models. Solar Energy 45, 9–17. Revfeim, K.J.A., 1978. A simple procedure for estimating global daily radiation on any surface. J. Appl. Meteorol. 17, 1126–1131. Ruiz, E., Soler, A., Robledo, L., 2002. Statistical assessment of a model for global illuminance on inclined surfaces from horizontal global illuminance. Energy Convers. Manage. 43, 693–708.

Skartveit, A., Olseth, J.A., 1986. Modelling slope irradiance at high latitudes. Solar Energy 36, 333–344. Souza, A.P.d., Escobedo, J.F., 2013. Estimates of hourly diffuse radiation on tilted surfaces in Southeast of Brazil. Int. J. Renew. Energy Res. 3, 207–221. Steven, M.D., 1977. Standard distributions of clear sky radiance. Quart. J. Roy. Meteorol. Soc. 103, 457–465. Steven, M.D., Unsworth, M.H., 1979. The diffuse solar irradiance of slopes under cloudless skies. Quart. J. Roy. Meteorol. Soc. 105, 593–602. Steven, M.D., Unsworth, M.H., 1980. The angular distribution and interception of diffuse solar radiation below overcast skies. Quart. J. Roy. Meteorol. Soc. 106, 57–61. Temps, R.C., Coulson, K., 1977. Solar radiation incident upon slopes of different orientations. Solar Energy 19, 179–184. Tian, Y., Davies-Colley, R., Gong, P., Thorrold, B., 2001. Estimating solar radiation on slopes of arbitrary aspect. Agric. Forest Meteorol. 109, 67–74. Torres, J., Blas, M.D., García, A., 2006. New equations for the calculation of the horizon brightness irradiance in the model of Perez. Solar Energy 80, 746–750. Utrillas, M., Martinez-Lozano, J., 1994. Performance evaluation of several versions of the Perez tilted diffuse irradiance model. Solar Energy 53, 155–162. Vasar, C., Prostean, O., Prostean, G., 2016. Evaluating solar radiation on a tilted surfaces – a study case in Timis (Romania). IOP Conference Series: Materials Science and Engineering, 106, p. 012026. Wattan, R., Janjai, S., 2016. An investigation of the performance of 14 models for estimating hourly diffuse irradiation on inclined surfaces at tropical sites. Renew. Energy 93, 667–674. Willmott, C.J., 1982. On the climatic optimization of the tilt and azimuth of flat- plate solar collectors. Solar Energy 28, 205–216. Włodarczyk, D., Nowak, H., 2009. Statistical analysis of solar radiation models onto inclined planes for climatic conditions of Lower Silesia in Poland. Arch. Civil Mech. Eng. 9, 127–144. Yadav, A.K., Chandel, S., 2013. Tilt angle optimization to maximize incident solar radiation: a review. Renew. Sust. Energy Rev. 23, 503–513. Yadav, A.K., Chandel, S., 2014. Solar radiation prediction using artificial neural network techniques: a review. Renew. Sust. Energy Rev. 33, 772–781. Yang, D., Dong, Z., Nobre, A., Khoo, Y.S., Jirutitijaroen, P., Walsh, W.M., 2013. Evaluation of transposition and decomposition models for converting global solar irradiance from tilted surface to horizontal in tropical regions. Solar Energy 97, 369–387. Yang, D., Dong, Z., Reindl, T., Jirutitijaroen, P., Walsh, W.M., 2014a. Solar irradiance forecasting using spatio-temporal empirical kriging and vector autoregressive models with parameter shrinkage. Solar Energy 103, 550–562. Yang, D., Ye, Z., Lim, L.H.I., Dong, Z., 2015. Very short term irradiance forecasting using the lasso. Solar Energy 114, 314–326. Yang, D., Ye, Z., Nobre, A.M., Du, H., Walsh, W.M., Lim, L.I., Reindl, T., 2014b. Bidirectional irradiance transposition based on the Perez model. Solar Energy 110, 768–780. Yao, W., Li, Z., Zhao, Q., Lu, Y., Lu, R., 2015. A new anisotropic diffuse radiation model. Energy Convers. Manage. 95, 304–313. Yoon, K., Yun, G., Jeon, J., Kim, K.S., 2014. Evaluation of hourly solar radiation on inclined surfaces at Seoul by photographical method. Solar Energy 100, 203–

216.
