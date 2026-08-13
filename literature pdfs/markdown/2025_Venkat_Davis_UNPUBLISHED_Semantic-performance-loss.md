# Semantic Performance Loss Analysis of Photovoltaic Modules Under Stress: A

# Multimodal, Data-Driven Approach

|1,2|1,2|2,3|
|---|---|---|
|3|3 1,2,3,4|4,5|

Sameera Nalin Venkat, Joseph Raby, Brent A. Thompson, Max A. Liggett 1*,*2, Dylan J. Colvin, Hubert P. Seigneur, Roger H. French, Kristopher O. Davis

1. Department of Materials Science and Engineering, University of Central Florida,
Orlando, Florida, U.S.A.

2. Resilient, Intelligent and Sustainable Energy Systems (RISES) Research Center,
University of Central Florida, Orlando, Florida, U.S.A.

3. Florida Solar Energy Center (FSEC), University of Central Florida, Cocoa,
Florida, U.S.A.

4. Department of Materials Science and Engineering, Case Western Reserve
University, Cleveland, Ohio, U.S.A.

5. Solar Durability and Lifetime Extension (SDLE) Research Center, Case Western
Reserve University, Cleveland, Ohio, U.S.A.

6. CREOL, the College of Optics and Photonics, University of Central Florida,
Orlando, Florida, U.S.A.

Corresponding Author Email Address:kristopher.davis@ucf.edu

Keywords: photovoltaics; modules; accelerated aging; durability; deep learning

Abstract:

## 1 Introduction

The economic value of photovoltaic (PV) systems is derived from the produc- tion of energy from these systems over a long period of time [1], typically over 25 years. These systems have a high upfront capital cost but then produce energy over time with no fuel costs and very little operations and mainte- nance costs under normal circumstances. PV module warranties in the range of 20-30 years are a common means of guaranteeing high production (*>*80% nameplate) over an extended period. These warranties are often expressed in terms of an expected maximum power output (*PM P*) under standard test con- ditions (STC) after a certain number of years. This is related to the power loss rate (*rP LR*) or degradation rate (*rd*) of the modules, often expressed as the percentage of power lost over time in units of % per year. A combina- tion of accelerated testing and field testing are used to evaluate how likely the modules will last. When degradation is higher than expected, manufacturers and researchers try to understand the source or root cause of the problem and develop appropriate solutions. Various measurement and analysis methods can be used to quantify power loss and better understand the reasons behind it, but in nearly all cases, illumi- nated current-voltage (*I − V*) and electroluminescence (EL) imaging is carried

out. These are arguably the two most common measurements used to eval- uate the reliability and durability of PV modules. Table1displays a survey of 16 research articles from 2020 to 2025 focused on PV module reliability and durability based on *I−V* and EL data. This survey covers a range of industrially-relevant PV cell technologies, exposure conditions (*e.g.*, acceler- ated aging, field exposure), and environmental stressors. From this survey, we see this is an area that needs to be explored. The methods of featurization and analysis of the *I−V* curves and EL images can be varied. In the simplest cases, this may mean simply extract- ing *PM P*as a means of quantifying power loss, and then visually inspecting the EL images for non-uniformities or anomalous patterns in the images. Ide- ally, some semantic meaning could be assigned to these observations in an objective and automated manner, which would accelerate cycles of learning in reliability and durability studies. Techniques like curve fitting can be used to extract features from *I−V* curves using both physical models (*e.g.*, Shock- ley diode equation, semiconductor device physics) and data-driven models. This provides PV researchers with meaningful insights into the underlying loss mechanisms causing performance loss (*e.g.*, optical, recombination, resis- tive, carrier-selectivity). This mechanistic understanding can facilitate better materials selection and design choices in an empirical and data-driven manner. Featurization of EL images is less common in practice. In many of the research articles featured in Table1and in the literature more generally, *I − V* features (*e.g.*, *PM P*) are reported in a quantitative and reproducible manner, whereas EL images are often presented as anecdotal evidence confirming or disputing a potential root cause. Progress has been made on EL image fea- turization using statistical, machine, and deep learning methods to analyze images and provide semantic meaning behind observed patterns. Supervised deep learning methods like semantic segmentation are particularly useful for this task [2–14], because they provide both a means of quantitatively ana- lyzing image features and qualitatively assigning meaningful names for these features, like those outlined in available test standards [15]. This work extends further into the realm of semantic performance loss analysis by using semantic defect segmentation of EL images, *I−V* features, and network structural equation modeling into a single framework. Here, a new semantic model for tracking the evolution of defects in PV modules is proposed with three differentiated metrics: durability, stability, and resilience. Together, these metrics can be used to more completely characterize the overall durability and reliability of PV modules in the face of individual or combined stressors. The three metrics are defined as follows:

1. Durability-The extent to which a PV module continues to operate at its original performance level as a function of stressor, time under stress, or time in field operation. This is a classic metric that only requires *I − V* features at each point. It can be represented by the following equation, where: *t* is the duration of time the modules is exposed to, or exposure steps, exposure cycles, or some other dose of the stressor (*e.g.*, force, flux,

bias); *P* (*t*) is the module *PM P*at each point in time; and *Pi*is initial *PM P*before the exposure sequence begins.

<u>P (t)</u> *vs. t* (1) *Pi*

2. Stability-The extent to which a PV module resists the formation and/or growth of a defect(s) as a function of *t*. This cannot be determined with *I−V* features alone, but instead requires some technique that can both classify this defect with a semantic label and track its evolution (*e.g.*, EL imaging with semantic segmentation) at each point. In the case of semantic segmentation of EL images, the following equation can be used to represent stability, where: *f*
*d*

(*t*) is the fractional area of the EL image
featuring this defect; and *fid*represents this same fraction defect area before the exposure sequence begins. Note, in this work, we focus on tracking the evolution of a single *f* *d* (*i.e.*, fractured area), but multiple defects could actually be monitored independently (*e.g.*, *f* *d* 1, *f* *d* 2, *f* *d* 3 ).

<u>f</u> *d*

<u>(t)</u>
1 *−* *d* *vs. t* (2) *f* *i*

3. Resilience-The extent to which a PV module maintains its original performance level as the defect grows. This requires both the *I −V* features (*i.e.*, *P*) and the independently monitored defect (*i.e.*, *f*
*d* ).

<u>P (t) f</u> *d*

