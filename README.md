<!-- <img alt="" src='' height="600px" width="1000px" align='center'> -->

# Fraud Case Study

![badge](https://img.shields.io/badge/last%20modified-may%20%202020-success)
![badge](https://img.shields.io/badge/status-in%20progress-yellow)

|Team Shut the FRAUD Down!!|
|---|
[Tyler Woods](https://github.com/tylerjwoods)  | 
|[Cindy Wong](https://github.com/cwong690) |
|[Ben Weintraub](https://github.com/b-weintraub)|


## Overview

This is a Flask based web app that streams events and automatically detects fraudulent events. 

Due to privacy, the data and website are not available but the pickled model and code is.

## Data Preparation

### EDA

Fraudelent categories

   Channels vs Fraud       |  Delivery Method vs Fraud |     Gross Profits vs Fraud
:-------------------------:|:-------------------------:|:-------------------------:
![](images/channels_eda.png) |   ![](images/delivery_method_eda.png)|    ![gross profits](images/gross_profits_dummie.png)

   FB Published vs Fraud   |  Ticket Length vs Fraud   |     User Type vs Fraud
:-------------------------:|:-------------------------:|:-------------------------:
![](images/fb_published.png)|   ![](images/ticket_type_length.png)|    ![gross profits](images/user_type.png)

   Sale Duration vs Fraud  |  Gmail vs Fraud           |     Previous Payout vs Fraud
:-------------------------:|:-------------------------:|:-------------------------:
![](images/sale_duration2.png)|   ![](images/gmail_account_eda.png)|    ![gross profits](images/previous_payouts_eda.png)



## Models


<img src="https://github.com/tylerjwoods/shut_the_fraud_down/blob/master/images/ROC_curves.jpeg" width="400" height="400" title="ROC Curve" />




## Future Work

- [ ] KNN
- [ ] Better Model
- [ ] Clean up files