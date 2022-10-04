### Literature Review Document
https://docs.google.com/document/d/1hNrWtPQ8_Mc9PpwksHeYbJL3kSzEJLRHBUIHqADImRU/edit#heading=h.dl1m4p2l72yf

--------------------------------------
### Problem Definition Related:

 #### GPI Definition/Equation (or Lanfall TCs Count)
 - https://agupubs.onlinelibrary.wiley.com/doi/full/10.3894/JAMES.2010.2.1 （EGPI Definition, Emanuel, 2010) 
 - https://texmex.mit.edu/pub/emanuel/PAPERS/em_nolan_extended_2004.pdf (ENGPI Definition, Emanuel & Nolan, 2004)
 - https://www.pnas.org/doi/10.1073/pnas.1301293110
 - https://texmex.mit.edu/pub/emanuel/PAPERS/bisteremanuel98.pdf (potential intensity)
 - https://www.nature.com/articles/s43247-022-00410-z#Equ3 (DGPI)

 - 
 
 #### Notes
 - absolute vorticity of the 850 hPa flow
 - potential intensity
 - magnitude of the 850 hPa–250 hPa wind shear
 - saturation moist static energy of the free troposphere
 - representative value of the actual moist static energy of the middle troposphere
 - saturation moist static energy of the sea surface
 - Code for GPI Calculation and Processing: https://doi.org/10.7910/DVN/PDJ34K
 
 

--------------------------------------
### General Approach Related:
- DL using simulated data: https://ibm.enterprise.slack.com/files/U0419SXRD4H/F0418KJ2P6E/seasonal_precipitation_prediction.pdf?origin_team=T0D0Z6X2N&origin_channel=C040X85F2SE
- Study suggesting using ENSO for TC genesis prediction: https://journals.ametsoc.org/view/journals/clim/33/24/jcliD200255.xml
- Converting data into representative index like GPI: https://doi.org/10.1175/WAF-D-15-0062.1
- Transfer Learning: https://doi.org/10.1007/s13351-022-1174-7

--------------------------------------
### Databases/Features Related:
 #### Reanalysis Data
 - ORAS5: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-oras5?tab=overview
 - SODA
 - ERA5 (server currently down): https://confluence.ecmwf.int/display/CKB/The+family+of+ERA5+datasets#
 - MERRA: https://gmao.gsfc.nasa.gov/reanalysis/MERRA/

 #### Simulated Data
 - CESM: https://www.cesm.ucar.edu/experiments/cesm1.0/#20thc
 - CMIP6: https://esgf-node.llnl.gov/projects/cmip6/
 - CMIP6 + Reanalysis (SSH): https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-water-level-change-timeseries-cmip6?tab=overview
 - NMME: https://www.cpc.ncep.noaa.gov/products/NMME/

 #### Other Features (not sure which data type above it belongs to)
 - Southern Oscillation Index: https://www.ncei.noaa.gov/access/monitoring/enso/soi
 - Nino Index: https://www.ncei.noaa.gov/access/monitoring/enso/sst
 - QBO: https://climatedataguide.ucar.edu/climate-data/qbo-quasi-biennial-oscillation
 
 #### TC Count
 - IBTrACS: https://www.ncei.noaa.gov/products/international-best-track-archive?name=introduction
--------------------------------------
### Model Architecture Related:

 #### Baseline SVR
 - https://doi.org/10.1016/j.procs.2012.09.069

 #### Proposed CNN
 - https://iopscience-iop-org.ezaccess.libraries.psu.edu/article/10.1088/1741-2552/aace8c
 
 #### Other Models
 - ANN: https://doi.org/10.1007/s00703-016-0446-0
--------------------------------------
### Model Explainability Related:

 #### SVR Related
 
 #### CNN Related
 
--------------------------------------
### Others