<u>(t)</u>
*vs.* (3) *Pif* *id* To implement this framework, fifty PV c-Si modules were evaluated via *in* *situ I − V* and EL imaging performed under mechanical loading, as reported in prior work [16–19]. At fixed time intervals, the externally applied mechanical pressure, *p* *ext*, is increased and both *I −V* curves and EL images obtained. Cells within the module begin to fracture as the applied mechanical force increases, as observed in EL images. The *I−V* curves provide *P* of the module, and in this case, *P* (*t*) corresponds to *P* (*p* *ext* ). Semantic segmentation is used to determine the fractional area of fractured cells within the measured module, thus providing *f* *d*, or *f* *crack* to be more precise. The *f* *crack* at each pressure is obtained, *f* *crack* (*p* *ext* ), thereby allowing the quantitative durability, stability, and resilience metrics, as defined above, are determined and reported.

Table 1: Survey of recent studies on PV module reliability and durability from

2020–2025, utilizing *I*–*V* measurements and EL imaging. Abbreviations: exposure (exp.); potential induced degradation (PID); monocrystalline silicon (mono); Al back surface field (Al-BSF); accelerated (acc.); damp heat (DH); high voltage (HV); glass/backsheet (G/B); glass/glass (G/G); unencapsulation (unencap.); degradation (degr.); thermal cycling (TC); silicon heterojunction (SHJ).

|Year|PV Cell Tech.|PV Module|Exposure|Key Observations||
|---|---|---|---|---|---|
|[Ref.]||Design|Type|||
|2020 [20]|Varied|Varied|Field exp.|PID, interconnect problems, and contact corrosion||
|2020 [21]|Mono Al-BSF|One-cell, G/B and G/G|Acc. DH|Contact corrosion near interconnects||
|2020 [22]|Mono Al-BSF|One-cell, G/B|Acc. DH|Contact corrosion||
|2020 [23]|Mono Al-BSF with Cu grid|One-cell, G/B|Acc. DH|Higher degree of degr. in Cu vs. Ag contacts||
|2020 [24]|Varied|Four-cell, G/B|Acc. DH|Contact corrosion||
|2021 [25]|Varied|-|Field exp.|Corrosion, delamination, & discoloration||
|2021 [26]|Multi PERC|Varied|Light, heat|Varied degradation response based on manufacturer||
|2022 [27]|Mono PERC|One-cell, G/B|Acc. DH|Contact corrosion & discoloration||
|2022 [28]|Mono PERC|144 half-cell,|Acc. DH|Contact corrosion||
||& Multi Al-BSF|G/B||||
|2022 [29]|Multi Al-BSF|60-cell, G/B|Acc. DH, HV||PID|
|2023 [30]|Mono SHJ|One-cell, G/G|Acc. UV|Laminate discoloration||
|2024 [31]|Mono SHJ|One-cell, G/G|Acc. DH, voltage||PID|
|2024 [32]|Mono TOPCon|One-cell, unencap.|Acc. DH|R increase, localized recombination||
|2024 [33]|Mono PERC|8 half-cell,|Acc. DH|Localised regions with high||
||& Mono TOPCon|G/B|||R|
|2025 [34]|TOPCon|132-144 half-cell, G/G|Varied|TOPCon sensitivity to UV, static loading, and moisture||
|2025 [35]|Mono Al-BSF|36-cell, G/B|Field exposure|Reduced material aging in high altitudes||

*S*

*S*

## 2 Methods

The overarching workflow proposed in this study is shown in Figure1. The experimental workflow consists of the PV modules under investigation and the exposure-measurement cycle, where the modules alternate between character- ization through *I−V* and measurements and exposure to mechanical loading

using a LoadSpot system produced by BrightSpot Automation [16,17,36–39]. The computational workflow consists of the collection of the metadata and data, processing and feature extraction, and then fusion of the metadata, data, and features for analysis and modeling.

### 2.1 Experimental

Fifty c-Si modules were considered in this study, which come from several manufacturers. The modules all have between 60-96 cells and were produced with either aluminum back surface field (Al-BSF), passivated emitter and rear cell (PERC), or silicon heterojunction (SHJ) cells. Using a LoadSpot mechanical load tester, these modules were individually tested using standard IEC 61215 sequences (one cycle of 2,400 Pa, one cycle of 5,400 Pa, and 1,000 cycles of ±1,000Pa) and expanded sequences with *>*1,000 cycles of ±1,000Pa. Before, during, and after mechanical loading, the modules were character- ized using multi-irradiance illuminated *I–V*, Suns-*VOC*(open-circuit voltage), and EL imaging. For dynamic load testing, measurements were typically taken every 200 cycles and for static load testing, measurements were typi- cally taken at 200 Pa increments. Multi-irradiance illuminated *I–V*, Suns-*VOC* were obtained using a Sinton FMT-350 Flash Tester. Pseudo-*I-V* curves are obtained from Suns-*VOC*, showing device performance without the influence of series resistance (*RS*) [40]. An accurate *RS*is calculated by evaluating the voltage difference at the maximum power current (*IM P*). Important per- formance parameters (*i.e.*, *I−V* features) at STC are extracted from the equipment directly, including *PM P*, short-circuit current (*ISC*), open-circuit voltage (*VOC*), and fill factor (*F F*). EL images at nameplate *ISC*were obtained for all modules in this work. The modules used for mechanical load testing were imaged using a Nikon D5100 with a 950-nm longpass filter.

### 2.2 Data Collection and Management

Producing FAIR (findable, accessible, interoperable, reusable) data allows complex data science work to be performed, capturing key metrics and draw- ing new insights from historical data [41,42]. The computational workflow in this work utilizes a hybrid Python/SQLite system for data management, track- ing metadata, and data provenance throughout the experiment’s measurement sessions by printed bar code. At each stage of the study, all metadata were tracked and related to itself, capturing complex relationships between different study stages [43–45]. Central to this model is the unique module-id, relating back all charac- terization methods performed on a module to a single point. The PV module metadata contains the information referring the specfic make and model of the module, including the cell technology, number of busbars, interconnection scheme, packaging type, and nameplate performance parameters. Each mea- surement produced individual files that are tabular data or images of various

Fig. 1: Illustration of the experimental (*i.e.*, physical) and computational (*i.e.*, dig-

ital) workflow proposed in this study. There are four modules: 1) Experiment, 2) Data Collection, 3) Data Processing and Feature Extraction, and 4) Data Fusion, Analysis, and Modeling. The experimental workflow deals with using the PV mod- ules for measurements and collecting data at regular exposure intervals. At the data collection stage, *I−V* and EL data are collected, which are processed and features are extracted. In the data fusion, analysis, and modeling module, exploratory data analysis and data-driven modeling are done to extract more insights about semantic performance of PV modules.

formats. Each file is represented as an observation in dedicated tables, track- ing important metadata such as date, time, filename, etc. Additional tables for

