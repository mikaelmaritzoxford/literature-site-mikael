Energy 70 (2014) 382e392

Contents lists available at ScienceDirect

# Energy

journal homepage: www.elsevier.com/locate/energy

## Estimation of direct normal irradiance from measured global and corrected diffuse horizontal irradiance

M.C. Kotti, A.A. Argiriou, A. Kazantzidis* Laboratory of Atmospheric Physics, Physics Department, University of Patras, 26500 Patras, Greece
### article info abstract

Article history: DNI (direct normal irradiance) can be calculated from global and diffuse horizontal irradiance mea- Received 19 November 2013 surements. However, the diffuse irradiance values need to be corrected because the pyranometer’s Received in revised form shadowband does not obstruct only the solar disk but also a larger part of the sky vault. In this study, 4 April 2014 we use four diffuse correction models (Drummond [1], LeBaron et al. [2], Batlles et al. [3], Muneer and Accepted 5 April 2014 Zhang [4]) and, considering the importance of DNI for several solar energy projects, we try to assess the Available online 1 May 2014 performance of the models when the calculated DNI is compared to the measured one by the pyrhe- liometer. Based on 1-min averaged measurements covering a one-year period in Athens, Greece, it is Keywords: concluded that the empirical approach of Batlles et al. performs best. It presents the lowest residuals Direct normal irradiance Diffuse horizontal irradiance ( 1%) with no dependence from the clearness index. The estimated annual DNI, derived from the synergetic use of this model with measurements of horizontal global and diffuse irradiance, is lower by Shadowband correction model

0.4%, while the calculated values from the global and uncorrected diffuse irradiances are overestimated by 7.7%.
2014 Elsevier Ltd. All rights reserved.

1. Introduction Solar irradiance reaching the earth’s surface has two compo- nents; the direct coming from the sun disc and the diffuse, as a result of scattering of the direct component from the atmospheric constituents. GHI (global horizontal irradiance), the vector sum of direct and diffuse components, is measured nowadays in many stations around the globe. Not all of these stations measure diffuse irradiance while DNI (direct normal irradiance) is measured in a limited number of stations. However, the accurate assessment of DNI reaching the earth’s surface is necessary for several applica- tions related to the design, simulation and performance assessment of several solar energy systems and plants but also passive solar buildings. DNI is very sensitive to the aerosol optical depth and is strongly affected by clouds covering the Sun. As a result, DNI ex- hibits higher spatial and temporal variability than GHI and com- plicates the accurate simulation of solar power plants or other systems requiring DNI as input. A common way to calculate DNI derives from synchronized GHI and DHI (diffuse horizontal irradiance) measurements and taking
into account the incidence angle of the sun rays using the following equation:

GHI DHI DNI ¼ (1) cosðq Þz

where q is the solar zenith angle. GHI is measured using a pyranometer on a horizontal surface. z

DHI is also measured using a pyranometer positioned horizontally on a support equipped with an adjustable device that blocks the direct component from the sensor. The most commonly used shading devices are shadowbands and shade disks, painted black in order to reduce any reflection towards the sensor. Tracking shadow disks are sometimes used to block the direct component of the sun. These devices may require a little correction [5] and can provide accurate diffuse radiation measurements; however their operation requires a relatively expensive tracking device and presents drawbacks similar to those associated with the pyrheliometer. A fixed shadowband is the most widely used technique in measuring DHI. It requires manual adjustment for Sun declination in the northesouth axis every few days and shadows the sensor constantly so that diffuse measurements are being recorded for extended periods of time. However, an inherent problem to the use of the shadowband is that at any time it screens not only the DNI but also a small portion of the DHI. Because of the anisotropy of

