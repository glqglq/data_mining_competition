## 4-26

- [glqglqglq2]放入除了instance_id、user_id、context_id、item_category_list、item_property_list、context_timestamp、predict_category_property以外的特征；再加入item_category_sub、context_hour、context_weekday-0.0268-0.16
  - id_features = ["item_brand_id", "item_city_id", "item_id", "shop_id", **"item_category_sub"**]
  - cat_features = ["user_gender_id", "user_occupation_id", "context_hour", "context_weekday"]
  - con_features = ["item_collected_level", "item_price_level", "item_pv_level", "item_sales_level", "shop_review_num_level","shop_review_positive_rate", "shop_score_delivery", "shop_score_description", "shop_score_service","shop_star_level", "user_age_level", "user_star_level", "context_page_id"]



## 4-27

- 加入catFeat.csv-？-0.14832

## 4-28

## 4-29

- [glqglqglq2]6号：0.03089-0.14875
- [兄贵要过年]7号上午后面1/5：0.169217-0.14927
- [post5862]6号+7号上午：0.09412-0.17159 
- [小帅哥]6号下午+7号上午：0.102727-0.17456
- 7号上午n折cv：



## 4-30

- [兄贵要过年]6号验证+加入word embedding、jaccard+xgb：？-0.14827
- [小帅哥]6号验证+加入jaccard+xgb：0.030932-0.14841
- [post5862]6号验证+加入jaccard+lbg：0.0383225-0.14763
- **[glqglqglq2]6号验证+加入word embedding、jaccard+lbg：0.0385504-0.14782**


## 5-1

- 6号验证、其余训练
  - [Baseline]lgb：0.0384551-
  - []加入jaccard+lbg：0.0383225-0.14763
  - **[]加入embedding+lbg：0.0385107**
  - **[]加入word embedding、jaccard+lbg：0.0385504-0.14782**
  - **[]加入word embedding、jaccard、browse-count：0.039007**
  - **[]加入word embedding、jaccard、buy-count：0.0385769**
  - **[]加入word embedding、jaccard、ratio：0.039714-**
  - **[1-post5862]加入word embedding、jaccard、browse-count、buy-count、ratio：0.0396044-0.14731**
  - **[2-glqglqglq2]加入word embedding、jaccard、browse-count、buy-count、ratio、比例：0.0397299-0.14754**





- 丢去7号、6号验证
  - [Baseline]lgb：0.0310285
  - **[]加入jaccard+lbg：0.0311298**
  - **[]加入embedding+lbg：0.0311327**
  - [Baseline]加入word embedding、jaccard+lbg：0.0309669
  - []加入word embedding、jaccard、browse-count+lbg：0.0308668
  - []加入word embedding、jaccard、buy-count+lbg：0.0306849
  - []加入word embedding、jaccard、ratio+lbg： 0.0304467
  - **[3-兄贵要过年]加入word embedding、jaccard、browse-count、buy-count、ratio+lbg：0.0305134-0.18154**
  - **[4-小帅哥]加入word embedding、jaccard、browse-count、buy-count、ratio+lbg、比例：0.0305264-0.18007**





- 7号1/5验证

  - [Baseline]lgb：0.169365
  - **[]加入jaccard+lbg：0.169477**
  - []加入embedding+lbg：0.169258
  - [Baseline]加入word embedding、jaccard+lbg：0.169271
  - []加入word embedding、jaccard、browse-count：0.168718
  - []加入word embedding、jaccard、buy-count：0.168723
  - []加入word embedding、jaccard、ratio：0.16851
  - []加入word embedding、jaccard、browse-count、buy-count、ratio：0.168236
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、比例：0.168145

## 5-2

- 6号验证：
  - [Baseline]lgb：0.0384551-
  - []加入jaccard+lbg：0.0383225-0.14763
  - **[]加入embedding+lbg：0.0385107**
  - **[]加入word embedding、jaccard+lbg：0.0385504-0.14782**
  - **[]加入word embedding、jaccard、browse-count：0.039007**
  - **[]加入word embedding、jaccard、buy-count：0.0385769**
  - **[]加入word embedding、jaccard、ratio：0.039714-**
  - **[1-post5862]加入word embedding、jaccard、browse-count、buy-count、ratio：0.0396044-0.14731**
  - **[2-glqglqglq2]加入word embedding、jaccard、browse-count、buy-count、ratio、比例：0.0397299-0.14754**
  - [1-glqglqglq2]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat：0.039946-0.14699 
  - **[2-post5862]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayItemClickCountFeat：0.0398032- 0.15842**  
  - **[3-小帅哥]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat：0.0409946-0.14822**
  - [4-兄贵要过年]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、浩彬：0.0408191-0.14688