the calculated *I−V* and EL results are outputs in addition to the *I−V* and EL metadata tables. Each table has all metadata in individual columns, with a filename column pointing to location of the raw data. These curated tables were joined based on date and time, capturing the stepwise measurements performed between *I−V* and EL characterizations.

### 2.3 Data Processing and Feature Extraction

### 2.3.1 I−V Curve Pre-Processing and Feature Extraction

Each *I −V* curve produced by the Sinton FMT-350 Flash Tester is a composite measurement of voltage, current, and temperature, over a set number of flashes. These curves are generated immediately before the corresponding EL image is taken. There are 400+ points of data per curve, equating to a flash of the sun. In this work, only the extracted *I−V* features are included in the final data tables for this workflow. Prior to use in a combined dataset, all of the columns are standardized and the data is cleaned. The measured columns are each important features that allow advanced methods to discover trends, as well as track the access to raw data as needed.

### 2.3.2 EL Image Pre-Processing

Segmentation models perform better with consistent and reliable training images. Each EL image is taken by a Nikon DSLR 5100, and any measurement artifacts that remain are corrected by our automated pre-processing pipeline. The first step is to do a minor perspective correction to align the module to a two dimensional plane. The remaining border is removed, and the module is cropped out of the image using the Pillow library’s automated crop and background removal feature. Each module is then gray-scaled for better edge detection. The cropped EL image of the module is then automatically split into cells based on the cell dimensions that are calculated by detecting how many rows and columns the module has.

### 2.3.3 EL Image Feature Extraction: Semantic Segmentation

Semantic segmentation is a computer vision technique that classifies every pixel into a meaningful category. After the module is split into cells, each individual cell is then fed into the semantic segmentation model developed by Fioresi *et al.* based on DeepLabv3 [7]. After training on 13,651 images, their model was able to achieve a score of at least 0.80 in every metric for the crack class making it an effective starting point for this work. The stability of each evaluation metric of the crack class justifies the selection of this model as the starting point for the computational workflow developed in this study, where a new dataset has been created, referred to from here on as EL-Defect-Evolution as it focuses on tracking the growth of crack defects over the course of a mechanical loading test. After the EL module images are converted to EL images of cells in the pre- processing stage, the semantic segmentation model performs inference on the

EL cell images to predict the class of each pixel. To facilitate visualization, a semitransparent mask is applied to each pixel of the EL cell image, color-coded to each class category. Red represents crack-related defects, blue represents contact-related defects, purple represents interconnect-related defects, and yel- low represents corrosion related defects. Due to the focus on mechanical loading and corresponding cell fracture in this dataset, only crack and contact defects were inspected in great detail in this study. For each EL cell image, the number of pixels featuring that defect (*N* *d* *i* ) and the total number of pixels in the image (*N* *total* ) can be determined. The fractional area of each defect category (*f* *d* *i* ) within a cell or a module can then be determined by the following ratio:

*d* *i* <u>N</u> *d* *i* *f* = *total* *,* (4) *N* Where the subscript *i* indicates that multiple defect classes can be present. *crack* <u>N</u> *crack* In this work, the focus is on *f* calculated from *Ntotal*.

### 2.3.4 EL Image Post-Processing

The EL images of cells are then stitched back together with the semitrans- parent masks, forming a EL module image with the appropriate cells in the appropriate locations. The module images are then downscaled to 4k resolu- tion for ease of use. This creates a complete module image that shows the entire panel with all defect categories represented by their distinctive color. Figure2shows an example of one module progressing through the mechani- cal load testing at different external pressure (*p* *ext* ) values. The fracture and resulting crack defects become increasingly more abundant and clear as *p* *e* *xt* increases. The other defects are also visible using the full 4k resolution images produced by this pipeline.

Fig. 2: Example of reconstructed EL images of a module with the semitranspar-

ent segmentation mask progressing through mechanical load testing and increasing external pressure (*p* *ext* ) values, from (a) 200 Pa to (f) 5,000 Pa.

### 2.3.5 EL Image Dataset Validation

Using the EL images with the semitransparent segmentation masks, a manual visual inspection was then performed on the EL-Defect-Evolution dataset used in this work. For the first iteration of prediction, the model showed signs of under-prediction for crack-related defects. An example of this can be seen in Figure3. To resolve this and optimize the model’s performance, a threshold sweep analysis was performed. The module was evaluated on the EL-Defect- Evolution dataset using every threshold value between 0 and 1 (exclusive) with an interval of 0.05 which can be seen in Figure4. Since this work is focused on crack-related defects, the ideal threshold value is 0.5 or 0.55, in line with the value of 0.54 used by Fioresi *et al.* previously [7].

Fig. 3: Visual example of the model under-predicting resistive vs. isolated crack-

related defects for the new EL-Defect-Evolution dataset used in this study.

Fig. 4: Evaluation metrics of the EL-Defect-Evolution dataset across all defect

categories as a function of threshold.

### 2.4 Data Fusion, Analysis, and Modeling

### 2.4.1 Characteristics of the Merged Data Frame

The original *I−V* features were extracted at the module level into a data frame, whereas the initial EL features were obtained for each individual cells and saved into another data frame. These two data frames were merged into one by 1) identifying and creating common columns for merging and 2) calcu- lating module-level EL features based on cell-level EL features. The cell-level specifications and the cell-level EL features were first merged based on the filename and cell number to obtain the cell-level EL data frame. The pixels corresponding to cracks across all cells in a module was stored (*SumCracks*). The *I − V* data frame was further processed by extracting measurement date, time, and pressure information from filenames and sample ID. Since the *I − V* features and area fraction of cracks would be used for subsequent data-driven modeling and analysis tasks, they were normalized. For *I −V* features, the nor- malization was based on dividing the values by the value at zero pressure. For obtaining normalized area fraction, *SumCracks* was divided by the total num- ber of pixels corresponding to any given module (*N ormCracks*). The merged data frame contains *I −V*, EL features, and design specifications at the module level.

### 2.4.2 Network Structural Equation Modeling

Network structural equation modeling (netSEM) is a statistical approach to understand how the response of a system is affected by an environmental stres- sor and other contributing factors [46]. The contributing factors are tracked using variables obtained from characterization methods and are therefore referred to as mechanistic variables. The response, stressor, and mechanistic variables are represented as features connected by linear and non-linear rela- tionships in a pathway diagram. A typical pathway diagram obtained from netSEM is illustrated in Figure5. netSEM has several non-linear relationships such as simple linear, quadratic, simple quadratic, change point, exponential, logarithmic, square root, inverse square root, and non-linearizable exponential. For each set of pairwise features, the best-fitting relationship among all linear and non-linear relationships is determined on the basis of the highest adjusted R² (*Radj* 2 ) value, which is referred to as the best functional form. In this study, netSEM v0.7.0 was utilized with an expanded set of non-linear relationships, such as square root and inverse square root. The focus of this work is to obtain the best functional forms for stressor (normalized pressure or *N ormP res*), mechanistic variable (normalized area fraction of cracks or *N ormCracks*), and response (normalized power or *N ormP mp*).