* Corresponding author. Tel.: þ30 2610997549; fax: þ30 2610997989. E-mail address: akaza@upatras.gr (A. Kazantzidis).
[http://dx.doi.org/10.1016/j.energy.2014.04.012](http://dx.doi.org/10.1016/j.energy.2014.04.012) 0360-5442/ 2014 Elsevier Ltd. All rights reserved.

M.C. Kotti et al. / Energy 70 (2014) 382e392
scattered irradiance, with its maximum closer to the sun, this shaded part corresponds to an essential amount of the DHI under cloud-free or partly cloudy skies. Therefore, a correction factor must be introduced to the DHI measurements to compensate for the part of the sky vault obstructed by the shadowband. In more recent studies perforated, non-rotating shadowband is used to intermittently measure both global and diffuse solar irradiance [6]. Several correction models have been proposed [1e5,7e9] to compensate for the DHI component obstructed by the shadow- band. These models were usually applied and evaluated with measurements of the site in which the model was developed. Generally these models were taking into account the geometry of the shadowband and were based on assumptions regarding the sky radiance distribution. The latter is affected significantly from the solar zenith angle, the aerosol optical properties and cloudiness [9e 14]. Use of fixed shadowbands to block the sun may result either in additional errors or in compensation errors, depending on instru- ment and shadowband correction algorithm [15]. Historically, Drummond [1] developed a theoretical model based on geometric calculations for the fraction of the sky vault obstructed by the shadowband. The proposed formula could be applied any- where in the world in order to estimate the amount of DHI blocked by a polar geometry shadowband. In order to derive his correction factor, Drummond assumed an isotropic sky radiance distribution, but after applying this geometric correction to a large amount of data in South Africa, he observed that a further correction of 7% and 3% was necessary for cloud-free and overcast skies respectively in order to take into account the anisotropic radiance distribution. Several investigators stressed the importance of applying a correction factor on diffuse irradiance measurements due to the anisotropic distribution of sky radiance. Painter [7] performed synchronized measurements of DHI by using a ring and a motor- driven occulting disc. Based on the differences between the two diffuse measurements, a correction factor, necessary to equate the ring and disk measurements under various sky conditions, was proposed. The results were found to be in good agreement with the results of Drummond. Kasten [16] developed an empirical model that used cloudiness, turbidity and declination parameters of the Sun to characterize the sky conditions. Dehne [17] observed that the attempt to transfer these functions to other sites was unsatis- factory. Steven [18], based on measurements of the diffuse-to- global irradiance ratio for characterizing the sky radiance anisot- ropy, developed a simple two-parameter model to describe the relationship between the isotropic background and the circumsolar component for several types of sky conditions. Stanhill [8] and Kudish and Ianetz [19], applied Steven’s model on data from two sites in Israel and proposed that the anisotropic sky corrections, calculated at different times of the year, were up to 30% above the Drummond’s geometric corrections. LeBaron et al. [2] suggested a model that used four parameters to describe both isotropic and anisotropic sky conditions. Each parameter was classified into four categories, thus creating a model that classified the different sky conditions into 256 unique cate- gories. Batlles et al. [3] used the same parameters as LeBaron et al. [2] in order to perform a multiple linear regression analysis. Their model consisted of four equations functions of three of the LeBaron et al. parameters. The choice of the appropriate equation for the calculation of the correction factor was determined by the range of the values of the fourth parameter. More recently, Muneer and Zhang [4] developed and validated a new model based on the work of Moon and Spencer [20] for sky radiance distribution. Comparative studies were made [21e23,25] in order to assess the performance of the diffuse correction models considering both isotropic and anisotropic conditions as proposed by LeBaron et al., Batlles et al. and Muneer and Zhang with that of Drummond, which

considers only the geometric aspect and is valid only for isotropic conditions. López et al. [21]evaluated the performance of the four correction methods using hourly data from two sites in Bracknell, UK and Beer Sheva, Israel. They found that the use of an isotropic correction factor leads to an overestimation of DHI by 4e11% and they concluded that the LeBaron and MuneereZhang models were performing better than the Drummond’s and Batlles. They also made a comparative study with the same models for Almería, Spain [22] and concluded that the use of an isotropic correction factor leads to an underestimation of the actual diffuse of 10.2%. The use of anisotropic correction schemes reduced the above underestimation to 8.7%, 2.1% and 4.9% for the LeBaron, Batlles and Muneer’s models respectively. Kudish and Evseev [23] attempted to validate the performance of the four models under different sky conditions, based on a one-year hourly data from Beer Sheva, Israel; but did not arrive to a definite conclusion regarding the overall relative pre- dictive ability of the models. However, they stated that, taking into account an overall average performance, the model of Muneere Zhang performs better than the others. They also utilized the cor- rected horizontal diffuse irradiance to assess 11 models that predict the diffuse irradiance on a south-facing surface tilted at 40 [24]. Sánchez et al. [25] used one-year hourly averages of DHI, GHI and DNI from Babajoz, South-West Spain and evaluated six correction models. After adjusting the models to the local conditions, their analysis revealed that the empirical approaches developed by LeBaron et al. and Batlles et al. performed better and showed no dependence from the solar zenith angle and the clearness index. In an ulterior study they used these models to correct ultraviolet diffuse irradiance [26]. Results revealed that some aspects of the correction proposed for total diffuse radiation are not suitable for ultraviolet diffuse radiation. The purpose of this study is to provide an estimation method of the DNI using GHI and corrected DHI data. So, going a step forward from previous works, the results do not focus only on proposing a best model for the correction of DHI due to the shadowband effect but focus also on the uncertainties of the estimated DNI from collocated GHI and DHI measurements. In contrast with previous studies and due to the high temporal variability of DNI, we used 1- min averages of synchronized measurements of DHI, DNI and GHI. We applied four models (Drummond, LeBaron, Batlles and MuneereZhang) and we studied their relative performance not only regarding the DHI component but also regarding the calcu- lated DNI under different sky conditions. Preliminary results have been published in international conference [27].

2. Data and methodology The measured data used in this study were recorded by the radiometric station of the National Observatory of Athens, Greece, during the year 2001. The station is located at the northeast of Athens on a hill of the Penteli mountain (38 N, 24 E, 500 m a.s.l). The dataset consists of 1-min averaged measurements of GHI, DHI and DNI. The GHI and DHI were measured using a CM11 pyran- ometer; the pyranometer used for the DHI measurements was shaded using a CM121 shadowband having a 620 mm diameter and a 55 mm width. The DNI was measured using a CH1 pyrheliometer, mounted on a Kipp&Zonen Solys 2 solar tracker. All instruments were new and installed for the first time in 2001 therefore their original calibration factors (provided by the manufacturer Kipp&- Zonen [28]) were used. Before calculating the DNI using Eq. (1), a quality control has been applied on all data in order to detect and remove any erro- neous values or outliers. Measurements corresponding to qz≥ 70 were removed considering that the angular inaccuracy of the pyr- anometer exceeds 2% [28].Asdefined by López et al. [21], a set of

quality control filters was also applied. Table lists the filters applied, with Ggthe GHI, Gsc¼ 1366.1 W/m² the solar constant [29], Gbthe DNI, Gdthe measured uncorrected DHI, Gdtthe “true” DHI estimated from synchronized GHI and DNI measurements as defined by López et al. [21,22] and Kudish and Evseev [23], k the diffuse fraction Gd/Ggon a horizontal surface and ktis the clearness index, defined as:

k t¼ Gg½GsccosðqzÞ (2)

The estimated DNI (Gbi) derived from GHI and corrected DHI measurements using the equation:

<u>GgGdi</u> Gbi¼ (3) cosðqzÞ

where i denotes the measured uncorrected (u),or the estimated DHI values by the Drummond (D), LeBaron (L), Batlles (B) and Muneere Zhang (M) shadowband correction models.

Table 1 provides also the remaining number of data values after

the application of each filter. The original dataset consisted of 525,600 1-min measurements, 262,812 of which were the daytime records (qz90 ); after applying the filters, 120,948 measurements remained for further processing i.e., 46% of the original diurnal database. As expected, the stricter filter was that of qz70, which removed almost 31% of the initial database. The second stricter filter was in “true” diffuse irradiance (Gdt) that takes into account errors introduced during the calculation of the “true” diffuse irra- diance from global and DNI irradiance. Negative values that occurred after calculating the DNI from GHI and DHI measurements

|N||2|
|---|---|---|
|corrected|meas||
|i i ¼ 1 N|i||
|corrected|meas||
|i i ¼ 1|i||
|1 N|corrected|meas 2|
|N i ¼ 1|i|i|
|1|N meas||
|N|i ¼ 1||
|N corrected|meas||
|i ¼ 1 i|i||
|1 N N i ¼ 1 N meas i ¼ 1|meas||

were attributed, based on the meteorological observations at the site, to rainy weather conditions when the sky was completely overcast by thick clouds. Under those conditions, GHI and DHI values were very close and negative DNI values were derived due to the measurement uncertainties of the pyranometers. This result was also confirmed by the zero DNI measurements at the same time. The estimated DNI values were analyzed under different cloud conditions and assessed both graphically and statistically. The evaluation was based on regression analysis and the statistical indices used to numerically quantify the performance of the models were the slope of the best fit line, the resulting coefficient of determination (R²), the RMSE (root mean square error), the rRMSE (relative root mean square error), the MBE (mean bias error), the rMBE (relative mean bias error), and the t-statistic index, which is computed using both the RMSE and the MBE. The statistics are defined by the following expressions [30]:

Table 2

Statistical results for the 1-min values of the direct normal irradiance calculations from correction models for all, clear, partially cloudy and cloudy sky conditions. corrected diffuse irradiance data without and with the four shadowband

2 2 2 <u>Correction models Slope R RMSE (W/m ) MBE (W/m ) t-Statistic</u> All sky conditions: N ¼ 120,816 min, Gb Meas¼ 651:73 W=m² Uncorrected 1.057 0.992 60.8 (9.3%)a50.1 (7.7%)a505.08 Drummond 1.029 0.994 39.3 (6.0%) 26.3 (4.0%) 313.32 LeBaron et al. 0.993 0.994 29.7 (4.6%) 5.0 ( 0.8%) 59.62 Batlles et al. 0.996 0.994 29.0 (4.5%) 2.7 ( 0.4%) 32.21 Muneer and Zhang 1.005 0.995 <u>28.6 (4.4%)</u> 8.3 (1.3%) 105.89 Clear sky conditions: N ¼ 97,446 min, Gb Meas¼ 760:57 W=m² Uncorrected 1.052 0.982 55.6 (7.3%)a45.5 (6.0%)a443.66 Drummond 1.026 0.983 36.2 (4.8%) 23.5 (3.1%) 266.16 LeBaron et al. 0.994 0.984 27.9 (3.6%) 5.8 ( 0.7%) 67.10 Batlles et al. 0.996 0.981 28.1 (3.7%) 3.1 ( 0.4%) 34.71 Muneer and Zhang 1.003 0.985 25.3 (3.3%) 4.4 (0.6%) 54.97 Partially cloudy sky conditions: N ¼ 18,158 min, Gb Meas¼ 245:92 W=m2 Uncorrected 1.200 0.979 86.7 (35.2%)a79.5 (32.3%)a311.24 Drummond 1.110 0.980 55.2 (22.4%) 44.3 (18.0%) 181.87 LeBaron et al. Batlles et al.

0.981
0.999
0.976
0.979
38.5 (15.7%)
35.4 (14.4%)
8.4 (
1.6 (
3.4%)
0.6%)
30.17
6.17
Muneer and Zhang 1.062 0.981 42.7 (17.3%) 27.6 (11.2%) 114.47 Cloudy sky conditions: N ¼ 5212 min, Gb Meas¼ 30:74 W=m² Uncorrected 1.629 0.887 43.8 (142.5%)a35.1 (114.1%)a96.51 Drummond 1.336 0.907 27.2 (88.5%) 16.8 (54.5%) 56.51 LeBaron et al. Batlles et al.

1.286
1.089
0.896
0.917
28.5 (92.0%)
18.3 (59.6%)
22.3 (72.5%)
1.7 (5.6%)
90.11
6.88
Muneer and Zhang 1.293 0.907 25.4 (82.7%) 15.0 (48.8%) 52.76 aRMSE and MBE as percentage of G. b Meas

vffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi u u X RMSE ¼ t <u>1</u> x x (4) N

X MBE ¼ <u>1</u> x x (5) N

rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi P x x rRMSE ¼ P (4a) xi

<u>1</u> P x x rMBE ¼ N P (5a) xi

P where ð1=NÞ xi is the mean value of the measured DNI

Table 1

Quality control filters of solar irradiance.

|Irradiance|Filter|1-min values removed|Remaining 1-min values|
|---|---|---|---|
|All (q z 90 )|q z 70|82,362 (31.3%)|180,450|
|Global|0<G g < 1.2G sc 0 < k t < 1|0 (0%) 417 (0.16%)|180,450 180,033|
|Measured diffuse|0<G d < 0.8G sc G d < G g 0 < k < 1|0 (0%) 38 (0.01%) 0 (0%)|180,033 179,995 179,995|
|Direct normal|0<G b < G sc|7 (0%)|179,988|
|“True” diffuse Negative values of corrected DNI|0<G dt < 0.8G sc 0.6G dt < G d < G dt|11 (0%) 26,660 (10.14%) 29,402 (19.1%)|179,977 153,317 123,915|
|Operational errors||||
|Disconnected instruments||3099 (2.50%)|120,816|

sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi <u>ðN 1ÞMBE²</u> t ¼ 2 2

(6)
RMSE MBE

The results are summarized in Table 2. The sky conditions were defined according to clearness index kt [23]:

Cloudy 0 kt< 0:35 (7a)

Partially cloudy 0:35 kt0:65 (7b)

Clear sky kt> 0:65 (7c)

In existing literature analysis of solar radiation data is mainly based on hourly irradiance data therefore the analysis was also performed on hourly-averaged values of the same dataset.

3. Description of the shadowband correction models All models provide a correction factor, Ci, which is applied along with the measured DHI (Gd) data in order to calculate the corrected DHI (Gdi) using the formula: Gdi¼ CiGd(8) In this study, we present the following four models named after the name of the first author of the paper who introduced them:
3.1. The Drummond model Drummond was one of the pioneers in proposing shadowband correction methods. He used global and diffuse irradiance data from nine stations located at Pretoria, South Africa, an area much of which lies in the relatively cloud-free anticyclonic belt of the Southern Hemisphere. Drummond’s model [1], is thus based on an assumption that the diffuse radiation is isotropically distributed over the sky hemisphere. Due to this assumed diffuse radiation’s isotropy, the correction factor can be estimated from the shadow- band geometrical features of pyranometer. The factor correcting the irradiance intercepted by the shad- owband was calculated by comparing the sky irradiance measured using the shadowband against the sky irradiance measured by replacing the shadowband with a 10 cm diameter disk placed 1 m above the sensor. The comparisons were limited to cloudless skies. The fraction of the diffuse horizontal irradiance obstructed by the shadowband (X) is given by [21,23]: X ¼ 2b cos³ðdÞtosinð4ÞsinðdÞþcosð4ÞcosðdÞsinðtoÞ=ðprÞ (9) with b the width and r the radius of the shadowband and t o¼ cos 1 ½tanð4ÞtanðdÞ (10) the hour angle at the sunset (qz¼ 90 ) in radians, 4 the latitude of the location and d the solar declination. The Drummond isotropic correction factor is then expressed as CD¼ 1=ð1 XÞ (11) Drummond also compared the diffuse irradiance measured us- ing a shadowband against the total irradiance for completely overcast skies and concluded [31] that a further correction of 7%, 5% and 3% for cloud-free, partly cloudy and overcast skies respectively was necessary in order to take into account the anisotropic distri- bution of solar irradiance.
3.2. The LeBaron model The distribution of scattered solar irradiance changes markedly with sun’s elevation, atmospheric turbidity and cloudiness. Isotropic conditions are a satisfactory approach only for overcast skies. Based on two years of hourly data of global, diffuse horizontal and direct normal irradiance from Albany, New York, and Bluefield, West Virginia in order to include some variation in climatic con- ditions and latitude separation, LeBaron et al. [2] examined the anisotropic contribution to the total shadowband correction for seven different levels of sky cloudiness. They proposed a correction model that uses four parameters describing both isotropic (geo- metric) and anisotropic (sky conditions) effects. The first param- eter, the geometric screening, is the Drummond’s correction factor, C D, while the other three parameters, solar zenith angle qz, epsilon ε and delta D describe the anisotropic contribution to the final shadowband correction. Epsilon, the clearness index is defined as: ε ¼ðGduþ GbcÞ=Gdu(12) with Gduthe uncorrected measured DHI and Gbcthe DNI calculated from global and diffuse radiation measurements on a horizontal surface. Delta is the brightness index and is a function of the cloud thickness or aerosol loading. It is defined as: D¼G =ðGoncosðqzÞÞ (13) du where Gonis the extraterrestrial solar irradiance measured on a plane normal to the radiation and is calculated from the equation:
~~ <u>360n</u> Gon¼ Gsc1 þ 0:033 cos 365 (14)

where n is the day of the year (1e365). LeBaron’s model was developed by classifying each of the pa- rameters, qz, CD, ε, D, into four categories (i, j, k, l) thus creating a model of 256 categories in total; the LeBaron correction factor, CL,is looked up from a table [2].

3.3. The Batlles model Batlles et al. [3] developed two different correction models based on the same parameters as the LeBaron model. Using two- thirds of hourly data from Madrid, Spain, covering a two-year period and the other one-third plus 5-min data from Almería, Spain for validation purposes, resulted to two parameterizations, a simpler one, model A, and a more complex, model B. It appeared that model B was more universal than model A. The Batlles model B is based on the same parameters as the LeB- aron model. However, the proposed correction factor (CB) is param- eterized against ε and is expressed as an analytical function of CD, qz and D. The model is described by the following set of equations:
cosðqz Þ <u>1</u> ε 3:5/CB¼ 1:178CDþ 0:0207 logðDÞþ0:422e <u>1</u> 3:5 ε 8/CB¼ 1:454CDþ 0:655 logðDÞþ0:4756ecosðqz Þ

8 ε 11/CB¼ 1:486CDþ 0:495 logðDÞ

ε > 11/CB¼ 1:384CDþ 0:363 logðDÞ (15)

C Bdepends on the solar zenith angle (qz) in the two first equa- tions corresponding to scattered and overcast sky conditions. When there are few or no clouds at all (that is for higher ε values), CBis practically independent from qz.

Fig. 1. Calculated values of direct normal irradiance, for all sky conditions, using uncorrected diffuse irradiance measurements (a), Drummond (b), LeBaron (c), Batlles (e) and

MuneereZhang (d) shadowband correction models versus measurements.

3.4. MuneereZhang model of global horizontal, direct normal and diffuse irradiance
measured using a shadowband. The clearness index, kt, was used This anisotropic model is based on the use of a single diffuse irradiance distribution index, b, introduced after the work of Moon and Spencer [20]. As a follow up of Muneer’s previous work [32], the proposed model [4] was validated using two datasets from sites with completely different sky conditions, Bracknell, UK and Beer Sheva, Israel and compared to the

as a parameter to determine the value of b; b was then used to obtain a correction factor to account for the diffuse irradiance obscured by the shadowband. Muneer [4,21] derived a relation- ship between b and ktpresented in Eqs. (16) and (17). Parameters b₁ and b₂ represent the irradiance distribution indices for the two sky quadrants, the one containing the sun disk and the opposite Drummond’s model. The data consisted of one year hourly values to it

Fig. 2. Same as Fig. 1 but for clear sky conditions.

<u>1</u> 3:6 10:462kt1:565 þ 0:990ktCM¼ (18)

|k > 0:2/b₁|; b₂|(16)||1||
|---|---|---|---|---|---|
|t|t|t||IF||
||||||d|
|||||z||
|t|||d|||
|t||||z|2 1|
||M|||||

t¼ ¼IF d 0:4 þ 6:974kt0:957 0:660kt The parameter I is defined as: and ~ ~ <u>pL 3 þ 2b₁ 3 þ 2b₂</u> I ¼ þ (19) k 0:2/b₁ ¼ b₂ ¼ 1:68 (17) 1 þ b₁ 1 þ b₂

with k, the clearness index, as defined in Eq. (2). where L (W m sr) is the zenith radiance. The correction factor, C, is given by the expression: The parameter F is defined as:

Fig. 3. Same as Fig. 1 but for partly cloudy sky conditions.

≥ 3<u>I₁ þ b I1 2</u>

|2|2||
|---|---|---|
|o||o|
|2|2 o|o|

F ¼ 2wLzcos ðdÞ (20) I₂ ¼ t sin ð4Þsin ðdÞþ2 sinðt Þsinð4Þcosð4ÞsinðdÞcosðdÞ 1 þ b₁ ≥ þ cos ð4Þcos ðdÞ <u>t</u> sinð2t Þ with w the view angle of the shadowband subtended at the diffuse 2 þ irradiance sensor, d is the Sun’s declination and I₁ and I₂ are (22) calculated by:

I₁ ¼ cosð4ÞcosðdÞsinðtoÞþtosinð4ÞsinðdÞ (21) The hour angle at the sunset (t o ) is given from Eq. (10).

4. Results and discussion
higher than the measured values. For higher DNI values, corre- sponding to measurements under cloud-free skies and lower solar The calculated DNI values were validated against measurements zenith angles, there is a smaller dispersion of the points and they by graphical and statistical means under different sky conditions. tend to be closer to the y ¼ x line. However, for lower measured Based on the sky conditions defined by Eqs. (7aec), the clear sky DNIs, the dispersion of uncorrected DNI values is higher and the conditions cover 80.7% of the dataset, while the cloudy and partly overestimation is significant. It is also noticeable that all diffuse cloudy conditions correspond to 15.0% and 4.3% respectively. The corrections models improve the estimation of DNI. The improve- uncorrected and calculated DNI values (by the four models) are ment is slight when the Drummond model is applied and the DNI is presented as a function of the measured DNI for all sky conditions still overestimated. However, when the LeBaron, the Batlles and the in Figs. 1e4. In the vast majority of cases, the uncorrected DNI is MuneereZhang models are used, the improvement is much more

Fig. 4. Same as Fig. 1 but for cloudy conditions.

evident. Scattering in the model-to-measurement comparison graphs remains high for cloudy conditions for all models. The statistical analysis of the results is presented in Table 2. The average value of the measured DNI and the number of values (or minutes) that correspond to each condition are provided. The slopes corresponding to the LeBaron, the Batlles and the Muneere Zhang models are closer to unity for all sky and clear sky conditions. For partially cloudy and cloudy conditions all slopes increase significantly with the exception of that of the Batlles model that remains close to unity. LeBaron’s slope value is close to unity for all sky and clear sky conditions, decreases for partially cloudy condi- tions and increases for overcast skies. For the Drummond model, slopes up to 1.029 are obtained for all and clear sky conditions. However, the slope values increase to 1.110 for partially cloudy sky conditions and to 1.336 for cloudy conditions. Despite the high slope values, the Drummond model still improves the results when compared with the uncorrected estimates of DNI. For cloudy con- ditions, when the DNI values are too low, the best slope (1.089) is obtained using the Batlles model. In this case, the coefficient of determination (R²) is lower than 0.92 for all models. The root mean square error (RMSE) of all models is reduced when compared with the uncorrected DNI values. The reduction is higher for all sky and clear sky conditions for the Muneere Zhang model, where the RMSE is of about 50% lower compared to the respective values of the uncorrected DNI, followed by the Batlles and the LeBaron models. For partially cloudy and cloudy conditions the Batlles model has the smallest RMSE values reducing the dispersion up to almost 60%. High values for rRMSE for cloudy conditions reveal a significant variability and derive from the fact that 1-min averaged data were used. The mean bias error (MBE) values reveal that the Batlles model performs better for all types of sky conditions. The LeBaron model shows the same performance for all cases except for cloudy conditions. Under cloudy skies (when isotropy prevails) the MuneereZhang model and the Drummond model perform better than the LeB- aron model, where MBE value for the MuneereZhang model is only 11% better than that of the Drummond model. MBE values show a slight underestimation of the measured DNI using the LeBaron and the Batlles models and an overestimation using the Drummond and the MuneereZhang models. For overcast skies all models overestimate the measured DNI. t-statistic compares the various models and takes into account the dispersion of the re- sults which is not accounted for when the root mean square error and mean bias error are considered separately. The smaller the value of t, the better the model performs. According to the t- statistic results, the Batlles model performs the best in all cases, followed by the LeBaron model for all sky and partially cloudy conditions and by the MuneereZhang model for clear sky and cloudy conditions. An additional analysis is performed by comparing the model residuals as a function of the clearness index kt(Fig. 5). The re- siduals (calculated minus measured DNI values) are expressed as a percentage of the average value of the measured DNI. The residuals for the uncorrected DNI are always positive and become maximum (13.8%) under partially cloudy conditions. The residuals of the estimated DNI after applying the Drummond and the Muneere Zhang models present almost the same behavior; the residuals after applying the Drummond model are about 4% and 0% for cloud- free and cloudy skies respectively but increase for partially cloudy conditions. For the MuneereZhang model the residuals reach 0% for clear and overcast skies. When applying the LeBaron model, the DNI residuals are lower than those of the previous models but in- crease significantly (up to 4%) for kt< 0.5. The lowest residuals ( 1%), that are also independent from kt, are obtained using the Batlles model.

Fig. G

5.) as a function of the clearness index The residuals of all models (expressed
k. as a percentage of the mean value of bMeas t

The distribution of monthly sums of DNI values for the specific site is presented in Fig. 6. As seen from the second (red (in the web version)) bars, the calculated DNI values (from GHI and DHI mea- surements) exceed the measured ones (black colored bars). The differences in the calculated monthly irradiance values vary from

9.7 MJ/m² in December to 48 MJ/m² in May. When the diffuse irradiance is corrected with the LeBaron, the Batlles and the MuneereZhang models, the amount of calculated direct irradiance approaches the measured one for each month and the differences do not exceed 12 MJ/m², 8.5 MJ/m² and 8.3 MJ/m² respectively. The absolute and percent (%) differences between the calculated and measured values of the annually integrated DNI are presented in Fig. 7. The annual DNI is overestimated by 7.7% (363 MJ/m²) when calculated from the global and diffuse measurements. The calcu- lated DNI using the Drummond and the MuneereZhang models is also higher by 4.0% and 1.3% respectively (190.8 MJ/m² and 60.5 MJ/ m²) than the measured DNI. However, the calculated DNI using the LeBaron and the Batlles models is slightly lower ( 0.8% and 0.4% respectively) than the measured one. The corresponding absolute differences are 36.4 MJ/m² and 19.4 MJ/m².
Fig. 6. The distribution of monthly direct normal irradiance using measured, uncor-
 rected and model corrected data.

between and

|Fig. 7. The|absolute|and percentage|(%) differences|the calculated|
|---|---|---|---|---|
|measured values of the annually integrated direct normal irradiance.|||||

In many cases [21e26], diffuse correction factors are applied to hourly averaged irradiance data. In order to explore the effect of data averaging on our conclusions, 2178 values of hourly-averaged data were produced for the year 2001 after having been filtered (see

Table 1). Then the correction factors were applied to the hourly-

averaged data and revealed a similar statistical behavior, shown in Table 3.The Batlles model performs best for all sky types, clear sky and partially cloudy conditions. For cloudy conditions the LeBaron model performs better followed by the MuneereZhang model but the sample was very small to draw unambiguous con- clusions. Estimation of integrated annual energy differences be- tween the calculated and measured hourly-averaged DNI had the same performance as in Fig. 7 with the percentage differences being 8.1%, 4.1%, 1.1, 0.7% and 1.4% for the uncorrected, Drum- mond, LeBaron, Batlles and MuneereZhang models respectively.

5. Conclusions The DHI measured by a pyranometer with an adjusted shad- owband must be, a priori, corrected for the obscured portion of the sky. In this study, we use 1-min averaged measurements of GHI, DNI and four widely used models for correcting the DHI measured using a shadowband in Athens, Greece. The accuracy of this correction is important since the subsequent calculation of DNI is affected. The novelty of this study is that, considering the impor- tance of DNI for several solar energy applications, we try to assess the performance of the four diffuse correction models by comparing the calculated DNI with simultaneous pyrheliometer measurements, aiming to the more accurate estimation of DNI at stations where GHI and DHI are measured simultaneously. The data were divided according to the clearness index ktvalue in three sky conditions: clear, partially cloudy and cloudy. The diffuse correction models were applied to the complete dataset and also to the datasets corresponding to the above three sky condi- tions. It was found that the estimated DNI values using the DHI corrected by the Batlles model are closer to the pyrheliometer measurements. The Drummond’s purely geometric factor corrects less the DHI and consequently the derived DNI. The MuneereZhang model that corrects Drummond’s factor considering the clearness index and the irradiance distribution [4] has similar behavior to that of the Drummond model but has a clearly better performance and overestimates the energy calculated using the DNI values by
1.3% annually. The LeBaron model has similar performance to that of Batlles model underestimating the annual energy calculated by the DNI by 0.8%. When the monthly diffuse irradiance is corrected with the Batlles model, the annual energy calculated by the DNI is slightly underestimated only by 0.4%. The lowest residuals ( 1%), with no dependence from kt, are obtained using the Batlles model. Acknowledgments The study was conducted in the frame of project “Hellenic Network of Solar Energy” (HNSE, 09SYN-32-778), and funded by the General Secretariat for Research and Technology, Greek Min- istry of Education, Lifelong Learning and Religious Affairs. The authors would like to thank the Institute of Environmental

|shadowband|models|for all, clear,|cloudy and|cloudy sky|||||||
|---|---|---|---|---|---|---|---|---|---|---|
|conditions.|||||||||||
|Correction models|Slope R²|RMSE (W/m )|MBE (W/m )|t-Statistic|||||||
|All sky conditions: N ¼ 2178 hourly averages, G|||¼ 607:93 W=m²||||||||
|Uncorrected|1.059 0.996|57.8 (9.5%)|49.4 (8.1%)|76.77|||||||
|Drummond|1.030 0.998|35.7 (5.9%)|24.9 (4.1%)|45.59|[1] Drummond AJ. On measurements of sky radiation. Arch Meteorol Geophys||||||
|LeBaron et al.|0.994 0.998|26.9 (4.4%)|7.0 (1.2%)|12.72|Bioklimatol 1956;B7:413e36.||||||
|Batlles et al.|0.997 0.998|25.7 (4.2%)|4.2 (0.7%)|7.85|[2] LeBaron BA, Michalsky JJ, Perez R. A simple procedure for correcting shadow||||||
|Muneer and Zhang|1.007 0.999|24.9 (4.1%)|8.5 (1.4%)|17.01|band data for all sky conditions. Sol Energy 1990;44:249e56.||||||
|Clear sky conditions: N ¼ 1590 hourly averages, G|||¼ 742:57 W=m||[3] Batlles FJ, Olmo FJ, Alados-Arboledas L. On shadowband correction methods||||||
|Uncorrected|1.052 0.998|52.6 (7.1%)|44.3 (6.0%)|62.24|for diffuse irradiance measurements. Sol Energy 1995;54:105e14.||||||
|Drummond|1.026 0.999|33.9 (4.6%)|22.8 (3.1%)|36.33|[4] Muneer T, Zhang X. A new method for correcting shadow band diffuse irra-||||||
|LeBaron et al.|0.996 0.999|24.4 (3.3%)|3.9 (0.5%)|6.52|diance data. J Sol Energy Eng 2002;124:34e43.||||||
|Batlles et al.|0.998 0.999|24.7 (3.3%)|1.7 (0.2%)|2.74|[5] Ineichen P, Gremaud JM, Guisan O, Mernoud A. Study of the corrective factor||||||
|Muneer and Zhang|1.006 0.999|23.4 (3.2%)|5.8 (0.8%)|10.26|involved when measuring the diffuse solar radiation by the use of the ring||||||
|Partially cloudy sky conditions: N ¼ 523 hourly averages, G||||¼ 267:15 W=m|method. Sol Energy 1984;32:585e90.||||||
|Uncorrected|1.178 0.983|73.1 (27.4%)|63.3 (25.2%)|53.66|[6] Brooks MJ. Performance characteristics of a perforated shadow band under clear sky conditions. Sol Energy 2010;84:2179e94.||||||
|Drummond|1.088 0.991|42.1 (15.7%)|33.4 (12.5%)|29.75|[7] Painter HE. The shade ring correction for diffuse irradiance measurements. Sol||||||
|LeBaron et al.|0.959 0.989|33.9 (12.7%)|18.1 (6.8%)|14.40|Energy 1981;26(4):361e3.||||||
|Batlles et al.|0.979 0.991|29.1 (10.9%)|10.9 (4.1%)|9.29|[8] Stanhill G. Observations of shade-ring corrections for diffuse sky radiation||||||
|Muneer and Zhang|1.042 0.993|29.7 (11.1%)|17.0 (6.4%)|15.95|measurements at the dead sea. Q J R Meteorol Soc 1984;111(70):1125e30.||||||
|Cloudy sky conditions: N ¼ 65 hourly averages, G|||¼ 56:24 W=m||[http://dx.doi.org/10.1256/smsqj.47012.||||||](http://dx.doi.org/10.1256/smsqj.47012.||||||)
|Uncorrected|1.415 0.953|35.9 (63.9%)|31.5 (56.0%)|14.59|[9] LeBaron|BA, Peterson|WA, Dirmhrin|I. Corrections|for diffuse|irradiance|
|Drummond|1.128 0.965|17.3 (30.7%)|9.3 (16.6%)|5.12|measured|with shadowbands.|Sol Energy|1980;25:1e13.|[http://dx.doi.org/||](http://dx.doi.org/||)
|LeBaron et al.|1.001 0.931|18.7 (33.2%)|4.1 (7.2%)|1.79|10.1016/0038-092X(80)90401-6.||||||
|Batlles et al.|0.845 0.918|20.4 (36.3%)|13.0 (23.1%)|6.63|[10] Harrison|AW, Coombes|CA. An opaque|cloud cover|model of|sky short|
|Muneer and Zhang|1.08 0.962|15.7 (28.0%)|6.2 (11.0%)|3.41|wavelength radiance. Sol Energy 1988;41:387e92. [11] Brugner AP, Hooper FC. An anisotropic sky radiance model based on narrow||||||
|RMSE and MBE as percentage of G||.|||field of view measurements of shortwave radiance. Sol Energy 1993;51:53e||||||
||||||64.||||||
 Research and Sustainable Development of the National Observatory of Athens for providing the solar radiation data used in this study. References
Table 3

Statistical results for the hourly-averaged values of the direct normal irradiance calculations from global and diffuse irradiance data with and without the four shadowband correction models for all, clear, partially cloudy and cloudy sky

2 2

b Meas a a

b Meas 2 a a

b Meas 2 a a

2 ab Meas a

a b Meas

[12] Igawa N, Koga Y, Matsuzawa T, Nakamura H. Models of sky radiance distri- bution and sky luminance distribution. Sol Energy 2004;77:137e57. [13] Li ZQ, Goloub P, Devaux C, Gu XF, Dueze JL, Qiao YL, Zhao FS. Retrieval of aerosol optical and physical properties from ground-based spectral, multi- angular, and polarized sun-photometer measurements. Remote Sens Envi- ron 2006;101:519e33. [14] Kocifaj M. Angular distribution of scattered radiation under broken cloud arrays: an approximation of successive orders of scattering. Sol Energy 2012;86(12):3575e86. [15] Gueymard CA, Myers DR. Evaluation of conventional and high-performance routine solar radiation measurements for improved solar resource, climato- logical trends, and radiative modeling. Sol Energy 2008;83:171e85. [16] Kasten MD. Improvement of measurements of diffuse solar radiationIn Solar radiation data, series F. 2nd ed. Dordrecht: D. Reidel; 1983. [17] Dehne K. Diffuse solar radiation measured by the shade ring method improved by a correction formula, 1984, Papers Presented at the WMO Technical Conference on Instruments and Cost-effective Meteorological Observations (TECIMO), Instruments and Observing Methods Report No. 15, Geneva, pp. 263d267. [18] Steven MD. The anisotropy of the diffuse solar radiation determined from shade-ring measurements. Q J R Meteorol Soc 1984;110:261e70. http:// dx.doi.org/10.1002/qj.49711046317. [19] Kudish AI, Ianetz A. Analysis of diffuse radiation data for Beer Sheva: measured (shadow ring) versus calculated (global-horizontal beam) values. Sol Energy 1993;51:495e503. [20] Moon P, Spencer DE. Illumination from a non-uniform sky. Trans Illum Eng Soc 1942;37:707e25. [21] López G, Muneer T, Claywell R. Assessment of four shadow band correction models using beam normal irradiance data from the United Kingdom and Israel. Energy Convers Manag 2004;45:1963e79.

[22] López G, Muneer T, Claywell R. Comparative study of four shadow band diffuse irradiance correction algorithms for Almería, Spain. J Sol Energy Eng 2004;126(2):696e701. [http://dx.doi.org/10.1115/1.1666895](http://dx.doi.org/10.1115/1.1666895). [23] Kudish AI, Evseev EG. The assessment of four different correction models applied to the diffuse radiation measurements with a shadow ring using global and normal beam radiation measurements for Beer Sheva, Israel. Sol Energy 2008;82:144e56. [24] Evseev EG, Kudish AI. The assessment of different models to predict the global solar radiation on a surface tilted to the south. Sol Energy 2009;83:377e88. [25] Sánchez G, Serrano A, Cancillo ML, Garcia JA. Comparison of shadow-ring correction models for diffuse solar irradiance. J Geophys Res 2012;117: D09206. [http://dx.doi.org/10.1029/2011JD017346](http://dx.doi.org/10.1029/2011JD017346). [26] Sánchez G, Serrano A, Cancillo ML. Shadow-band correction for diffuse ul- traviolet radiation measurements. J Geophys Res D Atmos 2013;118(9):3807e

16.
[27] Kotti MC, Argiriou AA. Use of shadowband correction models for predicting beam solar irradiance. Adv Meteorol Climatol Atmos Phys Springer Atmos Sci; 2013:1069e74. [28] Kipp and Zonen. CM11 pyranometer and CM14 albedometer instruction manual; 2000. [29] Gueymard CA. The sun’s total and spectral irradiance for solar energy appli- cations and solar radiation models. Sol Energy 2004;76(4):423e53. [30] Stone RJ. Improved statistical procedure for the elevation of solar-radiation estimation models. Sol Energy 1993;51:281e91. [31] Drummond AJ. Comments on “Sky radiation measurement and corrections”. J Appl Meteorol 1964;3:810e1. [32] Muneer T. Solar radiation model for Europe. Build Serv Eng Res Technol 1990;11(4):153e63.