- 丢弃7号，6号验证，其余训练
  - [Baseline]lgb：0.0310285
  - []加入jaccard+lbg：0.0311298-0.14763
  - []加入embedding+lbg：0.0311327
  - [Baseline]加入word embedding、jaccard+lbg：0.0309669-0.14782
  - []加入word embedding、jaccard、browse-count+lbg：0.0308668
  - []加入word embedding、jaccard、buy-count+lbg：0.0306849
  - []加入word embedding、jaccard、ratio+lbg： 0.0304467
  - [3-兄贵要过年]加入word embedding、jaccard、browse-count、buy-count、ratio+lbg：0.0305134-0.14731
  - **[4-小帅哥]加入word embedding、jaccard、browse-count、buy-count、ratio+lbg、比例：0.0305264-0.14754**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat：0.0304193-0.14699
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayItemClickCountFeat：0.03058- 0.15842
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat：0.0303799-0.14822**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、浩彬：0.0304019-0.14688
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600：0.0304049



- 7号1/5验证
  - [Baseline]lgb：0.169365
  - **[]加入jaccard+lbg：0.169477**
  - []加入embedding+lbg：0.169258
  - [Baseline]加入word embedding、jaccard+lbg：0.169271
  - []加入word embedding、jaccard、browse-count：0.168718
  - []加入word embedding、jaccard、buy-count：0.168723
  - []加入word embedding、jaccard、ratio：0.16851
  - []加入word embedding、jaccard、browse-count、buy-count、ratio：0.168236
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、比例：0.168145
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat：0.168149
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayItemClickCountFeat：0.168212**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat：0.16813
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、浩彬：0.168231**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600：0.167544
  - 



- 6号+7号1/5验证：
  - [Baseline]lgb：0.0451686
  - []加入jaccard+lbg：0.045071
  - **[]加入embedding+lbg：0.0451814**
  - **[]加入word embedding、jaccard+lbg：0.045105**
  - **[]加入word embedding、jaccard、browse-count：0.0451313**
  - []加入word embedding、jaccard、buy-count：0.0448541
  - []加入word embedding、jaccard、ratio：0.0447092
  - []加入word embedding、jaccard、browse-count、buy-count、ratio：0.0446625
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、比例：0.0446775**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat：0.0446313
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayItemClickCountFeat：0.0446678**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat：0.0445726
  - **[]加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、浩彬：0.0445949**
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600：0.0445564
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today：0.0437716
  - []加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour：0.043681
  - 加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last：0.0435304
  - **加入word embedding、jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、hour_browse_is_last：0.0436032**





- 线上
  - []加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat：0.0447893
  - [1-小帅哥]加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat+换参数：0.0445504-0.14658
  - **[2-兄贵要过年]加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、浩彬：0.0447974-0.14841** 
  - [3-post5862]加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last：0.0434247-0.14699
  - **[4-glqglqglq2]加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last：0.0434408-0.14570**
  - **[4-glqglqglq2]加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last：0.0435517**

# 5-5

- []所有特征：0.0435421
- **除去simple_uesful_features.csv（浩彬）： 0.0436317**
- [1]除去proportion：0.0434196
- [2]除去proportion、embedding-similarity：0.0434075
- **[3]除去proportion、embedding-similarity、shiftDayItemClickCountFeat.csv：0.0434481**
- **[4]除去proportion、embedding-similarity、browse_count_today：0.0436612**

# 5-6

- [Baseline]6号、7号1/5验证 + 加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last：0.0434408-0.14570
- **[Baseline]6号、7号1/5验证 + 加入last_browse_time_interval：0.0435123**
- **[Baseline]6号、7号1/5验证 + 加入shiftDayItemClickCountFeat.csv：0.0436525**
- [Baseline]6号、7号1/5验证 + 加入simple_uesful_features.csv：0.0433591
- **[Baseline]6号、7号1/5验证 + 加入last_browse_time_interval、simple_uesful_features.csv：0.0434481**
- **[Baseline]+加入simple_uesful_features.csv、删除browse_count_7_division：0.0434066**
- **[Baseline]+加入simple_uesful_features.csv、删除buy_count_7_division：0.0436009**
- 



- 线上：
  - [1-post5862]0-5号+7号4/5训练，6号+7号1/5验证：0.0432235-
  - [2-glqglqglq2]7号上午11点验证：0.162338-0.14754
  - [3-小帅哥]7号4/5训练，7号1/5验证：0.163133-0.14936

# 5-7