## 3 Results

### 3.1 Segmentation of Electroluminescence Images

The EL-Defect-Evolution dataset was created by running 1,855 EL images of modules having gone through the experimental workflow described in section 2.1. After carrying out the image processing steps in section 2.3, 1,000 random EL cell images were then extracted and annotated by experts from the total 111,300 segmented EL cell images. Each non-continuous defect in a cell counts as a single, unique annotation. These 1,000 random cell images created a total of 5,555 individual annotated defects used to measure the model’s performance using the standardized metric definitions below. TP and FP refer to true and false positive, TN and FN refer to true and false negatives, and IoU refers to intersection over union. These were created using global pixel-level averages as in [7].

<u>T P + T N</u> *Accuracy* =*,* (5) *T P* + *T N* + *F P* + *F N* <u>T P</u> *P recision* =*,* (6) *T P* + *F P* <u>T P</u> *Recall* =*,* (7) *T P* + *F N* <u>T P</u> *IoU* =*.* (8) *T P* + *F P* + *F N* After running the model using a threshold of 0.5 we found the results below: Tables2:

Table 2: Segmentation prediction results of the EL-Defect-Evolution dataset for

each defect class. The overall global accuracy is 0.930.

|Class|Precision|Recall|F1-Score|IoU|
|---|---|---|---|---|
|Crack|0.666|0.722|0.693|0.530|
|Contact|0.612|0.344|0.440|0.282|
|Interconnect|0.284|0.003|0.007|0.003|
|Corrosion|0.373|0.512|0.432|0.275|

The segmentation results demonstrate that the DeepLabv3-based model can effectively identify and localize crack-related defects across a significantly larger set of EL cell images. The initial tendency toward under-prediction, particularly for faint or discontinuous crack features, was mitigated through threshold tuning, which improved detection sensitivity while maintaining acceptable false positive rates. Importantly, these results confirm that this segmentation workflow produces reliable estimates of defect area fractions, supporting its use as a quantitative feature extraction step for further analysis in our greater netSEM model.

### 3.2 netSEM Results

Figure5shows the netSEM pathway diagram connecting stressor (blue), mech- anistic variables (yellow), and response (purple). Each pathway in the diagram is defined on the basis of best functional form and its corresponding *Radj* 2. In this figure, only the pathways having *Radj* 2 of greater than 0.7 are displayed to simplify the representation. The line width of each pathway varies on the basis of *Radj* 2.

Fig. 5: Network structural equation modeling (netSEM) pathway diagram connect-

ing the stressor, mechanistic variables, and response. Here, the stressor is normalized pressure (*N ormP res*) and response is normalized power (*N ormP mp*), whereas the mechanistic variables are normalized *I−V* features and normalized area fraction of cracks obtained (*N ormCracks*). Each pathway is defined by the best functional form and corresponding *Radj* 2.

### 3.3 Durability, Stability, and Resilience of Modules

In this subsection, the behavior of modules under the influence of stressor and how cracks influence power loss are illustrated using facet plots in which each individual panel displays the variation of data for a particular module. The module IDs are indicated on the top of each panel. In each of these facet plots, the best functional form for pairwise variables is represented by a dark blue line and the area under the curve is shaded using light blue color. The area under the fitted functional form enables comparison of module behavior despite having different best functional forms. The best functional form is indicated on the bottom-right corner of each panel. We display the facet plot for visualizing changes in durability, stability, and resilience. Figure6shows the variation of durability, stability, and resilience for mod- ules that have the best functional form with an *Radj* 2 of equal to or greater than

0.7. Through visual inspection of the facet plot, some of the modules have a significant drop in power due to applied pressure that translates to formation of cracks. For quantitative assessment and comparison of module behavior, we rely on areas under the curves.

Table3displays the quantitative values of durability, stability, and resilience of modules based on normalized areas under the fitted curves to enable comparison of performance. Figure7shows a visual representation of how durability, stability, and resilience compare across modules. A value closer to 1 in either of the category indicates best performance. Even small changes in either of the categories have a significant impact on the module performance, as observed in EL images and quantitative results. F1707-0011, F2405-0037, and FPCAL-0002 are the best-performing modules in terms of durability, stability, and resilience. On the other hand, F0000-0040 has lower values of durability, stability, and resilience, indicating that applied pressure caused cracks, which lead to power loss. In the case of F0000-0177, a slightly lower value of stabil- ity indicates that there are cracks formed due to applied pressure, but a high resilience value is because the formed cracks do not lead to power loss. The rest of the modules have a significant impact on power loss as a result of crack formation.

Table 3: Quantification of module durability, stability, and resilience. Abbreviations:

crystallinity (crystal.); technology (tech.); interconnection (inter.); busbar (BB).

|Module ID|Wafer Crystal.|Inter.|No. of|Durability Stability||Resilience|
|---|---|---|---|---|---|---|
||and Cell Tech.|Scheme|BBs||||
|FPCAL-0002|Mono SHJ|Ribbon|3|0.99|0.99|0.99|
|F2405-0037|Mono Al-BSF|Ribbon|4|0.99|0.99|0.99|
|F0000-0177|Multi Al-BSF|Ribbon|3|0.99|0.95|0.99|
|F1707-0011|Mono SHJ|Ribbon|3|0.99|0.99|0.99|
|F1707-0006|Mono PERC|Wire|12|0.99|0.99|0.99|
|F2405-0035|Mono Al-BSF|Ribbon|4|0.96|0.97|0.95|
|F2405-0030|Mono Al-BSF|Ribbon|4|0.96|0.98|0.94|
|F2405-0031|Mono Al-BSF|Ribbon|4|0.99|0.97|0.95|
|F2405-0034|Mono Al-BSF|Ribbon|4|0.95|0.97|0.93|
|F2405-0032|Mono Al-BSF|Ribbon|4|0.96|0.97|0.92|
|F2405-0036|Mono Al-BSF|Ribbon|4|0.93|0.96|0.91|
|F0000-0035|Multi Al-BSF|Ribbon|3|0.91|0.96|0.90|
|F0000-0040|Multi Al-BSF|Ribbon|4|0.76|0.88|0.79|

## 4 Discussion

### 4.1 FAIR Data

FAIR Data has gained a foothold within the scientific community for its value in creating high quality datasets. Fair is defined as “four foundational princi- ples—Findability, Accessibility, Interoperability, and Reusability—that serve to guide data producers and publishers” [41]. Data serves as a foundation of study for nearly every discipline, and in this specific study the data is tran- sitioned through more than six steps of processing to reach its final form in netSEM. Tracking and maintaining the data in reproducible, transparent, and usable ways promotes further insight and is good data stewardship. Difficulties remain with tracking all stages of a study protocol like this one and solutions are proposed that encompasses the entire life cycle of data [44].

Fig. 6: Variation of durability, stability, and resilience of modules based on changes

in pairwise variables. Each panel in the facet plot corresponds to individual module. The best functional form is fit to the data using the netSEM package and indicated at the bottom-right corner. The *Radj* 2 values of the best functional forms is greater than or equal to 0.7. The area under the curve in each panel is shown as shaded region (light blue).

### 4.2 Image Segmentation

A key challenge addressed in this study is the model’s sensitivity to defect visi- bility and contrast. Crack-related defects in EL images can vary significantly in appearance, ranging from well-defined, high-contrast fractures to faint, diffuse patterns that are difficult to distinguish from background noise. The observed under-prediction in early model outputs highlights this challenge and under- scores the importance of calibration. By performing a threshold sweep analysis, the model’s outputs were adjusted, improving overall performance. Another important contribution of this work lies in the scalability of our workflow. By automating every processing stage in this pipeline the model is able to process large volumes of EL data with minimal manual interven- tion. This consistency is essential for ensuring that model predictions are not influenced by variations in image acquisition conditions and will allow for the creation of even larger datasets than any previously used.

Fig. 7: Lollipop plot to compare durability, stability, and resilience across modules.

It is the visual representation of information in Table3.

Despite these strengths, the performance of the model remains dependent on the class distribution of the training data. Although the most abundant and relevant class for this study, cracks, perform reasonably well, the other classes are only able to perform well with extremely different threshold values. With- out a massive increase in uniformly diverse training data, category-specific calibration may be necessary for broader applications. The reliance on pixel- level classification also introduces sensitivity to noise and imaging artifacts, which must be carefully managed through pre-processing. From a broader perspective, the computational workflow developed in this work lays the foundation for more advanced, integrated analyses of PV module degradation. While the primary emphasis here is on accurately identifying and quantifying defects, the ability to generate consistent, high-quality features from EL images enables downstream modeling efforts that connect physical degradation to electrical performance. In this sense, the workflow we present serves as a critical intermediary step towards more advance reliability insights in PV modules.

### 4.3 Semantic Understanding of Performance Loss

From Figure6and Table3, F0000-0040 was seen to have lowest values of durability, stability, and resilience among all the modules. The cracks formed in F0000-0040 due to applied pressure contributes to increased power loss. To

better understand the module behavior, we correlate the power loss to the EL images at different applied pressures. Figure8shows that in F0000-0040, there are horizontal isolated electrical regions between the busbars even before any pressure is applied. As the pressure is progressively applied in small increments, the existing cracks open up widely, which are indicated by the dark isolated regions. In addition, at around 2,000 Pa, diagonal cracks form in cells located closer to the edges of the module and these deepen and branch out. As these diagonal cracks deepen and intersect the busbars and the existing horizontal isolated regions deepen beyond 2,600 Pa, the power loss shows a downward trend and then reaches a plateau.

Fig. 8: Normalized power as a function of the applied external pressure, i.e., *P* (*p*

*ext* ), for a single PV module (F0000-0040). The highlighted red regions represents locations specified as cracks, i.e., *f* *crack*.

To compare and contrast the behavior of F0000-0040 and other modules, Figure9features segmented EL images of modules in their final state with pro- gressively increasing stability going from left to right, going from F0000-0040 (Multi Al-BSF, 4 BB), F2405-0036 (Mono Al-BSF, 4 BB), F2405-0031 (Mono Al-BSF, 4 BB), F1707-0006 (Mono PERC, 12 BB), and F1707-0011 (Mono SHJ, 3BB). Notably, the more advanced cell and interconnect technologies ten to show higher stability than the older multi Al-BSF technologies. However, a larger study featuring a more comprehensive collection of modules would be needed to make more general conclusions about the role of design choices on the durability, stability, and resilience. Ultimately, this computational frame- work featuring semantically rich metadata and data enables such studies to

be performed on datasets already being collected during accelerated aging test by PV testing laboratories.

Fig. 9: Examples of the segmented EL images of modules in their final state with

progressively increasing stability going from left to right. The highlighted red regions indicating cracks, i.e., *f* *crack*, clearly increase moving from the F0000-0040 module on the far left and incrementally going to the right.

## 5 Conclusion Acknowledgements

This material is based upon work supported by the U.S. Department of Energy’s Office of Critical Minerals and Energy Innovation (CMEI) under award number DE-EE0009347. This material is also based on research at the Materials Data Science for Stockpile Stewardship Center of Excellence (MDS3- COE)and supported by the U.S. Department of Energy’s National Nuclear Security Administration under award number DE-NA0004104. This work made use of the High Performance Computing Resource in the Core Facility for Advanced Research Computing at Case Western Reserve Uni- versity. This work also used the Open Storage Network and Anvil at Purdue University through allocation MAT250039 from the Advanced Cyberinfras- tructure Coordination Ecosystem: Services & Support (ACCESS) program, which is supported by U.S. National Science Foundation grants #2138259, #2138286, #2138307, #2137603, and #2138296.

## References