- [1-兄贵]：0.0432235-0.1459
  - 划分：0-5号+7号4/5训练，6号+7号1/5验证
  - 特征：
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard、last_browse_time_interval
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [2-小帅哥]：0.0431538-0.1461（logloss降）
  - 划分：**0-5号+7号4/5训练，6号+7号1/5验证**
  - 特征：**比1删除了last_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [3-]：0.162567（logloss升）
  - 划分：**7号11点验证**
  - 特征：**比1删除了last_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [4-]：0.163219（logloss升）
  - 划分：**7号4/5训练、7号1/5验证**
  - 特征：**比1删除了last_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [5-post5862]：0.0433051（logloss升）-0.1458 
  - 划分：**0-5号+7号4/5训练，6号+7号1/5验证**
  - 特征：**比1增加了next_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard、last_browse_time_interval、next_browse_time_interval
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [6-]：0.162443（logloss升）
  - 划分：**7号11点验证**
  - 特征：**比1增加了next_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard、last_browse_time_interval、next_browse_time_interval
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat
- [7-]：0.163046（logloss降）
  - 划分：**7号4/5训练、7号1/5验证**
  - 特征：**比1增加了next_browse_time_interval**
    - 我的：browse_count_7_division、buy_count_7_division、ratio_7、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、property-jaccard
    - 浩彬：simple_uesful_features.csv、time_gap_next：
    - 冲哥：shiftDayShopClickCountFeat

# 5-9

- 最好：加入jaccard、browse-count、buy-count、ratio、catFeat、shiftDayShopClickCountFeat、browse_count_hour_ago_3600、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last：0.0434408-0.163587-0.164534-0.14570（1）
- 最好+删除hour_browse_is_last：0.0434247-0.163529-**0.164664**-？
- 最好+删除day_browse_is_last：0.0434133-**0.164099**-**0.164707-？**
- 最好+加入browse_count_hour_ago_900、browse_count_hour_ago_1800：0.0434381-**0.163595**-0.164386-0.14583-不好，暂时不加
- 最好+加入last_browse_time_interval：-0.163154-
- 最好+加入last_browse_time_interval、next_browse_time_interval：-0.162298-
- **最好+加入last_browse_time_interval、next_browse_time_interval、shiftDayItemClickCountFeat.csv：0.162505**
- 最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv：0.162237
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、preDayClickCountFeat.csv：0.162405**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、shopFeat.csv：0.162348**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、singleCvrFeat.csv：0.162328**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、timeFeat.csv：0.162361**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、userDayClickRankFeat.csv：0.162414**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、浩彬simple feature：0.162437**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、browse_count_hour_ago_900、browse_count_hour_ago_1800：0.162399**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、browse_count_hour_ago_900：0.16237 **
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、browse_count_hour_ago_1800：0.162354**
- **最好+加入last_browse_time_interval、next_browse_time_interval、clickTradeRatioFeat.csv、删除browse_count_hour_ago_3600：0.162377**
- 最好+加入clickTradeRatioFeat.csv：0.163433
- **最好+加入clickTradeRatioFeat.csv、preDayClickCountFeat.csv：0.163581**
- **最好+加入clickTradeRatioFeat.csv、shopFeat.csv：0.163521**
- **最好+加入clickTradeRatioFeat.csv、singleCvrFeat.csv：0.163524**
- **最好+加入clickTradeRatioFeat.csv、timeFeat.csv：0.163455**
- 最好+加入clickTradeRatioFeat.csv、userDayClickRankFeat.csv：0.163283
- **最好+加入clickTradeRatioFeat.csv、simple_uesful_features.csv：0.163542**



# 5-11

- [1-]初始特征0.0679913
- **[2-]加入browse_count_7、buy_count_7：0.0680773**
- **[3-]加入ratio-7：0.0680052**
- [4-]加入browse_count_7、buy_count_7、ratio-7：0.0680275
- [5-]加入browse_count_7、buy_count_7、ratio-7、**browse_count_today、browse_count_tohour**：0.0679847
- [6-]加入browse_count_7、buy_count_7、ratio-7、browse_count_today、browse_count_tohour、**day_browse_is_last、hour_browse_is_last**：0.0679908
- **[7-]加入browse_count_7、buy_count_7、ratio-7、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、browse_count_hour_ago_3600、browse_count_hour_ago_1800、browse_count_hour_ago_900：0.0680326**
- [8-]加入browse_count_7、buy_count_7、ratio-7、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、browse_count_hour_ago_3600、browse_count_hour_ago_1800、browse_count_hour_ago_900、**next_browse_time_interval、last_browse_time_interval**：0.0680104
- **[9-]加入browse_count_7、buy_count_7、ratio-7、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、browse_count_hour_ago_3600、browse_count_hour_ago_1800、browse_count_hour_ago_900、next_browse_time_interval、last_browse_time_interval、property-jaccard：0.0680399**
- [10-]加入browse_count_7、buy_count_7、ratio-7、browse_count_today、browse_count_tohour、day_browse_is_last、hour_browse_is_last、last_browse_time_interval、next_browse_time_interval：0.0680104-0.168442