[1]Peters, I.M., Hauch, J., Brabec, C., Sinha, P.: The value of stability in photovoltaics. Joule 5(12), 3137–3153 (2021).[https://doi.org/10.1016/j](https://doi.org/10.1016/j). joule.2021.10.019. Accessed 2025-11-05

[2]Deitsch, S., Buerhop-Lutz, C., Sovetkin, E., Steland, A., Maier, A., Gallwitz, F., Riess, C.: Segmentation of Photovoltaic Module Cells in Uncalibrated Electroluminescence Images. Machine Vision and Appli- cations 32(4), 84 (2021).[https://doi.org/10.1007/s00138-021-01191-9](https://doi.org/10.1007/s00138-021-01191-9). arXiv: 1806.06530. Accessed 2021-06-21

[3]Lin, H.-H., Dandage, H.K., Lin, K.-M., Lin, Y.-T., Chen, Y.-J.: Efficient Cell Segmentation from Electroluminescent Images of Single-Crystalline Silicon Photovoltaic Modules and Cell-Based Defect Identification Using Deep Learning with Pseudo-Colorization. Sensors 21(13), 4292 (2021). [https://doi.org/10.3390/s21134292](https://doi.org/10.3390/s21134292). Publisher: Multidisciplinary Digital Publishing Institute. Accessed 2025-11-05

[4]Otamendi, U., Martinez, I., Quartulli, M., Olaizola, I.G., Viles, E., Cam- barau, W.: Segmentation of cell-level anomalies in electroluminescence images of photovoltaic modules. Solar Energy 220, 914–926 (2021).https: //doi.org/10.1016/j.solener.2021.03.058. Accessed 2025-11-05

[5]Pratt, L., Govender, D., Klein, R.: Defect detection and quantification in electroluminescence images of solar PV modules using U-net semantic segmentation. Renewable Energy 178, 1211–1222 (2021).[https://doi.org/](https://doi.org/)

10.1016/j.renene.2021.06.086. Accessed 2025-11-05
[6]Sovetkin, E., Achterberg, E.J., Weber, T., Pieters, B.E.: Encoder–Decoder Semantic Segmentation Models for Electroluminescence Images of Thin- Film Photovoltaic Modules. IEEE Journal of Photovoltaics 11(2), 444– 452 (2021).[https://doi.org/10.1109/JPHOTOV.2020.3041240](https://doi.org/10.1109/JPHOTOV.2020.3041240). Accessed 2025-11-05

[7]Fioresi, J., Colvin, D.J., Frota, R., Gupta, R., Li, M., Seigneur, H.P., Vyas, S., Oliveira, S., Shah, M., Davis, K.O.: Automated Defect Detection and Localization in Photovoltaic Cells Using Semantic Segmentation of Electroluminescence Images. IEEE Journal of Photovoltaics 12(1), 53– 61 (2022).[https://doi.org/10.1109/JPHOTOV.2021.3131059](https://doi.org/10.1109/JPHOTOV.2021.3131059). Conference Name: IEEE Journal of Photovoltaics

[8]Chen, X., Karin, T., Jain, A.: Automated defect identification in electro- luminescence images of solar modules. Solar Energy 242, 20–29 (2022). [https://doi.org/10.1016/j.solener.2022.06.031](https://doi.org/10.1016/j.solener.2022.06.031). Accessed 2024-11-26

[9]Chen, X., Karin, T., Libby, C., Deceglie, M., Hacke, P., Silverman,

T.J., Jain, A.: Automatic Crack Segmentation and Feature Extraction in Electroluminescence Images of Solar Modules. IEEE Journal of Photo- voltaics 13(3), 334–342 (2023).[https://doi.org/10.1109/JPHOTOV.2023](https://doi.org/10.1109/JPHOTOV.2023). 3249970. Conference Name: IEEE Journal of Photovoltaics. Accessed 2024-11-26
[10]Eesaar, H., Joe, S., Rehman, M.U., Jang, Y., Chong, K.T.: SEiPV-Net: An Efficient Deep Learning Framework for Autonomous Multi-Defect Segmentation in Electroluminescence Images of Solar Photovoltaic Mod- ules. Energies 16(23), 7726 (2023).[https://doi.org/10.3390/en16237726](https://doi.org/10.3390/en16237726). Publisher: Multidisciplinary Digital Publishing Institute. Accessed 2025- 11-05

[11]Otamendi, U., Martinez, I., Olaizola, I.G., Quartulli, M.: A Scalable Framework for Annotating Photovoltaic Cell Defects in Electrolumi- nescence Images. IEEE Transactions on Industrial Informatics 19(9), 9361–9369 (2023).[https://doi.org/10.1109/TII.2022.3228680](https://doi.org/10.1109/TII.2022.3228680). Conference Name: IEEE Transactions on Industrial Informatics. Accessed 2024-10-30

[12]Xu, W., Shi, Y., Yang, R., Ye, B., Qiang, H.: Automatic Classification of Defective Solar Panels in Electroluminescence Images Based on Random Connection Network. Electronics 13(13), 2429 (2024).[https://doi.org/10](https://doi.org/10). 3390/electronics13132429. Accessed 2024-07-15

[13]Mahboob, Z., Khan, M.A., Lodhi, E., Nawaz, T., Khan, U.S.: Using SegFormer for Effective Semantic Cell Segmentation for Fault Detection in Photovoltaic Arrays. IEEE Journal of Photovoltaics 15(2), 320– 331 (2025).[https://doi.org/10.1109/JPHOTOV.2024.3450009](https://doi.org/10.1109/JPHOTOV.2024.3450009). Accessed 2025-11-05

[14]Zhou, Z., Jiang, J., Zhang, J.: Defective Electroluminescence Image Gen- eration for Data Imbalance in Solar Cell Defect Inspection. IEEE Journal of Photovoltaics, 1–7 (2025).[https://doi.org/10.1109/JPHOTOV.2025](https://doi.org/10.1109/JPHOTOV.2025). 3599613. Accessed 2025-09-15

### [15]IEC Technical Specification 60904-13 (2018)

[16]Schneller, E.J., Gabor, A.M., Lincoln, J., Janoch, R., Anselmo, A., Wal- ters, J., Seigneur, H.: Evaluating solar cell fracture as a function of module mechanical loading conditions. In: 2017 IEEE 44th Photovoltaic Specialist Conference (PVSC), pp. 2897–2901 (2017). IEEE

[17]Schneller, E.J., Frota, R., Gabor, A.M., Lincoln, J., Seigneur, H., Davis,

K.O.: Electroluminescence Based Metrics to Assess the Impact of Cracks on Photovoltaic Module Performance. In: 2018 IEEE 7th World Confer- ence on Photovoltaic Energy Conversion (WCPEC) (A Joint Conference of 45th IEEE PVSC, 28th PVSEC & 34th EU PVSEC), pp. 0455–0458.

IEEE, Waikoloa Village, HI (2018).[https://doi.org/10.1109/PVSC.2018](https://doi.org/10.1109/PVSC.2018). 8547636. [https://ieeexplore.ieee.org/document/8547636/](https://ieeexplore.ieee.org/document/8547636/) Accessed 2022- 01-17

[18]Seigneur, H., Lincoln, J., Schneller, E., Gabor, A.M.: Accelerating cyclic loading. In: 2018 IEEE 7th World Conference on Photovoltaic Energy Conversion (WCPEC)(A Joint Conference of 45th IEEE PVSC, 28th PVSEC & 34th EU PVSEC), pp. 1328–1332 (2018). IEEE

[19]Gabor, A.M., Schneller, E.J., Seigneur, H., Rowell, M.W., Colvin, D., Hopwood, M., Davis, K.O.: The impact of cracked solar cells on solar panel energy delivery. In: 2020 47th IEEE Photovoltaic Specialists Conference (PVSC), pp. 0810–0813 (2020). IEEE

[20]Golive, Y.R., Zachariah, S., Dubey, R., Chattopadhyay, S., Bhaduri, S., Singh, H.K., Bora, B., Kumar, S., Tripathi, A.K., Kottantharayil, A., Vasi, J., Shiradkar, N.: Analysis of Field Degradation Rates Observed in All-India Survey of Photovoltaic Module Reliability 2018. IEEE Jour- nal of Photovoltaics 10(2), 560–567 (2020).[https://doi.org/10.1109/](https://doi.org/10.1109/) JPHOTOV.2019.2954777. Number: 2 Conference Name: IEEE Journal of Photovoltaics

[21]Ino, Y., Asao, S., Shirasawa, K., Takato, H.: Investigation of Degradation Mode Spreading Interconnectors by Pressure-Cooker Testing of Photo- voltaic Cells. IEEE Journal of Photovoltaics 10(1), 188–196 (2020).https: //doi.org/10.1109/JPHOTOV.2019.2950079. Conference Name: IEEE Journal of Photovoltaics

[22]Semba, T.: Corrosion mechanism analysis of the front-side metallization of a crystalline silicon PV module by a high-temperature and high- humidity test. Japanese Journal of Applied Physics 59(5), 054001 (2020). [https://doi.org/10.35848/1347-4065/ab8274](https://doi.org/10.35848/1347-4065/ab8274). Number: 5 Publisher: IOP Publishing. Accessed 2020-07-02

[23]Karas, J., Michaelson, L., Munoz, K., Hossain, M.J., Schneller,

E., Davis, K.O., Bowden, S., Augusto, A.: Degradation of copper- plated silicon solar cells with damp heat stress. Progress in Photovoltaics: Research and Applications 28(11), 1175–1186 (2020).[https://doi.org/10.1002/pip.3331](https://doi.org/10.1002/pip.3331). Number: n/a eprint: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3331](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3331). Accessed 2020-08-20
[24]Curran, A.J., Wang, M., Whitaker, C.M., Moran, T., Huey, B.D., Dai, J., Jaubert, J.-N., Colvin, D., Iqbal, N., Davis, K.O., Bruck- man, L.S., Braid, J.L., French, R.H.: Degradation of Bifacial PERC and Al-BSF Cell Minimodules with White and Clear Encapsulant

Combinations in Modified Damp Heat. In: 2020 47th IEEE Pho- tovoltaic Specialists Conference (PVSC), pp. 2076–2082 (2020). [https://doi.org/10.1109/PVSC45281.2020.9300990](https://doi.org/10.1109/PVSC45281.2020.9300990). ISSN: 0160-

8371. [https://ieeexplore.ieee.org/abstract/document/9300990](https://ieeexplore.ieee.org/abstract/document/9300990) Accessed 2025-11-04
[25]Luo, W., Clement, C.E., Khoo, Y.S., Wang, Y., Khaing, A.M., Reindl, T., Kumar, A., Pravettoni, M.: Photovoltaic module failures after 10 years of operation in the tropics. Renewable Energy 177, 327–335 (2021).https: //doi.org/10.1016/j.renene.2021.05.145. Accessed 2025-10-07

[26]Ciesla, A., Kim, M., Wright, M., Zafirovska, I., Chen, D., Hallam, B., Chan, C.: A case study on accelerated light- and elevated temperature- induced degradation testing of commercial multi-crystalline silicon passi- vated emitter and rear cell modules. Progress in Photovoltaics: Research and Applications 29(11), 1202–1212 (2021).[https://doi.org/10.1002/pip](https://doi.org/10.1002/pip).

3455. eprint: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3455](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3455). Accessed 2025-11-04
[27]Kyranaki, N., Smith, A., Yendall, K., Hutt, D.A., Whalley, D.C., Gottschalg, R., Betts, T.R.: Damp-heat induced degradation in photovoltaic modules manufactured with passivated emitter and rear contact solar cells. Progress in Photovoltaics: Research and Applications 30(9), 1061–1071 (2022).[https://doi.org/10.1002/pip](https://doi.org/10.1002/pip).

3556. eprint: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3556](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3556). Accessed 2024-05-28
[28]Iqbal, N., Colvin, D.J., Schneller, E.J., Sakthivel, T.S., Ristau, R., Huey,

B.D., Yu, B.X.J., Jaubert, J.-N., Curran, A.J., Wang, M., Seal, S., French, R.H., Davis, K.O.: Characterization of front contact degradation in monocrystalline and multicrystalline silicon photovoltaic modules fol- lowing damp heat exposure. Solar Energy Materials and Solar Cells 235, 111468 (2022).[https://doi.org/10.1016/j.solmat.2021.111468](https://doi.org/10.1016/j.solmat.2021.111468). Accessed 2021-11-18
[29]Dhimish, M., Tyrrell, A.M.: Power loss and hotspot analysis for photovoltaic modules affected by potential induced degradation. npj Materials Degradation 6(1), 11 (2022).[https://doi.org/10.1038/](https://doi.org/10.1038/) s41529-022-00221-9. Publisher: Nature Publishing Group. Accessed 2025- 10-07

[30]Pinochet, N., Couderc, R., Therias, S.: Solar cell UV-induced degra- dation or module discolouration: Between the devil and the deep yellow sea. Progress in Photovoltaics: Research and Applications 31(11), 1091–1100 (2023).[https://doi.org/10.1002/pip.3725](https://doi.org/10.1002/pip.3725). eprint: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3725](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3725). Accessed 2025-10-07

[31]Arriaga Arruti, O., Gnocchi, L., Jeangros, Q., Ballif, C., Vir- tuani, A.: Potential-induced degradation in bifacial silicon heterojunction solar modules: Insights and mitigation strate- gies. Progress in Photovoltaics: Research and Applications 32(5), 304–316 (2024).[https://doi.org/10.1002/pip.3765](https://doi.org/10.1002/pip.3765). eprint: [https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3765](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pip.3765). Accessed 2025-11-04

[32]Wu, X., Wang, X., Yang, W., Nie, J., Yuan, J., Khan, M.U., Ciesla, A., Sen, C., Qiao, Z., Hoex, B.: Enhancing the reliability of TOPCon tech- nology by laser-enhanced contact firing. Solar Energy Materials and Solar Cells 271, 112846 (2024).[https://doi.org/10.1016/j.solmat.2024.112846](https://doi.org/10.1016/j.solmat.2024.112846). Accessed 2025-09-08

[33]Sen, C., Wang, H., Khan, M.U., Fu, J., Wu, X., Wang, X., Hoex, B.: Buyer aware: Three new failure modes in TOPCon modules absent from PERC technology. Solar Energy Materials and Solar Cells 272, 112877 (2024). [https://doi.org/10.1016/j.solmat.2024.112877](https://doi.org/10.1016/j.solmat.2024.112877). Accessed 2024-05-28

[34]Gebhardt, P., Marletti, S., Markert, J., Kr¨aling, U., Tu, M., Haedrich, I., Philipp, D.: Comparison of Commercial TOPCon PV Modules in Accel- erated Aging Tests. IEEE Journal of Photovoltaics 15(1), 24–29 (2025). [https://doi.org/10.1109/JPHOTOV.2024.3483317](https://doi.org/10.1109/JPHOTOV.2024.3483317). Accessed 2025-11-04

[35] Ozkalay, E., Quest, H., Gassner, A., Virtuani, A., Eder, G.C., Vorstof-¨ fel, S., Buerhop-Lutz, C., Friesen, G., Ballif, C., Burri, M., Bucher, C.: Three decades, three climates: environmental and material impacts on the long-term reliability of photovoltaic modules. EES Solar, 10–1039400040 (2025).[https://doi.org/10.1039/D4EL00040D](https://doi.org/10.1039/D4EL00040D). Accessed 2025-06-02

[36]Smith, R.M., Colvin, D.J.: V10: Fixed dark bias current as a photovoltaic module damage assessment metric. Solar Energy 288, 113271 (2025). [https://doi.org/10.1016/j.solener.2025.113271](https://doi.org/10.1016/j.solener.2025.113271)

[37]Seigneur, H., Schneller, E., Lincoln, J., Gabor, A.M.: Cyclic mechan- ical loading of solar panels – a field experiment. In: 2018 IEEE 7th World Conference on Photovoltaic Energy Conversion (WCPEC) (A Joint Conference of 45th IEEE PVSC, 28th PVSEC 34th EU PVSEC), pp. 3810–3814 (2018).[https://doi.org/10.1109/PVSC.2018.8548153](https://doi.org/10.1109/PVSC.2018.8548153)

[38]Lincoln, J.L., Gabor, A.M., Schneller, E.J., Seigneur, H., Walters, J., Janoch, R., Anselmo, A., Huayamave, V., Schoenfeld, W.: Forecasting environmental degradation power loss in solar panels with a predictive crack opening test. In: 2017 IEEE 44th Photovoltaic Specialist Confer- ence (PVSC), pp. 2839–2843 (2017).[https://doi.org/10.1109/PVSC.2017](https://doi.org/10.1109/PVSC.2017). 8366573

[39]Seigneur, H., Gabor, A.M., Schneller, E., Lincoln, J.: Electroluminescence- testing induced crack closure in pv modules. In: 2019 IEEE 46th Pho- tovoltaic Specialists Conference (PVSC), pp. 2252–2258 (2019).https: //doi.org/10.1109/PVSC40753.2019.8981398

[40]Sinton, R.A., Cuevas, A.: A Quasi-Steady-State Open-Circuit Voltage Method for Solar Cell Characterization. In: 16th European Photovoltaic Solar Energy Conference, Glasgow, Scotland, pp. 1152–1155 (2000)

[41]Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J., Appleton, G., Axton,

M., Baak, A., Blomberg, N., Boiten, J.-W., Da Silva Santos, L.B., Bourne,
P.E., Bouwman, J., Brookes, A.J., Clark, T., Crosas, M., Dillo, I., Dumon,
O., Edmunds, S., Evelo, C.T., Finkers, R., Gonzalez-Beltran, A., Gray,
A.J.G., Groth, P., Goble, C., Grethe, J.S., Heringa, J., ’T Hoen, P.A.C., Hooft, R., Kuhn, T., Kok, R., Kok, J., Lusher, S.J., Martone, M.E., Mons,
A., Packer, A.L., Persson, B., Rocca-Serra, P., Roos, M., Van Schaik, R., Sansone, S.-A., Schultes, E., Sengstag, T., Slater, T., Strawn, G., Swertz,
M.A., Thompson, M., Van Der Lei, J., Van Mulligen, E., Velterop, J., Waagmeester, A., Wittenburg, P., Wolstencroft, K., Zhao, J., Mons, B.: The FAIR guiding principles for scientific data management and stew- ardship 3(1), 160018.[https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18). Accessed 2025-12-11
[42]Nihar, A., Curran, A.J., Karimi, A.M., Braid, J.L., Bruckman, L.S., Koyut¨urk, M., Wu, Y., French, R.H.: Toward findable, accessible, interop- erable and reusable (fair) photovoltaic system time series data. 2021 IEEE 48th Photovoltaic Specialists Conference (PVSC), 1701–1706 (2021)

[43]Rajamohan, B.P., Bradley, A.C.H., Tran, V.D., Gordon, J.E., Caldwell,

H.W., Mehdi, R., Ponon, G., Tran, Q.D., Dernek, O., Kaltenbaugh, J., *et* *al.*: Materials data science ontology (mds-onto): Unifying domain knowl- edge in materials and applied data science. Scientific Data 12(1), 628 (2025)
[44]Yao, A.D., Tran, V.D., Caldwell, H.W., Dernek, O., Thompson, B., Luu, V.-K., Alyasiri, A., Tran, Q.D., Li, M., Davis, K.O., Bruckman,

L.S., Wu, Y., French, R.H., Barcelos, E.I.: A reasoning framework for knowledge learning in photovoltaics degradation science studies. In: 2025 IEEE 53rd Photovoltaic Specialists Conference (PVSC), pp. 1050–
1052. IEEE.[https://doi.org/10.1109/PVSC59419.2025.11133115.https:](https://doi.org/10.1109/PVSC59419.2025.11133115.https:) //ieeexplore.ieee.org/document/11133115/Accessed 2025-12-11
[45]Tran, Q.D., Barcelos, E.I., Bruckman, L.S.: Designing data-centric study protocols guided by fair principles. Interdisciplinary Information Sciences 31(1), 75–82 (2025)

[46]Bruckman, L.S., Wheeler, N.R., Ma, J., Wang, E., Wang, C.K., Chou,

I., Sun, J., French, R.H.: Statistical and Domain Analytics Applied to PV Module Lifetime and Degradation Science. IEEE Access 1, 384–403 (2013).[https://doi.org/10.1109/ACCESS.2013.2267611](https://doi.org/10.1109/ACCESS.2013.2267611). Accessed 2026- 05-13
